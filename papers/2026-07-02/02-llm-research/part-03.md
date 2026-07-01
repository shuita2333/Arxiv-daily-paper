# 🧠 大模型相关研究 | 2026年07月02日

> 本类共 **121** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-121**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-121**

---

### 101. [Attend, Transform, or Silence: Operator-Level Visual Skipping for Efficient Multimodal LLM Inference](https://arxiv.org/abs/2606.31903)

**<font color=#1a73e8>作者：</font>** Zhaoyang Luo, Runmin Dong, Miao Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) increasingly process long visual-token sequences, increasing the overall inference computation. Existing acceleration methods usually remove visual tokens or skip visual-token updates in entire layers, but these coarse strategies may discard fine-grained evidence or suppress useful operators together with redundant ones. In this paper, we study visual-token computation from an answer-observable perspective and find that late visual-token updates can remain large while having little effect on answer-token representations. Motivated by this answer-silent redundancy, we decompose each Transformer layer into attention and FFN operators and show that useful visual computation is often operator-dominant and layer-dependent. We propose an operator-level visual-token skipping framework that preserves the full visual-token sequence while selectively bypassing redundant attention, FFN, or both. Experiments across three MLLM architectures and 10 VQA benchmarks show that our method achieves strong efficiency-accuracy trade-offs, reducing \textbf{33.7\%} TFLOPs on Qwen3-VL while retaining \textbf{99.5\%} of the vanilla model performance.

---


### 102. [Theory of Mind and Persuasion Beyond Conversation: Assessing the Capacity of LLMs to Induce Belief States via Planning and Action](https://arxiv.org/abs/2606.31916)

**<font color=#1a73e8>作者：</font>** Ben Slater, Matteo G. Mecattaf, Lucy G. Cheke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Theory of Mind (ToM) benchmarks for Large Language Models (LLMs) typically rely on passive question-answering formats, but the deployment of LLMs in increasingly agentic and autonomous forms demands new evaluations. In this paper we evaluate an agent's ability to induce specific belief states in other agents by taking actions rather than using conversational persuasion, a capability we call Non-Conversational Planning ToM (NCP-ToM). NCP-ToM is likely to be essential for many agent use-cases, including within user-assistant interactions and pedagogical contexts, but may also present manipulation or misinformation risks. Using a novel framework, NCP-ExploreToM, we subvert the conventional task structure by providing models with a set of belief state goals and requiring them to move objects or direct characters into rooms to achieve their goals. We evaluated six frontier models, including GPT-5, Gemini 2.5 Pro and the Claude 4 series, and a cohort of human participants, across 600 task instances. GPT-5 was successful on approximately 80% of tasks in the agentic setting, and was the only model to outperform human participants on our task, but was still less robust than humans across contexts. We additionally found that all models, like humans, performed better on tasks inducing true belief states than false belief states, which is a positive signal for alignment efforts. These findings highlight emerging social-reasoning capabilities in LLMs for non-conversational task completion and underscore the necessity of agentic evaluations for understanding the safety and alignment of autonomous social agents.

---


### 103. [Signed-Permutation Coordinate Transport for RMSNorm Transformers](https://arxiv.org/abs/2606.31963)

**<font color=#1a73e8>作者：</font>** John Sweeney  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern LLM workflows move coordinate-indexed objects across checkpoints: steering vectors, sparse autoencoders, top-$k$ neuron sets, attribution lists, and merge alignments. This is only well posed after fixing the model's residual-stream gauge, which we show is architecture-dependent: LayerNorm residual charts have permutation gauge $S_d$ (up to a global sign flip), while RMSNorm charts with generic per-channel gain have signed-permutation gauge $B_d = S_d \ltimes \{\pm 1\}^d$. Permutation-only alignment is therefore symmetry-incomplete for RMSNorm models. We introduce sign-marginalized Hungarian matching and prove a sharp failure mode: with decorrelated coordinates, raw signed-correlation matching has a structural permutation-accuracy ceiling at the positive-sign fraction of the true gauge, which sign-marginalization removes. We then make coordinate-preserving transport, not function-level merging, the primary object: composing saved-checkpoint local $B_d$ gauges along same-base fine-tuning trajectories recovers 91.1% of cross-run coordinates at 1500 steps versus 60.3% for endpoint matching, and the gain is not explained by merely routing through the base. The recovered gauge transfers tools that permutation-only alignment breaks: TinyLlama SAE reconstruction has NMSE 0.004 under $B_d$ versus 1.08 under $S_d$; Qwen sentiment steering preserves 95.8% of its effect versus 17.2%; refusal steering reverses sign under $S_d$; coordinate-preserving merges behave the same way. The same covariance governs stateful training: signed transport of AdamW state preserves the resumed trajectory, while permutation-only state follows a different one from a functionally identical checkpoint. Finally, gauge-sweep audits show index-level interpretability claims are reproducible only relative to an explicit gauge.

