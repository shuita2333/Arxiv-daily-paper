# 🧠 大模型相关研究 | 2026年07月01日

> 本类共 **247** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-247](./part-05.md)

---

### 151. [GUICrafter: Weakly-Supervised GUI Agent Leveraging Massive Unannotated Screenshots](https://arxiv.org/abs/2606.29705)

**<font color=#1a73e8>作者：</font>** Sunqi Fan, Lingshan Chen, Runqi Yin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data, as the fundamental substrate of modern intelligence, has greatly driven the development of current foundation models. Naturally, researchers aim to extend this paradigm to the domain of GUI agents, hoping to build strong GUI agents through a similar paradigm. However, GUI agent data cannot be directly harvested from the internet, making it costly and difficult to collect at scale. As a result, current GUI agents suffer from poor cross-device generalization and limited visual grounding ability for fine-grained GUI elements. As an attempt to address data challenge in GUI agents, we propose GUICrafter, a weakly-supervised GUI agent leveraging massive unannotated screenshots to substantially reduce the reliance on expensive human annotations. GUICrafter explores a curriculum learning framework for training GUI agents through two progressive stages. First, the model learns visual grounding from large-scale unannotated screenshots and webpages, leveraging the rich contextual signals inherent in GUI interactions without human annotations. Then, in Stage 2, we leverage a small amount of high-quality data to calibrate the model via reinforcement learning. Experiments show that GUICrafter achieves competitive, or even superior, performance to advanced systems like UI-TARS while using only 0.1% of its data. Furthermore, under the same amount of annotated data, GUICrafter surpasses all previous methods such as GUI-R1. Code, data, and models are available at this https URL.

---


### 152. [Why Struggle with Continuous Latents? Interpretable Discrete Latent Reasoning via Rendered Compression](https://arxiv.org/abs/2606.29712)

**<font color=#1a73e8>作者：</font>** Shuochen Chang, Qingyang Liu, Shaobo Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models achieve high reasoning performance via explicit chain-of-thought and reinforcement learning, but require long output sequences and extended inference time. Latent reasoning reduces this cost by shifting computation into a latent space; however, continuous latent methods are hard to train, suffering from unstable and uninterpretable reasoning trajectories. We argue these issues stem from a misalignment between continuous-space reasoning and discrete symbolic supervision, as continuous states lack explicit anchors for step-by-step alignment. To resolve this, we propose \textbf{Discrete Latent Reasoning~(DLR)}, the first method that converts continuous latent states into explicit discrete tokens. Inspired by render-based compression, we render textual chains of thought into images, extract visual features, and construct a discrete latent vocabulary via clustering-based fine-tuning. Expanding the vocabulary and output head enables standard autoregressive modeling over both natural language and latent tokens, supporting pretraining alignment, SFT, and RL. Experiments on five reasoning benchmarks and two model series~(Qwen3-VL and LLaMA-3) confirm that \textbf{DLR} outperforms prior latent reasoning baselines with up to \textbf{20$\times$ compression}. Furthermore, the learned latent trajectories retain an interpretable semantic structure. Overall, discrete latent tokens provide a controllable and interpretable basis for efficient latent reasoning.

---


### 153. [A Diagnostic Framework and Multi-Evaluator Audit of Evaluator-Driven Preference Dynamics in Self-Adapting LLM Agents](https://arxiv.org/abs/2606.29719)

**<font color=#1a73e8>作者：</font>** Liu Zewen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Measurements of proprietary LLM evaluators can become invalid within weeks -- we document one case and provide the diagnostic framework to detect it. We introduce EPC -- comprising the Multimodal Preference Collapse Index (MPCI), evaluator-indexed coupling matrix, and Jensen-Shannon divergence (JSD) -- and apply it across eight experimental conditions (N=112 main + N=10 ablation = 122 unique repetitions, all reported). Coupling coefficients range from 0.00 to 1.18 across per-condition means (CV approx 0.9, n=8 conditions). Four conditions show strong coupling (N=36; GPT-4o May, GPT-4o-mini, Qwen3.7-plus, DashScope 30r); four collapse to near-zero (N=76; GPT-4o June, qwen-plus N=30, symmetric LR, DeepSeek self-eval). The May-to-June GPT-4o drift -- an N=8 re-replication inverting the study's conclusion -- is the most informative measurement: a diagnostic instrument detecting its own instability demonstrates the fragility it was designed to measure. Self-evaluation (97% zero, JSD=0.003) consistently collapses, though floor effects are possible. Output-format confound analysis finds per-strategy aggregate rho=0.89 but per-instance rho=0.219 (p=0.093); PCI reported as preference-convergence metric. We release EPC with all data. The finding is not any single coupling magnitude but the pattern of version-conditional instability that makes single-snapshot evaluator studies unreliable.

---


### 154. [Optimizing Nursing Care Taxi Dispatch Leveraging Integer Linear Programming Solvers and Machine Learning](https://arxiv.org/abs/2606.29725)

**<font color=#1a73e8>作者：</font>** Riku Nakao, Akihito Hiromori, Hamada Rizk 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we formulate a new vehicle dispatch optimization problem, called Nursing Care Taxi Dispatch, as a variant of the Vehicle Routing Problem, considering constraints related to wheelchair use, user compatibility, pick-up and drop-off times, and vehicle limitations. Previous neural-based methods for Vehicle Routing Problems have typically addressed a few simple constraints, while our new problem involves multiple complex constraints, resulting in having fewer destinations to select. This complexity makes it more difficult to obtain solutions that allow all nodes to be visited with a limited number of vehicles. To balance low violation rate, computational efficiency, and solution quality, we propose a supervised machine learning approach based on the Transformer architecture. We first obtain a set of high-quality solutions using an integer linear programming solver for given inputs and then train our learning model through supervised learning. Additionally, we introduce the post-processing of the paths generated by the learning model, ensuring that all constraints are satisfied. We compared each instance's objective function value (operating time), execution time, and constraint violation rate across different methods: our proposed method and some existing methods including integer linear programming and machine learning-based methods, using real-world facility data. Our method successfully produced balanced solutions regarding operating time, execution time, and constraint violation rate. Notably, we observed a decrease in the operating time for all problem sizes and regions, while keeping constraint violations to a minimum compared to existing methods. Especially, the decrease reached up to 8% for problem sizes with fewer than 30 users.

---


### 155. [DeepTrans Studio: Turning Expert Interventions into Shared Team Knowledge in Agentic Translation Workflows](https://arxiv.org/abs/2606.29727)

**<font color=#1a73e8>作者：</font>** Ziyang Lian, Qingya Zhang, Hao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Professional translation is often a team-based process: translators, reviewers, and project managers must coordinate terminology, legal force, and accountability across documents. Yet many LLM-based translation tools treat human corrections as isolated edits. Expert decisions made in one segment or by one member are rarely captured as reusable knowledge for the rest of the team. We present DeepTrans Studio, a collaborative translation workspace that lets professionals intercept selected nodes in an agentic translation workflow, review evidence, revise AI outputs, and save approved decisions to a shared team memory. During the demo, attendees will role-play translators and reviewers, resolve preset terminology and legal-modal risks, and see how their decisions are propagated to downstream segments and surfaced in a teammate's workspace as reusable precedents. The demo illustrates how human interventions in AI-mediated work can become shared, traceable knowledge rather than one-off corrections.

---


### 156. [How Far Do On-Prem Open LLMs Get on Text-to-SQL? A Cross-Family Size x Technique Frontier on BIRD](https://arxiv.org/abs/2606.29733)

**<font color=#1a73e8>作者：</font>** Vladimir Beskorovainyi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Organizations that cannot send data to a cloud API increasingly ask: how good is Text-to-SQL if the model must run on-premises on open weights, and which popular accuracy "recipes" are worth their compute? We answer with an honest, fully reproducible benchmark on the BIRD development split (n=1534, Execution Accuracy), evaluating three open model families across two generations -- Qwen2.5-Coder (7B/14B/32B), CodeLlama-Instruct (7B/13B/34B), and Llama-3.x (8B, 70B) -- under one matched protocol, ablating a model-agnostic recipe (schema linking, self-correction, self-consistency) component by component, with every difference tested by the paired McNemar test. Four findings stand out. (i) Generation matters more than raw size, and the recipe is family-robust: Qwen2.5-Coder dominates the older CodeLlama at matched size (39.1 vs 20.9 at 7B), but a modern non-Qwen model (Llama-3.3-70B, 49.2 on a matched serving) is competitive, so CodeLlama's weakness reflects its 2023 generation, not "non-Qwen = weak". (ii) Self-correction is a robust, near-free win, significant on all three families where there is room to improve. (iii) Schema linking does not help, and a stronger linker does not rescue it: a retrieval/embedding linker with 96.5% gold-table recall is statistically indistinguishable from no linking, ruling out the "weak lexical strawman" objection across three families. (iv) Self-consistency is poor value (+0.13 pp for ~5x tokens, not significant). We report real per-stage cost ($/1k queries) and release all code, predictions, and summaries; archived code and data: this https URL

