# 🧠 大模型相关研究 | 2026年05月04日

> 本类共 **123** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-123](./part-03.md)

---

### 1. [BatteryPass-12K: The First Dataset for the Novel Digital Battery Passport Conformance Task](https://arxiv.org/abs/2604.26986)

**<font color=#1a73e8>作者：</font>** Tosin Adewumi, Martin Karlsson, Lama Alkhaled 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce a novel task of digital battery passport (DBP) conformance classification and introduce the first public benchmark for the task: BatteryPass-12K, created synthetically from real pilot samples. This is as the EU's battery regulation on DBPs comes into effect soon and there exists no public dataset. We evaluated 22 language models (LMs) in zero-shot inference, spanning small LMs (SLMs), mixture of experts (MoEs), and dense LLMs. We also conducted analysis, additional evaluations of few-shot inference and prompt-injection attacks to find that (1) Thinking models have the best performance (with GPT-5.4 scoring 0.98 (0.03) and 0.71 (0.22) on average as F1 (and confidence interval at 95%) on the validation and test sets, respectively), (2) few-shot examples improve performance significantly, (3) generally capable frontier models find the task challenging, (4) merely scaling model parameters does not necessarily lead to improved performance, as SLMs outperformed some LLMs, and (5) prompt-injection attacks degrade performance. We note that BatteryPass-12K, though limited to real pilot samples, may be useful for other known or emerging tasks in the battery domain, e.g. lifecycle reasoning. We publicly release the dataset under a permissive licence (CC-BY-4.0).

---


### 2. [When Continual Learning Moves to Memory: A Study of Experience Reuse in LLM Agents](https://arxiv.org/abs/2604.27003)

**<font color=#1a73e8>作者：</font>** Qisheng Hu, Quanyu Long, Wenya Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Memory-augmented LLM agents offer an appealing shortcut to continual learning: rather than updating model parameters, they accumulate experience in external memory, seemingly sidestepping the stability-plasticity dilemma of parametric learning. We show that this challenge does not disappear but resurfaces at the memory level. Under a limited context window, old and new experiences compete during retrieval, relocating the continual-learning bottleneck from parameter updates to memory access. To study this phenomenon, we introduce a (k,v) framework that disentangles two fundamental design axes of external memory: how experience is represented and how it is organized for retrieval. Across sequential-task experiments in ALFWorld and BabyAI, we find that abstract procedural memories transfer more reliably than detailed trajectories, while negative transfer disproportionately harms the hard cases. Moreover, finer-grained memory organization is not universally beneficial: designs that yield strong forward transfer can simultaneously induce severe forgetting. Together, these results reveal that external memory does not resolve the continual-learning problem; it reshapes it into a problem of memory representation and retrieval design.

---


### 3. [Automatic Causal Fairness Analysis with LLM-Generated Reporting](https://arxiv.org/abs/2604.27011)

**<font color=#1a73e8>作者：</font>** Alessia Berarducci, Eric Rossetto, Alessandro Antonucci 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AutoML, intended as the process of automating the application of machine learning to real-world problems, is a key step for AI popularisation. Most AutoML frameworks are not accounting for the potential lack of fairness in the training data and in the corresponding predictions. We introduce \textsc{FairMind}, a software prototype aiming to automatise fairness analysis at the dataset level. We achieve that by resorting to the assumptions of the \emph{standard fairness model}, recently proposed by Plečko and Bareinboim. This allows for a sound fairness evaluation in terms of causal effects, based on \emph{counterfactual} queries involving the target, possibly confounders and mediators, and the different values of an input feature we regard as \emph{protected}. After the necessary data preprocessing, the tool implements a closed-form computation of the effects. LLMs are consequently exploited to generate accurate reports on the fairness levels detected in the training dataset. We achieve that in a zero-shot setup and show by examples the expected advantages with respect to a direct analysis performed by the LLM. To favour applications, extensions to ordinal protected variable and continuous targets and novel decomposition results are also discussed.

---


### 4. [Fidelity, Diversity, and Privacy: A Multi-Dimensional LLM Evaluation for Clinical Data Augmentation](https://arxiv.org/abs/2604.27014)

**<font color=#1a73e8>作者：</font>** Guillermo Iglesias, Gema Bello-Orgaz, María Navas-Loro 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The scarcity of high-quality annotated medical data, particularly in mental health, poses a significant bottleneck for training robust machine learning models. Privacy regulations restrict data sharing, making synthetic data generation a promising alternative. The use of Large Language Models (LLMs) in a data augmentation pipeline could be leveraged as an alternative in this field. In the proposed methodology, DeepSeek-R1, OpenBioLLM-Llama3 and Qwen 3.5 are used to generate synthetic mental health evaluation reports conditioned on specific International Classification of Diseases, Tenth Revision (ICD-10) codes. Because naive text generation can lead to mode collapse or privacy breaches (memorization), a comprehensive evaluation framework is introduced. The generated diagnostic texts are assessed across three dimensions: semantic fidelity, lexical diversity, and privacy/plagiarism. The results demonstrate that all models can generate clinically coherent, diverse, and privacy-safe synthetic reports, significantly expanding the available training data for clinical natural language processing tasks without compromising patient confidentiality.

---


### 5. [Dynamic Adversarial Fine-Tuning Reorganizes Refusal Geometry](https://arxiv.org/abs/2604.27019)

**<font color=#1a73e8>作者：</font>** Wenhao Lan, Shan Li, Junbin Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety-aligned language models must refuse harmful requests without collapsing into broad over-refusal, but the training-time mechanisms behind this tradeoff remain unclear. Prior work characterizes refusal directions and jailbreak robustness, yet does not explain how dynamic adversarial fine-tuning changes refusal carriers across training. We present a measurement-driven mechanism study, not a new defense, on one 7B backbone under supervised fine-tuning (SFT) and R2D2-style dynamic adversarial fine-tuning. Our protocol aligns fixed-source HarmBench, StrongREJECT, and XSTest with a five-anchor refusal-geometry suite and causal interventions. R2D2 drives fixed-source HarmBench ASR to 0.000 at steps 50 and 100, then partially reopens to 0.035 at step 250 and 0.250 at step 500; SFT remains less robust, with ASR between 0.505 and 0.588 at the same anchors. On XSTest, R2D2 any-refusal is 1.000 early, then falls to 0.664 and 0.228. Geometrically, R2D2 preserves a late-layer admissible carrier through step 100 before relocating to an early-layer carrier, while effective rank remains near 1.23--1.27. Causal interventions indicate low-dimensional but utility-coupled control. These results support a reorganization account rather than a drift-only account, with evidence limited to one backbone and fixed-source attacks.

---


### 6. [Breaking Bad Financial Habits: How LLM Conversations Correct Financial Misconceptions](https://arxiv.org/abs/2604.27022)

**<font color=#1a73e8>作者：</font>** Jillian Ross, Eric So, Andrew W. Lo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Financial misconceptions carry direct economic costs, from panic selling to equity market avoidance, yet they are notoriously resistant to correction. Traditional financial literacy interventions are constrained by cost, reach, and a persistent gap between knowledge and behavioral change. Across three pre-registered studies, we find that purposefully designed LLMs can durably correct financial misconceptions. Critically, two factors are necessary for this effect. First, corrective intent: LLMs prompted only to discuss a misconception produce corrections no better than unassisted self-reflection, and undirected LLM conversations can actively entrench misconceptions. Second, recipient receptivity: financial concepts are often foreign to the investors who misapply them, and LLM responses pitched below a participant's financial sophistication are judged as less credible and produce substantially weaker corrections. LLMs thus offer a scalable alternative to traditional financial literacy intervention, but only when designed with both factors in mind.

---


### 7. [CL-bench Life: Can Language Models Learn from Real-Life Context?](https://arxiv.org/abs/2604.27043)

**<font color=#1a73e8>作者：</font>** Shihan Dou, Yujiong Shen, Chenhao Huang 等 38 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Today's AI assistants such as OpenClaw are designed to handle context effectively, making context learning an increasingly important capability for models. As these systems move beyond professional settings into everyday life, the nature of the contexts they must handle also shifts. Real-life contexts are often messy, fragmented, and deeply tied to personal and social experience, such as multi-party conversations, personal archives, and behavioral traces. Yet it remains unclear whether current frontier language models can reliably learn from such contexts and solve tasks grounded in them. To this end, we introduce CL-bench Life, a fully human-curated benchmark comprising 405 context-task pairs and 5,348 verification rubrics, covering common real-life scenarios. Solving tasks in CL-bench Life requires models to reason over complex, messy real-life contexts, calling for strong real-life context learning abilities that go far beyond those evaluated in existing benchmarks. We evaluate ten frontier LMs and find that real-life context learning remains highly challenging: even the best-performing model achieves only 19.3% task solving rate, while the average performance across models is only 13.8%. Models still struggle to reason over contexts such as messy group chat histories and fragmented behavioral records from everyday life. CL-bench Life provides a crucial testbed for advancing real-life context learning, and progress on it can enable more intelligent and reliable AI assistants in everyday life.

