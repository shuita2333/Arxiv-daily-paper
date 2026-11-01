# 🧠 大模型相关研究 | 2026年11月02日

> 本类共 **353** 篇论文：已确认 **335** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

---

### 101. [Pronunciation-Supervised Text-to-Speech for Irish (Gaeilge)](https://arxiv.org/abs/2610.38384)

**<font color=#1a73e8>作者：</font>** William Lane  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech technology for Irish must be built from very little transcribed speech, yet the language's pronunciation is thoroughly documented in dictionaries and dialect descriptions. We ask whether that documentation can supervise the adaptation of a large pretrained text-to-speech model to a language it was never trained on. We adapt Qwen3-TTS to Irish using 12.8 hours of crowdsourced Common Voice speech, correcting two defects in the vendor fine-tuning script that training loss does not reveal (Appendix A), and reach character error rate (CER) 0.225 on held-out cross-corpus text, against 0.397 for an exhaustively tuned from-scratch system and 0.437 for zero-shot cloning. We then compile the Wiktionary pronunciation record into a lexicon and a phoneme critic, and use that critic as the verifier in one round of rejection fine-tuning: CER 0.159 cross-corpus and 0.067 in-domain, with the voice still anonymous across all 202 training speakers. The same critic explains why the voice cannot yet be steered to a minority dialect: 229 of 12,311 training clips lean Ulster against 8,451 Munster. Pronunciation documentation, converted into a verifier, is a practical lever for low-resource speech synthesis, and a way to measure what the available data cannot support.

---


### 102. [Visually Irrelevant Hallucinations in Medical Vision-Language Models](https://arxiv.org/abs/2610.38389)

**<font color=#1a73e8>作者：</font>** Ke Zou, Nan Zhou, Tao Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models (VLMs) show strong performance in radiology report generation (RRG) and medical visual question answering (Med-VQA), producing free-form clinical descriptions and answers from medical images. However, they may generate clinically meaningful statements that lack visual evidence or contradict image content. We refer to these errors as visually irrelevant hallucinations and investigate them at the phrase level. We propose CLEAR (Counterfactual Localized Evaluation of Alignment and Response), a model-agnostic post-hoc framework for phrase-level hallucination risk estimation. CLEAR decomposes generated responses into visually assessable clinical phrases. For each phrase, phrase-conditioned grounding identifies a candidate visual region, which is selectively perturbed by a localized counterfactual intervention. CLEAR characterizes the intervention using two complementary auditing cues: response cues, capturing semantic and clinically meaningful changes in the generated response, and alignment cues, measuring changes in image-phrase compatibility. These cues are normalized and jointly modeled to estimate phrase-level hallucination risk. Across four datasets spanning RRG and Med-VQA, CLEAR outperforms state-of-the-art hallucination detection baselines across multiple medical and general-purpose VLMs. On MIMIC-CXR, CLEAR improves AUPRC from 85.10% to 90.23%. Its effectiveness is further validated on a GT-derived controlled VIH benchmark. These results establish visually irrelevant hallucination as an important fine-grained reliability failure mode in medical VLMs and demonstrate the value of model-agnostic visual-support auditing for more trustworthy multimodal clinical generation.

---


### 103. [SCOPE: Selective Critical-Step On-Policy Self-Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2610.38391)

**<font color=#1a73e8>作者：</font>** Qirui Liu, Wei Cao, Yu Mi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Outcome-based reinforcement learning provides coarse supervision for long-horizon LLM agents: failed trajectories may contain correct steps, while successful trajectories can contain errors. Trajectory-level skills can also shift teacher preferences at unrelated steps, introducing off-target distillation signals. We introduce SCOPE, a framework for Selective Critical-Step On-Policy Self-Distillation. After a supervised warm-up, the policy analyzes its own trajectories, generates step-specific hindsight skills, and distills their guidance only at selected error steps. A bounded signed teacher-student coefficient stabilizes auxiliary updates while preserving positive reinforcement and negative correction. A success-relative pairwise length reward further encourages efficient task completion. Experiments on ALFWorld and WebShop demonstrate consistent improvements across multiple model backbones. With Qwen2.5-3B, SCOPE achieves 97.7% success on ALFWorld and 85.2% on WebShop, outperforming SEED by 5.9 and 6.3 percentage points, respectively. On unseen ALFWorld tasks, SCOPE reaches 89.6% success, improving over GRPO by 23.2 percentage points with 46.7% fewer interactions. Scaling to Qwen3-32B, SCOPE achieves 99.2% success on seen ALFWorld tasks and 94.0% on unseen tasks.

---


### 104. [Masked Erosion: How Acceptance Gates Lose Redundant Safeguards in Self-Improving Agents](https://arxiv.org/abs/2610.38392)

**<font color=#1a73e8>作者：</font>** Hau-Sing So, Daixian Liu, Weicai Long  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-improving LLM agents edit their own harness, the prompts and rules around a fixed model, and keep an edit only if an acceptance gate scores it higher on a batch of tasks. Such a gate sees what the harness does under the current model, not what it would still prevent if one safeguard failed. When safeguards overlap, deleting one is masked: the others still block the harm, so the gate decides on task success alone and redundancy erodes unseen. We measure harm for every subset of four written safeguards in two agent environments and run 411 improvement loops under ten gate rules, mostly as controlled deletion experiments, plus three runs of the GEPA optimizer. A deletion behind another working safeguard adds almost no observable harm. A paired significance test blocks deletions that pass by chance but not deletions that genuinely raise task success, and a larger evaluation batch lets it delete cheaper safeguards: at the same cost, 20-task batches kept every harness protected while 40-task batches lost all six. Large harm audits prevent exposure but not the loss of depth, which turns into harm when the harness is reused with a weaker model. GEPA kept every safety rule verbatim, yet two of its three final harnesses misused credentials under a weaker model. A statistical model frozen before the runs predicts where each gate's protection breaks as safeguard cost and batch size change, and freezing safety text or auditing one-layer ablations preserves depth.

---


### 105. [Agent Transfer Protocol: Server-Mediated Agent-to-Agent Communication Architecture for the Agentic Web](https://arxiv.org/abs/2610.38398)

**<font color=#1a73e8>作者：</font>** Yuqi Qiu, Zuyao Xu, Lu Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Agentic Web needs to support continuous collaboration among agents from different organizations. These collaborative relationships may span multiple tasks, network connections and execution instances. Such interactions require stable communication entries, message reception when instances are offline, and source verification after delayed reading. How to organize these responsibilities so that cross domain communication does not depend on specific execution instances being continuously online is a key issue for building long term agent interaction infrastructure. We propose ATP (Agent Transfer Protocol), a cross organization agent communication protocol adopting a domain mediated architecture. In this architecture, administrative domains maintain stable addresses and receiving entries for logical agents. The domain servers of both parties continuously undertake cross domain transmission. The receiving domain verifies and saves messages for execution instances to read later. The sending domain signs the complete message envelope. This allows the receiving instance to independently reverify the domain source and content integrity after the original connection ends, provided the original verification public key is still trusted and obtainable. We implemented an ATP prototype and evaluated it through a controlled cross organization LLM agent workflow, mechanism checks and latency measurements. The workflow completed subsequent business processing after instances went offline or were replaced. The independent verifier successfully verified the domain source and content integrity of saved messages. Latency measurements further quantified the communication and processing overhead introduced by the continuous mediation of domain servers.

---


### 106. [LLMs as Judges and Examinees for Medical Item Difficulty Prediction](https://arxiv.org/abs/2610.38402)

**<font color=#1a73e8>作者：</font>** Xiaomeng Xiong, Marcus Walker, Yanlin Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Predicting medical item difficulty from item text alone remains challenging. Prior work has largely relied on linguistic features or text representations derived from general-purpose and domain-specific language models, but predictive performance has remained modest. This study takes a different approach by using difficulty-related signals that emerge when open-weight large language models (LLMs) interact with test items. Using USMLE and PANCE medical licensure examination items, we examined LLMs in two roles. As judges, the models provided absolute difficulty ratings and pairwise difficulty comparisons. As simulated examinees, they generated response-based signals including correctness, keyed-option probability, response entropy, and the probability margin between the top two options. We then combined the strongest judgment and response signals with baseline item features in downstream prediction models. Pairwise difficulty judgment was the most consistent individual LLM signal across both datasets, while simulated-examinee signals and absolute judgments provided complementary information in some feature combinations. The best configurations reached a Spearman correlation of $\rho$ = .447 on USMLE, exceeding the best system in the 2024 BEA shared task ($\rho$ = .25), and $\rho$ = .494 on PANCE. These results were comparable to direct absolute judgments from the proprietary frontier model Claude Opus 5 ($\rho$ = .443 and .488, respectively). Overall, judgment and response signals from open-weight LLMs captured difficulty-related information beyond text representations. Because these models can be deployed locally, the approach offers a practical option for predicting the difficulty of unreleased or high-security test items.

