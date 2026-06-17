# 🧠 大模型相关研究 | 2026年06月18日

> 本类共 **133** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-133](./part-03.md)

---

### 51. [Surrogate Assisted Pedestrian Protection Design via a Foundation Model Orchestrated Workflow](https://arxiv.org/abs/2606.17577)

**<font color=#1a73e8>作者：</font>** Osamu Ito, Akihiko Katagiri, Yoshikazu Nakagawa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-driven engineering workflows face particular challenges in crash safety design: unlike aerodynamics, crash events involve highly nonlinear contact dynamics, material nonlinearity, and discrete state transitions that are difficult to capture with data-driven surrogate models. To the best of our knowledge, we present the first foundation model--orchestrated workflow for crash safety design that enables surrogate-assisted exploration for pedestrian protection, reducing evaluation time from hours per CAE simulation to seconds.
The workflow integrates four components: (1) a surrogate trained on CAE crash simulations to predict pedestrian leg injury metrics from design parameters, achieving an average $R^2=0.87$ and providing distribution-free conformal prediction intervals; (2) multiobjective evolutionary search (NSGA-II) to discover diverse feasible parameter sets under user-specified constraints; (3) a morphing-based geometry generator that maps parameters to topology-preserving 3D shapes; and (4) a natural-language interface in which an LLM orchestrates the workflow and a vision--language model supports semantic comparison of generated designs.
In an automotive front-bumper case study, the workflow produces 35 distinct safety-compliant alternatives from a single exploration, a process that would require weeks with conventional CAE iteration. These results suggest that foundation models can serve as integration layers between ML surrogates and physics-based simulation, helping bring AI capabilities to safety-critical engineering domains.

---


### 52. [LLM Features Can Hurt GNNs: Concatenation Interference on Homophilous Graph Benchmarks](https://arxiv.org/abs/2606.17579)

**<font color=#1a73e8>作者：</font>** Zhongyuan Wang, Pratyusha Vemuri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adding LLM-generated node features to graph neural networks (GNNs) is widely reported to improve accuracy on standard benchmarks. We document a contrasting observation: when LLM features are introduced through pure input concatenation (rather than joint training, distillation, or prompt-conditioning), they can systematically degrade accuracy on the same homophilous benchmarks where end-to-end LLM pipelines succeed. With an MLP backbone on the Planetoid public split and bag-of-words original features, concatenating SBERT-encoded GPT-4o-mini TAPE features reduces PubMed test accuracy by -17.0 +/- 0.3 pp and Cora by -4.3 +/- 0.6 pp (CiteSeer -0.6 +/- 0.8 pp, within seed noise). The drop attenuates as we relax each condition (GCN / GCNII / GAT backbones, random splits, smaller encoders) and reverses on medium-homophily WikiCS (+4.4 pp) and ogbn-arxiv (+11.7 pp). To predict when concatenation helps versus hurts, we report a simple measure of LLM-alone discriminability, Delta_sig. Across 9 datasets Delta_sig correlates with the concatenation cost more strongly than homophily at point estimate (r^2 = 0.38 vs. 0.06; N=9, bootstrap CIs overlap). The bootstrap-best change-point is tau = 13.8 pp, and the rule "Delta_sig <= tau predicts non-positive concat cost" classifies 7/9 datasets correctly; since 60% of bootstrap samples place tau in [5, 30] pp, we treat Delta_sig as an interpretive lens rather than a precision filter. A dimension-controlled ablation on PubMed places the LLM-feature drop between same-source PCA (-2.3 pp) and same-dim Gaussian noise (-37.3 pp), ruling out dimensionality and weight-decay artifacts. Nine PubMed configurations fit a power law |Delta_concat| proportional to (sqrt(d_l/n))^1.31 with r^2 = 0.97; the low-Delta_sig, small-n corner is exactly where the headline -17 pp PubMed deficit appears.

---


### 53. [The Benchmark Illusion: Pruned LLMs Can Pass Multiple Choice but Fail to Answer](https://arxiv.org/abs/2606.17609)

**<font color=#1a73e8>作者：</font>** Rui Wen, Lu Sun, Jiayang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Compressing large language models reduces memory use and inference cost, but it can also create failures that standard benchmarks miss. A pruned model may still perform well on multiple-choice evaluations, yet fail to answer the same question in open generation. We ask what pruning changes: does it erase the correct answer, or does it make the answer harder to produce as the top output?
We study this question with multilingual question answering, tracking the same questions before and after pruning. We find a benchmark illusion. Under high-sparsity pruning, especially Wanda, models often fail in greedy open generation while still selecting the correct answer under multiple-choice scoring. In these recognition-only errors, the answer is usually not gone, but demoted: it often reappears with beam search, sampling, or one in-context example. Overall, multiple-choice benchmarks can overstate the usability of compressed LLMs, creating an evaluation blind spot. Compressed models should be tested on what they can produce, not only on what they can recognize.

---


### 54. [SkillMoV: Mixture-of-View Routing with Prototype-Conditioned Gating for Unified Multi-View Proficiency Estimation](https://arxiv.org/abs/2606.17615)

**<font color=#1a73e8>作者：</font>** Edoardo Bianchi, Antonio Liotta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating human proficiency from video is a key challenge for automated skill assessment, with applications in sports coaching, music pedagogy, surgical training, and workplace learning. Existing approaches often focus on individual scenarios or rely on shared multi-view aggregation, limiting their ability to adapt to heterogeneous camera viewpoints and activity domains. We introduce SkillMoV, a unified, parameter-efficient framework for multi-scenario proficiency estimation from synchronized multi-view video. At its core, SkillMoV introduces a Mixture-of-View Projector (MoVP), which adapts the mixture-of-experts paradigm to camera-specific view features. MoVP is composed of four stages: (i) a Mixture-of-View soft router with twelve expert MLPs that learns view-dependent expert preferences without camera-identity supervision; (ii) cross-view attention to align synchronized cameras; (iii) learnable prototype anchoring to condition the representation on class-level reference vectors; and (iv) a prototype-conditioned gated projection that produces the final skill embedding. We evaluate SkillMoV on EgoExo4D across six skill domains and three separately trained view configurations: Ego, Exos, and Ego+Exos. SkillMoV reaches 50.17% overall accuracy in the Exos setting with a single model trained jointly across all scenarios, surpassing the strongest reported Exos result among the compared methods by 3.57 percentage points. In Ego+Exos, SkillMoV remains close to the best reported result in that setting (47.63% versus 48.20%). Ablations on the selected Exos configuration validate each component: MoV routing contributes +6.61 pp over attentive aggregation, cross-view attention +4.92 pp, prototype anchoring +4.07 pp, and stochastic view dropout +3.90 pp. Through LoRA adaptation, SkillMoV trains only 23.32% of its parameters and adds limited measured overhead relative to a LoRA-only baseline.

---


### 55. [RAVA: Retrieval-Augmented Viewpoint Alignment for Subject-Driven Image Generation](https://arxiv.org/abs/2606.17619)

**<font color=#1a73e8>作者：</font>** Qiwei Yan, Zhiqiang Yuan, Chongyang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-driven image generation has made rapid progress on identity preservation, but reliable viewpoint control across different subjects remains poorly understood. The difficulty is not merely generating a new image of the target subject: the model must infer the implicit viewpoint of one subject and transfer it to another subject using only image-level evidence, without camera poses, depth, or ray-based conditions. In this setting, existing generators conditioned on multiple image references often rely on spurious semantic correlations, which lead to viewpoint drift, part-level structural mismatches, and missing or unsupported target-specific content. We formulate this challenge as cross-subject viewpoint alignment and propose RAVA, a retrieval-augmented framework that supplies explicit geometric evidence before generation. RAVA first learns a cross-instance viewpoint embedding that retrieves target-subject images aligned with the anchor viewpoint, then applies a LogDet-based subset selection strategy to retain a compact reference set that is both view-consistent and structurally complementary. The selected references are finally consumed by a fine-tuned multi-reference image generator. Experiments show that generic semantic embeddings are nearly random for this task, while the proposed retriever substantially improves viewpoint retrieval quality. On cross-subject generation, RAVA consistently outperforms zero-shot baselines and stronger retrieval alternatives under the same generation backbone. These results indicate that cross-subject viewpoint alignment benefits from retrieval-augmented geometric grounding rather than relying on end-to-end generation alone.

---


### 56. [Prompt Perturbation for Reliable LLM Evaluation over Comparison Graphs](https://arxiv.org/abs/2606.17634)