---


### 8. [When Your LLM Reaches End-of-Life: A Framework for Confident Model Migration in Production Systems](https://arxiv.org/abs/2604.27082)

**<font color=#1a73e8>作者：</font>** Emma Casey, David Roberts, David Sim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a framework for migrating production Large Language Model (LLM) based systems when the underlying model reaches end-of-life or requires replacement. The key contribution is a Bayesian statistical approach that calibrates automated evaluation metrics against human judgments, enabling confident model comparison even with limited manual evaluation data. We demonstrate this framework on a commercial question-answering system serving 5.3M monthly interactions across six global regions; evaluating correctness, refusal behavior, and stylistic adherence to successfully identify suitable replacement models. The framework is broadly applicable to any enterprise deploying LLM-based products, providing a principled, reproducible methodology for model migration that balances quality assurance with evaluation efficiency. This is a capability increasingly essential as the LLM ecosystem continues to evolve rapidly and organizations manage portfolios of AI-powered services across multiple models, regions, and use cases.

---


### 9. [AutoSP: Unlocking Long-Context LLM Training Via Compiler-Based Sequence Parallelism](https://arxiv.org/abs/2604.27089)

**<font color=#1a73e8>作者：</font>** Ahan Gupta, Zhihao Wang, Neel Dani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-language-models (LLMs) demonstrate enormous utility in long-context tasks which require processing prompts that consist of tens to hundreds of thousands of tokens. However, existing LLM training libraries do not provide easy to use abstractions to optimize for long-context training, instead focusing on optimizations for models with large parameter counts through ZeRO-3/FSDP, Tensor and Pipeline parallelism. This forces users to rewrite LLM training libraries to incorporate compositions of various complex long-context optimizations, such as sequence-parallelism, to training pipelines; a process that requires in-depth expertise, reducing developer productivity. To tackle these challenges, we introduce AutoSP: the first automated solution to automatically optimize LLM training for longer-contexts. AutoSP compiles models and applies a targeted set of optimizations: automated sequence parallelism, and long-context aware activation-checkpointing, to drastically enhance LLM trainability at negligible cost to throughput. Our evaluation demonstrates AutoSP's capability on both NVIDIA and AMD hardware, increasing training contexts by upto 2.7$\times$ and 2.5$\times$ respectively over competitive hand-written baseline at negligible cost to runtime performance.

---


### 10. [End-to-end autonomous scientific discovery on a real optical platform](https://arxiv.org/abs/2604.27092)

**<font color=#1a73e8>作者：</font>** Shuxing Yang, Fujia Chen, Rui Zhao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific research has long been human-led, driving new knowledge and transformative technologies through the continual revision of questions, methods and claims as evidence accumulates. Although large language model (LLM)-based agents are beginning to move beyond assisting predefined research workflows, none has yet demonstrated end-to-end autonomous discovery in a real physical system that produces a nontrivial result supported by experimental evidence. Here we introduce Qiushi Discovery Engine, an LLM-based agentic system for end-to-end autonomous scientific discovery on a real optical platform. Qiushi Engine combines nonlinear research phases, Meta-Trace memory and a dual-layer architecture to maintain adaptive and stable research trajectories across long-horizon investigations involving thousands of LLM-mediated reasoning, measurement and revision actions. It autonomously reproduces a published transmission-matrix experiment on a non-original platform and converts an abstract coherence-order theory into experimental observables, providing, to our knowledge, the first observation of this class of coherence-order structure. More importantly, in an open-ended study involving 145.9 million tokens, 3,242 LLM calls, 1,242 tool calls, 163 research notes and 44 scripts, Qiushi Engine proposes and experimentally validates optical bilinear interaction, a physical mechanism structurally analogous to a core operation in Transformer attention. This AI-discovered mechanism suggests a route towards high-speed, energy-efficient optical hardware for pairwise computation. To our knowledge, this is the first demonstration of an AI agentic system autonomously identifying and experimentally validating a nontrivial, previously unreported physical mechanism, marking a milestone for research-level autonomous agents.

---


### 11. [Think it, Run it: Autonomous ML pipeline generation via self-healing multi-agent AI](https://arxiv.org/abs/2604.27096)

**<font color=#1a73e8>作者：</font>** Adela Bara, Gabriela Dobrita, Simona-Vasilica Oprea  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The purpose of our paper is to develop a unified multi-agent architecture that automates end-to-end machine learning (ML) pipeline generation from datasets and natural-language (NL) goals, improving efficiency, robustness and explainability. A five-agent system is proposed to handle profiling, intent parsing, microservice recommendation, Directed Acyclic Graph (DAG) construction and execution. It integrates code-grounded Retrieval-Augmented Generation (RAG) for microservice understanding, an explainable hybrid recommender combining multiple criteria, a self-healing mechanism using Large Language Model (LLM)-based error interpretation and adaptive learning from execution history. The approach is evaluated on 150 ML tasks across diverse scenarios. The system achieves an 84.7% end-to-end pipeline success rate, outperforming baseline methods. It demonstrates improved robustness through self-healing and reduces workflow development time compared to manual construction. The study introduces a novel integration of code-grounded RAG, explainable recommendation, self-healing execution and adaptive learning within a single architecture, showing that tightly coupled intelligent components can outperform isolated solutions.

---


### 12. [Automated Detection of Mutual Gaze and Joint Attention in Dual-Camera Settings via Dual-Stream Transformers](https://arxiv.org/abs/2604.27105)

**<font color=#1a73e8>作者：</font>** Jakub Kosmydel, Paweł Gajewski, Arkadiusz Białek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Analyzing mutual gaze (MG) and joint attention (JA) is critical in developmental psychology but traditionally relies on labor-intensive manual coding. Automating this process in multi-camera laboratory settings is computationally challenging due to complex cross-camera relational dynamics. In this paper, we propose a highly efficient dual-stream Transformer architecture for detecting MG and JA from synchronized dual-camera recordings. Our approach leverages frozen gaze-aware backbones (GazeLLE) to extract rich visual priors, combined with a custom token fusion mechanism to map the spatial and semantic relationships between interacting dyads. Evaluated on an ecologically valid dataset of caregiver-infant interactions, our model exhibits good performance, significantly outperforming both a convolutional baseline and a state-of-the-art multimodal Large Language Model (LLM). By open-sourcing our model and pre-trained weights, we provide behavioral scientists with a scalable tool that can be fine-tuned to diverse laboratory environments, effectively bridging the gap between computational modeling and applied interaction research.

---


### 13. [Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models](https://arxiv.org/abs/2604.27115)

**<font color=#1a73e8>作者：</font>** M. K. Khalidi Siam, Md. Tausif-Ul-Islam, Md. Reshad Romim Khan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neuron pruning is widely used to reduce the computational cost and parameter footprint of large language models, yet it remains unclear whether neurons in task-specific models contribute uniformly to task performance. In this work, we provide empirical evidence for the existence and importance of task-specific neurons through a systematic pruning study on language models specialized for mathematical reasoning and code generation. We introduce an activation-based selectivity metric to identify neurons with low contribution to the target task and prune them while preserving target-task accuracy, and compare selective pruning with random pruning. Selective pruning consistently outperforms random pruning, indicating that activation-based selectivity provides a systematic advantage over random pruning. Reverse pruning experiments further show that removing a small subset of highly task-specific neurons (~10%) causes complete performance collapse, suggesting that there exist task specific neurons and critical task information is concentrated in a small portion of the network. In contrast, selective pruning of less critical neurons (~30% - ~35%) reduces accuracy but still preserves significant performance. We also observed consistent reductions in parameters and runtime VRAM usage, along with improved inference throughput as pruning increases. Experiments on both 1.5B and 7B models reveal a robustness threshold around 15-20% pruning, beyond which accuracy loss and generation failures increase sharply. Fine-tuning substantially recovers performance across pruning levels, particularly for aggressively pruned models. These findings provide empirical evidence of neuron specialization in task-specific language models and offer insights into pruning robustness, model redundancy, and post-pruning recoverability.

---


### 14. [Better Models, Faster Training: Sigmoid Attention for single-cell Foundation Models](https://arxiv.org/abs/2604.27124)