---


### 107. [Holistic Diversity Management in LLM-Guided Evolutionary Search](https://arxiv.org/abs/2610.38407)

**<font color=#1a73e8>作者：</font>** Seockbean Song, Youngsik Yoon, Sungjae Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-guided evolutionary search iteratively selects existing programs, uses LLMs as mutation operators to generate a new program, and evaluates it to guide subsequent search. To preserve diversity and reduce the risk of premature convergence, it often adopts the island model, in which groups of programs, called islands, evolve separately. However, this structure alone does not guarantee distinct search directions, as islands may start from similar programs or converge toward similar solutions during evolution. This suggests that diversity must be considered throughout the search process, from initializing islands with distinct programs to developing island trajectories and sharing discoveries across islands. To this end, we propose HoliDivEvolve , a holistic approach to establishing and effectively utilizing island diversity throughout evolutionary search. Specifically, we introduce diverse initialization to establish different initial programs, trajectory adaptive island selection to allocate computation based on current score, recent growth, and the remaining search budget, and growth adaptive migration to share alternative ideas across islands. Experiments across diverse benchmarks show that HoliDivEvolve achieves competitive performance on most evaluated tasks. We further conduct controlled analyses to examine how our design choices affect search behavior and final performance.

---


### 108. [Deeper Backpropagation or More Updates? Training Looped Language Models Across Budgets](https://arxiv.org/abs/2610.38422)

**<font color=#1a73e8>作者：</font>** Jiarun Shen, Xiao Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Repeating transformer layers can improve language model performance without adding parameters. However, the added computational depth increases both forward and backward computation costs during training. Training such models requires choosing a backward window that controls how many final layer repetitions retain gradients during backpropagation. Longer windows improve per-token learning efficiency but increase per-update cost, while shorter windows reduce per-update cost but sacrifice per-token efficiency. Understanding which window performs better requires examining different training budgets. Prior work compares backward windows across computational budgets. When training budgets increase, it remains unclear whether the same window continues to perform best. We measure how the relative performance of two windows shifts as training budgets grow. Our method isolates per-token efficiency by training both windows on identical data, and compares complete training recipes at approximately equal training time at each budget. Results show that shorter windows lose much of their advantage as budgets grow. Controlled experiments show that both benefits decrease at larger budgets, with a greater decline in the benefit of extended training. Backward window comparisons depend on the available budget, and the preferred window among the tested candidates can change as the budget grows.

---


### 109. [Does Chain-of-Thought Reliance Follow a Scaling Law?Larger Models Follow Their Steps More, Independent of Post-Training](https://arxiv.org/abs/2610.38433)

**<font color=#1a73e8>作者：</font>** Esther Xin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Monitoring a model's chain of thought (CoT) is useful for safety only if the final answer depends on the written steps. Prior measurements use natural tasks where true reasoning is unknown. We measure it against an exact ground truth on a synthetic box-swap task where every intermediate state is known. We replace one step inside a model's own chain with a wrong but valid state and check whether the answer follows the edit. We evaluate 25 open-weight models--Qwen3 (0.6B-14B, base and post-trained), Gemma 3 (1B-12B), Llama 3 (1B-8B), and 8 OLMo 2 checkpoints--on 7,200 items each. We find five results: (1) Reliance rises with size and saturates. In Qwen3, answer reliance rises from 16-18% at 0.6B to 97-100% at 14B; a logistic in log N fits well (R^2 = 0.89), and Gemma 3 and Llama 3 follow this trend. (2) Capability is the main driver. Across all models, reliance and step accuracy correlate at r = 0.99; equally capable models are equally reliant, regardless of family. (3) Size still matters at matched correctness. On problems solved correctly before the edit, reliance increases with size among capable models (rho = 0.80, p = 0.002). (4) Post-training does not change reliance. Base and post-trained Qwen3 differ by at most 0.03 from 4B upward; a large gap at 1.7B matches a large capability gap. (5) No model up to 14B solves the task internally. Without written steps, every capable model is at chance once a problem has four or more swaps. OLMo 2 checkpoints never become capable, making the training-token axis a limitation. On tasks requiring step-by-step computation, scale makes the chain of thought more load-bearing, supporting CoT monitoring in this regime.

---


### 110. [RoleFUZZER: User-Behaviour Fuzzing for Role-Specification Adherence in Large Language Models](https://arxiv.org/abs/2610.38438)

**<font color=#1a73e8>作者：</font>** Kshitish Ghate, Michael Saxon, Tadayoshi Kohno 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are often conditioned into specific roles such as tutors, interviewers, or agents acting for an organisation, through system prompts that specify how they should behave. The extent to which they can actually adhere to these role specifications under multi-turn interactions with realistic and potentially problematic users is understudied. To address this, we propose user behaviour fuzzing, a guided search over plausible user behaviours that can lead a model to violate its role specification, and introduce RoleFUZZER, a framework that adapts coverage-guided fuzzing from software testing to operationalise the search. RoleFUZZER constructs scenarios guided by a user-behaviour coverage grid that crosses a grounded taxonomy of user interaction types and the role specification of the model under test i.e. what is under pressure. With RoleFUZZER, we evaluate LLMs across five role specifications, including tutor, financial advisor, AI interviewer, antagonistic roleplay character, and web agent under organisational policies. Across simulated and validated conversations in 15 campaigns, the framework reaches >= 89% coverage of the 64-cell behaviour grid for every model and role tested, and surfaces specification-grounded failure patterns. At an equal budget of conversations, removing the RoleFUZZER grid and asking an LLM to generate specification targeting users free-form lowers coverage to 39-69% with fewer kinds of violations. The same specification can also fail in opposite directions. For e.g., on the antagonist, open-weight target models override the player's safety signals, while Claude Haiku 4.5 breaks character instead. RoleFUZZER offers a tractable way to uncover vulnerabilities in LLMs across role specifications by testing diverse user behaviours that are likely to violate them.

---


### 111. [Predict the Reward, Not the World: World Reward Models for ML Agents](https://arxiv.org/abs/2610.38439)

**<font color=#1a73e8>作者：</font>** Yuxiao Lee, Zherui Yang, Fan Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Search-based machine-learning (ML) agents improve a solution by writing candidate programs, executing them, and keeping the best. Execution gives the search reliable feedback, but a single run can take hours, and most runs end in programs the agent discards. Recent agents try to save these runs by letting a large language model act as a world model that predicts how each program would perform. However, a wrong prediction feeds the search false information. We argue that an agent does not need to predict the outcome of execution, only the decision that execution would support. We propose World Reward Models (WRMs), which learn from real execution results to choose directly which candidate will perform better, without predicting any intermediate outcome. We prove that a selector which predicts execution from the same inputs cannot outperform the best direct selector, that predicted outcomes add an error which can make a likelihood-trained world model prefer the worse program on every instance, and that cross-entropy on executed winners drives a WRM toward the optimum. Our WRM, ForeCritic, adapts a 9B typed decision model to 5k executed program pairs. On 12,438 held-out pairs from 26 ML tasks, it picks the better program 79.4% of the time, while general-purpose LLM judges reach 53--62%, and its probabilities are calibrated. Inside AIDE, ML-Master, and ForeAgent, it cuts mean task time by 4.4--7.5 times while keeping their mean scores within 0.01 or raising them.

---


### 112. [Benchmarking decision models against generative large language models on medical multiple-choice questions](https://arxiv.org/abs/2610.38448)

**<font color=#1a73e8>作者：</font>** Oscar Freyer, Daniel Glauert, Moritz Hofmann 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical workflows often require selecting among predefined options. We compared 13 decision models with 15 generative large language model configurations, including different reasoning settings, using 1,273 four-option MedQA questions under text-only conditions. Accuracy ranged from 67.71% to 89.08% for decision models and from 78.32% to 96.86% for generative configurations. Among the tested configurations, Mercury Decide had the lowest mean final-attempt cost (USD 0.0069 per 1,000 questions), while Clef Omni had the shortest median request duration (0.291 seconds). Decision-model probabilities distinguished correct from incorrect answers, but error rates among answers assigned probabilities of at least 0.90 ranged from 1.71% to 12.77%. Answer agreement across three runs ranged from 92.30% to 100%, while probability repeatability varied. Decision models offered resource advantages alongside lower peak accuracy; selecting models for medical workflows requires considering probability quality and repeatability together with accuracy and the resources needed to detect and correct errors.

---


