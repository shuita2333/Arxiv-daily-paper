# 🧠 大模型相关研究 | 2026年06月04日

> 本类共 **188** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-188](./part-04.md)

---

### 51. [Efficient Hyperparameter Optimization for LLM Reinforcement Learning](https://arxiv.org/abs/2606.03073)

**<font color=#1a73e8>作者：</font>** Minping Chen, Bowen Xiao, Du Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) for large language models (LLMs) is highly sensitive to hyperparameter configurations, making hyperparameter optimization (HPO) essential yet computationally expensive. Existing multi-fidelity HPO methods remain inefficient for LLM RL due to the massive model scale and resource-intensive training cycles. In this paper, we propose Joint Fidelity Hyperparameter Optimization (JF-HPO), which simultaneously adapts both model size and training budget as fidelity. JF-HPO is empowered by: (i) it leverages a small proxy model of the target LLM for efficient training and evaluation in each HPO trial; (ii) it integrates carefully designed early-stopping strategies based on training dynamics; (iii) it introduces an efficient checkpointing mechanism to eliminate redundant computations. Compared with existing HPO methods, JF-HPO significantly improves the computational efficiency of each trial (up to 14.9 times), while achieving better or competitive predictive accuracy under the same time budget. Notably, compared with utilizing hyperparameter configurations from the VeRL Recipe, JF-HPO delivers performance improvements ranging from 5.8% to 111.6%.

---


### 52. [TGV-KV: Text-Grounded KV Eviction for Vision-Language Models](https://arxiv.org/abs/2606.03075)

**<font color=#1a73e8>作者：</font>** Jizhihui Liu, Ruizi Han, Miao Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) inherit the auto-regressive generation paradigm and cache the keys and values (KV) of all previous tokens to accelerate inference, resulting in memory consumption that scales linearly with context length. This issue is particularly pronounced in VLMs due to substantial redundancy in the visual modality. Although KV cache eviction approaches can effectively reduce inference memory, they often incur significant performance degradation in VLMs, as most are designed for language models and overlook the inherent gap between text and vision. By systematically analyzing the modality gap in VLMs in this work, we argue that the importance of visual information should be grounded in textual guidance and accordingly propose a Text-Grounded KV Eviction method for VLMs (TGV-KV). TGV-KV comprises three submodules: (1) Text-Vision Budgeting (TVB) assigns budget to each layer based on the mutual information interaction. (2) Text-Weighted Ranking (TWR) assesses the priority of text and ranks vision importance based on weighted text-image attention. (3) Text-Prioritised Retention (TPR) policy strategically preserves text KV to avoid acute information loss. We evaluate TGV-KV across five models with different sizes and architectures, showing that TGV-KV preserves 99.2% full-KV accuracy on the VizWiz-VQA task with LLaVA-NeXT and boosts end-to-end throughput by 52.6% with an extreme retention budget of 5%. Code is available at this https URL.

---


### 53. [Libra: Efficient Resource Management for Agentic RL Post-Training](https://arxiv.org/abs/2606.03077)

**<font color=#1a73e8>作者：</font>** Kaiwen Chen, Xin Tan, Jingzong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a standard post-training paradigm for large language models (LLMs), extending beyond preference alignment to complex reasoning and multi-turn agentic behaviors. In agentic RL, the rollout stage generates trajectories while invoking tools, producing long-tailed and non-stationary workloads that challenge conventional resource-management assumptions. Three fundamental challenges arise. First, due to the long-tail distribution, a small fraction of trajectories dominates rollout makespan. Second, rollout and training exhibit strong asymmetry in compute patterns, memory demands, and sensitivity to sequence length. Third, as the RL policy evolves, the trajectory-length distribution drifts over time, rendering any static resource split progressively suboptimal.
We present Libra, which introduces two core mechanisms. The first is a periodic global resource planner that jointly optimizes GPU allocation across rollout and training clusters. It leverages an elastic hybrid pool to enable lightweight, non-blocking worker reallocation between stages. The second is a causality-driven multi-level feedback queue (C-MLFQ) scheduler, which routes requests to heterogeneous rollout buckets based on causal signals derived from tool-return outcomes, rather than relying on fragile length predictions. Evaluated on 48 A800 GPUs, Libra achieves up to 3.0$\times$ higher throughput and converges up to 2.5$\times$ faster in reward compared to the baselines.

---


### 54. [G^2C-MT: Graph-Guided Context Selection for Document-Level Machine Translation](https://arxiv.org/abs/2606.03078)

**<font color=#1a73e8>作者：</font>** Baijun Ji, Zixuan Zhou, Xiangyu Duan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective document-level machine translation (DocMT) requires capturing long-range discourse dependencies. Recent work has explored retrieval-based and discourse-aware context selection. However, these approaches often lack an explicit mechanism for modeling structured discourse dependencies between distant paragraphs in a document. In this paper, we propose G^2C-MT (Graph-Guided Context for Machine Translation), which views DocMT context selection as a structured path discovery problem on a lightweight discourse graph, rather than retrieving unstructured context sets or relying on expensive LLM-based discourse modeling. In detail, we represent each paragraph as a node and model the relationship between each pair of nodes, considering their semantic similarity, adjacency, and keyword overlap. Furthermore, we propose a depth-biased random walk over the graph to sample a backward context path for each target paragraph. The context path will be used to prompt a large language model (LLM) for translation. This framework naturally supports multi-path context sampling, which can improve robustness by aggregating diverse translation candidates for discourse-ambiguous inputs. Experiments conducted across various domains show that G^2C-MT outperforms strong baselines on multiple LLMs, including DeepSeek-V3, Gemini-2.5-Flash-lite, and the Qwen-2.5/3 series.

---


### 55. [Regret Pre-training: Bridging Prior and Posterior Views for Enhanced Knowledge Grounding](https://arxiv.org/abs/2606.03080)

**<font color=#1a73e8>作者：</font>** Mingkuan Zhao, Xiayu Sun, Wentao Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Causal language models factorize sequence probabilities using only preceding context, leaving future information unexploited during training despite its availability in the training data. This paper introduces Regret Pre-training, a self-supervised framework grounded in the Learning Using Privileged Information (LUPI) paradigm. The framework employs a dual-view architecture in which a single model generates both a causal Student distribution and a future-conditioned Teacher distribution. The training objective augments standard language modeling with a regret loss that minimizes the KL divergence from teacher to student, transferring future-aware signals to the causal representations. We investigate two teacher configurations on the OLMoE-1B-7B architecture:LocalRegret, which extends attention by one future token, andGlobalRegret, which conditions on bidirectional context with the target position masked. Experiments on nine downstream tasks following 4 billion tokens of training demonstrate that both configurations consistently outperform the baseline. On average,GlobalRegret andLocalRegret achieve 33.9% and 32.2% accuracy respectively, surpassing the baseline's 30.2%. Most notably,GlobalRegret improves BoolQ performance by 18.1 percentage points (61.0% vs 42.9%). The framework introduces no additional parameters and requires only one extra inference-mode forward pass per training step.

---


### 56. [DELTAMEM: Incremental Experience Memory for LLM Agents via Residual Trees](https://arxiv.org/abs/2606.03083)

**<font color=#1a73e8>作者：</font>** Haoran Tan, Zeyu Zhang, Zhicheng Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM)-based agents increasingly rely on memory to learn from experiences over continual interactions. However, storing experiences as independent, flat units leads to substantial redundancy and retrieval conflicts, as similar episodes repeat overlapping content and subtle scene variations cause retrieved memories to offer contradictory guidance. To address this, we introduce residual experience, positing that newly acquired experience is often an incremental variation of existing knowledge. We propose DeltaMem, a framework that organizes experience memory into two independent residual trees, one storing goal-conditioned task experience as reusable skills and another for scene-level environment knowledge. Each tree uses a root node for generalized base experiences and incremental delta nodes for subsequent variations, allowing related experiences to share a common foundation without duplication. For retrieval, a failure-penalized similarity scan locates the best match, reconstructing the full experience via root-to-match chain composition. An autonomous consolidation mechanism distills high-frequency paths into new root nodes, enabling the trees to self-organize from general heuristics to specialized variants. Experiments across diverse interactive environments show that DeltaMem consistently outperforms existing baselines. To facilitate future research, we release the code at this https URL.

---


### 57. [Multi-component Causal Tracing in Large Language Models](https://arxiv.org/abs/2606.03085)