**<font color=#1a73e8>作者：</font>** Dong Huang, Jianbo Sun, Pengkun Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating large language models (LLMs) is important for understanding their capabilities, comparing competing systems, and supporting the deployment of reliable models in practice. For open-ended tasks, pairwise evaluation has become a popular paradigm, in which two responses to the same prompt are compared and the resulting judgments are aggregated into an overall ranking. A central challenge of this paradigm is intransitivity: the induced comparison outcomes may fail to support any coherent global ranking. For example, one may observe cyclic preferences such as $A \succ B \succ C \succ A$, or inconsistencies involving ties such as $A \equiv B\equiv C\neq A$. Such contradictions make the resulting leaderboard unstable and challenging to interpret. In this paper, we propose a prompt perturbation framework for improving the consistency of pairwise LLM evaluation. Our approach generates perturbed variants of each prompt, uses the resulting comparison graphs to identify and filter out structurally inconsistent comparison patterns, and then applies standard ranking methods to the filtered comparisons. A key feature of the proposed framework is that graph-level structural consistency is incorporated explicitly into the evaluation pipeline before ranking aggregation. This provides a simple and principled way to reduce cyclic inconsistencies and improve the reliability of LLM rankings.

---


### 57. [Brick-DICL: Dynamic In-Context Learning for Automated Brick Schema Classification](https://arxiv.org/abs/2606.17637)

**<font color=#1a73e8>作者：</font>** Yiyue Qian, Shinan Zhang, Huan Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Building Management Systems (BMS) are essential for optimizing energy efficiency and operational performance in modern buildings. However, the lack of standardization across BMS points from different manufacturers creates significant barriers to integration and data utilization. While the Brick schema offers a standardized ontology for building systems, mapping BMS points to appropriate Brick classes presents three critical challenges: (i) the extensive number of Brick classes (936 in the latest version), (ii) limited domain-specific knowledge in large language models (LLMs), and (iii) substantial manual effort required for verification. To address these challenges, we propose Brick-DICL, a two-stage dynamic in-context learning framework for automated Brick schema classification. Brick-DICL consists of two primary components: metadata-RAG, which retrieves relevant examples to enhance LLMs' domain knowledge, and class-RAG, which narrows down potential Brick classes to address the large classification space. Additionally, we implement a multi-LLM filtering mechanism that compares predictions across multiple models, flagging low-confidence classifications for human review. As a result: (i) General: Brick-DICL is applicable to any building management system regardless of manufacturer or metadata format; (ii) Novel and Powerful: as the first dynamic in-context learning approach for Brick schema classification, Brick-DICL achieves significant classification accuracy improvements on building datasets, outperforming existing methods; (iii) Efficient: our multi-LLM filtering strategy reduces manual verification effort, enabling rapid digital building onboarding. Extensive experiments demonstrate Brick-DICL's effectiveness across diverse building datasets, accelerating the path toward standardized, interoperable building management systems.

---


### 58. [FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness](https://arxiv.org/abs/2606.17642)

**<font color=#1a73e8>作者：</font>** Pianran Guo, Pengcheng Zhou, Yucheng Jian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial multimodal reasoning requires agents to coordinate numerical computation, retrieval, visual interpretation, and temporal grounding across heterogeneous evidence sources. Existing tool-augmented agents improve execution fidelity, yet remain largely stateless across episodes, repeatedly rediscovering reasoning strategies and failure patterns. In high-stakes financial settings, this leads to unreliable tool routing, noisy retrieval, and hallucination-prone reasoning. We present FinAcumen, a financial reasoning agent framework centered on selective experience memory for tool-augmented multimodal reasoning. FinAcumen accumulates financially grounded reasoning experience from prior trajectories, distilling successful strategies and failure-derived cautionary rules into a persistent memory bank. During inference, retrieved experiences condition reasoning only when semantic relevance exceeds a calibrated threshold, while irrelevant memory is explicitly suppressed through a fallback mechanism. A deterministic financial tool environment further grounds numerical computation, retrieval, visual decoding, and answer this http URL four financial multimodal reasoning benchmarks, FinAcumen consistently improves a frozen 8B vision-language model over finance-specialized models and approaches leading proprietary general-purpose models. Further analysis shows that selective experience activation improves reasoning reliability under retrieval uncertainty. Our code is anonymously available at this https URL

---


### 59. [Beyond Domains: Reusing Web Skills via Transferable Interaction Patterns](https://arxiv.org/abs/2606.17645)

**<font color=#1a73e8>作者：</font>** Shiqi He, Yue Cui, Feijie Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) web agents are usually deployed as tool callers: each turn, the model reads a fresh page observation and emits one structured tool action. When every action is a low-level primitive, horizons grow quickly and so do policy-facing LLM completions, dominating latency and cost on benchmarks such as Mind2Web and WebArena. Recent systems therefore wrap repeated interaction fragments as web skills: callable tools built from successful trajectories or induced programs, so one call can replace several primitives. However, prior skill libraries are still triggered mainly by instruction similarity or coarse site metadata, which yields low skill reuse on held-out sites and leaves much of the potential step and token reduction on the table.
We present SkillMigrator, an agent that learns reusable web skills and transfers them across sites by matching layout structure rather than specific element references. Each induced skill is stored as a transferable interaction pattern (TIP): the skill paired with a structural sketch of the snapshot at induction time. At test time, SkillMigrator retrieves TIPs by layout similarity and grounds their references on the live page. The rest of the stack is standard: accessibility-snapshot observations with stable references, and fixed tool calling over primitives plus skill invocations. Compared with the state-of-the-art approaches, SkillMigrator reduces the average LLM-action count on successful trajectories by 8-10% across both WebArena and Mind2Web at matched success rate.

---


### 60. [From Brewing to Resolution: Tracing the Internal Lifecycle of Code Reasoning in LLMs](https://arxiv.org/abs/2606.17648)

**<font color=#1a73e8>作者：</font>** Siyue Chen, Yifu Guo, Yuquan Lu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Standard accuracy metrics cannot explain why LLMs handle variable tracking but fail on semantically equivalent loops. We study an internal lifecycle of code reasoning in which models first brew the answer, making it linearly recoverable many layers before it becomes self-decodable, and then diverge into one of four resolution outcomes: Resolved, Overprocessed, Misresolved, or Unresolved. Understanding this lifecycle matters because similar task accuracies can mask fundamentally different failure modes that surface-level evaluation cannot detect. We introduce a dual diagnostic framework pairing layer-wise linear probing with Context-Stripped Decoding (CSD) and apply it to six code-reasoning task families across 16 models spanning Qwen, Llama, and DeepSeek architectures. All four outcomes carry substantial mass in every task family: overall Resolved is only 41.5%, with multiple tasks below 30%. Controlled sweeps over structure, depth, and operators expose task-specific failure bottlenecks: Function Call Resolved plunges from 61.1% to 2.5% as call depth increases from one to three. Across architectures and scales, the brewing scaffold remains stable, with normalized brewing duration 24-42% across all 16 models, while resolution success varies with capability. This indicates that the scaffold is a stable empirical regularity across the tested decoder-only Transformer families, whereas resolution success covaries with capability, scale, and training. Code: this https URL

---


### 61. [A Risk Decomposition Framework for Pre-Hoc Fine-Tuning Prediction](https://arxiv.org/abs/2606.17649)

**<font color=#1a73e8>作者：</font>** Yuxiang Luo, Chen Wang, Nan Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The high cost of fine-tuning LLMs poses a significant economic barrier; pre-hoc performance prediction offers a critical solution to substantially reduce this expense. However, the theoretical limits of pre-hoc performance prediction remain unexplored. We formulate it as a stochastic estimation problem under information constraints, decomposing prediction risk into two components: an intrinsic limit (static data-model compatibility) and a reducible optimization variance. We prove that optimization variance admits a necessary lower bound on its decay rate, implying fundamental constraints on how quickly uncertainty dissipates, regardless of the predictor used. Based on these dynamics, we derive a budget-optimal probing principle and introduce a predictability phase diagram that organizes tasks into three distinct regimes: Static-Sufficient, Dynamic-Critical, and Noise-Dominant. Extensive experiments on synthetic and real-world benchmarks validate these theoretical regimes and demonstrate the efficiency of our probing strategy.

---


### 62. [Using Cognitive Models to Improve Language Model Simulation of Human Persuasion Games](https://arxiv.org/abs/2606.17657)

**<font color=#1a73e8>作者：</font>** Zirui Cheng, Zeyu Shen, Thomas L. Griffiths 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> People make decisions differently in strategic interactions. Some update beliefs like a Bayesian; others exhibit biases like motivated reasoning. Although creators of large language models use simulated humans for safety evaluations and training, they often fail to cover this breadth of human behavior. We argue that cognitive science and economics provide a convenient tool for doing so, making use of mathematical models of human decision-making. We propose an approach that we call Equation-to-Behavior Prompting for guiding large language models to match cognitive models, and evaluate this approach on persuasion games based on legal decision-making. We find that large models can approximate equation-based specifications -- Bayesian updating, affine distortion, motivated updating, and Grether's $\alpha$-$\beta$ model -- using prompting, but small models fail to do so. However, training small models with reinforcement learning to adhere to mathematical rules, Equation-to-Behavior RL, reduces belief error by 26.5% in out-of-distribution parameterizations. We show that these simulations can help create diverse training environments; training small models to consider different kinds of decision-makers improves average belief change by 2.5%--12% over Bayesian-only training, even when persuading GPT-5-mini. Our work could improve human simulations for training and evaluation in increasingly realistic settings, and could also enable novel research into more complicated mathematical models of human decision-making.