---


### 157. [DEEPMED Search: An Open-Source Agentic Platform for Medical Deep Research with Introspective Verification](https://arxiv.org/abs/2606.29746)

**<font color=#1a73e8>作者：</font>** Maolin Liu, Fanyu Xu, Ruoqing Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Navigating the deluge of heterogeneous medical data, from academic literature (PubMed) to clinical guidelines (Web) and private knowledge bases, remains a critical bottleneck for evidence-based medicine. While commercial black-box tools lack transparency, standard open-source RAG implementations frequently suffer from reasoning drift when handling complex, long-tail queries. We present DEEPMED Search, a fully open-source, agentic platform designed for transparent medical deep research. Built on a high-performance this http URL architecture, DEEPMED Search features a source-adaptive router that autonomously dispatches sub-queries to PubMed, web search, or local graph-based knowledge bases based on information density. Crucially, the platform integrates an introspective verification module, powered by a causal-consistent multi-agent debate framework, to validate retrieved evidence against diagnostic logic before synthesis. To demonstrate its robustness, we showcase DEEPMED Search's ability to autonomously decompose high-difficulty rare disease queries, filter out confounding noise, and generate structured, citation-backed research reports in minutes. By open-sourcing this software, we provide the community with a robust infrastructure to democratize access to trustworthy, glass-box medical reasoning in research and prototyping settings.

---


### 158. [Managing Map Cardinality in Automatic Disease Classification Mapping: Balancing Precision, Recall and Coverage](https://arxiv.org/abs/2606.29750)

**<font color=#1a73e8>作者：</font>** Santosh Purja Pun, Oliver Obst, Jim Basilakis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic mapping between disease classification systems, such as the International Classification of Diseases (ICD), is a challenging yet essential task for integrating health data and conducting longitudinal data analysis. Existing embedding-based methods primarily focus on \emph{one-to-one} mappings, overlooking more complex \emph{one-to-many} scenarios. The threshold-based and top-K methods offer natural extensions; however, they involve inherent trade-offs between \emph{precision}, \emph{recall} and \emph{mapping coverage} -- the proportion of source codes with at least one mapping to a target code. To address this challenge, we introduce a novel method, which is inspired by the \emph{blocking-and-matching} pipeline commonly used in \emph{entity resolution}. In particular, we first generate a block of candidate matches (\emph{blocking}) and then employ a large language model (LLM) to identify all valid mappings within each block (\emph{matching}). Empirically, we show that the proposed method achieves higher precision with comparable recall and broader coverage across multiple ICD version pairs (ICD-9-CM$\leftrightarrow$ICD-10-CM and ICD-10-AM$\leftrightarrow$ICD-11). Our source code and dataset is available at: this https URL.

---


### 159. [PS-PPO: Prefix-Sampling PPO for Critic-Free RLHF](https://arxiv.org/abs/2606.29758)

**<font color=#1a73e8>作者：</font>** Doo Hwan Hwang, Kee-Eung Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Human Feedback (RLHF) for Large Language Models increasingly relies on critic-free methods as a practical alternative to actor--critic training. Despite their simplicity, existing critic-free approaches propagate a trajectory-level learning signal uniformly across all tokens in a trajectory. This requires full-trajectory policy updates for every rollout, leading to substantial optimization cost for long reasoning traces, even though intermediate prefixes often contain enough information to largely determine the final outcome. We propose Prefix-Sampling Proximal Policy Optimization (PS-PPO), a compute-efficient critic-free method for RLHF that exploits this temporal redundancy. PS-PPO introduces a prompt-conditioned cutoff distribution and samples a cutoff timestep for each trajectory. During the update pass, PS-PPO backpropagates only through the sampled prefix of each trajectory and applies an importance-weighting correction so that the resulting truncated gradient estimator remains unbiased with respect to the full-trajectory objective. Experiments on mathematical reasoning and RLHF benchmarks show that PS-PPO achieves large reductions in training compute and peak GPU memory, while maintaining accuracy comparable to strong critic-free baselines.

---


### 160. [TopoAgent: An Agentic Framework for Automated Topology Learning in Medical Imaging](https://arxiv.org/abs/2606.29763)

**<font color=#1a73e8>作者：</font>** Guangyu Meng, Pengfei Gu, Xueyang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Topological data analysis (TDA), particularly persistent homology (PH), captures geometric structural properties in medical images (e.g., connected components, loops, shape characteristics), which conventional pixel-level deep learning approaches often neglect. While many topological descriptors are known for converting persistence diagrams (PDs) or raw images into topological feature vectors, existing methods mostly default to a single fixed descriptor (e.g., persistence images), leaving the diversity of topological representations largely unexplored. To the best of our knowledge, there is no known large language model (LLM)-based agentic framework that can automatically determine the most suitable topological descriptors for a given image dataset and produce the corresponding topological feature vectors for downstream tasks. To fill this gap, we propose \textbf{TopoAgent}, an LLM-based agentic framework that automates topology learning for medical image this http URL operates through a Perception--Reasoning--Action--Reflection loop supported by 21 domain-specific tools and dual memory that accumulates experience across runs. Its skill set is distilled from systematic evaluation of 15 topological descriptors across 26 datasets with six classifiers. TopoAgent analyzes input images and their topological characteristics, reasons about which topological descriptors best suit the input, and determines the optimal descriptor and its configuration, all without task-specific training.

---


### 161. [CLQT: A Closed-Loop, Cost-Aware, Strategy-Consistent Benchmark for Diagnostic Evaluation of LLM Portfolio-Management Agents](https://arxiv.org/abs/2606.29771)

**<font color=#1a73e8>作者：</font>** Bo Qu, Mingguang Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly cast as autonomous portfolio managers, and benchmarks have moved from financial question-answering to sequential trading. Yet most still rank agents by returns over a fixed window -- a weak proxy, since a period's return is dominated by the market path and apparent alpha can dissolve once look-ahead leakage is controlled. Such a ranking certifies neither sound reasoning, nor a consistent strategy, nor a durable edge. We introduce CLQT, which reframes closed-loop trading evaluation as diagnosis rather than ranking: an instrument that localizes where and why an agent's process succeeds or fails. CLQT is a fully closed-loop, cost-aware, strategy-consistent, temporally-gated environment whose agents run a five-stage cycle: gather, synthesize, allocate, execute, reflect. Each round emits a complete DecisionRound sealed into a recompute-verifiable hash chain, so every metric is reconstructable from the trail. Six pillars form the substrate: a hard TimeGate, institutional transaction- and financing-cost modeling, strategy-consistency scoring, three-tier memory, a Model-Context-Protocol tool layer, and mandate-aware synthesis. The same agent runs as a constrained committee of specialized roles or a single full-autonomy orchestrator, making process scaffolding an experimental variable. From the audit trail we compute a five-axis capability scorecard (APM-CS: Coherence, Acuity, Composure, Discipline, Reliability), with Coherence judged partly by a held-out, out-of-cohort LLM to curb self-preference bias. We validate it on a contamination-controlled multi-model backtest with an ablation grid and a live broker track on unseen, post-cutoff data, against a repeated-run noise floor. CLQT separates outcome from capability, yielding not a model ranking but a durable, extensible map of agent competencies and limitations.

---


### 162. [GLIP: Graph and LLM Joint Pretraining for Graph-Level Tasks](https://arxiv.org/abs/2606.29773)

**<font color=#1a73e8>作者：</font>** Haoxin Sun, Yiqing Lin, Yajun Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graphs are widely used to model relational systems, with applications in domains such as social networks, finance, and biomedicine. Graph neural networks (GNNs) have become a mainstream approach for learning graph representations. With the rise of large language models (LLMs), recent studies have attempted to combine GNNs with LLMs. However, most existing works concentrate on node-level and edge-level tasks, while graph-level tasks, which require capturing more complex structural and feature information, remain relatively underexplored. Moreover, graph pretraining is a widely adopted strategy to alleviate the challenge of label scarcity. Most existing approaches are designed solely for GNNs such as GraphCL, leaving LLMs uninvolved in the process. To address these limitations, we propose GLIP, a Graph-LLM JoInt Pretraining framework for graph-level tasks. GLIP first performs graph augmentation to construct positive and negative pairs and introduces a multi-token selection strategy to identify patches informative in both structure and features. It further leverages a diffusion-based projector to enrich them with contextual information, enabling GLIP to capture signals from both global and local perspectives. Finally, GLIP employs a joint objective that integrates the LLM's semantic judgments with a contrastive alignment loss, ensuring consistent supervision at both the semantic and structural levels. After pretraining, GLIP is fine-tuned with limited labeled data for downstream tasks, and extensive experiments show that it outperforms state-of-the-art methods on graph-level classification and reasoning tasks. Our source code is publicly available at this https URL.

