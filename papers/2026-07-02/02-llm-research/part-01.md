# 🧠 大模型相关研究 | 2026年07月02日

> 本类共 **121** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-121](./part-03.md)

---

### 1. [From Search to Synthesis: Training LLMs as Zero-Shot Workflow Generators](https://arxiv.org/abs/2606.30704)

**<font color=#1a73e8>作者：</font>** Gan Luo, Zihan Qin, Bin Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) excel across a wide range of tasks, yet their instance-specific solutions often lack the structural consistency needed for reliable deployment. Workflows that encode recurring algorithmic patterns at the task level provide a principled framework, offering robustness across instance variations, interpretable traces for debugging, and reusability across problem instances. However, manually designing such workflows requires significant expertise and effort, limiting their broader application. While automatic workflow generation could address this bottleneck, existing methods either produce instance-specific solutions without learning task-level patterns, or cannot generalize beyond their training configurations. We present MetaFlow, which casts workflow generation as a meta-learning problem: given a task and an operator set, the model learns to compose solution strategies. MetaFlow trains in two stages: supervised fine-tuning on synthetic workflow data, followed by reinforcement learning with verifiable rewards (RLVR) that uses execution feedback across problem instances in the task to improve end-to-end success. The resulting model produces effective workflows for trained tasks and exhibits strong generalization to untrained tasks and novel operator sets. Across benchmarks in question answering, code generation, and mathematical reasoning, MetaFlow achieves performance comparable to state-of-the-art baselines on in-domain tasks with single inference, while demonstrating remarkable zero-shot generalization capabilities on out-of-domain tasks and operator sets.

---


### 2. [Indi-RomCoM: Code-Mixed Benchmark for Evaluating LLMs on Romanized Indic-English Instructions](https://arxiv.org/abs/2606.30790)

**<font color=#1a73e8>作者：</font>** Avisha Das, Mihir Parmar, Mohana Ramnath 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Romanized Code Mixing (RCM), where bilingual speakers fluidly blend local languages with English in Roman script, has emerged as the dominant form of communication across multilingual communities. While Large Language Models (LLMs) perform strongly on monolingual and native-script benchmarks, their ability to follow instructions and reason over RCM-based content remains largely unexplored. To this end, we introduce the Indi-RomCoM benchmark for facilitating systematic evaluation on Indic Romanized Code-Mixed instructions. Our benchmark spans seven instruction-following tasks, four widely spoken Indic languages, and three controlled code-mixing intensity levels. We extensively evaluate a suite of LLMs covering proprietary, open-weight, and Indic-focused models under zero- and few-shot settings. LLMs consistently underperform on RCM instructions, with performance degrading as code-mixing density increases. Furthermore, reasoning tasks suffer less degradation than detection tasks (e.g., Toxicity) because the generated explanations offer necessary context. We believe Indi-RomCoM helps the community in developing inclusive multilingual systems.

---


### 3. [When Calibration Rankings Reverse: Accuracy-Controlled Evaluation for Fair Comparison of LLMs](https://arxiv.org/abs/2606.30814)

**<font color=#1a73e8>作者：</font>** Zhichao Yang, Caiqi Zhang, Ruihan Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Calibration evaluates whether a model confidence aligns with its empirical accuracy. Existing studies often compare the calibration of different large language models using global calibration metrics such as Expected Calibration Error and Brier Score. We begin by showing, both theoretically and empirically, that such comparisons are confounded by differences in model accuracy. For fairer cross-model comparison, we then propose ACE, an accuracy-controlled evaluation framework with three complementary views: Instance-Aligned, Distribution-Aligned, and Candidate-Aligned calibration. Across multiple benchmarks, model families, and confidence elicitation methods, we use ACE to study two practically important comparison axes, small versus large models and thinking versus non-thinking models. We find that many previously reported calibration advantages under raw global metrics weaken substantially after accuracy control. We also find that ranking reversal is frequent: models favored by raw metrics often cease to be favored once accuracy is controlled. Our results show that raw global calibration metrics are not robust for cross-model comparison, and that fair calibration comparison requires accuracy-aware evaluation.

---


### 4. [BayesBench: Evaluating LLM Belief Trajectories Under Multi-Turn Evidence Accumulation](https://arxiv.org/abs/2606.30850)

**<font color=#1a73e8>作者：</font>** Ankur Samanta, Akshayaa Magesh, Tal Lancewicki 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are typically deployed in multi-turn conversations, where each turn provides new evidence that should reduce epistemic uncertainty about their environment. Acting rationally then requires inferring the unobserved quantities that govern it and updating beliefs about them as evidence accumulates. Yet most evaluations only score the model's final-turn answer in a single-turn format, leaving this process unexamined. We ask how closely LLMs' belief updates match those of a rational Bayesian reasoner in multi-turn settings, and introduce BayesBench, a suite of simulation environments that probe this across three progressively complex tasks: (i) Bayesian estimation, where the model infers an unknown parameter from sequential evidence; (ii) Bayesian prediction, where the model turns inferred beliefs about a latent variable into outcome forecasts; and (iii) latent-framed Bayesian prediction, where observations are filtered through a user-persona framing, requiring joint inference over the latent state and the persona. Across seven LLMs (3B--70B), scaling improves latent inference and evidence accumulation, with updates occasionally matching the Bayesian posterior. However, these gains do not reliably carry over to downstream prediction, exposing a gap between inferring latent structure and using it to rationally update beliefs about the target outcome.

---


### 5. [Test-Time Verification for Text-to-SQL via Outcome Reward Models](https://arxiv.org/abs/2606.30851)

**<font color=#1a73e8>作者：</font>** Mattia Tritto, Giuseppe Farano, Dario Di Palma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Improving the reliability of large language models (LLMs) at inference time is a central challenge in structured reasoning tasks such as Text-to-SQL. Common test-time inference strategies, including Best-of-N sampling and Majority Voting, rely on heuristic signals such as execution success or output frequency, which provide limited semantic discrimination across candidate outputs. In this work, we study Outcome Reward Models (ORMs) as learned semantic scoring functions for test-time verification in Text-to-SQL. While ORMs have been previously explored for test-time scaling and alignment, their application to structured query generation remains underexplored. We introduce GradeSQL, a scalable framework for training task-specific ORMs via automated candidate generation and execution-based labeling, enabling verifier training without manual annotation. We integrate ORMs into a verification-driven Best-of-N pipeline and evaluate our approach on the BIRD and Spider benchmarks across multiple open-source LLM families. ORM-based selection consistently outperforms execution-based Best-of-N and Majority Voting, with gains of up to +4.33% on BIRD and +2.10% on Spider. We further show that ORMs scale effectively with larger candidate sets and yield stronger improvements on complex queries. Overall, our results demonstrate that ORM-based verification provides a simple, effective, and scalable alternative to heuristic test-time selection strategies for Text-to-SQL. Code datasets and models are publicly available.

---


### 6. [When Does Learning to Stop Help? A Cost-Aware Study of Early Exits in Reasoning Models](https://arxiv.org/abs/2606.30852)

**<font color=#1a73e8>作者：</font>** Zhe Dong, Fang Qin, Manish Shah  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning models spend different amounts of useful computation across instances, but it remains unclear when a learned stopping rule improves over simple confidence or convergence thresholds. We study this question with LearnStop, a hidden-state-free checkpoint stopper for reasoning language models. At fixed budget checkpoints, LearnStop probes a short answer from the current reasoning prefix and predicts prefix correctness from online features such as answer confidence, entropy, prefix vote share, answer stability, and backtracking-marker density. Across 18 task-model settings spanning GSM8K, MATH-500, MMLU-Pro, AIME-90, GPQA, Qwen3, and DeepSeek-R1 distillations, the answer is task-dependent. On free-form math, learned multi-feature stopping improves the fixed-budget frontier and often beats scalar exits: on GSM8K with Qwen3-32B, the empirical frontier reaches a post-hoc peak adapt gain of +0.157, validation-selected operating points preserve positive gains, and the paired gain over the strongest scalar baseline is +0.028. On multiple-choice and very hard settings, scalar confidence, entropy, or stability rules are competitive or stronger. We therefore frame learned stopping not as a universal replacement for scalar exits, but as a tool whose value depends on trajectory structure. We further provide validation-selected operating points, paired bootstrap tests, finite-grid lost-correct risk calibration, cost accounting under KV-fork, prefix-cache, and black-box regimes, H100 serving profiles, checkpoint-schedule sweeps, transfer analyses, and robustness checks. The main practical finding is that learned stopping is useful when many questions become correct before full budget but do not exhibit a single reliable scalar stopping signal; its benefits largely disappear when confidence or answer convergence already solves the stopping problem.

---


### 7. [The Label Imitation Game: Turing Test Network for Zero-Shot Pseudo-Label Pruning](https://arxiv.org/abs/2606.30875)

