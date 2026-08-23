# 🧠 大模型相关研究 | 2026年08月24日

> 本类共 **121** 篇论文：已确认 **114** 篇，待复核 **7** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-121**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-121**

---

### 101. [InsufficiencyBench: Evaluating LLM legal advice on underspecified user queries](https://arxiv.org/abs/2608.20220)

**<font color=#1a73e8>作者：</font>** Samuel J. Vincent, Daniel Calloway, Fangyi Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Legal AI systems are increasingly used to answer legal questions, yet existing benchmarks assume queries arrive fully specified. In practice, users omit facts that materially determine the legal outcome. We introduce InsufficiencyBench, the first legal benchmark targeting query-side insufficiency: whether a model recognizes when a query lacks legally material information, identifies what is missing, and refrains from premature conclusions. We formalize a taxonomy of eight canonical missing-element categories across three structural failure modes---switch, gating, and fatal prerequisite--- and construct 202 benchmark items (58 base queries, 144 deficient variants) spanning six legal domains and 24 US jurisdictions and annotated by practising attorneys. Evaluating ten frontier models, we find that no model exceeds F2 = 0.46 on missing-element identification and that the median recall is 0.44. Models either hedge indiscriminately or answer silently under fabricated presumptions. No model both identifies and qualifies responses to deficient queries while directly addressing complete ones.

---


### 102. [Rule-Compliant Visual Spatial Planning for Multimodal Large Language Models](https://arxiv.org/abs/2608.20237)

**<font color=#1a73e8>作者：</font>** Yu Chen, Ting Lei, Yaoyi Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) combine linguistic reasoning with visual perception, yet their ability to perform visual spatial planning under explicit or previously unseen rule constraints remains underexplored. This setting requires models to jointly understand spatial layouts, interpret natural-language rules, and plan valid actions accordingly. To address this gap, we introduce RuleMaze, a controllable benchmark in which MLLMs must navigate mazes while obeying natural-language rules of varying complexity. RuleMaze isolates rule-compliant spatial planning by requiring accurate perception, rule interpretation, and constrained action planning. To enable scalable and systematic rule construction, we propose Language-Logic-Function Hybridization, which automatically generates natural-language rules and translates them into logical representations and executable validators, eliminating manual rule engineering. To improve rule following and generalization, we introduce Disentangled Multimodal Planning (DMP), which separates perception, execution, and rule verification through interpretable reasoning primitives. By disentangling these components, DMP facilitates systematic generalization to more complex and previously unseen rules, while providing transparent intermediate planning traces. Experiments demonstrate that DMP substantially improves rule compliance and planning success compared to end-to-end textual planning baselines. Overall, RuleMaze establishes a principled benchmark for studying grounded and interpretable rule-based spatial planning in MLLMs. Code is available at this https URL.

---


### 103. [Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation](https://arxiv.org/abs/2608.20256)

**<font color=#1a73e8>作者：</font>** Gijs Kassenaar, Zhao Yang, Vincent François-Lavet  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning language models trained with reinforcement learning typically operate under a fixed token budget rather than an explicitly adaptive one, which can lead to over-computation on easy problems and insufficient computation on difficult ones. We study whether a model can learn to allocate its own reasoning effort by choosing, as the first token of its response, one of three modes: \textsc{NoThink} (answer as quickly as possible), \textsc{Short} (brief reasoning), or \textsc{Long} (extended reasoning). The choice is learned inside Group Relative Policy Optimization (GRPO) with no separate router, through a shaped reward that makes each mode worthwhile at a different response length, together with hard per-mode token caps that keep the modes distinct. On a 1.5B distilled model trained on MATH, the three modes emerge without collapsing to a single choice, and the brief modes end up more accurate than \textsc{Long}, which shows that the router sorts problems by difficulty rather than at random. Averaged over three seeds, the resulting policy stays close to the base model's accuracy on the held-out MATH500 ($0.782$ vs.\ $0.796$) while cutting the mean response length from $4{,}796$ to $2{,}811$ tokens (a $41\%$ reduction). Interestingly, it also transfers to other benchmarks without retraining, with the largest savings where problems are easier, with for instance 76\% token reduction on GSM8K and at higher accuracy than the baselines at similar response length. In short, we build a reasoning model that adaptively chooses how much to reason for each problem.