---


### 104. [MECoBench: A Systematic Study of Multimodal Agent Collaboration in Embodied Environments](https://arxiv.org/abs/2606.31966)

**<font color=#1a73e8>作者：</font>** Qingyun Liu, Jiwen Zhang, Jingyi Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models (MLLMs) have strong potential as embodied agents, but their ability to collaborate in visually grounded environments remains underexplored. To address this gap, we introduce MECoBench, a multimodal embodied cooperation benchmark with an evaluation platform spanning diverse real-world tasks, two cooperation structures, and three collaboration modes. Through extensive experiments across various MLLMs, we summarize three key findings: (i) Collaboration generally improves embodied task completion, but its benefits depend on balancing collaborative gains against coordination complexity. (ii) Communication is essential to collaboration gains, while the best collaboration mode depends on team size and model capability. (iii) Moreover, collaboration improves robustness under noisy priors and exploration conditions. Generally, MECoBench provides a systematic testbed for understanding the mechanisms and limits of multimodal embodied collaboration. Code and dataset are available at this https URL.

---


### 105. [TreeAgent: A Generalizable Multi-Agent Framework for Automated Bias Labeling in Forestry via Compiled Expert Rules and Vision-Language Models](https://arxiv.org/abs/2606.31976)

**<font color=#1a73e8>作者：</font>** Shiyi Chen, Nicholas Saban, Collin Hargreaves 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human-labeled data are widely used as reference annotations in ML, despite known variability across annotators in many expert-driven domains. In addition, expert annotation is slow, inconsistent, and remains a major bottleneck for scaling tasks like tree height bias classification in forestry remote sensing. We propose a multi-agent system (MAS) that orchestrates expert decision trees with Vision-Language Models (VLMs), treating the decision tree as a structural prior while VLMs perform localized semantic perception at individual nodes, with multi-agent voting to mitigate VLM stochasticity. We formalize a Decoupled Declarative Decision (D3) Framework that enables zero-modification generalization across diverse expert-defined decision structures. On a tree bias classification testbed, our framework outperforms supervised ML baselines and reduces the amount of expert labeling effort required. These results suggest that agentic orchestration of VLMs with expert priors can reproduce expert-defined labeling procedures at substantially lower annotation cost while maintaining interpretability.

---


### 106. [DigitalCoach: Communication and Grounding Gaps in Human and Agentic Computer Use Coaching](https://arxiv.org/abs/2606.31980)

**<font color=#1a73e8>作者：</font>** Meng Chen, Anya Ji, Tsung-Han Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agents are increasingly capable of automating software tasks, but can they teach humans how to use software themselves? We introduce DigitalCoach, a multimodal dataset of 72 human expert-novice computer use coaching sessions consisting of 22,752 dialogue turns grounded in 28.1 hours of screen and input event recordings across five software applications. We use DigitalCoach to evaluate whether state-of-the-art models can teach humans how to use computers. Automated evaluation shows that models differ from humans in how they coach: models provide more direct instructions, but fewer explanations, error diagnoses, and knowledge-check questions. When we fix the coaching method, models produce utterances similar to human references yet poorly grounded in visual context. Interactive evaluation confirms that model coaches cause learners to passively follow instructions without deeper engagement and fall short in visual grounding. DigitalCoach lays a foundation for collaborative and proactive computer use coaching agents.

---


### 107. [ERA: Entropy-Guided Visual Token Pruning with Rectified Attention for Efficient MLLMs](https://arxiv.org/abs/2606.31982)