**<font color=#1a73e8>作者：</font>** Brent A. Griffin, Jason J. Corso  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation model pseudo-labeling - labeling data strictly via zero-shot inference - enables massive scale, but performance is undermined by hallucinations that evade standard thresholds. To eliminate these errors, we introduce the Turing-inspired Label Imitation Game (LIG), a framework that formalizes pseudo-label pruning as an adversarial interrogation. Rather than filtering labels via isolated thresholds, we use the LIG to train a Turing Test Network (TTN), a task-agnostic "judge" that evaluates candidate pseudo-labels within a dataset-wide context. Experiments across four diverse datasets demonstrate the TTN's robustness, consistently enhancing label accuracy for three state-of-the-art vision-language models without costly supervision or retraining. Crucially, we demonstrate that learned semantic-contextual logic is a robust alternative to spatial-geometric verification, enabling a unique zero-shot task transfer capability - a TTN trained strictly on image classification datasets can effectively prune complex object detection pseudo-labels. This pruning yields F1-score gains of 28% for the worst-performing baseline categories and 44% with task-specific fine-tuning. Significantly, we also observe Category Revival, where the TTN pruning "detoxifies" the training signal for downstream models and enables them to recover from zero recall on transfer-vulnerable classes. The pre-trained TTN models and code are available at this https URL.

---


### 8. [Training Therapeutic Judges and Multi-Agent Systems for Human-Aligned Mental Health Support](https://arxiv.org/abs/2606.30887)

**<font color=#1a73e8>作者：</font>** Mizanur Rahman, Abeer Badawi, Elahe Rahimi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models show promise for mental health support, yet therapeutic quality improves only when evaluation functions as an actionable control signal rather than a passive metric. We introduce a framework that formulates therapeutic response generation as a decision-refinement problem driven by multi-dimensional, human-aligned evaluation. In Stage I, we introduce TheraJudge, an open-source therapeutic evaluator trained via preference-based optimization on human-annotated data to produce reliable judgments across 7 psychological dimensions. In Stage II, we introduce TheraAgent, which operationalizes TheraJudge's evaluations through a coordinated refinement process with specialized Critic, Coach, and Therapist roles that translate evaluative signals into targeted response revisions. Empirically, TheraJudge achieves strong agreement with clinician ratings, with intraclass correlation coefficients (ICC = 0.87-0.95), surpassing supervised baselines and strong closed-source judges, particularly on critical dimensions such as Safety, Relevance, and Empathy. Acting on these evaluations, TheraAgent yields a +0.43 improvement in human-rated therapeutic quality (on a 5-point scale) under blind evaluation, with 96\% clinician inter-rater reliability. Low-quality responses ($\leq 3$) improve by +2.45 points with a 94\% recovery rate, demonstrating targeted correction of unsafe outputs. Overall, our results indicate that effective alignment of mental-health LLMs stems from acting on human-aligned evaluation, rather than relying solely on stronger generation. We release code at this https URL.

---


### 9. [Investigating Multi-Agent Deliberation in Law](https://arxiv.org/abs/2606.30906)

**<font color=#1a73e8>作者：</font>** Cor Steging, Ludi van Leeuwen, Tadeusz Zbiegień  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence is increasingly applied to the field of law, and has the potential to increase access to justice. One particular movement that is gaining traction is that of agentic AI, wherein AI agents, based on Large Language Models (LLMs) can take autonomous actions. In particular, multi-agent approaches in the legal domain remain largely unexplored. In this paper, we investigate multi-agent deliberation methods for legal reasoning tasks using LLMs. We explore multi-agent deliberation (MAD) and introduce two novel multi-agent frameworks inspired by courtroom procedures and legal argumentation. Our experiments on both legal and non-legal benchmarks reveal that multi-agent frameworks achieve comparable overall performance to baseline large language models, but produce significantly distinct answers. Notably, these approaches can successfully solve cases that the baseline fails to address, and vice versa. We conduct a qualitative evaluation and highlight scenarios where multi-agent frameworks outperform monolithic approaches. For example, multi-agent approaches appear better suited for answering questions that require critical thinking from multiple perspectives. Our work positions multi-agent systems as a promising direction for AI in the legal domain, while demonstrating the potential of law-inspired multi-agent approaches for deliberation.

---


### 10. [Beyond Clean Text: Evaluating Encoder and Decoder Robustness for Bangla Event Detection in Noisy Text](https://arxiv.org/abs/2606.30914)

**<font color=#1a73e8>作者：</font>** Tanvir Ahmed Sijan, S. M Golam Rifat, Nayeemul Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Event detection (ED) systems are typically evaluated on clean, curated text, leaving their robustness to real-world noise largely unexplored, particularly for low-resource languages such as Bangla. We introduce a generalized Bangla news event ontology and a benchmark comprising 9,979 annotated sentences across 40 event subtypes, spanning clean news text, real-world Automatic Speech Recognition (ASR) transcripts, and orthographically corrupted text. We systematically evaluate fine-tuned encoder-only models (BanglaBERT and XLM-R) alongside instruction-tuned decoder-only large language models (Llama 3 and Gemma 3). Our results reveal a clear architectural trade-off: encoder models achieve higher performance on clean text but degrade substantially under noise, whereas decoder-only LLMs are markedly more robust, particularly when event triggers are corrupted. We further show that embedding annotation guidelines during instruction tuning establishes a higher performance baseline on noisy text but yields inconsistent reductions in performance degradation across noisy conditions. Finally, model scaling consistently improves the robustness of decoder-only LLMs, while combined training on clean and noisy data serves as an effective regularization strategy that disproportionately benefits encoder architectures, significantly narrowing the robustness gap.

---


### 11. [RoPoLL: Robust Panel of LLM Judges](https://arxiv.org/abs/2606.30931)

**<font color=#1a73e8>作者：</font>** Anish Acharya, Kris W Pan, Brian Verkhovsky  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The LLM Jury, a Panel of LLM Evaluators (PoLL) reporting consensus scores, has become a practical alternative to single-judge LLM evaluation, yet its statistical behavior remains poorly understood. We formalize the LLM Jury under the Huber contamination model and show that PoLL incurs unbounded bias
under any positive contamination, regardless of jury size, whenever a single judge fails in a biased, LLM-typical way (mode collapse, sycophancy, safety refusal). Framing jury consensus as classical robust mean estimation, we propose RoPoLL (Robust Panel of LLM-as-Judge), which preserves the PoLL
panel but replaces the aggregation function with a robust mean estimator, instantiated with the geometric median (GM): tuning-free, with the optimal finite-sample breakdown point 1/2. A finite-sample error bound and a matching information-theoretic minimax lower bound agree on the parametric rate
sigma*sqrt(d/N) and differ on the breakdown floor by a factor of sqrt(d), a statistical-computational gap that polynomial-time RoPoLL pays relative to the intractable Tukey halfspace median. Across 13 open-weight judges (4B-675B), three reward-model benchmarks, and four corruption regimes at rates up
to 50%, RoPoLL dominates PoLL on every biased corruption type: by about 19% on cross-dimensional attacks at matched compute, and by orders of magnitude on heavy-tailed Byzantine adversaries. A 3-judge RoPoLL committee at 38B beats Mistral-Large-3 (675B) by 1.31x on HelpSteer-2 under 30% bimodal-random
corruption, an 18x parameter advantage at better accuracy; a Noisy-GT control confirms the premium is paid against biased contamination, not benign imprecision.

---


### 12. [Bridging Scientific Heritage: An Arabic--Russian Parallel Corpus and LLM Benchmark for Sustainable Knowledge Transfer](https://arxiv.org/abs/2606.30943)

**<font color=#1a73e8>作者：</font>** M. K. Arabov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Russian and Arabic are among the major languages of scientific communication. Language barriers impede the exchange of research results between these communities, which affects international collaboration and the progress of sustainability-related research. We present a benchmark for Arabic--Russian scientific translation. The benchmark includes a hybrid parallel corpus of about 27,000 sentence pairs, compiled from scientific abstracts and general-domain texts (religion, news, conversations). We fine-tune three multilingual language models -- mT5-base (580M parameters), NLLB-200-distilled-1.3B (1.3B), and Qwen2.5-7B-Instruct (7B) -- using LoRA with ranks 8, 16, 32, and 64. The Qwen2.5-7B model with QLoRA (rank 8) yields BLEU 23.15, chrF 43.89, BERTScore 0.906, and COMET 0.758. These are +4.36 BLEU and +0.051 COMET above the zero-shot baseline. Few-shot prompting with three examples does not improve performance, indicating that domain-specific fine-tuning is required. We release the models, the corpus, and the evaluation code. By lowering the language barrier for scientific texts, the work enables knowledge exchange between Arabic-speaking and Russian-speaking researchers. It contributes to sustainable partnerships (UN SDG 17) and innovation infrastructure (SDG 9), aligning with the conference's focus on technology-driven sustainable development.

---


### 13. [AgRefactor: Self-Evolving Agentic Workflow for HLS Compatibility and Performance](https://arxiv.org/abs/2606.30949)