---


### 104. [Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents](https://arxiv.org/abs/2608.20274)

**<font color=#1a73e8>作者：</font>** Yiyang Feng, Biddut Sarker Bijoy, Niranjan Balasubramanian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents can induce skills from completed tasks and reuse them later to grow more capable with experience. In practice, induced skills may transfer unreliably and can even harm the agent that retrieves them. When agent-induced skills transfer reliably across tasks remains an open question. We conduct a comprehensive and controlled study of how the way skills are induced shapes their transfer across tasks. Specifically, we compare task-level with subtask-level skill induction and text with code skill formats, the two axes along which existing methods differ. Task-level skills mostly reduce the agent's performance below its no-memory baseline while subtask-level skills raise it above on average, and text skills transfer better than code skills. To further understand our findings, we examine two complementary properties of the induced skills: specificity, which measures how closely a skill matches real tasks, and abstractness, which measures how evenly its relevance spreads across tasks. Neither property alone predicts task success, but their combined effect does, which we propose as a skill utility score. The score correlates consistently with task success when skills are transferred, and subtask-level and text skills score higher. Computing skill utility only needs the skills and task descriptions but not any task execution, so our score serves as a practical diagnostic of a skill memory before any new task runs.

---


### 105. [Inject, Align, Recover: Staged Post-Training for Retrieval-Free Document Knowledge Internalization](https://arxiv.org/abs/2608.20281)

**<font color=#1a73e8>作者：</font>** Qian Kou, Xiaofeng Shi, Xiaosong Qiu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often fail to answer questions about a bounded document collection when the source documents are not retrieved at inference time. We study this setting as document knowledge internalization: converting a fixed corpus into usable parametric knowledge for retrieval-free question answering. We propose IAR (Inject, Align, and Recover), a three-stage post-training framework that separates structured document knowledge injection, QA behavior alignment, and general ability recovery. Unlike conventional continued pretraining, Inject converts source documents into continuation, rewrite, and instruction-conditioned reconstruction objectives. Align then adapts the injected model with answer-only QA supervision, while Recover merges the domain-adapted model with the base instruction model to recover general capabilities. Across Common Corpus (CC) and CCI, and across Llama, Phi, Qwen, and SmolLM model families, IAR improves the domain-primary domain-general frontier for retrieval-free document internalization. In the main comparison, IAR improves over Vanilla SFT on all four reported metrics in 7 of 8 dataset-model settings, with average gains of 3.6 percentage points in domain QA accuracy and 12.1 percentage points in mean general performance across IFEval, MMLU, and MSBench. Extended CC baselines show that LoRA and FAPM can win individual general metrics, but among methods that also reach leading or near-leading domain internalization, IAR retains one of the strongest general profiles.

---


### 106. [Phantom Gains: Auditing Self-Improvement Against a Measured Null](https://arxiv.org/abs/2608.20290)

**<font color=#1a73e8>作者：</font>** Cheng Xu, Nan Yan, Liming Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Whether a language model has improved itself is increasingly judged not by mean accuracy but by which individual problems it gains and loses. Tracking these transitions means differencing two noisy estimates, leaving them vulnerable to measurement artifacts. Auditing three rounds of rank-$32$ LoRA self-training on Qwen3-8B against a frozen control pushed through the identical pipeline, we identify seven measurement failures, each of which inverts a reported finding when its control is absent. Several are standard practice. A ledger built on a single greedy decode manufactures capability changes on an untrained model, largely an artifact of inference batching; the expansion statistic separating acquisition from sharpening assigns that same model a rate of $0.280$. The natural threshold repair does not survive replication: estimated across the frozen comparisons such a design already contains, its null stays non-zero. We replace it with a per-problem exact test against a pooled baseline under false-discovery-rate control, which detects nothing on any held-out replicate and is unchanged under the multiple-testing rule, error rate and pool size. Applied to a ladder of arms matched in stream, volume and evaluation, the audit finds that external distillation improves problems the base model rarely reaches while three forms of self-training do not; a regression rejects this asymmetry as a by-product of distillation's larger overall gain ($p < 10^{-8}$). On the far smaller set of problems the base model never reaches, the evidence is inconclusive, while self-training corrupts problems solved at baseline at rates well above the measured floor. Transition-level auditing therefore requires a separately measured null for every statistic it reports: nulls that cost no new experiments, built from baseline replicates a multi-arm study already owns, though not from as few as most possess.