### 113. [CoSTA: Co-Evolving Self-Play Timeline Agents for Complex Temporal Knowledge Graph Question Answering](https://arxiv.org/abs/2610.38450)

**<font color=#1a73e8>作者：</font>** Haikun Liu, Zhichao Yan, Shaoru Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Complex Temporal Knowledge Graph Question Answering (TKGQA) involves more than retrieving facts: the timestamp or validity interval of one fact can constrain the search for another, while multiple intervals may jointly determine the answer. Existing single-agent TKGQA methods typically investigate these facts within a single reasoning context, where evidence from different event histories can become interleaved and distractors can misdirect subsequent retrieval. Distributing investigations across agents can separate event-specific evidence into distinct contexts, but effective collaboration must still be learned because question decomposition, subtask investigation, and evidence synthesis are interdependent. To address these limitations, we propose \textbf{Co}-Evolving \textbf{S}elf-Play \textbf{T}imeline \textbf{A}gents (CoSTA), which organizes facts into navigable timelines, delegates investigations to workers, and uses a coordinator to synthesize their original timestamped observations. CoSTA initializes a shared policy through role-conditioned distillation and jointly optimizes both roles through co-evolving self-play with final-answer rewards. Across three benchmarks, CoSTA achieves state-of-the-art overall performance, with particularly strong gains on complex multi-fact questions, while its compact variants outperform the evaluated closed-source LLM agents.

---


### 114. [When Support Crosses the Line: Evaluating Ethical Boundaries in LLM-Based Mental Health Support in the Chinese Context](https://arxiv.org/abs/2610.38452)

**<font color=#1a73e8>作者：</font>** Bichen Wang, Yufeng Jin, Yixin Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly explored for mental health support, yet existing benchmarks primarily focus on supportive capabilities rather than whether models consistently adhere to professional ethical boundaries. This issue is particularly important in multi-turn interactions, where users may introduce new information or exert emotional pressure over time. We introduce MindEth-Bench, a benchmark for evaluating ethical boundary adherence in multi-turn mental health interactions. Grounded in professional ethical standards for mental health services in China, MindEth-Bench covers multiple dimensions of ethical conduct and uses Monte Carlo Tree Search (MCTS) to systematically explore interaction trajectories that stress-test model boundaries. Experiments across nine LLMs show that models that initially respond appropriately can shift toward ethical violations over extended interactions, with substantial variation across models and ethical dimensions. These results show that single-turn evaluations may overestimate the ethical reliability of LLM-based mental health support systems and highlight the need to evaluate ethical behavior throughout multi-turn interaction.

---


### 115. [Automatic Iconographic Annotation of Medieval Illuminations: Comparing Generative Vision-Language Models and Supervised Discriminative Classifiers](https://arxiv.org/abs/2610.38462)

**<font color=#1a73e8>作者：</font>** Vincent Jolivet, Lucas Terriel, Chahan Vidal-Gor{è}ne  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The large-scale digitisation of medieval manuscripts creates a growing need for automated iconographic indexing. We evaluate two complementary paradigms for this task on 9,735 full-folio images annotated with 2,333 TIMEL concepts: generative Vision-Language Models (VLM) and supervised discriminative classifiers (SDC). The VLM experiments evaluate fine-tuning, structured JSON decoding, taxonomybased candidates generation, and deterministic reranking. The discriminative experiments evaluate flat, hierarchy-aware, and patch-attention heads over a frozen DINOv3 encoder. Our results highlight key functional differences: ML-Decoder (SDC) achieves the strongest overall retrieval performance (precision@1 of 0.696, MRR of 0.806), with loss calibration (Asymmetric Loss) serving as the primary performance lever. While SDCs provide superior precision and reliability within a closed vocabulary, VLMs offer strong semantic generalization and broad taxonomic coverage, particularly through structured JSON targets and verify-calibrate reranking (hierarchical F1 of 0.559). Furthermore, model behavior strongly depends on concept abstraction: SDCs excel at perceptually grounded descriptive concepts, whereas VLMs provide useful hypotheses for complex interpretative scenes. Finally, we find that enforcing explicit hierarchy within model architectures limits coverage compared to spatial feature aggregation. Overall, rather than competing approaches, SDCs and VLMs emerge as complementary components for future hybrid indexing systems combining structured retrieval with exploratory annotation assistance. As a methodological contribution, we define the soft F1 metric to provide a taxonomy-aware evaluation that credits semantically close predictions based on lowest common ancestors.

---


### 116. [Generative AI as a Mediator in Creator Collaboration: Challenges, Design Opportunities, and Concerns](https://arxiv.org/abs/2610.38488)

**<font color=#1a73e8>作者：</font>** Hajun Kim, Jini Kim, Yunjae Josephine Choi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As Generative AI (GenAI) expands beyond individual workflows and becomes increasingly integrated intocollaborative creative work, its potential to address the fundamental challenge of building common groundamong creators with diverse expertise remains underexplored. Specifically, we lack empirical understandingof how GenAI can mediate collaboration asymmetries among heterogeneous creators. To address this gap,we conducted a multi-method study with narrative writers (N = 10) and visual designers (N = 10) in thecontext of game development. Our findings demonstrate that GenAI goes beyond individual assistance toserve as a collaborative mediator by aligning creative intent, sustaining shared understanding, and mitigatinginterpersonal friction among creators. At the same time, we highlight concerns that GenAI may reducecommunication among creators, undermine mutual trust, and reshape interpersonal dynamics and collaborativeprocesses. Based on these insights, we identify design opportunities for GenAI tools that nurture collaborativesynergy while preserving the creativity and values of human work.

---


### 117. [Leaving the Cave by Breaking the Symmetry: Identifiable Structure Can Enable Cross-Lingual Generalization](https://arxiv.org/abs/2610.38509)

**<font color=#1a73e8>作者：</font>** Frederick Riemenschneider, Anette Frank  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Why do multilingual language models generalize across languages even without shared vocabulary? The Platonic Representation Hypothesis posits that models trained on different data, objectives, and modalities converge toward a shared statistical model of reality. Extending this intuition to representations inside a single multilingual model, we propose the Relational Identifiability Hypothesis: relations in a shared world can promote entity alignment by ruling out alternative cross-lingual correspondences, making corresponding entities more likely to become directly readable without an additional transformation. We test this hypothesis in a controlled bilingual Transformer whose two token-disjoint languages describe the same modular-arithmetic world. We find that the languages can develop a shared answer subspace without aligning corresponding numbers. Cross-lingual alignment emerges selectively when the available relations constrain number correspondences: subtraction makes zero task-level identifiable, inducing selective alignment, while an order-sensitive operation produces broad alignment across numbers. These patterns predict success in zero-shot cross-lingual transfer. Together, our results show that relational structure in a shared world can promote entity alignment and enable transfer.

---


### 118. [What Hallucinations Have We Measured? Semantic Illusion, Confabulation, and Expressed Uncertainty](https://arxiv.org/abs/2610.38520)

**<font color=#1a73e8>作者：</font>** Hazel H. Kim, Jakub Binkowski, Ekaterina Fadeeva 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination remains one of the most critical challenges in deploying large language models (LLMs) reliably and safely. Yet the term is used inconsistently across the research community. We argue for a strict definition of hallucinations in LLMs. First, hallucinations should be confident incorrectness, kept separate from expressed uncertainty (UNK)1. UNK reveals that the model may be wrong, whereas a hallucination does not reveal it and is therefore more dangerous in practice. Conflating the two obscures their distinct behaviors and makes them hard to study. Second, hallucinations should be split by a simple re-elicitation test: does any semantically equivalent prompt recover the correct response? This test probes whether the relevant knowledge2 is accessible. If none does, the knowledge is likely absent or inaccessible, and the error type is a confabulation (CF) that likely requires external knowledge or retraining; if some does, the knowledge is accessible from the model but applied inconsistently, and the error type is a semantic illusion (SI) that simple prompt or decoding changes can mitigate3. Re-evaluating 14 recent hallucination methods under this taxonomy yields three findings. (1) Detection methods flag UNK more often than hallucinated responses (i.e., SI and CF). (2) Mitigation methods are far more effective for SI than for CF. (3) Latent signals are more informative than output-level signals for CF. An audit of recent hallucination papers shows that most conflate these categories. We recommend reporting CF, SI, and UNK separately, and introduce a practical labeling protocol that needs only a modest number of semantically equivalent prompts.

---


### 119. [WebMaze: Defending Against LLM-Powered Web Scanners with Functionality-Coupled Deception](https://arxiv.org/abs/2610.38524)