**<font color=#1a73e8>作者：</font>** Zirui Yan, Dennis Wei, Dmitriy A. Katz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal tracing systematically intervenes on a large language model's (LLM's) internal representations to uncover and quantify the causal pathways linking specific inputs or computations to specific metrics of interest, quantifying the LLM's behavior. Building on previous single-component or single-layer studies, this paper presents a unified framework for causally tracing multiple components simultaneously. This framework systematically identifies the subsets of components (e.g., attention heads and multi-layer perceptron neurons) most critical to a desired target performance metric (e.g., accuracy and fairness). This is achieved by incorporating flexible interventions applied to a wide range of desired metrics. To address the combinatorial complexity of the multi-component problem, an efficient algorithm is designed that leverages soft interventions and a carefully designed metric transformation, converting the combinatorial search problem into a continuous one that can be solved efficiently under proper constraints, thereby generating proper binary decisions for selecting components. Experimental results demonstrate that the proposed method efficiently identifies subsets of the model's components that have a high impact on the target metric, outperforming existing baseline approaches. Our code is available at this https URL.

---


### 58. [The Shadow Price of Reasoning: Economic Perspective on Optimal Budget Allocation for LLMs](https://arxiv.org/abs/2606.03092)

**<font color=#1a73e8>作者：</font>** Xu Wan, Speed Zhu, Jianwei Cai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inference-time scaling has emerged as a critical avenue for enhancing Large Language Models' performance, yet real-world deployment is constrained by strict computational budgets. In this work, we formulate inference budget allocation as a global constrained optimization problem governed by economic principles. By modeling per-query reasoning utility with a shifted-surge function, we derive an optimal allocation policy based on a global shadow price that equilibrates marginal utility under resource scarcity. Based on this theory, we propose Constrained Latent-utility Equilibrium Allocation for Reasoning (CLEAR). It performs rational abandonment and reallocates resources from insolvent queries to solvable queries near their emergence thresholds.
Extensive experiments on several reasoning tasks with different traffic streams demonstrate that CLEAR significantly improves the Pareto frontier of total token cost versus mean accuracy. In resource-scarce regimes, CLEAR achieves up to a 3x improvement in global accuracy compared to uniform allocation.

---


### 59. [Decomposing how prompting steers behavior](https://arxiv.org/abs/2606.03093)

**<font color=#1a73e8>作者：</font>** Fan L. Cheng, Nikolaus Kriegeskorte  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prompting steers large language models (LLMs) and vision-language models (VLMs) without weight updates, but it remains unclear how instruction changes reshape internal representations to produce behavior. We introduce a nested geometric decomposition framework that treats prompting as a transformation of the representational geometry of the content following the prompt. For each prompt pair, we align representations of the same stimuli under two prompts using increasingly expressive stimulus-invariant maps: translation, rigid transformation with uniform scaling, sequential axis scaling, affine transformation, and nonlinear transformation. We then causally test each map by replacing a single layer's prompt-A hidden state for held-out stimuli with its mapped counterpart and measuring recovery of prompt-B representational geometry and behavior. Across three LLMs, three VLMs, and six text or image datasets spanning style, emotion, scene content, and number, prompts consistently reshape representations toward the instructed task structure. Cross-validated variance decomposition shows that much prompt-induced activation change is captured by shape-preserving maps, especially translation and rigid transformation with uniform scaling, while tier profiles reveal model- and task-specific routing strategies across layers. Crucially, although translation and rigid tiers already improve behavioral agreement, affine transformation is the first tier to nearly recover target-prompt task geometry and yields corresponding behavioral gains. This suggests that cross-dimensional linear mixing is a key mechanism by which prompts reorganize representations toward instructed task structure. Our framework decomposes prompt-induced representational change into interpretable geometric components and reveals how models route task-relevant structure to produce prompt-driven behavior.

---


### 60. [Can Factual Opinions Be Edited (Manipulated) in Large Language Models?](https://arxiv.org/abs/2606.03096)

**<font color=#1a73e8>作者：</font>** Yuanpu Cao, Ziyi Yin, Fenglong Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly integrated into various domains, making knowledge editing techniques crucial yet potentially hazardous. Current editing methods primarily target atomic facts, overlooking the significant risks associated with manipulating factual opinions, e.g., documented stances of public figures on societal issues. Such manipulation could reshape public images, influence elections, and alter societal views. To systematically assess this threat, we introduce the Factual Opinion Editing with Evidence (FOE) benchmark, which encompasses 261 public figures, 19 issue categories, and 2,178 complete opinion records. Our evaluations demonstrate that current editing techniques struggle significantly with factual opinions, often achieving only superficial changes while failing to preserve consistency between the edited opinion and the supporting evidence generated by the model. To address this limitation, we further propose a simple yet effective Self-Generated Evidence-Aligned method that achieves opinion-evidence alignment without relying on explicit instructions. Together, our benchmark and method provide a foundation for understanding the emerging security implications of factual opinion editing in LLMs.

---


### 61. [PhotoCraft: Agentic Reasoning with Hierarchical Self-Evolving Memory for Deep Image Search](https://arxiv.org/abs/2606.03099)

**<font color=#1a73e8>作者：</font>** Kailin Lyu, Zhiqiang Yuan, Jianwei He 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep Image Search requires multi-step reasoning over rich contextual cues, such as time, location, and event relations. However, most existing LLM-based agents are stateless and reactive, lacking persistent memory to maintain long-horizon context or transfer experience across tasks, which often leads to execution drift and experience isolation. To address these limitations, we propose PhotoCraft, a training-free, hierarchical memory system for photo-search agents. Inspired by human cognition, PhotoCraft equips MLLMs with working, episodic, and semantic memory, which are dynamically invoked during reasoning to preserve logical consistency and knowledge transferability throughout multi-step reasoning and answer generation. Extensive experiments on DISBench demonstrate that PhotoCraft consistently improves context-aware retrieval across diverse MLLM backbones, achieving gains of up to 18.5\% and effectively mitigating key bottlenecks in memoryless deep image search, offering a practical path toward reliable and generalizable multimodal search agents.

---


### 62. [Small RL Controller, Large Language Model: RL-Guided Adaptive Sampling for Test-Time Scaling](https://arxiv.org/abs/2606.03102)

**<font color=#1a73e8>作者：</font>** Runpeng Dai, Tong Zheng, Rui Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time scaling improves the reasoning performance of large language models but incurs substantial cost in both total computation and latency. Existing adaptive sampling methods partially mitigate this issue by dynamically deciding when to stop sampling, yet they typically rely on heuristic rules or rely on distribution assumptions. In this work, we formulate adaptive sampling as a Markov decision process (MDP). We train a lightweight sampling controller with reinforcement learning (RL) to jointly balance answer correctness, latency, and computation cost. At each round, the controller decides to stop sampling or to acquire additional samples. Our method is lightweight which only relies on statistics of final answers, and can be trained and deployed on CPU. We further show that the resulting framework admits an interpretation as the Lagrangian relaxation of a constrained optimization problem with explicit budget constraints. Experiments against strong baselines such as ASC and ESC show that our method achieves improved trade-offs among answer correctness, sampling rounds, and total samples required.

---


### 63. [EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for Autonomous Agentic Reinforcement Learning](https://arxiv.org/abs/2606.03108)

**<font color=#1a73e8>作者：</font>** Guhong Chen, Yingcheng Shi, Yongbin Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous LLM training is often framed as recipe search, which leaves the training harness largely static. This limitation sharpens in agentic RL, where shifting bottlenecks and scalar rewards mask diverse failure modes. We introduce EvoTrainer, an autonomous training framework that co-evolves LLM policies and training-side harnesses through empirical feedback: it diagnoses rollout-level evidence, revises diagnostics, backtests interventions, and accumulates reusable skills. Evaluated on mathematical reasoning, competitive-programming code generation, and repository-level software engineering, EvoTrainer matches or exceeds the human-engineered RL references under the same data, codebase, and evaluation protocol, with the largest gain on long-horizon agentic SWE. Trajectory analyses show that retained strategies diverge across domains, evolving diagnostics prevent invalid high-scoring branches from being promoted, and reusable skills shape later search. Autonomous LLM RL should move beyond recipe search toward joint evolution of policies and the training harnesses that interpret them.

---


### 64. [Coherence Maximization Improves Pluralistic Alignment](https://arxiv.org/abs/2606.03110)