**<font color=#1a73e8>作者：</font>** Yuhao Wang, Mu Qiao, Haiwen Diao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) incur prohibitive inference costs due to long visual token sequences. Training-free visual token reduction provides an efficient solution. However, existing methods distort attention distributions, giving rise to a phenomenon we term Attention Logit Collapse. To address this issue, we propose ERA, an Entropy-guided visual token pruning framework with Rectified Attention for efficient MLLMs. Specifically, ERA comprises three crucial components: Dual-view Entropy Pruning (DEP), Bias-aware Token Recycling (BTR), and Logit-preserving Attention Rectification (LAR). First, DEP identifies representative anchor tokens by jointly modeling visual diversity and head-wise saliency. BTR then recycles pruned tokens into their corresponding anchors while estimating a cluster-level logit bias. Building upon this, LAR injects the estimated bias into attention logits, effectively rectifying the collapse induced by token reduction. Together, these components preserve visual evidence even under aggressive compression, enabling robust performance across single-image, multi-image, and video settings on a wide range of MLLMs. Beyond delivering practical acceleration, ERA establishes logit-preserving visual token pruning as a principled framework for efficient MLLMs, unifying theoretical foundation, algorithmic design, and practical deployment. The code is at this https URL.

---


### 108. [CoLT: Teaching Multi-Modal Models to Think with Chain of Latent Thoughts](https://arxiv.org/abs/2606.31986)

**<font color=#1a73e8>作者：</font>** Lianyu Hu, Shengqian Qin, Zeqin Liao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning has enabled multi-modal large language models (MLLMs) to tackle complex visual reasoning tasks by generating explicit intermediate reasoning steps in natural language. However, this text-based reasoning paradigm is inherently slow at inference time with even thousands of tokens and fundamentally constrained by the expressiveness of natural language. In this paper, we propose CoLT, (Chain of Latent Thoughts), a novel framework that teaches multi-modal models to reason through a chain of latent thought representations instead of verbose text tokens, which can perform thinking with as few as 3 steps. Naively forcing the model to think with latent states easily produces meaningless semantics and makes training unstable. To effectively regulate the latent reasoning process, we introduce a lightweight external decoder that provides step-level supervision for each latent reasoning step in two complementary directions: a forward mode that decodes latent thoughts into the textual reasoning of the next step, and a backward mode that aligns decoder hidden states with the model's latent thoughts given preceding textual context. We further incorporate internal supervision that encourages coherent step-by-step latent transitions. The decoder and internal supervision are removed during inference to maintain high efficiency of latent reasoning. Extensive experiments on eight benchmarks demonstrate that CoLT not only outperforms existing latent reasoning methods such as CODI and SIM-CoT, but also surpasses latent visual reasoning approaches that rely on auxiliary images with costly annotation requirements. Compared to text CoT methods, CoLT can notably reduce the inference time by 10.1$\times$ and text decoding time by 22.6$\times$. Code is released at this https URL.

---


### 109. [Self-Study Reconsidered: The Hidden Fragility of Learning from Self-Generated QA](https://arxiv.org/abs/2606.32002)

**<font color=#1a73e8>作者：</font>** Ekaterina Alimaskina, Denis Shveykin, Gleb Molodtsov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly taught from synthetic question--answer (QA) supervision: a model generates questions about a document, answers them from the same text, and the resulting pairs are used to fine-tune, distill, or compress knowledge into another model. We show that this generation step is not neutral preprocessing. It is an implicit policy that both selects which evidence becomes training signal and decides how that evidence is answered, and it is fragile at both stages. When choosing what to ask, generators do not scan a document uniformly. Coverage saturates early and concentrates on salient spans, diverse prompts converge on the same regions, and what looks question-worthy is driven by local presentation. As a result, salient artifacts such as poorly cleaned markup can hijack question generation across model families and scales. When answering, the model that produces the supervision tends to obey instruction-like passages embedded in the text. This compliance depends on the intent and surface form of the passage rather than its strictness, and is worst under task conflict, where larger models comply more often. These failure modes arise from choices made during QA generation, so they can be reduced without changing the training loop. Tying each question to a fixed target reduces biased selection, and filtering instruction-like spans before answering lowers mean injection compliance from $88\%$ to $13\%$ in our evaluation while retaining nearly all clean text.

---


### 110. [AxDafny: Agentic Verified Code Generation in Dafny](https://arxiv.org/abs/2606.32007)