---


### 63. [TuneAhead: Predicting Fine-tuning Performance Before Full Training Begins](https://arxiv.org/abs/2606.17660)

**<font color=#1a73e8>作者：</font>** Yuxiang Luo, Haonan Long, Chen Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models (LLMs) is compute-intensive and error-prone: model performance depends sensitively on data quality and hyperparameter choices, and naïve runs can even degrade model performance. This raises a practical question:can we predict fine-tuning performance before committing to a full training run? We present TUNEAHEAD, a lightweight framework for pre-hoc prediction of fine-tuning performance. TUNEAHEAD encodes each candidate run as a meta-feature vector that combines static dataset descriptors with dynamic probe features from a short standardized probe. A predictor maps these features to performance estimates, while SHAP-based attributions provide interpretable diagnostics that reveal which specific features drive the prediction. Across 1,300+ fine-tuning runs on Qwen2.5-7B-Instruct, TUNEAHEAD consistently outperforms strong baselines such as Early-Stop Extrapolation and ProxyLM. On a held-out test set of 370 runs, TUNEAHEAD achieves an RMSE of 1.47 percentage points and places 95.1% of predictions within +3/-3 percentage points of the true score. These accurate continuous predictions support practical go/no-go screening policies that can reduce unnecessary full fine-tuning while retaining most promising runs.

---


### 64. [See First, Answer Later: Visual Evidence Pre-Alignment via Sufficiency-Driven RL](https://arxiv.org/abs/2606.17678)

**<font color=#1a73e8>作者：</font>** Yilian Liu, Sicong Leng, Guoshun Nan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) integrate strong text reasoning with visual inputs, yet their responses can be inconsistent with the underlying images, indicating ineffective utilization of visual evidence during inference. The prevailing training paradigm relies on large-scale caption-based pretraining for general alignment, followed by supervised fine-tuning and reinforcement learning to enable instruction following and complex reasoning. However, such pretraining provides only weak visual grounding: short, coarse captions bias models toward salient objects while neglecting fine-grained visual evidence. In this paper, we introduce Visual Evidence Pre-Alignment (VEPA), an intermediate stage between pretraining and post-training that explores a novel sufficiency-driven objective with Group Relative Policy Optimization (GRPO) to optimize question-conditioned visual evidence descriptions. Extensive experiments across diverse benchmarks show that our VEPA consistently enhances performance on visually demanding evaluations and complements standard supervised post-training. Further analyses show that the income stems from strengthened, transferable visual grounding, rather than from additional task-specific training.

---


### 65. [EnvRL: Learn from Environment Dynamics in Agentic Reinforcement Learning](https://arxiv.org/abs/2606.17680)

**<font color=#1a73e8>作者：</font>** Zhitong Wang, Songze Li, Hao Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has emerged as a powerful paradigm for training Large Language Models (LLMs) as agents. However, conventional RL methods for long-horizon agentic tasks often struggle with sparse outcome rewards. Intuitively, this overlooks the rich environment dynamics information contained in rollout interaction trajectories. We argue that the interaction experience inherently serves as an implicit supervision signal, reveals the underlying transition mechanisms of the environment, and enables the agent to construct a more accurate internal model of the environment.. Therefore, in this work, we investigate how to leverage this additional signal to improve policy learning. Specifically, we propose EnvRL, a framework that incorporates environment dynamics learning into agentic RL via two auxiliary objectives: state prediction and inverse dynamics. By jointly optimizing with the primary RL objective, we encourage the agent to internalize environment dynamics from its own interaction experience. Extensive experiments on two long-horizon agentic benchmarks demonstrate that EnvRL achieves significant improvements on success-rates over RL-only baselines, e.g., when trained with GRPO, lifting Qwen-2.5-1.5B-Instruct from 72.8% to 77.4% on ALFWorld, and from 56.8% to 67.0% on WebShop.

---


### 66. [From Trainee to Trainer: LLM-Designed Training Environment for RL with Multi-Agent Reasoning](https://arxiv.org/abs/2606.17682)

**<font color=#1a73e8>作者：</font>** Chao Chen, Chengzu Li, Zhiwei Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning pipelines for Large Language Model (LLM) training often rely on manually redesigned environments between stages, requiring practitioners to heuristically infer which configuration will best improve the current policy. To automate this process, we propose the LLM-as-Environment-Engineer framework in which the current policy model analyzes failure trajectories together with contextual information and proposes modifications to the next-stage training environment configuration. We also introduce MAPF-FrozenLake, a controllable testbed whose generator exposes multi-dimensional environment configurations, making it suitable for studying and benchmarking environment redesign. On this testbed, we condition the environment engineer on structured summaries of policy behavior, failure cases, and environment statistics, from which it produces the configuration for the next training stage. With Qwen3-4B as the backbone, our framework achieves the strongest aggregate performance on our benchmarks, outperforming larger proprietary LLMs (e.g., GPT, Gemini) and fixed-environment training baselines. We further analyze which forms of context are most effective, finding that successful environment updates rely on failure evidence and preserve configurations that already work. Interestingly, the current RL checkpoint serves as a better environment engineer than the original base model, suggesting that policy learning improves the model's ability to diagnose its remaining weaknesses.

---


### 67. [Bridging Functional Correctness and Runtime Efficiency Gaps in LLM-Based Code Translation](https://arxiv.org/abs/2606.17683)

**<font color=#1a73e8>作者：</font>** Longhui Zhang, Jiahao Wang, Chenhao Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While large language models (LLMs) have greatly advanced the functional correctness of automated code translation systems, the runtime efficiency of translated programs has received comparatively little attention. With the waning of Moore's law, runtime efficiency has become increasingly important for program quality, alongside functional correctness. Our preliminary study reveals that LLM-translated programs often run slower than human-written ones, and this issue cannot be remedied through prompt engineering alone. Therefore, our work proposes SwiftTrans, a code translation framework comprising two key stages: (1) Multi-Perspective Exploration, where MpTranslator leverages parallel in-context learning (ICL) to generate diverse translation candidates; and (2) Difference-Aware Selection, where DiffSelector identifies the optimal candidate by explicitly comparing differences between translations. We further introduce Hierarchical Guidance for MpTranslator and Ordinal Guidance for DiffSelector, enabling LLMs to better adapt to these two core components. To support the evaluation of runtime efficiency in translated programs, we extend existing benchmarks, CodeNet and F2SBench, and introduce a new benchmark, SwiftBench. Experimental results across all three benchmarks show that SwiftTrans achieves consistent improvements in both correctness and runtime efficiency.

---


### 68. [LLMs Infer Cultural Context but Fail to Apply It When Responding](https://arxiv.org/abs/2606.17688)

**<font color=#1a73e8>作者：</font>** Yisong Miao, Jian Zhu, Vered Shwartz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that LLMs overrepresent dominant cultures, particularly Western ones, while marginalizing others. We investigate whether this affects models' ability to generate culturally adapted responses by evaluating their use of local measurement units based on the user's perceived cultural background. We introduce Cultural and Pragmatic Response Inference (CAPRI), a dataset of conversations with varying levels of cultural cues. Experiments with state-of-the-art LLMs show that models can infer cultural background and recall relevant conventions, but often fail to utilize the information to adapt their answers to the relevant cultural conventions, unless explicitly prompted to perform the tasks sequentially. We further evaluate adaptation to the interpretation of time and quantity expressions, two subjective language grounding dimensions that are affected by culture. We find that models increasingly adapt their answers as cultural cues accumulate, but their priors are not culture-neutral, sometimes aligning with the model's country of origin. Overall, CAPRI provides a resource for future research aimed at narrowing the gap between cultural knowledge and culturally adaptive language generation.

---


### 69. [FllumaOne: A Code-Native Multimodal CAD Dataset with Executable Programs and Kernel-Validated Feature Histories](https://arxiv.org/abs/2606.17696)

**<font color=#1a73e8>作者：</font>** Jizong Zhan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parametric computer-aided design records both final geometry and the ordered construction history that determines how a part can be edited. Datasets for editable CAD research should therefore expose modeling operations, parameters, and feature dependencies together with validated geometry. We introduce FllumaOne, a code-native multimodal CAD dataset whose models are generated by executable Python programs in Flluma, a Qt/C++ OpenCASCADE-based CAD system. Each sample aligns its program with a structured feature tree, a training-oriented intermediate representation, STEP geometry, a surface point cloud, natural-language descriptions, metadata, and eight canonical visible-edge renderings.
The primary release, FllumaOne-100K, contains 100,000 accepted samples across four template-level complexity regimes. Programs are executed and retained only after kernel geometry, solid validity, and export checks; release reports also record modality completeness and split-level duplicate tests. A Qwen2.5-Coder-1.5B LoRA baseline trained on 80,000 samples achieves 99.98% Python syntax validity, 99.97% Flluma build success, and 99.14% STEP-export validity on the held-out 10,000-sample test split. For the 9,909 predictions converted to surface point clouds, the mean normalized Chamfer Distance is 0.002124. The dataset supports conditioned CAD reconstruction, executable program synthesis, feature-tree prediction, B-Rep analysis, retrieval, design completion, and editable reverse engineering.