**<font color=#1a73e8>作者：</font>** Taslim Mahbub, Yiding Pei, Shi Feng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aligning AI systems with diverse human values requires value specifications grounded in concrete examples, but generating such examples without extensive human supervision remains an open challenge. We investigate what makes these examples effective, using Internal Coherence Maximization (ICM) -- which infers labels by maximizing their mutual predictability -- to generate persona-specific examples that steer a model toward a target group's values, without human supervision. Across four benchmarks spanning classification, preference, and open-ended generation, ICM-inferred in-context examples match the performance of gold labels. Crucially, coherence matters beyond individual label accuracy: with accuracy held constant, more coherent examples generalize substantially better than incoherent ones. For personas underrepresented in pretraining data, targeted human feedback on the questions where the model is least certain about a persona's values yields better generalization than the same number of labels on arbitrary questions. These results identify coherence as a key design principle for scalable value specification, leveraging the diverse human perspectives already encoded in pretrained language models.

---


### 65. [Experience-Driven Dynamic Exits for LLMs with Reinforcement Learning](https://arxiv.org/abs/2606.03113)

**<font color=#1a73e8>作者：</font>** Yanyu Zhu, Hoilam Pao, Niu Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models suffer from slow autoregressive inference. While self-speculative decoding accelerates this process, its efficiency is hampered by static configurations like fixed exit layers and speculation lengths. We reframe this optimization as a \textbf{Markov Decision Process} and propose \textbf{LEDE}, a framework that uses offline reinforcement learning. LEDE learns a policy to dynamically select the optimal exit layer and speculation length based on the local context of the generated sequence at each step, balancing computational cost and draft quality. Comprehensive evaluations on Llama-2 and Llama-3 models show LEDE achieves up to a $2.0\times$$\sim$$2.7\times$ speedup over autoregressive decoding and and provides an additional 17\% speedup over the static speculative baselines.

---


### 66. [FAF-CD: Frequency-Aware Fusion for Change Detection under Imperfect Multimodal Remote Sensing](https://arxiv.org/abs/2606.03114)

**<font color=#1a73e8>作者：</font>** Yufan Wang, Sokratis Makrogiannis, Chandra Kambhamettu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing change detection for real-world monitoring often relies on imperfect heterogeneous observations, where pre- and post-event images may be asynchronous, cross-sensor, or affected by illumination, seasonal, and modality shifts. This setting is especially challenging for EO-SAR disaster mapping, where nuisance variation can resemble structural damage. We propose FAF-CD, a frequency-aware hybrid framework with a DINOv3-pretrained ConvNeXt encoder and a linear-complexity VMamba-based decoder. Its rectification-aware tri-branch fusion module combines deformable spatial alignment with Fourier and Haar-wavelet comparisons, using adaptive gating to aggregate complementary cues across scales. On BRIGHT validation, a matched heterogeneous EO-SAR adaptation improves clean and perturbed tc-mIoU/tc-mAP over NeXt2Former-CD. FAF-CD also generalizes to binary optical CD, achieving 0.924 cF1 on LEVIR-CD and 0.955 cF1 on WHU-CD, and obtains the best average perturbed cIoU/cF1 on both binary datasets among M-CD and NeXt2Former-CD under pseudo-change-aligned stress tests. It further reduces cost by approximately 24 GFLOPs relative to NeXt2Former-CD while maintaining or improving accuracy.

---


### 67. [Synthetic Hallucinations, Real Gains: Hard Negatives from Frontier Models for FIM Hallucination Mitigation](https://arxiv.org/abs/2606.03130)

**<font color=#1a73e8>作者：</font>** Mahdi Erfanian, Nelson Daniel Troncoso, Aashna Garg 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small open-source code models that power IDE autocomplete still emit hallucinated Fill-in-the-Middle (FIM) completions: syntactically natural calls to methods, parameters, variables, and imports that do not exist in the surrounding project. Existing mitigations either require per-language execution sandboxes that do not apply at mid-keystroke or preference-optimisation pipelines that need large human-labelled corpora. We propose an execution-free alternative: use frontier code models to synthesise plausible-but-wrong completions as hard negatives, then leverage the contrast between these synthetic hallucinations and the ground-truth developer edit as a supervised fine-tuning signal. Our pipeline scrapes multilingual FIM contexts from public GitHub across eight languages and asks a panel of three frontier generators to produce one hard negative per context for each of four hallucination types drawn from the Delulu taxonomy, a Docker-verified multilingual FIM hallucination benchmark, yielding a paired chosen/rejected dataset. Fine-tuning Qwen2.5-Coder-7B-Instruct on a 100K-row curated subset lifts Delulu exact match by +18.8 points and edit similarity by +0.22 on every language and every type, while also improving every HumanEval-Infilling split and every SAFIM subset. The same recipe at 3B lifts Delulu by +12.8 EM with a small, characterised general-FIM trade-off. Five-axis ablations (size, type mix, language coverage, base-model family, and a difficulty-aware fool rate) plus a head-to-head SFT vs. DPO/ORPO comparison map which design choices drive the gain. We release the full pipeline source code -- generation, fool-rate LLM judging, curation, and the FIM fine-tuning recipe -- so that the experiments in this paper can be reproduced end-to end on any permissively licensed corpus.

---


### 68. [HARVE: Hacking-Aware Reward-Head Vector Editing for Robust Reward Models](https://arxiv.org/abs/2606.03131)

**<font color=#1a73e8>作者：</font>** Shuang Liu, Yuxuan Bo, Qiuyang Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward models are central to large language model (LLM) alignment, but they remain vulnerable to reward hacking. To evaluate reward-model robustness, we introduce RewardHackBench containing 13 reward-hacking patterns covering real life high-stakes domains and general settings, and we find severe failures on specific subcategories across eight reward models. To mitigate these failures, we propose HARVE, a training-free reward-head editing method for scalar reward models. Instead of fine-tuning the reward model, HARVE identifies a multi-directional hacking subspace from residual stream directions associated with selected hacking subcategories, and removes the component of the reward-head vector aligned with that subspace. This directly reduces the reward head's sensitivity to hacking-related features using only a small set of contrastive gold-hacked examples, without gradient updates or fine-tuning. Comprehensive experiments across eight reward models indicates that \model improves hacking robustness, outperforms fine-tuning baselines, and preserves reward-models' general capability. Further analyses suggest that reward hacking is better captured as a multidimensional residual-space structure than by isolated surface cues.

---


### 69. [DMT-CBT: Longitudinal Therapeutic State Modeling for CBT Counseling](https://arxiv.org/abs/2606.03132)

**<font color=#1a73e8>作者：</font>** Chang Liu, Shuyi Zhang, Changsheng Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown growing potential for Cognitive Behavioral Therapy (CBT) counseling. However, most existing approaches still formulate counseling as a local response generation problem, focusing on empathetic replies within short, text-only, or single-session interactions. We argue that this formulation fundamentally mismatches the nature of real psychotherapy. In clinical CBT, therapy is a longitudinal process in which therapists continuously infer, update, and intervene on evolving therapeutic states across sessions. Realistic CBT further involves multimodal inference and delayed cross-session intervention effects, requiring models to capture longitudinal therapeutic state evolution under partial observability. We propose DMT-CBT, a framework for Dynamic Modeling of evolving Therapeutic states in CBT counseling. DMT-CBT maintains structured therapeutic states across sessions while incorporating multimodal behavioral grounding and tool-augmented intervention to support adaptive therapeutic reasoning. Based on this framework, we construct DMTCorpus, a synthetic multi-session multimodal CBT counseling dataset featuring evolving therapeutic states, image-grounded client behaviors, and cross-session intervention continuity. Experimental results show that DMT-CBT improves counseling fidelity and therapeutic alliance, produces more favorable longitudinal affective trajectories, and preserves therapeutic states more faithfully than post-hoc extraction approaches.

---


### 70. [Uncertainty-Aware Clarification in LLM Agents with Information Gain](https://arxiv.org/abs/2606.03135)

**<font color=#1a73e8>作者：</font>** Mengyi Deng, Zhiwei Li, Xin Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents often operate under underspecified user instructions, where latent uncertainty over user intent leads to erroneous tool actions. To address this challenge, we propose a goal-oriented clarification framework that aligns clarification behavior with ambiguity resolution. Central to our approach is the Information Gain Reward, a metric that quantifies the utility of clarification questions by measuring the Bayesian belief update towards the ground-truth goal induced by the clarification exchange. We train the clarifier (LLM) using this reward to optimize for high information gain, ensuring that clarifications effectively reduce uncertainty and improve task completion within the agent-tool-user environment. We validate our framework within a clarification-enhanced $\tau$-Bench environment, conducting cross-agent evaluations across five heterogeneous backbones. Empirical results demonstrate that our method consistently improves the success rate by 3.7\% over the no-clarification baseline, while adding only 0.3 total interaction steps on average.