---


### 163. [Towards Generalizable and Evidential Nuclear Magnetic Resonance-Based Molecular Structure Elucidation via Large Language Model Agent](https://arxiv.org/abs/2606.29776)

**<font color=#1a73e8>作者：</font>** Zheng Fang, Chen Yang, Yusen Tan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nuclear Magnetic Resonance (NMR) spectroscopy is the gold standard for molecular structure elucidation, yet interpreting complex spectra for unknown molecules remains a bottleneck reliant on human expertise. While artificial intelligence has advanced this field, current methods face a critical trade-off: database retrieval cannot identify novel scaffolds, while de novo molecular structure elucidation models operate as black boxes, lacking the atom-level interpretability required for rigorous scientific validation. Here, we present NMRAgent, an evidential reasoning agent powered by large language models (LLMs) that bridges this gap by integrating specialized spectral analysis tools with chemical knowledge graphs. Unlike previous approaches, NMRAgent mimics the deductive reasoning of human experts: it takes experimental NMR spectra and molecular formula as input, plans the elucidation process, proposes candidate structures, verifies peak-atom consistency, and refines misaligned substructure through formula-aware fragment optimization. Enabled by its evidential reasoning, NMRAgent outperforms state-of-the-art methods, improving top-1 accuracy by 46.5% and Tanimoto similarity by 0.502 on a scaffold-split benchmark with novel scaffolds in the test set. Besides, we demonstrate the agent's practical utility by elucidating the structures of two previously unknown natural products isolated from Hydrangea davidii and Vitex trifolia, and by correcting structural misassignments in established literature. By combining high-accuracy prediction with transparent and evidence-based reasoning, NMRAgent establishes a new paradigm for interpretable AI in analytical chemistry.

---


### 164. [Graph-GSReg: Leveraging 3D Scene Graphs for Gaussian Splatting Registration](https://arxiv.org/abs/2606.29782)

**<font color=#1a73e8>作者：</font>** Jaewon Lee, Mangyu Kong, Euntai Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Merging multiple 3D Gaussian Splatting (3DGS) scenes into a single unified Gaussian representation is essential for large-scale 3D mapping and long-term map management. Despite its importance, this area remains underexplored, and existing solutions exhibit several limitations. Learning-based methods attempt direct correspondence between Gaussian primitives and require training on large 3DGS datasets. Image-based optimization methods depend heavily on coarse initialization from generic foundation models and often incur expensive refinement. We present \ourmodel. Our method constructs a 3D scene graph from a 3DGS and its rendered images, \textit{reformulating 3DGS registration as a graph registration problem}. The proposed 3D scene graph represents each 3DGS at a higher-level representation, enabling a globally consistent understanding of semantic information and structural context for accurate registration. To further construct a seamless unified scene, we introduce a Self-Supervised Test-Time Optimization. Naively merging two 3D Gaussian scenes often suffers from occlusion artifacts such as hollows and floaters. To alleviate this issue, we refine the merged Gaussians to preserve visual consistency between the original scenes and the merged scene. We evaluate our method on real and synthetic benchmarks, demonstrating competitive registration accuracy and merged scene rendering quality.

---


### 165. [MemLeak: Diagnosing Information Leaks in Multimodal Agent Memory](https://arxiv.org/abs/2606.29788)

**<font color=#1a73e8>作者：</font>** Kuan Wang, Chao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a multimodal AI agent is asked to forget a fact, current memory systems usually delete the text entry and report success. We find that the fact can remain recoverable from retained user images, including images tagged to entirely different facts, because VLMs use implicit visual cues at inference time. We introduce the Information Provenance Graph (IPG), a taxonomy that classifies memory representations by deletion affordance. The IPG reveals that deletion fails through multiple channels. Our benchmark, MemLeak, measures this across a deletion cascade: direct probing of deletion-capable systems yields <1%, but retained correlated text enables 18.3% recovery, and retained images enable 12.0% recovery (0.0% blind baseline, 0.3% FPR) -- with 47% of image leaks not text-recoverable. Content-aware semantic deletion reduces the image residual to 2.0%. The residual appears across multiple VLMs, a production memory system, and real Unsplash-licensed photographs. Dual-annotator human validation (kappa = 0.88) confirms judge reliability.

---


### 166. [Are Humans Evolved Instruction Followers? An Underlying Inductive Bias Enables Rapid Instructed Task Learning](https://arxiv.org/abs/2606.29792)

**<font color=#1a73e8>作者：</font>** Anjishnu Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human adults can often perform a novel task correctly on the first attempt after only receiving verbal or written instructions. This rapid instructed task learning (RITL) is a hallmark of human cognitive flexibility, yet its mechanisms and parallels in artificial systems remain under-explored across disciplines. In this position paper, we argue that humans possess an evolved instruction-following bias -- an inductive bias shaped by evolution to interpret and execute linguistic instructions which critically enables fast generalization of behavior from language. This bias functions analogously to the way large language models (LLMs) leverage instruction tuning to achieve zero-shot task performance. We synthesize evidence from cognitive science, neuroscience, and machine learning research to support this hypothesis. While instruction-following in AI is currently achieved via specialized training protocols, we posit that in humans it arises as an innate cognitive architecture feature. We outline testable predictions and call for more interdisciplinary research to investigate Instruction-Following as a unifying mechanism enabling rapid task learning in both natural and artificial neural networks.

---


### 167. [The CRISTAL Method: Neurosymbolic analysis from AI-synthesized world models](https://arxiv.org/abs/2606.29799)

**<font color=#1a73e8>作者：</font>** Rafael Kaufmann, Felix Neubürger, Michael Walters 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This project introduces the CRISTAL Method (Coherent Reliable Intentional Synthesis of Truthful Analysis Logic), a neurosymbolic framework for automating complex analysis workflows, with fundamental investment analysis as a primary use case. This domain poses major challenges: high structural uncertainty, noisy and subjective data, tight attention budgets, and the need for justified, reproducible decisions. Human analysts often struggle in this domain due to cognitive biases and limitations, suggesting significant value in automation. But while LLM-based agents have been proposed as analytical aids, their limitations -- poor numerical reasoning, unawareness of uncertainty, and lack of reproducibility -- hinder their effectiveness in this context. CRISTAL addresses these gaps through a principled blend of statistical model synthesis, continuous learning, and active learning. Starting from a natural-language prior knowledge curriculum, CRISTAL builds a dynamic, interpretable probabilistic program that enables full Bayesian inference, including uncertainty quantification and budget-aware data acquisition. CRISTAL continually refines its world model during analysis, leveraging LLMs for code synthesis and learning. We validate CRISTAL on a novel benchmark of synthetic equities with rich financial and textual data. On a company classification task, CRISTAL achieves Bayes-optimal accuracy with just 5 examples and a 5-second budget, outperforming state-of-the-art LLMs that plateau around 40\% accuracy even with order-of-magnitude more input data and compute.

---


### 168. [Clearer Sight, Fewer Lies: Oriented Pickup Preference Optimization for Multimodal Hallucination Mitigation](https://arxiv.org/abs/2606.29805)

**<font color=#1a73e8>作者：</font>** Xin Zou, Haolin Deng, Yibo Yan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) are prone to hallucination as their generation preferences are insufficiently calibrated to visual evidence, causing them to fall back on linguistic priors, rather than faithful grounding. In this work, we start from an empirical observation: when query-relevant visual evidence is explicitly strengthened using the model's own attention, generation becomes more accurate, suggesting that many failures do not arise solely from missing perception, but from an insufficient tendency to trust the evidence the model has already attended to. Motivated by this finding, we propose Oriented Pickup Preference Optimization (\texttt{OPPO}), an evidence-aware alignment objective that learns preferences over the strength of visual evidence, rather than only response quality. Concretely, \texttt{OPPO} contrasts the same faithful response under stronger, anchored, weaker-evidence views, turning naive visual preference into ordered visual-evidence alignment. We further combine this objective with fine-grained span-level and token-level regularization to stabilize the training. Besides, we provide a theoretical analysis showing that ordered evidence margins induce a positive lower bound on local visual sensitivity. Extensive evaluations across hallucination and general-purpose benchmarks demonstrate that \texttt{OPPO} consistently outperforms baseline methods.

