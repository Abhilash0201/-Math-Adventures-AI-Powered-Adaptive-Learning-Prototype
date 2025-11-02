import streamlit as st
from puzzle_generator import gen_problem
from tracker import Tracker
from adaptive_engine import AdaptiveEngine, LEVELS
import time
import numpy as np
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title='Math Adventures', layout='centered')
st.title('Math Adventures — Adaptive Math Practice')

if 'tracker' not in st.session_state:
    st.session_state['tracker'] = Tracker()
if 'current_level' not in st.session_state:
    st.session_state['current_level'] = 'Easy'
if 'name' not in st.session_state:
    st.session_state['name'] = ''
if 'engine' not in st.session_state:
    st.session_state['engine'] = None
if 'last_question' not in st.session_state:
    st.session_state['last_question'] = None
if 'ml_model' not in st.session_state:
    st.session_state['ml_model'] = None
if 'recent_attempts' not in st.session_state:
    st.session_state['recent_attempts'] = []

with st.sidebar:
    st.header('Session Settings')
    name = st.text_input('Your name', st.session_state['name'])
    st.session_state['name'] = name
    init_level = st.selectbox('Initial difficulty', LEVELS, index=0)
    use_ml = st.checkbox('Use ML adaptive engine (optional)', False)
    if st.button('Reset Session'):
        for k in ['tracker','current_level','last_question','recent_attempts','ml_model']:
            if k in st.session_state:
                del st.session_state[k]
        st.rerun()

if st.session_state.get('engine') is None:
    mode = 'ml' if use_ml else 'rule'
    st.session_state['engine'] = AdaptiveEngine(mode=mode)

if use_ml and st.session_state.get('ml_model') is None:
    st.info('Training tiny synthetic ML model for demonstration...')
    X=[]; y=[]; rng=np.random.RandomState(42)
    for _ in range(400):
        lvl=rng.randint(0,3); acc=rng.rand(); avg_t=rng.rand()*15
        if acc>0.75 and avg_t<(8+lvl*2): label=1
        elif acc<0.45 or avg_t>(20-lvl*2): label=-1
        else: label=0
        X.append([lvl,acc,avg_t]); y.append(label)
    model=LogisticRegression(multi_class='multinomial',solver='lbfgs',max_iter=300)
    model.fit(X,y)
    st.session_state['ml_model']=model
    st.session_state['engine'].set_model(model)
    st.success('ML model trained (demo).')

col1, col2 = st.columns([3,1])
with col1:
    st.subheader(f"Player: {st.session_state.get('name','(no name)')}")
    st.write(f"Current difficulty: **{st.session_state.get('current_level','Easy')}**")
    if st.button('Generate Next Puzzle', key='gen'):
        lvl = init_level if len(st.session_state['recent_attempts'])==0 else st.session_state['current_level']
        q,a,meta = gen_problem(lvl)
        st.session_state['last_question'] = {'q':q,'a':a,'time':time.time(),'difficulty':lvl}
        st.session_state['question_display'] = q
        st.session_state['feedback'] = None

with col2:
    st.write('Tips')
    st.write('- Try to answer quickly and accurately.')

if st.session_state.get('last_question') is not None:
    qd = st.session_state['last_question']
    st.markdown('---')
    st.subheader('Current Puzzle')
    st.write(f"**{qd['q']}** (Difficulty: {qd['difficulty']})")
    ans = st.text_input('Your answer', key='ans_input')
    if st.button('Submit Answer'):
        try:
            resp_time = time.time() - qd['time']
            val = float(ans) if ans else 0
            correct = abs(val - float(qd['a'])) < 1e-6
            st.session_state['tracker'].log(qd['q'], correct, resp_time, qd['difficulty'])
            st.session_state['recent_attempts'].append({'correct': correct, 'response_time': resp_time})
            next_lvl, reason = st.session_state['engine'].decide_next(st.session_state['current_level'], st.session_state['recent_attempts'])
            st.session_state['current_level'] = next_lvl
            st.session_state['feedback'] = {'correct':correct, 'resp_time':resp_time, 'reason':reason}
            del st.session_state['last_question']
            st.rerun()
        except Exception as e:
            st.error('Error while submitting answer: ' + str(e))

if st.session_state.get('feedback') is not None:
    fb = st.session_state['feedback']
    if fb['correct']:
        st.success(f"Correct! Response time: {fb['resp_time']:.2f}s — {fb['reason']}")
    else:
        st.error(f"Incorrect. Response time: {fb['resp_time']:.2f}s — {fb['reason']}")

st.markdown('---')
st.header('Session Summary')
if st.button('Show Summary'):
    s = st.session_state['tracker'].summary()
    if not s:
        st.info('No attempts yet.')
    else:
        st.write(f"Total attempts: {s['total']} — Accuracy: {s['accuracy']:.2f}")
        st.write(f"Average response time: {s['avg_time']:.2f}s")
        for k,v in s['by_level'].items():
            st.write(f"- {k}: count={v['count']}, accuracy={v['accuracy']:.2f}")