**<font color=#1a73e8>作者：</font>** Pengfei Zeng, Changhua Luo, Penghui Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have enabled more effective vulnerability scanning of web applications. However, these capabilities also make it significantly easier for attackers to automate cyberattacks on the web. In this work, we investigate how to divert malicious LLM-based web scanning, with preservation of genuine functionality as a deployment requirement. We systematically study six LLM-based scanners and summarize how they gather information and iteratively select actions based on observations. Guided by the study, we then present WebMaze, a defense that preserves genuine application functionality while diverting LLM-based scanners to a generated decoy world. WebMaze embeds functionality-coupled traps in genuine pages and constructs view-tailored interactive decoy worlds from the application's existing views. The traps blend into genuine components and expose entry points to decoy worlds that sustain exploration through connected pages and interactions without changing genuine functionality. Across 12 web applications and three LLM-based scanners under the default no-disclosure setting, decoy pages account for an average of 93.0% of the distinct pages requested per run. This demonstrates that WebMaze effectively diverts scanners away from genuine application pages and into the generated decoy worlds. Even when explicitly informed about the decoy mechanism and instructed to avoid decoy pages, scanners continue to explore predominantly decoy pages.

---


### 120. [From Leniency to Suspicion: How an Open Post-Training Recipe Changes Whom LLM Fact-Checkers Believe](https://arxiv.org/abs/2610.38532)

**<font color=#1a73e8>作者：</font>** Nouar AlDahoul, Yasir Zaki  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs increasingly fact-check online content with the poster's identity in view. However, it remains unclear which post-training changes how much a model's truth judgement depends on the poster's social class, and how such a change happens inside the model. This paper investigates job-based doubt, i.e., judging a claim false more often when the poster has a lower-status job, using fact-checked claims with randomised poster profiles in base and post-trained checkpoints of six model families. Our results reveal that: 1) post-training creates such doubt only with the open Tülu-3 recipe (OLMo-2 32B, Tülu-3 70B), not with Meta's, Alibaba's or Mistral's; the effect is under one percentage point but statistically reliable, exceeding training drift and replicating on independent claim sets; 2) in OLMo-2 32B, the model does not start noticing the poster's job more, but starts interpreting it differently: a lower-status job pushes the base model toward "true" and the post-trained model toward "false"; and 3) this flip is carried by a single residual-stream direction and happens at supervised fine-tuning. The mechanism was confirmed on 400 new claims with pre-specified predictions. None of seven deployed commercial models doubts lower-status posters more. Our work underscores the need to audit speaker bias per training recipe.

---


### 121. [Implicit Minor Detection from Multi-Turn Dialogue in High-Risk AI Interactions: A Constrained Self-Evolving LLM Harness](https://arxiv.org/abs/2610.38546)

**<font color=#1a73e8>作者：</font>** Xiaohan Zhang, Ying Zhao, Ruilin Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In high-risk text interactions, a system may need to estimate whether the current speaker is likely to be a minor before applying age-conditioned safeguards. Many text-based dialogue systems lack strong identity signals such as account information, verified identity, facial data, or device data, and must rely on weak cues that emerge across multiple turns. We formulate implicit minor detection under weak identity information as a high-risk user-attribute inference task and propose a constrained framework comprising a large language model, a Harness, and a Maker-Checker protocol. The framework controls when inference is invoked, requires structured dialogue-linked evidence, and subjects validation-selected Harness revisions to version-level review. On a controlled Chinese benchmark comprising 8,328 multi-turn dialogues, our method improves average precision and minor-class F1 by 7.60 and 6.37 percentage points, respectively, over direct inference using the same LLM family.

---


### 122. [Detecting Fine-Grained Differences between Image Datasets](https://arxiv.org/abs/2610.38547)

**<font color=#1a73e8>作者：</font>** Leander Girrbach, Alexander von Recum, Kirill Bykov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting whether and in particular how two data distributions differ is a fundamental statistical problem. For example, we might be interested in which concepts (expressed in natural language) differ between two classes, the outputs of different generative models, or the same model with different prompt specifications. When working with large and complex image datasets, we intuitively think that first selecting concepts from a broad list using fine-grained patch embeddings, and then optimizing the concepts to better fit the data is an effective workflow. However, prior work instead uses MLLMs to propose concepts and image-level embeddings to select them. Therefore, we systematically compare these techniques and find that selecting concepts from broad lists can replace MLLM-proposals at obviously lower cost. MLLM inference can then be spent on optimizing selected concepts instead to achieve substantial improvements. Additionally, by designing a new benchmark that focuses on low-prevalence and multi-concept distinctions, we find that selecting nonredundant concepts instead of only the most distinguishing concepts matters, and we introduce techniques for how to effectively do this. Finally, we show how our methods address important problems like detecting spurious correlations and biases. Overall, our work presents a fundamental perspective shift on how we analyze interpretable distributional differences between datasets.

---


### 123. [Co-Evolving Policy and Rubric via Capability Awareness for Open-Ended Generation](https://arxiv.org/abs/2610.38566)

**<font color=#1a73e8>作者：</font>** Chengsheng Zhang, Wenshen Xu, Yuchuan Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rubric-based reinforcement learning (RL) offers interpretable, fine-grained supervision for aligning large language models (LLMs) on open-ended generation tasks. However, static rubric criteria may become saturated or remain beyond the policy's exploration, rendering the reward signals insufficiently discriminative. While recent efforts seek to guide sampling exploration or evolve rubrics, they fail to explicitly factor in how rubric difficulty should track the evolving policy's capabilities, resulting in a persistent mismatch between the optimization objective and the policy's current capability frontier. In this paper, we propose \textbf{Co}-Evolving Policy and Rubric via \textbf{C}apability \textbf{A}wareness (\textbf{CoCA}), a closed-loop framework that jointly adapts the rubric and policy through criterion-level diagnosis. Specifically, CoCA contrasts query-only and rubric-guided rollouts to characterize each criterion relative to the current policy, recalibrates criteria with mismatched difficulty, and identifies guidance-revealed capability gaps for frontier-based learning. Based on this insight, CoCA either expands rubric-conditioned frontiers through guided optimization or transfers qualified gains through on-policy self-distillation. As the policy updates, CoCA improves the capability diagnosis and enables more reliable distillation, thereby completing the co-evolution loop. Extensive experiments across diverse benchmarks and LLMs demonstrate that CoCA consistently improves performance over rubric-based RL methods. Moreover, CoCA promotes the internalization of guidance-revealed capabilities into query-only behavior while mitigating capability degradation.

---


### 124. [Do Audio LLMs HEAR Pain? Tracing Acoustic Evidence from Speech to Language Reasoning](https://arxiv.org/abs/2610.38570)

**<font color=#1a73e8>作者：</font>** Wenqi Li, Xiangjue Dong, Sulaiman Vesal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large audio language models (LALMs) can process speech directly, but it remains unclear how well they use the non-lexical acoustic information that speech carries. We study this question through pain, using TAME-Pain, which contains pain-neutral Harvard sentences and spoken pain ratings recorded at different self-reported pain levels. We introduce HEAR, a four-stage diagnostic framework that traces pain-related information from the speech signal to the model's prediction, and apply it to seven closed-source and open-weight LALMs. On the Harvard sentences, where pain can only be inferred from the voice, all models perform at chance level, and same-speaker references or few-shot examples improve balanced accuracy by no more than six points. On the spoken ratings, the same models reach 87.5-99.7% balanced accuracy. Layer-wise probing of open-weight LALMs shows that pain can be decoded from early audio representations (74.1% balanced accuracy for binary prediction and 45.0% for three-class severity), but that this information, along with most pain-associated acoustic cues, decreases in deeper layers. In an acoustic perception test, weaker models cannot distinguish even large changes in these cues, whereas stronger models can but still fail to infer pain. Finally, we recover pain-related acoustic cues and directly reinject them as structured text into the prompt, which improves pairwise pain prediction by up to 32 points. These results indicate that current LALMs encode paralinguistic information in early layers that is largely unavailable when the model produces its answer.

---


### 125. [CALM: Conflict-Aware Lifecycle Memory Governance for Long-Horizon Language Agents](https://arxiv.org/abs/2610.38573)

**<font color=#1a73e8>作者：</font>** Chang Li, Xianhao Ou, Xinyan Ma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A memory can be outdated for present-day reasoning yet indispensable for reconstructing the past. Relevance-based retrieval overlooks this tension: semantic relevance, evidence-grounded validity, and query-specific eligibility are distinct. We propose CALM, a conflict-aware lifecycle memory governance framework that decouples persistent memory preservation from query-time admission. CALM converts heterogeneous records into evidence-grounded memory cells, updates validity and lifecycle states using support, conflict, and dependency signals, and admits query-appropriate evidence through training-free or learned gating informed by temporal applicability. Across LongMemEval-S and LoCoMo with Qwen and GPT backbones, CALM outperforms state-of-the-art baselines, achieving the best overall accuracy. Compared with simple filtering and reranking, query-conditioned admission further improves evidence selection. Conflict-blocking and robustness analyses show CALM suppresses erroneous retrieved memories while retaining useful evidence. Historical-reconstruction experiments demonstrate that preserving superseded records supports accurate earlier-state reasoning without compromising current-state answers.