---


### 107. [MidTool: Mid-training Data Synthesis for Agentic Tool Use](https://arxiv.org/abs/2608.20314)

**<font color=#1a73e8>作者：</font>** Fengqing Jiang, Yite Wang, Boyi Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mid-training is increasingly recognized as a critical stage for shaping the capabilities of large language models. Recent work has shown that targeted mid-training can strengthen reasoning-intensive abilities such as math and science, and can also improve agentic capabilities in software-engineering settings. In this work, we study the parallel but less explored agentic capability: general tool use. We present MidTool, an open corpus construction pipeline for agentic tool-use mid-training that combines large-scale web, PDF, and code data with synthesized supervision from real-world tool APIs, MCP skills, and document-grounded workflows. MidTool is designed to teach models how to recognize tool affordances, ground arguments from context, compose tool call workflow, and recover from incomplete information. We mid-train Qwen3-4B-Base and Qwen3-8B-Base on MidTool-Mix, and then apply follow-up post-training with both supervised fine-tuning and reinforcement learning. Compared with baselines, MidTool-Mix consistently improves downstream performance under both SFT and RL on BFCL, tau2-Bench, and MCP Universe. These results suggest that general tool use, like other important LLM capabilities, benefits from dedicated mid-training rather than being left entirely to post-training.

---


### 108. [Explainable Transformer Models for Clinical Prediction Tasks on Structured Electronic Health Records](https://arxiv.org/abs/2608.20315)

**<font color=#1a73e8>作者：</font>** Jun Ni Du, Lukas Adamek, Maxim Kryukov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive models over structured electronic health records (EHRs) remain central to machine learning for healthcare, but few have jointly emphasized quantitative laboratory information and interpretability with respect to input medical events. We present BERT-LER, a BERT-style model for coded EHR timelines pretrained and fine-tuned from a de-identified EHR dataset of 75 million patients, that encodes laboratory test results as discrete tokens while retaining graded information through percentile-based binning, paired with Integrated Gradients for token-level attributions grounded in the input EHR sequence. We benchmark our approach on the public EHRShot benchmark suite and on an asthma severity progression study based on real-world data. This addresses a methodological gap in EHR foundation-style modeling by unifying laboratory value representation and explainability in a single framework, while assessing whether both predictive performance and explanations generalize beyond standard clinical prediction tasks. Across EHRShot and asthma tasks, BERT-LER achieves predictive performance that is competitive with, and on laboratory-related tasks often exceeds, publicly available benchmark models, and provides attributions that align with clinically known risk factors. Our architecture and explainability approach can be applied to many therapeutic areas and prediction tasks using language models trained on structured EHRs.

---


### 109. [Pandora's AI Model Routing Box: Efficient Allocation with Costly Value Estimation](https://arxiv.org/abs/2608.20316)

**<font color=#1a73e8>作者：</font>** Adam Fisch, Shubhendu Trivedi, Fantine Huot 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Heterogeneous AI systems composed of multiple models, architectures, harnesses, or inference-time settings can improve quality and efficiency by routing queries to the specialist who can answer most effectively at the lowest cost. Routing requires estimating each specialist's expected return, but this value estimation has a cost. Cheap estimators (e.g., embedding-based predictors) are fast but noisy, while accurate estimators (e.g., fine-tuned models with access to retrieval results or partial reasoning traces) are expensive. We formalize this tradeoff as an instance of Pandora's Box, the classical problem of optimal search with costly inspection. Under a Gaussian signal model, the resulting policies have closed-form value-of-information expressions that determine, for each specialist and input, whether refining the value estimate is worth its cost. We call the centralized policy Pandora's Router. We extend this to a decentralized setting, Pandora's Bidder, where specialists independently decide whether to invest in self-assessment before accepting an offered price to claim a query. Experiments across three domains---a standard multi-LLM benchmark, retrieval-augmented specialists, and LLMs with variable inference-time reasoning---show that Pandora's Router matches the routing quality of exhaustive estimation, while querying the expensive estimator far less often. In the decentralized setting, value-of-information reasoning improves allocative efficiency when competing estimates are accurate; when competing estimates are noisy, however, it can increase the strategic specialist's utility at the expense of others.