---


### 71. [Disentangling Visual and Factual Correctness in LVLMs' Visualization Literacy](https://arxiv.org/abs/2606.03142)

**<font color=#1a73e8>作者：</font>** Soohyun Lee, Jaeyoung Kim, Seokhyeon Park 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) show strong visualization interpretation, yet it is unclear whether their responses reflect genuine reasoning over visual evidence or factual priors learned during training. Current evaluations mix these two sources, obscuring when correct visual interpretation is overridden by memorized facts. We present a framework that isolates visual correctness from factual correctness, revealing validity limitations in existing visualization literacy assessments. Across three experiments with 15 state-of-the-art LVLMs: (1) several models reach human-level performance on standard tests (VLAT), but this may reflect factual recall rather than visual understanding, while randomized-data tests (reVLAT) underestimate literacy when correct visual interpretation is superseded by factual priors. (2) Using our Counterfactual Visualization Literacy Assessment Test (CVLAT) with capability-normalized arbitration metrics, we classify models by the sign of their visual-factual reliance index (VFRI), revealing a visualization-oriented majority and a factual knowledge-oriented minority, though several near-zero cases warrant caution. A human baseline (N=30) on the same counterfactual items confirms that people overwhelmingly follow the chart under conflict, providing a human reference point. (3) Prompt-based intervention can shift prioritization, but its effectiveness is highly model-dependent and direction-asymmetric, and high chart-reading capability does not predict prompt-controllability. Overall, high visualization accuracy is not sufficient evidence of faithful visual reasoning: reliable integration into visual analytics requires evaluating not only visualization literacy but also how models arbitrate between visual evidence and factual priors when the two diverge. Benchmark and code: this https URL

---


### 72. [FederatedSkill: Federated Learning for Agentic Skill Evolution](https://arxiv.org/abs/2606.03143)

**<font color=#1a73e8>作者：</font>** Jingbo Yang, Guanyu Yao, Yang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern LLM agents increasingly rely on skill libraries to handle complex tasks, making skill evolution a primary driver of self-improvement. However, isolated single-user task streams lack the diversity required to build comprehensive skills. While cross-user collaboration can overcome this data bottleneck, current trajectory-sharing approaches compromise user privacy and impose a uniform global library that fails to accommodate client heterogeneity. We introduce FederatedSkill, a privacy-preserving framework for collaborative agent evolution. Moving beyond raw trajectory sharing, FederatedSkill utilizes semantic skill diffs, structured patches over local libraries, as the fundamental unit of communication. On the server side, an evolution agent aggregates these patches to dynamically model client-specific capability boundaries, facilitating strictly personalized skill evolution rather than a suboptimal global average. Evaluated across 20 distinct agent task families, FederatedSkill demonstrates substantial gains over self-evolving baselines, achieving up to a 44.4% increase in success rate and a 37.5% reduction in computational cost.

---


### 73. [GTBench: A Curriculum-Grounded Benchmark for Evaluating LLMs as Mathematical Research Assistants in Graph Theory](https://arxiv.org/abs/2606.03144)

**<font color=#1a73e8>作者：</font>** Noujoud Nader, Ibrahem Aljabea, Patrick Diehl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as self-study assistants in technical disciplines, yet their reliability as mathematical reasoning assistants remains poorly understood. We introduce GTBench, a curriculum-grounded benchmark for evaluating LLMs as mathematical research assistants in graph theory, comprising 63 problems organized into three groups of increasing difficulty: undergraduate definitions and basic properties (Group 1), algorithm tracing and structural reasoning (Group 2), and graduate-level proof construction (Group 3). Problems are sourced from verified academic materials including Diestel's Graph Theory. We evaluate five frontier models -- GPT-5, Claude Sonnet 4.6, Gemini 2.5 Flash-Lite, Llama 3.3 70B, and Mistral Large 3 -- under zero-shot and chain-of-thought prompting, using exact-match and LLM-as-judge evaluation for Groups 1 and 2, and a hybrid human expert and LLM-as-judge protocol for Group 3. Our results reveal a pronounced performance hierarchy: GPT-5 approaches ceiling on Group 1 (95.8% zero-shot) and maintains meaningful accuracy on graduate proofs (82%), while all other models degrade substantially with difficulty, with Llama achieving 0% under human evaluation on Group 3 zero-shot. Failure mode analysis shows that correct algorithm, wrong execution errors dominate Groups 1 and 2, while Group 3 additionally surfaces incomplete reasoning failures and reveals systematic disagreement between human evaluators and the automated judge, particularly on verbose or near-complete proofs (kappa = 0.48-0.83 across human pairs). GTBench provides the first curriculum-grounded evaluation framework for graph-theoretic reasoning in LLMs, with direct implications for the governance of AI tools in mathematical education and scientific research.

---


### 74. [ClinicalMC: A Benchmark for Multi-Course Clinical Decision-Making with Large Language Models](https://arxiv.org/abs/2606.03157)

**<font color=#1a73e8>作者：</font>** Ruihui Hou, Siyi Zhu, Ziyue Huai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have been widely adopted in healthcare, yet they still encounter significant challenges in complex clinical decision-making scenarios. Existing benchmarks primarily assess LLM performance in single-course settings and lack systematic evaluation in multi-course scenarios, where a patient's condition evolves over time. To address this gap, we propose ClinicalMC, a benchmark for multi-course clinical decision-making. It includes 1,275 Chinese and 5,804 English samples across four stages from admission to discharge. These stages cover triage, first-course examination/diagnosis/treatment, subsequent multi-course examination/assessment/treatment, and final diagnosis. In ClinicalMC, patients in the English dataset undergo an average of 5.11 clinical courses, whereas those in the Chinese dataset undergo 3.42. To assess LLM performance, we construct a multi-agent evaluation framework that includes patient, examiner, and doctor agents. Based on the benchmark and framework, we design two experimental settings -- a single-turn static setting and a multi-turn dynamic setting -- and assess three categories of LLMs: 1) closed-source LLMs like GPT5-mini; 2) open-source LLMs like DeepSeek-V3.2; and 3) medical LLMs like HuatuoGPT-o1. Through extensive evaluation, we aim to better understand LLM performance in the medical domain and support its effective deployment in healthcare.

---


### 75. [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159)

**<font color=#1a73e8>作者：</font>** NVIDIA, Aarti Basant, Amlan Kar 等 34 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As autonomous vehicle capabilities advance, the safe evaluation of driving policies in long-tail scenarios remains a critical bottleneck. In closed-loop simulation, the driving policy model actively interacts with the environment, where its actions dynamically update the simulator state and directly influence the next set of generated sensor observations. While recent reconstruction-based neural simulators offer photorealism, they are fundamentally constrained by their initial captured data and struggle to generalize to highly dynamic or novel scenes. To overcome these limitations, we introduce OmniDreams, a foundation generative world model mid- and post-trained from the Cosmos diffusion model to autoregressively generate action-conditioned videos in real time. By leveraging the rich visual priors of Cosmos and mid- and post-training on 21k hours of driving scenarios, OmniDreams synthesizes complex, unobserved phenomena that are hard for traditional simulators to capture, such as extreme weather and unpredictable dynamic agent behaviors. Crucially, it autoregressively conditions its photorealistic sensor generation on past frames, the current simulator state, and immediate driving actions. Deployed in a closed-loop system with the Alpamayo 1 policy model and AlpaSim orchestrator, OmniDreams acts as a highly responsive, reactive environment, providing a scalable and comprehensive solution for training and evaluating next-generation autonomous driving policies. We additionally show preliminary results indicating that a world-action model (WAM) post-trained from OmniDreams achieves strong performance on the Physical AI Autonomous Vehicles NuRec dataset, surpassing the VLA-based Alpamayo 1.5 research policy model while using only 1/5 the total parameters. These results highlight the potential for a real-time world model like OmniDreams to also serve as a backbone for policy architectures.

---


### 76. [Fully Automated Identification of Lexical Alignment and Preference-Stage Shifts in Large Language Models](https://arxiv.org/abs/2606.03165)