---


### 169. [Making Multimodal LLMs Reliable Chart Data Extractors: A Benchmark and Training Framework](https://arxiv.org/abs/2606.29808)

**<font color=#1a73e8>作者：</font>** Yuchen He, Peizhi Ying, Liqi Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Chart data extraction, which reverse-engineers data tables from chart images, is essential for reproducibility, analysis, retrieval, and redesign. Existing interactive tools are reliable but tedious, and mixed-initiative systems, while more efficient, lack generalizability. Recent multimodal large language models (MLLMs) offer a unified interface for chart interpretation, yet their ability to extract accurate data tables, especially without visible labels, remains unclear. We build a benchmark featuring diverse real-world charts without data labels to evaluate this capability. Results show that, while current MLLMs reliably reconstruct table structures, they struggle with precise value recovery. To address this, we revisit chart data extraction from a human-centered perspective and argue that extraction should follow a progressive learning process similar to how people read charts. Our training framework substantially improves numerical accuracy, achieving state-of-the-art performance with a 7B-parameter model. A user study further shows that our model effectively supports mixed-initiative workflows for reliable chart data extraction.

---


### 170. [Consistency as Inductive Bias: Learning Cross-View Invariance for Robust Multimodal Reasoning](https://arxiv.org/abs/2606.29812)

**<font color=#1a73e8>作者：</font>** Xin Zou, Haolin Deng, Yibo Yan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inductive biases steer learning toward generalizable solutions by encoding task structure. In this work, we identify a crucial missing bias in MLLMs: cross-view consistency, \textit{i.e.}, semantically invariant views of the same instance should lead to the same answer. Standard reinforcement learning with verifiable rewards (RLVR) objectives do not impose this constraint, but instead assign pointwise rewards to each visual input. Even with data augmentation (DA), transformed views are typically rewarded independently, providing little signal once within-view rewards saturate. We propose \textbf{ConsistRoll}, a simple but effective method that injects cross-view consistency into RLVR training by reusing the group-sampling mechanism of GRPO. Specifically, ConsistRoll places original and semantically invariant transformed views in the same generation group, and assigns a joint reward only when paired completions are both correct and consistent. In this way, ConsistRoll turns consistency into an online credit-assignment signal, \textbf{without extra generation overhead and annotations}. Theoretically, we show that cross-view consistency is a valid inductive bias, and ConsistRoll introduces a cross-view correction term absent from DA, penalizing view dependence and alleviating advantage collapse. Comprehensive benchmarks across math, general-purpose, hallucination domains confirm that ConsistRoll achieves robust improvements in multimodal reasoning.

---


### 171. [SrDetection: A Self-Referential Framework for Data Leakage Detection in Code Large Language Models](https://arxiv.org/abs/2606.29815)

**<font color=#1a73e8>作者：</font>** Shuaimin Li, Liyang Fan, Zeyang Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating code large language models (Code LLMs) requires reliable detection of data leakage, where benchmark performance is artificially inflated by exposure to benchmark data during pre-training. Existing approaches either assume access to proprietary training corpora, rely on brittle heuristics such as timestamp filtering, or use external reference sets with manually tuned, non-generalizable thresholds. To address these limitations, we introduce \textbf{SrDetection}, a unified \textbf{s}elf-\textbf{r}eferential leakage detection framework for both gray-box (access to model logits) and black-box (access to model outputs) settings. SrDetection generates semantically equivalent variants of a benchmark sample and detects leakage by contrasting the model's behavior on the original versus its variants, flagging cases where the original is disproportionately easier for the model. We further design a controlled leakage detection testbed and evaluate SrDetection in this environment. Across different models and training stages, SrDetection improves average F1 by 21.52 points in the gray-box setting and 14.46 points in the black-box setting over strong baselines, demonstrating robust, threshold-independent leakage detection. Finally, a gray-box study of 15 widely used Code LLMs on four popular benchmarks reveals benchmark-specific leakage patterns beyond prior overlap-based analyses\footnote{\footnotesize Source code and data are available at this https URL

---


### 172. [Neural Procedural Memory: Empowering LLM Agents with Implicit Activation Steering](https://arxiv.org/abs/2606.29824)

**<font color=#1a73e8>作者：</font>** Chengfeng Zhao, Yuqiao Tan, Shizhu He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) excel as static solvers, transforming them into autonomous agents remains challenging. This transition requires continuous environmental interaction, yet current agents lack the necessary persistent procedural memory. Existing approaches predominantly employ Retrieval-Augmented Generation (RAG) to inject explicit textual guidelines into model contexts. However, relying solely on symbolic instructions can introduce a text-action disconnect, frequently failing to activate the internal representations necessary for correct task execution. To address this, the paper introduces Neural Procedural Memory (NPM), a training-free framework that represents agent memory through implicit activation steering rather than explicit instructions. By distilling procedural skills from historical contrastive experiences into steering vectors in the activation space, NPM directly activates the task-relevant neural mechanisms to guide task execution. Evaluations across four agent benchmarks show that NPM performs comparably to baselines using explicit textual instructions. Furthermore, the results show that combining implicit steering with explicit workflows provides complementary advantages, leading to more robust task execution. Representational analyses indicate that these steering vectors encode consistent task logic, forming organized structures within the activation space. These findings suggest that implicit activation steering provides a promising approach for managing agent memory.

---


### 173. [See Only When Needed: Context-Aware Attention Intervention for Mitigating Hallucinations in LVLMs](https://arxiv.org/abs/2606.29847)

**<font color=#1a73e8>作者：</font>** Yuqing Lei, Wenbo Lyu, Yingjun Du 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) excel at multimodal tasks but remain prone to object hallucinations. Prior training-free remedies often uniformly strengthen visual signals, which may also amplify irrelevant regions and introduce spurious evidence, harming fluency. We propose Context-aware Attention Intervention (CAI), a training-free inference-time mechanism that enforces a see only when needed principle via two-axis selectivity: where to look and when to intervene. At each decoding step, CAI derives token-specific visual relevance from early-layer representations to localize semantically aligned regions, and applies a conservative, entropy- and depth-gated attention tilt only for uncertainty-spiking tokens in deeper layers where visual grounding degrades, leaving confident tokens and irrelevant regions largely unchanged. This targeted intervention strengthens visual grounding while preserving linguistic fluency, and it yields consistent improvements even without contrastive decoding, which remains optional as an auxiliary bias-suppression module. Extensive experiments across multiple LVLM backbones and benchmarks show that CAI achieves state-of-the-art hallucination mitigation, and our analysis characterizes CAI as a KL-minimal attention reweighting with bounded interference under inactive gates or small tilts. Code is available at this https URL.

---


### 174. [KbSD: Knowledge Boundary aware Self-Distillation for Behavioral Calibration in Agentic Search](https://arxiv.org/abs/2606.29863)

**<font color=#1a73e8>作者：</font>** Tao Feng, Xinke Jiang, Chao Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic search equips large language models with dynamic retrieval abilities, but existing reinforcement learning methods remain limited by reward sparsity in knowledge boundary calibration -- deciding when to trust parametric memory, when to rely on retrieved evidence, and when to abstain. Binary rewards can penalize undesirable outcomes, but provide little guidance on the reasoning process required to make calibrated decisions across different knowledge states. To address this, we propose KbSD (Knowledge boundary Self-Distillation), a framework that tackles this limitation through dense token-level supervision, outcome-level sparse rewards, and quadrant-adaptive optimization. KbSD constructs a hint-augmented teacher, architecturally identical to the student, that receives explicit knowledge boundary signals -- including parametric certainty, retrieval quality, and ground-truth answers -- to generate calibrated reasoning demonstrations. This information-asymmetric self-distillation enables dense supervision without requiring a larger external model. To further account for the heterogeneous reasoning distributions across knowledge states, we introduce a quadrant-adaptive distillation objective: reverse KL for concentrated integration, forward KL for diverse refusal, and Pareto-optimal bidirectional KL for asymmetric quadrants requiring both precision and coverage. Experiments on multiple benchmarks show that KbSD consistently improves both task accuracy and hallucination mitigation over strong baselines, with the largest gains appearing in the challenging quadrants where sparse rewards are least informative.

---


### 175. [ARKD: Adaptive Reinforcement Learning-Guided Bidirectional KL Divergence Distillation for Text Generation](https://arxiv.org/abs/2606.29869)