---


### 70. [SegTME-UNI2: A Foundation Model-Based Framework for Generalisable Multiclass Cell Segmentation and LLM-Driven Tumour Microenvironment Characterisation in Histopathology](https://arxiv.org/abs/2606.17702)

**<font color=#1a73e8>作者：</font>** Wan Siti Halimatul Munirah Wan Ahmad, Faris Syahmi Samidi, Mohammad Badal Ahmmed 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Characterising the tumour microenvironment (TME) from routine H&E-stained histology images requires simultaneous cell segmentation, feature extraction, and interpretable clinical reporting. We present SEGTME-UNI2, a unified framework addressing these requirements. Its core is UNI2-UPERHOVER, a dual-head segmentation model pairing the UNI2-H pathology foundation model (ViT-Giant, pretrained on >100M tiles from 100K slides) with two parallel UperNet decoders: one for six-class semantic segmentation and one for horizontal-vertical gradient regression enabling watershed-based nuclear instance separation. To address the lack of pixel-level annotations in large real-world repositories, UNI2-UPERHOVER undergoes a three-stage progressive pseudo-label curriculum. Each stage trains a fresh model without weight transfer, driving improvement entirely via increased pseudo-label quality: Stage 1: Uses human-annotated PanNuke (7,901 images, 189,744 nuclei, 0.25 um/pixel). Stage 2: Uses entropy-filtered pseudo-labels from the Stage 1 model on 271,711 TCGA-UT scale-0 patches (0.5 um/pixel). Stage 3: Uses pseudo-labels from the Stage 2 model on all 1,608,060 TCGA-UT patches across six resolution scales (0.5-1.0 um/pixel). Segmentation outputs feed a structured TME feature extraction pipeline computing 20+ per-patch compositional, morphological, spatial entropy, and intercellular distance metrics. These are encoded as JSON and passed to a fine-tuned NVIDIA BioNeMo GPT model to generate clinically interpretable TME narratives. Preliminary validation on held-out PanNuke and TCGA-UT partitions demonstrates framework feasibility and internal consistency. The pseudo-labelled TCGA-UT dataset and UNI2-UPERHOVER checkpoint are publicly released to support large-scale TME profiling and spatial biology research.

---


### 71. [Vision-language models for chest radiography do not always need the image](https://arxiv.org/abs/2606.17710)

**<font color=#1a73e8>作者：</font>** Mahshad Lotfinia, Sebastian Ziegelmayer, Lisa Adams 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models report strong chest radiograph accuracy, and this is increasingly read as evidence that they use the image. That inference is unsafe: a model exploiting finding-name priors scores like one that reads the scan, and no standard benchmark separates them. We introduce a causal audit that intervenes on the image, occluding the relevant region, occluding an irrelevant one, and swapping in another patient's same-label scan, and combines three behavioral metrics to test whether a correct answer depends on the image. Across nine systems, a text-only model with no image access reaches within 5.7 accuracy points of the best multimodal one, and a 119-billion-parameter multimodal model is statistically indistinguishable from a 7-billion text-only baseline. The audit splits the cohort into three models that ignore the image, one that is unstable, and five that use it selectively, for a subset of findings; the categories hold across a second dataset, resolution, and prompt phrasing. Against board-certified radiologists, a text-only model is statistically indistinguishable from a radiologist's accuracy while grounding at zero, whereas the image-using models ground at radiologist-comparable rates. Reported confidence flags ungrounded answers only when a model uses the image. Grounding audits, not accuracy, should gate clinical deployment.

---


### 72. [ActWorld: From Explorable to Interactive World Model via Action-Aware Memory](https://arxiv.org/abs/2606.17730)

**<font color=#1a73e8>作者：</font>** Zhexiao Xiong, Yizhi Song, Hao Kang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive world models aim to simulate environment dynamics under real-time user actions. However, their action vocabulary is largely confined to navigation: most actions correspond to motion (e.g., walk, turn, look around), while interaction with objects in the scene (e.g., pick up plates, open doors, or trigger physical responses) is either absent, restricted to game domains, or relegated to prompt-to-full-video scenarios. The resulting worlds are visually explorable but not truly actionable. In this work, we present ActWorld, an interactive world model that extends prior navigation-centric generators to support mid-rollout object interaction within a chunk-autoregressive framework. We argue that the navigation-interaction gap stems from two bottlenecks. First, a data bottleneck: the lack of human-object interaction data with accurate, dense labels. Second, a memory bottleneck: recency-biased history compression in existing world models discards the event-transition frames that causally determine subsequent object states, leading to an action-forgetting pathology. On the data side, we construct a 100K interaction video dataset, each annotated with per-chunk captions via chain-of-thought reasoning. On the model side, we introduce a hierarchical action-aware memory design that routes history compression by interaction importance, complemented by a persistent memory bank that maintains event-update and object-identity tokens across long rollouts. Experiments show that ActWorld supports both flexible navigation and rich object interaction within a single model, substantially improving interaction fidelity over navigation-only baselines without sacrificing viewpoint control. Project page is available at this https URL.

---


### 73. [Shattering the Autoregressive Curse: Dynamic Epistemic Entropy Orchestrated Erasable Reinforcement Learning for LLMs](https://arxiv.org/abs/2606.17735)

**<font color=#1a73e8>作者：</font>** Ziliang Wang, Kang An, Faqiang Qian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although reinforcement learning (RL) has expanded the cognitive boundaries of large language models (LLMs), it often remains vulnerable to the autoregressive curse in long-horizon logical reasoning: small epistemic perturbations introduced early in generation can propagate irreversibly along the Markov decision process flow, triggering cascading failures that drive the reasoning trajectory toward collapse. To overcome this autoregressive cascade, in which a single early mistake can compromise all subsequent reasoning steps, we propose dynamic epistemic entropy orchestrated erasable reinforcement learning ($\text{E}^3\text{RL}$). $\text{E}^3\text{RL}$ eliminates reliance on external signals by grounding the model's endogenous local autoregressive cross-entropy as an intrinsic coordinate of epistemic uncertainty. By introducing segment-level adaptive dynamic thresholds and advantage allocation, $\text{E}^3\text{RL}$ enables the model to precisely excise localized logical defects while reusing historical key-value (KV) cache streams, thereby endowing the reasoning process with a self-healing capability. We train $\text{E}^3\text{RL}$ on the DeepMath-103k dataset. Experimental results show that $\text{E}^3\text{RL}$ reshapes the exploration efficiency of long-sequence reasoning and improves sample efficiency while maintaining linear memory overhead. On mathematical reasoning benchmarks such as AIME, $\text{E}^3\text{RL}$ achieves substantial performance gains, with the 4B and 8B parameter models surpassing previous state-of-the-art (SOTA) results by 5.349\% and 6.514\%, respectively. These findings suggest that $\text{E}^3\text{RL}$ shatters the autoregressive curse in long-sequence reasoning and establishes a theoretical and systems-level foundation for the next generation of self-healing artificial general intelligence (AGI).

---


### 74. [Mind Companion: An Embodied Conversational Agent for Process-Based Psychotherapy](https://arxiv.org/abs/2606.17789)

**<font color=#1a73e8>作者：</font>** Sofie Kamber, Lukas Diebold, Pascal Riachi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Access to evidence-based psychotherapy remains limited worldwide, with long waitlists even in high-income regions. Recent advances in large language models (LLMs) offer potential for scalable mental health support when designed with clinical oversight and safety mechanisms. We present Mind Companion, an LLM-based embodied conversational agent integrating multi-layered psychological analysis with process-based therapy principles. The system performs real-time analysis of client statements across fact extraction, psychological flexibility process detection, emotion recognition, and safety monitoring. Analysis results are stored for supervising clinicians to inform therapeutic planning. Response generation incorporates retrieval-augmented generation from evidence-based therapeutic literature and context-aware prompting. Responses are delivered through an embodied avatar with synchronized speech synthesis and animation. We evaluated three LLM configurations (GPT-4.1-mini, GPT-5.2, Claude Sonnet 4.5) against therapist responses from real therapy sessions using automated LLM-judge assessment and expert evaluation with 11 professional psychotherapists. GPT-5.2 achieved higher ratings than human therapist responses across understanding, interpersonal effectiveness, collaboration, and therapeutic alignment in both evaluations, demonstrating the feasibility of LLM-based conversational agents as tools to complement clinical care.