**<font color=#1a73e8>作者：</font>** Benjamin Breen, Austin Letson, Borja Requena Pozo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study agentic code generation in Dafny, where a model must generate both executable code and the proof artifacts for verification. We present AxDafny, a verifier-guided repair framework that iteratively generates implementations, invariants, assertions, and termination arguments. We also introduce LiveCodeBench-Pro-Dafny (LCB-Pro-Dafny), a benchmark of 250 competition-style programming problems translated into Dafny with formal specifications and a verifier-based evaluation harness. On LCB-Pro-Dafny, AxDafny substantially improves verification success over baseline GPT-5.5 performance. On DafnyBench, AxDafny achieves 92.7\% verification success, outperforming the strongest previously reported proof-hint baseline by 6.5 percentage points. Lastly, we show that verification success and runtime test performance measure different aspects of generated code.

---


### 111. [Surrogate Fidelity: When Can Open LLMs Explain Closed Ones?](https://arxiv.org/abs/2606.32008)

**<font color=#1a73e8>作者：</font>** Philippe Chlenski, Zachariah Carmichael, Ayush Warikoo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability (MI) requires full access to model internals, yet the APIs for most widely deployed language models at best expose log-probabilities over output tokens. This creates a surrogate problem: when do measurements made on open models allow us to make claims about a closed model? We evaluate surrogate fidelity at the prediction, attribution, and representation levels. For binary classification tasks, log-odds provide an API-compatible scalar readout of the model's representation space, and leave-one-out attributions provide insight into model behavior. Across eleven models spanning four families (Llama, Qwen, GPT, and Gemini), we find that prediction fidelity substantially overstates attribution fidelity: models that agree on what the answer is often disagree on why. We document an access-validity inversion: white-box signals like attention patterns and perturbation magnitudes are highly stable across models but only weakly predictive of causal attributions, which black-box input ablations capture by design. Mechanistic insight does not automatically transfer to closed targets, and prediction-level agreement is insufficient to warrant such transfer. Code and results are available at this https URL.

---


### 112. [CoMet: Context and Multiplicity Decomposition for Multimodal Uncertainty Estimation](https://arxiv.org/abs/2606.32012)

**<font color=#1a73e8>作者：</font>** Sanghyuk Chun, William Yang, Amaya Dharmasiri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty estimation has been a long-standing challenge in AI models; it amounts to "knowing what you don't know," and metacognition is notoriously difficult even for humans (cf. the Dunning-Kruger effect). Although it is still far from solved even in simpler classification systems, tackling it in multimodal large language models (MLLMs) is becoming increasingly important. Within MLLMs, uncertainty can stem from any of the diverse sources as well as from their relationships, and further can stem from the unbounded answers in the open-ended setting. To tackle the issues, we propose CoMet, an MLLM uncertainty estimation method by decomposing uncertainty into a context-specific term and a multiplicity-specific term. The former captures ambiguity induced by the given context (e.g., task or prompt), while the latter captures how many plausible answers determined by the context remain compatible with the given input. We train a lightweight post-hoc uncertainty module to estimate these quantities, which enables efficient uncertainty estimation without autoregressive answer generation or repeated sampling. Experiments on various open-ended multimodal benchmarks, hallucination detection, and multiple-choice visual question answering benchmarks show that CoMet consistently improves uncertainty estimation over existing baselines while remaining efficient in practice. Code is available at this https URL

---


### 113. [FedLAB: Traceable Semantic Codebooks for Federated Multimodal Graph Foundation Learning](https://arxiv.org/abs/2606.32016)

**<font color=#1a73e8>作者：</font>** Zekai Chen, Kairui Yang, Xuaner Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal graph foundation models aim to learn reusable knowledge from graphs enriched with text, images, attributes, and relational topology, thereby supporting diverse graph-centric and modality-centric tasks. In practice, however, such multimodal graphs are often distributed across decentralized clients, where raw contents and local structures cannot be centrally shared due to privacy constraints. This motivates federated multimodal graph foundation learning, which requires not only transferable representation learning but also intrinsic semantic traceability under strict data isolation. Existing methods usually exchange or store knowledge through parameters, prototypes, embeddings, or compact codebooks, which support optimization and transfer but do not explicitly expose how modality evidence, node semantics, and topology context jointly support predictions. To bridge this gap, we propose FedLAB, a traceable semantic codebook framework that organizes multimodal graph knowledge into typed hierarchical codebooks for modality evidence, node semantics, and topology context. FedLAB further refines these trace units through federated semantic barycenter pre-training while keeping raw multimodal contents and graph structures local. Extensive experiments on 10 benchmarks and 6 downstream tasks show that FedLAB improves over state-of-the-art baselines by up to 7.53\%, while preserving a native semantic trace interface.