**<font color=#1a73e8>作者：</font>** Zilong Liu, Xuewen Zhang, Jinrui Xing 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) is a key technique for compressing Large Language Models (LLMs), yet methods relying on a single KL objective often fail to balance primary distribution fitting with long-tail probability modeling, limiting both generation quality and generalization. To address this, we analyze the complementary roles of forward and reverse KL divergence (FKL/RKL) in distribution alignment from theoretical and empirical perspectives. We then propose a reinforcement-learning-based adaptive KL-weighted distillation framework, in which a policy network dynamically assigns weights to FKL and RKL based on teacher-student distributional characteristics, guided by immediate reward signals to achieve dual alignment on principal and long-tail modes. Extensive experiments demonstrate consistent improvements across Rouge-L and BertScore metrics, surpassing greedy heuristics by 0.4-0.6 points and outperforming other baseline methods on diverse benchmarks.

---


### 176. [Clinical Reasoning Graphs: Structured Evaluation of LLM Diagnostic Reasoning Reveals Competence Without Consistency](https://arxiv.org/abs/2606.29876)

**<font color=#1a73e8>作者：</font>** Nisarg A. Patel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern large language models (LLMs) reach 60-70% diagnostic accuracy on complex clinical case benchmarks, but accuracy alone cannot distinguish stable clinically-grounded reasoning from pattern matching. We introduce clinical reasoning graphs, structured graph representations extracted from free-text LLM diagnostic traces using a domain-grounded ontology with 5 node types and 7 edge types. We apply this pipeline to 750 traces from five LLMs across 50 New England Journal of Medicine Clinicopathological Conference cases and three prompt conditions, and test whether diagnostic traces show stable structured reasoning patterns, or diagnostic schemas, for clinically similar cases. We operationalize this as higher graph similarity among clinically similar cases than among clinically dissimilar ones. Across 15 model-condition comparisons, within-cluster and between-cluster composite similarity are nearly equal, and no comparison survives multiple-testing correction; a component-level analysis finds any residual content signal far below schema scale. Graph similarity is also nearly identical for pairs of models that are both correct (0.488) and both incorrect (0.484), suggesting that graph structure captures a dimension not reflected in diagnostic accuracy. Structured reflection prompting increases explicit discriminating-feature analysis within traces (+33%) but does not increase cross-case consistency. These results show diagnostic competence without schema-scale reasoning consistency, and indicate that final-answer accuracy should be complemented by process-level evaluation. We release the ontology, extraction pipeline, validation protocol, and the extracted reasoning graphs and similarity artifacts as resources for structured evaluation of LLM clinical reasoning.

---


### 177. [LWDrive: Layer-Wise World-Model-Guided Vision-Language Model Planning for Autonomous Driving](https://arxiv.org/abs/2606.29879)

**<font color=#1a73e8>作者：</font>** Chen Yang, Yuhao Wei, Ze Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) provide powerful semantic understanding and commonsense reasoning for End-to-End Autonomous Driving (E2E-AD) planning. However, trajectories directly generated by VLMs often encode only coarse driving intentions and remain insufficient for geometrically accurate, future-aware, and multi-view-grounded planning. To address these limitations, we develop the Layer-Wise World-Model-Guided Driving framework (LWDrive). LWDrive is a VLM planning framework that refines coarse trajectories through layer-wise world-model guidance. Instead of treating the VLM output as the final trajectory, LWDrive uses it as an intent-aware coarse plan, expands a diverse candidate space around it, and progressively refines the candidates through a Foresight Cascade Planner (FCP). Specifically, we introduce future-frame generation supervision to encourage the VLM to learn forward-looking scene representations, thereby injecting planning-relevant predictive dynamics into its internal hidden states. Built upon these world-model-supervised representations, FCP exploits VLM features across multiple layers and integrates historical temporal states, Action-Query representations, and current-frame multi-view Bird's-Eye-View (BEV) features to refine candidate trajectories in a coarse-to-fine manner. This design enables progressive correction of spatial positions and motion trends while grounding trajectory refinement with multi-view scene cues and preserving the high-level driving intention produced by the large model. Finally, a score head evaluates the refined candidates and selects the best trajectory as the final planning output. Experiments show that LWDrive achieves a score of 92.0 on the NAVSIM benchmark and 89.6 on NAVSIM-v2. Code and models will be made publicly available.

---


### 178. [LLM-based Multimodal Personality Recognition via Facial Action Unit-Text Semantic Fusion](https://arxiv.org/abs/2606.29900)

**<font color=#1a73e8>作者：</font>** Tianyi Zhang, Wei Shan, Yuan Zong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personality recognition in asynchronous video interviews (AVIs) has become increasingly important due to their widespread adoption in modern recruitment. Existing approaches often rely on large language models (LLMs) to analyze textual responses of interviewees in AVI. However, unimodel methods often suffer from information loss (e.g., ignore facial cues). In contrast, multimodal methods that employ full-face images or sparsely sampled frames can discard fine-grained temporal dynamics critical for accurate personality assessment. To overcome these limitations, we propose an LLM-based framework that semantically fuse facial action units (AUs) with textual responses of AVI. AU sequences are first converted into interpretable textual descriptions, which are then fused with participants' textual responses through an LLM. A lightweight regression head transforms the resulting embeddings into continuous personality scores without disrupting the underlying semantic space. Experiments on the AVI-6 benchmark demonstrate consistent improvements over most baselines, with lower prediction errors and stronger correlations with human-rated scores across multiple traits. Further analysis reveals that AU-derived semantic representations offer complementary non-verbal cues to textual responses. Decoupling semantic understanding from regression prediction within the LLM also leads to greater training stability and clearer interpretability. Overall, these findings demonstrate that AU-text fusion provides a psychologically grounded and computationally efficient framework for personality recognition in AVIs.

---


### 179. [Traffic-CBM: A Structurally Interpretable Multimodal Framework for Encrypted Traffic Classification](https://arxiv.org/abs/2606.29909)

**<font color=#1a73e8>作者：</font>** Honglei Jin, Wenshuo Chen, Shaofeng Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Encrypted traffic classification has achieved strong performance, but its decision process remains difficult to interpret. Existing methods usually combine flow statistics, packet sequences, and byte-level representations into opaque latent features, making it unclear which type of evidence actually drives the prediction. In this paper, we propose Traffic-CBM, a structurally interpretable multimodal framework for encrypted traffic classification. Instead of directly fusing heterogeneous traffic signals into a black-box representation, Traffic-CBM organizes them into a unified hierarchical concept space. These concepts are not manually annotated semantic attributes; rather, they are scalar evidence summaries constrained by predefined traffic evidence groups. More specifically, grouped flow statistics are mapped to statistical concepts, dedicated temporal encoders learn temporal concepts from disjoint feature subspaces, and byte-level evidence is further organized into packet-level and cross-packet concepts. This design turns heterogeneous traffic evidence into an explicit concept representation and makes different levels of traffic evidence easier to analyze. We evaluate Traffic-CBM on multiple encrypted traffic benchmarks. Results show that it achieves competitive and balanced classification performance while providing a clearer structural interpretation interface than conventional end-to-end fusion models. Further analyses suggest that the learned concept space is actively used in the prediction process and provides a clearer structural explanation of multimodal traffic evidence.

---


### 180. [MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation](https://arxiv.org/abs/2606.29914)

**<font color=#1a73e8>作者：</font>** Kuan Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent memory systems are increasingly evaluated against RAG and full-context baselines, but reported gains often mix changes in the memory method with changes in the language model, embedding model, or retrieval pipeline, making it unclear what is actually being measured. We present MemDelta, a controlled evaluation protocol that varies one component at a time on LongMemEval-S (500 questions, 50+ sessions, three model families). Four findings emerge: (1) verbatim RAG matches full-context GPT-4o-mini (47.2% vs. 49.8%, p = 0.34), but the ranking reverses across models: Gemini gains +14pp from full context, while Sonnet gains +31pp from RAG, partly because it refuses 63% of full-context queries; (2) swapping only the embedding model in an identical pipeline shifts accuracy by +6.2pp at n = 500 (p = 0.004), and Mem0 beats MiniLM-RAG by +11pp but loses to cloud-RAG by 1.2pp, so one variable flips the conclusion; (3) agent self-memory (42%) underperforms basic retrieval (47%); (4) on 2 of 6 question types (n = 88), Mem0 matches cloud RAG (72.7% vs. 73.9%, p = 1.0) at 50x the cost, suggesting narrow rather than general gains. We recommend memory evaluations fix embedding models across comparisons, stratify by model family, and report write-path cost before attributing gains to architecture.