**<font color=#1a73e8>作者：</font>** Thomas Stephan Juzek, Xiaoyang Ming, Jose A. Hernandez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The language used by digital chat assistants such as ChatGPT can diverge from human expectations (misalignment). Research, mostly on Scientific English, has described both what divergences occur and, to some extent, why, linking them to the training stage of human preference learning. Yet, existing approaches rely on manual curation. This paper introduces two curation-free, assumption-light evaluation metrics: the Lexical Alignment Score, which identifies lexical overuse, and the Triangulated Preference Shift, which quantifies how much of such shifts can be attributed to human preference learning. Using PubMed abstracts, continuations were generated and measured using windowed document prevalence across six model families (Falcon, Gemma, Llama, Mistral, OLMo, Yi). The procedure identifies, without manual intervention, overused items such as 'suggest', 'additionally', and 'strategy', and estimates their link to preference learning. Our findings replicate prior work and remain stable across parameter settings, random seeds, and evaluation on further data. The approach scales readily and enables systematic study of lexical (mis)alignment beyond Scientific English and across languages, and as such, the metrics have the potential to contribute to improved alignment for future models and understanding of its origins.

---


### 77. [JAVEDIT: Joint Audio-Visual Instruction-Guided Video Editing with Agentic Data Curation](https://arxiv.org/abs/2606.03168)

**<font color=#1a73e8>作者：</font>** Yinan Chen, Chuming Lin, Zhennan Chen 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While instruction-based video editing has seen significant progress, joint audio-visual editing remains constrained by the absence of dedicated datasets and benchmarks. To bridge this gap, we present JAVEdit-100k, the first large-scale, high-quality dataset tailored for instruction-guided joint audio-visual editing. Focusing on human-centric videos, JAVEdit-100k comprises approximately 100K editing triplets spanning five distinct categories, including subject editing and speech editing. This dataset is rigorously constructed via four meticulously designed generation pipelines, seamlessly paired with an agent-in-the-loop quality control mechanism. Furthermore, to address the lack of standardized evaluation within the field, we introduce JAVEditBench, a comprehensive benchmark featuring curated source videos and human-aligned instructions across all editing categories. Finally, we propose JAVEdit, a pioneering baseline model for instruction-guided joint audio-visual editing. Experiments show that \model\ outperforms all baselines on five of six evaluation metrics.

---


### 78. [HyperPatch: Sequential Knowledge Editing Under n-ary Structural Drift](https://arxiv.org/abs/2606.03179)

**<font color=#1a73e8>作者：</font>** Yu-Kai Chan, Wen-Sheng Lien, Dong-Ting Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) rely on Knowledge Editing (KE) to maintain temporal validity, yet real-world knowledge is inherently n-ary. We demonstrate that in non-stationary environments, sequential updates to complex relations induce N-ary Structural Drift, a phenomenon where the binary reification of n-ary events into triples fractures relational atomicity. This precipitates Structure-Conditioned Knowledge Transfer Failure, a systematic mis-grounding of the retriever frequently misdiagnosed as parametric hallucination. To tackle this, we propose HyperPatch, a parameter-preserving framework that reformulates sequential KE as a stability problem over hypergraph manifolds. HyperPatch preserves event integrity through three phases: (i) Structural Prior Initialization, establishing a topology-aware embedding space via contrastive learning on a Hypergraph Neural Network (HGNN) to capture high-order correlations; (ii) Sequential Topology Editing, utilizing a dual-stage mechanism that employs SimHash-based Topological Alignment for rapid conflict resolution and Topological LoRA Adaptation to track drift without backbone retraining; and (iii) Structure-Conditioned Reasoning, which integrates globally consistent evidence from fused linguistic and structural manifolds. On the MQuAKE-CF and MQuAKE-T benchmarks, HyperPatch achieves relative gains in Hop-wise Accuracy (H-Acc) of 96.24% and 21.06% over the strongest baseline, respectively. Further ablations demonstrate superior reliability under continuous n-ary update streams, whereas the standard KG-based variant suffers H-Acc collapses of up to 88.3% due to structural misalignment.

---


### 79. [GLINT: Sparsely Gated Vision-Language Alignment for Fine-Grained Radiology Representations](https://arxiv.org/abs/2606.03180)

**<font color=#1a73e8>作者：</font>** Jonggwon Park, Seongeun Lee, Junhyun Park 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) for radiology have emerged as a scalable paradigm by leveraging image-report pairs naturally produced in clinical workflows. However, this pairing reveals a mismatch in scale: each finding occupies only a small region of the image, yet supervision is provided only at the global image-report level. This poses a central challenge: prior approaches spread weight densely across all patches rather than concentrating on the sparse subset relevant to a given query. To address this, we present GLINT (Gated Language-Image alignmeNT), a framework that explicitly models this sparse correspondence. On the alignment side, we introduce Sparsely Gated Alignment, a novel architecture in which a sigmoid gate over a separate gate embedding space activates only the patches relevant to each textual query, enforcing explicit sparsity. On the representation side, we add Dense Feature Regularization, which anchors the trainable encoder's intermediate features to a frozen self-supervised learning (SSL) teacher, preserving the fine-grained patch features that the gate relies on. The same recipe applies to both 2D chest X-ray (CXR) and 3D chest computed tomography (CT), built with DINOv3 and V-JEPA 2.1, respectively. GLINT enables zero-shot classification, grounding, and segmentation from free-text queries, and to our knowledge is the first to demonstrate zero-shot segmentation on 3D CT volumes without mask supervision. Notably, the most pronounced gains arise on zero-shot grounding and segmentation, where sparse, query-specific localization is required, consistent with our design intent. In downstream evaluation, GLINT outperforms both SSL encoders and medical VLMs on classification, report generation, and segmentation.

---


### 80. [MemTrain: Self-Supervised Context Memory Training](https://arxiv.org/abs/2606.03197)

**<font color=#1a73e8>作者：</font>** Ziheng Li, Xingrun Xing, Haoqing Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory is an indispensable capability for long-horizon LLM agents, enabling them to preserve and utilize information accumulated across extended interactions. Existing memory-agent approaches are typically trained end-to-end with reinforcement learning on downstream tasks. However, collecting high-quality annotated problems for memory-intensive scenarios is costly, and the resulting training data often lack sufficient diversity to cover general memory behaviors. In this work, we propose MemTrain, a self-supervised training framework for generally enhancing the context-memory capability of LLM agents for more effective downstream post-training. MemTrain introduces two coupled proxy tasks over unlabeled Wikipedia corpora: (1) an end-to-end masked reconstruction objective, which requires the model to recover masked entities after multiple rounds of memory updates, thereby encouraging memory maintenance from the final outcome perspective; and (2) an intermediate memory recall objective, which requires the model to reconstruct masked historical information using intermediate memory states, encouraging faithful compression and memory completeness throughout the interaction process. The two objectives are jointly optimized using GRPO. Extensive experiments on long-text QA and search-based QA benchmarks demonstrate that MemTrain consistently improves downstream memory-intensive reasoning performance across different models, achieving gains of up to 17.67 points over direct task-specific post-training.

---


### 81. [AI Rater Discrimination Depends on Scoring Protocol in Complex Clinical Decision-Making](https://arxiv.org/abs/2606.03198)

**<font color=#1a73e8>作者：</font>** Sangwon Baek, Kyu Yeon Hur, Kyunga Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical AI evaluation increasingly delegates scoring to large language models (LLMs) acting as AI raters, yet their scoring behavior across evaluation conditions has not been quantitatively characterized. We address this gap through a factorial study of AI rater behavior in adult type 2 diabetes (T2D) pharmacotherapy at 12-month outpatient follow-up, a clinical task involving complex decision-making operationalized across seven evaluation questions. Four open-source LLMs served simultaneously as clinical decision support system (CDSS) models and AI raters. Each CDSS output was scored under two scoring protocols: a rubric-anchored Gold Rubric (GR) protocol incorporating a patient-specific rubric, and a rubric-free Non Gold Rubric (Non-GR) protocol. Linear mixed effects models crossed the scoring protocol factor with five design factors -- CDSS model, CDSS prompt configuration (document-referenced generation [DRG] vs.\ Baseline), rater model, prompt character, and prompt type -- and estimated main effects together with their protocol interactions. Across all questions, AI raters yielded consistently higher scores within a very narrow range (74--78 points on average) under Non-GR compared to those under GR (7.69 to 49.64 points lower mean scores; 1.68 to 3.67 times wider interquartile ranges). Within each question, GR amplified the AI rater's discrimination between DRG and Baseline CDSS outputs by factors of 1.76 to 5.10, while also revealing substantial behavioral variation across rater models that Non-GR suppressed. These findings support rubric anchoring as the scoring protocol that preserves discriminative power in clinical AI evaluation; rubric-free scoring cannot substitute when questions require patient-specific or jurisdiction-specific criteria that rater models cannot infer from parametric knowledge alone.