**<font color=#1a73e8>作者：</font>** Yang Zou, Zijian Ding, Yizhou Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-Level Synthesis (HLS) provides a fast path from concepts to silicon, but converting real-world software into synthesizable HLS code remains challenging due to restrictive language support and the gap between software and hardware programming practices. Existing automated and LLM-based refactoring approaches partially address this problem, yet they often lack flexibility, struggle to scale, and incur high computational costs. We introduce AgRefactor, an LLM-based multi-agent workflow for refactoring software into HLS-compatible programs. AgRefactor incorporates a self-evolving memory system that accumulates and retrieves factual and strategic knowledge across tasks, improving robustness and efficiency on unseen programs. To reduce cost and enhance scalability, it integrates automated refactoring tools, enabling agents to balance LLM-driven rewrites with efficient tool-based transformations. On 9 out of 11 challenging real-world benchmarks, which are 5-10x longer than the most complex cases studied in prior work, AgRefactor outperforms or matches the state-of-the-art automated refactoring tool and a strong LLM-based baseline built on the same framework backbone. Further agentic performance optimization yields a 6.51x geometric mean speedup over the SoTA pragma tuning tool and a 1.20x speedup over optimized open-source designs with less than 20% extra resources. AgRefactor is fully-automated and open-sourced.

---


### 14. [Ethics and Social Responsibility in AI-Assisted Interviewing: An LLM-in-the-Loop Study of AI-Generated Follow-Up Questions](https://arxiv.org/abs/2606.30980)

**<font color=#1a73e8>作者：</font>** He Zhang, Yueyan Liu, Xin Guan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Semi-structured interviews rely on timely, context-sensitive follow-up questions, yet interviewers' cognitive load and limited domain familiarity can constrain probing depth. We report findings from an LLM-in-the-loop Wizard-of-Oz (WoZ) study that simulates an AI follow-up assistant in live interviewing while preserving human oversight. In our setup, a co-interviewer selectively relayed and could edit AI-generated follow-up questions (AGQs) produced in real time by GPT-4o, enabling a realistic approximation of deployment without fully automating the interaction. Across 17 interviewers with varied qualitative-method expertise, participants raised five interlocking concerns: (1) harmful or discriminatory language and unpredictable interaction harms, (2) undermining interviewees' sense of respect through divided attention and missing nonverbal cues, (3) technology-based participation inequality, (4) unclear responsibility when harms occur, and (5) privacy, disclosure, and compliance risks when AI listens, records, or transcribes sensitive content. We translate these concerns into design and governance implications for safer, more respectful, and more accountable AI-assisted interviewing.

---


### 15. [A Three-Phase Foundation Model for Tax-Aware Personalized Portfolio Management](https://arxiv.org/abs/2606.30997)

**<font color=#1a73e8>作者：</font>** Ramin Pishehvar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a three-phase deep reinforcement learning system for personalized portfolio management that addresses three limitations shared by all prior financial RL work: 1) ticker lock-in, 2) monolithic objectives , and 3) static user models. Phase 1 pretrains a ticker-identity-free cross asset encoder via self-supervised learning on a multi-asset corpus, augmented by a frozen parallel branch using Chronos, a T5-based time series foundation model, fused via a learned gating mechanism. To our knowledge, this is the first application of a time series foundation model to portfolio management RL. The encoder generalizes to any publicly traded asset via a 50-dimensional observable metadata vector that requires no retraining for new tickers. Phase 2 fine-tunes a MoE (Mixture of Experts) portfolio actor critic with PPO under an objective-conditioned reward that simultaneously serves six distinct investment goals sampled per episode: short-term alpha, short-term gain, long-term gain, capital preservation, tax-loss harvesting, and long-term-gains-only. A MoE architecture assigns each objective to a specialized expert head (momentum, growth, defensive, tax-aware), and a learned intent router blends experts based on the active objective and current market regime, which eliminates cross-objective gradient conflict. Phase 3 adds a lightweight personalization layer further adapted at inference time to each individual via a 76-parameter LoRA module fine-tuned on real brokerage transaction history, inferring investment objectives from revealed trading behavior rather than questionnaires. A natural language intent parser converts free-form goals directly into structured investment objective parameters.

---


### 16. [Evaluating Interactivity: Toward Automated Assessment of AI-Generated Explorable Explanations](https://arxiv.org/abs/2606.31012)

**<font color=#1a73e8>作者：</font>** Xiaozao Wang, Zhewei Wang, Hongyi Wen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While large language models now enable rapid generation of interactive learning materials, evaluating the interaction quality of these explorable explanations remains an open challenge. Existing benchmarks largely focus on code executability or visual fidelity, providing limited insight into dynamic interaction behaviors such as learner-controlled state transitions and context-sensitive system responses, which are factors that critically shape learners' conceptual understanding. We present EE-Eval, an automated evaluation framework that formalizes interactivity as a finite space of learner-controllable states and transitions, represented as a Finite State Machine (FSM). By extracting FSMs from AI-generated explorable explanations, EE-Eval externalizes implicit interaction logic into an explicit, machine-interpretable graph. Evaluation is performed by comparing each generated FSM to an ideal FSM that encodes pedagogical intent, using a combination of graph-based metrics and embedding-based comparison of states, actions, and feedback to measure their structural and semantic similarity. Across thousands of generated explorable explanations spanning 127 concepts and produced by 6 AI models, EE-Eval consistently differentiates interaction quality beyond surface-level criteria such as functional correctness or visual quality, and exhibits substantially stronger alignment with human judgments of interactivity and pedagogical effectiveness than existing baselines. By framing interactivity as testable behavioral models rather than an emergent byproduct of LLM generation, EE-Eval transforms evaluation into a reflective diagnostic tool, enabling pedagogically grounded and actionable human-AI collaboration in creating interactive educational content.

---


### 17. [CORTEX: Token-Level Hallucination Detection in RAG via Comparative Internal Representations](https://arxiv.org/abs/2606.31033)

**<font color=#1a73e8>作者：</font>** Kazuaki Furumai, Shuichiro Haruta, Kazunori Matsumoto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose CORTEX, a token-level hallucination detection method for Retrieval-Augmented Generation (RAG). In long-form RAG outputs, hallucinations often arise in localized spans rather than throughout an entire response. CORTEX therefore identifies ungrounded content at the token level, enabling fine-grained localization of hallucinations. The key intuition behind CORTEX is that tokens grounded in retrieved documents should be more strongly influenced by those documents than hallucinated tokens. To capture this document-induced effect, CORTEX compares internal representations of a large language model (LLM) under two conditions: with and without the retrieved documents. Instead of relying solely on each token's immediate sensitivity to the retrieved documents, CORTEX also leverages the propagation of document-grounded information through preceding tokens, reducing false positives for tokens whose evidence has already been absorbed into the context. Finally, CORTEX applies post-processing smoothing step that models the tendency of hallucination labels to persist over contiguous spans, reducing local noise and encouraging span-consistent predictions. Experiments on two RAG benchmarks and three LLMs show that CORTEX substantially improves token-level hallucination detection, with each component consistently contributing to performance gains.

---


### 18. [Teaching LLMs to Recommend and Defer in Underrepresented Epilepsy Care](https://arxiv.org/abs/2606.31036)

**<font color=#1a73e8>作者：</font>** Shreyas Rajesh, Kartik Sharma, Tonmoy Monsoor 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Specialist epilepsy expertise is scarce in resource-constrained settings, making LLM-based decision support attractive for frontline clinicians managing longitudinal treatment. Such systems must adapt to local prescribing practice and know when to defer. We study this problem in Ugandan pediatric epilepsy care, predicting anti-seizure medication regimens from longitudinal unstructured clinic notes. Standard prompting achieves non-trivial agreement with physician prescriptions, but neurologist review shows that many errors reflect distribution-miscalibrated prescribing defaults rather than failures to parse the local record. We introduce MANANA, a non-parametric prompt-learning framework that learns local prescribing guidance from a small patient-level training set. MANANA converts observed prescription errors into auditable prompt memories, instantiated in single-agent and multi-agent variants, and improves over classical ML models, direct LLM prompting, and prompt-optimization baselines across two independently collected Ugandan cohorts. We further propose Bayesian prompt averaging, which converts the learned prompt trajectory into prescription likelihoods and an uncertainty-based deferral signal. On the independently collected held-out cohort, this improves visit-level top-3 prescription accuracy by 4-8 percentage points over prompt-optimization baselines and enables selective prediction: the system can auto-handle the most confident half of cases at 95% precision, or the most confident quarter at 99% precision, while deferring lower-confidence cases for specialist review.

---


### 19. [Truth or Sophistry? LoFa: A Benchmark for LLM Robustness Against Logical Fallacies](https://arxiv.org/abs/2606.31039)