---


### 75. [The Slop Paradox: How Synthetic Standardization Erodes Clinical Uncertainty and Cross-Modal Alignment in AI-Rewritten Radiology Reports](https://arxiv.org/abs/2606.17791)

**<font color=#1a73e8>作者：</font>** Samar Ansari  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI-assisted clinical documentation tools increasingly summarize, standardize, and reformat radiology reports using large language models (LLMs). We present a controlled measurement of the resulting information degradation. Using 450 chest X-ray reports from the Indiana University dataset, we generate synthetic versions via three realistic LLM rewriting tasks: EHR summarization, standardized rewriting, and teaching case preparation. We measure entity erosion (via medical NER), hedging collapse (loss of clinical uncertainty language), and cross-modal alignment degradation (via BiomedCLIP image-text similarity). Our central finding is a dissociation between information loss and cross-modal fidelity. EHR summarization is the most destructive at the content level, eroding 51.4% of clinical entities and 43.7% of hedging language, yet it preserves image-text alignment almost entirely (a 2.5% drop). The two tasks meant to produce cleaner training data, standardized rewriting and teaching case preparation, do the reverse: they preserve more entities (26.8% and 29.3% eroded) but cause 14.9-16.5% alignment drops, six to seven times those of EHR summarization. We term this the slop paradox: rewriting that makes clinical text look cleaner for multimodal training is precisely what pulls it away from the image. Contrary to our pre-specified hypothesis, rare pathologies were not preferentially degraded: across nine rare-versus-common comparisons, no difference survived multiple-comparison correction, and nominal differences ran in the opposite direction (common > rare), so contamination is invisible to condition-specific monitoring. The dominant determinant of degradation is the type of AI rewriting task, not the clinical content. These findings bear on multimodal medical AI dataset construction and the governance of AI-assisted clinical documentation.

---


### 76. [ARES: A Platform for Adaptive Role-Based Evaluation of Social Engineering Risks in Human--AI Games](https://arxiv.org/abs/2606.17793)

**<font color=#1a73e8>作者：</font>** Roberto Daza, Javier Irigoyen, Ivan Lopez 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This work introduces ARES, a platform and open pilot dataset for auditing adaptive social engineering risks in LLM-mediated social decision-making through controlled social games. ARES supports human--human, human--AI, and AI--AI settings, combining configurable game templates, role-conditioned LLM agents, psychology-informed participant profiling, structured interaction trees, and synchronised behavioural and biometric acquisition, filtering, and deep-learning-based feature extraction. The pilot dataset was collected from 15 participants interacting with a role-conditioned GPT-5.4 agent in two concatenated games: an adapted Prisoner's Dilemma and an Ultimatum Game. It comprises 340 GB of raw and processed multimodal data across six streams: interaction logs, video, screen recordings, gaze logs, smartwatch signals, and game/questionnaire metadata. These data include interaction paths, written justifications, psychological profiles, subjective feedback, perceived counterpart identity, game outcomes, and derived behavioural, facial, and gaze features. Alongside the dataset, we provide descriptive analyses to characterise the pilot release. Rigorous risk evaluation is essential for the deployment of secure AI systems, as it enables the identification and mitigation of vulnerabilities, ensures the protection of sensitive data, and supports compliance with evolving regulatory and ethical standards in society.

---


### 77. [LiveStarPro: Proactive Streaming Video Understanding with Hierarchical Memory for Long-Horizon Streams](https://arxiv.org/abs/2606.17798)

**<font color=#1a73e8>作者：</font>** Zhenyu Yang, Kairui Zhang, Bing Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the remarkable progress of Video Large Language Models (Video-LLMs), current online architectures still struggle to simultaneously process continuous video streams, decide autonomously when to respond, and preserve long-horizon contextual memory. These obstacles undermine real-time responsiveness and cause severe forgetting throughout prolonged interactions. In this work, we introduce LiveStarPro, a live streaming assistant that is designed for proactive video understanding over long-horizon streams. The design of LiveStarPro rests on three complementary components. The first component is Streaming Verification Decoding (SVeD), an inference framework that identifies the appropriate response timing through single-pass perplexity verification, thereby eliminating the dependency on explicit silence tokens. The second component is Streaming Causal Attention Masks (SCAM), a training strategy that enforces incremental video-language alignment over variable-length streams. The third component is Tree-Structured Hierarchical Memory (TSHM), a recursive memory architecture that organizes evicted historical information into event chains and consequently enables efficient retrieval from effectively unbounded video streams. To facilitate a comprehensive evaluation under realistic online conditions, we further present OmniStarPro, a large-scale benchmark that spans 15 diverse real-world scenarios and that extends to hour-scale streams for the assessment of long-term recall. Extensive experiments demonstrate that LiveStarPro consistently surpasses existing methods, attaining a 28.9% improvement in semantic correctness and an 18.2% reduction in timing error, while its streaming key-value cache further yields a 1.58x inference speedup over the same model without caching. The model and the code are publicly available at this https URL.

---


### 78. [MaineCoon: Pursuing A Real-Time Audio-Visual Social World Model](https://arxiv.org/abs/2606.17800)

**<font color=#1a73e8>作者：</font>** Lichen Bai, Tianhao Zhang, Shitong Shao 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As an increasing majority of global video content is consumed on social platforms for interactive social purposes, video generation models built for social worlds are important but largely overlooked by previous studies. In this work, we define the position of social world models and build a prototype model as the first step towards this goal. While previous world models successfully simulate physical environments or gaming world exploration, they remain fundamentally detached from human-centric social dynamics. To bridge this gap as the first step to social world models, we present MaineCoon, the first real-time audio-visual autoregressive model that has 22B parameters and is capable of real-time streaming generation and sub-second interaction, with a record-breaking frame rate of up to 47.5 FPS, on a single GPU. To the best of our knowledge, MaineCoon is also the first real-time audio-visual generation model specifically optimized for social-interactive applications. To enable efficient and stable training, we introduce several novel techniques into MaineCoon, including self-resampling, cross-modal representation alignment, domain-aware preference optimization, and reinforced online-policy distillation (ROPD). We also design the first agentic streaming inference framework that supports thousand-second-scale or even longer generation while mitigating drift with agentic cache management and prompt planing. These innovations significantly accelerate training while optimizing real-time inference performance. We believe this work not only sets a new state-of-the-art (SOTA) performance benchmark for high-quality, low-latency, and long-horizon audio-visual autoregressive models, but also points out the paradigm shift desired for next-generation AI-native social platforms.

---


### 79. [Million-scale multimodal pollen microscopy with expert-guided foundation models](https://arxiv.org/abs/2606.17809)

**<font color=#1a73e8>作者：</font>** András Biricz, Björn Gedda, Donát Magyar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated pollen identification from microscopy remains a bottleneck in aerobiology, palaeoecology and biodiversity monitoring, because scalable systems must generalise across specimen preparation, scanner settings and geographic origins while retaining palynological interpretability. To address this gap, we present a million-scale multimodal pollen microscopy resource, Pollen AI Atlas, assembled from pure-species whole-slide bright-field images spanning four geographic origins, four scanner settings and 46 taxon labels across 31 botanical families. Seeded by one manually selected exemplar per source slide, token-level mining and filtering produced 1,511,390 released grain detections with 99.6\% proposal precision in expert-curated test regions. Each detection was paired with machine-generated grain-level morphological captions from five open-weight vision-language models, guided by expert-verified palynological anchors, yielding structured descriptions of aperture systems, wall ornamentation, shape and size. Among the evaluated models, Gemma4 provided the most controlled primary caption set, combining tight length control, no leakage and the strongest text-retrieval performance. Baseline benchmarks with frozen visual features reached 88.16\% top-1 accuracy, while cross-regional retrieval showed that caption-derived text embeddings remained robust when image similarity degraded (mAP@20 0.811 versus 0.262). Released data, annotations, captions, splits, code, and weights provide a benchmark for pollen recognition, cross-regional domain adaptation and domain-specific multimodal microscopy learning.

---


### 80. [Improving low-resource ASR using bilingual fine-tuning with language identification: a cross-linguistic evaluation](https://arxiv.org/abs/2606.17820)

**<font color=#1a73e8>作者：</font>** Reihaneh Amooie, Yun Hao, Wietse de Vries 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study explores how bilingual fine-tuning affects automatic speech recognition (ASR) in low-resource languages. We evaluate this method across nine linguistically and geographically diverse language pairs, covering a range of language families and writing systems. To distinguish the two languages, during training, we pre-pend each input text with a language identification token. At inference, the model jointly predicts both the language and transcription from the speech input alone. As texts for which the language is incorrectly determined show low ASR performance, we also conduct a follow-up experiment in which the language identification token is provided both during training and inference. Our results show that bilingual fine-tuning can be beneficial when language identification accuracy is high, and that in cases where language identification performance is low, including the language identification token at inference helps to improve ASR performance.