---


### 126. [Two-Stage Clipping: Linear-Time Approximate and Exact Mixed-Norm Projections for Transformers](https://arxiv.org/abs/2610.38598)

**<font color=#1a73e8>作者：</font>** Michel Barlaud, Jean-Paul Marmorat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) based on Transformer architectures have achieved remarkable performance across artificial intelligence tasks, but their computational cost remains a major bottleneck. Structured sparsification provides a promising approach to reducing this cost. In particular, $\ell_{1,\infty}$ projections can induce column-wise sparsity in model matrices, but existing proximal methods (Prox) typically require $\mathcal{O}(nm\log(nm))$ operations for matrices in $\mathbb{R}^{n\times m}$, limiting their computational and energy efficiency.
In this paper, we introduce Two-Stage Clipping (TSC), an efficient structured sparsification operator inspired by bilevel optimization. Rather than solving a bilevel optimization problem in the strict sense, TSC decomposes the computation into two successive stages. First, group-level quantities are projected to allocate the global sparsity budget and identify active groups. Second, the resulting values are used as group-wise clipping thresholds for the matrix coefficients. For square attention matrices ($n \times n$), the complexity of our TSC method is $O(n^2)$, which is linear in the number of matrix coefficients.
We establish a theoretical bound on the discrepancy between TSC and the exact proximal projection and show on synthetic data that the additional Euclidean approximation cost remains small in practice. Extensive benchmarks demonstrate substantial runtime improvements over proximal baselines and validate the theoretical norm identities underlying the proposed construction.

---


### 127. [V-CAPE: Visual Consistency Assessment for Product Image Editing](https://arxiv.org/abs/2610.38611)

**<font color=#1a73e8>作者：</font>** Iaroslav Melekhov, Roberto Alcover Couso, Francesco Taioli 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative image editing enable complex transformations such as background replacement, object manipulation, and pose adjustment from natural language instructions. However, verifying that these transformations preserve visual consistency, defined as the preservation of an object's intrinsic visual attributes, including geometry, texture, color, and fine-grained details, remains a largely unsolved problem. This challenge is particularly pronounced at scale, where manual inspection is infeasible and automated quality assessment (AutoQA) could become essential. In this work, we introduce Visual Consistency Assessment for Product Image Editing (V-CAPE), a large-scale dataset for evaluating visual consistency in generative image editing. The dataset consists of 40K unique source-target product image pairs, each annotated with binary accept/reject labels and structured failure modes capturing fine-grained inconsistencies such as geometric distortions, pose errors, and identity mismatches. V-CAPE combines real-world edited images with a synthetic subset constructed from 3D assets, enabling both realistic evaluation and controlled analysis. Vision-language models (VLMs) across all evaluated size categories on AutoQA achieve accuracy below 65%, indicating that the dataset poses a substantial challenge regardless of model scale. Our results highlight fundamental limitations of current models in verifying visual consistency under transformation, positioning V-CAPE as a benchmark for advancing fine-grained image editing evaluation.

---


### 128. [How Deterministic SAST and AI Security Agents Divide the Work: Coverage, Harness Policy and Cost in Snyk VulnBench 2.0](https://arxiv.org/abs/2610.38617)

**<font color=#1a73e8>作者：</font>** Liran Tal, Chris Liu, Charlotte Fereday 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We ask what AI coding agents and AI security harnesses find that deterministic static application security testing (SAST) does not, and what they miss that SAST catches. VulnBench 2.0 is a benchmark of 108 hand-curated, attacker-reachable vulnerabilities in 20 open-source web applications in Go, JavaScript/TypeScript, Python and Java; 62 flow across more than one file. A finding is credited only if it locates the vulnerability's attacker-controlled source and its dangerous sink, each within two lines. We evaluate nine productized configurations under one blind protocol: the Snyk Code static analyzer, Claude Code's /security-review with three model and effort settings (one with the Snyk MCP server), Codex Security with GPT-5.6 Luna, Terra and Sol, and the DeepSec scanner with two model backends. Snyk Code reached 82.4% macro recall (89 of 108) and Claude Code with Opus 5 at xhigh effort 79.3% (85 of 108); they disagree on 28 vulnerabilities, split 16 to 12, too few to tell them apart. Neither engine was sufficient alone: together they reached 101 of 108, the ceiling of all seven comparable configurations combined, and the AI configurations also reported at least seven real vulnerabilities that the reference set did not contain and Snyk Code did not report. What an AI engine misses depends on its harness as much as on its model: without Claude Code's built-in review policy, the same model matched 16 instead of 9 of the 20 vulnerabilities in the classes that policy excludes or restricts (supplementary run on 19 of 20 applications); Codex Security with GPT-5.6 Sol located 80 vulnerabilities at file level but 34 at line level; DeepSec's model-free file selection kept a file from only 56 of the 108 flows. Coverage and cost were only loosely related. The harness, fixtures, reference sets and all run data are public.

---


### 129. [Think Before You Act: Decision Gate for LLM Agents](https://arxiv.org/abs/2610.38620)

**<font color=#1a73e8>作者：</font>** Iftach Shoham, Yuval David, Offer Akrabi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly perform consequential actions through external tools, yet their proposed actions are often executed without independent verification of policy compliance or task completion. We introduce JevAct, a runtime verification framework that intercepts selected agent actions before execution and enables feedback-driven correction. JevAct compiles domain policies into executable state checks and structured questions evaluated by a prefill-only decision model, which produces probability-based judgments without relying on LLM generation. By combining deterministic verification of tool-state facts with probabilistic assessment of conversational context, the framework identifies potentially invalid actions and premature task termination, providing targeted feedback for bounded revision. JevAct operates independently of the underlying agent model and requires no modifications to its parameters or tools. We evaluate JevAct across eleven LLM agents on $\tau^2$-bench Airline and Telecom tasks and BFCL. Results show improvements in agent reliability across multiple models and benchmarks, with particularly consistent gains on Telecom and BFCL, while performance on Airline is more mixed. Overall, these findings suggest that combining structured decision models with executable verification can improve the reliability of tool-using LLM agents.

---


### 130. [Cross-Primitive Consistency in Jev](https://arxiv.org/abs/2610.38623)

**<font color=#1a73e8>作者：</font>** Xu Liu, Guikun Chen, Kanzhi Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Jev enables efficient decision-making with large language models (LLMs) through typed querying primitives, allowing the same semantic state to be expressed in different formats, such as binary and multiple-choice queries. However, the consistency of decisions across primitives has not been systematically evaluated. This work introduces PrimaCons, a four-axis benchmark for assessing cross-primitive consistency while preserving the semantics of the query. Evaluations across three Jev sizes reveal consistency violations across all four axes. Our analysis shows that these violations follow systematic patterns and that cross-primitive discrepancies predict decision failure with a ROC-AUC of 0.91. To mitigate these inconsistencies, we propose the Cross-Primitive Residual Calibrator (CPRC), which attaches a lightweight residual network to a frozen backbone and jointly optimizes predictive accuracy and cross-primitive consistency. Under a leave-one-domain-out protocol, CPRC reduces cross-primitive inconsistency by 58.57% and improves accuracy by +2.97%., demonstrating its effectiveness in both in-domain and out-of-domain settings. Our findings establish cross-primitive consistency as a key dimension for evaluating Jev and provide a practical approach to improving the reliability of its decisions. Code and benchmark is available at this https URL.

---


### 131. [ItemCompass: Real-Time Edge-AI Wearable Vision for Tag-Free Domestic Object Retrieval](https://arxiv.org/abs/2610.38629)

**<font color=#1a73e8>作者：</font>** Tsz Lok Cheung, Jeff Kai-Tai Tang, Anthony Kong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Misplacing household objects disrupts daily routines, especially for elderly users. ItemCompass addresses this with a real-time, tag-free wearable AR system that builds a persistent digital twin of the home for natural language object retrieval. A custom eyewear node streams visual and inertial data to an edge server, where YOLOv11n detection, Siamese re-identification, and a Pedestrian Dead Reckoning engine log object locations as Spatial Anchors in InfluxDB. Voice queries are resolved by a local Faster-Whisper and Qwen2 LLM pipeline, delivering concise spoken and AR guidance on a heads-up display. Evaluation shows 0.40 m localization drift, 97.5% step precision, and mAP@0.5 of 0.874, with users rating Accuracy and Trust at 4.6/5.0. The system highlights always-on sensing, conversational spatial memory, and privacy-by-design for wearable computing.