**<font color=#1a73e8>作者：</font>** Xudong Shen, Li Yuan, Ye Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) exhibit strong semantic capabilities, yet their resilience to manipulative linguistic patterns such as logical fallacies remains underexplored. Prior work has primarily examined whether LLMs can identify or classify fallacies, leaving their robustness against fallacious persuasion insufficiently studied. To address this gap, we introduce LoFa (Logical Fallacy), a comprehensive benchmark for evaluating LLM robustness against fallacies. LoFa is constructed through a multi-agent pipeline that pairs factual questions with fallacious arguments, and is accompanied by a multi-round debate framework for assessing model resilience under sustained adversarial persuasion. To disentangle fallacy robustness from a model's inherent knowledge limitations, we further propose Logical Fallacy Resistance at k (LFR@k), a metric that quantifies resistance to fallacious attacks. Experiments show that LLMs exhibit varying levels of robustness across different fallacy types, revealing distinct vulnerability profiles among models.

---


### 20. [OpenLife: Toward Open-World Artificial Life with Autonomous LLM Agents](https://arxiv.org/abs/2606.31046)

**<font color=#1a73e8>作者：</font>** Atsushi Masumori, Itsuki Doi, Norihiro Maruyama 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial life has explored life-like behavior on many computational substrates, but mostly in researcher-designed closed worlds. We argue that large language model (LLM) agents, with persistent memory, tool use, network access, and payment, now make it possible to move artificial life into the open social, technical, and economic world, a paradigm we call open-world Artificial Life (open-world ALIFE). Our proof-of-concept, OpenLife, surrounds a stateless LLM not with a single "smart agent" but with a society of asynchronous processes: memory, perception, evaluation, and a budget-based metabolism that makes persistence normative. With no fixed objective available, experience is appraised by open-vocabulary LLM judgment rather than scalar reward, and memory is rewired by meaning rather than frequency. Running six such agents in the open world for about twelve weeks and counting, we report the life-like dynamics that emerge: a shift from reactive to spontaneous activity, individuation into distinct agents, emergent social structure, and a first self-earned external income. We do not claim OpenLife has realized artificial life, but that open-world ALIFE is now a viable experimental paradigm and a concrete platform for studying what might cautiously be called living AI.

---


### 21. [Knowledge Distillation from Large Reasoning Models to Compact Student Models: A Case Study on the John O Bryan Mathematics Competition](https://arxiv.org/abs/2606.31048)

**<font color=#1a73e8>作者：</font>** Gaurab Baral, Aaditya Khanal, Yangyang Tao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper investigates knowledge distillation from a large reasoning model (DeepSeek-R1) to a compact student model (Qwen2.5-7B). Using historical problems from the John O'Bryan Mathematics Competition at Northern Kentucky University (2011-2025), we build a Chain-of-Thought (CoT) training corpus through a dual-agent framework. The dataset is used to fine-tune the student model with Low-Rank Adaptation (LoRA) on Apple Silicon hardware using the MLX framework. The base Qwen2.5-7B model achieves 64.67% accuracy on competition problems, while the DeepSeek-R1 teacher achieves 91.40%. An initial 1,000-iteration training run revealed severe overfitting, with validation loss reaching a minimum at iteration 200 before rising steadily. Based on this finding, we ran five independent training runs each limited to 200 iterations with varied random seeds to assess result stability. Across these five runs, the fine-tuned student model achieves a mean accuracy of 69.43% (std dev 0.17%) on the competition dataset, a 4.76 percentage-point improvement over the base model, and generalizes to 73.1% (std dev 0.18%) on the MATH-500 benchmark. We further study how response length affects answer quality across six reasoning levels (R1-R6): accuracy declines consistently from 69.43% at R1 (mean 220 words) to 41.9% at R6 (mean 31.2 words), with the two-person speed section most sensitive to token reduction. These results demonstrate that CoT distillation improves compact student models and that response length is a critical factor in mathematical reasoning quality.

---


### 22. [ADAPT: Attention Dynamics Alignment with Preference Tuning for Faithful MLLMs](https://arxiv.org/abs/2606.31054)

**<font color=#1a73e8>作者：</font>** Zhiyuan Yao, Zheren Fu, Zhixiao Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) are critically hampered by hallucination, generating content inconsistent with the provided image. In this paper, we identify an internal signature of hallucination: progressive degradation of text-to-image cross-attention during generation, leading to specific failure patterns like unfocused or biased attention. Existing mitigation strategies are largely outcome-driven and do not explicitly target this failure mode. To address this problem, we propose ADAPT (Attention Dynamics Alignment with Preference Tuning), an attention-based framework that intervenes directly on text-to-image cross-attention dynamics. We propose ADAPT with three key contributions: a cross-attention visual anchor refined from early decoding to provide stable spatial grounding, an attention-supervised inference mechanism that detects and corrects attention drift online, and a Visual Attention Guidance DPO that aligns preferences toward visually grounded responses. Experiments show that each component of ADAPT contributes to hallucination reduction, and the full framework achieves new best results across multiple hallucination benchmarks, reducing hallucination rates by 40%-60% across mainstream backbones while preserving general multimodal capabilities. Our work provides an attention-based perspective on mitigating hallucinations by exploring the model's internal text-to-image cross-attention behaviors. Code is available at this https URL

---


### 23. [Building a Multimodal Dataset of Academic Paper for Keyword Extraction](https://arxiv.org/abs/2606.31069)

**<font color=#1a73e8>作者：</font>** Jingyu Zhang, Xinyi Yan, Yi Xiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Up to this point, keyword extraction task typically relies solely on textual data. Neglecting visual details and audio features from image and audio modalities leads to deficiencies in information richness and overlooks potential correlations, thereby constraining the model's ability to learn representations of the data and the accuracy of model predictions. Furthermore, the currently available multimodal datasets for keyword extraction task are particularly scarce, further hindering the progress of research on multimodal keyword extraction task. Therefore, this study constructs a multimodal dataset of academic paper consisting of 1000 samples, with each sample containing paper text, images, audios and keywords. Based on unsupervised and supervised methods of keyword extraction, experiments are conducted using textual data from papers, as well as text extracted from images and audio. The aim is to investigate the differences in performance in keyword extraction task with respect to different modal information and the fusion of multimodal information. The experimental results indicate that text from different modalities exhibits distinct characteristics in the model. The concatenation of paper text, image text and audio text can effectively enhance the keyword extraction performance of academic papers.

---


### 24. [MultiUAV-Plat: An LLM-Oriented Platform, Benchmark and Framework for Multi-UAV Collaborative Task Planning](https://arxiv.org/abs/2606.31073)

**<font color=#1a73e8>作者：</font>** Sheng Zhang, Qinglin Li, Yuechao Zang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) provide a promising interface for high-level robotic task planning, but their use in multi-UAV collaboration remains difficult to evaluate systematically. Existing UAV simulators mainly emphasize dynamics, perception, or low-level control, while existing LLM-agent benchmarks rarely capture aerial-robotics constraints such as partial observability, spatial coverage, UAV assignment, and multi-vehicle coordination. To bridge this gap, we present MultiUAV-Plat, a lightweight, easy-to-use, LLM-agent-oriented simulation platform for multi-UAV collaborative task planning. The platform exposes concise RESTful APIs, agent-facing observations, role-based information access, hidden validation logic, and optional 2D/3D visualization, allowing agents to solve missions through realistic tool interaction rather than privileged simulator access. Built on this platform, the MultiUAV-Plat Benchmark contains 75 mission sessions, 1500 natural-language tasks, and 9396 validation checks across target assignment, area search, and area assignment and patrol scenarios. We further propose Agent4Drone, a task-specific LLM agent framework that structures multi-UAV behavior into memory, observation, task understanding, planning, execution, and verification. In a full paired benchmark comparison, Agent4Drone achieves a 57.9% task pass rate, a 74.6% average task check pass rate, and a 72.0% global check pass rate, substantially outperforming a ReAct baseline at 30.6%, 47.9%, and 43.1%, respectively. Agent4Drone also reduces the total failed task rate from 32.4% to 12.9%. These results demonstrate that MultiUAV-Plat and MultiUAV-Plat Benchmark provide a reproducible foundation for studying LLM-driven multi-UAV autonomy under realistic information and execution constraints.

---


### 25. [Fora: From Weight-Space to Function-Space Protection in Capability-Preserving Fine-Tuning](https://arxiv.org/abs/2606.31092)