---


### 181. [Can LLM-as-a-Judge Reliably Verify Rubrics in Agentic Scenarios?](https://arxiv.org/abs/2606.29920)

**<font color=#1a73e8>作者：</font>** Yangda Peng, Yunjia Qi, Hao Peng 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubric-based scoring has become a widely used paradigm in model evaluation, typically with LLM-as-a-Judge (LaaJ) for rubric scoring. However, the reliability of LaaJ for rubric scoring remains underexplored. This concern is especially pronounced in agentic scenarios, where long, complex outputs further challenge reliable scoring. To address this, we conduct a systematic meta-evaluation of LaaJ reliability for rubric verification. We introduce RuVerBench, the first benchmark for assessing LaaJ reliability in rubric verification for agentic scenarios. RuVerBench covers two prevalent agentic domains, deep research and agentic coding, with 2,458 instances, each containing a model-generated output, a rubric, and a human-annotated label indicating whether the output satisfies the rubric. Using RuVerBench, we evaluate numerous frontier LLMs and find that even the most advanced models achieve strong performance but still exhibit substantial noise. We further analyze the impact of key LaaJ strategies, including prompt design, batching, and majority voting, on rubric verification. We find that weaker models are more sensitive to prompt variations, batched verification presents a trade-off between accuracy and efficiency, and majority voting yields effective but diminishing returns. We have released our dataset and code to facilitate future research: this https URL.

---


### 182. [HippoSpark: An On-Demand Experience System for LLM Reasoning](https://arxiv.org/abs/2606.29929)

**<font color=#1a73e8>作者：</font>** Jingyao Liu, Danling Meng, Chen Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Distilling historical trajectories into reusable experience to enhance future problem-solving has become a focal point of recent LLM research. However, existing methods predominantly operate at the task level, leveraging general summaries or rules under the assumption that analogous tasks share universal solution patterns. This approach often fails in complex reasoning, which typically falters at local bottlenecks that require precise, state-specific guidance rather than broad heuristics. We introduce HippoSpark, a state-level experience system that performs on-demand retrieval tailored to the immediate needs of the current reasoning state. Across mathematical, scientific, and programming benchmarks, HippoSpark consistently outperforms both standard prompting and task-level experience baselines. Our findings reveal that the most effective experience systems are those that provide actionable guidance at critical bottlenecks rather than serving as generic task-level context. Our code is available at this https URL.

---


### 183. [Towards Physical Intuitions for Alignment Dynamics: A Case Study With Randomness Crystallization](https://arxiv.org/abs/2606.29933)

**<font color=#1a73e8>作者：</font>** Kunal Samanta, Ari Holtzman, Peter West  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The alignment of language models is typically studied through the lens of capability benchmarks, but the dynamics of how models change during post-training remain poorly understood. We argue that the physical sciences, and thermodynamic phase-transition theory in particular, offer a principled and underexplored vocabulary for reasoning about these dynamics. As a case study, we instantiate this position through the lens of material Crystallization, which is a well-studied thermodynamic phase transition. For tasks like random number generation, this breaks into 3 phases: (1) the high entropy liquid phase in the pretrained model, with many distinct sampling distributions promptable from the model; (2) the nucleation phase caused by supervised finetuning, in which behavior collapses onto a single seed distribution present in the pretrained LLM; and (3) a settling phase in which reinforcement learning techniques redistribute probability of the collapsed distribution, but largely keep it concentrated on the same options as the seed distribution. We propose intuitive metrics to verify the transitions between these phases, and validate the idea across a range of random tasks. Crystallization is one instance of a broader class of physical frameworks we believe alignment research should import to answer questions about where alignment-induced structure comes from, why it converges where it does, and what it fundamentally cannot change.

---


### 184. [IHDec: Divergence-Steered Contrastive Decoding for Securing Multi-Turn Instruction Hierarchies](https://arxiv.org/abs/2606.29960)

**<font color=#1a73e8>作者：</font>** Nicole Geumheon Liu, Haeun Jang, Yonghyun Jun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) often fail to maintain instruction hierarchies (IH) when processing multi-source inputs with varying role-level priorities, paradoxically adhering to lower-priority directives during conflicts. While existing defenses mitigate this issue, they are largely restricted to single-turn scenarios and require expensive fine-tuning. In this paper, we formalize this failure mode in multi-turn contexts via a Jensen-Shannon Divergence (JSD) framework, uncovering a pervasive role-influence inversion phenomenon where subordinate inputs override superior roles. To rectify this without training, we propose IHDec (Instruction Hierarchy-steered Decoding). IHDec leverages JSD to automatically detect token-level hierarchy violations and dynamically executes contrastive decoding to suppress misaligned subordinate roles. Extensive evaluations demonstrate that IHDec outperforms training-based baselines in multi-turn conflicts while fully preserving general response quality. Furthermore, IHDec strengthens safety against adversarial prompt injections and exhibits a robust scaling synergy with larger models. The Code is available at this https URL

---


### 185. [Atompack: A Storage and Distribution Layer for Read-Heavy Atomistic ML Training Datasets](https://arxiv.org/abs/2606.29975)

**<font color=#1a73e8>作者：</font>** Ali Ramlaoui, Daniel T. Speckhard, Sagar Pal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Atomistic machine learning datasets are increasingly used for training: large immutable snapshots are read repeatedly, shuffled across epochs, staged across clusters' storage systems, and republished as reusable scientific artifacts. This workload differs from interactive scientific curation, where mutable records and ad hoc inspection are often more important than random indexed throughput. We present Atompack, an append-oriented storage format and distribution layer designed around a simple workload: training pipelines usually consume complete molecular records, while the order of records is randomized by the learning algorithm. Atompack appends records efficiently during dataset construction, then commits an immutable index and serves records through a memory-mapped read path optimized for training. We compare Atompack with HDF5, LMDB, and ASE baselines representing array stores, key-value records, serialized records, and object-oriented databases. The benchmarks measure sequential reads, shuffled reads, shared-filesystem behavior, write throughput, and artifact size. On a representative 64-atom workload, Atompack is 96x faster than ASE LMDB on shuffled training-style reads while producing artifacts about 79\% smaller. The results indicate that serving complete molecule records, rather than field chunks or reconstructed objects, improves shuffled training throughput while keeping artifacts compact enough for public distribution.

---


### 186. [Exploration and Online Transfer with Behavioral Foundation Models](https://arxiv.org/abs/2606.29980)

**<font color=#1a73e8>作者：</font>** Louis Bagot, Mathieu Lefort, Laëtitia Matignon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Zero-shot Transfer in Reinforcement Learning (RL) aims to train an agent that can generate optimal policies for any reward function, without additional learning at transfer time, while training only on reward-free trajectories. For their generality over tasks, such models are sometimes called ``Behavioral Foundation Models'' (BFMs). While they have shown strong performances and improvements in recent years, the current framework and algorithms still assume that, during the transfer phase, the agent is informed offline about the reward (the task to solve) through a dataset of state-reward pairs, which it uses to pick the best policy to deploy. However, in practice if the reward is a black-box (e.g. direct user feedback), it is not possible to generate such a dataset: it is necessary to observe the reward through interactions with the environment. In other words, the current framework of offline transfer is not aligned with the traditional RL setting of online learning through trial-and-error, which requires exploration in order to find rewards. This paper proposes to tackle this new online transfer in zero-shot RL, with the key insight that the BFM itself can be used to generate exploration policies. We show that it is possible to frame this online learning problem in terms of a bandit-like exploration-exploitation problem. More precisely, at each step the bandit algorithm recommends a policy, the BFM executes it in the environment, which yields a reward and a new state; we repeat the process until we converge to the optimal policy. In the popular context of linear reward approximation, we derive a formulation inspired by Upper Confidence Bound and show that exploration can be achieved through the minimization of the eigenvalues of an uncertainty matrix. We evaluate qualitatively and quantitatively our framework on a simple environment to validate the concept of our method.

---


### 187. [Be Faithful When Response: Returning Fluent and Grounded Answers for Vision-Language Models Reinforcement Learning](https://arxiv.org/abs/2606.29984)