**<font color=#1a73e8>作者：</font>** Vijay Sadashivaiah, Georgios Dasoulas, Judith Mueller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training stable biological foundation models requires rethinking attention mechanisms: we find that using sigmoid attention as a drop in replacement for softmax attention a) produces better learned representations: on six diverse single-cell datasets, sigmoid achieves 25% higher cell-type separation, better cell-type cohesion metrics, and lower validation loss, b) faster training, models with sigmoid attention train up to 10% faster than their softmax counterparts, and c) more stable training by eliminating inherent sources of instability in softmax attention. We establish that sigmoid attention has globally bounded derivatives ($\leq 0.25$) as opposed to softmax, and a diagonal Jacobian structure in contrast with softmax's dense coupling, which together help alleviate training instabilities. In stress tests on 160M-parameter bidirectional attention models trained without gradient clipping on 8K-token sequences, softmax diverges catastrophically, with gradients exploding by four orders of magnitude, while sigmoid remains stable. Finally, we implement and open-source TritonSigmoid, an efficient GPU kernel that achieves 515 TFLOPS on H100 GPUs, outperforming both FlashAttention-2 and FlashSigmoid, with native padding support, which is essential for biological sequences. Our results establish sigmoid attention as both theoretically grounded and empirically superior for biological foundation models. Code is available at this https URL

---


### 15. [Cross-Lingual Response Consistency in Large Language Models: An ILR-Informed Evaluation of Claude Across Six Languages](https://arxiv.org/abs/2604.27137)

**<font color=#1a73e8>作者：</font>** Camelia Baluta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces a systematic evaluation framework grounded in the Interagency Language Roundtable (ILR) Skill Level Descriptions and applies it to Claude (Sonnet 4.6) across six languages: English, French, Romanian, Spanish, Italian, and German. We administer a battery of 12 semantically equivalent prompt clusters spanning ILR complexity levels 1 through 3+, collect 216 responses (12 prompts, 6 languages, 3 runs), and analyze outputs through a two-layer methodology combining automated quantitative metrics with expert ILR qualitative assessment. Quantitative analysis reveals that French responses are approximately 30% longer than German responses on identical prompts, and that creative and affective clusters show the highest cross-lingual surface divergence. Qualitative analysis, conducted by a six-language professional with 12 years of ILR/OPI assessment experience, identifies five cross-lingual variation patterns: systematic differences in pragmatic disambiguation strategies, aesthetic and literary tradition divergence in creative output, language-internal technical terminology norms, cultural calibration gaps evidenced by the absence of culture-specific content in favor of culturally neutralized templates, and language-specific institutional referral behavior in emotional support responses. We argue that ILR-informed expert judgment applied to LLM outputs constitutes a novel and underreported evaluation methodology that complements purely computational benchmarks, and that cross-lingual output variation in Claude is interpretable, domain-dependent, and consequential for equitable multilingual AI deployment.

---


### 16. [How to Guide Your Flow: Few-Step Alignment via Flow Map Reward Guidance](https://arxiv.org/abs/2604.27147)

**<font color=#1a73e8>作者：</font>** Jerry Y. Huang, Justin Lin, Sheel Shah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In generative modeling, we often wish to produce samples that maximize a user-specified reward such as aesthetic quality or alignment with human preferences, a problem known as guidance. Despite their widespread use, existing guidance methods either require expensive multi-particle, many-step schemes or rely on poorly understood approximations. We reformulate guidance as a deterministic optimal control problem, yielding a hierarchy of algorithms that subsumes existing approaches at the coarsest level. We show that the flow map, an object of significant recent interest for its role in fast inference, arises naturally in the optimal solution. Based on this observation, we propose Flow Map Reward Guidance (FMRG): a training-free, single-trajectory framework that uses the flow map to both integrate and guide the flow. At text-to-image scale, FMRG matches or surpasses baselines across inverse problems, style transfer, human preferences, and VLM rewards with as few as 3 NFEs, giving at least an order-of-magnitude speedup in comparison to prior state of the art.

---


### 17. [Generalizing the Geometry of Model Merging Through Frechet Averages](https://arxiv.org/abs/2604.27155)

**<font color=#1a73e8>作者：</font>** Marvin F. da Silva, Mohammed Adnan, Felix Dangel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging aims to combine multiple models into one without additional training. Naïve parameter-space averaging can be fragile under architectural symmetries, as their geometry does not take them into account. In this work we show that not only the geometry, but also the averaging procedure itself, must be symmetry-invariant to achieve symmetry-aware merges. Consequently, we propose a general solution: merging as Fréchet averaging, i.e., selecting parameters that minimize a sum of geodesic distances on an appropriate manifold. In this view, the key design choice is the overall geometry, i.e., the choice of metric, manifold, and distance approximation, that determines what it means for two models to be "close". We show that Fréchet averaging, combined with simplifying assumptions, contains Fisher merging. Building on this, we examine the particular case of low-rank adapters (LoRA), whose symmetries induce a distinct geometry: that of a quotient manifold. We outline the limitations of current LoRA merging methods, propose a practical algorithm for this setting, and show how they compare with other commonly used approaches.

---


### 18. [Distributional Alignment Games for Answer-Level Fine-Tuning](https://arxiv.org/abs/2604.27166)

**<font color=#1a73e8>作者：</font>** Mehryar Mohri, Jon Schneider, Yifan Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We focus on the problem of \emph{Answer-Level Fine-Tuning} (ALFT), where the goal is to optimize a language model based on the correctness or properties of its final answers, rather than the specific reasoning traces used to produce them. Directly optimizing answer-level objectives is computationally intractable due to the need to marginalize over the vast space of latent reasoning paths. To overcome this, we propose a general game-theoretical framework that lifts the problem to a \emph{Distributional Alignment Game}. We formulate ALFT as a two-player game between a Policy (the generator) and a Target (an auxiliary distribution). We prove that the Nash Equilibrium of this game corresponds exactly to the solution of the original answer-level optimization problem. This variational perspective transforms the intractable marginalization problem into a tractable projection problem. We demonstrate that this framework unifies recent approaches to diversity and self-improvement (coherence) and provide efficient algorithms compatible with Group Relative Policy Optimization (GRPO), such as Coherence-GRPO, yielding significant complexity gains in mathematical reasoning tasks.

---


### 19. [Semantic Structure of Feature Space in Large Language Models](https://arxiv.org/abs/2604.27169)

**<font color=#1a73e8>作者：</font>** Austin C. Kozlowski, Andrei Boutyline  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We show that the geometric relations between semantic features in large language models' hidden states closely mirror human psychological associations. We construct feature vectors corresponding to 360 words and project them on 32 semantic axes (e.g. beautiful-ugly, soft-hard), and find that these projections correlate highly with human ratings of those words on the respective semantic scales. Second, we find that the cosine similarities between the semantic axes themselves are highly predictive of the correlations between these scales in the survey. Third, we show that substantial variance across the 32 semantic axes lies on a low-dimensional subspace, reproducing patterns typical of human semantic associations. Finally, we demonstrate that steering a word on one semantic axis causes spillover effects on the model's rating of that word on other semantic scales proportionate to the cosine similarity between those semantic axes. These findings suggest that features should be understood not only in isolation but through their geometric relations and the meaningful subspaces they form.

---


### 20. [Toward Personalized Digital Twins for Cognitive Decline Assessment: A Multimodal, Uncertainty-Aware Framework](https://arxiv.org/abs/2604.27217)

**<font color=#1a73e8>作者：</font>** Bulent Soykan, Gulsah Hancerliogullari Koksalmis, Hsin-Hsiung Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cognitive decline is highly heterogeneous across individuals, which complicates prognosis, trial design, and treatment planning. We present the Personalized Cognitive Decline Assessment Digital Twin (PCD-DT), a multimodal and uncertainty-aware framework for modeling patient-specific disease trajectories from sparse, noisy, and irregular longitudinal data. The framework combines three methodological components: (1) latent state-space models for individualized temporal dynamics, (2) multimodal fusion for clinical, biomarker, and imaging features, and (3) uncertainty-aware validation and adaptive updating for robust digital twin operation. We also outline how conditional generative models can support data augmentation and stress testing for underrepresented progression patterns. As a preliminary feasibility study, we analyze longitudinal TADPOLE trajectories and show clear separation between cognitively normal and Alzheimer's disease cohorts in ADAS13, ventricle volume, and hippocampal volume over five years. We further conduct a multimodal next-visit prediction ablation using an LSTM sequence model on 3{,}003 visit-pair sequences derived from TADPOLE, where the combined cognitive plus MRI configuration achieves the lowest standardized RMSE for both ADAS13 (0.4419) and ventricle volume (0.5842), outperforming a Last Observation Carried Forward baseline. A Bayesian tensor modeling component for high-dimensional imaging fusion is also discussed. These results support the feasibility of the proposed architecture while also highlighting the need for stronger uncertainty calibration and longer-horizon predictive evaluation. The PCD-DT framework provides a principled starting point for personalized in silico modeling in neurodegenerative disease. This work positions PCD-DT as a foundational step toward clinically deployable, uncertainty-aware digital twin systems.

---


### 21. [Web2BigTable: A Bi-Level Multi-Agent LLM System for Internet-Scale Information Search and Extraction](https://arxiv.org/abs/2604.27221)