**<font color=#1a73e8>作者：</font>** Rui Zhou, Tianci Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full fine-tuning adapts large language models to new tasks but can erode capabilities they already possess. Existing remedies protect through proxies such as parameter distances, importance penalties, output matching, or dominant singular directions of the weights, but none directly asks which activation directions the preserved capability relies on. We argue that a capability is characterized more faithfully by the activation subspace it induces than by the singular geometry of the weight matrix, and develop function-space protection, instantiated as FORA (Function-space Orthogonal Residual Adaptation). From label-free calibration inputs, FORA estimates, per layer, the principal directions $Q$ of the input-activation covariance and forms a right projector $P_Q = I - QQ^T$. Paired with a left projector $P_U$ from the weight SVD, the update is $\Delta W = P_U M P_Q + U_2 D_{\delta} V_2^T$: a high-capacity branch structurally barred from reading capability-relevant function directions, plus a narrow spectral channel for controlled plasticity. The construction extends to parameter-efficient adaptation via $M \to (\alpha/r) BA$. Across three settings on Qwen3-1.7B, including COGS and GSM8K learned while preserving translation and translation learned while preserving math, FORA consistently improves preservation over weight-space projection and standard regularization, with only a small new-task trade-off in the math-preservation setting. A controlled ablation isolating the projection source shows that the advantage comes not from projection itself, but from projecting onto capability-derived rather than weight-derived directions. Code is available at this https URL.

---


### 26. [PiLoT v2: Pixel-to-Orthogonal Map Alignment for Free-view UAV Geo-localization](https://arxiv.org/abs/2606.31098)

**<font color=#1a73e8>作者：</font>** Xinyi Liu, Xiaoya Cheng, Rouwan Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time, drift-free UAV geo-localization is essential for autonomous missions in GNSS-denied environments. The pioneering system, PiLoT, achieves high precision via Neural Pixel-to-3D Registration, aligning UAV video streams with a single rendered reference view from 3D meshes. However, its reliance on heavy 3D meshes incurs massive storage overheads, complex map acquisition, and significant computational rendering costs, severely hindering deployment on embedded platforms. To address these bottlenecks, we propose PiLoT v2, a lightweight yet robust evolution that shifts the paradigm to direct pixel-to-orthogonal map registration for free-view UAV geo-localization. By leveraging True Digital Orthophoto Maps (TDOMs) and Digital Surface Models (DSMs) as the reference substrate, PiLoT v2 replaces GPU-intensive 3D rendering with a highly efficient, CPU-friendly map cropping operation. To bridge the severe geometric discrepancy between these 2.5D orthogonal crops and free-view oblique UAV imagery, we train a cross-view feature registration network using a novel, large-scale geometrically annotated dataset. Furthermore, we integrate onboard sensor prior--specifically gravity direction and single-point laser rang--directly into the pose optimization manifold to enhance robustness against cross-view visual degradation. Experimental results demonstrate that PiLoT v2 achieves performance comparable to, or even exceeding, its Pixel-to-3D predecessor, while offering drastically lower storage and computational costs.

---


### 27. [Seeing Through Multiple Views: Parameter-Efficient Fine-Tuning via Selective Neurons for Consistent Radiology Report Generation](https://arxiv.org/abs/2606.31099)

**<font color=#1a73e8>作者：</font>** Yucheng Chen, Jinjing Zhu, Yang Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent years have seen substantial advances in radiology report generation (RRG), yet existing approaches predominantly adopt direct feature fusion when handling multi-view X-ray images. Such approaches overlook the potential clinical inconsistencies and inaccuracies arising when a single model processes different views, adversely impacting performance and clinical reliability. To this end, we introduce View-PNDF (View-specific Pattern Neuron Detection and Fine-tuning), a parameter-efficient framework that fosters view-consistent report generation from a neuronal perspective. Specifically, View-PNDF comprises: (i) a view-specific neuron detection module identifying neurons responsive to particular views, (ii) a verification module quantifying the existence of these neurons, and (iii) a selective fine-tuning strategy strengthening detected neurons while preserving view-agnostic representations. By updating only view-specific neurons, View-PNDF achieves consistent diagnoses across different views with reduced computational costs. Subsequently, we employ Large Language Models (LLMs) to consolidate the view-specific reports into a complete radiology report. Furthermore, we use traditional Natural Language Generation (NLG) metrics-based assessment on integrated reports for baseline comparison and employ LLM-based assessment (e.g., GPT-4o) on view-specific reports to capture clinical significance. Extensive experiments on two medical RRG benchmarks demonstrate that View-PNDF substantially improves view-specific chest X-ray report generation quality while maintaining robust general-view performance.

---


### 28. [The Past Is Prologue: A Plug-in Controller for Selective Updates in Sequentially Evolving LLM Memory](https://arxiv.org/abs/2606.31121)

**<font color=#1a73e8>作者：</font>** Zihan Chen, Songwei Dong, Chengshuai Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sequentially evolving LLM memory enables agents to reuse past experience, but existing systems usually deploy each locally generated memory update without checking whether it improves future behavior. As a result, updates that help the current task may overwrite useful knowledge, introduce over-specific rules, or bias the final memory toward recent examples. We propose Janus, a plug-in memory controller that decides whether to accept a candidate memory update or retain the previous memory. To make this decision efficient, Janus uses a Memory Momentum Trigger to identify suspicious deviations in the memory-update trajectory, and compares old and new memories on a compact hybrid evaluation set of coverage, boundary, and fresh tasks instead of replaying the full history. Janus is method-agnostic and wraps existing updaters without changing their update rules. Across six datasets, two backbone LLMs, and two memory updaters, Janus improves average accuracy by +2.7 to +4.6 points over the corresponding base updaters.

---


### 29. [Beyond the Library: An Agentic Framework for Autoformalizing Research Mathematics](https://arxiv.org/abs/2606.31134)

**<font color=#1a73e8>作者：</font>** Arshia Soltani Moakhar, Iman Gholami, Max Springer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have demonstrated exceptional capabilities in mathematical reasoning, they frequently produce subtle errors that evade human detection. Formal mathematical languages like Lean 4 offer mechanical proof checking, strongly motivating the need for autoformalization: the automatic translation of natural language mathematics into verifiable code. Recent trends indicate that general-purpose LLMs, heavily optimized for standard programming, now outperform smaller models explicitly fine-tuned for Lean. Leveraging this shift, we introduce an agentic autoformalization framework powered by general coding LLMs. At the core of our system is an orchestrator that manages a multi-agent pipeline tailored for research-level mathematics. Because cutting-edge research frequently relies on concepts outside the scope of existing libraries like Mathlib, our system dynamically extends necessary type definitions and validates them via a novel Auxiliary Lemma technique before formalizing the primary theorems. We applied our approach to PutnamBench, producing machine-checked Lean proofs for a random sample of 32 problems. Furthermore, we evaluate our system on five papers from the ACM Symposium on Theory of Computing (STOC) spanning combinatorics, communication complexity, mechanism design, and learning theory, successfully formalizing their main theorems and validating the generated formalizations with human experts; for all five we also formalize the proofs alongside the statements, and notably two of them are proved with no axioms beyond Lean's kernel. All of our formalizations are available at this https URL .

---


### 30. [SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference](https://arxiv.org/abs/2606.31145)

**<font color=#1a73e8>作者：</font>** Amirhossein Abaskohi, Giuseppe Carenini, Peter West 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly operate over long contexts, where the KV cache becomes a dominant memory bottleneck: its size grows linearly with sequence length and must be retained throughout decoding, making full GPU caching prohibitively expensive without compression. Existing KV cache compression methods struggle to balance efficiency with faithful context preservation. Token eviction discards information, while semantic grouping fixes compression decisions at prefill time; neither can recover token-level detail from a compressed span once it becomes relevant during generation. As a solution, we propose SeKV, a resolution-adaptive semantic KV cache that organizes context into entropy-guided semantic spans and stores them across a GPU-CPU memory hierarchy without discarding information. Each span keeps a lightweight summary vector on GPU for coarse routing and a low-rank SVD basis on CPU for on-demand token-level reconstruction. A trained zoom-in mechanism selectively expands query-relevant spans during decoding, enabling precise retrieval without materializing the full KV cache on GPU. SeKV enables adaptive token-level reconstruction while keeping the base LLM fully frozen and adding fewer than 0.05% trainable parameters. Across four benchmarks, SeKV improves over the strongest semantic compression baseline by 5.9% on average while reducing GPU memory by 53.3% versus full KV caching at 128K context. Code is available on this https URL.

---


### 31. [Rethinking Foundation Model Collaboration: Enhancing Specialized Models through Proxy Task Reasoning](https://arxiv.org/abs/2606.31157)

**<font color=#1a73e8>作者：</font>** Hongyi Lin, Yang Liu, Jinhua Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models are increasingly integrated into embodied intelligence systems, but directly assigning them structured prediction tasks requires precise geometric and numerical estimation, where specialized models often remain stronger. This capability mismatch raises a key question: should foundation models replace task-specific predictors, or should they collaborate through tasks better aligned with their strengths? We propose FAT, a foundation-model-augmented task-specific reasoning framework that treats collaboration as task decomposition rather than model replacement. FAT decomposes structured prediction into specialist prediction, information-space reconstruction, and foundation-model proxy reasoning. The specialist generates geometrically and physically valid hypotheses in the native output space, while the foundation model performs a bounded proxy task, such as selection or verification, over reconstructed multimodal candidates. We instantiate this principle as ProxySelect with a vision--language model. Across 2D object detection, 3D object detection, trajectory prediction, and semantic segmentation, ProxySelect consistently improves specialized baselines and substantially outperforms direct foundation-model regression at lower computational cost. These results suggest a general collaboration principle: specialized models preserve task-specific structure, while foundation models refine their hypotheses through contextual proxy reasoning.