**<font color=#1a73e8>作者：</font>** Peng, Yin Zhang, Yanglin Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) is an important paradigm for improving the reasoning capabilities of Vision-Language Models (VLMs). However, directly applying RL to rollout multimodal reasoning can lead to instability, due to the exploitation of language priors, the neglect of visual evidence, and the generation of reasoning traces that are fluent yet not visually grounded. The question arises: Can initially steer the policy toward visually faithful reasoning regime before applying reinforcement learning? To this end, we propose a Faithful Warm-Start (FWS) strategy that first curates samples with explicit vision-language causal relationships from six general VQA benchmarks to construct the FaithfulQA dataset, where each of the image-question pairs gains a certain degree of visual observations, question requirements, commonsense knowledge, domain knowledge, and the final answer. Subsequently, a VLM-based judge is employed to further purify the dataset, ensuring strong causal consistency and visual faithfulness. This warm-start stage equips the model with the capability to understand causally grounded vision-language patterns before subsequent RL optimization under sparse answer-level rewards. Experimental results show that such faithful supervision improves answer accuracy, stabilizes RL training, and reduces visually unsupported reasoning.

---


### 188. [Are We Measuring Strategy or Phrasing? The Gap Between Surface- and Approach-Level Diversity in LLM Math Reasoning](https://arxiv.org/abs/2606.29985)

**<font color=#1a73e8>作者：</font>** Sangmook Lee, Minbeom Kim, Jeonghye Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diversity in LLM mathematical reasoning is critical for exploration, but common diversity metrics mostly capture surface-level variation rather than differences in how a problem is solved. We address this gap by introducing approach-level diversity: variation in strategies across correct solutions to the same problem. Using a human-calibrated LLM judge framework, we show that prior diversity measures are unreliable proxies for approach-level diversity, and this mismatch carries over to diversity-aware RLVR, where target metrics are preserved while approach-level diversity declines. Investigating when approach-level diversity helps and whether it can be directly induced, we find that approach-diverse candidate sets improve test-time scaling. However, optimizing an LLM judge diversity reward during training causes the policy to exploit judge-specific preferences rather than broaden its approaches, leaving direct optimization of approach-level diversity as an open problem. Together, our work introduces the notion of approach-level diversity and uncovers a systematic divergence between surface- and approach-level signals, marking a step toward LLMs that reason in genuinely diverse, human-like ways.

---


### 189. [Rigel: Self-Distilled Score Adaptation for Image and Video Captioning Evaluation](https://arxiv.org/abs/2606.29997)

**<font color=#1a73e8>作者：</font>** Shuitsu Koyama, Kazuki Matsuda, Yuiga Wada 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic evaluation of image and video captioning is essential for benchmarking multimodal systems, although standard evaluation metrics show limited alignment with human judgments. Recent approaches using large language models (LLMs), commonly referred to as LLM-as-a-Judge, have improved alignment with human judgments but still suffer from a mismatch between large-vocabulary language modeling and evaluation over a small label set. To address this, we propose Rigel, an automatic evaluation metric for image and video captioning, based on self-distilled score adaptation. The metric employs an evaluation-specific scoring head distilled from a frozen LLM, which captures judgment signals in a task-aligned space without relying on large-vocabulary token sets. We then refine the LLM backbone with human judgment data. To train Rigel, we constructed the Vid-Lepus dataset, which contains 3,338 video clips, 33,380 reference captions, and 5,637 candidate captions. Experiments on multiple benchmarks show that Rigel outperforms state-of-the-art metrics, achieving over 10-point improvements on ActivityNet-Fact in the reference-free setting.

---


### 190. [LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via a Proprioceptive Dashboard](https://arxiv.org/abs/2606.30005)

**<font color=#1a73e8>作者：</font>** Binyan Xu, Haitao Li, Kehuan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon tool agents are bottlenecked by how their context grows toward the limits of the context window. Recent systems make context management agent- or system-controlled, but they either learn a compression policy that discards evidence or manage context in a layer the agent never sees. We argue both leave a more basic gap unaddressed. Frontier language models are proprioceptively blind to their own context. From the prompt alone they cannot see how large, how old, or how used each block is, the signals a keep-or-drop decision needs. We hypothesize that competent context management is already latent in capable models, and that what is missing is not a learned policy but an interface exposing this state. We introduce VISTA (Visible Internal State for Tool Agents), a training-free, model-agnostic layer that represents working memory as typed, addressable blocks, surfaces a runtime dashboard of per-block token usage, recency, and access history, and archives blocks as recoverable full-fidelity payloads. On LOCA-Bench, BrowseComp-Plus, and GAIA, the same untrained interface transfers across million-, 100K-, and 10K-scale trajectories. On LOCA-Bench it improves four backbones and lifts Gemini-3-Flash from 22.7 to 50.7%. The lift grows with context pressure and transfers across backbones. Ablations further confirm that the dashboard matters beyond archive and recovery tools.

---


### 191. [Node-to-Neighborhood Semantic Consistency: Text-Topology Alignment for TAGs Anomaly Detection](https://arxiv.org/abs/2606.30009)

**<font color=#1a73e8>作者：</font>** Bochen Lin, Jianxiang Yu, Jiayi Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Graph anomaly detection (GAD) on text-attributed graphs (TAGs) is vital for applications such as fraud detection and academic integrity verification. Existing approaches generally fall into two paradigms. GNN-based methods effectively capture structural patterns but struggle to capture fine-grained textual semantics. Methods integrating LLMs with graphs improve semantic understanding yet fail to fully comprehend topological relationships among neighboring nodes. Moreover, both paradigms overlook the correspondence between textual semantics and graph topological relationships, limiting their ability to identify nodes whose semantics are inconsistent with their neighborhoods. In this paper, we formalize TAG anomaly detection as a node-to-neighborhood semantic consistency problem, where anomalies may arise from either textual semantic mismatch or topological deviation between a node and its neighbors. We propose N2NSC (Node-to-Neighborhood Semantic Consistency), a framework that captures the correspondence between graph topology and textual semantics through two complementary fusion paths. The two pathways work synergistically, enabling the LLM to fully leverage both textual and structural neighborhood information for anomaly detection. Extensive experiments across eight datasets demonstrate that N2NSC consistently outperforms current state-of-the-art methods.

---


### 192. [Parametric Skills](https://arxiv.org/abs/2606.30015)

**<font color=#1a73e8>作者：</font>** Xuan Zhao, Haonan He, Qingyu Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Since intelligence fundamentally relies on efficient skill acquisition (Chollet, 2019), the ability to leverage skills is critical. For LLMs, skills, manually authored or extracted from task trajectories, are textual recipes encoding mature problem-solving experience and are critical to agentic capabilities. Despite widespread deployment, their utility is limited by the model's ability to comprehend and follow skill instructions, especially under complex and long-context scenarios, where key instructions are difficult to locate and adhere to. To address this limitation, we propose ParametricSkills, a framework that can convert free-form textual skills into parameters at test time, enabling context-free skill exploitation. Specifically, we first construct a large-scale, high-quality skill library, and synthesize single-turn and multi-turn skill exploitation trajectories built around these skills with OpenCode. Using these data, we then train a hypernetwork that parameterizes both the skill content and the test-time exploitation methodology by receiving textual skills and converting them into LoRA adapters. Experimental results on six complex software engineering (SWE) subtasks demonstrate that, the proposed ParametricSkills averagely outperforms in-context learning by 6.44 points as judged by DeepSeek-V4-Flash, while also achieving significantly higher BERT Score and F1 score, confirming its effectiveness. Beyond performance, we further find that parametric skills, being inherently accumulative, offer a preliminary yet promising avenue toward test-time continual learning.

---


### 193. [OmniDance: Multimodal Driven Dance Video Generation with Large-scale Internet Data](https://arxiv.org/abs/2606.30019)

**<font color=#1a73e8>作者：</font>** Kaixing Yang, Jiashu Zhu, Xulong Tang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Music-driven dance video generation aims to synthesize expressive human motion that is temporally aligned with music while maintaining high visual fidelity. Despite recent progress, existing methods still face two key limitations: the lack of large-scale, high-quality dance video datasets, and the absence of principled frameworks for integrating music as a complementary conditioning signal into Video Generation Foundation Models. To address these limitations, we introduce CIPE-Dance, a large-scale Internet-sourced dance video dataset with choreography-informed text annotations, constructed via a progressive expert pipeline. To the best of our knowledge, CIPE-Dance is the largest dataset for dance video generation to date, comprising 300k high-quality clips over 400 hours and covering diverse dancers, environments, and dance genres. We further propose OmniDance, a framework-level recipe for integrating music into a TI2V foundation model without sacrificing its original controllability or visual fidelity. Motivated by the complementary roles of text as low-frequency semantics and music as high-frequency temporal dynamics, OmniDance co-designs a depth-aware specialization architecture, an anchored easy-to-hard curriculum learning strategy, and a modality-specialized time-dependent CFG strategy, enabling unified TI2V, MI2V, and MTI2V generation. Extensive experiments on CIPE-Dance demonstrate that OmniDance achieves state-of-the-art performance across all three tasks and exhibits robust multimodal integration capability. Project is available at this https URL.