---


### 110. [AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement](https://arxiv.org/abs/2608.20318)

**<font color=#1a73e8>作者：</font>** Yizhe Chi, Wenyi Li, Deyao Hong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) asks whether an AI system can improve the process that produces AI systems, so that the next system inherits the improvement. That process is the training algorithm: a better objective or update rule improves the compute\mbox{-}capability exchange rate for every subsequent run, including the one that produces the next agent. Whether RSI is feasible therefore turns on whether an agent can design training algorithms. No benchmark isolates that ability: existing suites are won by collecting data or by tuning hyperparameters, and none tells a change to how a run is executed apart from a change to how the model learns. We present AI4AI\mbox{-}Bench, 10 frozen research repositories spanning 10 training algorithm families. In each task, an agent has 4 hours on one B300 to rewrite the training algorithm; its code is then rerun from scratch for up to 12 hours and scored by a fixed evaluator hidden from the agent, against the repository's original algorithm under the same procedure. Because the 10 metrics are incommensurable, every task is mapped onto one scale on which $0$ is an uninformative model, $0.1$ is the algorithm the repository ships, and $1.0$ is the task optimum. Across 29 configurations of 6 systems on all 10 tasks the mean score is $0.166$, and the best system reaches $0.250$: even the strongest closes under a fifth of the distance between the algorithm that was already there and the optimum. The submissions show where that distance went: most never change how the model learns at all, and the minority that do average $0.226$ against $0.126$ for the rest. More reasoning effort mostly buys the willingness to go there, taking that minority from $8\%$ of submissions to $64\%$ and the mean score from $0.094$ to $0.196$. We release the task suite, the evaluators and every scored submission, so that the measurement can be repeated as these systems change.

---


### 111. [Inducing Task Models from Computer-Use Traces](https://arxiv.org/abs/2608.20319)

**<font color=#1a73e8>作者：</font>** Yucheng Jiang, Zora Zhiruo Wang, Ruishi Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Naturalistic computer-use traces, passively recorded screenshots and mouse or keyboard actions, are a valuable resource for deriving symbolic, auditable, and reusable models of how everyday work is done. Such models matter as computer-use agents enter real work, where agents need to learn how tasks are actually performed, and organizations need to audit and reuse that knowledge. However, inducing such task models is challenging, as activity is observed only as low-level events and real-world work is multi-threaded with interleaved goals. Existing methods assume a given task or a single workflow, and produce step-level summaries rather than structured task models. We introduce Task Model Induction (TMI), which (i) discovers the latent tasks in an unconstrained trace, disentangling concurrent activity, and (ii) for each latent task, induces a task model pairing a hierarchical objective model of recursive goal decomposition with a procedure model of the control flow that organized the execution. Intrinsically, on controlled human and agent trajectories, TMI recovers interleaved tasks with 0.974 agreement against ground-truth groupings and reconstructs 74.9% of the observed execution steps, far more than the strongest workflow induction baseline. Extrinsically, skills derived from TMI's task models improve held-out task accuracy by 30.0% over the strongest baseline.

---


### 112. [An Agentic Approach for Active Data Collection, Travel Behavior Modeling, and Weather-Sensitive Demand Prediction](https://arxiv.org/abs/2608.20320)

**<font color=#1a73e8>作者：</font>** Narges Ahmadi, Yubo Jiao, Jônatas Augusto Manzolli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Travel behavior research increasingly combines digital data collection with predictive modeling, yet these stages are often developed and evaluated separately. This study proposes a three-agent workflow integrating conversational data collection, structured data processing, and behavioral prediction. A chatbot-administered, image-augmented stated-preference survey collected mode choices from student commuters across five predefined weather scenarios, yielding 454 respondent-scenario observations. Weather-related associations were analyzed using a multinomial logit model, while logistic regression and random forest provided machine-learning benchmarks. Nine locally deployed large language models (LLMs), ranging from 2 to 35 billion parameters, were evaluated across four zero-shot prompt-and-context conditions and extended through persona, few-shot, and vision-based configurations. Random forest achieved 69.6% five-class accuracy, while the best text-only zero-shot LLM reached 69.9% without task-specific fitting. Habitual travel information produced the most consistent gains, Expert framing generally outperformed Role-Play, and persona information was most useful when habitual travel information was unavailable. Few-shot prompting improved prediction for several models, with gains stabilizing after a small number of examples. Using the same weather images shown to respondents, the best vision-based configuration reached 71.5% five-class accuracy, indicating that visual context may provide additional predictive information for selected models. Overall, the study shows how conversational surveys, structured data processing, conventional behavioral modeling, machine learning, and multimodal LLM prediction can be coordinated within an auditable multi-agent workflow.