---


### 81. [DecoSearch: Complexity-Aware Routing and Plan-Level Repair for Text-to-SQL](https://arxiv.org/abs/2606.17821)

**<font color=#1a73e8>作者：</font>** Esteban Schafir, Xu Zheng, Hojat Allah Salehi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable capabilities in translating natural language to SQL, yet existing methods still falter on complex queries requiring multi-step, data-aware reasoning. We introduce DecoSearch, a training-free framework that addresses this by routing each query to the appropriate level of reasoning effort. A lightweight Schema Selector first prunes the full database schema to the relevant tables and columns. An LLM Judger then decides whether the question requires decomposition: straightforward questions follow a direct generation path and complex ones are escalated to a Directed Acyclic Graph (DAG) of atomic sub-questions, each solved by a targeted SQL generation step. A RAG component grounds the decomposer with semantically similar training examples, and a Topology Refiner restructures the reasoning plan when execution failures signal a flawed decomposition rather than a fixable SQL error. DecoSearch achieves 70.53% execution accuracy on BIRD and 88.31% on Spider with a DeepSeek backbone, surpassing all training-free baselines while consuming an order of magnitude fewer tokens than competing methods. It also functions as a model-agnostic wrapper, consistently improving fine-tuned SQL generation backbones without any modification to the pipeline.

---


### 82. [From Drift to Coherence: Stabilizing Beliefs in LLMs](https://arxiv.org/abs/2606.17832)

**<font color=#1a73e8>作者：</font>** SongEun Kim, Seungyoo Lee, Edwin Fong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are often hypothesized to perform implicit Bayesian inference, yet a key coherence condition, the martingale property of predictive beliefs, has been shown to fail in controlled synthetic in-context learning settings. We revisit this question in a more typical usage regime: generic multiple-choice question answering. Exploiting the discrete answer space, we compute exact predictive distributions and study belief dynamics induced by autoregressive answer resampling. We introduce prompted predictive resampling (PPR), where an LLM generates a sequence of answers to the same question. Empirically, PPR reveals early-stage belief drift, indicating martingale violations. However, after sufficient resampling steps, the belief process self-stabilizes and converges to a coherent predictive distribution. Based on this observation, we further propose (i) a seed-answer prompting strategy to accelerate stabilization, and (ii) a self-consistency loss that amortizes early-stage drift into the model via fine-tuning. Experiments on multiple-choice QA benchmarks show that our methods substantially reduce belief drift and improve predictive coherence without sacrificing accuracy.

---


### 83. [Environment-Grounded Automated Prompt Optimization for LLM Game Agents](https://arxiv.org/abs/2606.17838)

**<font color=#1a73e8>作者：</font>** Rean Clive Fernandes, Lukas Fehring, Theresa Eimer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents in interactive environments are highly sensitive to their prompts, yet prompt engineering remains a manual, task-specific process. We introduce an automated prompt optimization framework for LLM agents that decomposes the observation-to-action pipeline into a goal-conditioned descriptor agent and an action selection agent, and iteratively refines each module's prompt through an LLM-driven evolutionary loop guided by environment returns. We propose a behavior analyzer to attribute episode outcomes to specific prompt components, and a mutator to propose targeted revisions to the prompt, before validating them through environment rollouts. We evaluate on all five BabyAI tasks in the BALROG benchmark, comparing our pipeline against BALROG's RobustCoTAgent under both plain and guided prompt initializations. Optimization improves performance consistently across tasks and conditions, without requiring updates to the model weights. On PutNext, a multi-step coordination task where the RobustCoTAgent achieves 0% success, our framework reaches up to 72.5% success rate using the same underlying LLM with optimized prompts. These results suggest that a multi-agent framework, combined with automatic prompt optimization, enhances LLMs without the need for fine-tuning or extensive human supervision.

---


### 84. [FlowRAG: Synergizing Explicit Reasoning via Frequency-Aware Multi-Granularity Graph Flow](https://arxiv.org/abs/2606.17856)

**<font color=#1a73e8>作者：</font>** Bihao Zhan, Zongsheng Cao, Jie Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph-based retrieval-augmented generation (GraphRAG) is effective for knowledge-intensive and multi-hop query tasks; however, many existing methods primarily seed entity-based graphs and rely on implicit semantic relevance propagation. This often (i) under-retrieves when user queries are abstract and semantically sparse at the entity level, and (ii) suffers from brittle multi-hop reasoning, where noisy activations can derail entity-to-entity transitions and corrupt the inferred relation chain, yielding unreliable conclusions. To this end, we propose \texttt{FlowRAG}, a semantic-aware retrieval framework that improves both semantic recall and explicit reasoning. Specifically, \texttt{FlowRAG} constructs a quad-level heterogeneous graph over passages, summaries, sentences, and entities, where summary nodes serve as a coarse semantic hub. At retrieval time, a dual-granularity activation module combines summary--query alignment with sentence-level matching to activate relevant entities under paraphrase and abstraction robustly. We then introduce a frequency-aware weighted flow module that routes relevance through entity--passage links weighted by within-passage term frequency, pruning noisy connections and extracting high-confidence reasoning paths as an explicit logic skeleton for generation. Extensive experiments show that \texttt{FlowRAG} obtains state-of-the-art performance on complex reasoning benchmarks.

---


### 85. [A Quantitative Analysis of Multimodal Biomarkers in Alzheimer's Disease](https://arxiv.org/abs/2606.17867)

**<font color=#1a73e8>作者：</font>** Antonio Scardace, Daniele Ravì  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite increasing adoption of multimodal approaches in Alzheimer's Disease (AD) research -- aimed at integrating molecular, structural, clinical, and genetic biomarkers to enhance disease characterization -- the relationships among these modalities remain poorly understood. A systematic analysis of their dynamic interaction is essential for improving disease modeling, identifying redundant assessments, and reducing patient burden and acquisition costs. In this paper, we present a quantitative analysis of multimodal AD biomarkers by integrating tau-PET, structural MRI, cognitive scores (MMSE and CDR), and APOE4 data from 789 subjects drawn from the ADNI dataset. In our analyses, we (A) quantify cross-modal mutual information and explained variance to assess redundancy and predictive dependencies; (B) examine associations between tau topologies and structural atrophy across brain regions to select informative ROIs; (C) perform a statistical decomposition of the tau-cognition association into atrophy-related and atrophy-independent components; (D) and identify a dominant neurodegenerative trajectory that aligns with cognitive decline. This study provides a systematic characterization of cross-modal relationships, improving the interpretability and selection of biomarkers in AD. Code is publicly available at: this https URL.

---


### 86. [StepGuard: Guarding Web Navigation via Single-Step Calibration](https://arxiv.org/abs/2606.17871)

**<font color=#1a73e8>作者：</font>** Zhihao Cui, Yuchen Zhang, Xiyang Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web navigation requires agents to follow natural language goals, interact with web pages, and produce accurate answers. While recent advances leverage vision-language models and reinforcement learning, existing methods still suffer from single-step fragility due to reward misalignment and error propagation. To tackle the reward entanglement, we design Dynamic Dual-Policy Optimization (DDPO), which dynamically switches between a navigation-first mode for exploration and an answer-first mode for question-answering to mitigate reward conflict. To calibrate the single-step error, we propose Confidence-Guided Adaptive Navigation Reflection (CANR), a mechanism that estimates per-step confidence, triggers reflection only when necessary, and uses contrastive rewards to encourage self-correction to calibrate the single-step inaccuracy. With the above as the main components, we finally develop our StepGuard, a new framework of Guarding Web Navigation via Single-Step Calibration. Experiments demonstrate that our approach significantly improves navigation and answer accuracy, setting new state-of-the-art performance on standard web navigation benchmarks.

---


### 87. [AnchorKV: Safety-Aware KV Cache Compression via Soft Penalty with a Refusal Anchor](https://arxiv.org/abs/2606.17872)

**<font color=#1a73e8>作者：</font>** Ning Ni, Yingjie Lao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) outperform earlier architectures on generative inference and long-context tasks, but their large size introduces significant challenges in memory usage, energy cost, and on-device deployment. Since scaling pre-trained language models improves downstream capability \cite{zhao2023survey}, the key-value (KV) cache becomes a dominant inference bottleneck. Recent KV cache compression methods \cite{jo2025fastkv,li2024snapkv,zhou2024dynamickv} reduce this cost by retaining only a subset of attention-relevant tokens. However, while these approaches preserve accuracy on benign workloads, their compression policies either fail to defend against jailbreak attacks \cite{jiang2024robustkv} or degrade safety alignment under aggressive eviction.
We propose AnchorKV, a drop-in modification to KV cache compression that biases token retention scores away from directions in key space associated with harmful prompts. AnchorKV constructs an offline safety anchor by adapting a difference-of-means representation engineering approach \cite{arditi2024refusal,zou2023representation} to the layer-specific key projection space used in KV caching. Based on this anchor, a soft penalty token selection rule trades a small amount of utility for substantially improved safety alignment, while reducing to the original compressor when the penalty is zero.