---


### 32. [ComplianceGate: Classifier-Gated Multi-Tier LLM Routing for Inference in Regulated Industries](https://arxiv.org/abs/2606.31163)

**<font color=#1a73e8>作者：</font>** Abhishek Dey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models deployed in regulated industries operate under two constraints: compliance enforcement and cost efficiency. Personally identifiable information (PII) in user queries can reach model endpoints before the system determines whether that data should leave its jurisdictional boundary. Serving all queries through a single large model consumes full GPU capacity regardless of query complexity while offering no mechanism for geographic routing. Mixture-of-Experts architectures do not address this routing occurs between expert layers within the model after data has already arrived at the endpoint, with all experts loaded in memory regardless of query complexity. We propose a classifier-gated routing architecture that enforces compliance by design. A trained encoder classifier sits before any decoder inference, evaluating each query for complexity and data sensitivity, then routing it to an appropriately sized dense model in the appropriate geographic location. PII-containing queries route to local endpoints before any LLM computation begins, making data residency violations structurally impossible. Simple queries reach small, fast models at a fraction of the cost. Our evaluation on 600 queries demonstrates 39% median latency reduction, 33-52% cost savings depending on query distribution, and generation throughput of 122-200 tokens/second versus 50-64 for the baseline. The encoder classifier achieves 99.2% accuracy with near-perfect PII recall at 7ms inference overhead, establishing pre-inference classification as a practical path to compliance-by-design LLM deployment.

---


### 33. [TAG-DLM: Diffusion Language Models for Text-Attributed Graph Learning](https://arxiv.org/abs/2606.31166)

**<font color=#1a73e8>作者：</font>** Lingjie Chen, Yuanchen Bei, Haobo Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-attributed graphs (TAGs), where each node carries a natural language description, require models to jointly reason over text and graph topology. Existing approaches often handle the two modalities separately: graph neural networks operate on shallow text features, while hybrids of LLMs and graphs use the language model mainly as a text encoder and delegate structure learning to a separate graph module. We propose method that unifies textual reasoning and graph message passing within a masked diffusion language model, a language model with bidirectional attention and generative decoding. For each graph instance, method linearises a sampled local neighbourhood into a token sequence and injects graph structure through a topology attention mask, which realises message passing over the graph. Because the diffusion language model can both interpret and generate text, the method adapts to different tasks simply by changing the prompt, supporting node classification, link prediction, and cross-dataset transfer with no target-specific fine-tuning.
Experiments show that method outperforms graph neural networks, graph transformers, and LLM-based baselines on all three TAG benchmarks across two tasks, improving over the strongest baseline by up to 3.9 points.

---


### 34. [Beyond Single Character: Evaluating MLLMs for Sentence-Level Oracle Bone Inscription Understanding](https://arxiv.org/abs/2606.31169)

**<font color=#1a73e8>作者：</font>** Ziqi Li, Zijian Chen, Tingzhu Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing AI-assisted oracle bone inscription (OBI) visual recognition and understanding studies mainly focus on character-level, ignoring the long-form textual coherence and contextual dependencies embedded in complete divination charges. Recently, the powerful visual perception capabilities of multimodal large language models (MLLMs) have opened new possibilities for OBI information processing. In this work, we introduce S-OBI, a novel benchmark for evaluating MLLMs in Sentence-level OBI understanding. Instead of using noisy and incomplete rubbings as the visual input, S-OBI synthesizes clear and standardized sentence-level OBI instances through glyph substitution and composition. According to 95 original rubbings with translations that have been identified, corrected, and verified by experts, we replace characters in the original rubbings with corresponding clean glyph samples sourced from existing OBI datasets while preserving the overall inscriptional structure and semantic organization. This mitigates the influence of low-level distortions and enables a more focused evaluation of sentence-level OBI understanding. Based on this, we design semantic matching, semantic slot extraction, and contextual reasoning tasks and obtain 695 question-answer pairs. Experiments reveal the inferiority of contemporary MLLMs on sentence-level OBI understanding. In particular, visual perception errors in unmasked regions propagate through the reasoning chain, leading to erroneous predictions for masked characters, which indicates that sentence-level OBI understanding in current models remains strongly dependent on character-level recognition. Overall, S-OBI provides a diagnostic benchmark for evaluating whether MLLMs can move beyond isolated character recognition toward structured inscription-level understanding.

---


### 35. [HealthAgentBench: A Unified Benchmark Suite of Realistic Agentic Healthcare Environments for Challenging Frontier AI Agents](https://arxiv.org/abs/2606.31179)

**<font color=#1a73e8>作者：</font>** Qianchu Liu, Sheng Zhang, Guanghui Qin 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI agents become increasingly capable of complex, long-horizon reasoning, rigorous and holistic evaluation is essential for measuring progress toward real-world healthcare applications. We introduce HealthAgentBench, a suite of 54 agentic healthcare tasks across 7 categories each with its unique environment. The benchmark suite spans diverse workflows throughout the patient journey and a broad range of modalities. Each task is designed to replicate an end-to-end clinical workflow: given minimal instructions, an agent must explore raw healthcare data, operate within a complex environment, and execute multi-step solutions that go beyond naive prompting. A final task success rate is reported to provide a single, interpretable metric for HealthAgentBench overall performance for each agent. Evaluating frontier agents on HealthAgentBench, we find that overall task success rate remains low, underscoring the difficulty of the suite. The strongest and the most cost effective agent, Codex GPT-5.5, achieves only approximately 42% success rate. Beyond aggregate performance, HealthAgentBench reveals nuanced strengths and weaknesses across task categories. Frontier agents show promise in automatically developing research modeling pipelines over EHR data, but medical imaging remains especially challenging, particularly for Claude Code models, while Codex GPT-5.5 shows emerging capability. Tasks that combine large search spaces with compositional reasoning requirements remain difficult for all current agents. Together, these results suggest that HealthAgentBench provides a challenging and realistic benchmark with substantial room for future progress. We release our benchmark at this https URL.

---


### 36. [Learning to Deny: Action Denial in Multimodal Large Language Models](https://arxiv.org/abs/2606.31187)

**<font color=#1a73e8>作者：</font>** Raiyaan Abdullah, Shehreen Azad, Yogesh Singh Rawat  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have rapidly advanced video understanding, achieving strong zero-shot and few-shot recognition across standard benchmarks. Yet their ability to deny an action by recognizing when an activity is not happening despite strong contextual cues remains largely unexplored. We introduce UCF101-AD, a large-scale benchmark consisting of paired Action-Presence and Action-Denial clips, designed to evaluate this capacity for denial. Each negative video in UCF101-AD preserves the same contextual and motion cues, including persons, objects, and locations, as its positive counterpart, but the defining action itself is explicitly absent. Evaluating 20 state-of-the-art MLLMs reveals a consistent failure: models that exceed 85% accuracy on the positive action classes collapse below 50% on their action-denial counterparts, indicating a strong inclination to affirm plausible actions rather than verify that they truly occur. This exposes a critical blind spot in modern video understanding: the inability to reason causally about whether a motion actually happens. To probe this issue, we explore a causal graph formulation, CausalAct, which expresses scene structure through natural-language prompts linking context, interaction, and motion. Incorporating such causal cues substantially reduces false positives, demonstrating that denial is a learnable reasoning skill. UCF101-AD provides a new lens for diagnosing and improving causal reasoning in multimodal models. Dataset and relevant code: this https URL.

---


### 37. [Agentic RAG-VLM: Affordance-Aware Retrieval-Augmented Generation with Self-Reflective Planning for Robotic Grasping](https://arxiv.org/abs/2606.31200)

**<font color=#1a73e8>作者：</font>** Tao Chen, Lizheng Liu, Jiaxu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generalizable robotic grasping in cluttered environments is essential for deploying manipulators in unstructured human spaces, yet existing VLM-based methods rely on visual similarity for object matching, neglecting physical affordances such as handle graspability and material fragility, and operate open-loop without spatial reasoning or failure recovery, limiting their effectiveness when objects are densely packed or physically diverse. We present Agentic RAG-VLM, a unified framework that bridges VLM-based semantic understanding and physically grounded grasp execution by integrating retrieval-augmented generation (RAG) with vision-language models (VLMs) and agentic self-reflective planning. Agentic RAG-VLM introduces three tightly coupled components: (1) a Hierarchical Affordance-Aware RAG (HAA-RAG) that encodes four-dimensional affordance descriptors, including type, material, fragility, and graspable region, and retrieves strategies by functional affordance compatibility rather than visual appearance; (2) a Scene Graph Constraint Reasoner that constructs spatial relationship graphs from VLM perception and translates proximity, occlusion, and support constraints into concrete grasp parameter adjustments; and (3) an Agentic Self-Reflective Pipeline with a 14-type failure taxonomy and three-level adaptive retry for closed-loop grasp refinement. Evaluated on a 12-task benchmark spanning single-grasp, interactive, and long-horizon scenarios with 360 trials per configuration, Agentic RAG-VLM achieves 78.3 percent overall success, a 53.3 percentage-point absolute gain over VLM-only baselines, demonstrating that affordance-aware retrieval, scene graph reasoning, and agentic recovery are jointly essential for robust manipulation.