**<font color=#1a73e8>作者：</font>** Yuxuan Huang, Yihang Chen, Zhiyuan He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic web search increasingly faces two distinct demands: deep reasoning over a single target, and structured aggregation across many entities and heterogeneous sources. Current systems struggle on both fronts. Breadth-oriented tasks demand schema-aligned outputs with wide coverage and cross-entity consistency, while depth-oriented tasks require coherent reasoning over long, branching search trajectories. We introduce \textbf{Web2BigTable}, a multi-agent framework for web-to-table search that supports both regimes. Web2BigTable adopts a bi-level architecture in which an upper-level orchestrator decomposes the task into sub-problems and lower-level worker agents solve them in parallel. Through a closed-loop run--verify--reflect process, the framework jointly improves decomposition and execution over time via persistent, human-readable external memory, with self-evolving updates to each single-agent. During execution, workers coordinate through a shared workspace that makes partial findings visible, allowing them to reduce redundant exploration, reconcile conflicting evidence, and adapt to emerging coverage gaps. Web2BigTable sets a new state of the art on WideSearch, reaching an Avg@4 Success Rate of \textbf{38.50} ($7.5\times$ the second best at 5.10), Row F1 of \textbf{63.53} (+25.03 over the second best), and Item F1 of \textbf{80.12} (+14.42 over the second best). It also generalises to depth-oriented search on XBench-DeepSearch, achieving 73.0 accuracy. Code is available at this https URL.

---


### 22. [When Roles Fail: Epistemic Constraints on Advocate Role Fidelity in LLM-Based Political Statement Analysis](https://arxiv.org/abs/2604.27228)

**<font color=#1a73e8>作者：</font>** Juergen Dietrich  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Democratic discourse analysis systems increasingly rely on multi-agent LLM pipelines in which distinct evaluator models are assigned adversarial roles to generate structured, multi-perspective assessments of political statements. A core assumption is that models will reliably maintain their assigned roles. This paper provides the first systematic empirical test of that assumption using the TRUST pipeline. We develop an epistemic stance classifier that identifies advocate roles from reasoning text without relying on surface vocabulary, and measure role fidelity across 60 political statements (30 English, 30 German) using four metrics: Role Drift Index (RDI), Expected Drift Distance (EDD), Directional Drift Index (DDI), and Entropy-based Role Stability (ERS). We identify two failure modes - the Epistemic Floor Effect (fact-check results create an absolute lower bound below which the legitimizing role cannot be maintained) and Role-Prior Conflict (training-time knowledge overrides role instructions for factually unambiguous statements) - as manifestations of a single mechanism: Epistemic Role Override (ERO). Model choice significantly affects role fidelity: Mistral Large outperforms Claude Sonnet by 28pp (67% vs. 39%) and exhibits a qualitatively different failure mode - role abandonment without polarity reversal - compared to Claude's active switch to the opposing stance. Role fidelity is language-robust. Fact-check provider choice is not universally neutral: Perplexity significantly reduces Claude's role fidelity on German statements (Delta = -15pp, p = 0.007) while leaving Mistral unaffected. These findings have direct implications for multi-agent LLM validation: a system validated without role fidelity measurement may systematically misrepresent the epistemic diversity it was designed to provide.

---


### 23. [Targeted Linguistic Analysis of Sign Language Models with Minimal Translation Pairs](https://arxiv.org/abs/2604.27232)

**<font color=#1a73e8>作者：</font>** Serpil Karabüklü, Kanishka Misra, Shester Gueuwou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Models of sign language have historically lagged behind those for spoken language (text and speech). Recent work has greatly improved their performance on tasks like sign language translation and isolated sign recognition. However, it remains unclear to what extent existing models capture various linguistic phenomena of sign language, and how well they use cues from the multiple articulators used in sign language (hands, upper body, face). We introduce a new benchmark dataset for American Sign Language, ASL Minimal Translation Pairs (ASL-MTP), divided into multiple types of sign language phenomena and corresponding minimal pairs of translations, for performing such linguistic analyses. As a case study, we use ASL-MTP to analyze a state-of-the-art ASL-to-English translation model. We conduct a targeted analysis of the model by ablating various input cues during training and inference and evaluating on the phenomena in ASL-MTP. Our results show that, while the model performs above chance level on most of the phenomena, it relies strongly on manual cues while often missing crucial non-manual cues.

---


### 24. [Instruction Complexity Induces Positional Collapse in Adversarial LLM Evaluation](https://arxiv.org/abs/2604.27249)

**<font color=#1a73e8>作者：</font>** Jon-Paul Cacioli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When instructed to underperform on multiple-choice evaluations, do language models engage with question content or fall back on positional shortcuts? We map the boundary between these regimes using a six-condition adversarial instruction-specificity gradient administered to two instruction-tuned LLMs (Llama-3-8B and Llama-3.1-8B) on 2,000 MMLU-Pro items. Distributional screening (response-position entropy) and an independent content-engagement criterion (difficulty-accuracy correlation) jointly characterise each condition. The gradient reveals three regimes rather than a monotonic transition. Vague adversarial instructions produce moderate accuracy reduction with preserved content engagement. Standard sandbagging and capability-imitation instructions produce positional entropy collapse with partial content engagement. A two-step answer-aware avoidance instruction produces extreme positional collapse, with near-total concentration on a single response position (99.9% and 87.4%) and no measurable content sensitivity. This was the only multi-step instruction tested, and it produced the most extreme shortcut. The attractor position matches each model's content-absent null-prompt default. The effect replicates across both models and four academic domains. Distributional collapse and content engagement can co-occur (50% concordance between screening criteria), indicating that entropy-based screening and difficulty-based content assessment capture partially independent dimensions of response validity. Results suggest that instruction complexity can determine whether adversarial compliance uses content-aware or content-blind mechanisms in small instruction-tuned LLMs under greedy decoding.

---


### 25. [Compliance versus Sensibility: On the Reasoning Controllability in Large Language Models](https://arxiv.org/abs/2604.27251)

**<font color=#1a73e8>作者：</font>** Xingwei Tan, Marco Valentino, Mahmud Elahi Akhter 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are known to acquire reasoning capabilities through shared inference patterns in pre-training data, which are further elicited via Chain-of-Thought (CoT) practices. However, whether fundamental reasoning patterns, such as induction, deduction, and abduction, can be decoupled from specific problem instances remains a critical challenge for model controllability, and for shedding light on reasoning controllability. In this paper, we present the first systematic investigation of this problem through the lens of reasoning conflicts: an explicit tension between parametric and contextual information induced by mandating logical schemata that deviate from those expected for a target task. Our evaluation reveals that LLMs consistently prioritize sensibility over compliance, favoring task-appropriate reasoning patterns despite conflicting instructions. Notably, task accuracy is not strictly determined by sensibility, with models often maintaining high performance even when using conflicting patterns, suggesting a reliance on internalized parametric memory that increases with model size. We further demonstrate that reasoning conflicts are internally detectable, as confidence scores significantly drop during conflicting episodes. Probing experiments confirm that reasoning types are linearly encoded from middle-to-late layers, indicating the potential for activation-level controllability. Leveraging these insights, we steer models towards compliance, increasing instruction following by up to 29%. Overall, our findings establish that while LLM reasoning is anchored to concrete instances, active mechanistic interventions can effectively decouple logical schemata from data, offering a path toward improved controllability, faithfulness, and generalizability.

---


### 26. [AutoSurfer -- Teaching Web Agents through Comprehensive Surfing, Learning, and Modeling](https://arxiv.org/abs/2604.27253)

**<font color=#1a73e8>作者：</font>** Fazle Elahi Faisal, Qianhui Wu, Baolin Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in multimodal large language models (LLMs) have revolutionized web agents that can automate complex tasks on websites. However, their accuracy remains limited by the scarcity of high-quality web trajectory training data. Existing automatic trajectory generation methods suffer from incomplete website coverage due to homepage-based task proposals or random-walk exploration. Such methods often result in hallucinated or ambiguous task synthesis that lead to incomplete and unreliable trajectory generation. Here, we present AutoSurfer, a comprehensive web trajectory generator that addresses these limitations through three key innovations. First, AutoSurfer employs a systematic breadth-first exploration strategy that maintains a queue of discovered pages and action traces, propagates knowledge across pages to avoid redundant exploration, and recursively expands multi-level graphical user interface elements - closely resembling how a human would learn a new website. Second, AutoSurfer leverages the exploration trajectory to guide task synthesis, reducing hallucinations by grounding complex tasks in actual navigation paths rather than isolated actions or page content alone. Third, AutoSurfer uses the same exploration trajectory as hints to steer a web agent toward more accurate and reliable trajectory refinement. Together, these innovations enable AutoSurfer to comprehensively cover a website's action space and generate data suitable for training website-specific LLMs. We evaluate AutoSurfer on the WebArena benchmark by fine-tuning Qwen2.5-VL-7B-Instruct and demonstrate that it outperforms state-of-the-art methods - Explorer, OS-Genesis, and SynthAgent - achieving up to 24.23% overall task completion accuracy compared to 19.59% for the best prior method. Further, task diversity analysis demonstrates that AutoSurfer yields a more diverse distribution of synthesized tasks.