---


### 114. [TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning](https://arxiv.org/abs/2606.32017)

**<font color=#1a73e8>作者：</font>** Yuanda Xu, Zhengze Zhou, Hejian Sang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning requires assigning credit to environment-facing actions such as searches, clicks, edits, navigation commands, and object interactions. Standard GRPO uses the final verifier outcome as a uniform advantage over all action tokens. This outcome signal is useful but structurally incomplete: it punishes useful exploration in failed rollouts and reinforces redundant or regressive actions in successful rollouts. We propose TRIAGE, a role-typed credit assignment framework that adds a semantic role axis to outcome credit. A structured judge classifies each segment as decisive progress, useful exploration, no-progress infrastructure, or regression, and a fixed role-conditioned rule maps these labels to bounded segment-level process rewards. This keeps verifier outcomes as the source of optimization direction while correcting the two main blind spots of outcome-only credit. We further show that role-conditioned credit is the optimal segment-level correction expressible from role labels alone -- a projection of the per-segment advantage residual onto the role variable -- so that the fixed role constants reduce advantage estimation error whenever the judge is reliable, and we connect this to lower-variance policy gradients. Across ALFWorld, Search-QA, and WebShop, TRIAGE improves success rates over GRPO for two policy models and outperforms both a scalar judge-derived process reward and an outcome-supervised shared-backbone value baseline. Ablations show that the gain comes from role typing rather than merely adding dense rewards: reliable detection of regression inside successful trajectories is the dominant contributor, while exploration credit provides a consistent secondary gain; on completed ALFWorld and WebShop rollouts, TRIAGE also reduces environment-facing turns by an additional $10.4\%$ and $14.8\%$ relative to GRPO.

---


### 115. [SemRF: A Semantic Reference Frame for Residual-Stream Dynamics in Language Models](https://arxiv.org/abs/2606.32022)

**<font color=#1a73e8>作者：</font>** Jian Gu, Aldeida Aleti, Chunyang Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residual-stream analysis asks how language-model computation evolves across depth, but intermediate decoding requires comparable readout coordinates across layers. If embedding anchors and unembedding readout disagree on the chosen span, apparent motion may reflect measurement drift rather than computation. We introduce \emph{Semantic Reference Frames} (SemRF), an anchor-based formalism separating semantic measurement from residual dynamics. A SemRF fixes anchors and measures states against them. Pseudo-inverse tying gives exact synchronization; under restricted bi-invertibility, SemRF yields stable semantic-basis coordinates, distortion bounds, and near-identity changes. With the frame fixed, residual computation becomes a depthwise semantic trajectory. The anchors induce a semantic Voronoi diagram: distance, or evidence such as logits, assigns each layer to a coarse cell, while coordinates retain within-cell motion and margins. We define layerwise steps, contribution profiles, and imbalance diagnostics, then use the Voronoi trace to define a margin-relaxed tube. The canonical trace is the minimum-action path inside this tube; when nonempty with positive quadratic weight, it is unique and obeys a discrete spline equation away from active constraints. Excess action controls step, curvature, and profile mismatch. Low curvature implies piecewise-linear compressibility and local knowledge density: lower trace complexity means fewer semantic knots. Through the parameter-to-trajectory map, this gives a conditional link to parameter efficiency: among admissible settings fitting data, lower-action and lower-complexity traces use fewer semantic degrees of freedom. The guarantees require controlled interface error and small projection residual under explicit tube constraints.

---


### 116. [Generative Skill Composition for LLM Agents](https://arxiv.org/abs/2606.32025)