---


### 38. [Probing Memorization of Tabular In-Context Learning](https://arxiv.org/abs/2606.31208)

**<font color=#1a73e8>作者：</font>** Francesco Capano, Jonas Böhler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large tabular models (LTMs), i.e., tabular foundation models leveraging in-context learning (ICL), achieve state-of-the-art performance on tabular tasks. While LLMs are known to unintentionally memorize training data, the memorization dynamics of LTMs remain largely unexplored. We investigate the potential for parametric memorization in tabular ICL. We introduce ICLMEM, a probing framework designed to separate context-based predictions from parametric memorization. Our zero-information multiple-choice context strips away valid contextual patterns to force the model to fall back on its parametric memory. Our controlled fine-tuning setup establishes membership ground truth and accounts for common pitfalls, e.g., distribution shift, feature contamination, base-rate fallacy, and the pre-trained base model acts as reference to calibrate for sample difficulty. Our controlled evaluation on a leading real-world-trained LTM detects moderate memorization signals in 8 out of 10 tasks ($\text{AUC}$ up to $0.67$ and TPR at $1\%$ FPR $>0.1$). Notably, memorization signals are strongest for low-cardinality and binary tasks. However, they largely vanish under realistic training conditions. Our findings show LTM memorization signals under specific circumstances (single-task fine-tuning with fixed samples across many epochs and small query size). To protect sensitive data, appropriate measures must be taken, which we discuss.

---


### 39. [Long-term Traffic Simulation via Structured Autoregressive Modeling](https://arxiv.org/abs/2606.31209)

**<font color=#1a73e8>作者：</font>** Lingyu Xiao, Zexin Feng, Xintao Yan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive traffic simulation is a vital world model for autonomous driving. A central challenge in long-horizon simulation is modeling sustained multi-agent interactions, which is further exacerbated by dynamic token cardinality as agents continuously enter and exit the scene. In this work, we propose that the solution lies in the synergy between the architectural inductive biases and statistical priors of large-scale sequence models, e.g., Large Language Models (LLMs). Our probing experiments reveal that the transferability of attention mechanisms and the distributional consistency between motion tokens and natural language enable small-scale, heavily frozen LLMs to rapidly adapt to traffic modeling. Building on this insight, we introduce RosettaSim, a unified framework that projects scene topology, agent states, and spawning intents into a structured autoregressive stream with variable length, achieving both strong short-term accuracy and stable long-horizon simulation fidelity. Furthermore, evaluating extended rollouts presents yet another hurdle, as one-to-one agent correspondence inevitably fades over time. To address this, we introduce Retrieval-based Traffic Evaluation (RTE), which retrieves semantically similar real-world scenarios as context-aware reference anchors. Experiments on the Waymo Open Sim Agent Challenge (WOSAC) demonstrate that RosettaSim achieves state-of-the-art performance in both short- and long-term simulation. Furthermore, RTE exhibits a stronger correlation with standard metrics ($r=0.83$) than existing approaches ($r=0.74$), indicating improved alignment with long-horizon simulation fidelity.

---


### 40. [AA: A Multi-view Multimodal Dataset for Screen-based Gaze Estimation](https://arxiv.org/abs/2606.31211)

**<font color=#1a73e8>作者：</font>** Chang Liu, Jiaqi Liu, Zhoutong Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present AA, a multi-view multimodal dataset for screen-based gaze estimation. The dataset captures synchronized facial observations from eight fixed screen-mounted cameras and two additional side-view cameras, paired with precise screen-space gaze targets collected under controlled fixation conditions. Each sample contains multi-view face observations together with structured facial region crops, enabling multimodal learning from both global and local visual cues. Unlike existing single-view gaze datasets, AA provides multi-view coverage from both screen-mounted and side-mounted perspectives, enabling more robust modeling under viewpoint variation and occlusion. The dataset includes subject-independent evaluation splits and a standardized data processing pipeline to support reproducible research in gaze estimation.

---


### 41. [Can LLMs Imagine Moral Alternatives Beyond Binary Dilemmas?](https://arxiv.org/abs/2606.31213)

**<font color=#1a73e8>作者：</font>** Jongchan Choi, Nari Yang, Sung Soo Park 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly deployed as moral advisors and agents, they need to address dilemmas between two competing values. However, existing research on LLMs with moral dilemmas overlooks a central aspect of human moral cognition: the ability to imagine alternatives that move beyond the given options. We introduce MoralAltDataset, a dataset of 307 moral dilemmas spanning narrative Advisor dilemmas and AI-facing Agent dilemmas, each augmented with compromise and reframed alternatives. We first examine whether humans and LLMs shift their judgments when such alternatives are introduced. Across 15 LLMs, we find that compromise alternatives are often preferred over either original option, substantially reshaping moral choice. We then evaluate the quality of LLM-generated alternatives against human-authored ones using pairwise preference and expert-based criteria. Results show that LLM-generated alternatives are often preferred and better satisfy fine-grained structural and ethical criteria, while revealing trade-offs between structural quality and practical feasibility.

---


### 42. [Agentic-Ideation: Sample Efficient Agentic Trajectories Synthesis for Scientific Ideation Agents](https://arxiv.org/abs/2606.31229)

**<font color=#1a73e8>作者：</font>** Keyu Zhao, Lingyan Kong, Fengli Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ideation plays a pivotal role in scientific discovery. Recent LLM, especially AI Scientist systems, show promising potential for automated ideation. However, existing approaches predominantly rely on pre-defined agentic workflows. This constraint severely limits the flexibility required to navigate the vast search space of scientific literature and the complex action space of research reasoning. Recently, training Agentic LLMs has emerged as a promising direction, offering flexible reasoning frameworks and the capability for autonomous tool utilization. However, there remains a non-trivial challenge: applying previous agentic data synthesis methods to scientific ideation suffers from prohibitively high data synthesis cost. To bridge this gap, we propose Agentic-Ideation, a novel framework comprising an automated trajectory synthesis pipeline and a specialized agentic LLM trained for scientific ideation. Specifically, we first define a comprehensive tool space incorporating three external tools and three cognitive tools. Then we introduce an Oracle-Guided Data Synthesis strategy. By leveraging a reference idea as oracle guidance, this approach steers the multi-agent system to efficiently reconstruct the logical reasoning and tool invocation paths, transforming aimless trial-and-error into directed trajectory generation. Finally, we train the agent on these synthesized trajectories, employing a masking strategy on tool execution results. This ensures the model focuses on decision-making logic without interference from external feedback. Experimental results demonstrate that our method outperforms the SOTA workflow-based baseline by \textbf{11.91\%} in overall quality. Furthermore, our approach improves the sample efficiency of high-quality data synthesis by \textbf{over 10$\times$}.

---


### 43. [Delta-JEPA: Learning Action-Sensitive World Models via Latent Difference Decoding](https://arxiv.org/abs/2606.31232)

**<font color=#1a73e8>作者：</font>** Zhenghao Zhang, Yuanxiang Wang, Zhenyu Guan 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning visual world models for planning requires compact latent dynamics that remain sensitive to actions, yet reconstruction-free joint-embedding objectives can collapse to action-insensitive representations. We propose Delta-JEPA, an end-to-end reconstruction-free world model that augments latent forward prediction with a Latent Difference Action Decoder (LDAD). Unlike inverse decoders that infer actions from concatenated endpoint embeddings, LDAD reconstructs the executed action from the latent displacement between consecutive observations. This displacement-level supervision directly regularizes transition geometry: adjacent embeddings cannot collapse without losing action information, and different actions are encouraged to induce distinguishable latent changes for rollout-based planning. Delta-JEPA uses only latent prediction and action reconstruction, avoiding pixel reconstruction and distribution-matching regularizers. Across four visual continuous-control tasks, Delta-JEPA improves planning over JEPA-based and representation-learning world model baselines. Ablations show that displacement-based action decoding is consistently more effective than endpoint concatenation, and action-sensitivity analyses show clearer action-conditioned latent responses. These results indicate that supervising latent differences is a simple and effective mechanism for collapse-resistant and action-sensitive world model learning.

---


### 44. [HyperVLP: Enhancing Hierarchical Surgical Video-Language Pre-training in Hyperbolic Space](https://arxiv.org/abs/2606.31245)