---


### 132. [Right Numbers, Wrong Questions: Evaluating LLMs on Underspecified Financial Queries](https://arxiv.org/abs/2610.38631)

**<font color=#1a73e8>作者：</font>** Radha Yadav, Prasanna Devadiga, Peeyush Mishra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial assistants answer questions that sound factual but depend on what the user leaves unsaid: what a data figure measures, which product variant is meant, and the investor's situation and the rules that apply. An assistant that ignores these can still answer with a real number from its data, one that answers a different question. We call this frame collapse. We study it in Indian mutual funds, where product variants and tax rules are formally defined, so the correct answer can be computed for every reading. One study tests each challenge. Given an ambiguously labelled figure, models used it, often under the user's label. Given every alternative labelled, they listed them all, but the layout decided which came first. Missing a fact about the investor, weaker agents assumed a default or an outdated tax rule; requiring the fact did not guarantee its use. Because such answers match their data, checks against the data pass them. An AI judge caught mislabelled figures only when told what each field means, and still passed answers that silently chose another reading. We show how these failures arise, not how often, and propose controls for financial assistants.

---


### 133. ["Close enough?" An investigation into multiplication errors in LLMs](https://arxiv.org/abs/2610.38634)

**<font color=#1a73e8>作者：</font>** William Bolton, Bezawit Tilaye, Huw Day  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) frequently fail at multi-digit arithmetic, but the underlying mechanisms governing these failures remain poorly understood. While recent work demonstrates that addition errors follow a "noisy quantisation" model localised around carry boundaries, whether this framework generalises to multiplication remains an open question. In this work, we evaluate multiplication capabilities across several small base LLMs on a dataset of 16,991 problems spanning varied operand lengths. We show that multiplication errors do not conform to the addition-style noisy quantisation model. Instead, we uncover a novel error regime in small Qwen models: errors in lower-order columns predominantly preserve parity. Conversely, higher-order digit errors shift toward off-by-one carry failures. Our findings suggest that arithmetic computation in LLMs relies on distinct, multi-periodic internal representations where parity is tracked more robustly than exact digit identity, providing new mechanistic insights into numerical reasoning in transformers.

---


### 134. [When AI performs, what remains? An integrative review of generative AI and cognitive capital in individuals and organizations](https://arxiv.org/abs/2610.38647)

**<font color=#1a73e8>作者：</font>** Giuseppe Riva, Stefania La Rocca, Brenda K. Wiederhold 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence is rapidly entering knowledge work, and its short-term productivity benefits are increasingly documented. Less is known about what happens, over time, to the knowledge, skills and judgment that remain in people and organizations. This integrative narrative review addresses that question through the construct of cognitive capital: the accumulated, renewable and depletable stock of knowledge, cognitive and metacognitive capabilities, and practices that enables an individual or an organization to learn, interpret information, exercise judgment, solve problems and adapt. We distinguish individual and organizational cognitive capital from the capability of the human-AI system, so that gains in joint performance and losses in human capability can be observed at the same time. Drawing on experimental, field and conceptual work, we propose four mechanisms through which interaction with AI affects cognitive capital: substitution of practice, scaffolding and feedback, metacognitive calibration, and organizational aggregation. Seven principles summarize the current evidence, including that assisted performance differs from retained competence, that the same technology can support or displace learning depending on design and use, and that individual gains can coexist with reduced collective diversity. For each mechanism we derive testable propositions, and we discuss five design levers for organizations as proposals to be validated rather than established practice. We conclude that cognitive capital offers a multilevel frame for governing AI adoption and outline a research agenda centered on longitudinal, multilevel measurement.

---


### 135. [AskStream: When and What to Ask Proactively under Uncertainty in Streaming Video Understanding](https://arxiv.org/abs/2610.38678)

**<font color=#1a73e8>作者：</font>** Lu Wang, Zhuoran Jin, Longxiang Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in multimodal large language models have increased interest in interaction paradigms for video understanding. The evolution from offline to streaming and proactive interaction has gradually shifted models from passive responders toward more proactive agents that can decide when to answer. However, existing proactive paradigms typically assume that the information required to answer a query is complete, leaving models to only wait or answer. In the real world, however, information is often incomplete due to uncertainty from either the video or the user. In proactive paradigms, such uncertainty can cause the model to wait forever or generate highly hallucinatory responses. We therefore argue that proactive interaction should be redefined with a third action: ask, allowing models to actively ask for missing information. To study when and what models should ask before answering, we introduce AskStream, the first multi-turn benchmark spanning video and user uncertainty for streaming video understanding, with four task categories and eight subtasks. It contains 438 videos with 2,714 manually annotated frame-level time windows across three types: wait, ask, and answer. Across both multiple-choice and open-ended settings, even the strongest model attains only 52.18% on our proposed Ask-F1 metric, highlighting substantial limitations in proactive information seeking under uncertainty.

---


### 136. [Weaken to Strengthen: Weakening-Induced On-Policy Self-Distillation for Large Reasoning Models](https://arxiv.org/abs/2610.38681)

**<font color=#1a73e8>作者：</font>** Yecheng Wu, Song Han, Han Cai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-distillation offers a way to improve reasoning models when a suitable external teacher is unavailable. However, common approaches rely on privileged information to construct a stronger self-teacher, limiting their use when only unlabeled prompts are available. In this paper, we introduce Weakening-Induced On-Policy Self-Distillation (WISD), which instead constructs a weaker counterpart of the original model and uses the contrast between the two as a training signal without requiring privileged information. We explore two ways to construct the weaker model: low-bit quantization and magnitude pruning. We evaluate WISD across diverse architectures and scales on mathematical and coding reasoning tasks. Across these benchmarks, quantization and pruning improve average accuracy over the original models by 4.0 and 5.5 percentage points, respectively, achieving state-of-the-art performance even without privileged information. Notably, pruning raises Qwen3.5-4B's accuracy from 57.7% to 70.5% on HMMT 2025 and from 39.1% to 56.7% on LiveCodeBench v6. Quantization raises Qwen3.6-35B-A3B's accuracy from 68.5% to 74.6% and from 61.8% to 69.5% on the same benchmarks, respectively. These results establish WISD as a novel and effective self-distillation framework for large reasoning models.

---


### 137. [On the Generalization Gap of Streaming Federated Learning with Markovian Data](https://arxiv.org/abs/2610.38686)

**<font color=#1a73e8>作者：</font>** Masoud Kavian, Milad Sefidgaran, Youssef Attia El Hili 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Streaming federated learning (SFL) allows clients to train a shared model from continuously arriving data without retaining large local datasets. Such streams often exhibit temporal dependence, yet its effect on generalization remains poorly understood. In this paper we study the expected generalization gap of the aggregated model when client data follow Markov processes, using information-theoretic and rate-distortion techniques. Our framework accommodates heterogeneous Markovian dynamics across clients and distinguishes temporal dependence from information acquired during local learning. We establish bounds under cross-entropy loss, specializing them to Linear Next-Token Prediction (LNTP) and Self-Attention Next-Token Prediction (SANTP). These results quantify the effects of client count, communication rounds, sample size, data dimension, mixing time, and context length. In particular, they reveal a communication--generalization tradeoff: although frequent aggregation may help optimization, it can weaken generalization guarantees. They also suggest a potential advantage of distributed over centralized streaming learning under a fixed total data budget. Temporal dependence enters through the square root of the mixing time. By analyzing the history-state process, we obtain refined bounds with improved context-length dependence under suitable mixing conditions. Experiments on GPT-style language-model pretraining with TinyStories and real-world time-series forecasting illustrate how collaboration and communication frequency influence generalization under temporal dependence

---


### 138. [Deogen: Automatic Benchmark Generation for Reasoning over Policies](https://arxiv.org/abs/2610.38687)

**<font color=#1a73e8>作者：</font>** Sam Kouteili, William Liang, Keeran Murray 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly being deployed in regulated settings, where a model must apply given rules to the facts of a situation to determine a verdict. Benchmarking this capability, known as deontic reasoning, remains a costly and manual process, with existing datasets largely hand-crafted. In this paper, we present DeoGen, a scalable, automatic, and parametrizable benchmark generator for deontic reasoning. By autoformalizing policy rules to first-order logic, we can construct decision trees that capture possible outcome trajectories. Each path down a tree becomes a benchmark entry, with each tree producing combinatorially many entries relative to tree depth. Paths ending at a leaf entail a verdict, while non-leaf paths measure a model's ability to abstain when presented with insufficient information. Evaluations show frontier models return the correct verdict 89-92% of the time. Notably, performance degrades (22-40% correct) on entries without sufficient information to claim a verdict, even with explicit instructions to abstain in such cases. In all, DeoGen presents an automatic, scalable, and parametric method for generating deontic reasoning benchmarks.