**<font color=#1a73e8>作者：</font>** Xinyu Zhao, Zhen Tan, Vaishnav Tadiparthi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent LLM agents benefit from skills for solving complex tasks. Skills encapsulate modular packages of procedural knowledge and instructions for performing specialized tasks, such as setting up a sandboxed environment, running a test suite, or refactoring a function across multiple files. As skill libraries grow and become reusable across tasks and domains, selecting an appropriate skill composition has emerged as a central bottleneck. Existing approaches fall into two categories. One exposes the agent's reasoning to the entire skill collection; the other performs skill retrieval via embeddings or LLM-based rerankers. Both provide useful insights; however, they miss the structural nature of skill composition, which is a joint decision over which skills, how many, and in what order -- three dimensions that cannot be decoupled. We formalize this as structured skill composition: given a task and a skill library, predict an executable skill plan that jointly specifies the activated subset, count, and execution order. We propose SkillComposer, which instantiates structured skill composition as task-conditioned skill sequence prediction. SkillComposer uses a constrained autoregressive decoder over skill identifiers, so subset, count, and order emerge jointly from a single decoding pass, and dependencies between successive skills are captured naturally. We build a training set of task-composition pairs from a real, human-curated skill library. We then evaluate SkillComposer along two axes: composition quality on a held-out test set, and downstream task success on SkillsBench across two production-grade coding agents. On GPT-5.2-Codex, Gemini-3-Pro-Preview, SkillComposer raises the pass rate by +23.1, +18.2pp over the no-skill baseline, surpassing top-3 retrieval and matching the gold-skill retrieval upper bound at lower prompt-token cost.

---


### 117. [AdaJEPA: An Adaptive Latent World Model](https://arxiv.org/abs/2606.32026)

**<font color=#1a73e8>作者：</font>** Ying Wang, Oumayma Bounou, Yann LeCun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models enable planning from high-dimensional observations by predicting future states in a compact latent space. However, these models are typically kept frozen at test time: when their predictions become inaccurate, planning can fail, especially under test-time distribution shift. To address this, we propose AdaJEPA, an adaptive latent world model that performs test-time adaptation within the closed loop of model predictive control (MPC). After training, AdaJEPA plans and executes the first action chunk, uses the observed next-state transition as a self-supervised adaptation signal, and replans with the updated model. This closed-loop update continuously recalibrates the world model without additional expert demonstrations. Across a range of goal-reaching tasks, AdaJEPA substantially improves planning success with as few as one gradient step per MPC replanning step.

---


### 118. [When LLMs Read Tables Carelessly: Measuring and Reducing Data Referencing Errors](https://arxiv.org/abs/2606.32029)

**<font color=#1a73e8>作者：</font>** Yuqing Yang, Qi Zhu, Zhen Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While large language models (LLMs) perform well on table tasks, they still make data referencing errors (DREs), i.e., incorrectly citing or omitting table values, despite understanding the table structure. Beyond final-answer accuracy, DREs directly compromise the correctness and reliability of intermediate reasoning steps. Yet prior studies have only offered limited, small-scale analyses. In this work, we present the first systematic evaluation of tabular data referencing errors across different models and tasks. Our results show that DREs occur across all tested models (1.7B to 20B parameters). Furthermore, we demonstrate that incorporating data referencing as a critic significantly improves answer accuracy up to 12.0%, through critic-based filtering and rejection sampling. Finally, we trained a lightweight 4B-parameter critic model that achieves an average F1 score of 78.2% in detecting both in-distribution and out-of-distribution DREs, and effectively assists inference for larger models.

---


### 119. [Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs](https://arxiv.org/abs/2606.32032)