---


### 88. [MathVis-Fine: Aligning Visual Supervision with Necessity via Progressive Dependency-Guided Training for Multimodal Mathematical Reasoning](https://arxiv.org/abs/2606.17888)

**<font color=#1a73e8>作者：</font>** Wanshi Xu, Haokun Zhao, Haidong Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) reasoning has extended from purely linguistic domains to multimodal scenarios; however, existing approaches often treat visual inputs as homogeneous or auxiliary signals, failing to capture the intricate and sample-specific dependencies between text and images in mathematical problem-solving. This gives rise to two core issues: first, the supervisory signals for visual content are generalized and coarse-grained, lacking adaptation to the actual necessity of visual information in each sample; second, training feedback becomes inaccurate when visual rewards are uniformly applied without distinguishing the complementary relationships among inputs. These limitations hinder models from achieving precise multimodal reasoning. In this work, we propose a framework for modeling fine-grained visual dependencies in mathematical reasoning. We first construct the MathVis-Fine dataset, augmenting fine-grained visual annotations with visual dependency ratings. Building upon this dataset, we introduce a two-stage progressive visual enhancement training paradigm that balances answer correctness rewards and visual grounding rewards according to the intrinsic visual dependency level of each sample, thereby mitigating reward bias and improving supervision accuracy. Extensive experiments demonstrate that the MathVis-Fine framework effectively enhances visual perception progressively based on visual dependency, offering a more precise training framework for multimodal mathematical reasoning. We will release the dataset upon acceptance.

---


### 89. [Dynamic Rollout Editing for Reducing Overthinking in RL-Trained Reasoning Models](https://arxiv.org/abs/2606.17890)

**<font color=#1a73e8>作者：</font>** Zihao Wei, Wenjie Shi, Liang Pang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-form chain-of-thought reasoning can improve LLM performance on complex tasks, but models often continue generating unnecessary reasoning after a correct answer has emerged. We refer to this behavior as overthinking. We study this phenomenon from the perspective of GRPO-style reinforcement learning (RL) post-training, framing it as a training-time credit-assignment problem rather than merely a decoding-time stopping problem. In rollouts sampled at the onset of GRPO training, we observe that successful trajectories can exhibit a slightly higher degree of overthinking than unsuccessful trajectories for the same prompts. This early imbalance provides a starting point for an undesirable feedback loop: because GRPO assigns sequence-level credit, it cannot distinguish the solution-reaching prefix from the unnecessary continuation that lengthens a successful trajectory. Both receive positive update signal, allowing the initial imbalance to grow into more severe overthinking during training. To address this issue, we introduce Dynamic Rollout Editing (DRE), a training-time intervention for successful trajectories that continue thinking after answer emergence. DRE preserves the accepted verified prefix, edits the remaining thinking, and prefers the edited trajectory within the same RL group, weakening the preference signal for unnecessary thinking without penalizing the reasoning needed to reach the answer. Experiments across diverse tasks show the effectiveness of DRE.

---


### 90. [DiagFlowBench: Evaluating How Language Models Handle Off-Procedure Inputs in Grounded Diagnostic Dialogue](https://arxiv.org/abs/2606.17904)

**<font color=#1a73e8>作者：</font>** Guillermo Gil de Avalle, Laura Maruster, Shaina Raza 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models increasingly serve as advisory systems in maintenance operations. To prevent hallucination, recent systems ground these models in procedural documentation to constrain them to approved steps. In practice, however, operator queries frequently stray from this path, requiring models to recognise out-of-scope inputs mid-conversation, a dynamic that current benchmarks rarely prioritise. We introduce DiagFlowBench, a dataset of 50 industrial diagnostic flowcharts from a consumer manufacturer converted into 1,676 multi-turn conversations that contrast compliant with out-of-scope utterances. Evaluating a panel of ten commercial and open-weight models reveals high variability in abstention rates, with models commonly selecting a real but contextually inadequate step rather than fabricating facts. The inherent plausibility and authority of this mapped but wrong advice exposes a challenging vulnerability for grounding systems.

---


### 91. [Trustworthy Self-Composable Big-Data-as-a-Service: An LLM-Orchestrated Multi-Agent Framework for Automated Data Engineering, AutoML, MLOps Deployment, and Drift-Aware Lifecycle Optimization](https://arxiv.org/abs/2606.17915)

**<font color=#1a73e8>作者：</font>** Aueaphum Aueawatthanaphisut, Badri Raj Lamichhane  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Big-Data-as-a-Service (BDaaS) platforms require re liable automation across data ingestion, cleaning, feature engi neering, model development, deployment, and post-deployment monitoring. However, existing LLM-based data science agents and AutoML systems mainly focus on isolated workflow stages, leaving limited support for lifecycle-level orchestration, artifact governance, human oversight, and drift-aware adaptation. This paper proposes a trustworthy self-composable BDaaS frame work based on LLM-orchestrated multi-agent collaboration. The proposed architecture decomposes the BDaaS lifecycle into specialized agents for data ingestion, data cleaning, feature engineering, AutoML training, model evaluation, MLOps de ployment, monitoring, and drift detection. A central LLM or chestration layer coordinates agent execution, validates interme diate outputs, manages workflow context, and enables dynamic workflow composition. The framework also incorporates shared artifact governance, reproducibility support, human-in-the-loop checkpoints, and drift-aware feedback loops. A prototype-based evaluation is conducted using controlled tabular benchmark datasets with missing values, categorical variables, outliers, class imbalance, and simulated covariate drift. Compared with manual ML, AutoML-only, and single-agent LLM baselines, the pro posed multi-agent BDaaS pipeline achieves competitive predictive performance while improving lifecycle-level reliability, including workflow completion, artifact traceability, deployment readiness, reproducibility, and drift recovery. The results suggest that LLM-orchestrated multi-agent systems can extend conventional AutoML toward trustworthy, adaptive, and production-oriented BDaaS lifecycle automation.

---


### 92. [How Inference Compute Shapes Frontier LLM Evaluation](https://arxiv.org/abs/2606.17930)

**<font color=#1a73e8>作者：</font>** Jessica McFadyen, Ole Jorgensen, Harry Coppock 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI evaluations are shifting toward harder tasks that benefit from longer trajectories involving tool use and iterative problem solving. As a result, performance is increasingly sensitive to the amount and allocation of compute available at test time ("inference compute"). Yet many evaluations still report performance at a single restrictive budget, meaning that low scores may reflect the evaluation setup rather than the model's underlying capability. To test this, we evaluate up to 12 frontier language models on seven challenging benchmarks spanning software engineering, mathematics, medicine, and cybersecurity. We use a controlled setup combining three simple inference-scaling interventions: larger token budgets, context compaction, and repeated submission attempts, guided either by the model itself or by minimal correctness feedback. We find three main results. First, larger token budgets substantially improve performance on benchmarks across multiple domains, including cybersecurity, FrontierMath, Humanity's Last Exam, and TerminalBench. Second, fixed-budget evaluations can increasingly understate frontier capability as models advance. Newer models reach higher performance at large budgets, where they unlock harder tasks and solve them more reliably. Third, benchmarks differ in which inference-scaling methods help most: repeated submission broadly improves performance, but the value of larger token budgets, external feedback, and parallel attempts varies by benchmark. Overall, our results show that benchmark scores are protocol-dependent. We therefore argue that evaluations should report capability as a function of inference-time compute, specify protocol choices explicitly, and compare model generations over a large shared compute range at matched budgets, especially in safety- or policy-relevant settings.

---


### 93. [Small Initialization Matters for Large Language Models](https://arxiv.org/abs/2606.17945)

**<font color=#1a73e8>作者：</font>** Liangkai Hang, Junjie Yao, Zhiyu Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models provide a tractable system for asking how intelligence itself emerges, rather than only how LLMs can be engineered. Although progress is usually attributed to scale, data and architecture, we show that parameter initialization is a gene-like determinant of training and, in particular, of model capacity. Reducing the initialization scale consistently improves pretraining, with the largest gains on reasoning-demanding tasks. We identify two widely used empirical settings that restrain the advantage of small initialization, and show how relaxing them restores favorable scaling. We further uncover a critical initialization that balances the reasoning and training. Mechanistically, small initialization drives a distinct developmental trajectory: parameters first condense into low-complexity structures and later expand into richer representations, giving concrete form to the idea that compression is intelligence. Token-level analyses show that the gains concentrate on non-trivial, context-constrained predictions rather than all tokens uniformly. These results motivate a simple $\gamma$-initialization rule: expose initialization rage as an explicit knob and use small initialization by default, an almost cost-free intervention that improves pretraining and strengthens reasoning across model scales.