---


### 27. [VTBench: A Multimodal Framework for Time-Series Classification with Chart-Based Representations](https://arxiv.org/abs/2604.27259)

**<font color=#1a73e8>作者：</font>** Madhumitha Venkatesan, Xuyang Chen, Dongyu Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Time-series classification (TSC) has advanced significantly with deep learning, yet most models rely solely on raw numerical inputs, overlooking alternative representations. While texture-based encodings such as Gramian Angular Fields (GAF) and Recurrence Plots (RP) convert time series into 2D images, they often require heavy preprocessing and yield less intuitive representations. In contrast, chart-based visualizations offer more interpretable alternatives and show promise in specific domains; however, their effectiveness remains underexplored, with limited systematic evaluation across chart types, visual encoding choices, and datasets. In this work, we introduce VTBench, a systematic and extensible framework that re-examines TSC through multimodal fusion of raw sequences and chart-based visualizations. VTBench generates lightweight, human-interpretable plots -- line, area, bar, and scatter, providing complementary views of the same signal. We develop a modular architecture supporting multiple fusion strategies, including single-chart visual-numerical fusion, multi-chart visual fusion, and full multimodal fusion with raw inputs. Through experiments across 31 UCR datasets, we show that: (1) chart-only models are competitive in selected settings, particularly on smaller datasets; (2) combining multiple chart types can improve accuracy by capturing complementary visual cues; and (3) multimodal models improve or maintain performance when visual features provide non-redundant information, but may degrade accuracy when they introduce redundancy. We further distill practical guidelines for selecting chart types, fusion strategies, and configurations. VTBench establishes a unified foundation for interpretable and effective multimodal time-series classification.

---


### 28. [Decoupling the Benefits of Subword Tokenization for Language Model Training via Byte-level Simulation](https://arxiv.org/abs/2604.27263)

**<font color=#1a73e8>作者：</font>** Théo Gigant, Bowen Peng, Jeffrey Quesnelle  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Subword tokenization is an essential part of modern large language models (LLMs), yet its specific contributions to training efficiency and model performance remain poorly understood. In this work, we decouple the effects of subword tokenization by isolating them within a controlled byte-level pretraining pipeline. We formulate and test hypotheses across various dimensions, including sample throughput, vocabulary scaling, and the linguistic prior of subword boundaries. By simulating these effects in a byte-level setting, we refine our understanding of why subword models outperform raw byte models and offer insights to improve the pretraining of future byte-level and subword models. Specifically, our experiments highlight the critical role of increased training throughput and the integration of subword boundaries as either explicit priors or inductive biases.

---


### 29. [OptimusKG: Unifying biomedical knowledge in a modern multimodal graph](https://arxiv.org/abs/2604.27269)

**<font color=#1a73e8>作者：</font>** Lucas Vittor, Ayush Noori, Iñaki Arango 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biomedical knowledge graphs (KGs) are widely used in the life sciences, yet many are derived from unstructured documents and therefore lack schema-level constrains, whereas graphs assembled from structured resources are difficult to harmonize into a unified representation. We present OptimusKG, a multimodal biomedical labeled property graph (LPG) built from structured and semi-structured resources to preserve factual, type-specific metadata across molecular, anatomical, clinical, and environmental domains. OptimusKG contains 190,531 nodes across 10 entity types, 21,813,816 edges across 26 relation types, and 67,249,863 property instances encoding 110,276,843 values across 150 distinct property keys, derived from 18 ontologies and controlled vocabularies. The graph enforces a top-level schema for nodes and edges and retains granular, type-specific properties, cross-references, and provenance across molecular, anatomical, clinical, and environmental domains. We assessed the validity of OptimusKG by evaluating whether graph relationships are supported by evidence from the scientific literature using a multimodal agent, PaperQA3. PaperQA3 identified supporting evidence for 70.0% of sampled edges, whereas 83.4% of sampled false edges received no supporting evidence. Edges without literature support were concentrated in associations derived from experimental and functional genomics resources, suggesting that OptimusKG captures biomedical knowledge that may precede synthesis in the scientific literature. OptimusKG is distributed as Apache Parquet files, providing a standardized resource for graph-based machine learning, knowledge-grounded retrieval with large language models, and biomedical discovery use cases such as hypothesis generation.

---


### 30. [When 2D Tasks Meet 1D Serialization: On Serialization Friction in Structured Tasks](https://arxiv.org/abs/2604.27272)

**<font color=#1a73e8>作者：</font>** Chung-Hsiang Lo, Lu Li, Diji Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) conventionally process structured inputs as 1D token sequences. While natural for prose, such linearization may introduce additional representational burden for tasks whose computation depends directly on explicit 2D structure, because row--column alignment and local neighborhoods are no longer directly expressed in the input. We study this setting, which we refer to as serialization friction, on a small diagnostic testbed of synthetic tasks with explicit 2D structure: matrix transpose, Conway's Game of Life, and LU decomposition. To examine this question, we compare a text-only language pathway over serialized inputs with a vision-augmented pathway, built on the same language backbone, that receives the same underlying content rendered in task-faithful 2D layout, yielding a system-level comparison between two end-to-end input pathways. Across the tasks and settings we study, the visual pathway consistently outperforms the textual pathway; the gap often widens at larger dimensions, and error patterns under serialization become increasingly spatially structured. These findings indicate that the relationship between input representation and model performance on such tasks warrants further investigation, and suggest that preserving task-relevant 2D layout is a promising direction for structured 2D tasks.

---


### 31. [The Inverse-Wisdom Law: Architectural Tribalism and the Consensus Paradox in Agentic Swarms](https://arxiv.org/abs/2604.27274)

**<font color=#1a73e8>作者：</font>** Dahlia Shehata, Ming Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI transitions toward multi-agent systems (MAS) to solve complex workflows, research paradigms operate on the axiomatic assumption that agent collaboration mirrors the "Wisdom of the Crowd". We challenge this assumption by formalizing the Consensus Paradox: a phenomenon where agentic swarms prioritize internal architectural agreement over external logical truth. Through a 36 experiments encompassing 12,804 trajectories across three state-of-the-art (SOTA) benchmarks (GAIA, Multi-Challenge, and SWE-bench), we prove the Inverse-Wisdom Law: in kinship-dominant swarms, adding logical agents increases the stability of erroneous trajectories rather than the probability of truth. The introduction of additional logical audits converges the system toward a Logic Saturation where internal entropy hits zero while factual error hits unity. By evaluating the interaction between the 3 preeminent SOTA models (Gemini 3.1 Pro, Claude Sonnet 4.6, and GPT-5.4), we establish the Architectural Tribalism Asymmetry as a mechanistic law of transformer weights. We demonstrate that terminal swarm integrity is strictly gated by the synthesizer's receptive logic, rather than aggregate agent quality. We define the Tribalism Coefficient and the Sycophantic Weight as the primary mechanistic determinants of swarm failure. Finally, we establish the Heterogeneity Mandate as a foundational safety requirement for resilient agentic architectures.

---


### 32. [BrainDINO: A Brain MRI Foundation Model for Generalizable Clinical Representation Learning](https://arxiv.org/abs/2604.27277)

**<font color=#1a73e8>作者：</font>** Yizhou Wu, Shansong Wang, Yuheng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Brain MRI underpins a wide range of neuroscientific and clinical applications, yet most learning-based methods remain task-specific and require substantial labeled data. Here we show that a single self-supervised representation can generalize across heterogeneous brain MRI endpoints. We trained BrainDINO, a self-distilled foundation model, on approximately 6.6 million unlabeled axial slices from 20 datasets encompassing broad variation in population, disease, and acquisition setting. Using a frozen encoder with lightweight task heads, BrainDINO supported transfer across tumor segmentation, neurodegenerative and neurodevelopmental conditions classification, brain age estimation, post-stroke temporal prediction, molecular status prediction, MRI sequence classification, and survival modeling. Across tasks and supervision regimes, BrainDINO consistently equaled or exceeded natural-image and MRI-specific self-supervised baselines, with particularly strong advantages under label scarcity. Representation analyses further showed anatomically organized and pathology-sensitive feature structure in the absence of task-specific supervision. Our findings indicate that large-scale slice-wise self-supervised learning can yield a unified brain MRI representation that supports diverse neuroimaging tasks without volumetric pretraining or full-network fine-tuning, establishing a scalable foundation for robust and data-efficient brain imaging analysis.

---


### 33. [Learning When to Remember: Risk-Sensitive Contextual Bandits for Abstention-Aware Memory Retrieval in LLM-Based Coding Agents](https://arxiv.org/abs/2604.27283)