---


### 194. [Uncertainty Estimation in Pathology Foundation Models via Deep Mutual Learning](https://arxiv.org/abs/2606.30020)

**<font color=#1a73e8>作者：</font>** Gbègninougbo Aurel Davy Tchokponhoue, Sevda Öğüt, Ali Idri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology foundation models (PFMs) offer generalizable representations for whole-slide image (WSI) analysis, yet their clinical adoption remains limited. Specifically, their predictions lack reliable confidence estimates, and no single PFM is universally best across tasks, which severely undermines trust in medical settings. To overcome this, we propose $\mathtt{DICE}$, a plug-and-play framework that ensembles $K$ frozen PFMs and models their disagreement as a proxy for uncertainty estimation. To ensure this proxy yields meaningful estimates, we align the ensemble members via deep mutual learning, and theoretically show that this objective upper-bounds the model uncertainty. Additionally, we demonstrate that the ensemble's consensus localizes abnormalities at the patch level without any explicit supervision. We evaluate $\mathtt{DICE}$ on three challenging WSI benchmarks. Notably, our framework provides reliable uncertainty estimates that accurately flag failure-prone cases under in- and out-of-distribution settings, while matching or outperforming SOTA baselines in classification, calibration, and localization. Overall, $\mathtt{DICE}$ takes a crucial step toward translating PFMs into uncertainty-aware decision-support systems.

---


### 195. [MuseBench: Benchmarking Intent-Level Audiovisual Arts Understanding in MLLMs](https://arxiv.org/abs/2606.30026)

**<font color=#1a73e8>作者：</font>** Yuxuan Fan, Gyusik Seo, Jing Hao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audiovisual arts encompass diverse creative disciplines, including cinema, visual arts, stage performance, and game design, where artistic meaning arises from deliberate combinations of visual, auditory, and narrative elements (e.g., fear amplified through claustrophobic framing, or grief conveyed through silence and lingering close-ups). True artistic understanding extends beyond recognizing what is depicted to reasoning about why it is expressed through particular creative choices. Despite the strong progress of multimodal large language models (MLLMs), this critical aspect of artistic understanding remains underexplored, as existing benchmarks largely measure perceptual recognition while overlooking reasoning about creative intent. To address this gap, we introduce Musebench, a comprehensive benchmark designed to evaluate MLLMs on nuanced artistic understanding. It comprises 4,016 questions spanning cinematic arts, static visual arts, stage performing arts, and game arts, distilled from over 10K candidate video essays that pair professional commentary with visual demonstration. To capture the open-ended nature of artistic analysis at scale, the benchmark combines single-select and variable-option multi-select questions. All questions are generated and refined through a four-phase iterative pipeline combining shortcut filtering, adversarial distractors, and expert validation. Comprehensive zero-shot evaluation of 28 state-of-the-art MLLMs reveals that even the best-performing model achieves only 48.29% accuracy, substantially below human expert performance of 87.18%, exposing a significant gap in current models' creative domain expertise.

---


### 196. [Building Multi-Task Agentic LLMs via Two-Phase Distillation](https://arxiv.org/abs/2606.30044)

**<font color=#1a73e8>作者：</font>** Huaijie Wang, Shusheng Xu, Yi Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A key step toward artificial general intelligence is to train models that can perform multiple tasks. In this paper, we study how to build such models by first training separate RL experts for individual tasks and then consolidating them via distillation, as an alternative to directly training a single model on mixed tasks. We show that off-policy distillation degrades in multi-task settings due to the mode-covering nature of forward KL: aggregating data from multiple tasks introduces a large number of behavioral modes that can exceed the student's capacity, forcing it to average across behaviors and leading to degraded performance. In contrast, on-policy distillation is mode-seeking but requires strong initialization. Inspired by these observations, we propose a two-phase approach: off-policy distillation followed by on-policy refinement. Evaluation across conversational agents and text-based games confirms that this two-phase approach matches single-task RL expert performance for each individual task, whereas off-policy or on-policy distillation alone fails to match this performance.

---


### 197. [Illuminating Unified Multimodal Model for Free-form Interleaved Text-Image Generation](https://arxiv.org/abs/2606.30054)

**<font color=#1a73e8>作者：</font>** Chonghuinan Wang, Zhikai Chen, Chunwei Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The advancement of generative AI models capable of producing text and image marks a critical step forward in the realm of multimodal intelligence, particularly for tasks involving the interleaving of both modalities. To advance this intelligence to the next stage, it is crucial for models to autonomously generate free-form interleaved text-image sequences. In this paper, we introduce ILLUME-X, an advanced unified multimodal paradigm that enables high-quality, free-form interleaved text-image generation by improving multimodal data efficiency and stabilizing the multimodal training process. ILLUME-X comprises three key components: (i) an expanded training data pipeline optimized for interleaved text-image generation, (ii) a progressive training strategy with self-adaptive objectives for free-length multimodal token sequences, and (iii) an objective and comprehensive evaluation method ILScore for interleaved text-image sequences. Notably, our ILLUME-X outperforms previous unified models across multiple interleaved text-image generation tasks like style transfer, image decomposition and storytelling.

---


### 198. [From Failure Taxonomy to Intervention: A Diagnostic Methodology for Industry-Scale AVLM in Video and Live-Streaming Platform Moderation](https://arxiv.org/abs/2606.30059)

**<font color=#1a73e8>作者：</font>** Shuchang Ye, Jinqiang Yu, Zhujun Xiao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industry-scale video and live-streaming moderation imposes requirements that are difficult to satisfy with generic pretrained public models or external APIs, including adaptation to platform-specific data distributions, policy-specific objectives, and product-level safety constraints. As a result, platforms must undertake internal model development, naturally turning to shared public research for guidance. However, existing multimodal foundation-model studies primarily report architectures, training recipes, data scaling strategies, and benchmark results, but provide less systematic guidance on how failures should be localized and translated into targeted model-development interventions. Interventions are essential because deployment failures are rarely self-explanatory. Similar failures can originate from different causes. Without targeted interventions, improvement reduces to heuristic trial-and-error, where benchmark improvements are weakly attributable, and failures are difficult to trace to their underlying causes. To address this gap, we present a diagnostic methodology for industry-scale Audio-Visual-Language Models AVLM development. The methodology maps model failures into a taxonomy of observable failure signatures and links each class of failure to an intervention space. We instantiate this methodology across the development and alignment lifecycle of an AVLM foundation model for a large-scale video and live-streaming platform. The resulting system supports over 100 regions and is designed for noisy, ambiguous, and highly diverse content drawn from global platform traffic.

---


### 199. [Little Brains, Big Feats: Exploring Compact Language Models](https://arxiv.org/abs/2606.30062)

**<font color=#1a73e8>作者：</font>** Dari Baturova, Elena Bruches, Ivan Chernov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While large language models have been dominating the research landscape recently, small language models remain highly relevant across various domains; yet, they receive far less attention. In this study, we investigate how smaller language models perform during the generation stage within a Retrieval-Augmented Generation (RAG) system. To benchmark these models effectively, we utilised both open-source and proprietary datasets covering diverse subject areas and question types. Our findings demonstrate that a RAG system with small language models can be executed directly on-device without requiring any GPU hardware within a reasonable time. The experimental code and links to the supplementary materials can be accessed through the GitHub repository: this https URL.

---


### 200. [Online Data Selection for Instruction Tuning via Gaussian Processes](https://arxiv.org/abs/2606.30077)

**<font color=#1a73e8>作者：</font>** Jun Wang, Quoc Phong Nguyen, Julien Monteil 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With Large Language Model (LLM) pre-training and fine-tuning shifting its focus from data volume to data quality, quality data selection has emerged as a critical research topic. Existing online data selection methods for LLM training are typically "batch-constrained", limiting optimization to local utility within random batches. To overcome this, we propose GAIA (Global Adaptive Instruction tuning via GAussian processes), a framework that formulates data valuation as a global estimation process. GAIA employs Gaussian Process regression to model continuous utility manifolds across the semantic space, utilizing an adaptive strategy fusion mechanism to dynamically prioritize high-utility samples. By casting the strategy-posterior update as an instance of the classical fixed-share Hedge framework for tracking the best expert, we inherit a dynamic-regret guarantee that characterizes GAIA's robustness under non-stationary quality scores during training. Empirical evaluations on three datasets demonstrate that GAIA significantly outperforms state-of-the-art baselines like \greats, establishing our method as a scalable and robust solution for efficient instruction tuning.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-247](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