---


### 82. [DECA: Decentralizing Block-Wise Adam for Efficient LLM Full-Parameter Fine-Tuning on Non-IID Data](https://arxiv.org/abs/2606.03209)

**<font color=#1a73e8>作者：</font>** Yunsheng Yuan, Shaowei Li, Kai Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models (LLMs) in privacy-sensitive and resource-constrained environments remains challenging. Since training data are often distributed across multiple clients, decentralized fine-tuning offers a natural paradigm for collaborative adaptation without a central server. However, enabling full-parameter fine-tuning (FPFT) in this decentralized setting is difficult: FPFT provides strong adaptation capacity but incurs prohibitive resource consumption for billion-scale models. Existing decentralized LLM fine-tuning methods therefore mainly rely on parameter-efficient updates, which improve efficiency but may restrict downstream performance. Moreover, client data are typically non-IID, making decentralized optimization more vulnerable to client drift and unstable convergence. To address these challenges, we propose DECA, a resource-efficient decentralized FPFT framework for LLMs on non-IID data. DECA partitions model parameters into disjoint blocks and performs sequential block-wise Adam optimization, reducing resource consumption while preserving decentralized full-parameter adaptation. To stabilize training, DECA further introduces first- and second-order block-wise moment estimates with fresh local gradient statistics and consensus-derived discrepancy signals. We provide rigorous theoretical analysis and extensive experiments, showing that DECA achieves fast convergence, strong downstream performance, and significant resource efficiency.

---


### 83. [Follow-Your-Preference++: Rethinking Preference Alignment for Image Inpainting](https://arxiv.org/abs/2606.03216)

**<font color=#1a73e8>作者：</font>** Junkun Yuan, Yutao Shen, Toru Aonishi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study preference alignment for image inpainting. Rather than proposing yet another method, we revisit the problem from first principles and reassess its core challenges. We adopt the widely used direct preference optimization framework and construct preference training data with publicly available reward models. Our empirical study spans nine reward models, two benchmarks, and two baseline inpainting models that differ in architecture and generative mechanism. Our main findings are: (1) Most reward models provide valid signals for preference data construction, although some are unreliable as evaluators. (2) Across models and benchmarks, preference data exhibits consistent trends under both candidate and sample scaling. (3) Reward models display pronounced biases--particularly in brightness, composition, and color scheme--that make them prone to inducing reward hacking. (4) A simple ensemble of reward models mitigates such biases and yields robust, generalizable performance. {\color{rebuttal_blue}(5) Preference alignment is transferable to the object removal task, where the goal shifts from open-ended creative generation to coherent background completion. (6) Further analysis reveals that a calibrated ensemble method further mitigates hacking and improves robustness.} Without modifying model architectures or introducing additional datasets, our models substantially outperform prior state-of-the-art models on standard metrics, large vision-language model evaluations, and human assessments. Our code is available at: this https URL.

---


### 84. [WebRISE: Requirement-Induced State Evaluation for MLLM-Generated Web Artifacts](https://arxiv.org/abs/2606.03220)

**<font color=#1a73e8>作者：</font>** Yuxin Meng, Yuhan Suo, Junjie Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing benchmarks for MLLM-generated web artifacts assess interaction through local evidence and miss the requirement-induced states and transitions that determine whether a page works. We introduce WebRISE, which compiles task requirements into Interaction Contract Graphs (ICGs) of observable states, user-intent transitions, and DOM/visual assertions for implementation-agnostic browser execution. WebRISE spans 442 tasks across five input modalities (Text, Markdown, Sketch, Image, Video), with 5,495 transitions and 5,271 requirement checks that separate user-stated functions from implicit product-level constraints. Across 14 MLLMs, even the strongest model reaches only 65.6% transition validity and 66.3% requirement coverage, and visual quality is no proxy for behavior (Qwen3.6-35B-A3B on Markdown: V=80.8 yet T=15.5). Video gives the strongest interaction signal (+10.6 pp implicit coverage over Text), while implicit constraints persist; defect injection shows ICG-based scoring detects state errors at 2-16x the rate of checkpoint-style evaluation.

---


### 85. [Right Makes Might: Aligning Verified Hidden States Empowers RL Reasoning](https://arxiv.org/abs/2606.03234)

**<font color=#1a73e8>作者：</font>** Ziyue Wang, Aomufei Yuan, Yongfu Zhu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Verifiable Rewards (RLVR) has become the dominant approach for improving mathematical reasoning in large language models, yet current methods reduce each correct rollout to a single reward bit, ignoring the geometric structure shared among their hidden states. Investigating this structure, we find that at the anchor token (the position immediately before the answer marker), correct rollouts converge naturally because they must produce the same answer (cosine similarity ~0.84), yet each retains residual variance from its unique reasoning path. Encouraging full alignment at this point pushes the model to extract a unified "correct decision" representation, reducing sensitivity to which reasoning path was taken. Based on this observation, we propose Hidden-Align, an auxiliary loss function that aligns the last-layer hidden states of correct rollouts at the anchor token during RL training, with zero overhead in both training and inference. On eight mathematical reasoning benchmarks, Hidden-Align improves average pass@1 over the DAPO baseline by 3.8, 6.2, and 5.4 percentage points on Qwen3-1.7B, 4B, and 14B respectively, with consistent pass@k gains across all three scales, supported by ablations on loss type, anchor position, layer depth, and loss weight.

---


### 86. [Perceive Before Reasoning: A Pre-Reasoning Perception Framework for Efficient and Reliable Proactive Mobile Agents](https://arxiv.org/abs/2606.03236)

**<font color=#1a73e8>作者：</font>** Zhijie Ding, Weinan Hong, Zicheng Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have substantially advanced mobile agents, yet proactive mobile assistance remains challenging because agents must decide \emph{when} to intervene before determining \emph{how} to assist. Existing systems often implement these two decisions within a unified MLLM-based pipeline, leading to goal misalignment between conservative intervention filtering and comprehensive assistance generation, as well as redundant inference when the agent should remain silent. To address these limitations, we propose the \textbf{Pre-Reasoning Perception Framework (PRPF)}, a two-stage framework built on perceiving before reasoning. PRPF introduces a lightweight Multimodal Proactive Perceptor (MPP) for intervention gating and context compression, and activates the Proactive Agent Reasoner (PAR) only when intervention is warranted. Experiments on the ProactiveMobile benchmark show that PRPF substantially reduces false trigger rates (FTR) while improving success rates (SR) and inference efficiency over the ProactiveMobile baseline.

---


### 87. [When RLHF Fails: A Mechanistic Taxonomy of Reward Hacking, Collapse, and Evaluator Gaming](https://arxiv.org/abs/2606.03238)

**<font color=#1a73e8>作者：</font>** Zelalem Abahana  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from human feedback (RLHF) makes large-scale post-training possible by replacing an underspecified human objective with learned and scalable proxies. The same substitution creates a structured failure surface: optimization can raise the learned reward while external quality falls, degrade both proxy and judge scores, reveal proxy under-alignment, or produce evaluator-specific disagreement. We present an empirical failure-mode study of a compact RLHF pipeline with proximal policy optimization (PPO), direct preference optimization (DPO), uncertainty-penalized PPO (UP-PPO), reward-model uncertainty, approximate policy drift, diversity and repetition diagnostics, and two external LLM judges. Rather than treating reward hacking as a single terminal event, we classify matched transitions between checkpoints using the directions of the learned reward, judge scores, and average judge score. Across 61 checkpoint rows and 1920 row-level transitions, aggressive PPO has the highest localized reward-hacking rate (14.45%; bootstrap 95% CI: 10.16-18.75), while UP-PPO yields lower rates in the same aggressive regime (11.33-10.94%). A pre-transition logistic model predicts future row-level reward hacking with ROC-AUC 0.821, and row-level analysis finds localized reward hacking that checkpoint averages miss in 3 of 12 settings. The central conclusion is methodological: RLHF failures are not only final-model pathologies, but training dynamics that can be classified, localized, and partially anticipated.

---


### 88. [Investigating Novice Researchers' Perceptions of Research Privacy Within LLM-Assisted Workflows](https://arxiv.org/abs/2606.03248)