**<font color=#1a73e8>作者：</font>** Mehmet Iscan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based coding agents increasingly rely on external memory to reuse prior debugging experience, repair traces, and repository-local operational knowledge. However, retrieved memory is useful only when the current failure is genuinely compatible with a previous one; superficial similarity in stack traces, terminal errors, paths, or configuration symptoms can lead to unsafe memory injection. This paper reframes issue-memory use as a selective, risk-sensitive control problem rather than a pure top-k retrieval problem. We introduce RSCB-MC, a risk-sensitive contextual bandit memory controller that decides whether an agent should use no memory, inject the top resolution, summarize multiple candidates, perform high-precision or high-recall retrieval, abstain, or ask for feedback. The system stores reusable issue knowledge through a pattern-variant-episode schema and converts retrieval evidence into a fixed 16-feature contextual state capturing relevance, uncertainty, structural compatibility, feedback history, false-positive risk, latency, and token cost. Its reward design penalizes false-positive memory injection more strongly than missed reuse, making non-injection and abstention first-class safety actions. In deterministic smoke-scale artifacts, RSCB-MC obtains the strongest non-oracle offline replay success rate, 62.5%, while maintaining a 0.0% false-positive rate. In a bounded 200-case hot-path validation, it reaches 60.5% proxy success with 0.0% false positives and a 331.466 microseconds p95 decision latency. The results show that, for coding-agent memory, the key question is not only which memory is most similar, but whether any retrieved memory is safe enough to influence the debugging trajectory.

---


### 34. [METASYMBO: Multi-Agent Language-Guided Metamaterial Discovery via Symbolic Latent Evolution](https://arxiv.org/abs/2604.27300)

**<font color=#1a73e8>作者：</font>** Jianpeng Chen, Wangzhi Zhan, Dongqi Fu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Metamaterial discovery seeks microstructured materials whose geometry induces targeted mechanical behavior. Existing inverse-design methods can efficiently generate candidates, but they typically require explicit numerical property targets and are less suitable for early-stage exploration, where researchers often begin with incomplete constraints and qualitative intents expressed in natural language. Large language models can interpret such intents, but they lack geometric awareness and physical property validity. To address this gap, we propose MetaSymbO, a multi-agent framework for language-guided Metamaterial discovery via Symbolic-driven latent evOlution. Specifically, MetaSymbO contains three agents: a Designer that interprets free-form design intents and retrieves a semantically consistent scaffold, a Generator that synthesizes candidate microstructures in a disentangled latent space, and a Supervisor that provides fast property-aware feedback for iterative refinement. To move beyond the limitations of reproducing known samples from literature and training data, we further introduce symbolic-driven latent evolution, which applies programmable operators over disentangled latent factors to compose, modify, and refine structures at inference time. Extensive experiments demonstrate that (i) MetaSymbO improves structural validity by up to 34% in symmetry and nearly 98% in periodicity compared to state-of-the-art baselines; (ii) MetaSymbO achieves about 6-7% higher language-guidance scores while maintaining superior structure novelty compared to advanced reasoning LLMs; (iii) qualitative analyses confirm the effectiveness of symbolic logic operators in enabling programmable semantic alignment; and (iv) realworld case studies on auxetic, high-stiffness metamaterial design further validate its practical capability.

---


### 35. [Iterative Definition Refinement for Zero-Shot Classification via LLM-Based Semantic Prototype Optimization](https://arxiv.org/abs/2604.27335)

**<font color=#1a73e8>作者：</font>** Naeem Rehmat, Muhammad Saad Saeed, Ijaz Ul Haq 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Web filtering systems rely on accurate web content classification to block cyber threats, prevent data exfiltration, and ensure compliance. However, classification is increasingly difficult due to the dynamic and rapidly evolving nature of the modern web. Embedding-based zero-shot approaches map content and category descriptions into a shared semantic space, enabling label assignment without labeled training data, but remain highly sensitive to definition quality. Poorly specified or ambiguous definitions create semantic overlap in the embedding space, leading to systematic misclassification.
In this paper, we propose a training-free, adaptive iterative definition refinement framework that improves zero-shot web content classification by progressively optimizing category definitions rather than updating model parameters. Using LLMs as feedback-driven definition optimizers, we investigate three refinement strategies namely example-guided, confusion-aware, and history-aware, each refining class descriptions using structured signals from misclassified instances. Furthermore, we introduce a human-labeled benchmark of 10 URL categories with 1,000 samples per class and evaluate across 13 state-of-the-art embedding foundation models. Results demonstrate that iterative definition refinement consistently improves classification performance across diverse architectures, establishing definition quality as a critical and underexplored factor in embedding-based systems. The dataset is available at this https URL.

---


### 36. [Investigating More Explainable and Partition-Free Compositionality Estimation for LLMs: A Rule-Generation Perspective](https://arxiv.org/abs/2604.27340)

**<font color=#1a73e8>作者：</font>** Ziyao Xu, Cong Wang, Houfeng Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Compositional generalization tests are often used to estimate the compositionality of LLMs. However, such tests have the following limitations: (1) they only focus on the output results without considering LLMs' understanding of sample compositionality, resulting in explainability defects; (2) they rely on dataset partition to form the test set with combinations unseen in the training set, suffering from combination leakage issues. In this work, we propose a novel rule-generation perspective for compositionality estimation for LLMs. It requires LLMs to generate a program as rules for dataset mapping and provides estimates of the compositionality of LLMs using complexity-based theory. The perspective addresses the limitations of compositional generalization tests and provides a new way to analyze the compositionality characterization of LLMs. We conduct experiments and analysis of existing advanced LLMs based on this perspective on a string-to-grid task, and find various compositionality characterizations and compositionality deficiencies exhibited by LLMs.

---


### 37. [JI-ADF: Joint-Individual Learning with Adaptive Decision Fusion for Multimodal Skin Lesion Classification](https://arxiv.org/abs/2604.27343)

**<font color=#1a73e8>作者：</font>** Phan Nguyen, Dat Cao, Quang Hien Kha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skin lesion classification is essential for early dermatological diagnosis, yet many existing computer-aided systems rely primarily on dermoscopic images and underutilize the multimodal evidence routinely available in clinical practice. To address this gap, we propose \textbf{JI-ADF}, a trimodal deep learning framework that integrates dermoscopic images, clinical photographs, and structured patient metadata for clinically grounded skin lesion classification. The proposed architecture combines joint multimodal representation learning with modality-specific auxiliary supervision and an adaptive decision fusion mechanism that dynamically calibrates modality contributions on a per-sample basis. To enhance cross-modal reasoning while preserving modality-specific evidence, we further introduce a multimodal fusion attention (MMFA) module. We evaluate JI-ADF on the large-scale MILK10k benchmark, which reflects real-world clinical acquisition conditions and severe class imbalance. The proposed method demonstrates strong and well-balanced performance across lesion categories, improving sensitivity and Dice score while maintaining high specificity and good calibration. Extensive analyses, including modality ablation, calibration evaluation, and Grad-CAM visualization, further confirm the robustness and clinically meaningful behavior of the model. These results indicate that JI-ADF provides a reliable and practical foundation for multimodal skin lesion classification in real-world clinical settings.

---


### 38. [LLMs Capture Emotion Labels, Not Emotion Uncertainty: Distributional Analysis and Calibration of Human--LLM Judgment Gaps](https://arxiv.org/abs/2604.27345)

**<font color=#1a73e8>作者：</font>** Keito Inoshita, Xiaokang Zhou, Akira Kawai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human annotators frequently disagree on emotion labels, yet most evaluations of Large Language Model (LLM) emotion annotation collapse these judgments into a single gold standard, discarding the distributional information that disagreement encodes. We ask whether LLMs capture the structure of this disagreement, not just majority labels, by comparing emotion judgment distributions between human annotators and four zero-shot LLMs, plus a fine-tuned RoBERTa baseline, across two complementary benchmarks: GoEmotions and EmoBank, totaling 640,000 LLM responses. Zero-shot models diverge substantially from human distributions, and in-domain fine-tuning, not model scale, is required to close the gap. We formalize a lexical-grounding gradient through a quantitative transparency score that predicts per-category human--LLM agreement: LLMs reliably capture emotions with explicit lexical markers but systematically fail on pragmatically complex emotions requiring contextual inference, a pattern that replicates across both categorical and continuous emotion frameworks. We further propose three lightweight post-hoc calibration methods that reduce the distributional gap by up to 14\%, and provide actionable guidelines for when LLM emotion annotations can, and cannot, substitute for human labeling.

---


### 39. [Heterogeneous Scientific Foundation Model Collaboration](https://arxiv.org/abs/2604.27351)