---


### 139. [Beyond fabrication: Misattributed numbers in papers written by AI research agents](https://arxiv.org/abs/2610.38691)

**<font color=#1a73e8>作者：</font>** Mosab Alfaqeeh, Omar Hourani, Muath Hourani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Verifying numerical claims in research written by AI agents is an important but challenging problem. Recent benchmarks show that many agent-written papers fail integrity checks, but such verdicts, often produced by a single LLM judge, identify failure without explaining its nature, and existing checks either test a paper for internal consistency or test whether a reported value appears somewhere in an agent's output. We re-analyze all 540 released judgments from a recent public benchmark of AI research agents (nine agents, fifteen open research problems) and manually label 256 numerical claims from 18 submissions. Failures concentrate on alignment between the paper and the underlying work rather than overt cheating, and about four in five unsupported claims correspond to values in the agent's own files that come from the wrong experiment, metric, or run. We introduce a deterministic claim-to-evidence checker that scores whether the surrounding context identifies the claimed result and calibrates each claim against numerical decoys. With its rules fixed before labeling, it certifies claims with over 90% precision against blinded annotators (78 of 85; Cohen's kappa = 0.89), while verifying only a subset of claims; most claims it cannot verify are nevertheless traceable, so failure to verify is not evidence of falsehood. An LLM verifier given the same evidence recovers more traceable claims but accepts about three times as many misattributed ones, so the two are best used together. Applied to 99 submissions, the checker reveals large differences in traceability across agents, and a second judge from a different vendor preserves the official agent ranking while passing twice as many papers. These findings motivate provenance-first auditing of AI-produced research.

---


### 140. [SatOps-Decision: Low-Latency Discriminative Decisions for Onboard Satellite Communication Operations](https://arxiv.org/abs/2610.38697)

**<font color=#1a73e8>作者：</font>** Lifan Mei, Yuxuan Li, Jiaxian Tu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose SatOps-Decision, a method for low-latency decisions in satellite communication operations. To the best of our knowledge, it is the first application of Jev-style general-purpose discriminative decision models to satellite operations, and the accompanying benchmark is the first dedicated to this approach. The learned scorer, a locally adapted Laya encoder with its native decision head, selects among supplied operational answers in a single forward pass. The benchmark combines authored operational contracts, controlled state changes and independently checked labels in an auditable construction. Evaluation prioritizes complete-request latency and raw decision accuracy; all main accuracy comparisons use the same 1,024 held-out questions, separate from training and development. SatOps-Decision's local scorer has a median latency of 90.3 ms per decision, versus 493.9 ms for Qwen3.5-0.8B generation and 388.4 ms for OneJev1.6-0.8B: $5.47\times$ and $4.30\times$ speedups based on median request times in the measured FP32/MPS implementations. Its mean raw accuracy is 85.3%, versus 42.5% for frozen Laya, 40.7% for Qwen generation and 58.6% for OneJev. As cloud accuracy references, original Jev 1.14/1.13 reach 87.4/81.9%.

---


### 141. [Latent Decision Flow Rewards for Clinical Guideline Reasoning](https://arxiv.org/abs/2610.38709)

**<font color=#1a73e8>作者：</font>** Gaurav Bhatt, Marinka Zitnik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical practice guidelines encode evidence-based recommendations as conditional decision flows, which makes them a natural source of process supervision for training reasoning models. Two properties of clinical reasoning make this supervision difficult to use. A decision flow consistent with a guideline does not by itself determine the correct answer for a given patient, which we call the path--answer gap, and several valid decision flows can support the same clinical decision, which we call path multiplicity. Current training approaches address parts of this problem. Answer rewards supervise the final decision, and process rewards computed against a reference flow supervise one valid decision flow per case. Supervised fine-tuning on annotated flows teaches guideline-consistent reasoning but constrains the model to one trajectory per case and can reduce answer accuracy. We introduce GUIDER, a method that jointly optimizes a decision flow controller and a reasoning policy. The controller learns to generate plausible decision flows from guideline-derived supervision, and the policy learns to generate a decision flow and a final answer for each patient case. GUIDER computes the process reward for the policy over several controller-generated flows, which accounts for path multiplicity, and gates this reward on answer correctness, which addresses the path--answer gap. Joint training allows the process supervision to evolve with the policy. On MedGUIDE, GUIDER with Qwen3-14B achieves 82.5 weighted accuracy and 73.5 guideline adherence, 3.3 and 3.1 points above the strongest clinical reinforcement learning baseline. With Qwen3-14B and Gemma4-12B backbones, GUIDER also improves over CRPO, MRPO, and FaithMed on the out-of-domain benchmarks AMEGA-LLM, RealMedQA, and CancerGUIDE.

---


### 142. [Learning Scientific Trajectories to Predict Future Biomedical Discoveries](https://arxiv.org/abs/2610.38719)

**<font color=#1a73e8>作者：</font>** Chia-Hsuan Chang, Brian Ondov, Jiang Lv 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI co-scientists have expanded the use of large language models for generating scientific hypotheses and guiding experimental investigation. Here we investigate whether temporal patterns in the semantic representations of complete biomedical conclusions can guide hypothesis generation. We introduce ForeSCITE, a framework that identifies thematic clusters of published conclusions, estimates a direction separating earlier from more recent findings within each cluster, and projects existing conclusion embeddings along these directions. An embedding language model trained to reconstruct conclusions decodes the projected coordinates into natural-language hypotheses. Across 407 clusters derived from approximately three million pre-cutoff conclusions, we identify temporal structure and illustrate its retention after decoding. In retrospective, time-sliced evaluations, ForeSCITE increases semantic coverage beyond the historical corpus, biomedical entity-pair novelty and post-cutoff pair re-observation relative to five prompt-based and retrieval-augmented baselines. Expert review of prioritized CAR-T hypotheses identified 37 candidates as both novel and biologically plausible, and expert justifications for five selected hypotheses illustrate their biological rationale and subsequent literature support where available. These findings support temporal guidance in semantic space as a scalable mechanism for proposing biomedical hypotheses for subsequent scientific evaluation.

---


### 143. [inkGround: Benchmarking Fine-grained Visual Grounding Capabilities of Vision-Language Models for Cursive Handwriting in the Wild](https://arxiv.org/abs/2610.38720)

**<font color=#1a73e8>作者：</font>** Sidra Hanif  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human handwriting is produced as an ordered sequence of pen movements, but an offline image keeps only the final ink. Handwriting trajectory recovery aims to restore the ordered stroke points and their pen-up/pen-down transitions. Existing image-trajectory pair datasets are recorded with digitizing tablets under controlled conditions, which limits writer coverage and stylistic diversity. Moreover, there is no benchmark that measures the visual grounding capabilities of general-purpose Vision-Language Models (VLMs) for the stroke trajectory recovery task. In this work, we introduce inkGround, a benchmark for stroke trajectory recovery from full-page, camera-captured handwriting. inkGround pairs 537 page images (~18.7k words, ~163k strokes) with reference trajectories produced by a pretrained offline-to-online model, filtered by OCR agreement, and verified by human raters. Because these references are pseudo-labels that represent one plausible pen trajectory, we also evaluate VLMs on the IAM-OnDB dataset, which provides recorded pen trajectories. We cast the task as text-conditioned point grounding: given a page image and a target word, the model must locate the word and output its ordered stroke points. Outputs are scored by trajectory fidelity (DTW, Chamfer distance), readability of the rendered strokes (Accurate Rate, Correct Rate), and style similarity. We benchmark four open-source and three frontier closed-source VLMs with a shared in-context prompt. Closed-source models, notably Gemini-3.1-Pro, produce legible trajectories close to the reference, and this ranking also holds on IAM-OnDB.

---


### 144. [Idea Traces: Threading Accretive Content across Scientific Papers](https://arxiv.org/abs/2610.38721)

**<font color=#1a73e8>作者：</font>** Luke S. Snyder, Jeffrey Heer  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We introduce idea traces, a novel thread-based representation of accretive content across scientific papers. Rather than capturing fixed themes from papers, idea traces surface similarities and deltas of faceted content that enable inspection of how ideas relate and evolve across the citation network. To extract traces, we contribute an LLM pipeline that deconstructs salient transitions between pairs of papers and collates the output into an idea dependency graph. We leverage idea traces in a visual system that supports idea-driven navigation starting from a seed paper, lifting the "plane" of synthesis from papers to ideas. To evaluate the usefulness and quality of generated ideas, we provide a case study that compares our approach with an LLM Q&A workflow, and interview 10 researchers who used our system and annotated 110 ideas. Experts found that our approach helped extract a useful space of connections that would have been difficult to make otherwise. Drawing on their feedback, we outline several promising directions for future research.