---


### 113. [WithEveryone: Unified Planning and Identity Grounding for Group Image Generation](https://arxiv.org/abs/2608.20336)

**<font color=#1a73e8>作者：</font>** Hengyuan Xu, Qixun Wang, Yiji Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identity-preserving image generation becomes increasingly unreliable when a scene must contain many specified people. Beyond retaining each identity, the model must bind every reference to a distinct person and location, while training-time identity losses must establish correspondence among several noisy predicted faces. We introduce WithEveryone, a unified framework for generating group images up to ten reference identities. WithEveryone injects each selected identity as an addressed token, predicts a structured identity--layout plan, and renders the plan as a visual condition. Its key objective, Layout-Grounded ID Loss, uses annotated face regions to supervise the intended identities directly, avoiding unstable embedding-based face matching; ID Representation Forcing additionally trains a prediction for each identity before image synthesis. On an identity-disjoint benchmark, WithEveryone achieves the highest target-context identity similarity, improving face similarity from 0.462 for GPT-Image-2 to 0.499, while reducing copy-paste artifacts from 0.169 to 0.055. It further covers 97.3\% of the requested identities with a duplicate rate of only 2.8\%. These results show that explicit identity--layout grounding enables identity-preserving generation to scale to larger groups without relying on direct reference-face copying.

---


### 114. [ConceptGuard: Benchmarking Context-Sensitive Unlearning in Large Language Models](https://arxiv.org/abs/2608.20338)

**<font color=#1a73e8>作者：</font>** Sahil Kale, Ian Harris  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) increasingly require selective removal of harmful or sensitive knowledge, called unlearning, yet existing methods and benchmarks fail to evaluate this capability completely. Current approaches rely on disjoint forget and retain sets composed of independent facts, and measure success using simple and direct factual recall. This framing fails to capture a key requirement of unlearning, namely the ability to eliminate harmful behaviors while preserving benign and beneficial knowledge. We argue that effective unlearning must operate at the level of concepts, ensuring complete removal of unsafe applications while maintaining their correct and useful usage, thereby achieving conceptually meaningful and complete unlearning. To better evaluate unlearning techniques from such a practical viewpoint, we introduce the notion of dual-use concepts: concepts that can be used in both harmful and benign contexts. Building on these concepts, we construct a benchmark called ConceptGuard where forget and retain sets are explicitly complementary in concept usage. Our benchmark uniquely enables unlearning to be explored and gauged at the level of concepts, instead of sparse facts, and evaluation is intent-sensitive with the goal of maximizing contextual separation to promote safer behavior. We demonstrate that current unlearning techniques perform poorly under this setting, showing weak contextual separation alongside poor performance in ROUGE and concept-level metrics. Our results reveal strong forgetting-utility trade-offs, limited gains in contextual sensitivity, and poor consistency in concept-level control across methods, and provide ideas for unlearning approaches that better align with real-world safety requirements. Our dataset is publicly available.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 115. [A Virtual Member of a Community of Practice for the Society of Petroleum Engineers: From Prototype to Deployment](https://arxiv.org/abs/2608.19199)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** John Boden, Joshua Eckroth, Dayne Freitag 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe the evolution of a virtual assistant, called ATHENA, designed to support the capture, retrieval, and dissemination of knowledge for members of a Community of Practice (CoP) related to the Oil and Gas sector. An evaluation of a first prototype involving 75 professionals from the Society of Petroleum Engineering (SPE) showed that ATHENA dramatically improved both their productivity and performance equality on a set of realistic well-planning tasks compare to their use of a state-of-the-art RAG baseline system. However, the evaluation also identified areas for improvement. This paper describes technical advances to our first prototype in the areas of multi-document retrieval, support for answer validation, and more focused proactive dissemination. Evaluation results show that this enhanced version of ATHENA provides better support for completing knowledge-intensive tasks related to well planning than does a state-of-the-art baseline. ATHENA has been integrated into the SPE Research Portal and is being deployed for use by the society's membership.