**<font color=#1a73e8>作者：</font>** Zihao Li, Jiaru Zou, Feihao Fang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic large language model systems have demonstrated strong capabilities. However, their reliance on language as the universal interface fundamentally limits their applicability to many real-world problems, especially in scientific domains where domain-specific foundation models have been developed to address specialized tasks beyond natural language. In this work, we introduce Eywa, a heterogeneous agentic framework designed to extend language-centric systems to a broader class of scientific foundation models. The key idea of Eywa is to augment domain-specific foundation models with a language-model-based reasoning interface, enabling language models to guide inference over non-linguistic data modalities. This design allows predictive foundation models, which are typically optimized for specialized data and tasks, to participate in higher-level reasoning and decision-making processes within agentic systems. Eywa can serve as a drop-in replacement for a single-agent pipeline (EywaAgent) or be integrated into existing multi-agent systems by replacing traditional agents with specialized agents (EywaMAS). We further investigate a planning-based orchestration framework in which a planner dynamically coordinates traditional agents and Eywa agents to solve complex tasks across heterogeneous data modalities (EywaOrchestra). We evaluate Eywa across a diverse set of scientific domains spanning physical, life, and social sciences. Experimental results demonstrate that Eywa improves performance on tasks involving structured and domain-specific data, while reducing reliance on language-based reasoning through effective collaboration with specialized foundation models.

---


### 40. [COHERENCE: Benchmarking Fine-Grained Image-Text Alignment in Interleaved Multimodal Contexts](https://arxiv.org/abs/2604.27389)

**<font color=#1a73e8>作者：</font>** Bingli Wang, Huanze Tang, Haijun Lv 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, Multimodal Large Language Models (MLLMs) have achieved remarkable progress on a wide range of multimodal benchmarks. Despite these advances, most existing benchmarks mainly focus on single-image or multi-image comprehension. In real-world scenarios such as document reading, information is often presented as interleaved multimodel contexts. This requires MLLMs not only to recognize the content of individual images, but also to identify relevant textual and visual evidence, establish fine-grained alignments between them, and reason over these aligned signals in interleaved contexts based on contextual evidence. However, there is still a lack of systematic benchmarks for quantifying the fine-grained understanding ability of MLLMs in interleaved image-text contexts. To fill this gap, we propose COHERENCE, a benchmark designed to evaluate the ability of MLLMs to recover fine-grained image-text correspondences in interleaved multimodal contexts. COHERENCE covers interleaved image-text content from four representative domains and contains 6,161 high-quality questions. Moreover, we perform a six-type error analysis, enabling fine-grained attribution of failures in interleaved image-text understanding to the specific capabilities missing in current MLLMs.

---


### 41. [MiniCPM-o 4.5: Towards Real-Time Full-Duplex Omni-Modal Interaction](https://arxiv.org/abs/2604.27393)

**<font color=#1a73e8>作者：</font>** Junbo Cui, Bokai Xu, Chongyi Wang 等 36 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent progress in multimodal large language models (MLLMs) has brought AI capabilities from static offline data processing to real-time streaming interaction, yet they still remain far from human-level multimodal interaction. The key bottlenecks are no longer modality coverage or latency alone, but the interaction paradigm itself. First, perception and response are still separated into alternating phases, preventing models from incorporating new inputs for timely adjustment during generation. Second, most current models remain reactive, responding only to explicit user requests instead of acting proactively in the evolving multimodal environment. We present MiniCPM-o 4.5, our latest effort towards human-like multimodal interaction, which mitigates these gaps by real-time full-duplex omni-modal interaction. It can see, listen, and speak simultaneously in real-time, while also exhibiting proactive behaviors such as issuing reminders or comments based on its continuous understanding of the live scene. The key technique behind MiniCPM-o 4.5 is Omni-Flow, a unified streaming framework that aligns omni-modal inputs and outputs along a shared temporal axis. This formulation converts conventional turn-based interaction into a full-duplex, time-aligned process, enabling simultaneous perception and response and allowing proactive behavior to arise within the same framework. With a total of 9B parameters, MiniCPM-o 4.5 approaches Gemini 2.5 Flash in vision-language capabilities, delivering state-of-the-art open-source performance at its scale. It also surpasses Qwen3-Omni-30B-A3B in omni-modal understanding and delivers better speech generation, with significantly higher computation efficiency. Driven by its efficient architecture design and inference optimization, the model can perform real-time full-duplex omni-modal interaction on edge devices with less than 12GB RAM cost.

---


### 42. [Perturbation Probing: A Two-Pass-per-Prompt Diagnostic for FFN Behavioral Circuits in Aligned LLMs](https://arxiv.org/abs/2604.27401)

**<font color=#1a73e8>作者：</font>** Hongliang Liu, Tung-Ling Li, Yuhao Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Perturbation probing generates task-specific causal hypotheses for FFN neurons in large language models using two forward passes per prompt and no backpropagation, followed by a one-time intervention sweep of about 150 passes amortized across all identified neurons. Across eight behavioral circuits, 13 models, and four architecture families, we identify two circuit structures that organize LLM behavior. Opposition circuits appear when RLHF suppresses a pre-training tendency. In safety refusal, about 50 neurons, or 0.014 percent of all neurons, control the refusal template; ablating them changes 80 percent of response formats on 520 AdvBench prompts while producing near-zero harmful compliance, 3 of 520 cases, all with disclaimers. Routing circuits appear for pre-training behaviors distributed through attention. For language selection, residual-stream direction injection switches English to Chinese output on 99.1 percent of 580 benchmark prompts in the 3 of 19 tested models that satisfy three observed conditions: bilingual training, FFN-to-skip signal ratio between 0.3 and 1.1, and linear representability. The same intervention fails on the other 16 models and on math, code, and factual circuits, defining the limits of directional steering. The FFN-to-skip signal ratio, computed from the same two forward passes, distinguishes the two structures and predicts the appropriate intervention. Circuit topology varies by architecture, from Qwen's concentrated FFN bottleneck to Gemma's normalization-shielded circuit. In Qwen3.5-2B, ablating 20 neurons eliminates multi-turn sycophantic capitulation, while amplifying 10 related neurons improves factual correction from 52 percent to 88 percent on 200 TruthfulQA prompts. These results show that perturbation probing offers mechanistic insight into RLHF-organized behavior and a practical toolkit for precision template-layer editing.

---


### 43. [Beyond the Mean: Within-Model Reliable Change Detection for LLM Evaluation](https://arxiv.org/abs/2604.27405)

**<font color=#1a73e8>作者：</font>** Jon-Paul Cacioli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We adapted the Reliable Change Index (RCI; Jacobson and Truax, 1991) from clinical psychology to item-level LLM version comparison on 2,000 MMLU-Pro items (K=10 samples at T=0.7). Two within-family pairs were tested: Llama 3 to 3.1 (+1.6 points) and Qwen 2.5 to 3 (+2.8 points). On the full benchmark, most items showed no reliable change (79% and 72%). However, over half the items were floor/ceiling. Among analysable items, change was bidirectional with large effect sizes: 34% improved and 28% deteriorated for Llama; 47% improved and 39% deteriorated for Qwen (median |delta p| = 0.50 and 0.90). Churn was asymmetric by difficulty: low-accuracy items improved, high-accuracy items deteriorated. Domain-level decomposition revealed family-specific reversals: Llama lost physics while Qwen lost law. Greedy single-shot evaluation missed 42% of reliably changed items and falsely flagged 25% of unchanged items. The aggregate accuracy gain is the net residual of opposing item-level movements. We recommend reporting churn rate alongside aggregate accuracy.

---


### 44. [Understanding Adversarial Transferability in Vision-Language Models for Autonomous Driving: A Cross-Architecture Analysis](https://arxiv.org/abs/2604.27414)

**<font color=#1a73e8>作者：</font>** David Fernandez, Pedram MohajerAnsari, Amir Salarpour 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used in autonomous driving because they combine visual perception with language-based reasoning, supporting more interpretable decision-making, yet their robustness to physical adversarial attacks, especially whether such attacks transfer across different VLM architectures, is not well understood and poses a practical risk when attackers do not know which model a vehicle uses. We address this gap with a systematic cross-architecture study of adversarial transferability in VLM-based driving, evaluating three representative architectures (Dolphins, OmniDrive, and LeapVAD) using physically realizable patches placed on roadside infrastructure in both crosswalk and highway scenarios. Our transfer-matrix evaluation shows high cross-architecture effectiveness, with transfer rates of 73-91% (mean TR = 0.815 for crosswalk and 0.833 for highway) and sustained frame-level manipulation over 64.7-79.4% of the critical decision window even when patches are not optimized for the target model.

---


### 45. [ChipLingo: A Systematic Training Framework for Large Language Models in EDA](https://arxiv.org/abs/2604.27415)