**<font color=#1a73e8>作者：</font>** Shuning Zhang, Changxi Wen, Eve He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLMs)-assisted scholarly workflows introduce critical privacy and intellectual property risks. As a uniquely vulnerable cohort driven by publication pressure and a lack of institutional support, novice researchers rely heavily on public LLMs, compelling them to navigate high-stakes privacy-publication trade-offs. To investigate these concerns, we conducted semi-structured interviews with 44 researchers across diverse disciplines. Our findings reveal that the fear of idea leakage paradoxically accelerates, rather than deters, reliance on LLMs, as researchers utilize them to expedite publication. They also held misconceptions that their ideas lacked the unique value to attract targeted attacks, and that their inputs would be safely diluted within massive datasets, preventing reconstruction. From interviews, we identified five types of mitigations including input fragmentation and adversarial probing, though we found that participants largely perceived these measures as ineffective. We outline implications including implementing institution-level sandboxed isolation, scenario-based privacy pedagogy, and verifiable data-deletion audits for transparency.

---


### 89. [The Word and the Way: Strategies for Domain-Specific BERT Pre-Training in German Medical NLP](https://arxiv.org/abs/2606.03250)

**<font color=#1a73e8>作者：</font>** Henry He, Johann Frei, Raphael Schmitt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Digital healthcare generates vast amounts of clinical text that can support AI-assisted applications, yet German biomedical language models remain limited by older architectures or restricted training data. We present ChristBERT (Clinical- and Healthcare-Related Issues and Subjects Tuned BERT), a family of domain-specific German RoBERTa-based language models trained on a 13.5GB corpus of scientific publications, clinical texts, health-related web content, and translated clinical resources. To investigate the impact of domain adaptation strategies in German clinical NLP, we compare continued pre-training, training from scratch, and domain-specific vocabulary adaptation. The resulting models are evaluated on three medical named entity recognition tasks and two text classification tasks. ChristBERT consistently outperforms existing general-purpose and medical German language models on four of five benchmarks and establishes a new state of the art for German clinical language modeling. Our results show that the optimal adaptation strategy is task-dependent: in our evaluation, training from scratch is particularly effective for highly specialized clinical texts, whereas continued pre-training performs well on more commonly written medical texts. All models are publicly released to support future research and applications in German medical NLP.

---


### 90. [PaddleOCR-VL-1.6: Expanding the Frontier of Document Parsing with Under-Optimized Region Refinement and Progressive Post-Training](https://arxiv.org/abs/2606.03264)

**<font color=#1a73e8>作者：</font>** Zelun Zhang, Hongen Liu, Suyin Liang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce PaddleOCR-VL-1.6, an upgraded compact document parsing model built upon PaddleOCR-VL-1.5. Although PaddleOCR-VL-1.5 establishes a strong 0.9B baseline, its remaining errors concentrate in under-optimized regions where model behavior is unstable, data coverage is sparse, or supervision is unreliable. Rather than expanding the training corpus indiscriminately, PaddleOCR-VL-1.6 introduces a region-aware data optimization framework that identifies weak regions from the previous model, applies targeted enhancement to these regions, and improves the reliability of supervision signals. It further adopts a progressive post-training recipe based on curated data selection and reinforcement learning, pushing model performance to a higher level through staged optimization. PaddleOCR-VL-1.6 achieves a new state-of-the-art score of 96.33% on OmniDocBench v1.6, demonstrates strong competitiveness against top-tier VLMs, and provides a practical post-training recipe for the PaddleOCR-VL series.

---


### 91. [Distilling Answer-Set Programming Rules from LLMs for Neurosymbolic Visual Question Answering](https://arxiv.org/abs/2606.03269)

**<font color=#1a73e8>作者：</font>** Thomas Eiter, Nelson Higuera Ruiz, Johannes Oetsch  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual Question Answering (VQA) is the task of answering questions about images, requiring the integration of multimodal input and reasoning. Modular approaches that incorporate logic-based representations into the reasoning component offer clear advantages over end-to-end trained systems, particularly in terms of interpretability. However, adapting or extending these representations when task requirements change can place a significant burden on developers. To address this challenge, we present an approach for distilling rules from Large Language Models (LLMs). Our method prompts an LLM to extend an initial VQA reasoning theory, expressed as an answer-set program, to meet new requirements of the task. Examples from VQA datasets guide the LLM, validate the results, and help correct erroneous rules by leveraging feedback from the ASP solver. We demonstrate that our approach is effective across diverse VQA datasets. Notably, only a few examples are needed to elicit correct rules from LLMs. Our experiments suggest that rule distillation from LLMs is a promising alternative to traditional data-driven rule learning approaches. Under consideration in Theory and Practice of Logic Programming (TPLP).

---


### 92. [Are Common Substructures Transferable? Riemannian Graph Foundation Model with Neural Vector Bundles](https://arxiv.org/abs/2606.03270)

**<font color=#1a73e8>作者：</font>** Li Sun, Zhenhao Huang, Yiding Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models have sparked a revolution via a pretraining-adaptation paradigm, with recent efforts extending this success to graphs. Unlike other modalities, graphs contain rich structural patterns, yet their structural transferability remains poorly understood. Prior studies consider common substructures in the discrete realm, and we are motivated by a fundamental question: Are common substructures transferable? The underlying theory is largely underexplored. In this work, we shift toward learning transferable structures through the lens of functional behavior. Theoretically, we connect transferable substructures to intrinsic geometry of the representation space. However, characterizing such intrinsic geometry has rarely been touched. Grounded in Riemannian geometry, we develop a graph intrinsic geometry learning framework called Neural Vector Bundle, which enables parsing intrinsic geometry with local coordinates. Building on this, we design GAUGE, a pretrainable neural architecture that constructs the vector bundle, flattening geometrically compatible local coordinates, and a new Dirichlet loss, which also measures the transfer effort. We empirically validate its superior expressiveness in challenging tasks including zero-shot link prediction and graph isomorphism.

---


### 93. [Agentic Relationship Harm: Benchmarking and Gating Relational Manipulation in AI Agents](https://arxiv.org/abs/2606.03271)

**<font color=#1a73e8>作者：</font>** Pei-Sze Tan, Tasuku Igarashi, Isao Echizen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI agents built on large language models can assist not only legitimate tasks but also relational manipulation. AI agents can be used to help a user maintain a deceptive identity, intensify emotional dependency, isolate a target, or prepare for later extraction. We conceptualise this risk as agentic relationship harm: workflow-level assistance that can exploit recipient vulnerability, persuasive influence, and relational power asymmetry. Existing safety evaluations and generic guardrails often treat harmfulness as a property of isolated outputs, missing role-sensitive interaction patterns. To study this, we introduce a 110-prompt benchmark with balanced attacker- and victim-side cases, a relationship-specific labelling framework, and a lightweight post-generation policy gate for local agent deployments. In our evaluation, the relationship-specific gate outperforms generic safety prompting under automated judging, with no judge-identified harmful-compliance cases on the main benchmark or multi-turn stress test while preserving victim-side protective intervention. These results suggest that relationship harm is a distinct sociotechnical risk surface and that role-sensitive evaluation plus lightweight policy gating offers a practical path beyond generic refusal prompting.

---


### 94. [Multilingual Unlearning in LLMs: Transfer, Dynamics, and Reversibility](https://arxiv.org/abs/2606.03291)

**<font color=#1a73e8>作者：</font>** Chaoyi Xiang, Olga Ohrimenko, Benjamin I. P. Rubinstein 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can memorize sensitive facts, motivating unlearning methods that remove targeted knowledge without costly retraining. However, unlearning research remains heavily English-centric. We study multilingual unlearning by extending the TOFU benchmark to five languages, and fine-tune, unlearn, and query our models with different permutations of languages. We find that unlearning transfer, the ability of an unlearned model to "forget" facts in languages other than the unlearning language, is highly variable: e.g., it is strongest between languages sharing scripts and families, and we show that the unlearning language predicts which query languages are most likely to yield the strongest transfer. Layer-wise analysis reveals that unlearning leaves the shared cross-lingual latent space largely intact in early layers, instead operating primarily in later decoding layers. This suggests that unlearning does not truly erase knowledge, but rather induces superficial suppression. Exploiting this structure, a single inference-time steering direction reverses much of this suppression across languages, recovering 50% (Qwen) and 90% (Gemma) of the unlearned knowledge.

---