---


### 116. [Scientific Data Skills: Enabling Agent-Ready Scientific Data Services at Scale](https://arxiv.org/abs/2608.19625)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiaohan Huang, Qingqing Long, Xiaolei Du 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific data are increasingly used by AI agents, yet existing dataset representations provide limited support for autonomous discovery, interpretation, and invocation. This limitation stems from the fragmentation of scientific data across heterogeneous repositories and from dataset representations designed primarily for human use. To address this limitation, we introduce the Scientific Data Skill (SciDSK), an agent-ready representation that packages dataset-specific knowledge and operational guidance as a reusable agent skill. A SciDSK integrates dataset descriptions, scientific context, file organization, usage procedures, quality checks, and provenance information while retaining the underlying data in its original repository. We define a structured SciDSK specification and develop a systematic construction pipeline that grounds each SciDSK in authoritative dataset records and associated supporting materials. We further establish the Scientific Data Skill Bank, a unified platform that publishes SciDSK resources across six scientific disciplines and supports package access, persistent identification, and traceability to source datasets. We evaluate SciDSK through a retrieval benchmark for dataset discovery and controlled cases for dataset interpretation. The results show that SciDSK improves agent-driven dataset discovery and provides more precise and actionable support for dataset interpretation. These findings support the value of organizing dataset-specific knowledge in an agent-ready representation.

---


### 117. [Scaffolding Minds: Optimizing Latent Visual Target Representations for Multimodal Reasoning](https://arxiv.org/abs/2608.19669)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haoqiang Kang, Yinpeng Chen, Luyang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent reasoning has advanced multimodal reasoning through a two-stage training paradigm: (1) a helper image is encoded into latent tokens to teach visual chain-of-thought during a supervised fine-tuning (SFT) stage, and (2) these latent tokens are further refined with reward feedback during a reinforcement learning (RL) stage. In this paper, we identify two key limitations of this framework, one in each stage. First, the SFT stage typically relies on an off-the-shelf vision encoder to encode the helper image, yielding suboptimal latent representations that may not be well aligned with the downstream reasoning task. Second, existing RL methods treat the latent component only through deterministic regularization, which constrains policy drift but does not create alternative latent trajectories for exploration. To address these limitations, we propose Scaffolding Minds. Our approach learns a dedicated scaffolding encoder that provides an optimized target in latent space, and learns both the mean and variance of the RL sampler. We further show that these two improvements are complementary, together yielding substantial gains over strong baselines. Empirically, our method improves over the strongest latent-reasoning baseline by +9.5% on FrozenLake spatial planning, with the gain widening to +19% at 32x32 grid map, and by +5.2% on average across nine visual-centric reasoning benchmarks.

---


### 118. [Robust Cross-Modal Foundation Model Perception for Underwater Robots under Degraded Visual Conditions](https://arxiv.org/abs/2608.19710)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mohammad Arif Ul Alam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable underwater robotic perception remains difficult because optical imagery degrades under turbidity, wavelength-dependent attenuation, low illumination, scattering, and blur. Although sonar provides complementary information that is less affected by optical visibility, prior visual-sonar research has largely focused on feature alignment and nominal detection performance. We investigate cross-modal robustness as visual reliability deteriorates and assess whether pretrained visual foundation-model representations can be complemented by sonar under severe degradation. We use frozen DINOv2 as the visual encoder and construct a controlled five-level benchmark ranging from clean to extreme visual conditions. We compare conventional visual detection, frozen foundation-model representations, sonar context, fixed multimodal fusion, clean-trained adaptive gating, and degradation-aware gated fusion. Our method trains the fusion mechanism across the full range of degradation while keeping the visual and sonar encoders frozen, allowing modality contributions to adapt without fine-tuning the pretrained backbone. Under extreme combined degradation, the DINOv2 baseline achieves 0.4610 balanced accuracy, while degradation-aware visual-sonar fusion reaches 0.6152, a 33.5% relative improvement. The learned sonar contribution increases from 14.2% under clean conditions to 41.3% under extreme degradation, demonstrating adaptive redistribution of cross-modal reliance. Fusion provides the largest gains under severe turbidity and blur, whereas color attenuation alone yields little additional benefit. These results show that foundation-model representations remain valuable but insufficient under severe information loss, and that explicitly adapting fusion to modality reliability can improve robust underwater multimodal perception.