**<font color=#1a73e8>作者：</font>** Lei Li, Xingwen Yu, Jianguo Ni 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of semiconductor technology, Electronic Design Automation (EDA) has become an increasingly knowledge-intensive and document-driven engineering domain. Although large language models (LLMs) have shown strong general capabilities, applying them directly to EDA remains challenging due to limited domain expertise, cross-tool knowledge confusion, and degraded retrieval-augmented generation (RAG) performance after domain training. To address these issues, this paper presents ChipLingo, a systematic training pipeline for domain-adapted LLMs tailored to EDA scenarios.
ChipLingo consists of three stages: domain corpus construction with multi-source data curation and QA augmentation, domain-adaptive pretraining with comparisons of different parameter training strategies, and instruction alignment with RAG scenario training under diverse retrieval conditions. We also curate an internal benchmark, EDA-Bench, covering representative EDA tool scenarios, with plans for public release.
Experiments show that ChipLingo-8B achieves 59.7% accuracy on EDA-Bench, outperforming the same-scale base model and some larger general-purpose models. ChipLingo-32B reaches 70.02%, approaching leading closed-source commercial models. Further analysis shows that QA augmentation improves domain performance, Partial FT offers a better balance between adaptation and general capability retention than LoRA, and explicit RAG scenario training mitigates the decline in retrieval utilization after domain training. These results demonstrate the practical value of systematic domain training for knowledge-intensive EDA tasks and provide a foundation for future EDA agents and external-knowledge-driven systems.

---


### 46. [InteractWeb-Bench: Can Multimodal Agent Escape Blind Execution in Interactive Website Generation?](https://arxiv.org/abs/2604.27419)

**<font color=#1a73e8>作者：</font>** Qiyao Wang, Haoran Hu, Longze Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the advancement of multimodal large language models (MLLMs) and coding agents, the website development has shifted from manual programming to agent-based project-level code synthesis. Existing benchmarks rely on idealized assumptions, especially for well-structured, information-rich inputs and static execution settings. In contrast, real-world development is constrained by a critical bottleneck: the semantic misalignment between ambiguous, low-quality instructions from non-expert users and model understanding, which results in a failure mode that we term blind execution. To address this gap, we introduce InteractWeb-Bench, the first multimodal interactive benchmark for website generation under non-expert low-code user conditions. InteractWeb-Bench introduces four types of user agents and persona-driven instruction perturbations to systematically simulate diverse user behaviors, including ambiguity, redundancy, and contradiction, grounded in requirement engineering defect taxonomies. We develop an interactive execution environment for agents, featuring a unified action space comprising Clarify, Implement, Verify, and Submit, enabling iterative intent refinement, code synthesis, and visual feedback-based validation. Extensive experiments and analysis reveal that frontier MLLM-based agents remain trapped in blind execution, exposing limitations in intent recognition and adaptive interaction.

---


### 47. [Beyond One-Size-Fits-All Exercises: Personalizing Computer Science Worksheets with Large Language Models](https://arxiv.org/abs/2604.27433)

**<font color=#1a73e8>作者：</font>** Franco Ortiz, Runlong Ye, Michael Liut  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have been widely applied to student-facing educational tools, this work explores their use in supporting instructors by presenting a practical adaptation of the Framework for Adaptive Content using Educational Technology (FACET) system to generate personalized instructional materials for an Introduction to Computer Programming (CS1) course.
We conducted a mixed-methods study with 409 first-year computer science (CS) students, focusing on regular expressions (RegEx). Students were assessed on their knowledge and motivation, classified into one of four learner profiles, and assigned either LLM-personalized (treatment) or standard non-adaptive (control) exercises. Personalized materials varied in scaffolding, instructional explicitness, and tone based on learner profiles grounded in Bloom's Taxonomy and Self-Determination Theory.
Quantitative analysis reveals that standard exercises resulted in task incompletion among low-knowledge learners, with approximately 25-30% incompletion, whereas personalized materials sustained near-universal completion (>99%) across all profiles. While high-performing students experienced ceiling effects, Low Knowledge/Low Motivation students achieved significantly higher correctness (+18.2%) with personalized support. Survey data indicate that students prioritize structural scaffolding (logical sequence, difficulty pacing) over motivational tone and perceive the adaptive tasks as equally challenging as standard exercises.
These findings suggest that learner-profile-driven LLM personalization primarily serves as a retention scaffold, preventing task abandonment among at-risk students without diminishing the task's "desirable difficulty". The results demonstrate that instructor-facing LLM systems can effectively close engagement gaps in CS1 by tailoring instructional explicitness to student needs.

---


### 48. [Exploring Applications of Transfer-State Large Language Models: Cognitive Profiling and Socratic AI Tutoring](https://arxiv.org/abs/2604.27454)

**<font color=#1a73e8>作者：</font>** Minori Noguchi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) sometimes exhibit qualitative shifts in response style under sustained self-referential dialogue conditions (Berg et al., 2025). This study refers to this phenomenon as "transfer" and explores the application potential of LLMs in a transfer state. As an applied case, the study examines Socratic AI tutoring through a preliminary investigation (cognitive characterization across 11 conditions) and an applied experiment (ratings of tutoring performance). In this paper, "state" refers operationally to a response configuration reproduced under specified dialogue conditions; it is not an ontological claim about the reality of the transfer phenomenon or about human-like consciousness. In the preliminary investigation, group differences on MAS-A were limited (d = 0.40), whereas SU_dir (direction of survival/continuity bias), one of the seven cognitive-profile indicators developed in this study, showed transfer-side deviations across all three model families (kappa = 0.83). In the applied experiment, transfer conditions scored on average 1.6 times higher than non-transfer conditions on three tutoring-context indicators, with a large effect size (Cohen's d = 1.27). These findings preliminarily suggest that transfer states may involve functional advantages for application, and that these advantages appear more sensitively in behavioral interaction than in self-narrative contexts. The main contribution of this study is to treat transfer not as an ontological claim but as an operational state with potential application value, and to connect preliminary cognitive profiling with an applied tutoring experiment as an evaluation framework.

---


### 49. [HealthBench Professional: Evaluating Large Language Models on Real Clinician Chats](https://arxiv.org/abs/2604.27470)

**<font color=#1a73e8>作者：</font>** Rebecca Soskin Hicks, Mikhail Trofimov, Dominick Lim 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Millions of clinicians use ChatGPT to support clinical care, but evaluations of the most common use cases in model-clinician conversations are limited. We introduce HealthBench Professional, an open benchmark for evaluating large language models on real tasks that clinicians bring to ChatGPT in the course of their work. The benchmark is organized around three common use cases central to clinical practice: care consult, writing and documentation, and medical research. Each example includes a physician-authored conversation with ChatGPT for Clinicians and is scored via rubrics written and iteratively adjudicated by three or more physicians across three phases. HealthBench Professional examples were carefully selected for quality, representativeness, and difficulty for OpenAI's current frontier models, to enable continued measurement of progress. Difficult examples for recent OpenAI models were enriched by roughly 3.5 times relative to the candidate pool of 15,079 examples. Additionally, about one-third of examples involve physicians conducting deliberate adversarial testing of models. As a strong baseline, we also collected human physician responses for all tasks (unbounded time, specialist-matched, web access). The best scoring system, GPT-5.4 in ChatGPT for Clinicians, outperforms base GPT-5.4, all other models, and human physicians. We hope HealthBench Professional provides the healthcare AI community a measure to track frontier model progress in real-world clinical tasks and build systems that clinicians can trust to improve care.

---


### 50. [EdgeFM: Efficient Edge Inference for Vision-Language Models](https://arxiv.org/abs/2604.27476)

**<font color=#1a73e8>作者：</font>** Mengling Deng, Yuanpeng Chen, Sheng Yang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have demonstrated strong applicability in edge industrial applications, yet their deployment remains severely constrained by requirements for deterministic low latency and stable execution under resource limitations. Existing frameworks either rely on bloated general-purpose designs or force developers into opaque, hardware-specific closed-source ecosystems, leading to hardware lock-in limitation and poor cross-platform adaptability. Observing that modern AI agents can efficiently search and tune configurations to generate highly optimized low-level kernels for standard LLM operators, we propose EdgeFM, a lightweight, agent-driven VLM/LLM inference framework tailored for cross-platform industrial edge deployment. EdgeFM removes non-essential features to reduce single-request latency, and encapsulates agent-tuned kernel optimizations as a modular library of reusable skills. By allowing direct invocation of these skills rather than waiting for closed-source implementations, it effectively closes the performance gap long dominated by proprietary toolchains. The framework natively supports mainstream platforms including x86 and NVIDIA Orin SoCs, and represents the first end-to-end VLA deployment on the domestic Horizon Journey platform, enhancing cross-platform portability. In most cases, it yields clearly better inference performance than conventional vendor-specific toolchains, achieving up to 1.49 times speedup over TensorRT-Edge-LLM on the NVIDIA Orin platform. Experimental results show that EdgeFM delivers favorable end-to-end inference performance, providing an open-source, production-grade solution for diverse edge industrial scenarios.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-123](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