---


### 94. [Plug-and-Adapt: Multimodal Coreference Resolution at First Sight with a Pretrained Alignment Model](https://arxiv.org/abs/2606.17950)

**<font color=#1a73e8>作者：</font>** Jinghan Wu, Jing Li, Ivor W. Tsang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual information helps resolve ambiguity in coreference resolution, leading to notable performance gains. However, existing Multi-modal Coreference Resolution (MCR) methods require training with (partially) annotated data from the target dataset before they can be applied, preventing their direct usability and raising concerns about generalization. While Vision-Language Large Models (VLLMs) with billions of parameters offer promising zero-shot capabilities, they remain largely inaccessible. Their massive size limits deployability, and many are only accessible through paid APIs. In this paper, we propose a plug-and-adapt method that strategically adapts a carefully pre-trained \emph{alignment model} for immediate use in MCR tasks, designed to eliminate the need for training on scarce benchmark datasets or relying on resource-intensive VLLMs. Specifically, we first pre-train a fine-grained alignment model between textual and visual contextual information using vision-language alignment datasets. We then repurpose the alignment model to MCR through similarity aggregation by fusing visual and categorical cues with evidence theory, thereby enhancing effectiveness. Experiments on the Coreference Image Narratives (CIN) benchmark dataset demonstrate the effectiveness of our method, achieving a 5.31\% and 2.12\% improvement in CoNLL F1 over SOTA dedicated methods and popular VLLMs, respectively. We further evaluate our method on a masked CIN dataset for robustness testing and on a specially constructed VCR-MCR dataset for generalization assessment, with results confirming both capabilities.

---


### 95. [SoftMoE: Soft Differentiable Routing for Mixture-of-Experts in LLMs](https://arxiv.org/abs/2606.17952)

**<font color=#1a73e8>作者：</font>** Mikołaj Zasada, Łukasz Struski, Jacek Tabor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts (MoE) architectures enable scaling LLM parameters under a fixed inference budget by activating only a small subset of experts via top-$k$ routing. While this preserves causality and suits autoregressive language models, the discrete top-$k$ operator is not differentiable, forcing a fixed number of active experts per input and resulting in inefficient use of computation. We propose SoftMoE, which replaces discrete routing with a truncated soft top-$k$ LapSum relaxation, allowing gradient-based optimization of expert routing. We further parameterize the mean number of active experts per layer and impose a global budget constraint, enabling the model to learn how to allocate expert capacity across layers. SoftMoE remains fully compatible with autoregressive modeling and achieves performance comparable to or better than sparse MoE on language modeling and downstream tasks, while activating significantly fewer experts. Notably, the learned allocation is highly non-uniform, with later layers activating more experts. The source code is publicly available$^\dagger$.

---


### 96. [MLLMs Get It Right, Then Get It Wrong: Tracing and Correcting Late-Layer Textual Bias](https://arxiv.org/abs/2606.17953)

**<font color=#1a73e8>作者：</font>** Xingming Li, Ao Cheng, Qiyao Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When vision contradicts text, multimodal large language models (MLLMs) consistently favor text, even when images provide clear evidence otherwise. This bias poses risks for applications requiring visual grounding, yet its cause remains unclear. In this paper, we uncover a surprising finding: models often get it right initially, forming correct vision-based predictions in their intermediate layers, before changing their minds and favoring text in the final output. We call this "late-layer textual override". The visual information is encoded, it simply does not survive to the output. More intriguingly, we find that how predictions change reveals whether they're correct: 85% of failures shift toward text, while 89% of successes shift toward vision. This directional signature enables a simple but powerful intervention: when we detect a confident visual prediction being suppressed, we restore it. We propose CALRD (Conflict-Aware Layer Reference Decoding), a training-free method that recovers overridden predictions at inference time. Experiments across five MLLMs of varying architectures demonstrate up to 9.4% absolute improvements on conflict benchmarks while largely preserving standard performance, without training or external knowledge. It recovers what the model already knew but failed to preserve.

---


### 97. [Beyond Visual Cues: CoT-Enhanced Reasoning for Semi-supervised Medical Image Segmentation](https://arxiv.org/abs/2606.17958)

**<font color=#1a73e8>作者：</font>** Yuming Chen, Yuxin Xie, Tao Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semi-supervised medical image segmentation has emerged as a dominant research problem in medical image analysis, mitigating annotation scarcity by leveraging consistency regularization on unlabeled data. However, existing approaches operate predominantly via visual pattern matching, relying heavily on pixel-level similarities. This visual-centric dependency often falters in clinical scenarios characterized by the visual-semantic mismatch, where visually similar lesions warrant distinct diagnostic conclusions, thus failing to capture the underlying diagnostic logic used by experts. To address this, we move beyond visual cues and propose CERS (CoT-Enhanced Reasoning Segmentation), a framework that integrates Chain-of-Thought (CoT) reasoning to distinguish pathologically distinct cases. Specifically, we construct a knowledge pool enriched with linguistic reasoning descriptions generated by large language models (LLMs). A semantic-aware reference selection strategy is introduced to identify historical evidence, filtering candidates first by morphology, and then refining them via CoT consistency to eliminate hard negatives. Furthermore, a multi-scale coordinate attention module (MCAM) is designed to effectively fuse this reasoning-derived context into the decoding process. Extensive experiments demonstrate the superiority of CERS against state-of-the-art approaches, particularly in resolving boundary ambiguities and semantic inconsistencies. The code is available at this https URL.

---


### 98. [A Neuro-Symbolic Approach to Strategy Synthesis for Strategic Logics](https://arxiv.org/abs/2606.17962)

**<font color=#1a73e8>作者：</font>** Marco Aruta, Vadim Malvone, Aniello Murano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Reasoning about what agents can achieve through strategic interaction is a core challenge in Multi-Agent Systems (MAS). Logics for strategic ability, such as ATL, provide rigorous methods, but their adoption is often hindered by the computational cost of strategy synthesis. We introduce a neuro-symbolic framework that integrates large language models (LLMs) into the model-checking pipeline for MAS. The LLM acts as a strategy-generation oracle, proposing candidate strategies that are then formally validated by a standard MAS model checker. This generate-and-certify architecture uses LLM guidance to navigate large combinatorial strategy spaces while preserving formal soundness: generated strategies are accepted only when certified by the verifier. We instantiate the framework for bounded strategic reasoning in NatATL and introduce the first NatATL strategy-synthesis dataset, consisting of 4211 instances. Experiments with an open-weight Qwen3-32B model show that our certified pipeline achieves 92\% accuracy on strategy-synthesis outcomes.

---


### 99. [Learning task-specific subspaces via interventional post-training of speech foundation models](https://arxiv.org/abs/2606.17967)

**<font color=#1a73e8>作者：</font>** Jack Cox, Jon Barker  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech foundation models, pre-trained on large corpora of unlabelled speech data, produce general-purpose representations which are useful across tasks. However, these representations encode information about salient speech variables in a distributed manner, while downstream speech tasks rely on only some of this variability. In this work, we propose a post-training refinement approach using interventional contrastive learning. By leveraging an interventional dataset and multi-part contrastive loss, we learn a transformation from the entangled representation space of speech foundation models into separate content and speaker subspaces. We evaluate the learnt representations on speaker verification and keyword spotting tasks, showing improved out-of-domain speaker verification performance and evidence that speaker and content information are separated across the learned subspaces.

---


### 100. [Fine-tuning LLMs for Passive Depression Severity Estimation from AI Mental Health Dialogue](https://arxiv.org/abs/2606.17973)

**<font color=#1a73e8>作者：</font>** Olivier Tieleman, Ziyi Zhu, Ting Su 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Depression is the leading cause of disability worldwide, and early detection of symptom change is essential for timely intervention. Validated instruments such as the Patient Health Questionnaire-9 (PHQ-9) support symptom monitoring at scale, but real-world completion rates are low, introducing response bias and systematic missingness. Passive approaches that infer severity from routinely generated data could close this gap. We address this by predicting PHQ-9 total scores directly from transcripts of conversations between users and an AI mental health application, requiring only conversation text and no additional clinical data. We fine-tune a Qwen3.5-27B backbone with a regression head, augment 3,111 ground-truth labels with pseudolabels generated by a reasoning model (Claude Opus) and iteratively trained intermediate models, for a combined dataset of 6,283 users. On a held-out test set of 842 users, our best model achieves MAE = 2.6, RMSE = 4.0, Pearson r = 0.80, and AUC = 0.91 at the PHQ-9 >= 10 clinical threshold. We also find AUC > 0.87 at every severity threshold from PHQ-9 >= 3 to PHQ-9 >= 24, demonstrating that the model captures depression severity across the full clinical spectrum. This work opens the door to passive, continuous symptom monitoring in AI mental health platforms, without requiring users to complete self-report measures.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-133](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