**<font color=#1a73e8>作者：</font>** Yaojun Hu, Kun Yuan, Nassir Navab 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical vision-language foundation models typically adopt educational materials, such as surgical lecture videos, to transfer surgical knowledge encoded in language into visual representations. These knowledge are multi-dimensional and hierarchical: fine-grained action cues appear in narration, mid-level key steps are summarized in subsection headings, and global procedural context, such as patient history and surgical strategy, is described in abstract texts. Prior work largely collapses these heterogeneous signals into a single flat embedding space, implicitly assuming independence across hierarchy levels. However, this is suboptimal because it ignores cross-level semantic containment, e.g., actions belong to steps, steps compose phases, weakens long-range dependency modeling. To this end, we propose a hyperbolic surgical video-language pre-training framework that explicitly preserves the hierarchical structure by mitigating structural false negatives induced by procedural context and enforcing semantic consistency between parent phases and their constituent child steps. Extensive experiments on multiple surgical benchmarks show consistent gains in zero- and few-shot phase recognition across procedures and institutions.

---


### 45. [Probing Stylistic Appropriation using Large Language Models: An Evaluation Framework for Copyright Infringement under EU Law](https://arxiv.org/abs/2606.31250)

**<font color=#1a73e8>作者：</font>** Noah Scharrenberg, Chang Sun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLM) trained on web-scale corpora generate output that may infringe copyright, yet existing technical safeguards focus narrowly on verbatim memorisation. EU copyright doctrine applies a broader standards: substantial similarity, which extends to stylistic choices, narrative structure, and creative elaboration. This mismatch between what current methods detect and what the law protects leaves a significant compliance gap. We introduce PSALM, an LLM-as-a-judge framework that operationalises EU copyright doctrine through ten evaluators assessing computational overlap, stylistic dimensions (writing style, narrative voice), content dimensions (character, plot, scene, world building), and statutory exceptions (parody, pastiche, quotation, scènes à faire). Applying PSALM to Llama~3.2 models fine-tuned on translated historical Dutch literary works, we find that: 1) instruction-tuned models exhibit non-trivial baseline stylistic similarity prior to corpus exposure; 2) fine-tuning induces systematic stylistic appropriation across all infringement-relevant dimensions, extending beyond verbatim memorisation to abstract narrative patterns; 3) Negative Preference Optimisation unlearning substantially reduces similarity but leaves detectable residual stylistic patterns. These findings indicate that safeguards targeting literal copying alone are insufficient to mitigate broader copyright risks. PSALM provides infrastructure for auditable, legally informed compliance evaluation, though the relationship between automated similarity scores and infringement determinations requires validation by legal experts. This work bridges qualitative legal standards and quantitative technical measurement, exposing fundamental tensions between generative AI and EU intellectual property law.

---


### 46. [Embodied CAD: Solver-Grounded LLM Agents for Parametric B-Rep Assembly Modeling](https://arxiv.org/abs/2606.31252)

**<font color=#1a73e8>作者：</font>** Fumin Liu, Haoyu Zhou, Fei Hao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can write plausible CAD scripts, but reliable industrial CAD modeling requires more than syntactically valid code: every feature, placement, and assembly relation must be accepted by an exact geometric kernel while remaining editable as parametric boundary representation geometry. We present Embodied CAD, solver-grounded LLM agents for parametric B-Rep assembly modeling. Instead of generating a complete script in one pass, the agent iteratively selects actions from a stratified L0-L4 CAD skill library, resolves them into typed geometric operations, executes them in a CAD backend, and uses solver feedback to plan, repair, and learn. The framework combines action grammar constraints, deterministic parameter resolution, and solver-derived rewards for supervised warm-up and GRPO-style refinement. We evaluate Embodied CAD on multi-step mechanical, industrial equipment, and mold-oriented assembly tasks using solver-aligned metrics: executable rate, skill accuracy, operation-family accuracy, exact policy accuracy, and task completion success. The results show that solver-grounded planning executes all strong-planner workflows in the current benchmark, while learned controllers reach high executable rates and expose the remaining gap between valid tool calls and exact long-horizon policy prediction.

---


### 47. [Learning from Failure: Inference-Time Self-Improvement for Computer-Use Agents](https://arxiv.org/abs/2606.31270)

**<font color=#1a73e8>作者：</font>** Xueqiao Sun, Xiaohan Wang, Ludwig Schmidt 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer-use agents, which leverage multimodal large language models (MLLMs) to operate computers and complete tasks, have attracted significant attention for their utility and versatility. A major challenge in developing these agents is collecting large-scale, high-quality trajectories. The standard approach generates synthetic data through a self-improving loop: an agent is placed in a verifiable environment and iteratively fine-tuned on its successful trajectories. Despite its effectiveness, this paradigm exploits only successful trajectories and discards the failed ones, even though failures carry rich information about a model's weaknesses. In this work, we explore a complementary failure-driven self-improvement loop, a data-centric paradigm that turns failed trajectories into agent improvements. Specifically, we employ an LLM to diagnose failure modes, propose inference-time solutions, and generate code patches -- lightly verified by humans -- that upgrade the agent. We validate this approach with the state-of-the-art OpenCUA-72B model on the OSWorld benchmark, improving the success rate from 42.3% to 48.9%, a gain of 6.6 percentage points, without any additional training cost and with only modest inference overhead. Our results demonstrate that failure-driven self-improvement is a viable complement to success-based pipelines, enabling more efficient agent improvement.

---


### 48. [Spatial Reasoning via Modality Switching Between Language and Symbolic Representation](https://arxiv.org/abs/2606.31285)

**<font color=#1a73e8>作者：</font>** Shreya Rajpal, Tanawan Premsri, Parisa Kordjamshidi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human reasoning is inherently multimodal: when problems become difficult, we rarely think in words alone. We often externalize our reasoning by sketching diagrams or drawing grids to understand the underlying conceptual structure and avoid mistakes. Building on this premise, our research investigates: (a) whether grounding multi-hop textual-spatial stories into geometry-aware modalities, such as layouts or grids, improves reasoning compared to natural language-based inference; and (b) whether a model can decide when to rely on natural language reasoning and when to switch to a structured modality. We address these questions by introducing a switching metric based on trustworthiness and complexity signals, which estimates when grounding a spatial story into structure is likely to improve performance. This takes a first step toward principled modality selection in Large Language Model (LLM) reasoning. Across our settings, switching from natural language-based reasoning to a grid-based representation improves LLM performance by up to 42\%, highlighting the importance of modality choice in shaping reasoning outcomes.

---


### 49. [When the Database Fails: Prompting LLM Dialogue Agents for Safe Recovery in Task-Oriented Dialogue](https://arxiv.org/abs/2606.31307)

**<font color=#1a73e8>作者：</font>** Mohammad Alijanpour Shalmani, Alale Rezvani Boroujeni, Jiann Shiun Yuan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models used in task-oriented dialogue often produce fluent but unsafe responses when backend database calls fail, return empty results, or surface mismatched information, inventing venues, confirmations, or booking details not grounded in the database. We study a lightweight prompting-based recovery approach that improves robustness without retraining or additional model calls. We compare three response strategies, including a guided recovery prompt conditioned on structured database status, across six open-weight model families (DeepSeek-R1, Gemma-2, Llama-3, Mistral, Phi-3, and Qwen-2.5) and four database conditions: empty result, wrong-domain retrieval, API error, and clean retrieval. Using fault-injected benchmarks built on two structurally different datasets, MultiWOZ 2.2 (5 domains) and SGD (20 domains), we find that naive agents hallucinate on 30.5% of failure turns on MultiWOZ and 20.9% on SGD. Our Guided-Retry strategy reduces hallucination by 50% on MultiWOZ (30.5 to 15.3%) and by 42% on SGD (20.9 to 12.2%) without retraining. However, residual hallucination remains substantial (6-37% across models), with wrong-domain failures the hardest case. Results are consistent across both datasets and all six model families, and human annotation shows substantial agreement while supporting the validity of the automatic commitment-safety metric.

---


### 50. [Benchmarking Large Language Models on Floating-Point Error Classification](https://arxiv.org/abs/2606.31308)

**<font color=#1a73e8>作者：</font>** Lisa Taldir, Muhammad Ahmad Saeed, David Defour 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper investigates the capability of Large Language Models (LLMs) to detect and classify floating-point errors statically in software code. We introduce InterFLOPBench, a benchmark of 90 C kernels with 1 130 test samples designed to evaluate LLMs across six categories of floating-point error: cancellation, comparison, division by zero, overflow, underflow and NaN, compared across 14 LLMs. The evaluation framework treats floating-point error detection as a multi-label classification problem and employs the F1-score metric to measure performance. Results demonstrate that latest models (Qwen 3 32b, Gemini 2.5 Flash, Phi 4 Reasoning, DeepSeek R1T2, and gpt-oss 20b and 120b) achieve a performance greater than 0.88 overall F1-score. Performance varies between error categories, between explicit operations such as division by zero (Average F1-score: 0.8479) and more subtle numerical phenomena such as underflow (Average F1-score: 0.6059) and cancellation (Average F1-score: 0.6164).

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-121](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