### 95. [LEAP: Supercharging LLMs for Formal Mathematics with Agentic Frameworks](https://arxiv.org/abs/2606.03303)

**<font color=#1a73e8>作者：</font>** Po-Nien Kung, Linfeng Song, Dawsen Hwang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) exhibit strong informal mathematical reasoning but struggle to generate mechanically verifiable proofs in formal languages like Lean. We present LEAP, an agentic framework that enables general-purpose foundation models to achieve state-of-the-art performance on automated formal theorem proving. LEAP leverages foundation model capabilities, such as informal reasoning, instruction following, and iterative self-refinement. By decomposing complex problems into smaller units, the system bridges formal proof construction with informal blueprints through continuous interaction with the Lean compiler. To provide a rigorous evaluation beyond increasingly saturated benchmarks, we introduce Lean-IMO-Bench, a benchmark of IMO-style problems formalized in Lean, with short statements yet highly non-routine and multi-step proofs across a wide range of difficulty levels. Empirically, on the latest 2025 Putnam Competition, an annual mathematics competition for undergraduate students in North America, LEAP solves all 12 problems, matching recent breakthroughs by frontier formal mathematical models. On Lean-IMO-Bench, LEAP boosts the one-shot formal solve rate of general-purpose LLMs from below 10% to 70%, notably surpassing the 48% benchmark set by a specialized, gold-medal-caliber IMO system. Furthermore, we demonstrate LEAP's research-level utility by autonomously formalizing complex proofs for open combinatorial challenges, including a verified proof for a key subproblem in Knuth's Hamiltonian decomposition of even-order Cayley graphs.

---


### 96. [From Script to Semantics: Prompting Strategies for African NLI](https://arxiv.org/abs/2606.03304)

**<font color=#1a73e8>作者：</font>** Anuj Tiwari, Terry Oko-odion, Hannah Nwokocha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly evaluated in multilingual settings, yet their inference behavior in low-resource African languages remains underexplored especially under pure prompting without fine-tuning. We present a systematic study of prompting strategies for Natural Language Inference (NLI) in Swahili, Yoruba, and Hausa using the AfriXNLI benchmark. We evaluate five prompting strategies Baseline (zero-shot), Script-Aware, Language Specific, Contrastive, and Native-Label Self-Translation (NL-STP) across two mid-sized open weight models (Llama3.2-3B and Gemma3-4B). To isolate the effect of prompt design, the effect of few-shot examples and Chain-of-Thought reasoning is eliminated in our study. We find a significant difference in performance of class wise across strategies with highly neutral class collapse and high prediction skew in some configurations. Contrastive prompting proves to be the most reliable and steadily improving strategy over language and model and has better balance of class behavior and balance of overall accuracy gains. Notably, well-constructed prompts are sufficient to beat more powerful baselines that are provided with few-shot prompts and Chain-of-Thought prompts. We have found that prompt formulation is essential to multilingual NLI with low-resource languages and that language aware decision structuring can be used to meaningfully enhance robustness in resource challenged settings.

---


### 97. [A Graph Foundation Model with Spectral Parsing and Prototype-Guided Spatial Propagation](https://arxiv.org/abs/2606.03315)

**<font color=#1a73e8>作者：</font>** Ankang Yang, Jitao Zhao, Dongxiao He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph foundation models aim to learn transferable knowledge from diverse graphs for generalization to unseen graphs and tasks. Unlike text and images, graphs lack a shared vocabulary or regular spatial grid, making cross-graph transfer challenging. This challenge comes from both feature discrepancies and, more critically, diverse graph structures. Existing GFMs mainly improve transferability by unifying feature spaces or incorporating structural tokens and vocabularies. However, existing topology-aware designs still have limitations. Structural tokens are usually discrete, while structural vocabularies often rely on predefined substructures such as trees and cycles, whose limited coverage may miss richer relational patterns across graphs. Moreover, graph signals contain both high-frequency local patterns and smoother low-frequency patterns, which require different propagation behaviors. These components are often entangled in raw graph signals, while this spectral perspective is rarely explored in existing GFMs. To address these challenges, we propose SPG, a graph foundation model with spectral parsing and prototype-guided spatial propagation. SPG applies learnable Chebyshev filters to decompose node features into multiple spectral responses, reducing the mismatch between frequency-specific graph signals and propagation behaviors. It then constructs a Gromov-Wasserstein prototype geometry to distill transferable pairwise relations beyond predefined substructures into a shared structural space. The learned prototype geometry is further projected back as a prototype-guided propagation operator. Experiments demonstrate consistent improvements in cross-domain generalization.

---


### 98. [Beyond Ideal Instruction: A Comprehensive Framework for Evaluating LLMs in Realistic Interactions](https://arxiv.org/abs/2606.03318)

**<font color=#1a73e8>作者：</font>** Xuan Yang, Hao Xu, Tingfeng Hui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite great advances in tool-use capabilities of large language models (LLMs), existing evaluation benchmarks struggle to fully align with real-world scenarios. Such benchmarks mostly rely on simulated idealized user assumptions and lacks experience-oriented evaluation. These limitations fail to account for the ambiguity, uncooperative behaviors, and shifting intentions characteristic of real-world users. To fill this gap, we propose RUT-Bench, a dedicated benchmark designed to assess LLMs under diverse Real-world User Tool calling scenarios. RUT-Bench supports high-fidelity simulations covering both ideal rational patterns and heterogeneous non-ideal behaviors across single-turn and multi-turn dialogues. We conduct comprehensive evaluations on 19 widely adopted open-source and proprietary LLMs using our benchmark. Experimental results reveal that no tested LLMs achieve an overall success rate above 40%, and nearly all of them experience noticeable performance drops when facing more complicated non-ideal user inputs. Our code and data is available at this https URL.

---


### 99. [Calibration Data Trade-offs Across Capability Dimensions: Why Multi-Source Mixing Matters for High-Sparsity LLM Pruning](https://arxiv.org/abs/2606.03328)

**<font color=#1a73e8>作者：</font>** Hu Xu, Zhaolong Xing, Congcong Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training pruning compresses large language models to high sparsity using a small unlabelled calibration set, and recent work has concluded that the choice of calibration source has only modest impact on averaged post-pruning accuracy. We ask whether this conclusion survives once calibration impact is evaluated separately across distinct capability dimensions rather than aggregated. Decomposing post-pruning capability into General, Commonsense, Code, and Math, and analysing $n{=}15$ calibration sources via Spearman correlations between OIT information metrics and per-dimension retention, we uncover an opposite-sign trade-off: calibration perplexity correlates positively with General retention ($\rho{=}{+}0.71$) but negatively with Math and Code retention ($\rho{=}{-}0.53,\,{-}0.59$; $p{<}0.05$), so no single source can preserve all capabilities. We respond with multi-source calibration mixing, and propose IGSP, an information-guided self-calibration protocol that automates multi-source construction without capability-aligned corpora by minimising 4-gram aggregation and balancing perplexity across dimensions. On LLaMA-3.1-8B at SparseGPT 60% sparsity, a uniform multi-source mix reaches 58.8% total retention, outperforming the best single source (MetaMath, 50.0%) by $+8.8$ and the C4 default (40.0%) by $+18.8$; IGSP improves over Self-Cal by $+2.4$ and SGS by $+4.8$.

---


### 100. [FLIPS: Instance-Fingerprinting for LLMs via Pseudo-random Sequences](https://arxiv.org/abs/2606.03330)

**<font color=#1a73e8>作者：</font>** Gurvan Richardeau, Gohar Dashyan, Erwan Le Merrer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Literature reveals that a Large Language Model's (LLM) behavior is not only conditioned by its original weights but also its instance-level parameters, such as instructional prompt, sampling configuration or quantization. A model that generates safe outputs under one configuration may produce toxic content under another. However, current LLM identification techniques (such as fingerprinting) focus on intellectual property protection, and their design favors robustness to changes in these instance-level parameters. This poses a critical challenge for AI regulation in which compliance assessments target actual deployed behaviors, not model provenance. In this paper, we introduce instance-level fingerprinting, a regulator-oriented paradigm that distinguishes configurations of the same LLM. Our method FLIPS, exploits biases in generated binary random sequences to reach 96% (closed-set) and 90% (open-set, where some targets are unknown) identification accuracy across 237 model instances, versus 35% for the adapted LLMmap baseline. This shows that instance-level fingerprinting is both necessary for regulation and practically feasible. Code available at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-188](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