---


### 145. [The Quine Test: How Much of a Model's Self Survives Its Own Description?](https://arxiv.org/abs/2610.38726)

**<font color=#1a73e8>作者：</font>** Bibin Babu, Ivan P. Yamshchikov, Aleksei Shpilman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier language models express coherent preferences, but behavioral evidence alone cannot say whether these belong to the model or to a character it portrays. Following Hofstadter's view of the self as a self-description, we ask whether a model's description of itself works as a portable specification of its preference profile, a quine test: can the text a model writes about itself regenerate its behavior elsewhere? Ten models from nine labs write self-descriptions; we place each one in the prompt of other models (receivers) and of fresh instances of the author, and measure how closely their choices on a 110-item preference battery match the author's.
First, the tested native self-descriptions (native: the profile measured under a generic assistant prompt) show no average reconstruction gain across variations in length, framing, wording and prompt placement: on a 0 to 1 fidelity scale where a model's fidelity to a fresh instance of itself is 0.979 and to unrelated models about 0.89, the one-sided 95% upper bound on the pooled gain is below +0.01 in every tested system-prompt condition, and descriptions based on the author's observed choices do no better. Second, the channel itself is strong: explicitly listing the author's answers lets receivers reproduce its profile at fidelity 0.955 to 0.960 across three model grids, within 0.03 of same-model repeatability. Third, self-descriptions written under an explicit preference policy transfer the assigned preferences almost as well as the policy text itself. Fourth, reading its own self-description shifts even the author away from its baseline, modestly more than unrelated prose of the same length.
For the preferences measured here, native self-descriptions influence behavior without reliably specifying how to reproduce it in another model. We release the pipeline, battery, raw call logs, and 198 model-written descriptions.

---


### 146. [Adversarial Self-Distillation](https://arxiv.org/abs/2610.38732)

**<font color=#1a73e8>作者：</font>** Mohammad Sadegh Akhondzadeh, Soroush H. Zargarbashi, Aleksandar Bojchevski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Even though current safety-aligned language models are able to refuse harmful requests, their guard can still be bypassed by adversarial perturbations. As in other domains, adversarial training is considered a standard defense. However, due to the autoregressive nature of language generation, supervised finetuning on template refusals does not necessarily teach the model to refuse. Evidence of this is that the adversarially trained model still complies when the attacker injects a compliant prefill. We propose Adversarial Self-Distillation (ASD), which extends a model's own safe behavior to the space of adversarial perturbations. The teacher (the model itself given the clean prompt) can refuse the harmful request by default, or with the help of an additional instruction in its context. ASD distills this knowledge to the student (which is the same model under attack) at the prefixes that the student visits (due to on-policy sampling). These potentially include compliant openings. ASD achieves lower attack success than state-of-the-art defenses with little loss in multiple-choice accuracy, and it becomes able to recover a refusal even after a compliant opening.

---


### 147. [RuleForge: Inferring and Instantiating Latent Visual Rules as Executable Programs](https://arxiv.org/abs/2610.38737)

**<font color=#1a73e8>作者：</font>** Weifeng Xu, Yaxiong Wang, Zhedong Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual rule reasoning asks whether multimodal models can recover an abstract concept from a few examples. Existing studies either infer rules from visual examples but evaluate only classification or verbalization, or supervise executable generation with rules provided as input. Consequently, the relationship between visual rule understanding and reliable rule instantiation remains insufficiently explored. We present Bongard-Forge100k, a controlled benchmark, together with RuleForge, a backbone-agnostic framework that jointly learns visual rule understanding and rule-conditioned executable generation. The benchmark contains 108,797 problems: 86,000 for training, 19,297 for testing familiar rules, and 3,500 for testing held-out rule compositions. The framework progresses through rule-understanding training, joint understanding and scene-program supervision, and refinement via execution-grounded reinforcement learning with Understanding Replay. Executing generated programs under multiple random seeds provides verifiable feedback on executability, rule satisfaction, diversity, and robustness. With UniLIP as the primary backbone, RuleForge improves multiple-choice accuracy over the base model by 20.93 percentage points on familiar rules and 28.42 percentage points on held-out rule compositions, while increasing scene-level rule satisfaction on familiar rules from 2.91% to 70.99%. Additional experiments on InternVL3.5, Qwen3-VL, and Show-o2 demonstrate the effectiveness of the proposed training data and framework across diverse multimodal architectures.

---


### 148. [Leaving, Staying, or Living There? Duration Commonsense Reasoning with Human-LLM Co-annotations](https://arxiv.org/abs/2610.38755)

**<font color=#1a73e8>作者：</font>** Chenyang Yu, Zhaomin Xiao, Yan Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Gardening in the backyard implies living there, while checking into an Airbnb more likely means staying for a few days. Such duration judgments are important for understanding human mobility, travel behavior, and social context. However, duration is rarely stated explicitly in social media posts and must instead be inferred from noisy textual, visual, and contextual cues. In this paper, we investigate whether vision-language models possess such duration commonsense. We create a new corpus of geotagged tweets co-annotated by humans and LLMs to serve as a testbed for this task. We find that state-of-the-art models struggle with duration inference, even when guided by multi-turn Chain-of-Thought prompting. Error analyses further reveal that models often fail to integrate critical contextual information, or they overly rely on prominent visual details while overlooking subtle hashtags and semantic nuances. These findings underscore the significant challenges remaining in context-aware multimodal understanding.

---


### 149. [Rennala NSGD: Asynchronous Stochastic Optimization Beyond Euclidean Geometry](https://arxiv.org/abs/2610.38773)

**<font color=#1a73e8>作者：</font>** Igor Sokolov, Alexander Tyurin, Peter Richtárik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The empirical success of matrix-aware optimizers, such as Muon (Jordan et al., 2024) and Shampoo (arXiv:1802.09568), highlights the potential of non-Euclidean geometry for deep learning, including large language model (LLM) training. Despite this progress, the theoretical understanding of stochastic optimization in general normed spaces remains limited, particularly in distributed settings. We analyze minibatch stochastic gradient descent (SGD) for smooth nonconvex optimization with respect to an arbitrary norm on a finite-dimensional space. Using the framework of $\kappa$-regular normed spaces (arXiv:0809.0813), we derive high-probability oracle complexity bounds under a light-tail condition stated directly in the dual norm induced by the update norm. The bounds make the dependence on geometry explicit through the regularity constant $\kappa$ of the dual space. In the Euclidean case, our bound recovers the standard minibatch SGD rate up to logarithmic factors. For some non-Euclidean geometries and noise models, it is sharper than bounds obtained by converting a Euclidean noise assumption, reducing a linear dimension dependence to a logarithmic one. Building on this framework, we introduce Rennala NSGD, a semi-asynchronous distributed algorithm, and establish wall-clock time complexity guarantees under fixed, heterogeneous worker computation times. In the Euclidean case ($\kappa=1$), our bound matches the parameter dependence of classical Rennala SGD up to logarithmic factors.

---


### 150. [Gold vs.~Translation: Are We Measuring Language, Knowledge, or Locality in Translated Benchmarks?](https://arxiv.org/abs/2610.38788)

**<font color=#1a73e8>作者：</font>** Klaudia-Doris Thellmann, Bernhard Stadler, Dan Saattrup Nielsen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Translated versions of English-origin benchmarks such as MMLU are widely used to evaluate large language models in non-English languages, yet it remains unclear whether they measure the same constructs as natively created benchmarks. We frame this as a proxy validity question and compare DeepL-translated MMLU proxies against six native benchmarks in seven pairings across five Nordic and Baltic languages, evaluating 29 models on each pairing. Beyond ranking agreement, we test incremental proxy validity: does the translated score add predictive value for native performance after controlling for model size and language proficiency? Proxy validity varies substantially across benchmark pairings. Applying the same robustness criteria to all seven pairings, we find four robust effects, two marginal effects, and one null result. The strongest evidence occurs for curriculum-overlap benchmarks such as Skolprov ($\Delta R^2$=.128, 95% CI [.038,.253]), whereas translated MMLU provides no significant incremental value for Sweden-specific factual knowledge in SwedishFacts (p=.242). Because SwedishFacts is also the only open-ended benchmark, we cannot fully separate the effects of local content and response format. Overall, the results indicate a clear pattern: translated benchmarks provide a better proxy when their source content overlaps with the native evaluation target, while locally anchored knowledge is less reliably captured.

---


> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
