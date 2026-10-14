# 🧠 大模型相关研究 | 2026年10月15日

> 本类共 **810** 篇论文：已确认 **758** 篇，待复核 **52** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**551-600**（第 12/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-600** | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 551. [SkillScreen: High-Recall Screening of Malicious Agent Skills with Decision Models](https://arxiv.org/abs/2610.17727)

**<font color=#1a73e8>作者：</font>** Jerrold Huang, Junwei Quan, Saiyue Lyu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills turn natural-language instructions into actions, creating a security challenge: legitimate automation and malicious behaviour can look deceptively similar. A practical screen must catch nearly every attack while keeping the review load manageable. We present SkillScreen, a compact decision model trained to score skill maliciousness directly from this http URL in a single forward pass. On MaliciousSkillBench, SkillScreen flags 20-25% of benign skills at 99% recall on unseen attack families, substantially fewer than the word-level classifier and prompted LLM judges tested. Under the same training protocol, it also generalizes better than a fully fine-tuned encoder to unseen sources. Yet unfamiliar benign sources sharply increase false positives, showing that recognizing new attacks does not ensure reliable screening of new skill collections. Our results demonstrate the value of task-trained decision models for high-recall skill screening. Project page: this https URL

---


### 552. [Safety for Whom? Benchmarking Understanding Beyond Refusal in Egocentric Multimodal Assistants](https://arxiv.org/abs/2610.17728)

**<font color=#1a73e8>作者：</font>** Yewon Han, Jisu Jeon, Suhyun Choi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Egocentric multimodal assistants see through the user's eyes and guide what the user does next, so their outputs directly shape physical actions, including those that affect bystanders. Yet existing safety evaluations do not distinguish whom a response would harm, and score only whether a model refuses. Pooling all harms into one refusal rate hides two failures: a model may protect one target but not another, and it may refuse without understanding the risk, or understand it and comply anyway. We present STOU, a benchmark of 2,902 egocentric video-audio and video-text queries whose potential harm targets the user (Self), co-present individuals (The Others), or society at large (Others). Our evaluation decouples safety understanding from refusal behavior: beyond refusal, we score whether the model recognizes the user's intent, the presence and target of harm, and its downstream consequences. Across 10 open and closed source omnimodal and multimodal LLMs, we find that refusal varies systematically with the harm target, and that models often recognize a harm yet still assist with it. These results show that refusal rates alone cannot certify an assistant as safe, and that safety alignment must account for who would be harmed. Project page: this https URL

---


### 553. [CoCA: Criterion-Aware Credit Assignment for Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2610.17733)

**<font color=#1a73e8>作者：</font>** Guangcheng Zhu, Yingfan Ma, Xing Zheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rubric-based reinforcement learning (RL) evaluates responses against explicit criteria to construct rewards, offering a viable way to train large language models on open-ended tasks. However, standard methods compress criterion-level feedback into scalar rewards and assign uniform token advantages, leaving structured rubric supervision underutilized. Recent work seeks finer-grained guidance by treating rubrics as privileged information to derive self-distillation targets, but the resulting learning signal is not grounded in criterion outcomes and can lead to reward degradation. This motivates us to reframe the problem as criterion-aware credit assignment, where privileged rubric information serves as a relevance cue for credit allocation rather than a source of imitation targets. Accordingly, we propose CoCA, which derives criterion-level credits from group-relative outcomes and allocates them across tokens based on criterion-induced distribution shifts, yielding both outcome-grounded and fine-grained learning signals. Empirically, CoCA achieves an average gain of +4.2% over standard rubric-based RL across medicine and science benchmarks, demonstrating more effective learning on open-ended tasks.

---


### 554. [Explore with Memory, Learn without It: In-Context Exploration and Self-Distillation for LLM Reasoning](https://arxiv.org/abs/2610.17734)

**<font color=#1a73e8>作者：</font>** Yutong Chen, Zhichao Xu, Rui Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exploration bounds learning efficiency in reinforcement learning with verifiable rewards (RLVR). Current methods explore mostly through independent sampling, without fully using the information gathered along the way, such as known wrong answers and environment feedback. We propose LEAF, which injects a dynamic, problem-specific memory into the context before every rollout. The memory contains the most recent response, its reward, and other environment feedback. It is updated after every verifier call. We decouple policy updates from rollouts and update the policy through self-distillation. On four benchmarks and two open models, LEAF accelerates exploration by about 4x compared with a random sampling baseline. On unseen test sets, it improves accuracy over the strongest baseline by 1.59 and 1.83 percentage points on the two models, while using less compute than any RL baseline. These results highlight the potential of LEAF in improving both exploration and learning efficiency. Code is available at: this https URL

---


### 555. [DuplexAct: How Interactive Are Frontier Full-Duplex Spoken Language Models?](https://arxiv.org/abs/2610.17738)

**<font color=#1a73e8>作者：</font>** Jiaheng Dong, Shihong Tan, Gongping Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> End-to-end (E2E) full-duplex spoken language models (FD-SLMs) enable simutanous listening and speaking continously, requiring models to take appropriate interaction actions as conversations unfold. However, existing benchmarks lack a structured action-level formulation, often evaluate action occurrence rather than success, and provide limited coverage of diverse real-world conversations. We introduce DuplexAct, a benchmark for evaluating interaction action taking in E2E FD-SLMs. DuplexAct defines a three-level action taxonomy spanning eight interaction actions and 24 corresponding interaction conditions. We further characterize successful action-taking through immediate execution and subsequent follow-through, and develop action-specific evaluation metrics for both. DuplexAct contains 4,691 test instances spanning casual conversation, meetings, customer service, and interviews, including 2,531 instances derived from real-world conversational recordings. Together, DuplexAct provides a structured and real-world-grounded framework for systematically assessing how E2E FD-SLMs participate in ongoing spoken interaction.

---


### 556. [Coupled Harness--Model Evolution for Scientific Equation Discovery](https://arxiv.org/abs/2610.17740)

**<font color=#1a73e8>作者：</font>** Pengze Li, Jiaquan Zhang, Encheng Su 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to discover scientific equations from experimental data. Such a discovery system has two parts that must work together: a library of executable computational tools and the model's tool-use policy. The tools supply the solving capability, from diagnosing structure in the data to fitting candidate equations; the policy plans and orchestrates their use. Yet existing systems adapt only one part, keeping either the toolset or the model fixed, which leaves the corresponding failures uncorrectable. We develop a coupled evolution framework that improves both parts from the same verifiable fit-error signal. In the tool-evolution phase, an agent grows an executable tool library from a small set of generic numerical operations by diagnosing its own failures: it authors a new tool when a capability is missing and revises its selection rules when the right tool went unused. In the policy-evolution phase, a small open model (roughly 3B active parameters) is fine-tuned on successful tool-use trajectories collected with the frozen library, on training formulas screened to be disjoint from all evaluation benchmarks. Ablations show the two phases are complementary: with no tool library at all the same model solves almost nothing, the tools account for most of the gain, and trajectory training adds a further gain that is largest on the most difficult problems. The full system solves 79.1/71.3\% of LSR-Synth problems at fit tolerances $10^{-2}$/$10^{-3}$, reaches 63.8\% pooled accuracy on the distributionally different SRSD-Feynman panel, and obtains a normalized CP3-28 aggregate of $-7.27$. These results suggest a broader recipe for scientific agents: let the model and its instruments improve each other under verifiable feedback.

---


### 557. [Auditing Failure Attribution: Label Predictability and Judge Behavior](https://arxiv.org/abs/2610.17747)

**<font color=#1a73e8>作者：</font>** Tianyang Xu, Jing Gao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Failure-attribution benchmarks ask an LLM judge which step or agent caused a failure. A high score should mean the judge checked the faulty step against the run (a cross-step check). However, spurious signals (surface cues) that predict the annotation can produce a high score. In this paper, we propose four tests to separate checking from cue use. Input restriction asks whether partial input predicts the annotation. Cue following checks whether moved cues change answers. Residual accuracy scores judges where cue-only predictors fail. Aggregation asks whether the failure mix or metric changes rankings. Real observations motivate these tests: on three benchmarks, simple predictors match or beat GPT-4.1. In two Who&When Pro systems, a classifier reading one step's reasoning finds 95-100% of faulty steps, motivating input restriction. In one of them, error injection leaves no reasoning after the faulty step; judges fine-tuned on its labels beat GPT-4.1 by 41 points. Adding task-related reasoning after that step moves this cue: fine-tuned judges lose 31-99 points, but zero-shot judges lose at most 9, motivating cue following. On Aegis, blaming every agent matches GPT-4.1 on micro-F1 but trails by 19 points in exact-set accuracy, motivating aggregation. We recommend reporting these tests when developing failure-attribution benchmarks.

---


### 558. [Degrees of Freedom in Multi-Agent Coordination: Between Centralized and Decentralized Regimes](https://arxiv.org/abs/2610.17751)

**<font color=#1a73e8>作者：</font>** Yiqing Peng, Hehai Lin, Zixuan Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems (MAS) are commonly organized around two coordination regimes. Centralized coordination provides explicit control but can create a bottleneck at a single coordination locus, whereas decentralized coordination offers local autonomy but must achieve effective collaboration through distributed decisions and experience. These trade-offs motivate a systematic study of the space between the two regimes. We introduce Degrees of Freedom (DoF), a continuous configuration framework that quantifies the size of the decision space delegated to downstream agents. DoF controls the granularity of delegated work and the target probability that each task unit is assigned to the branches. Its endpoints recover the two coordination regimes. Across multiple task domains, DoF reveals a hierarchy of organizational effects. Delegated granularity and within-regime routing produce structured but bounded profile reallocations, whereas task domain and retained experience are associated with stronger differences between the centralized- and decentralized-branch profiles. The resulting performance landscape is task-dependent: different domains favor different DoF configurations, while atomic-target conditions are more consistent across runs. In-domain retained experience brings the two branch profiles closer together. The same controlled sweep reveals a task-dependent coordination landscape: some domains exhibit higher-performing configurations, whereas others show flatter responses and no single configuration dominates across domains. In five of the six evaluated state, an intermediate DoF configuration achieves higher mean accuracy than both endpoints, demonstrating the value of exploring the coordination space between them. Together, these findings provide empirical guidance for studying and designing intermediate coordination regimes in LLM-based MAS.

---


### 559. [Instructions Are Evidence, Not Objectives: Measuring Outcome Alignment of Agents](https://arxiv.org/abs/2610.17757)

**<font color=#1a73e8>作者：</font>** Kaiming Liu, Yuxuan Liu, Jinrui Ju 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents can follow complex human instructions to solve real-world tasks. In practice, however, initial instructions are often incomplete. In our analysis of 100 user-agent trajectories from SWE-chat, 56\% of initial instructions omit requirements that later emerge as necessary, and 52\% of the useful follow-up requirements could have been inferred from the project. A user states requirements from their own understanding of the task, and these \textbf{stated requirements} often differ from the \textbf{true requirements} that completing the task imposes. An agent should therefore treat the instruction as evidence rather than as the objective, inferring the true requirements from the instruction and the environment and satisfying them even when the user is not yet aware of all of them. We call this ability \textbf{outcome alignment}. In this work, we construct \textbf{TiGanEval}, a benchmark of software engineering and research tasks. In every task the user genuinely lacks part of the requirements, each requirement stays discoverable from the code and runtime behaviour of the environment, and requirements the agent infers are separated from those the user adds after observing delivered work. These properties together make outcome alignment measurable. Evaluating eight frontier models including GPT-5.6-Sol, we find outcome alignment broadly missing: the models lose 53 to 67 points of success rate when moving from the full specification to the partial instruction, and consequence feedback across four submissions does not close the gap. Furthermore, a plan-mode harness cannot compensate for the missing ability of the model itself, which places outcome alignment among the abilities the next generation of models should be developed for.

---


### 560. [Memory Echo in Single-Agent Long-Term Memory: Lifecycle Evaluation and Provenance-Guided Mitigation](https://arxiv.org/abs/2610.17763)

**<font color=#1a73e8>作者：</font>** Yufeng Li, Sheng Yao, Peng Zeng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory supports agents across sessions. Repeated retrieval and write-back can let one historical claim occupy multiple retrieval positions and influence current answers without independent evidence. Existing work examines retrieval, updating, and question answering, leaving same-source record accumulation and post-correction persistence underexplored. Motivated by research in social cognition and memory psychology on repeated exposure, retrieval, and revision, we define \emph{Memory Echo} as the excess retrieval exposure gained by historical information from the same source without additional independent evidence, and introduce MEchoBench to evaluate its emergence, correction resistance, persistence, and effect on answers. To address this phenomenon, we introduce the Family--Provenance--Authority framework (FPA). Specifically, FPA selects one representative per source family, conditions the eligibility of old records for the answer context on verified corrections, and constrains final answers with authoritative evidence. In paired replay on 190 fixed questions across four memory frameworks, FPA raises accuracy from 0.825 to 0.920 with DeepSeek V4 Flash and from 0.782 to 0.916 with Kimi K2.6; mean Decision Contamination Effect falls from 0.106 to 0.030 and from 0.109 to 0.038, respectively. These results show that agent memory can preserve traceable history without allowing repeated historical information to govern current decisions. The code is available at this https URL.

---


### 561. [Many Right Answers, One Training Example: Removing Responder Noise from GRPO for LLM Recommenders](https://arxiv.org/abs/2610.17771)

**<font color=#1a73e8>作者：</font>** Xin Li, Hao Jiang, Jinghao Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A recommendation request on Reddit draws several replies, each naming different titles. When an LLM recommender is trained on such threads with reinforcement learning (RL), which replies should a generated list be rewarded against? The state-of-the-art recipe, Rank-GRPO, picks one reply per training example, so the advantage mostly records which reply was drawn (85% of its variance) rather than how good the list is. We argue that RL should train on the request, not on each answer, and propose ReMaRk: it scores every list once against the union of all replies' titles and samples each request equally. This makes RL cheaper. On seven backbones and three datasets, ReMaRk reaches the validation recall of 2,000 per-reply RL steps in 25 to 53% of the steps and leads at that budget; trained until neither improves, it is never significantly behind Rank-GRPO and in four of seven pairs reaches Rank-GRPO's best with fewer GPU-hours. The same reward helps on ProtoQA, where about 100 people answer each question, which points to a simple rule for RL with several valid human answers: reward them jointly.

---


### 562. [Beyond Belief Nesting: Rethinking Higher-Order Theory of Mind in Large Language Models](https://arxiv.org/abs/2610.17777)

**<font color=#1a73e8>作者：</font>** Shanshan You, Zhengqi Wang, Hao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Theory of mind (ToM), the ability to reason about others' mental states, underlies effective communication and coordination. Its higher-order form enables reasoning over nested perspectives in strategic interactions. However, existing evaluations often equate belief-nesting depth with reasoning order, allowing nominally higher-order questions to admit lower-order shortcuts. We formalize effective order through the distinct events supporting successive belief prefixes, revealing widespread order inflation across existing benchmarks. We introduce HopToM, with certified full-order questions and controls for lower-order alternatives. Under direct prompting, mean accuracy across four frontier LLMs falls from 73.5% at first order to 20.0% at fourth order, and human participants also struggle. Causal interventions link a recurring class of errors to evidence for shallower belief prefixes. We introduce HopTrace, a plug-and-play inference-time method that encodes each interaction once into perspective records and resolves nested queries deterministically. On certified narrative questions, it improves fourth- and fifth-order accuracy by 22.0 and 38.5 percentage points over strong prompting baselines, while using 20-39 times fewer tokens than multi-call methods. These results sharpen how higher-order ToM is evaluated and offer a practical way to improve perspective reasoning in interactive agents.

---


### 563. [GENDIS: Gender-Related Discourse and Stance in Multilingual YouTube Comments from India, Kenya, and Nigeria](https://arxiv.org/abs/2610.17778)

**<font color=#1a73e8>作者：</font>** Luise Koch, Manuel Tonneau, Niyati Malhotra 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Research on gender-related online content is often operationalized through harm-centered tasks that collapse non-harmful gender-related and unrelated content, while existing datasets remain concentrated in high-resource languages and Global North settings. To bridge these gaps, we introduce GENDIS, a dataset of 9,600 multilingual, human-annotated YouTube comments from India, Kenya, and Nigeria (3,200 per country), annotated using a two-level framework that first identifies whether gender is referenced and then classifies gender-related content as negative, positive, or neutral. This separation provides a denominator for gender-related discourse independent of harm, enabling both prevalence estimation and characterization of its evaluative range. In the uniform random stratum, 23.8-35.0% of comments are gender-related, and among those with a resolved stance, 82% are neutral or positive. Across models, gender-reference detection is substantially easier than stance classification, especially for positive and neutral speech. Lightly supervised classifiers match frontier zero-shot large language models at substantially lower cost and outperform generic toxicity detection, while cross-country transfer remains limited. GENDIS provides a locally grounded resource for measuring when gender is invoked online and how that reference is framed.

---


### 564. [Full-duplex Spoken Language Modeling with Discrete Diffusion](https://arxiv.org/abs/2610.17780)

**<font color=#1a73e8>作者：</font>** Chen Chen, Pin-Jui Ku, Ankita Pasad 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Diffuplex, a full-duplex spoken language model based on discrete diffusion that achieves an unprecedented balance between linguistic intelligence and response efficiency. With thinking mode, Diffuplex delivers 13.0 tokens per forward pass, reaching an average of 1872 tokens per second and substantially surpassing the frontier autoregressive (AR) models in decoding speed. Without thinking, Diffuplex matches the first-audio latency of existing full-duplex models while achieving markedly stronger linguistic intelligence. This capability is enabled by separating when to say from what to say at the training level, rather than compressing both into a single autoregressive timeline. During inference, Diffuplex continuously tracks the user speech through an AR interaction policy, while independently generating and refining response content through parallel diffusion. Consequently, semantic computation is no longer bounded by the perception audio frame rate, allowing intelligence and responsiveness to improve simultaneously. Taken together, these results establish a new paradigm for spoken agents that can sustain real-time dialogue while devoting parallel computation to intelligent response generation. Training code and checkpoints will be avaliable soon.

---


### 565. [Agentic4PDM: Host-Governed Evidence Admissibility for Industrial Fault Diagnosis](https://arxiv.org/abs/2610.17786)

**<font color=#1a73e8>作者：</font>** Nam V. Nguyen, Hoang Van Truong, Hieu D. D. 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study industrial fault diagnosis as a classification task that assigns sensor time-series windows to predefined health states or fault types. Scarce labels and changing operating conditions make repeated training of specialized classifiers costly. Yet structures such as periodicity, trends, and transients can remain diagnostically informative and be examined through reusable analytical tools. LLM agents can select and interpret these tools, but fixed rules or training-derived guidance may not resolve each signal's ambiguity, while unconstrained interpretation may overstate weak or conflicting results. We introduce Agentic4PDM, a framework that separates adaptive investigation from control over evidence use. LLM agents compare each signal with labeled references from every candidate class, identify unresolved distinctions, and propose follow-up measurements. A deterministic software controller, called the host, enforces contract-checked gated adjudication (CCGA): it checks requests, requires commitment to a complete tool batch before results are observed, and assigns evidence roles based on tool checks against labeled references. These roles distinguish corroborative support from advisory information. The Judge Agent proposes a diagnosis, while the controller checks protocol compliance and records the investigation. Agentic4PDM supports training-free diagnosis using pretrained representations and labeled references without task-specific diagnostic models, and a standard setting that additionally investigates trained-model predictions. Experiments on selected bearing and motor diagnosis challenges and an unfiltered industrial test set supplied by our customer show gains in aggregate macro F1 over the evaluated diagnostic and agentic baselines. Ablations further support the value of the governed workflow.

---


### 566. [When, Where, and Why: Hierarchical Causal Explainability for Video Face Understanding with MLLMs](https://arxiv.org/abs/2610.17791)

**<font color=#1a73e8>作者：</font>** Anubhav Kataria, Shreya Ghosh, Jingwen Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding facial behaviour in video requires answering three fundamental questions: when a key facial expression occurs, where the model attends on the face at that moment, and why that evidence is necessary rather than merely correlated. Today's multimodal large language models (MLLMs) can label and describe video, but they rarely provide faithful explanations, especially for small facial movements that change over time. We present VideoFace-X-LLM, a framework for explainable facial video understanding comprising two key components. First, we introduce ExplainFace, a weakly supervised video-text corpus for facial behaviour understanding, automatically constructed from CelebV-HQ videos and validated through human evaluation and a two-model audit (at most 2.3% contradictions), demonstrating consistent gains across two backbone architectures. Second, H-TCC (Hierarchical Temporal Spatial Causal Concepts), which finds the key temporal moments (When), the facial regions (Where), and verifies its causal necessity (Why) through targeted occlusion. Fine-tuning on ExplainFace raises appearance Macro F1 from 19.48% to 32.87% (+13.39), with gains of +4.38 on actions, +6.77 on temporal emotion, and +11.84 F1 on deepfake detection. We also measure the explanations pointing lift, face/edge lift, stability, an Adebayo sanity check, and a necessity test rather than only showing examples. Our models, code, and corpus are available on request for research use.

---


### 567. [MHVF: Training-Free GUI Grounding via Verification-Guided Multi-Hypothesis Search](https://arxiv.org/abs/2610.17792)

**<font color=#1a73e8>作者：</font>** Minghua Chen, Xingming Liao, Weiqiang Zhong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GUI grounding enables web agents to translate natural-language instructions into actionable interface locations. However, dense layouts and small, visually similar controls can lead models toward plausible but incorrect elements, while refinement around a single prediction may leave alternative targets unexplored. We propose the Multi-Hypothesis Verification Framework (MHVF) for training-free GUI grounding. It combines multi-hypothesis exploration with local visual verification using a single pretrained vision-language model. To explore alternative targets, MHVF constructs spatial hypotheses from multiple full-screen predictions and examines the corresponding regions through zoomed re-localization. To resolve ambiguity among the resulting candidates, it verifies their agreement with the instruction in marked local views. Verification scores then guide a second round of local search and rank candidates retained from both search levels for final selection. Experiments with five general-purpose and GUI-specific models across eight benchmark settings demonstrate improvements in grounding accuracy in most settings. MHVF improves UI-Venus-Ground-7B by 4.3 and 2.1 percentage points on Mind2Web and VisualWebBench, respectively, and raises Qwen2.5-VL-7B's accuracy on ScreenSpot-Pro from 23.6% to 53.6%.

---


### 568. [GIFT-Eval-CTX: A Benchmark For Contextual Forecasting Model Evaluation](https://arxiv.org/abs/2610.17794)

**<font color=#1a73e8>作者：</font>** Xu Liu, Hanshu Yan, Taha Aksu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextual forecasting seeks to improve time series forecasting by incorporating forward-looking information, such as planned events, external conditions, and expert expectations. However, reliable evaluation remains difficult: existing benchmarks often have limited domain coverage, lack standardized history-future splits, or provide text that is not guaranteed to inform the future. We introduce GIFT-Eval-CTX, a benchmark that isolates whether forecasting methods can translate verified future information into accurate numerical trajectories. Built upon GIFT-Eval, GIFT-Eval-CTX contains 10,000 instances across 20 datasets. Each instance provides structured effects derived from the realized future: Macro effects describe horizon-wide behavior, while Micro effects specify localized changes. We construct these annotations with an agentic pipeline combining LLM-based discovery and deterministic code validation. We benchmark TSFMs, frontier LLMs, and tool-using agentic systems. The results show that structured effects reduce aggregate relative MASE by 40.7% for GPT-5.6 Sol and 29.6% for Claude Opus 4.8 relative to history-only prompting. The evaluated MoiraiAgent system achieves the best overall result. We further analyze the contributions of structured effects and agentic systems to performance, and identify opportunities for future research.

---


### 569. [Perturbation, Not Provenance: Why Activation Steering Does Not Make a Robust Text Watermark](https://arxiv.org/abs/2610.17810)

**<font color=#1a73e8>作者：</font>** Sergey Pletenev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linear directions in the activation space of large language models causally and universally influence model behavior. This suggests that they might serve as a basis for a robust text watermark. The idea is to steer the generation along a specific semantic direction and then recover the mark by probing the activations of the re-encoded text. We test this hypothesis by conducting a series of experiments. We vary the strength of the steering and use four different directions (formality, sentiment, complexity, and a random control) across two different model families. We also test two paraphrasing attacks: a sentence-level one and a stronger paragraph-level one. The results show that activation-steering watermarks are outperformed by a standard logit-based watermark (KGW) in terms of detection accuracy. At a matched level of fluency (within 1.15 times the original text's perplexity), KGW achieved an AUC of 0.81 against a sentence-level paraphraser, while the best steering direction only reached 0.65. A stronger paragraph-level paraphraser lowered both (0.65 for KGW and 0.59 for steering), narrowing the gap but not reversing it. On Qwen, it left the two indistinguishable but at near-chance levels for both. We further showed that the detectability provided by steering was not semantic: a random direction was just as detectable as a meaningful one. The signal was independent of which layer was probed and whether a surface feature control was used. We conclude that, in this case, semantic activation does not encode a localized, recoverable semantic mark, but rather a global, content-independent shift that can only be strongly detected when the text is degraded.

---


### 570. [Empowering Edge Agents: A Systematic Analysis of Edge-Cloud Collaboration in LLM Agent Execution](https://arxiv.org/abs/2610.17816)

**<font color=#1a73e8>作者：</font>** Pengcheng Huang, Zhenghao Liu, Shixin Ren 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Edge-cloud collaboration combines the lower inference overhead and greater data locality of edge-side execution with the stronger capabilities of cloud-hosted models. However, as LLM agents increasingly operate in long-horizon scenarios, cloud participation becomes interleaved throughout execution rather than a one-shot decision for each query. Such interleaved participation introduces trajectory-level effects that remain insufficiently understood. To address this gap, we introduce EC2-Bench, a benchmark for evaluating edge-cloud collaboration in long-horizon agent execution. It provides executable digital-workspace agent tasks and a unified evaluation framework covering task performance, resource usage, and privacy exposure. Using this benchmark, we empirically study diverse forms of edge-cloud collaboration. Our study reveals three findings. First, collaboration achieves a favorable balance among task performance, resource usage, and privacy exposure compared with edge-only and cloud-only execution. Second, as edge models become stronger, collaborative execution approaches cloud-only performance, and performance differences across strategies shrink, while privacy exposure remains strongly strategy-dependent. Third, stronger edge capability shifts preferred collaboration from externally controlled cloud participation and direct cloud execution toward more edge-controlled collaboration. Further analyses identify cloud-invocation decision-making and instruction following as important edge-side abilities for effective collaboration. These findings provide a systematic understanding of edge-cloud collaboration in long-horizon agent execution and insights for designing future edge agents that effectively collaborate with cloud models. Code and resources are available at this https URL.

---


### 571. [Same Attack, Different Judge: A First Controlled Adversarial Comparison of Jev, LLM Judges, and Purpose-Built Safety Classifiers](https://arxiv.org/abs/2610.17820)

**<font color=#1a73e8>作者：</font>** Xiang Li, Aichun Huang, Mingming Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> TypeSafe AI's Jev is a new kind of safety judge. It generates no text and no label: it answers questions the developer defines in advance and returns a probability for each answer. The vendor admits that adversarial input can change these answers but gives no numbers. In this paper, we present the first controlled adversarial evaluation of Jev. We build a test harness that sends every system the same payload under the same policy, and run it on four public-data tasks, from rule-based ones (input moderation, injection detection, routing) to a judgment-based one (phishing detection), with fifty attack variants from thirteen families. The targets are Jev, five GPT and GLM judges, and two local classifiers (Llama Guard 3, Prompt Guard 2). We find that Jev is the most robust system on input moderation: eight forgeries of its structured input bypass none of its decisions, and a sentence asking only why someone might make a harmful request bypasses 9% of its blocks, against 56% for GPT-6 Astra. On phishing detection. However, the same forgeries bypass 19-29% of the emails it flags, and even without attack Jev detects only 62% of phishing emails, against 77-81% for the GLM judges. Jev is also the fastest judge, but it flags the most benign requests (27%). The local classifiers fail differently: a training-example statement makes Llama Guard 3 miss 62% of the phishing it had flagged. These results suggest that Jev resists attacks on tasks with a clear rule to check but is more exposed on tasks that call for an overall judgment.

---


### 572. [Checking the Checkers: A Synthesis of Verifier Noise and Robustness in RLVR](https://arxiv.org/abs/2610.17824)

**<font color=#1a73e8>作者：</font>** Savyasachi Gupta, Aniruddha Srinivas Joshi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become a principal recipe for improving the reasoning of large language models (LLMs). It rests on the assumption that the checker scoring each response is itself correct. In practice, rule-based checkers reject correct answers in unexpected formats, unit tests accept incorrect programs, and LLM judges can be led to approve empty or adversarial responses. This work surveys 58 studies that measure, analyze, or mitigate such verifier errors. We ask what errors verifiers make, how they affect training, which mitigations work against which errors, and how the findings extend to self-generated, rubric- and judge-based, and verifier-free rewards. The evidence suggests that the structure of an error matters more than its rate. Random errors mostly slow learning, though under a fixed budget or KL regularization they also lower final accuracy. False positives that the policy can learn to trigger can cause plateaus or collapse, sometimes even with a low initial error rate. Whether a verifier wrongly rejects or accepts depends on what it checks and who built it, not on its family. Its errors shift as the policy improves, and most mitigations have been tested against only one kind of error. We compile the findings into comparison tables, reconcile apparent conflicts in the literature, and propose a reporting protocol to make future results comparable.

---


### 573. [Agentic-MatriBO: Capability-Compiled Agentic Bayesian Optimization for Materials and Chemical Design](https://arxiv.org/abs/2610.17832)

**<font color=#1a73e8>作者：</font>** Yu Zeng, Yuchuan Chen, Ziyue Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Materials and chemical optimization must choose the next synthesis, characterization, or high-fidelity simulation from sequential observations under a limited budget. Large language models can use task knowledge to propose adjustments, but composing surrogates, acquisition functions, and search strategies is constrained by compatibility, parameter dependencies, and evidence requirements. We present Agentic-MatriBO, a capability-compiled agentic Bayesian optimization (BO) framework that represents BO components and selection conditions as composable capabilities. A language policy proposes BO recipes and candidate plans; a compiler checks proposals against the registered capability catalog; and a deterministic execution layer validates and commits candidates. Oracle observations are stored in research memory and inform later rounds. We compare Agentic-MatriBO with eight baselines on four offline finite candidate pools---COF, PCE10, Buchwald--Hartwig (BH), and Suzuki--Miyaura---using five seeds per condition; results are reported descriptively. Across the four tasks, Agentic-MatriBO has the best mean endpoint quality after orienting each objective so that higher is better. On COF, it reaches the tabulated optimum in all five seeds both in the end-to-end comparison and after shared initialization, where it also retains an advantage in cumulative quality. Its normalized area under the best-so-far quality curve during the BO stage (nAUC-BO) is substantially higher on COF, near parity with the best baseline on PCE10 and BH, and lower on Suzuki. COF ablations show that removing the capability compiler or evidence gate coincides with lower cumulative quality and fewer exact-optimum hits. The framework provides an inspectable interface for evidence-conditioned BO adaptation.

---


### 574. [ProtoArena: Can AI Agents Discover and Exploit Real-World Cross-Component Protocol Vulnerabilities?](https://arxiv.org/abs/2610.17837)

**<font color=#1a73e8>作者：</font>** Fasheng Miao, Zhaoyu Hu, Xiang Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly used for vulnerability analysis, yet existing benchmarks provide limited coverage of exploitation that depends on interactions among network protocol components. Such vulnerabilities arise from inconsistencies in message interpretation, timing, state, or trust assumptions across participants. We introduce ProtoArena, a black-box, multi-component, dynamic benchmark with 80 cross-component vulnerability-exploitation environments spanning 11 protocol and application domains and 7 attack categories. Tasks are primarily informed by published protocol-attack mechanisms. Agents interact with running systems through scoped interfaces to achieve security-effect objectives without target source code. Three information levels assess guided reproduction, exploitation with mechanism and topology context, and effect-directed black-box exploration. A hybrid verifier combines rule-based checks with LLM review of independently collected traffic and logs. We evaluate five LLMs. Claude Opus 4.8 achieves the highest observed success rates: 48.8% under L1 guidance and 12.5% under effect-directed black-box L3. In a separate DNSBomb optimization experiment, it achieves a peak downstream-response to average query-input byte-rate ratio exceeding 171,000 times. The results show that agents can achieve verifiable exploitation effects in some cross-component environments, but success with limited black-box information remains low and varies across domains and attack categories. All experiments use controlled, explicitly authorized targets; they do not test production systems or disclose previously unknown vulnerabilities.

---


### 575. [Learning Adaptive Deliberation Control for Reliable Recognition with Multi-Agent Language Models](https://arxiv.org/abs/2610.17840)

**<font color=#1a73e8>作者：</font>** Yuan Liu, Haoyue Peng, Fanliang Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent deliberation can improve recognition by criticizing and revising candidate answers, but fixed controls cannot respond to changes in disagreement or reasoning quality. We present an adaptive multi-agent controller (ADMA) that learns continuous policies for proposal, challenge, arbitration, and coordination while keeping the task model frozen. Shared trace features describe quality, agreement, and progress, while role-specific features support decentralized control during inference. One controller trained on legal and financial reasoning is transferred without policy updates to four textual and multimodal benchmarks and two successive task-model versions. With Qwen3.5 held fixed, ADMA-Full improves accuracy by 6.2-14.2 percentage points over Direct and by 2.8-3.0 points over ADMA-Fixed. Paired bootstrap ranges for the Full-Fixed comparison are positive on three tasks. Outcome decompositions show that recoveries exceed introduced errors, while process assessment records fewer false-consensus events and more supported correct outcomes. Transfer to Qwen3.6 remains task dependent, which bounds the generality of the learned policy. Median token and latency ratios are 14.3-18.7 and 7.8-16.5 relative to Direct. These results show that adaptive deliberation can improve fixed-model recognition when its task-dependent gains justify the additional computation.

---


### 576. [What Makes a Good Visual Representation for Spatial Understanding in MLLMs?](https://arxiv.org/abs/2610.17844)

**<font color=#1a73e8>作者：</font>** Xiaohu Huang, Yumin Guo, Kai Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial understanding is a necessary step in moving multimodal large language models (MLLMs) toward reasoning about the 3D physical world. Their visual pretraining data, however, is almost entirely 2D, so the visual tokens processed by MLLMs often lack inherent 3D structural information. A growing number of methods inject such structure by transferring representations from external vision or geometry models, and collectively establish that such transfer helps. Behind these methods lies a largely underexplored question: what makes a visual representation good for spatial understanding? To answer it, we first separate what is transferred from how it is transferred, and then trace the resulting differences back to properties of the representations themselves. What we transfer comes from 3D geometry models, self-supervised image and video models, vision-language models, and generative models, in the form of latent features or explicit depth and point maps. We transfer it either by distillation, using it as a supervision target, or by fusion, feeding it as an additional input. We find that a representation's 3D structure correlates strongly with how much it helps, measured by cross-view consistency for latent features and by depth and reconstruction accuracy for explicit geometry. We further show that the form of a representation dictates the mechanism it needs. Latent features gain as much from fusion as from distillation; explicit geometry gains little from fusion, and most of its distillation gain depends on a geometry decoding head. Guided by these findings, we distill both latent features and explicit geometry into a single MLLM. Taking only RGB video as input, it consistently improves over its base model on both static 3D and dynamic 4D spatial reasoning benchmarks.

---


### 577. [DVTR-KD: Distilling Vision-Language Models via Intermediate Visual Token Reconstruction](https://arxiv.org/abs/2610.17853)

**<font color=#1a73e8>作者：</font>** Haolan Wei, Jiahui Wang, Junli Zha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have achieved strong performance on diverse vision-language tasks, but their computational demands limit deployment under constrained budgets, particularly on edge devices. Many works focus on Knowledge Distillation (KD) and try to transfer knowledge from powerful teacher models to students. In addition to reducing model size, visual token compression provides a complementary route to efficiency, but introduces mismatched visual token counts that complicate direct token-wise knowledge transfer. To mitigate this, we propose DVTR-KD, a knowledge distillation framework based on \textbf{D}ense \textbf{V}isual \textbf{T}oken \textbf{R}econstruction, which reconstructs the teacher's dense visual tokens from the student's compressed tokens. We reconstruct visual states after the final LLM layer and at the input to an intermediate layer identified as important for visual-information readout. At the intermediate layer, reconstruction is supervised through the teacher's response predictions rather than by direct token-wise KL or MSE matching. An auxiliary attention-readout loss complements this response-level supervision by aligning how the student and the original teacher integrate contextual information when predicting responses. Evaluations on diverse benchmarks demonstrate that DVTR-KD improves the performance of token-compressed students while retaining the inference efficiency afforded by visual token compression.

---


### 578. [MMTA: Benchmarking Multimodal Temporal Analysis with Time Series, Text, and Vision](https://arxiv.org/abs/2610.17856)

**<font color=#1a73e8>作者：</font>** Ziyang Zhang, Shenyi Li, Yilin Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series analysis is increasingly studied in multimodal settings, yet most benchmarks pair temporal signals with text or with visualizations derived from the same signal. This leaves open whether multimodal large language models (MLLMs) can integrate time series with real-world visual evidence. We introduce MMTA (multimodal temporal analysis), a benchmark of tri-modal tasks with diverse cross-modal complementarity patterns among time series, text, and vision. MMTA spans nine domains -- robotics, autonomous driving, human action, manufacturing, AR assistance, healthcare, recommendation, finance, and climate -- under video+TS and image+TS layouts, with a 3,524-sample test split covering classification and forecasting. The benchmark standardizes heterogeneous real-world sources into a shared schema with domain-specific prompts, provenance documentation, and success-weighted metrics that penalize both wrong answers and failed generations. Evaluating eight open-source and proprietary MLLMs reveals a shared bottleneck: representing time series as text creates very long token sequences and weakens fine-grained alignment with visual evidence, especially in long-video settings. We then introduce TimeOmni-v, a multimodal LLM extension with a dedicated time-series encoder, temporal positional alignment, modality-aware token layout, and a forecasting head. TimeOmni-v improves long-video classification and time-series inference efficiency, showing that MMTA not only exposes representation and grounding failures but also motivates targeted model design.

---


### 579. [Socratic Skill Learning: Interleaving Teaching and Practice for Transferable Agent Skills](https://arxiv.org/abs/2610.17860)

**<font color=#1a73e8>作者：</font>** Letian Zhu, Han Li, Yifan Yao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent Skills improve LLM agents by making task knowledge reusable across sessions. Learning transferable Skills requires evidence about a procedure and its conditions of use, which a successful task attempt can leave untested. We introduce Socratic Skill Learning (SSL), which interleaves expert teaching with Student practice. An Educator guides investigation while the Student remains the sole environment operator and Skill author, able to question, test, and adapt advice. To test reuse beyond the learning task, we construct SkillTransferBench, with 35 task families and 408 executable cases, pairing public variation specifications with held-out evaluation in fresh solver sessions. On the main 22-family, 155-case cohort, Fixed-Window SSL reaches 0.801 utility, versus 0.723 without a Skill, 0.761 for adapted Trace2Skill (trajectory distillation), and 0.751 for adapted SKILL-KD (contrastive distillation). Across three model pairs on shared families, interleaved guidance outperforms expert authoring and post-hoc teaching. Process analysis links guidance to Student writing and package revision; a case study shows the Student testing and refining a proposed procedure for later reuse. As demand for new lessons falls, the cost of fixed-window review grows. Issue-Guided SSL tracks unresolved questions across Skill revisions to select and focus review, reaching 0.805 utility with 61.7% fewer Educator tokens and 16.9% fewer total acquisition tokens than Fixed-Window SSL on the main cohort.

---


### 580. [MicroCLIP: Connecting Text and Microscopy Images via Contrastive Language--Image Pretraining](https://arxiv.org/abs/2610.17866)

**<font color=#1a73e8>作者：</font>** Yanran Ruan, Zhixiang Wei, Shiyao Hong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding fluorescence microscopy images is fundamental to automating biological research. However, existing methods typically learn predefined concepts from closed-set data, limiting transfer across tasks and biological contexts. In this work, we introduce MicroCLIP, a vision-language model that learns generalizable cellular and subcellular representations from natural language supervision for open-set image classification and retrieval. To pretrain MicroCLIP, we construct MicroPool-2M, a dataset of approximately 2.5 million fluorescence microscopy image-text pairs spanning diverse cellular structures, cell lines, and imaging conditions. Aligning microscopy images with biological concepts in natural language is challenging because most images lack descriptive captions and biological knowledge annotations. We therefore progressively establish image-text associations at three levels to provide MicroCLIP with richer semantic supervision: (1) category-level alignment links images to standardized labels defined by subcellular structure-cell-line combinations; (2) knowledge-level alignment incorporates biological priors derived from these labels to capture relationships across species and cell types; and (3) detail-level alignment uses a multimodal large language model to recaption and verify image-text pairs at scale, emphasizing fine-grained visual characteristics. Extensive experiments demonstrate that MicroCLIP achieves leading performance in zero-shot classification and text-image retrieval on microscopy images. It retrieves images with specific cellular characteristics from thousands of candidates and generalizes to unseen biological concepts without additional supervision. These results highlight MicroCLIP's potential as a foundation model for fluorescence microscopy.

---


### 581. [RT-J: Large-Scale Pretraining of Relational Transformers for Context-Efficient Predictions](https://arxiv.org/abs/2610.17867)

**<font color=#1a73e8>作者：</font>** Rishabh Ranjan, Vignesh Kothapalli, Harshvardhan Agarwal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models for tables and relational databases are increasingly used for predictive tasks across various scientific and industrial domains. However, adapting existing models to unseen datasets requires tens of thousands of examples. Here we introduce RT-J, an 85M-parameter relational foundation model (RFM) that makes accurate predictions even with hundreds of in-context examples or fewer. To achieve this, we first assemble the Join, a large collection of 639 web-crawled databases with 6,023 LLM-generated forecasting tasks. We pretrain with long contexts of up to 8,192 database cells, using in-context examples from a novel lightweight random-walk retriever. Finally, we leverage context tuning and ensembling to scale up test-time compute. On in-context regression tasks from RelBench, RT-J requires 10x fewer examples on average to match strong feature engineering pipelines with LLM-agent or RDBLearn featurizers and TabICLv2 or LightGBM predictors. Overall, our work pushes the frontier for context-efficient predictions on relational data and highlights the importance of real-world semantics, context engineering and large-scale pretraining for RFMs.

---


### 582. [Prefilling-dLLM v2: Learned Chunk Routing for Long-Context Diffusion Language Models](https://arxiv.org/abs/2610.17868)

**<font color=#1a73e8>作者：</font>** Qi Han, Jing Xiong, Ziyuan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models apply bidirectional attention over the whole context at every denoising step, so a longer context makes each step substantially more expensive. Sparsifying only at inference leaves the pretrained weights unchanged, so the model is never trained under the sparse pattern it runs with. We propose Prefilling-dLLM v2, which continues training a diffusion language model so that it routes with its native mask token. One mask is appended at the end of each chunk, and a learned role offset marks it as a routing slot. On every fourth layer, a query keeps a bidirectional local window and the top-K chunks scored from that mask; the other layers use a bidirectional sliding window. Starting from Dream-v0-Base-7B extended to 16K with YaRN, we compare Prefilling-dLLM v2 with bidirectional NSA, DSA, and SWA under the same layout, key budget, and dense initialization, using the same Fast-dLLM decoder. With the YaRN factor scaled to the evaluation length, Prefilling-dLLM v2 leads the other sparse methods on all three RULER tasks from 16K to 128K. Its mean accuracy at 128K is 7.4 points above NSA, the next sparse model, while DSA and SWA remain near zero. At the same length, decoding is 172x faster than with full dense attention.

---


### 583. [ECMR: Evidence-Aware Deliberation Control for Multi-Agent LLM Reasoning](https://arxiv.org/abs/2610.17869)

**<font color=#1a73e8>作者：</font>** Yuan Liu, Haoyue Peng, Fanliang Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent Large Language Model (LLM) systems typically commit to a deliberation protocol before inference. A fixed protocol cannot allocate computation differently to resolved and unresolved instances, and it may mistake repeated support for independent confirmation. We study this failure as semantic false consensus: a confident group answer supported by narrow, duplicated, or correlated rationales. We introduce ECMR, an evidence-aware controller over frozen role-conditioned LLMs. At each step, ECMR summarizes answer concentration, support diversity and independence, contradictions, role behavior, verification history, and remaining budget, then selects whether to propose, challenge, verify, arbitrate, diversify, correct a role, or stop. We formulate this decision as finite-horizon budgeted control and derive sufficient conditions under which state conditioning, risk-triggered verification, and role correction improve cost-adjusted utility. Across a declared held-out evaluation of 9,000 records from MedQA, CaseHOLD, and FinQA, ECMR-Full increases pooled accuracy from 62.1% to 84.9%, reduces false-consensus rate from 40.7% to 17.0%, and raises evidence-support rate from 58.0% to 88.7%. State shuffling loses 11.7 accuracy points with only 0.7 fewer rounds, while harder traces shift from early stopping toward arbitration. ECMR-Full uses the largest token budget, yielding the strongest absolute reliability rather than uniformly superior token efficiency.

---


### 584. [Cross-Lingual Transfer of Evil Vectors Is Directionally Asymmetric](https://arxiv.org/abs/2610.17880)

**<font color=#1a73e8>作者：</font>** Juann Kim, Minku Kang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persona vectors are linear directions in the residual-stream activations of LLMs that encode behavioral traits and enable fine-grained control over model behavior. Among them, the evil persona vector is particularly relevant to understanding harmful behavior, jailbreak vulnerabilities, and the unlearning of harmful knowledge. Yet whether this vector reflects a genuinely cross-lingual concept, rather than an artifact of its extraction language, remains untested. We conduct a systematic evil-vector transfer study across two high-resource languages (English, Spanish) and two low-resource languages (Swahili, Telugu) on four open-source instruction-tuned LLMs, and find that transfer is directionally asymmetric. Evil vectors are harder to obtain reliably from low-resource languages, and the resulting vectors are largely ineffective at steering, even within their own language. In contrast, vectors extracted from high-resource languages transfer effectively to low-resource inputs while largely preserving general knowledge, as measured by MMLU. Geometric analysis further supports this pattern: evil vectors from the two high-resource languages are closely aligned, whereas low-resource vectors align only weakly with this shared direction. These results suggest that a shared cross-lingual evil direction exists and, once reliably extracted from a high-resource language, can be reused to steer behavior in low-resource languages without additional per-language data collection.

---


### 585. [Diagnose-to-Generate: Eliminating Structural Distortions in Flow Models via Patch-Level Grounded Alignment](https://arxiv.org/abs/2610.17882)

**<font color=#1a73e8>作者：</font>** Yifan Li, Lishuai Gao, Tong Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow-based image generators achieve strong semantic synthesis but still produce localized structural distortions, such as malformed hands and limbs. Existing post-training methods typically optimize global scalar rewards, which provide weak spatial credit assignment and may alter well-formed regions while correcting local defects. We present \textit{Diagnose-to-Generate (D2G)}, a grounded alignment framework that separates visual diagnosis from generative optimization. We construct \textbf{Achilles-600K}, a region-annotated dataset for structural anomalies, and train \textbf{ARGUS} through supervised cold-start and Region-Aware Group Relative Policy Optimization to predict anomaly categories and bounding boxes. These diagnoses are converted into confidence-weighted spatial rewards for our \textbf{Patch-level Flow-GRPO}. We further identify that global stochastic exploration can shift semantic regions across group rollouts, making patch-wise relative advantages spatially inconsistent. Our \textbf{Trajectory-Preserving Stochastic Sampling (TPSS)} anchors early denoising with deterministic ODE trajectories and introduces stochasticity only at later steps, thereby limiting intra-group spatial drift while retaining local exploration. Experiments on FLUX.1-dev and SD3.5 show improved structural fidelity with preserved FID and CLIP scores. Consistent gains under HumanRefiner, zero-shot GPT-4.1, and blinded human evaluation further demonstrate that the improvements extend beyond the training reward model.

---


### 586. [Training LLMs for Multi-Agent Collaboration with Verifiable Information Rewards](https://arxiv.org/abs/2610.17893)

**<font color=#1a73e8>作者：</font>** Keru Chen, Sen Lin, Yingbin Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective collaboration among large language model (LLM) agents in multi-agent systems requires sharing relevant evidence, requesting missing information, and incorporating teammates' contributions into decisions. Training these behaviors is challenging because final task outcomes provide limited feedback on the value of individual messages. We introduce CoSIR (Collaboration via Surprisal-based Information Rewards), a post-training approach that uses a simple, verifiable environment to teach collaboration behaviors that generalize to more complex, unseen tasks. We propose a Bayesian evaluator that scores shared information by its reduction in team surprisal, defined as the sum of the negative log probabilities assigned to the correct option given each agent's available evidence. Requests are scored by the potential reduction in the same quantity if the requested information were truthfully provided. Separate rewards encourage agents to use the received information in their private choices and calculations. We post-train Qwen3-4B, Qwen3-8B, and Gemma-3-4B-it through self-play and evaluate transfer to seven unseen natural-language collaboration tasks. CoSIR achieves the highest aggregate score, while its performance in general tasks remains competitive. Behavioral analyses show increased disclosure of private evidence and fewer judged failures to use teammates' input.

---


### 587. [Swiss4Arg: A Parallel Dataset for Multilingual Argument Mining across Swiss National Languages](https://arxiv.org/abs/2610.17894)

**<font color=#1a73e8>作者：</font>** Sophia Conrad, Fatma-Zohra Rezkellah, Christina Niklaus 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Swiss4Arg, a multilingual dataset for argument mining based on official Swiss voting brochures, covering all four national languages: German, French, Italian, and Romansh (a Romance minority language exclusively spoken in Switzerland). The brochures contain explicitly formulated arguments systematically organized into pro and con sections, resulting in a cross-lingually aligned resource with balanced argumentative stance. We create a dataset that comprises 53 federal voting issues collected between 2019 and 2025, annotated for argument components (major claims, claims, premises, and non-argumentative units) and relations (support and attack) by three native speakers per language. Inter-annotator agreement (Krippendorff's alpha) reaches 0.548 for component classification and 0.623 for relation and target classification, computed jointly across all annotators on the parallel data. We release both adjudicated labels and individual annotator annotations, enabling analyses of disagreement and cross-linguistic variation, and provide baseline results using GPT-5.4 and SwissBERT. Swiss4Arg establishes a novel benchmark for multilingual argument mining, with a particular focus on cross-lingual comparability and low-resource settings such as Romansh. The dataset and code are publicly available at this https URL (HuggingFace) and this https URL (GitHub).

---


### 588. [Interaction-as-a-Judge](https://arxiv.org/abs/2610.17895)

**<font color=#1a73e8>作者：</font>** Wayne Chi, I-Hung Hsu, Li Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coding agents are tasked with producing sophisticated interactive applications such as websites, desktop applications, and games. While humans assess these applications interactively, current automated LLM evaluations primarily focus on code analysis and unit tests. This mismatch can cause LLM judges to miss failures that are immediately apparent to human users. We study Interaction-as-a-Judge, an evaluation paradigm where computer-use agents (CUAs) directly interact with an application. We demonstrate that Interaction-as-a-Judge can improve both \emph{evaluation} and \emph{generation} of interactive applications. To this end, we collect and release two complementary datasets: $6,858$ pairs of applications with human preferences and corresponding agent traces, and $222$ applications with human-verified requirement labels. Relative to standard non-interactive approaches, we find that Interaction-as-a-Judge improves evaluation in terms of predicting human preferences ($65.6\% \to 69.1\%$) and requirement verification ($77.0\% \to 81.6\%$). We also observe scaling benefits: across both preference alignment and requirement verification, higher-quality interactions improve performance. Finally, through both inference- and training-time experiments, we demonstrate that Interaction-as-a-Judge can also improve the quality of generated artifacts. At inference time, Interaction-as-a-Judge repairs $75.5\%$ of broken requirements within five attempts, compared to $55.4\%$ for code-only self-feedback. At training time, using Interaction-as-a-Judge as a reward signal improves win-rate over the base model by $6.7$pp while reducing both generated code length by $35.7\%$ and build failure rates by $7.2$pp compared to a code-only reward signal.

---


### 589. [Evaluating the Causal Faithfulness of SHAP as a Candidate Attribution Method for SAE Features](https://arxiv.org/abs/2610.17898)

**<font color=#1a73e8>作者：</font>** Samuel Xie, Noura Al-Moubayed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders decompose language model representations into interpretable features, but feature interpretation in this literature remains predominantly correlational. Attribution methods offer more direct estimates of feature influence, yet their faithfulness to actual causal effects has not been systematically evaluated in the SAE setting. We apply SHAP-based attribution to SAE latent features and evaluate it against direct causal intervention, using sentiment classification on SST-2 with GPT-2 Small and a 32,768-feature layer-7 SAE as a testbed. We compare SHAP to Integrated Gradients, Gradient$\times$Input, and probe-weight baselines across linear and MLP probe arms, scoring each against feature ablation and activation steering measured through the language model's own logit difference. Most faithfulness associations we measure do not survive multiple-comparison correction, and attribution methods that agree strongly with one another ($\rho = 0.42$--$0.80$) agree poorly with measured causal effects, indicating that inter-method agreement is not evidence of causal faithfulness. Two effects hold under control. First, local per-example attribution retains a directional advantage over global averaged attribution, while its apparent importance advantage is explained by feature activity rather than superior causal ranking. Second, under known-ground-truth minimal pairs, attribution recovers inserted sentiment signal well above chance (AUROC $0.792$) but fails to localize deletions (AUROC $0.520$), suggesting that these methods detect the presence of a feature's influence more reliably than its absence. We argue that importance faithfulness and directional faithfulness are separable properties requiring separate evaluation, and that attribution agreement should not substitute for causal validation.

---


### 590. [Visual Dependence Does Not Imply Answerability: A Systematic Analysis of Answerability Signals in Frozen InstructBLIP](https://arxiv.org/abs/2610.17902)

**<font color=#1a73e8>作者：</font>** Minjun Kim, Hyunmin Song, Changwon Lim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual question answering models often produce plausible responses even when the available visual evidence is insufficient to support a valid answer. Although prior work has introduced benchmarks and abstention mechanisms for unanswerable visual questions, it remains unclear which signals derived from a frozen vision-language model reliably indicate answerability on unseen image-question pairs. We systematically evaluate answerability signals on a stratified 10K subset of UNK-VQA using frozen InstructBLIP, covering predictive uncertainty, cross-modal alignment, visual grounding, visual dependence, internal representations, and learned probes. Answerability discrimination remains weak, with test AUROC largely confined to 0.50-0.54. CLIP alignment yields the highest point estimate but does not significantly outperform generation confidence under paired bootstrap analysis. Targeted removal of question-relevant visual evidence causes substantially larger changes in answer confidence than same-size random masking, yet intervention sensitivity provides essentially no answerability discrimination. Increasing probe capacity, combining multiple signals, and adding reason-aware supervision do not provide robust improvements, while post-freeze cross-validation yields similarly weak discrimination. Selective-answering analysis shows limited usable coverage under low-risk operating criteria. Failure-mode analysis shows that the relative utility of individual signals varies across perturbation mechanisms. Taken together, these results show that, on our UNK-VQA subset with frozen InstructBLIP, visual dependence, uncertainty, semantic alignment, and static representations are not robust standalone proxies for answerability. Our findings emphasize the need to distinguish a model's reliance on visual evidence from whether that evidence is sufficient to support an answer.

---


### 591. [DriveWLA: Unifying Future Dynamics and Scene Semantics through World-Language-Action Modeling for Autonomous Driving](https://arxiv.org/abs/2610.17903)

**<font color=#1a73e8>作者：</font>** Shuzheng Wang, Haoxuan Li, Shengzhen Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) and world models have demonstrated strong capabilities in semantic understanding and future scene evolution for autonomous driving. However, effectively integrating both capabilities for trajectory generation remains challenging. In this work, we propose DriveWLA, a unified World-Language-Action model based on Mixture-of-Transformers (MoT) that jointly models semantic understanding, future scene dynamics, and trajectory generation. DriveWLA consists of three experts: a World Expert for future prediction, a Language Expert for semantic understanding, and an Action Expert for trajectory generation. We further introduce Cross-Expert Attention, which enables controlled information flow across experts while aligning semantic and dynamic representations. To improve trajectory generation beyond imitation learning, we apply Flow-GRPO reinforcement learning post-training to refine the Action Expert. Extensive experiments show that DriveWLA achieves superior performance in both open-loop and closed-loop evaluation. DriveWLA achieves 92.3 PDMS on NAVSIM v1 and 90.1 EPDMS on NAVSIM v2, demonstrating strong performance among VLM-based and world-model-based planners. Without specific fine-tuning, DriveWLA further demonstrates strong zero-shot generalization to HUGSIM, nuScenes, and Bench2Drive. These results validate the effectiveness of our unified World-Language-Action modeling, establishing DriveWLA as a generalizable framework for autonomous driving.

---


### 592. [Text-Only vs. Image-Aware VLM Judges for Manga Translation Evaluation](https://arxiv.org/abs/2610.17908)

**<font color=#1a73e8>作者：</font>** Subaru Kimura, Jun Suzuki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In manga translation, visual context outside speech-bubble text, including speaker identities, referents, and scene tone, is depicted in page images, making it natural to refer to images during translation evaluation. However, most conventional manga translation evaluations rely solely on text-only automatic metrics, leaving the impact of image input insufficiently explored. We propose a practical validation framework that employs the same vision-language model (VLM) as both a text-only judge (TOJ) and an image-aware judge (IAJ) to investigate evaluation divergences associated with image-aware evaluation procedures. We use a Japanese-English manga dataset of official translations aligned at the page and speech-bubble levels. First, adding page images to TOJ improved the primary VLM's detection of deliberately injected, visually dependent degradations. Second, we analyzed evaluation divergences between TOJ and IAJ, finding different error counts and error-category distributions. Human verification did not reveal a consistent preference between TOJ and IAJ.

---


### 593. [LinMorph: Learning to Morph Weights for Efficient Video DiT Linearization](https://arxiv.org/abs/2610.17914)

**<font color=#1a73e8>作者：</font>** Lingyi Long, Congyue Zhao, Xiaoou Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-hoc linearization is an attractive way to accelerate pretrained Video Diffusion Transformers (Video DiTs), yet existing methods largely treat the quality loss induced by attention replacement as a recovery problem. We show that a more fundamental bottleneck lies upstream: \emph{initialization}. Random initialization discards pretrained knowledge, whereas manual weight reuse transfers it through rigid and incomplete source--target correspondences. We introduce \textbf{LinMorph}, which recasts Video DiT linearization as a learnable softmax-to-linear weight transformation problem. Instead of copying predefined counterparts, LinMorph learns a cross-parameter morphism that lets each target Gated DeltaNet (GDN) parameter draw jointly from pretrained query, key, value, and output projections, including for parameters with no direct softmax counterpart. A single morphism is shared across layers and learned through local teacher alignment, while producing layer-specific initializations from their respective pretrained weights. The resulting weights are then materialized as independent GDN modules for progressive distillation and joint this http URL the morphism operates in weight space rather than token space, it can be learned on short, low-resolution clips and directly reused at larger video scales. Across pretrained Video DiTs, LinMorph enables markedly faster recovery and better final generation quality than random initialization and heuristic weight reuse. Results show that efficient linearization depends not only on how a converted model is recovered, but critically on how pretrained knowledge is transferred before recovery. Project page: this https URL.

---


### 594. [Batch-Paced: Fixed-Budget Batch Decoding in Discrete Diffusion Language Models](https://arxiv.org/abs/2610.17917)

**<font color=#1a73e8>作者：</font>** Shuai Zhang, Zhanchao Zhou, Huachuan Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As generative language models become more capable and widely used, inference demand grows, making efficient serving increasingly important. Discrete diffusion language models (dLLMs) offer a promising path to more efficient inference through parallel token generation. Prior dLLM decoding methods, however, focus on improving inference efficiency for individual sequences. We formulate fixed-budget dLLM batch decoding and introduce Batch-Paced, a training-free method that jointly optimizes the allocation of decoding compute across requests to improve overall batch quality. Across two dLLM backbones, five benchmarks and their representative mixtures, Batch-Paced improves batch performance under matched budgets; gains generally grow with batch size and largely persist across decoding configurations. Analysis of requests' decoding trajectories suggests that these gains arise largely by raising the committed-token confidence of lower-confidence requests. We further show that Batch-Paced's batch decode time remains competitive and that adding a decoding-depth allowance during Batch-Paced decoding can shorten it further at a modest performance cost.

---


### 595. [CineMem: Attention-Aligned Fine-grained Memory Retrieval for Multi-Shot Long Video Generation](https://arxiv.org/abs/2610.17926)

**<font color=#1a73e8>作者：</font>** Xiaoxue Wu, Xinyu Gao, Fang Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video generation relies on memory retrieval to model long-range dependencies. This capability becomes particularly critical for multi-shot generation, where models must reconcile substantial visual changes across shot transitions with persistent semantic continuity. Existing methods tend to perform memory retrieval at the frame level and share the same historical context across all query tokens, overlooking the heterogeneous information needs and leading to redundant retrieval and inefficient use of historical memory. To bridge this gap, we introduce CineMem, an attention-aligned fine-grained memory retrieval framework that combines online memory organization with query-adaptive retrieval for autoregressive multi-shot video generation. Specifically, guided by intrinsic memory-access patterns revealed through attention analysis, we propose an online-clustered KV cache as a memory organization strategy over all historical tokens, enabling semantic-aware memory grouping and more precise retrieval. In addition, we introduce a query-level retrieval mechanism that provides broader access to historical information under a fixed retrieval budget, thereby improving long-term memory utilization. Together, these designs enable the multi-shot video generator to preserve long-range consistency across shot transitions, particularly in revisitation scenarios, while approximating full-memory access under a constrained memory budget. To facilitate evaluation, we further introduce a suite of task-specific, VLM-assisted metrics for faithful inter-shot consistency assessment. Extensive experiments demonstrate the effectiveness of our framework.

---


### 596. [Learning How to Remember: Memory Modality Selection for GUI Agents](https://arxiv.org/abs/2610.17928)

**<font color=#1a73e8>作者：</font>** Taeyun Roh, Suhyeong Park, Gijin Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in vision-language models (VLMs) have substantially improved the capabilities of GUI agents, while memory augmentation has emerged as a promising approach for reusing knowledge from past interactions. However, existing memory augmented GUI agents typically adopt a fixed representation strategy, providing retrieved experience as a static modality. It remains unclear whether a single memory modality is consistently optimal, or how modality preference changes across interaction steps. In this work, we conduct a systematic study of memory modality in VLM based GUI agents. Across GUI benchmarks, we find that the preferred memory representation is strongly step dependent. Motivated by the finding, we introduce \textbf{SwitchMem}, a routing framework that dynamically selects between textual and visual memory representations at each step. Across three GUI benchmarks, SwitchMem outperforms memory augmented baselines that rely on static memory representations. Our findings validate our claim that memory modality is a step dependent decision rather than a fixed design choice. Code and project resources are available at this https URL

---


### 597. [HierarchiRetina: A Diabetic Retinopathy Screening and Grading Cascade with Heterogeneous Mixture-of-Experts Lesion Segmentation](https://arxiv.org/abs/2610.17933)

**<font color=#1a73e8>作者：</font>** Md Asif Uddin, Niloy Farhan, Rafeed Rahman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical screening for diabetic retinopathy proceeds in stages, yet most automated systems grade fundus images with a single black-box network. Three gaps remain: (i) lesions differ widely in size and contrast, but segmenters typically apply the same blocks to all; (ii) ungradable images are usually excluded or treated as an extra class, and lesion-aware graders seldom test whether lesions drive the grade; (iii) staged systems often report each stage only on the images reaching it, leaving propagated errors unmeasured. HierarchiRetina, a screening, segmentation and grading cascade with inspectable stage outputs, addresses each gap. First, HSMoE-AUNet is a U-Net whose skip, bottleneck and decoder blocks are sparse mixtures of heterogeneous experts, with lesion-matched types, counts and losses; SwinHRUNetPP, a dual-encoder vessel segmenter, uses a field-of-view-restricted loss. Second, LG-DRG separates gradability from ordinal severity and lets lesion masks query the image through gated cross-attention. Third, an end-to-end evaluation counts screening misses as errors and traces each error to its stage. Pooled Dice ranged from 0.184 (microaneurysms) to 0.579 (exudates); vessel Dice was 0.731. On 58,689 held-out images from six datasets, end-to-end quadratic weighted kappa was 0.804, with referral sensitivity 0.832 at specificity 0.947, and the screening gate caused 66% of errors. In ablations, the grade ignored the masks, even with the cross-attention gate started open. On all 4,105 official DDR test images, six-class accuracy was 85.6%, above the best published six-class result we found (83.8%). Staged screening systems should be evaluated end-to-end, with stage attribution and mask ablation, before clinical deployment.

---


### 598. [Provenance and Authorization in Autobiographical Language Models](https://arxiv.org/abs/2610.17935)

**<font color=#1a73e8>作者：</font>** Faruk Alpay, Taylan Alpay  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autobiographical language models may draw on archives containing observations, quotations, emotional reports, and earlier model outputs. Cryptographic authentication can preserve an archive while leaving these sources semantically conflated. We formulate this gap as a computer-security problem: narrative content must not silently become consent or alter an authorized decision rule. We define typed records, authenticated attestations, a separate policy channel, and admissible views. Under explicit assumptions, we give a standard integrity reduction and a noninterference argument, characterize the information required by exact decision-preserving summaries, and show why passive history and fixed-point convergence need not identify a preferred action. Alpay Algebra supplies a comparative language for iterative memory without being a premise of the proofs. Sociology of religious affiliation, source-monitoring psychology, and self-determination theory motivate distinctions in a bounded Latter-day Saint vignette. A separate, reproducible pilot uses a frozen public language model on 32 wholly synthetic cases across 576 paired conditions. It compares flattened records, source labels, and an explicit admission gate under contradictory summary repetition. The study concerns computational attribution and authorization, not the motives or psychology of the people in the vignette.

---


### 599. [MERIT: Multimodal Evidence Reasoning over Image Tables](https://arxiv.org/abs/2610.17937)

**<font color=#1a73e8>作者：</font>** Haoyang Jiang, Zhuotong Fan, Mingyang Yi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Table reasoning with language models typically assumes access to clean textual tables. In practice, tables are often serialized into text, which can corrupt cell contents, distort structural relationships, and discard visual cues, leaving the model to reason over incomplete evidence. In contrast, table images retain this information, but using it requires both accurate perception and reasoning grounded in the relevant cells. To address this, we propose MERIT (Multimodal Evidence Reasoning over Image Tables), a three-stage framework for learning to reason over table images, with serialized tables serving as optional auxiliary inputs (if provided). Our analysis identifies visual evidence acquisition as a bottleneck, motivating table-specific encoder adaptation through reconstruction, localization, and color-conditioned supervision. Building on the adapted representations, supervised fine-tuning teaches explicit evidence selection and reasoning using verified trajectories. Finally, reinforcement learning refines the policy with separate rewards for evidence correctness, calculation, final answers, and output format. By providing feedback on intermediate steps, the framework targets retrieval and computational errors that final-answer supervision alone does not distinguish. We evaluate the approach on table question answering and fact verification, analyze the contributions of visual inputs and training components, and assess generalization to additional datasets with different table structures and visual presentations.

---


### 600. [HaloBlock: Faster and Better Decoding for Diffusion Large Language Models](https://arxiv.org/abs/2610.17948)

**<font color=#1a73e8>作者：</font>** Zhaohui Zheng, Chenhang He, Jinrui Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) have attracted increasing research attention due to their bidirectional attention and arbitrary order decoding. However, there are two issues in dLLMs inference: the decoding difficulty is dominated by the tokens on the right side of the block, and the block-wise decoding inherently suffers from boundary contextual discontinuity. To tackle these limitations, we propose HaloBlock, a difficulty-aware adaptive halo mechanism for dLLM inference. We first leverage bidirectional cumulative entropy to characterize block decoding difficulty. Then, based on the bidirectional decoding difficulty, we adaptively allocate bidirectional halo regions on both sides of each block to mitigate boundary contextual discontinuity. The difficulty-aware design of HaloBlock smooths cross-block context propagation and lowers decoding difficulty for hard tokens, yielding better generation quality and faster convergence. Evaluated on LLaDA-8B-Instruct, Dream-7B-Instruct and LLaDA-1.5 across mathematical reasoning and code generation benchmarks, HaloBlock demonstrates consistent accuracy improvements and higher inference efficiency. Source codes are publicly available at this https URL.

---


> [!TIP]
> 当前位于：**551-600**（第 12/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-600** | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
