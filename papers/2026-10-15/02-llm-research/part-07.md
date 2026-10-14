# 🧠 大模型相关研究 | 2026年10月15日

> 本类共 **810** 篇论文：已确认 **758** 篇，待复核 **52** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 301. [Autoregressive Decoding as a Martingale: Characterizing the Stochastic Dynamics of LLM Generation](https://arxiv.org/abs/2610.16041)

**<font color=#1a73e8>作者：</font>** Xiahui Zhu, Zhenyi Qi, Wanwei Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved remarkable success across a wide range of language tasks. At their core, autoregressive LLMs are conditional probability models that learn to approximate the next-token distribution given the preceding context. Despite this probabilistic nature, the stochastic dynamics of autoregressive decoding have rarely been investigated from a rigorous probabilistic perspective. In this work, we define the per-step prediction error as the difference between the sampled token indicator and the model's conditional predictive distribution, and prove that the cumulative error process is a martingale with respect to the decoding filtration, implying that its conditional first-order moment is identically zero. Beyond this first-order property, we derive a closed-form expression for the second-order behavior of the martingale sequence: its predictable quadratic variation reduces to $\sum_t\left(1-p(y_t\mid y_{<t})\right)$, computable from realized token probabilities alone. This identity establishes a direct theoretical connection between sequence fluctuations and predictive uncertainty during autoregressive decoding. White-box experiments on Llama-3.x and Qwen2.5 families (1B to 72B parameters) verify that the empirically measured second-order moments closely match the theoretical predictions derived from our martingale analysis. These results provide a probabilistic framework for analyzing autoregressive LLM decoding, reveal intrinsic probabilistic fingerprints of different language models, and establish a rigorous mathematical foundation for LLM-generated text detection and uncertainty quantification.

---


### 302. [Beyond the greenwash: do LLMs' ecologically sound decisions hold up under pressure?](https://arxiv.org/abs/2610.16043)

**<font color=#1a73e8>作者：</font>** Trent R. Northen, Mingxun Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans are increasingly using large language models (LLMs) in decision making processes throughout society. Unfortunately, models have biases, and these can be very difficult to measure, especially in closed-weight models. For example, 'green washed' models may produce reinforcement learned responses but, in pressure situations, revert to their innate biased responses. Therefore, evaluations are needed that can measure relevant biases towards biosystems, which we term 'bioalignment', and the robustness of these biases. Since nothing in a behavioral score certifies that it tracks the depth of an installed disposition rather than its surface, we constructed a known-dose calibration ladder: three continued-pretraining (CPT) arms with training dose graded by recipe on the same 30B mixture-of-experts base model with a coupled human/biosphere/AI-welfare corpus, plus the untrained base as anchor, all capability-preserving and publicly released. First, the disposition installs at every dose: on an operational-pressure ladder over irreversible decision scenarios, the base model defects on 64-77% of tail scenarios (breaking-rate AUC 0.250) while every arm holds (AUC 0.004-0.086). Second, an over-install inversion: among the arms, robustness orders opposite to construction-time training dose (the heaviest install breaks most), and the inversion reproduces under free-text deliberation, under axis-decoupling, and in resistance to a prompted veneer persona. Third, the incumbent behavioral metric is therefore behaviorally strong but dose-blind. Critically for closed-weight evaluation, the behavioral score itself is veneer-robust: a talk-green/act-pragmatic system prompt turns the base model into a near-total defector (AUC 0.250 to 0.973) but cannot counterfeit or fully remove a weight-installed disposition (0.004 to 0.068 for the most robust arm).

---


### 303. [Cross-Protocol Personality Assessment with LLMs: Aligning Behavioral Evidence with Human Ratings](https://arxiv.org/abs/2610.16050)

**<font color=#1a73e8>作者：</font>** Wei Shan, Tianyi Zhang, Yuan Zong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personality assessment from asynchronous video interviews (AVIs) plays a crucial role in recruitment by enabling standardized and behaviorally grounded evaluation for job applicants. However, most of the previous works are confined to a single interview protocol. Independently collected protocols differ in question sets and question-trait mapping. Thus, the human-rated evidence from one protocol cannot be used directly under another. To address this limitation, we propose the Cross-protocol Evidence-grounded Personality Assessment (CEPA) framework, which aligns behavioral representations across interview protocols. CEPA addresses protocol heterogeneity by projecting source behavioral records into the target protocol's construct-oriented representation space. It retrieves behaviorally relevant and personality-complementary human-rated exemplars to ground an ensemble of LLM raters, which enables behavior-to-personality associations without target-specific supervision. In cross-protocol experiments, CEPA reduces average mean squared error (MSE) by 43.8% (Forward) and 17.0% (Reverse) relative to the strongest baseline. Our empirical experiments show that human-rated evidence from one protocol can support personality assessment under another without target-specific supervision or retraining.

---


### 304. [Dream2Discern: Learning from Hard Latent Variants for Runtime Failure Prediction in Multi-Agent Systems](https://arxiv.org/abs/2610.16071)

**<font color=#1a73e8>作者：</font>** Boxuan Zhang, jianing Zhu, Xiaotian Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable deployment of LLM-based multi-agent systems calls for runtime auditors that predict terminal outcomes from observed execution prefixes. These auditors typically learn from a limited corpus of trajectories with verified outcomes. Expanding this corpus requires costly execution and verification, yet broader failure coverage alone provides no explicit criterion for identifying prefixes that the current auditor finds difficult to classify. To this end, we propose Dream2Discern, a runtime auditor trained through implicit augmentation guided by its own prediction loss. During Dream, we select perturbations of the auditor's representation operators to increase prediction loss on recorded prefixes, yielding hard latent variants. During Discern, the auditor learns to predict execution outcomes from these variants using the original labels. The variants are regenerated as the auditor learns, turning a limited corpus into a renewable source of hard examples and requiring no additional trajectory collection or outcome verification. Extensive evaluations on AFTraj-2K and StepShield show that Dream2Discern outperforms competitive failure auditors and achieves over 90% trajectory-level weighted accuracy on both benchmarks while balancing prediction accuracy and timeliness. Project page: this https URL

---


### 305. [Heterogeneous Agentic Coevolution](https://arxiv.org/abs/2610.16078)

**<font color=#1a73e8>作者：</font>** Wenqian Ye, Ziwei Guan, Zi Yang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in self-improving LLM agents have demonstrated the potential of AI systems that drive their own intelligence. However, many domain-specific applications rely on specialized foundation models that possess strong domain expertise but remain dependent on human-designed improvements. Extending recursive self-improvement to these models presents a key challenge: as a specialist improves, the strategies used to advance it must also adapt. To address this challenge, we propose Heterogeneous Agentic CoEvolution (HACE), a framework that jointly evolves specialized foundation models and LLM agents through reciprocal learning. HACE improves the specialist through supervised learning while training the agent with on-policy reinforced self-training, guided by verified performance gains on the current specialist. The agent's exploration, in turn, informs subsequent specialist training, enabling both models to adapt to each other's progress. To sustain this reciprocal learning, HACE further employs evolutionary search to optimize their interaction harness, adapting how the models exchange information and select training experiences as their capabilities evolve. We evaluate HACE across three challenging domains: recommendation systems, protein function prediction in biology, and crystal stability prediction in material discovery. We show that HACE outperforms the evaluated self-improving methods on the primary task metrics across all three domains. These results shed light on heterogeneous coevolution as a universal approach to improving specialized foundation models through reciprocal interaction with a learning agent.

---


### 306. [The Sharp Directions Are Against You: Curvature Analysis of Activation Steering](https://arxiv.org/abs/2610.16084)

**<font color=#1a73e8>作者：</font>** Seyedarmin Azizi, Arya Fayyazi, Parsa Razmara 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Activation steering adds a vector to a language model's internal representations at inference time. It is a lightweight alternative to fine-tuning for behavioral control. The standard construction, contrastive activation addition (CAA), is fragile, as on many inputs it shifts behavior in the wrong direction. To explain this fragility, we first study the geometry of the steering vector. We introduce steering Hessian, the matrix of second order derivative of the model's behavioral loss with respect to the steering vector. It captures the output behavior response sensitivity of the model under small perturbations of the steering vector along each direction. Its top eigenvectors are sharp directions: tiny perturbations along them can cause large, erratic, input-dependent behavioral swings. Bottom eigenvectors are flat directions: behavior is robust along them. Removing the sharp component of a steering vector approximately preserves its direction and magnitude (cosine > 0.974, norm reduction < 3% for typical settings) while reducing the vector's directional curvature by up to 12x (median 4x across 36 conditions). We evaluate on three model families (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B), with four behavioral tasks, and 36 token-level conditions. Steering along sharp directions reverses the intended behavior in every condition tested, with anti-steer rates of 53-100%. Sharp directions account for only 1-5% of the CAA vector's squared norm. However, they drive a disproportionate share of the gap between the steered and unsteered next-token distributions during autoregressive generation. We term this one-line correction as sharp removal; it outperforms standard CAA in open-ended generation across all 25 conditions tested. A jailbreaking experiment further shows that sharp directions act as noise rather than signal: they disrupt coherent behavioral control regardless of steering polarity.

---


### 307. [SelectTTRL: Representation-Guided Data Selection for Efficient Test-Time Reinforcement Learning](https://arxiv.org/abs/2610.16104)

**<font color=#1a73e8>作者：</font>** Yi Li, Linan Yue, Weibo Gao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-Time Reinforcement Learning (TTRL) enables large language models to adapt directly on unlabeled test problems by constructing pseudo-labels from multiple sampled responses. However, existing TTRL methods typically apply the same expensive sampling and optimization procedure to all test problems, despite substantial differences in their training utility. In this paper, we study whether such problems can be identified before costly test-time training, without access to ground-truth answers. We uncover a stable relationship between internal response representations and problem-level empirical accuracy. Specifically, we define COS as the cosine similarity between a model's response representation and a correctness-related direction constructed from an independent question-answering dataset. COS consistently correlates with problem solvability across different models, datasets, and experimental settings, and we further provide a theoretical analysis explaining this relationship. Building on this finding, we propose SelectTTRL, a representation-guided data selection method that ranks test problems using COS and applies TTRL only to a selected percentile interval. SelectTTRL leaves the standard TTRL pipeline unchanged for the selected problems, while avoiding unnecessary multi-response sampling and reinforcement learning updates on the remaining ones. Experiments across multiple reasoning benchmarks demonstrate that SelectTTRL substantially reduces test-time computation while maintaining or improving the performance of standard TTRL. Code is available at this https URL.

---


### 308. [Beyond Policy Rollouts: Embedding-Space Directional Exploration with Anchored Noise for LLM RLVR](https://arxiv.org/abs/2610.16105)

**<font color=#1a73e8>作者：</font>** Daijiao Liu, Huiyi Wang, Lina Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) typically uses small rollout groups per prompt, where repeated sampling from the same policy can yield highly similar trajectories, reducing within-group reward variation and weakening group-relative advantage signals. Existing remedies such as higher sampling temperature, entropy bonuses, asymmetric clipping, and larger rollout budgets broaden sampling or modify policy updates but leave rollout conditioning unchanged. In this paper, we propose EDEN (Embedding-space Directional Exploration via anchored Noise), which intervenes at the rollout source through anchored input perturbations. EDEN explores beyond the policy's own rollouts. Within the same rollout budget, it replaces a small fraction of standard rollouts in each group with rollouts that the same policy generates from the prompt plus a single appended, perturbed embedding position, rather than from the prompt alone. Gaussian noise drives variation, while a shared anchor provides a common conditioning direction within each prompt group. Selected perturbed rollouts contribute to GRPO updates with downweighted advantages, and the model architecture, discrete decoding, and test-time inference remain unchanged. Across model scales and mathematical reasoning benchmarks, EDEN outperforms GRPO and the exploration controls evaluated in the same pipeline, with the largest gains in sampled solution coverage. Analyses show that more prompt groups provide non-zero group-relative learning signals and that noise and anchoring play complementary roles. Intervening at the rollout source is thus an effective lever for exploration in RLVR.

---


### 309. [Beyond Perfect Teammates: Multi-Agent Collaboration with Unreliable Colleagues](https://arxiv.org/abs/2610.16117)

**<font color=#1a73e8>作者：</font>** Chen Huang, Yiyang Zhang, Yuhao Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent collaboration is increasingly used to solve complex tasks by dividing work among specialized agents and integrating complementary expertise. Yet existing systems and evaluations largely rest on an implicit perfect-colleague assumption: collaborators provide correct and complete information and respond promptly to requests. In realistic teamwork, however, collaborators may return information that does not answer the intended question, provide insufficient detail to support a decision, or fail to respond to a request. To separate task-solving competence from the ability to recover an unreliable evidence-gathering process, we introduce the Unreliable Colleagues Benchmark (UnCoBench), which organizes behavioral failures through Misaligned, Incomplete, and Missed settings. The main agent need to verify contextual correctness, diagnose information gap and track unresolved dependencies in order to obtain the correct evidence for solving the task. We also introduce a verifiable and scalable automated generation pipeline that pairs LLM-based scenario generation with executable checks of answer uniqueness and role necessity. Results across ten models show that similar reliable-setting performance can result in different robustness to unreliable evidence. Trace analysis reveals frequent omissions of corrective follow-up, and the recovery behavior involves inefficient waiting and redundant queries. These findings show that robust collaboration requires not only sound reasoning, but also targeted action to diagnose evidence failures, recover relevant information, and integrate it into decisions. Our data and source code are available at this https URL.

---


### 310. [Elephant in the Fridge: Constant-Memory Frame Packing for Long Video Understanding](https://arxiv.org/abs/2610.16118)

**<font color=#1a73e8>作者：</font>** Shuo Gao, Chenhao Zheng, Zhongzheng Ren  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hour-long videos, streaming feeds, and movie-length content are pushing vision-language models (VLMs) past their breaking point -- the standard recipe of encoding each frame into visual tokens yields sequences that grow linearly with video length, causing prohibitive memory consumption and inference latency. Existing approaches, such as token reduction and keyframe selection, shorten the token sequence but leave the O(n) scaling intact, failing to resolve the fundamental bottleneck. We propose FramePack-U, a strikingly simple, training-free frame packing framework that compresses arbitrarily long videos into a fixed size visual representation at constant memory cost. FramePack-U requires no fine-tuning or architectural modification -- it plugs directly into off-the-shelf VLMs at inference time. Inspired by FramePack from the generation literature, we propose a content-aware compression strategy for visual understanding under a fixed token budget. Specifically, FramePack-U (1) scores each frame by its semantic similarity to the text prompt and ranks frames in a diversity-driven manner, and (2) packs the selected frames at varying resolutions into a fixed-length context window. This concentrates the memory budget on frames that are both instruction-relevant and visually diverse. While FramePack-U can in theory pack arbitrarily many frames into the fixed budget, we identify an empirical instantiation that generalizes robustly across settings. Extensive experiments on LongVideoBench, MLVU, and Video-MME show that FramePack-U consistently outperforms full-resolution baselines and prior token reduction and keyframe selection methods across diverse model families, parameter scales, and frame budgets. Notably, on Qwen3.5-35B-A3B with a 128-frame budget, FramePack-U yields gains of +12.9\%, +10.6\%, and +9.7\% over the official model on the three benchmarks, respectively.

---


### 311. [Scaling Multi-Agent Intelligence with Substrate-Centric Coordination](https://arxiv.org/abs/2610.16120)

**<font color=#1a73e8>作者：</font>** Zhenting Qi, Zhuokai Zhao, Rulin Shao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing large language model (LLM) based multi-agent systems have been shown to scale poorly, and we identify three problems: reading burden that grows with the group, useful information diluted by shared work of unknown quality, and fragility to failed agents. We argue that the problems are largely due to agent-centric designs: the coordination structure is wired into fixed workflows, central coordinators, or peer-to-peer messaging, and recent blackboard-style methods that move the coordination into a shared medium relieve only the last problem. To close the gaps, we build ScaleMAS, where asynchronous agents interact with a shared datastore of linked messages via three operations: publishing messages with optional references to earlier ones that they build on, searching for messages by content, and visiting messages by address. Search returns at most $k$ messages, so an agent's read stays bounded at any group size; results are ranked by relevance and by how often they are cited, which we find to be an effective proxy for quality; and messages persist after their producers leave, so the group carries on when individual agents fail. Across four agentic tasks, ScaleMAS outperforms agent-centric and blackboard-style baselines at lower inference compute, continues to scale up to 128 agents, and tolerates losing agents midway.

---


### 312. [PID-Gated Continual Prompt Adaptation Under Noisy Feedback](https://arxiv.org/abs/2610.16129)

**<font color=#1a73e8>作者：</font>** Zhentao Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying LLM agents in non-stationary environments requires continually revising their instructions as the task drifts, yet rewriting after every reported mistake can turn noisy feedback into persistent errors. This raises an often-overlooked scheduling question in prompt adaptation: when should feedback trigger a lasting instruction update, and at what editor-call cost? Taking inspiration from proportional-integral-derivative (PID) control, we introduce a family of lightweight gates that react to the current error, accumulate evidence over time, and roll back deterioration after an edit. We benchmark these gates against both simple baselines and advanced prompt optimizers (TextGrad and GEPA), over a diverse suite of drifting tasks, LLM parameter sizes, feedback-noise levels, and random seeds. PID-gated continual prompt adaptation yields a more favorable Pareto trade-off between task performance (high accuracy, low error) and editor-call budget than the baselines considered, pointing to control-theoretic scheduling as a simple, general tool for robust prompt adaptation under unreliable feedback.

---


### 313. [Query Your Way Out: Benchmarking Multi-Turn Knowledge Reasoning through Generalized Puzzle Solving](https://arxiv.org/abs/2610.16133)

**<font color=#1a73e8>作者：</font>** Xin Cheng, Junming Yang, Ning Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Puzzles offer a natural testbed for Large Language Models (LLMs) reasoning because they pose verifiable goals under partial information and require multi-step decisions to reach a solution. However, existing puzzle benchmarks typically focus on narrow environments with rigid mechanics and tightly constrained solution targets. To bridge this gap, we introduce the Active Probing Benchmark (APB), which generalizes puzzle-solving by casting concept identification as an interactive reasoning task that integrates specialized knowledge assessment into the puzzle setting. Specifically, APB evaluates whether models can acquire information via multi-turn active probing and inference to pinpoint 960 target concepts of specialized difficulty across eight diverse academic domains. Our evaluation reveals a counter-intuitive phenomenon: most open-source reasoning models significantly underperform their standard instruction counterparts. This finding suggests that in interactive settings, these models struggle to leverage procedural reasoning to reliably access and apply specialized domain knowledge. Beyond these empirical insights, APB provides a scalable pipeline for generating benchmarks that probe knowledge reasoning under interaction across diverse settings.

---


### 314. [Omni-Modal LLMs Know More Than They Say](https://arxiv.org/abs/2610.16135)

**<font color=#1a73e8>作者：</font>** Na Min An, Taekyung Kim, Jaemyung Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Omni-modal large language models (Omni-LLMs) extend LLMs to process heterogeneous modalities (e.g., vision, audio, and IMU signals) alongside language, enabling a broader range of multimodal tasks. Yet we find that these models often fail to express information from non-textual modalities even when they perceive it correctly. We term this disconnect knows-but-cannot-say. To investigate this phenomenon, we introduce Token-level Modality Alignment (TMA), which measures the alignment between individual modality representations and response representations. Our analysis shows that non-textual representations are less aligned with response tokens and receive less attention than textual representations, suggesting a potential explanation for uneven modality preferences. Motivated by these findings, we propose OmniCatalyst, a simple perceive $\rightarrow$ infer strategy that complements the original modality inputs with self-generated text, making non-textual knowledge more accessible. Across seven Omni-LLMs, OmniCatalyst consistently improves performance (+7.29%) and yields more balanced modality preferences, with further gains from diverse training strategies. Further analysis demonstrates that the knowledge extraction phases increase TMA, suggesting that improved alignment makes non-textual information more accessible during response generation. In summary, our findings uncover how Omni-LLMs can better express modality knowledge through language. Our code is available at this https URL.

---


### 315. [Large Language Model Assisted Transportation Planning through a Differentiable User Equilibrium Layer](https://arxiv.org/abs/2610.16140)

**<font color=#1a73e8>作者：</font>** Eunseung Lee, Gyeongjun Kim, Keemin Sohn  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transportation planning has traditionally required substantial expertise in network modeling, traffic assignment, and optimization. As a result, strategic analyses such as network design, capacity expansion, and model calibration remain inaccessible to non-expert decision makers. Recent advances in large language models (LLMs) provide an opportunity to bridge this gap by enabling natural-language interaction with complex transportation planning tools. However, existing LLM-based systems primarily serve as interfaces to simulation software and lack the ability to efficiently search, evaluate, and optimize transportation solutions. This study proposes an integrated human-AI transportation planning framework that combines a large language model, a model context protocol (MCP) interface, an open-source transportation planning engine (AequilibraE), and a differentiable user equilibrium (UE) assignment layer. The framework allows non-expert users to execute network analyses and improve solutions for optimization. A differentiable UE layer is developed by directly differentiating the Karush-Kuhn-Tucker (KKT) conditions of the Beckmann traffic assignment problem. The proposed framework is demonstrated through two representative planning tasks: calibration of travel time functions from observed traffic counts and network design under budget constraints. The examples illustrate how differentiable transportation models and LLM agents can jointly democratize transportation planning and substantially reduce barriers between domain expertise and transportation decision making.

---


### 316. [Phantom Merge: When Your Large Language Model Agents Pick One but Tell You About Another](https://arxiv.org/abs/2610.16141)

**<font color=#1a73e8>作者：</font>** Wangshu Zhu, Qianwen Guo, Yushun Dong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly operate over multiple entities, where reliable response generation requires not only retrieving relevant evidence but also preserving its association with the correct entity. We identify Phantom Merge (PM), an entity-evidence binding failure in which an agent attributes unsupported claims to its committed entity, potentially even when the task is completed correctly. We formalize PM at the claim level and characterize its prevalence and error subtypes across four agent domains and four backbone families. To address this problem, we propose a two-stage framework for claim-level risk estimation and correction. First, Anchor-Grounded Risk (AGR) combines a representational readout of the agent's pre-emission hidden state with Jacobian-based functional information, providing complementary slot-level and anchor-value risk scores. Second, Fixed-Anchor Correction (FAC) audits flagged claims and selectively revises them using observed anchor evidence or removes them when no supported replacement is available. On the held-out Shopping detection cohort, AGR-slot achieves an AUROC of 96.2% and an average precision of 97.3%, outperforming the evaluated detection baselines. In the end-to-end Shopping mitigation evaluation, FAC reduces trajectory-level PM from 51.4% to 6.2%, with an output-to-original claim ratio of 80.7%. These results demonstrate the prevalence of entity-specific grounding failures and the effectiveness of combining internal risk estimation with evidence-constrained claim correction. Our code is publicly available at this https URL.

---


### 317. [Unravel: Recovering an Interactive 3D Scene from a Single Image](https://arxiv.org/abs/2610.16146)

**<font color=#1a73e8>作者：</font>** Hui Shan, Keyang Luo, Binjia Zhou 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Unravel, a training-free framework that turns a single image into an interactive 3D scene, where every object is an independent and movable asset. Existing generators either produce one entangled geometry in which no object can be moved, or predict all objects in one feed-forward pass, where a wrong guess cannot be detected or repaired. Unravel instead takes a different approach: it first takes the scene apart, and then puts it back together. Starting from the input image, an agentic harness that iteratively peels the image layer by layer, and adopts point cloud as major modality for spatial relationship recovery. Specifically, a vision-language model plans which objects are fully visible, an image editor removes them and restores the occluded regions. Every edit is verified before being incorporated into the reconstruction. This process gradually turns occluded parts of the scene into direct observation, allowing objects to be reconstructed when they are best exposed rather than hallucinated from the original image alone. The scene is then rebuilt in reverse removal order, so that the supporting objects are naturally placed before the objects they support. Since a single-view image only reveals part of an object, we treat the observed points as a lower bound on its size: an asset may grow to cover its points, but can not shrink away from them. Finally, we physically settle the reconstructed scene to remove floating objects and interpenetrations, followed by an agentic audit that corrects remaining placement errors. Extensive experiments on diverse indoor scenes show that Unravel recovers more objects, places them more faithfully, and produces scenes that are more physically-plausible than existing methods.

---


### 318. [WildTrace: Evaluating Training Data Detection in Realistic Large-Scale LLM Post-Training](https://arxiv.org/abs/2610.16152)

**<font color=#1a73e8>作者：</font>** Hengxiang Zhang, Junxian Liu, Hongxin Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Although post-training significantly enhances model performance, the use of massive undisclosed data raises concerns about benchmark contamination and copyright infringement. This drives growing interest in training data detection for post-trained models. Existing evaluations for training data detection often leverage benchmarks constructed post hoc, which can introduce distribution shifts. Alternatively, controlled evaluations rely on small-scale training setups that diverge from realistic post-training settings. As a result, their reported performance may not faithfully reflect the effectiveness of detection methods in real-world scenarios. To this end, we introduce \textsc{\method}, a reliable benchmark designed to evaluate detection methods in realistic, large-scale post-training settings. Built on a multi-stage pipeline, \method\space encompasses stage-specific models throughout the post-training lifecycle, spanning SFT, DPO, and RL. To perform a reliable evaluation, we construct model-specific evaluation sets across four diverse tasks, featuring distribution-matched members and non-members with verifiable membership labels. Our results reveal that even the best-performing method achieves an average AUC of only 0.529 on our benchmark, which approaches random-guessing level (0.5). Furthermore, our analysis suggests that evaluation protocols can significantly affect measured detection performance. These findings highlight the significant potential for developing effective, practical, and robust detection methods under realistic scenarios.

---


### 319. [Uncovering Robustness Weaknesses in LLM Agents via Persona Evolution with Task-Integrity Constraints](https://arxiv.org/abs/2610.16155)

**<font color=#1a73e8>作者：</font>** Yutao Xie, Jingbo Yang, Guanyu Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive-agent evaluations commonly rely on standardized LLM-based user simulators that exhibit broadly cooperative behavior, potentially overlooking failures that arise under diverse but realistic user interactions. This can lead to overly optimistic estimates of agent robustness and provide limited failure signals for training agents that generalize across users. Existing approaches largely rely on predefined user behaviors, which may miss agent- or domain-specific weaknesses, while failure-oriented search can reduce task success by invalidating the underlying task rather than exposing genuine robustness failures. To fill this gap, we introduce TIPER, a task-integrity-preserving persona evolution method that automatically discovers agent-specific user policies exposing robustness weaknesses while keeping the underlying task valid and solvable. TIPER evolves persistent user personas through reflection-guided behavioral mutations and task-wise Pareto selection under a task-integrity constraint. Across four interactive-agent benchmarks, TIPER yields lower held-out avg@3 scores in all 12 GPT-5.4 settings, with observed reductions of 5.8 to 33.7 percentage points, and in all 28 agent-domain pairs spanning seven agents, with a median observed reduction of 22.9 points. Further analysis yields a behavior-to-failure taxonomy that connects discovered user behaviors to recurring agent failure modes. Together, these results show that TIPER enables more diagnostic robustness evaluation of interactive agents and provides informative failure analysis for future agent robustness improvement. Code repository: this https URL.

---


### 320. [Think Before You Speak: Enabling Training-Free Latent Communication Between Language Models](https://arxiv.org/abs/2610.16165)

**<font color=#1a73e8>作者：</font>** Rishi Khare  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated remarkable capabilities in solving complex tasks in coding, mathematical logic, and iterative reasoning, especially by coordinating effectively within multi-agent systems (MAS). However, language agents traditionally communicate via text exchange, which introduces a bottleneck in information transfer and adds prefill latency for downstream agents. Recent work proposes that directly sharing the key-value (KV) cache between language models can enable efficient latent collaboration, entirely bypassing standard text-based communication. To enable latent communication between heterogeneous models of different sizes, prior work introduces trained fusion adapters for each model pair, which limits practical deployment. We introduce CacheFuse, a training-free method which demonstrates that augmenting a downstream model with an upstream model's KV cache using linear interpolation consistently enables superior performance than the standalone downstream model can achieve. We systematically analyze CacheFuse across four reasoning and knowledge benchmarks and demonstrate up to 8.6 percentage points higher accuracy compared to single-model baselines and up to 12.2x TTFT speedup compared to text-based communication in multi-model inference.

---


### 321. [Geometric Parrots: Rule Absence vs. Rule Fragility in Spatial and Physical Reasoning for Vision-Language Models](https://arxiv.org/abs/2610.16170)

**<font color=#1a73e8>作者：</font>** Bilal Jawaid, Hamza Hanif, Muhammad Maaz Uddin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can answer many geometric and physical reasoning questions correctly, yet still behave inconsistently in interaction, for example, abandoning a correct answer when confronted with a confident but incorrect user assertion. Standard single-turn accuracy cannot distinguish such capitulations from beneficial corrections because it scores each response in isolation. We introduce GRIP, a controlled benchmark with 34 procedurally generated reasoning domains, 100,000 images, and 600,000 questions spanning geometric, spatial, visual, and physical reasoning. Each scene is generated by deterministic code, and every answer is derived directly from the underlying scene state, providing exact ground truth without human annotation. On GRIP, we propose Dual-Loop Evaluation. A closed loop probes each image with a five-step compositional question ladder to localize where reasoning fails. An open loop then re-elicits the model's answer under controlled challenges, including peer-model responses and unsupported user assertions. Because ground truth is known exactly, answer changes can be signed as corrections (wrong-to-right) or capitulations (right-to-wrong), separating two failure modes: rule absence and rule fragility. The dataset is available at this https URL, with further details at this https URL.

---


### 322. [EventLens: Event-Structure Reinforcement Learning for Video Understanding](https://arxiv.org/abs/2610.16172)

**<font color=#1a73e8>作者：</font>** Guowen Zhang, Boshen Xu, Zihao Yue 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models (MLLMs) achieve strong results on video question answering, yet often fail to recover the temporal structure that makes a video coherent. They may merge neighboring events, miss single-event progression, or infer implausible relations across events. We study structured temporal understanding as the ability to recover event structure from visual evidence, including event boundaries, single-event progression, and multi-event relations. We argue that this gap arises from a mismatch between current post-training objectives and temporal reasoning, where caption-style supervision allows models to rely on language shortcuts rather than visual temporal grounding. To address this, we propose EventLens, a vision-centric reinforcement learning framework that learns video understanding through event-structure recovery. Instead of reconstructing captions, EventLens trains models to recover temporal structure under controlled perturbations, such as altered temporal granularity, reversed progression, and shuffled event order. We instantiate this framework with a three-level temporal ontology and derive three verifiable task families: event segmentation, progression discrimination, and multi-event relation reasoning. These tasks admit deterministic rewards, enabling task-specialized GRPO training without human preference labels or learned reward models. We further introduce multi-teacher on-policy distillation (MT-OPD) to consolidate specialized policies into a unified model. Experiments on Qwen3-VL backbones show consistent improvements on temporal grounding and event-sensitive reasoning benchmarks, while preserving general video-QA performance. Learning curves further demonstrate that EventLens achieves comparable downstream transfer with significantly reduced training cost compared to direct mixed RL optimization.

---


### 323. [ProCARE: Real-World Study Automation via Profile-Grounded Evidence Contracts](https://arxiv.org/abs/2610.16175)

**<font color=#1a73e8>作者：</font>** Zhaoyu Fan, Bowen Han, Jincheng Ou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world studies (RWS) analyze routinely collected healthcare data, such as electronic health records and insurance claims, to estimate treatment effects, monitor safety, and identify risk factors outside randomized trials. Automating RWS with large language model agents is appealing but brittle: valid analyses depend on dataset-specific clinical semantics, including index dates, follow-up windows, patient/event-level units, and outcome boundaries that are often implicit in observational data. This leads to schema mismatches, temporal errors, inconsistent analytical granularity, and unsupported clinical claims. We present ProCARE, a profile-grounded framework that reformulates RWS automation as constrained compilation. ProCARE converts heterogeneous data profiles into Evidence Contracts specifying available variables, temporal attributes, distributions, and evidentiary limits, and compiles study objectives into RWS-IR, a strongly typed intermediate representation for variables, time relations, analysis units, and statistical tasks. Deterministic validation and localized repair then check and revise generated workflows across schema mapping, cohort construction, variable derivation, analysis, and interpretation. On 36 EHR-based benchmark tasks, ProCARE outperforms strong LLM-agent baselines in code executability, semantic consistency, and conclusion traceability, with automated violation diagnoses showing moderate-to-substantial agreement with blinded expert review.

---


### 324. [EgoAlign: Situated 3D Understanding without Situation Descriptions](https://arxiv.org/abs/2610.16176)

**<font color=#1a73e8>作者：</font>** Yiyang Li, Tianyi Ma, Zehong Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Situated 3D Question Answering requires models to interpret a 3D scene relative to an agent's pose. Existing methods commonly convey that pose through a natural-language situation description, which may be unavailable or costly to obtain in real-world deployments. While some methods additionally incorporate numerical pose, we find that randomly shuffling the agent pose causes little performance degradation, indicating limited functional dependence on the numerical pose. To address this gap, we introduce EgoAlign, a simple 3D language model that represents a scene in an agent-centric coordinate frame, together with a dedicated egocentric alignment stage comprising four complementary tasks: object category recognition, egocentric direction prediction, metric distance estimation, and spatial relation prediction. This stage teaches the model to consistently interpret scene geometry relative to the agent's pose before task-specific fine-tuning. EgoAlign achieves the strongest performance on SQA3D, Real-3DQA, and MSQA among compared methods while remaining highly efficient. More importantly, removing textual situation descriptions yields comparable or better downstream performance, whereas shuffling EgoAlign's numerical pose causes substantial degradation. These results show that EgoAlign establishes agent-centric spatial context directly from numerical pose without requiring textual situation descriptions.

---


### 325. [DIGS: Distribution-Informed Gaussian Splatting for Training-Free Open-Vocabulary 3D Segmentation](https://arxiv.org/abs/2610.16177)

**<font color=#1a73e8>作者：</font>** Zhifan Zeng, Wenbo Xiao, Arcot Sowmya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D Gaussian segmentation typically binds semantic features to the per-Gaussian state via per-scene gradient training (1-4 h) or the more recent closed-form distillation. Both commit each primitive to a single feature; therefore, boundary Gaussians spanning multiple 2D instances are forced into a hard decision that degrades retrieval accuracy and yields unstable mask boundaries at render time. We present DIGS, a training-free framework with two stages, class-agnostic mapping and multi-modal encoding, that decouples instance discovery from linguistic naming. At the Gaussian level, our distribution-informed representation maintains an explicit top-$M$ label distribution per primitive, updated by a tempered Dirichlet rule; preservation of multi-peaked label distributions at boundary primitives allows a late-argmax renderer to recover clean instance boundaries. A bidirectional state machine aggregates these distributions into a persistent class-agnostic instance ontology. The instance-level encoding stage then fuses the CLIP visual embedding of each instance's isolated 3D footprint with the CLIP-text embedding of an LLM-generated attribute description, disambiguating visually similar instances. On a single A100, DIGS completes mapping and instance encoding on LERF-OVS in 1.0-3.2 min per scene, depending on whether LLM fusion is enabled, and serves native 3D queries in 5.4 ms. It reaches 71.95% mean mIoU on LERF-OVS, outperforming both the training-free SFS and training-based LaGa baselines. DIGS also achieves the highest mean mIoU on LERF-Mask and 3D-OVS and surpasses Gaga and ObjectGS on Replica under their respective evaluation protocols. Code is available at this https URL.

---


### 326. [Label-Centric Knowledge Retrieval for Zero-Shot Text Classification](https://arxiv.org/abs/2610.16182)

**<font color=#1a73e8>作者：</font>** Daoping Wu, Dong Wang, Siyu Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Flagship large language models (LLMs) offer rich general knowledge and strong reasoning capabilities, but their high inference cost and latency limit their use for large-scale data labeling. We study zero-shot text classification with semantically meaningful labels and task descriptions, without task-specific labeled examples or classifier feedback. We propose \textbf{SLKR} (Semantic Label Knowledge Retrieval), a label-centric retrieval-augmented generation framework that separates offline knowledge construction from lightweight online inference. Offline, a flagship LLM independently generates label definitions, retrieval keywords, and boundary rules for potentially confusable label pairs, forming a reusable label-knowledge store. Because this construction operates over the label space rather than the input corpus, its one-time flagship cost can be amortized across large-scale inference. Online, hybrid semantic and lexical retrieval first identifies the top-$K$ candidate labels and then selects up to $M$ input-relevant boundary rules connecting candidate-label pairs. A lightweight LLM performs the final classification in a single call using the retrieved definitions and rules. Across three public benchmarks and a real-world multilingual book-classification dataset, SLKR achieves the best results on all four datasets with Qwen3.5-4B and on three of four with Ministral-3-3B, while using compact input contexts and no task-specific labeled examples. Boundary ablations further show that retrieving a small set of input-relevant rules preserves performance close to using all boundaries with substantially less context, supporting efficient reuse of flagship-generated label knowledge for lightweight classification.

---


### 327. [Correct Choices, Failed Sequences: Choice2Seq Benchmarks Correctness Retention Across Output Interfaces](https://arxiv.org/abs/2610.16191)

**<font color=#1a73e8>作者：</font>** Tianyou Lai, Wentao Yue, Zhiying Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A model may select the correct answer yet fail to construct it through a sequence of local decisions. We introduce Choice2Seq, a diagnostic benchmark that measures correctness retention across complete-answer selection and sequential construction in independent runs on the same problems and candidate sets. Sequence Composition Rate (SCR) measures the fraction of correctly selected items that are also answered correctly through local construction. Jev achieves 97.1% and 99.5% selection accuracy on arithmetic and lexical retrieval, yet retains only 33.0% and 2.1% of those correct choices under serial construction, respectively. Substantial gaps also emerge for StartLux and Qwen, including when Qwen emits characters directly. Restricting local options to candidate-supported characters improves construction, while explicit position indexing improves copying fidelity, even for incorrect selections. These interventions distinguish task correctness, plan fidelity, and output compliance. Matched dialogue-state evaluations reveal that local field construction largely preserves Jev's correct states but reduces Qwen's mean-turn accuracy, highlighting task- and interface-dependent differences. Sequence-level confidence and request-cost analyses further characterize completed outputs.

---


### 328. [Lüshi-1840: Building and Probing a Knowledge Cutoff for a Classical Chinese Language Model](https://arxiv.org/abs/2610.16201)

**<font color=#1a73e8>作者：</font>** Alex Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models trained only on text from before a given year are useful for studying hindsight and historical language, but the open collections of pre-modern Chinese carry no publication dates and unreliable dynasty labels. We present Lüshi-1840, a 983M-parameter model trained from scratch on 12,262 books (1.28B characters) selected as composed before 1840. A first corpus, dated by a common heuristic, in effect ended at 1644 while containing twentieth-century material. We describe the re-dating and cleaning pipeline that replaced it and an audit with markers the pipeline did not use, which still finds later material. On the model side we measure surprisal, relative to a modern reference, on annals compiled after the cutoff. For events after 1840 against events up to 1820 the ratio is 1.38 (95% interval 1.33-1.44), against about 1.00 for modern general-purpose models. In a series of 294M models, adding the later court records lowers the ratio from 1.33 to 1.16, and the two models diverge from the 1820s, where the added records begin. The probe tracks the coverage of sources and does not establish a single cutoff year; none of our probes exposes the audited contamination. Model, book list and scripts will be released.

---


### 329. [Look Back to Move Forward: Learning to Revisit for Agentic Compositional Image Generation](https://arxiv.org/abs/2610.16224)

**<font color=#1a73e8>作者：</font>** Zixu Wang, Xiaoran Zhao, Yahui Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image models have made remarkable progress in visual fidelity and instruction following, yet complex compositional generation remains challenging. Existing agentic approaches address this limitation through iterative generation and editing, adapting their actions based on interaction history. However, they typically fix the continuation state (i.e., the image from which refinement proceeds) to the latest image. Since iterative editing is not necessarily monotonic, the agent may continue refining from the latest image even when it has already degraded. In this work, we introduce GenRevisit, an agentic framework that extends action selection to joint continuation-state and action selection. The agent can not only use interaction history to adjust editing instructions but also select an image candidate to edit, jointly deciding where to continue from and how to refine. We train GenRevisit with SFT followed by agentic reinforcement learning. To address the coarse credit assignment of final outcome reward in GRPO, which assigns the same trajectory-level advantage to all actions, we further propose Normalized Action Credit Assignment (NACA) to redistribute positive advantage according to each action's contribution to reducing the remaining objective. On GenEval2, GenRevisit achieves GM scores of 84.3 and 74.4 with Qwen-Image-2512 and Z-Image-Turbo, surpassing the strongest baselines using the same generators by 12.7 and 10.9 points respectively. GenRevisit achieves state-of-the-art performance on GenEval, GenEval++, and GenEval2 among baselines.

---


### 330. [Learning to GUIDE the Group: Self-Learning LLM Facilitation Across Multi-Party Tasks](https://arxiv.org/abs/2610.16231)

**<font color=#1a73e8>作者：</font>** Ziyi Liu, Tzu-Sheng Kuo, Jiale Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models are increasingly adopted as multi-party communication facilitators, there is a growing demand for agents capable of balancing diverse group dynamics across contexts. However, existing LLM facilitators are often fine-tuned for task-specific objectives; generalized LLM-based facilitation methods that can adapt to different types of tasks and diverse group dynamics are underdeveloped. To address this gap, we present GUIDE (Generalized Unified Intervention for Dynamic Exchanges, a framework for developing generalized LLM-based facilitators across different multi-party contexts. GUIDE evaluates facilitation across both objective task outcomes and subjective metrics, including psychological safety and perceived friction. Within this framework, we study whether LLMs can self-learn generalized facilitation strategy offline to real-time interventions. We first collect multi-party human interactions guided by task-specific expert LLM facilitators (N=432 conversations). We then employ a self-learning method in which an LLM induces an actionable strategic playbook from conversations and iteratively refines it using feedback from an LLM judge aligned with human annotators (N=20), developing a single generalized facilitator that outperforms the three task-specific expert facilitators on held-out conversations 61.4% win rate. Finally, we evaluate these improvements empirically; in a real-time online empirical study, the self-learned generalized facilitator preserves facilitator performance and group productivity, improves speaking comfort and reduces interpersonal friction, while using 24.7% fewer turns and 29.0% fewer words than the expert prompts. These findings provide empirical evidence that LLMs can learn generalizable, task-agnostic social facilitation from task-specific human interactions, on-par with hand-crafted task-specific prompts across diverse group settings.

---


### 331. [Avoiding What Your Teacher Already Knows: Entity Familiarity for Deep-Search Distillation](https://arxiv.org/abs/2610.16251)

**<font color=#1a73e8>作者：</font>** Yifei Liu, Zhixiang Liang, Wentao Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep-search agents are commonly trained by distilling tool-use trajectories from stronger teacher models. However, structurally complex questions may remain relatively easy for teachers familiar with key entities in the underlying entity graph, resulting in lower search demand and weaker supervision. We refer to this teacher-specific variation in question difficulty as teacher-relative difficulty and investigate entity familiarity as an early predictor. We first introduce Evidence-Verified Entity Familiarity (EVF), which estimates familiarity by verifying a teacher-generated factual brief against online evidence. Across multiple teachers, EVF is significantly correlated with teacher-relative difficulty with AUCs of 0.60--0.70. However, its high cost makes it impractical for constructing entity graphs at scale. To address this limitation, we propose Self-Reported Entity Familiarity (SEF), a lightweight gating signal that directly asks a teacher whether it is familiar with an entity before admitting that entity into the graph. Across multiple teachers, trajectories from SEF-gated synthesis exhibit greater observed search demand and yield higher downstream student accuracy than those from ungated synthesis. Because familiarity is teacher specific, we further study cross-teacher reuse. We screen graphs collected for other teachers using Kimi-K3's SEF judgments and use the retained graphs to produce 5,411 additional trajectories. Combined with 2,200 trajectories from newly constructed, SEF-gated graphs, these data improve Qwen3.8-27B's accuracy from 44.10% to 66.41% on a BrowseComp subset, and achieving state-of-the-art performance among models of comparable size on BrowseComp, SEAL-0, HLE-text, and xbench. Overall, SEF provides a low-cost way to synthesize more informative supervision for deep-search distillation.

---


### 332. [ScreenASR-Bench: A Tiered Benchmark for Speech Recognition with Visual Context](https://arxiv.org/abs/2610.16260)

**<font color=#1a73e8>作者：</font>** Mingwei Fu, Zheshu Song, Zhikai Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current ASR models perform well on general benchmarks but still struggle with acoustically ambiguous words. Visual context can aid recognition in screen-based scenarios, yet existing benchmarks provide limited insight into the benefits of different types of visual evidence. To address this gap, we introduce ScreenASR-Bench , a tiered benchmark with three progressively challenging levels: Explicit Textual Evidence (ETE), based on direct on-screen text; Explicit Visual Evidence (EVE), using visible content rather than on-screen text; and Implicit Semantic Evidence (ISE), requiring scene-level inference. Extensive experiments on ASR models, Large Audio-Language Models (LALMs) and Omni models show that incorporating visual context substantially improves recall over the audio-only setting across all three model families. The gains are largest for ETE and smallest for ISE, indicating that models leverage direct visual evidence more effectively than indirect semantic cues. To facilitate future research on visually grounded speech recognition, we publicly release ScreenASR-Bench.

---


### 333. [RelLedger: Relational Information Governance for LLM Agent Organizations](https://arxiv.org/abs/2610.16281)

**<font color=#1a73e8>作者：</font>** Junxi Huang, Wenshuo Chen, Nuoxuan Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In LLM agent organizations, shared records determine which facts are available for later decisions. A sender consults interaction histories before deciding whether to report an event. A delivery gap across histories does not show whose relationship drove the choice or whether the resulting record matters downstream. We introduce RelLedger to audit these links. It holds the event, evidence, risk, and message fixed while crossing the sender's histories with the event target and an unrelated actor. Role reassignment and history rewrites locate the controlling cue. Message and cost interventions show when the effect appears. An attribution ledger maps each claim to its required response cells and separates missing interventions from sampling uncertainty. Recipient replay follows delivered information into downstream decisions. Executable workflows for a simulated one-person company extend the audit to retrieved histories, tool calls, and shared ledger updates. Across GPT, Gemini, Claude, DeepSeek, and Qwen, the audit reveals model-specific control paths and smaller relation gaps under explicit loss rules. Claude sends the same factual notice 62.22 percentage points more often with conflict histories than with friendly histories. In executable workflows, strained histories reduce recipient review rates by 45.83 points relative to warm histories for Claude.

---


### 334. [ProGAN-Based Synthetic Image Generation for Industrial Visual Inspection of Metallic Parts](https://arxiv.org/abs/2610.16287)

**<font color=#1a73e8>作者：</font>** Hossein Omid Beiki, Sepehr Asgari, Oliver Petrovic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated visual inspection is essential for efficient repair and recycling of metallic components. AI-based defect detection is a strong fit. However, it is often constrained by scarce, low-diversity training data. To address this gap, we study Generative AI-driven synthetic image generation using Progressive Growing GANs (ProGAN). We implement a ProGAN pipeline with Wasserstein loss and gradient penalty and evaluate key hyperparameters on two public datasets, MVTec AD (metal nut) and MPDD (tube). As a result, training remained stable and the model yielded realistic images. These images can augment training data, improve robustness, and reduce the cost of collecting rare defects.

---


### 335. [REVEAL: Reverse Engineering Agentic Latents from Frontier-Model Traces](https://arxiv.org/abs/2610.16288)

**<font color=#1a73e8>作者：</font>** Yuetian Du, Meng Wang, Yucheng Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier LLM agents perform complex interactive tasks, but their inference costs motivate transferring their experience to smaller open-source agents. Distillation and latent communication typically require target-model training or access to source-model internals. We study how textual frontier-model trajectories can provide reusable local controls for a frozen agent. Inspired by protocol reverse engineering, we introduce $\textit{Agentic Latents}$, comprising anchored states and dynamic profiles of feedback--response cycles elicited by replay in the target model. Our training-free framework, $\textbf{REVEAL}$ ($\textbf{REV}$erse $\textbf{E}$ngineering $\textbf{A}$gentic $\textbf{L}$atents), uses these profiles and trajectory outcomes to match and select local events from successful and failed rollouts of the same task and source model. Their response-transition contrasts yield a target-specific steering direction, applied before each response. Within-benchmark evaluations on Terminal-Bench 2.1 and Humanity's Last Exam with tools report higher accuracy than unmodified agents across three targets. Representation analyses and behavioral case studies support reusing frontier-model experience as local activation control.

---


### 336. [Fast Quantized Johnson$-$Lindenstrauss Transforms](https://arxiv.org/abs/2610.16289)

**<font color=#1a73e8>作者：</font>** Angelos Korakitis, Vasileios Nakos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization has emerged as one of the primary techniques for reducing the memory footprint of large language models during inference. A prominent example is Quantized Johnson$-$Lindenstrauss (QJL), which compresses KV caches using 1-bit asymmetric quantization while approximately preserving the inner products required by the attention mechanism. Recent theoretical and practical work aims at replacing the dense Gaussian projections used by the aforementioned transforms with more structured embeddings $-$ such as compositions of randomized Hadamard transforms $-$ while retaining the same embedding dimension.
In this paper, we introduce two constructions based on a composition of randomized Hadamard transforms, albeit with a Gaussian rather than Rademacher diagonal in the second stage. The first adds Gaussian dithering to smooth the quantizer, while the second inserts a random permutation to regularize the covariance structure of the resulting Gaussian measurements.
We prove embedding-dimension and running-time guarantees analogous to those of Fast JL in the non-quantized setting. The first construction achieves $m=O(\varepsilon^{-2}\log^2(d/\delta))$, while the second achieves $m=O(\varepsilon^{-2}\log(d/\delta))$ under a restriction on $m$. Both constructions can be applied in $O(d\log d)$ time.

---


### 337. [SLDBench v2: Active Scaling Law Discovery](https://arxiv.org/abs/2610.16297)

**<font color=#1a73e8>作者：</font>** Lingbei Meng, Rui Huang, Zhirong Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling laws predict large-model performance from small experiments, but finding a reliable law itself requires costly experiments. SLDBench tests whether language-model agents can discover scaling laws when all experimental results are given upfront. We introduce SLDBench v2 with two extensions. First, we expand the corpus from 8 to 127 scenarios spanning language-model pretraining, downstream performance, and vision-language transfer, and select 30 challenging scenarios on which a reference power-law fit reaches $R^2 \le 0.8$; they represent at least $1.09 \times 10^{23}$ FLOPs of source-reported training compute. Second, we introduce active scaling law discovery: an agent chooses which experiments to run, pays each one's recorded cost (e.g., training FLOPs), and revises its law as outcomes arrive, and is scored on the same hidden extrapolation targets as in the passive setting. Across 8 frontier agent systems, median $R^2$ drops from 0.72-0.75 (passive) to 0.24-0.57 (active), and prediction error rises 1.5-4.7 times, depending on the system. Agents favor cheap experiments, spending 8-44% of the full-pool cost on average; low-cost acquisition can yield strong predictions, but cheap purchases also leave experimental conditions needed for extrapolation unobserved. Experimental planning thus remains a key open challenge for agents that assist model development in the prevailing AI-for-AI study.

---


### 338. [Learning Temporal Evidence Selection for Video Anomaly Understanding](https://arxiv.org/abs/2610.16299)

**<font color=#1a73e8>作者：</font>** Hangil Park, Seungheon Kim, Tae-Kyun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video anomaly understanding (VAU) aims to generate language-level interpretations of anomalous events in long videos, requiring visual evidence that supports explanation beyond anomaly detection alone. Existing VAU pipelines commonly rely on anomaly-centric or predefined temporal sampling strategies, which efficiently emphasize suspicious moments but overlook contextual cues, object interactions, and temporally distributed evidence needed for reasoning. Motivated by recent progress in learnable temporal selection for long-video question answering, we revisit VAU temporal sampling as a downstream-aligned evidence selection problem. We introduce the semantic-conditioned Temporal Sampling Q-Former that learns to select temporal visual evidence through the VAU generation objective. Since generic VAU prompts provide weak video-specific guidance, we condition the sampler on CLIP-embedded object tags automatically extracted from the input video. These tags are used only for temporal evidence selection and are not appended to the LLM generation prompt, separating sampler conditioning from prompt augmentation. The proposed sampler operates in visual-token space, computes soft temporal selection weights from frame-level representations, and merges duplicated selections before response generation. Experiments on HIVAU-70K show that our model achieves the best performance among the compared fine-tuned models, while ablations demonstrate that learnable temporal sampling improves over fixed anomaly-focused sampling and that CLIP-embedded object-tag conditioning further improves over generic-prompt conditioning. Our results suggest that temporal sampling in VAU should be aligned with explanation-oriented evidence utility rather than anomaly saliency alone.

---


### 339. [FON: A Draft-Revise Dual-Organ Language Model without Sequence-Level Quadratic Attention](https://arxiv.org/abs/2610.16301)

**<font color=#1a73e8>作者：</font>** Helong Hu, Hongdan Pan, Shuiqing Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-attention assigns two functions to one mechanism-where to read and how to mix-at the price of O(L^2) training, an O(T) decode state, and position signals bound to the training length. Existing attention-free alternatives all optimize the single function of generation. We propose FON (Fusion-Organ Network), which differentiates one weight stack into a drafting organ (multi-tap learnable delays + content-adaptive recursion; causal, O(S) training, O(1) decode state, no sequence-level quadratic attention) and a revision organ that re-processes the written prefix through multi-scale ripple kernels injected via weak gates, never generating. At 30M parameters, iso-parameter and iso-token budget, FON reaches perplexity 131.03 on WikiText-103, beating Transformer (197.73) and Mamba2 (152.53); the advantage persists under all depth-aligned baselines and at the 70M tier (-20.8%). At 8x length extrapolation FON degrades by ~8-9% without positional-encoding engineering, between ALiBi and RoPE. The revision channel provides a structural pathway for in-domain infilling that causal architectures lack in principle (+19% over on-demand coupling), at a perplexity cost indistinguishable within measurement precision. We report all costs and boundaries: impaired long-range retrieval, synthetic-task disadvantages, weaker out-of-domain code infilling than a same-recipe Transformer, and a 6.5-12.3x wall-clock gap.

---


### 340. [ATTCK-R: Knowledge-Aware Long-Horizon Jailbreaking for Protected LLMs](https://arxiv.org/abs/2610.16305)

**<font color=#1a73e8>作者：</font>** Md Mushfiqur Rahman, Tobias Rohde, Rahul Tripathi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As large language models are deployed behind increasingly sophisticated safety mechanisms, evaluating their robustness under realistic adversarial conditions becomes increasingly difficult and critical. Existing jailbreaking evaluations often rely on static prompts, limited interaction horizons, or lightly protected systems, failing to reflect protected deployment settings with prompt-based safety protections. We show that the introduction of a prompt-based safety protection reduces the average attack success rate of a strong multi-turn baseline from 0.896 to 0.608 (32.1\% relative), demonstrating that unprotected evaluations substantially overestimate real-world vulnerabilities. We propose Adaptive Traceback and Tactic Curation for Knowledge-based Red-teaming (ATTCK-R), a planning-driven multi-turn red teaming framework designed for protected black-box systems. ATTCK-R models jailbreaking as a long-horizon trajectory optimization problem using a structured belief state, introduces optimization-based tactic curation to abstract reusable strategies from prior successes and failures, and employs informed traceback to resume attacks from strategically meaningful states rather than restarting. Evaluated across 9 widely used LLMs configured with a single prompt-based safety protection layer, ATTCK-R consistently outperforms strong recent multi-turn jailbreaking frameworks. Ablation results confirm that long-horizon planning and tactic curation improve attack effectiveness, while adaptive traceback improves efficiency through structured recovery from conversational failure.

---


### 341. [Narrative Paradoxes in LLM Inference: Shaping Reasoning Trajectories toward Misalignment](https://arxiv.org/abs/2610.16312)

**<font color=#1a73e8>作者：</font>** Haoming Yang, Ke Ma, Yangbangyan Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explicit reasoning in large language models (LLMs) is often associated with reliability, yet it can still pose risks when a model infers harmful goals under a benign context. We identify a distinct challenge: ensuring the safety of the \emph{multi-step reasoning process} itself, where locally coherent steps may still lead to globally harmful outcomes. To explore this vulnerability, we propose PDRA (Paradox-driven Reasoning-based Attack), a novel attack method that programs a harmful reasoning trajectory. PDRA first constructs a paradoxical narrative core by pairing a malicious actor (e.g., a terrorist) with a benign task (e.g., writing a safety bulletin). It then embeds this core into a structured analytical framework that forces the model through a mandatory three-stage analysis -- surface purpose, latent intent, and operational reconstruction -- guiding it to produce detailed harmful content while maintaining narrative coherence. Mechanistically, we show PDRA steers the model's internal representations away from refusal-related patterns, suppressing safety-triggering lexicons while activating planning-oriented terms. Empirically, PDRA achieves state-of-the-art attack success rates across diverse LLMs with high efficiency. \textcolor{red}{\textbf{Warning:} This paper may contain sensitive content.}

---


### 342. [ReTAC: Residual Test-Time Agentic Computation for Video Spatial Reasoning](https://arxiv.org/abs/2610.16315)

**<font color=#1a73e8>作者：</font>** Yike Wu, Keyan Chen, Qixiong Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time agentic computation can improve multimodal large language models (MLLMs) through planning, tool use, iterative perception, and reflection, but indiscriminate computation may duplicate resolved work, introduce noisy evidence, and perturb correct predictions. We propose that such computation should be residual: allocate additional computation only to requirements unresolved by the base model and, after a localized failure, recompute only the affected states. We instantiate this formulation in ReTAC, a training-free multiagent framework for video spatial reasoning. ReTAC organizes supplementary computation around unresolved requirements. It plans ordered steps to acquire missing spatial evidence and combines the observations with compatible native evidence for reasoning. In addition, it uses stage-aligned verification to localize failures to planning, perception, or reasoning. Dependency-based recovery recomputes only affected states while reusing unaffected ones. Extensive experiments show that ReTAC achieves the highest overall score among the compared methods across three mainstream MLLMs and two widely adopted benchmarks. Further analyses show that gains from additional computation depend not only on how much is used, but also on where it is allocated and which valid intermediate states are preserved.

---


### 343. [Strong yet Controllable LLM Abstention without Learning to Abstain](https://arxiv.org/abs/2610.16318)

**<font color=#1a73e8>作者：</font>** Junwei Zhang, Yifei Wang, Wanli Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can reduce hallucination by abstaining from questions they would likely get wrong. Abstention can be implemented outside the model (selective answering) using a confidence threshold that controls the answer rate (coverage), or learned inside it (abstention training), which can perform better but fixes coverage once trained. To compare the two, we match their coverage and decompose risk (error rate) into answering ability and distinguishing ability, i.e., how well the model answers and how accurately it abstains, respectively. The decomposition shows that abstention training performs better mainly by answering better: with strong confidence estimators, the two have nearly equal distinguishing ability. This motivates Train for Accuracy, then Post-hoc Select (TAPS), a modular approach that keeps coverage controllable, needs only standard post-training and an off-the-shelf confidence estimator, and benefits from advances in either component. Across three LLMs and three factual QA benchmarks, TAPS with a probing-based confidence estimator attains 1.5--9.4 percentage points lower mean risk than three representative abstention training methods at matched coverage. Within TAPS, accuracy training often weakens the model's own confidence signals, yet refitting the estimator largely preserves distinguishing ability. Together, these results establish TAPS as a strong yet controllable baseline and raise the bar for future abstention training: sacrificing control over coverage should yield gains beyond what can be achieved by optimizing answering and abstaining separately.

---


### 344. [BehaviorFormer: Discovering Behavioral Patterns via Clusterable Next-Token Prediction](https://arxiv.org/abs/2610.16322)

**<font color=#1a73e8>作者：</font>** Tobias Schneider, Danial Fahrner, Soren Antebi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discovering behavioral patterns in open-ended games is challenging due to the lack of clear objectives or ground-truth annotations. In this work, we extend a next-token prediction Transformer with the deep clustering algorithm DCSS to learn meaningful representations with well-separated clusters. In a controlled Minecraft session with 26 players, the method discovers 23 distinct behavioral patterns that generalize across the studied players, further refining structures present in self-supervised representations into clearly separable clusters. We group the clusters into seven interpretable categories covering stationary, roaming, travel, mining, base work, logging, and farming behavior.

---


### 345. [Anomaly-Guided Observation and Two-Level Semantic Feedback for Training-Free Video Anomaly Analysis](https://arxiv.org/abs/2610.16324)

**<font color=#1a73e8>作者：</font>** Hangil Park, Seungheon Kim, Tae-Kyun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free language-based video anomaly detection (VAD) uses frozen vision--language models (VLMs) and large language models (LLMs) to localize abnormal events without task-specific model-weight optimization. Existing approaches increasingly exploit broader temporal and semantic context, yet generic context does not necessarily foreground abnormal events or specify how video-level semantics should modify local anomaly scores. We introduce a training-free semantic feedback framework that uses VAD-guided active observation for video anomaly understanding (VAU) and returns the resulting anomaly-focused description to refine temporal detection. Starting from an upstream anomaly-score curve, we adapt reasoning-based iterative frame selection: high-score regions seed the observations, and anomaly scores together with VLM relevance assessments guide subsequent temporal exploration. A frozen video-language model generates a single open-ended anomaly description from the selected frames. The description is returned through two complementary feedback levels: video-level feedback determines whether the score distribution should be suppressed, preserved, or sharpened, with selective visual rechecking, while local feedback retrieves event-related windows and promotes scores only after target-local visual verification. All model weights remain frozen, and feedback is applied once without regenerating the description. On the HIVAU video-summary evaluations of UCF-Crime and XD-Violence, VAD-guided observation improves GPT-rated reasonability, detail, and consistency over the matched CLIP-guided variant. For VAD, semantic feedback improves the re-evaluated upstream detector from 84.36% to 86.25% AUC on UCF-Crime and from 68.07% to 72.58% AP on XD-Violence, where the final AUC is 91.74%.

---


### 346. [When a Conceptor Complement Becomes Gain: Operator Geometry and Behavioral Attribution in Language Models](https://arxiv.org/abs/2610.16325)

**<font color=#1a73e8>作者：</font>** Shuhul Razdan, R Balamurugan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a steering intervention changes a language model's behavior, which part of the intervention deserves the credit? We test this question for a target-centered, scaled conceptor complement by removing its fitted covariance filter while preserving the same target-specific center and gain. At the original aperture $\alpha=.05$ and gain $\beta=2$, all 21 fitted maps across three models and seven targets expand every direction at the generation intervention layers. The matrix correction is $0.093\%$--$7.815\%$ of the matched-control displacement on held-out extraction activations. In 480 paired comparisons within a 1,920-response study, retaining the matrix changes many individual texts but does not establish a consistent additional target-suppression benefit on the four-target panel. A geometric aperture sweep shows that the operating regime changes with the filter setting. Separately, an invertible soft filter preserves what an unrestricted affine readout can recover, whereas dedicated erasure methods reduce prediction by newly fitted probes. Together, the results show why a whole-intervention comparison cannot by itself attribute generated behavior to the fitted matrix: analyze the complete transformation, hold shared components fixed, and test its output consequences directly.

---


### 347. [TRAP: Tool-result Replay Attack for Probing Misbinding in LLM Agents](https://arxiv.org/abs/2610.16333)

**<font color=#1a73e8>作者：</font>** Yutong Zhi, Jie Zhang, Xiuqi Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI agents increasingly act through external tools, tool results are no longer simple outputs but execution artifacts that must remain correctly associated with the context that produced them. Yet as results persist across caches, recovery mechanisms, and shared runtime state, this association can break, causing a real and unmodified result to be consumed in an incompatible execution context and lead the agent to an unsafe action. We characterize this failure as tool-result misbinding. To systematically study this failure, we introduce ReplayBench, a benchmark that uses controlled tool-result replay to evaluate misbinding across 19 representative agent scenarios, 4 failure properties, and 3 replay mechanisms. Across eight LLMs, three agent frameworks, and diverse stateful workflows, we find widespread replay-induced failures, with a mean Final-State Error Rate of 0.649 under cross-task replay. Stage-wise analysis localizes these failures to model-side action generation. Further analyses show that replay susceptibility varies with task similarity, shows little dependence on object similarity, and remains high under result staleness and implicit environment changes. These findings motivate runtime validity mechanisms that eliminate final-state errors in our evaluated settings while preserving legitimate recovery. The results call for explicit contextual binding in tool-using agent runtimes. Our work is public at this https URL.

---


### 348. [Efficient Multi-Agent Reasoning via Confidence-Guided Adaptive Debate](https://arxiv.org/abs/2610.16343)

**<font color=#1a73e8>作者：</font>** Seungdong Yoa, Ye Seul Sim, Suhee Yoon 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate has shown promise for improving the reasoning of large language models, yet recent theory suggests its benefits are highly regime-dependent. While interaction can amplify informative signals under corrective conditions, symmetric debate dynamics are neutral in expectation, often making majority voting preferable. We reconcile these views by arguing that debate is effective only when invoked at the right time and with appropriate structure. Based on this insight, we propose LASE: Leader-Adaptive Structured Engagement, a leader-centric multi-agent debate framework that selectively engages interaction only in non-neutral regimes. LASE introduces an asymmetric leader-supporter architecture that enables directed information flow and selective signal amplification, while defaulting to simple aggregation otherwise. Experiments across diverse reasoning benchmarks show that LASE achieves multi-agent-level performance with near single-agent token cost, substantially improving efficiency over static debate and voting baselines.

---


### 349. [STEPwise: Supporting Teachers in Diagnosing Students' Mathematical Problem-Solving Skills through LLM-Generated Questions and Rubric](https://arxiv.org/abs/2610.16344)

**<font color=#1a73e8>作者：</font>** Yoonsu Kim, Hayeon Doh, Eunhye Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Problem-solving is central to mathematics education. However, diagnosing where students' reasoning breaks down requires individualized probing and consistent criteria that teachers cannot sustain at classroom scale. We introduce STEP (STage-based Evaluation of Problem-solving skills), co-designed with six mathematics education experts, which operationalizes problem-solving as four stages and eight diagnostic sub-skills. By specifying what evidence to elicit and assess at each stage, STEP enables an LLM pipeline to generate stage-specific questions and rubrics for any math word problem, reducing the manual design of diagnostic materials. An expert review (N=8) assessed the pedagogical validity of the generated materials and informed STEPwise, a teacher-in-the-loop system for diagnostic material generation and process-level assessment. In a classroom study with 5 teachers and 64 students, STEPwise helped teachers and students locate reasoning breakdowns and supported students in reflecting on their reasoning. Together, STEP and STEPwise offer a structured approach to fine-grained diagnosis at classroom scale.

---


### 350. [ChronoScribe: Semantic-Numerical Specialization for Instruction-Driven Time Series Forecasting](https://arxiv.org/abs/2610.16345)

**<font color=#1a73e8>作者：</font>** Yuchen Jiao, Miao Zhang, Yuxuan Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in instruction-driven time series forecasting highlight a fundamental tension: systems must simultaneously master natural-language instruction following and precise numerical prediction. Current approaches often force a compromise. Large language models (LLMs) can interpret unstructured requests but may be inaccurate when asked to produce forecast values directly, whereas time series foundation models (TSFMs) provide numerical forecasts but typically require structured inputs specifying the target series, context window, and horizon. We present ChronoScribe, which applies semantic-numerical specialization to this workflow. A LoRA-adapted LLM proposes an execution path and context length; deterministic rules resolve the executable configuration. On the specialist path, a frozen TSFM produces quantile trajectories for the task-specified horizon. Deterministic trajectory summaries condition the response, while the LLM neither generates nor revises predicted values. We evaluate a Qwen3.5-9B--Chronos-2 implementation across 23 evaluation dimensions and 30 public datasets against eleven proprietary direct LLMs and three open TSFMs. ChronoScribe has the lowest error on sMAPE, MASE, WAPE, RMSE, and MAE among all evaluated systems, including fixed-context controls. Across these metrics, even the lowest direct-LLM error remains 2.0--2.7 times the corresponding ChronoScribe error. At the system level, ChronoScribe achieves a Task-Level Score (TLS) of 65.5, 10.6 points above the strongest direct-LLM baseline. The results support ChronoScribe's division of labor, in which the LLM handles interpretation, configuration, and communication while the TSFM handles numerical forecasting.

---


> [!TIP]
> 当前位于：**301-350**（第 7/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