**<font color=#1a73e8>作者：</font>** Gabrielle Kaili-May Liu, Avi Caciularu, Gal Yona 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Metacognition is a critical component of intelligence that describes the ability to monitor and regulate one's own cognitive processes. Yet LLMs exhibit systemic deficiencies in key metacognitive faculties: they hallucinate with high confidence, fail to recognize knowledge boundaries, and misrepresent their internal uncertainty--undermining trustworthiness and reliability. Since monitoring task performance and adapting behavior accordingly are central to metacognition, we posit that models capable of accurately judging their own performance are better positioned to improve it. We operationalize this idea via two novel mechanisms: reinforcement learning with metacognitive feedback (RLMF), a paradigm to refine completion rankings during preference optimization based on the quality of a model's self-judgments of performance, and metacognitive data selection, which uses similar self-judgments to identify high-value training examples, outperforming naive active learning. We apply these innovations to the problem of faithful calibration (FC), a task that is itself fundamentally metacognitive: the goal is to align expressed with intrinsic uncertainty, difficult even for frontier LLMs. We adopt a two-stage, decoupled approach, first using these methods to calibrate the faithfulness of models' self-reported confidence scores, then mapping to natural, context-adaptable linguistic uncertainty via targeted output editing. Extensive experiments show RLMF achieves generalizable, state-of-the-art FC on diverse tasks while preserving accuracy. Further, RLMF surpasses standard RL by up to 63% while enhancing models' ability to assess and express their own capability limits. This positions RLMF as a promising paradigm to enhance LLM metacognition toward improved abilities and alignment, and suggests metacognitive performance as an effective RL signal to overcome limits of prior intrinsic feedback methods.

---


### 120. [QVal: Cheaply Evaluating Dense Supervision Signals for Long-Horizon LLM Agents](https://arxiv.org/abs/2606.32034)

**<font color=#1a73e8>作者：</font>** Sergio Hernández-Gutiérrez, Matteo Merler, Ilze Amanda Auzina 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly act over long horizons, where a single trajectory can contain hundreds or thousands of actions. In these settings, outcome-only rewards provide too sparse guidance, failing to inform the model about the goodness of intermediate actions. Dense supervision methods aim to solve this problem by scoring intermediate steps, from intrinsic confidence to self-distillation and embedding similarities. However, it is common practice to evaluate them by measuring the downstream performance of a training pipeline that integrates them. This is expensive, conflates supervision quality with training engineering confounders, and renders different methodological families requiring distinct training setups incomparable. As a result, dense supervision methods are rarely benchmarked on common ground. We introduce QVal, a training-free testbed for directly evaluating dense supervision signals. Given a state-action pair, QVal measures how well a method's score is Q-aligned: whether it orders actions according to the Q-values of a strong reference-policy. This lets us compare signals before any training run and separate signal quality from other engineering choices. We instantiate QVal as QVal-v1.0, benchmarking 21 dense supervision methods across four diverse environments and seven methodological families, with over 1.2K evaluation experiments across six open-weight model backbones. We find that simple prompting baselines consistently outperform recent dense supervision methods from the literature, and that performance clusters strongly by family. These findings hold across model sizes, environments, and observation modalities. QVal is designed to be easily extensible to new environments and methods, enabling researchers to iterate on dense supervision methods before any training run.

---


### 121. [FaceMoE: Mixture of Experts for Low-Resolution Face Recognition](https://arxiv.org/abs/2606.32040)

**<font color=#1a73e8>作者：</font>** Kartik Narayan, Vishal M. Patel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-resolution face recognition (LR-FR) remains a challenging task due to poor feature extraction and aggregation, as probe images often contain limited identity information resulting from extreme degradations such as blur, occlusion, and low contrast. Additionally, the domain gap between high-resolution (HR) gallery images and low-resolution (LR) probe images poses a significant challenge. A single feature encoder struggles to generalize effectively across both domains when fine-tuned on an LR dataset, and this issue is further magnified by catastrophic forgetting. To address these challenges, we propose FaceMoE, an effective adaptation of Mixture of Experts (MoE) transfomer architecture for low-resolution face-recognition . Specifically, we introduce multiple specialized feed-forward network (FFN) experts and incorporate a top-k router, which dynamically assigns tokens to appropriate experts. This design emergently promotes specialization across experts for different semantic regions of the face, which enables FaceMoE to perform resolution-aware feature extraction. Moreover, the top-k router facilitates sparse expert activation, enabling the model to preserve pretrained knowledge when finetuned on a LR dataset, while increasing model capacity without proportional computational overhead. FaceMoE is trained with a combined face recognition loss, router z-loss, and load balancing loss to ensure expert specialization and stable training. To the best of our knowledge, this is the first work leveraging MoE for LR-FR. Extensive experiments across eleven datasets, spanning HR, mixed-quality, and LR benchmarks, demonstrate that FaceMoE significantly outperforms state-of-the-art methods. Code: this https URL

---


> [!TIP]
> 当前位于：**101-121**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-121**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