---


### 119. [RecPFN: Prior-Fitted Networks for In-Context-Based Recommendations](https://arxiv.org/abs/2608.19735)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** En Zhi Tan, Jia Xiang Lim, Bryan Lijie Chew 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce RecPFN, a prior-fitted network that brings in-context learning to sequential recommendation. RecPFN is pretrained entirely on synthetic clickstream environments sampled from a broad structural causal prior, enabling it to amortize Bayesian-style inference from a small support set. At inference, a lightweight decoder-only transformer conditions on a handful of domain sequences and produces next-item predictions for queries in a single forward pass, without any weight updates. Across eight public benchmarks, RecPFN achives state-of-the-art zero-shot performance while remaining strongly competitive with supervised methods in low-compute and low-data regimes. It is deployment-efficient and robust to domain shift, outperforming strong zero-shot baselines that rely on large real-interaction corpora. RecPFN provides a practical path toward generalizable, data-efficient recommenders and opens avenues for richer priors, longer-context ICL, and multimodal extensions. Code for training and evaluation is publicly available at this https URL.

---


### 120. [Scale-Aware Pretraining of Time Series Foundation Models via Multi-Patch Token Alignment and Hybrid Masking](https://arxiv.org/abs/2608.20005)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Taihua Chen, Xiang Ma, Yixin Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretraining time series foundation models across heterogeneous datasets necessitates effective handling of varying sampling frequencies. Current methods either employ dataset-specific patch sizes and separate FFNs, leading to fragmented representations, or enforce a fixed patch size that neglects inherent temporal variations. To address this, we propose SATS, featuring a scale-aware token alignment mechanism that treats patch size as an explicit notion of scale. By incorporating a contrastive-inspired alignment regularizer, SATS aligns representation spaces across scales while preserving distinct modeling capacities. Furthermore, a hybrid masking strategy combining random and contiguous masking is introduced to capture multi-scale temporal structures. Experimental results on LSTF benchmarks demonstrate that SATS achieves a 9.2% improvement in MSE and an 8.3% gain in GIFT-Eval MASE compared to competitive baselines. Notably, SATS consistently delivers SOTA performance while achieving a 65.6% increase in model efficiency over advanced baselines, highlighting its effectiveness and scalability in time series pretraining.

---


### 121. [Swift-Image: Exploring the Performance Frontier of Compact Unified Image Generation Models](https://arxiv.org/abs/2608.20334)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Taihang Hu, Zhao Wang, Zuan Gao 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Swift-Image, a compact unified model for text-to-image generation, single-image editing, and multi-image editing. Our goal is to explore how far a relatively small visual generator can be pushed through systematic training engineering under a constrained computational budget. Swift-Image adopts an efficient 6B single-stream DiT and a progressive training pipeline that evolves from broad semantic coverage to higher resolution, stronger visual quality, and unified generation-editing supervision. For post-training, we employ parallel expert reinforcement learning followed by multi-teacher on-policy distillation to alleviate interference among heterogeneous objectives. We further decouple high-level reasoning from pixel-level rendering with a Prompt Enhancer that translates user requests into generator-aligned visual specifications. For efficient deployment, structural pruning and few-step distillation produce 3B and accelerated variants. Swift-Image achieves leading aggregate performance among evaluated open-source models with only 6B parameters and 243K GPU training hours; the compressed 3B model incurs nearly no loss, while few-step distillation further improves aggregate editing performance with substantially fewer sampling steps. Our study also summarizes practical lessons for architecture, data curriculum, post-training, prompt enhancement, and model compression.

---


> [!TIP]
> 当前位于：**101-121**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-121**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
