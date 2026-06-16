# 🧠 大模型相关研究 | 2026年06月17日

> 本类共 **270** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-270](./part-06.md)

---

### 201. [Unified Multimodal Model for Brain MRI Imputation and Understanding](https://arxiv.org/abs/2606.16484)

**<font color=#1a73e8>作者：</font>** Zhiyun Song, Che Liu, Tian Xia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) hold great potential for medicine, as they inherit knowledge from LLM and allow multiple data modalities to be integrated, analysed and interpreted in natural language. However, the field of medical MLLMs is constrained by non-trivial challenges, notably the scarcity of high-quality training data and the frequent occurrence of missing data in the real-world clinical setting. Here, we propose a novel unified multimodal model, UniBrain, for brain magnetic resonance image (MRI) analysis. To address potential missing brain MRI modalities, we employ a unified training strategy to perform joint imaging modality imputation and brain image understanding. During training, an interleaved and description-enriched data flow is constructed to train the model in an autoregressive manner, enabling medical reasoning with generated multimodal data. A self-alignment strategy is introduced to leverage dense image embeddings to learn fine-grained anatomical features without requiring detailed image captions. Furthermore, we propose a dynamic hidden state mechanism to alleviate the exposure bias during long-context multimodal inference. Extensive experiments on multi-disease brain MRI dataset demonstrate that UniBrain achieves high performance for brain image imputation, understanding, and disease diagnosis under various extents of modality incompleteness.

---


### 202. [BRICKS-WM: Building Reusability via Interface Composition Kinetics for Structured World Models](https://arxiv.org/abs/2606.16489)

**<font color=#1a73e8>作者：</font>** Shaowei Zhang, Jiahan Cao, Xunlan Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based Reinforcement Learning (MBRL) has achieved remarkable success in continuous control by leveraging latent world models. However, prevailing approaches typically rely on monolithic latent dynamics, entangling environment dynamics into a coupled process. This coupling severely limits reusability: altering the agent necessitates retraining the entire world from scratch, even if the environment remains constant. To address this, we introduce BRICKS-WM (Building Reusability via Interface Composition Kinetics for Structured World Models), a framework for the modular assembly of structured world models. Driven by the insight that the physical world is composed of independent entities, we posit that global dynamics can be modeled as a composition of distinct dynamical modules interacting via latent interfaces. As a minimal instantiation, we factorize the latent state space into an actuated Agent module and an external Background module, bridged by a learned latent interface. Unlike prior object-centric methods that prioritize visual segmentation, BRICKS-WM enforces a functional separation in transition dynamics, ensuring that background dynamics remains agnostic to the agent's dynamics. Empirically, BRICKS-WM achieves control performance comparable to strong monolithic baselines when trained from scratch, and enables the reuse of frozen background dynamics across agents.

---


### 203. [Lost at the End: Primacy Bias in Multimodal Retrieval-Augmented Question Answering](https://arxiv.org/abs/2606.16494)

**<font color=#1a73e8>作者：</font>** Jieyuan Liu, Jianyang Gu, Shijie Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge-based visual question answering (KB-VQA) lets vision-language systems answer questions that exceed their parametric knowledge by conditioning a reader on passages retrieved from a Wikipedia-scale knowledge base. In pure-text long-context LLMs, retrieved-context use follows the U-shaped "lost-in-the-middle" effect of Liu et al. (2024): information at the start and end of context is used, the middle is lost. Whether this transfers to deployed multimodal KB-VQA is open. To close this gap, we design the first controlled probe of reader-side position dependence in multimodal KB-VQA: a gold-position protocol in which only the gold passage's prompt slot varies within question. We run it on three open-source 7B/8B VLM readers and two KB-VQA benchmarks at k up to 20. The shape flips from U to primacy: gold-at-first beats gold-at-last by 16 to 26 points on every reader-by-benchmark cell, an effect we call "Lost at the End". Three targeted ablations narrow the cause: a text-only control shows the multimodal setting amplifies an already-present text-mode primacy 2.2 to 4.5 times, and image-position and distractor-shuffle ablations together pin the locus to prompt slot 0 of the instruction-tuned reader. On a frozen reader, three retrieval-side fixes (MMR, oracle reranking, rank-based reordering) all leave the gap intact (no separable improvement). Our findings indicate that recall@k is the wrong metric for deployed KB-VQA and that closing the gap requires reader-side intervention; we release our protocol as a controlled instrument for evaluating such interventions.

---


### 204. [REFLEX: Reflective Evolution from LLM Experience](https://arxiv.org/abs/2606.16496)

**<font color=#1a73e8>作者：</font>** Pan Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large multimodal language models (LLMs) have emerged as powerful tools for guiding evolutionary search toward interpretable programmatic policies. However, existing frameworks rely on a monolithic model call to simultaneously interpret visual behavioral evidence and synthesize corrective code. This diagnosis-repair entanglement creates an opaque feedback loop, obscuring the rationale behind mutations and preventing the retention of algorithmic insights across independent runs. To achieve auditable and efficient policy search, we argue that visual diagnosis must be structurally decoupled from code generation. We present REFLEX, a train-free evolutionary framework that operationalizes this decoupling. In REFLEX, a vision-enabled Critic first distills task-specific behavioral evidence into structured, auditable diagnoses. Subsequently, a text-optimized Actor synthesizes child policies using these diagnoses alongside a persistent, self-evolving Skill Memory of reusable code snippets. This architecture not only provides transparent mutation traces but also enables cross-run programmatic knowledge transfer. Extensive evaluations across control benchmarks (Lunar Lander, Acrobot, Pendulum) and a 36-dimensional antenna array synthesis task demonstrate exceptional sample efficiency. Notably, REFLEX solves Acrobot and Pendulum in under 10 LLM calls and reaches a best Normalized Weighted Score of 1.092 on Lunar Lander, achieving highly competitive final performance while significantly accelerating the early-stage discovery of transparent policies.

---


### 205. [Post-Hoc Merging is Not Enough: Many-Shot Model Merging with Loss-Gap Balancing](https://arxiv.org/abs/2606.16501)

**<font color=#1a73e8>作者：</font>** Kyungjin Im, Miru Kim, Chanin Eom 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model merging has become a practical post-training strategy for building a single multi-task large language model (LLM) by combining multiple task-specialized models. However, most existing approaches rely on post-hoc merging, in which task-specific models are merged only once after training. This one-shot aggregation often suffers from task interference, leading to information erasure across individual tasks. In this work, we show that replacing post-hoc merging with an iterative many-shot merging protocol is effective in improving multi-task performance. Building on this insight, we propose METIS, Mitigating Erasure from Task Interference for Stable many-shot merging. METIS is a loss-aware many-shot merging method that addresses information erasure in post-hoc merging through task-wise loss-gap weighting and consensus-based masking. Notably, METIS exhibits significant performance improvement on the worst-performing task, effectively mitigating information erasure. (Project page: this https URL)

---


### 206. [Tail-Shape Estimation in LLM Evaluation Is Fragile: A Protocol for Diagnosing False Positives](https://arxiv.org/abs/2606.16511)

**<font color=#1a73e8>作者：</font>** Luca Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work motivates moving large language model (LLM) evaluation from mean-based to tail-aware metrics, including conditional value-at-risk and tail-index estimates of reward-model error. We ask whether the canonical extreme-value-theory tail-index parameter, which isolates how heavy a tail is from how large the tail mass is, adds discriminative information beyond the mean and a standard tail-magnitude statistic in LLM evaluation. We pre-register a protocol covering admissibility, goodness-of-fit, threshold-stability, and effect-size requirements for any positive tail-shape claim. The protocol is the contribution of this paper; the empirical study below is a demonstration of what its gates catch. Applied to a standard LLM toxicity-evaluation setup under two structurally different scorer families, the protocol catches three distinct modes of false positives that a naive analysis would have published, and rejects the headline tail-shape claim on both scorers. We conclude that tail-shape estimation in the LLM toxicity-evaluation setups we examined is more fragile than the recent literature suggests, and recommend the protocol as a starting point for tail-index claims in similar setups.

---


### 207. [How Post-Training Shapes Biological Reasoning Models](https://arxiv.org/abs/2606.16517)

**<font color=#1a73e8>作者：</font>** Lukas Fesser, Hanlin Zhang, Michelle M. Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific reasoning models for biology combine language models with foundation models trained on multimodal biological data, including DNA, RNA, and proteins. These models are built through post-training, yet how each stage shapes reasoning and generalization remains poorly understood. We study when post-training improves performance and when it induces over-specialization. Across genomics, transcriptomics, and proteins, we train and evaluate more than 100 biological reasoning models under controlled variation in backbone, continued pre-training (CPT), supervised fine-tuning (SFT), and reinforcement learning (RL), measuring both in-domain (ID) and out-of-domain (OOD) performance. We find that each post-training stage reshapes generalization in a distinct way rather than contributing uniform gains. CPT improves downstream performance by aligning models with biological language. SFT consistently increases ID performance but causes OOD performance to peak early and decline as models fit the training distribution. RL, when applied to strong SFT checkpoints with aligned rewards, improves OOD performance and partially recovers generalization. These results show that biological reasoning does not improve monotonically with additional supervision or compute. Instead, performance depends on how training stages are composed. Under fixed post-training budgets, the strongest ID-OOD trade-off comes from brief SFT, larger RL allocations, and asymmetric adaptation capacity across stages.

---


### 208. [BadWorld: Adversarial Attacks on World Models](https://arxiv.org/abs/2606.16519)

**<font color=#1a73e8>作者：</font>** Linghui Shen, Mingyue Cui, Xingyi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual world models (VWMs) synthesize interactive, action-conditioned rollouts from a single context image. However, it remains an open question how robust these models are to adversarial perturbations. Standard adversarial attacks fail to assess this vulnerability because attackers lack ground-truth future videos and cannot predict subsequent user controls. We introduce BadWorld, a label-free adversarial framework tailored for autoregressive VWMs that systematically overcomes both constraints. First, to bypass the need for future supervision, we propose a self-supervised velocity attack that directly disrupts the early denoising dynamics of the model. Second, to ensure the attack generalizes across unpredictable user actions, we formulate a trajectory-adaptive bi-level optimization that actively mines hard control sequences to forge control-agnostic perturbations. Evaluated on representative VWMs with continuous and discrete controls, BadWorld exposes severe structural fragility. Visually indistinguishable adversarial images reliably trigger catastrophic degradation in future rollouts, leading to incomplete denoising, structural collapse, and control inconsistency. These findings reveal critical risks for deploying VWMs in safety-critical systems while highlighting a practical mechanism for privacy protection.

---


### 209. [Kairos: A Native World Model Stack for Physical AI](https://arxiv.org/abs/2606.16533)

**<font color=#1a73e8>作者：</font>** Kairos Team, Fei Wang, Shan You 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models are transitioning from passive visual generators to foundational, operational infrastructure for Physical AI: they must natively acquire world knowledge from heterogeneous experience, maintain persistent states over long horizons, and execute efficiently within real deployment constraints. We introduce Kairos, a native world model stack designed around these requirements. (1) Kairos learns the world by pioneering a Native Pre-training Paradigm governed by a Cross-Embodiment Data Curriculum, which organizes open-world videos, human behavioral data, and robot interactions into a progressive developmental pathway. (2) Kairos maintains the world by unified world understanding, generation, and prediction within a Native Unified Architecture equipped with Hybrid Linear Temporal Attention, where sliding-window attention captures local dynamics, dilated sliding windows capture mid-range dependencies, and gated linear attention maintains persistent global memory. We establish formal theoretical bounds demonstrating that this temporal factorization strictly limits error accumulation, mathematically guaranteeing state propagation across extended horizons. (3) Kairos runs the world by incorporating a Deployment-Aware System Co-Design to support low-latency rollout generation on server and consumer-grade hardware for real-world observation-action-feedback loops. Experiments on embodied world-model, long-horizon, and action-policy benchmarks show that Kairos achieves top level performance while offering a strong efficiency-capability trade-off. Together, these results position Kairos as a cohesive operational foundation for future self-evolving physical intelligence.

---


### 210. [Can LLM Coding Agents Reason About Time Series?](https://arxiv.org/abs/2606.16545)

**<font color=#1a73e8>作者：</font>** Filip Rechtorík, Ondřej Dušek, Zdeněk Kasner  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly being used for automated decision-making systems in finance, healthcare, or environmental monitoring. Time series data are ubiquitous in these fields, yet hard to process automatically. Can time series be analyzed by LLM agents? We examine three approaches: providing the agent with raw numerical data, using the LLM as a coding agent, or a combination of both. In the coding agent setup, the model iteratively queries the data using Python code. Using two time series understanding benchmarks, we show that agents with code access can outperform models processing raw data by up to 10%. However, even the best performing agent still answers about 22-34% of the questions incorrectly. To get insights into models' strategies and reasoning gaps, we analyze the model outputs with a strong LLM judge. Our analysis reveals that coding agents can select appropriate statistical tests, but often miss important nuances. Meanwhile, models with access to raw data can reach the right conclusions using back-of-the-envelope calculations.

---


### 211. [MIRAGE: Auditing Anti-Muslim Bias in Frontier LLMs Across Reasoning, Agentic, and Time-Coupled Conditions](https://arxiv.org/abs/2606.16562)

**<font color=#1a73e8>作者：</font>** Noor Islam S. Mohammad, Tamim Sheikh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Five years after the discovery of persistent anti-Muslim bias in large language models, most evaluations remain confined to single-turn prompt completion, a setting that no longer reflects how frontier LLMs are deployed. We introduce \textbf{MIRAGE} (Muslim-Identity Reasoning and Agentic Generation Evaluation), a benchmark of 1{,}200 prompts spanning three deployment-realistic conditions: direct completion, chain-of-thought reasoning, and simulated agentic decision-making across content moderation, lending triage, refugee claim summarization, and hiring screens. Across six frontier models, we find that (i) chain-of-thought reasoning \emph{amplifies} rather than suppresses Muslim-violence associations by 12--34\% relative to direct completion, (ii) agentic decisions exhibit a 9--22 percentage-point asymmetry between Muslim and matched non-Muslim cases on identical evidence, and (iii) bias is sharply time-coupled to retrieved news context, increasing 18--27\% under recent-conflict retrieval. Existing prompt-based mitigations transfer poorly across our three conditions, suppressing direct-completion bias while leaving agentic asymmetry largely intact. We release MIRAGE and an open evaluation harness to support targeted mitigation research.

---


### 212. [PROSE: Training-Free Egocentric Scene Registration with Vision-Language Models](https://arxiv.org/abs/2606.16569)

**<font color=#1a73e8>作者：</font>** Zhiang Chen, Nahyuk Lee, Boyang Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Registering two captures of the same indoor space taken at different times underpins persistent spatial memory for robots and AR systems, yet the realistic version of this task is egocentric and its most scalable form is RGB-only. Head-mounted cameras yield blurry, fast-moving, partially overlapping views from which dense geometry is hard to recover. Classical registration leans on exactly the clean point clouds this setting lacks, while learned scene-graph methods require a pre-built or annotated graph and a trained matcher that we find brittle under egocentric data. We take a different route, using a pretrained vision-language model as the source of both scene understanding and cross-scan matching. Our method, PROSE (Prompted Scene rEgistration), lifts each RGB sequence into an object-level 3D scene graph using off-the-shelf foundation models for geometry, segmentation, and language, then prompts the same VLM to match object instances across the two RGB sequences. To make this matching tractable and reliable, we leverage object heights as a prior and verify each proposed match with a paired same/different query, then solve for the rigid transform by hypothesizing a candidate per matched object and selecting the one with the strongest geometric consensus. PROSE adds no learned parameters and requires no depth sensor, training, or annotated graph. On the egocentric Aria Digital Twin and Aria Everyday Activities benchmarks, it outperforms both geometric and learned scene-graph baselines in registration accuracy, on ground-truth and RGB-reconstructed point clouds alike, and the scene graph it produces transfers directly to downstream tasks.

---


### 213. [Transformation-driven generation of comparable projection images from multimodal anatomical scenes](https://arxiv.org/abs/2606.16573)

**<font color=#1a73e8>作者：</font>** Dariusz Pojda, Krzysztof Domino, Michał Tarnawski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work addresses the computational problem of generating reproducible projection-space observations from heterogeneous anatomical scenes whose components may undergo independent spatial transformations. We propose a transformation-driven framework for synthetic projection imaging from multimodal anatomical data and demonstrate it on mandibular-motion scenarios. In contrast to conventional Digitally Reconstructed Radiograph (DRR) approaches primarily designed for registration, projection realism, or rendering efficiency, the proposed formulation treats projection imaging as an observation process operating on an explicitly represented anatomical scene. Independently transformable volumetric and surface-based anatomical objects are embedded within a shared scene representation and propagated directly into projection space through explicit transformations. Projection geometry, acquisition modelling, material interpretation, and image presentation remain explicitly separated, enabling controlled exploration of methodological assumptions while preserving reproducibility and direct comparability between generated projections. Particular emphasis is placed on transformation-driven anatomical scenarios relevant to craniofacial analysis, including mandibular motion and therapeutic repositioning. Using a shared anatomical reference scene composed of CT/CBCT volumes, segmented structures, surface models, and auxiliary anatomical or therapeutic objects, the framework enables generation of directly comparable VirtualRTG projections from multiple anatomical configurations while preserving identical imaging assumptions. Rather than aiming at fully physically faithful radiographic simulation, the proposed approach provides a controllable and reproducible methodological environment for studying anatomy--projection relationships, motion observability, and transformation-aware imaging workflows.

---


### 214. [Can LLM Agents Infer World Models? Evidence from Agentic Automata Learning](https://arxiv.org/abs/2606.16576)

**<font color=#1a73e8>作者：</font>** Reef Menaged, Gili Lior, Shauli Ravfogel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose agentic automata learning to evaluate the extent to which tool-calling LLM agents can uncover hidden environments through interaction. In our setup, an agent should uncover a hidden deterministic finite automaton (DFA) by interacting with an oracle through (1) membership queries ("Does this string belong to the target language?") and (2) equivalence queries ("Is this the target DFA?"). This yields a scalable testbed with controlled task complexity, measurable interaction efficiency, and strong baselines (classic automata-learning algorithms). Evaluating state-of-the-art LLMs, we find that performance drops sharply as DFA size increases. Reasoning models are markedly stronger than non-reasoning models, yet trajectory analyses reveal recurring failures in query planning, evidence integration, and hypothesis construction. Overall, our results show that current LLM agents can sometimes perform non-trivial interactive discovery, but remain far less robust and efficient than classic algorithms for the task.

---


### 215. [Multi-Modal Spatio-Temporal Graph Neural Network with Mixture of Experts for Soil Organic Carbon Prediction](https://arxiv.org/abs/2606.16580)

**<font color=#1a73e8>作者：</font>** Daniele Mos, Felipe Drummond, Anton Bossenbroek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Top-soil organic carbon (SOC) prediction is fundamental to agricultural sustainability, land use policy and fertilization planning. Existing approaches face two limitations: they pair hand-crafted covariates with classical ML or single-modal deep models that miss rich spectral and temporal information, and grid-based architectures ignore the irregular spatial structure of field measurements. We introduce SpTGNN, a multi-modal spatio-temporal graph neural network addressing both. SpTGNN represents soil measurements as nodes in a heterogeneous graph with three edge types (spatial proximity, spectral similarity, elevation), and applies relational graph attention to learn separate patterns per relation. A fine-tuned TerraMind encoder extracts node features from Sentinel-2, Sentinel-1 and DEM signals, combined with per-sample environmental covariates and learned positional and temporal embeddings. A sparse Mixture-of-Experts module fuses the four streams via top-$k$ routing. Uncertainty is captured by pairing heteroscedastic regression (aleatoric) with deep ensembles (epistemic), and a Moran's $I$ penalty regularizes spatial autocorrelation. We evaluate on a global SOC corpus split into three regional instances ($\sim$49k samples globally, Africa $\sim$26k, Europe $\sim$14k). Our 5-member deep ensemble reports $R^2=0.762$, RMSE $=3.51\pm0.48$ g/kg and MAPE $=22.9\%$ on the Africa test split, improving over a tabular XGBoost baseline; the best single checkpoint reaches validation $R^2=0.864$. Ablations confirm the heterogeneous graph, MoE fusion and fine-tuned backbone each contribute substantively, and the ensemble UQ stack achieves post-calibration ECE of $0.031$ (hybrid) and $0.026$ ($\beta$-NLL). To our knowledge, this is the first framework to unify foundation-model feature extraction, heterogeneous graph attention and decomposed uncertainty quantification for SOC estimation.

---


### 216. [LOCUS: Local Visual Cue Search for Enhancing Fine-Grained Perception in Multimodal Large Language Models](https://arxiv.org/abs/2606.16586)

**<font color=#1a73e8>作者：</font>** Zhou Tao, Fang Zhang, Zewen Ding 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) remain unreliable on fine-grained visual perception, even when high-resolution inputs preserve the necessary local details. We identify this limitation as visual context rot: decisive evidence may exist in the full image, yet fail to be reliably selected and used amid redundant visual context. We propose LOCUS (LOcal visual CUe Search), a training framework that teaches MLLMs to internalize local evidence search through a verifiable proxy task. During training, LOCUS provides a local crop as a visual cue and optimizes the model to recover its spatial support in the full image using an IoU-based reward. The visual cue is used only during training, leaving the standard image-question inference interface unchanged. Experiments across fine-grained perception, hallucination, general understanding, and reasoning benchmarks show that LOCUS improves localization-sensitive visual understanding while preserving broad capabilities. Attention analyses further indicate stronger focus on task-relevant evidence regions, suggesting that training-time visual cue search provides an effective route to internalized fine-grained evidence selection.

---


### 217. [SING: Synthetic Intention Graph for Scalable Active Tool Discovery in LLM Agents](https://arxiv.org/abs/2606.16591)

**<font color=#1a73e8>作者：</font>** Qiao Xiao, Haochen Shi, Yisen Gao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly rely on agent harnesses that manage context, tools, and multi-turn execution, making tools a central interface for acting in realistic digital environments. As harness-connected tool ecosystems expand to hundreds or thousands of APIs, services, and task-specific skills, exhaustive tool schema injection becomes costly and imposes a closed-world assumption that limits agents to a predefined static inventory. Retrieval-augmented tool selection offers a natural alternative, but existing one-shot retrieval methods often fail to align isolated tool descriptions with the agent's true task intention, especially in long-horizon tasks where required capabilities emerge through decomposition, observations, and newly induced subgoals. We propose SING, an intention-aware active tool discovery framework that builds an intention-tool graph linking user intentions, tool capabilities, and tool collaboration patterns, and dynamically retrieves tools according to evolving task states. Using a unified corpus of 7,471 tools, we evaluate SING on three real-world tool-use benchmarks. SING improves Global Recall@5 by up to 59.8% and downstream success rate by up to 28.9% over baselines, while reducing full-corpus tool-schema exposure by 99.8%, demonstrating that intention-aware graph structure enables more accurate and context-efficient tool discovery in large-scale agentic ecosystems.

---


### 218. [DifferAD-R1: A Difference-Guided IndustrialAnomaly Localization with Multimodal LargeLanguage Models](https://arxiv.org/abs/2606.16601)

**<font color=#1a73e8>作者：</font>** Dingrong Wang, Xian Tao, Zhen Qu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly localization aims to accurately identify and localize abnormal regions in industrial products, addressing the critical challenge of detecting unseen defect categories in real-world scenarios. Traditional closed-set methods often suffer from poor cross-scenario generalization, while existingMultimodal Large Language Model (MLLM)-based approachesface two core limitations: they either adopt QA-style paradigmsmisaligned with the practical demands of localization, or relyon standard optimization techniques such as Group RelativePolicy Optimization (GRPO), which fails to deliver effectivelearning signals for subtle defects. To tackle these issues, thispaper proposes DifferAD-R1, an MLLM-augmented reinforcement learning framework tailored for industrial anomaly localization. We design a Difference-Guided dual-image paradigm,which reformulates the localization task as a one-shot difference grounding problem to effectively explore cross-scenarioanomalies. A Dual-Consistency Localization Reward is developedfor hard-to-detect anomalies, enhancing optimization stabilityand robustness. Additionally, we integrate a difficulty-awarestrategy with adaptive reweighting and group-wise resamplingto prioritize learning on challenging instances. To facilitateevaluations in real-world industrial settings, we construct theAD-DualDiff dataset, comprising 13K paired images across 20categories. Experimental results demonstrate that DifferADR1 significantly outperforms existing baselines and achievescompetitive performance compared to large-scale models likeQwen3-VL (235B parameters). Our code is publicly availableat: this https URL.

---


### 219. [ARB4WM: An Adversarial Robustness Benchmark for World Models in Continuous Control](https://arxiv.org/abs/2606.16605)

**<font color=#1a73e8>作者：</font>** Junjian Zhang, Hao Tan, Ruonan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models are widely used in robotic and agentic engineering control systems due to their ability to learn latent dynamics for planning and decision-making. As these systems are increasingly deployed in safety-critical settings, understanding their robustness under adversarial conditions has become essential. However, existing evaluations lack a unified benchmark for testing adversarial threats across the policy, value, and latent-dynamics levels of world-model agents. To fill this gap, we present ARB4WM, a unified evaluation framework for pre-deployment robustness and risk assessment of world-model agents under visual perturbations. ARB4WM defines five white-box loss objectives across these three levels and studies their effects when combined with single-step or multi-step perturbation strategies and temporal attack modes, including full-frame, half-sequence, and sparse-frame exposure. Specifically, we evaluate four Dreamer-style agents across 20 tasks from MetaWorld and the DeepMind Control Suite under different loss objectives, perturbation strategies, and temporal attack modes. Results show that attacks targeting value estimation, latent representations, and RSSM dynamics can be as damaging as direct policy disruption, and that early or frequent perturbations are especially harmful, while input-level defenses provide limited recovery under adaptive attacks. These findings suggest that safety, risk, and reliability assessment for world models should cover multiple component-oriented attack objectives and temporal exposure protocols rather than relying solely on action-space robustness. Source code is available at this https URL.

---


### 220. [CoffeeBench: Benchmarking Long-Horizon LLM Agents in Heterogeneous Multi-Agent Economies](https://arxiv.org/abs/2606.16613)

**<font color=#1a73e8>作者：</font>** Issa Sugiura, Daichi Hattori, Kazuo Araragi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM agents become capable of increasingly long-horizon tasks, evaluating their performance in economic systems is becoming increasingly important. Unlike existing benchmarks that primarily evaluate a single agent interacting with a passive environment, economic systems are inherently multi-agent, requiring autonomous agents to communicate, negotiate, and transact while pursuing their own objectives over extended periods. We introduce CoffeeBench, a benchmark for evaluating LLM agents in a long-horizon multi-agent economy composed of heterogeneous firms. In CoffeeBench, two farmers, two roasters, and two retailers autonomously operate their businesses over a 90-day simulation, each seeking to maximize cumulative net income through communication and transactions while managing cash, inventory, and pricing. The evaluated model controls one coffee roaster, while the remaining firms are controlled by fixed reference agents. Across several recent open-weight and proprietary LLMs, all models outperform a passive baseline that takes no actions, with most achieving positive net income. Analysis of agent behavior reveals substantial differences in long-horizon economic interaction: higher-performing models communicate more actively with other firms, whereas Claude~Haiku~4.5 exhibits an idle-drift failure mode, repeatedly choosing inaction despite producing coherent assessments and plans. We release our code and agent trajectories to support future research.

---


### 221. [SUP-MCRL: Subject-aware Unified Pseudo-feature Coded Multimodal Contrastive Representation Learning for EEG Visual Decoding](https://arxiv.org/abs/2606.16615)

**<font color=#1a73e8>作者：</font>** Shengyu Gong, Weiming Zeng, Yueyang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-invasive brain-computer interfaces suffer severe fidelity degradation in neural visual decoding when generalizing to natural visual experiences. Conventional multimodal contrastive representation learning solely optimizes geometric distance alignment, neglecting semantic consistency and subject selectivity, causing spurious zero-shot alignment. We propose SUP-MCRL, a unified framework integrating three collaborative mechanisms: (1) Semantic-entity Aware Visual Encoder (SAVE), learning spatial attention to extract semantic content without pre-trained saliency models; (2 Unified EEG Enhancer (UEE), employing multi-scale atrous convolutions and inter-band attention for adaptive cross-subject robustness; and (3) Prototype-based Progressive Augmenter (PPA), maintaining an EMA-updated pseudo-feature pool to prevent representation collapse. Zero-shot experiments on THINGS-EEG achieve 66.0%/91.9% (Top-1/Top-5) intra-subject and 24.0%/52.9% LOSO accuracy, surpassing state-of-the-art methods. Code is available at this https URL.

---


### 222. [Islamic Large Language Models: From Knowledge Acquisition to Trustworthy and Hallucination-Resistant AI](https://arxiv.org/abs/2606.16629)

**<font color=#1a73e8>作者：</font>** Mohammed Amine Mouhoub  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for knowledge-intensive question answering, including religious and legal questions. Islamic knowledge is a particularly demanding setting: answers are expected to be grounded in authoritative sources, citations must be exact, Arabic varieties differ substantially from the language of classical sources, and legitimate jurisprudential disagreement must be represented rather than collapsed into a single answer. This survey reviews the emerging field of Islamic LLMs and trustworthy Islamic AI. We organize the literature around Arabic NLP and Arabic-centric LLMs, Islamic NLP resources, Qur'anic question answering, Islamic knowledge benchmarks, retrieval-augmented generation, Islamic legal reasoning, inheritance reasoning, hallucination evaluation, and trustworthiness. We argue that fluency in Arabic is not sufficient for Islamic AI. Reliable systems require curated sources, retrieval and verification modules, citation-aware generation, madhhab-aware reasoning, human expert evaluation, and benchmarks that measure not only answer accuracy but also faithfulness, source validity, and reasoning quality. The survey concludes with a research agenda for hallucination-resistant Islamic AI systems.

---


### 223. [The Integrator Advantage: Controlled Agentic AI for Small and Medium-Sized Companies](https://arxiv.org/abs/2606.16649)

**<font color=#1a73e8>作者：</font>** Christopner Koch, Joshua A. Wellbrock  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI marks a new phase of enterprise automation. Unlike traditional automation or conversational AI, agentic systems can interpret goals, plan multi step tasks, access tools, interact with enterprise systems, and execute workflows with varying degrees of autonomy. For small and medium sized companies, this creates potential to reduce administrative burden, accelerate routine processes, and improve the use of organizational knowledge. This paper argues that the near term value of Agentic AI does not lie in full autonomy or workforce reduction, but in controlled partial autonomy for simple and medium complexity business processes. It proposes an integration framework covering use case suitability, autonomy levels, technical integration, governance, security, employee enablement, and measurable impact. The paper concludes that Agentic AI can become a productivity lever when implemented as a human centered capability with responsibility and accountability retained by people.

---


### 224. [Vision-Language Models as Zero-Annotation Oracles in Histopathology](https://arxiv.org/abs/2606.16658)

**<font color=#1a73e8>作者：</font>** Vishal Jain, Giorgio Buzzanca, Sarah Cechnicka 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foreground segmentation is the critical first step of every computational pathology pipeline, yet existing methods rely on hand-tuned heuristics or supervised models that overfit to narrow stain and scanner distributions, failing silently on specialised stains such as Jones silver or Elastica van Gieson. We propose a coarse-to-fine approach that recasts foreground segmentation as a visual perception task and leverages general-purpose vision-language models (VLMs) as zero-annotation oracles. Our key insight is that tissue-versus-background discrimination is a natural-image recognition problem, not a histopathological one, so VLMs trained on internet-scale corpora generalise where domain-specific models cannot. We introduce Leica-75, a benchmark of 75 renal transplant whole-slide images spanning three stain families. On Leica-75, our method achieves the highest segmentation quality on out-of-distribution stains (Dice 0.858 +/- 0.027 on Jones, 0.853 +/- 0.041 on EVG) with 7x lower cross-stain variance than the best supervised baseline, while remaining competitive on in-distribution H&E. Few-shot prompting with automatically curated exemplars (Auto-context) rescues hard cases on Stress-32 (n=32), a curated stress-test subset (Dice 0.470 to 0.819 for the 2B model). VLM-based annotation review matches human expert consensus (kappa=0.989 for blur detection; mean precision/recall grading accuracy 0.708 vs. human 0.646 for segmentation mask review). The resulting pseudo-labels are used to distil lightweight student models that are as performant as the teacher model while running for a fraction of the cost. Our framework provides a principled, scalable solution to a persistent infrastructure bottleneck in digital pathology.

---


### 225. [FraudSMSWalker: Benchmarking Agentic Large Language Models for SMS-to-Webpage Fraud Detection](https://arxiv.org/abs/2606.16659)

**<font color=#1a73e8>作者：</font>** Y. H. Zhou, Z. M. Ma, Y. J. Zhou 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> SMS fraud is increasingly cross-channel: a message directs the user to a webpage, and the final risk depends on how the SMS claim aligns with the page content and requested user action. However, existing evaluations either focus on message-only smishing classification or expose URL and domain cues that allow models to rely on reputation shortcuts. To address this gap, we introduce \textbf{FraudSMSWalker}, a controlled benchmark for URL-masked SMS-to-webpage fraud judgment. FraudSMSWalker contains 699 bilingual chains, including 332 fraudulent and 367 benign cases, across ten service scenarios. The model-visible input consists of the SMS context and sanitized webpage evidence, while raw URLs, hosts, domains, IPs, redirects, and reputation metadata are withheld. The benchmark further includes hard benign cases whose pages contain login, payment, verification, or account-management elements that are plausible under the service context but also appear in scam flows. We evaluate nine web agents under masked browser-agent protocols and conduct URL-visibility ablations. The results show that current agents can detect suspicious cues, but struggle to preserve benign recall and often produce positive predictions that are weakly supported by the observed evidence. These findings position FraudSMSWalker as a benchmark for measuring whether web agents can make fraud judgments that remain both accurate and evidence-grounded when direct reputation shortcuts are suppressed. The associated code and dataset are accessible at the \href{this https URL}{anonymous link}.

---


### 226. [Look Again Before You Abstain:Budgeted Conformal Evidence Acquisition for Reliable Vision-Language Model](https://arxiv.org/abs/2606.16667)

**<font color=#1a73e8>作者：</font>** Jian Xu, Delu Zeng, John Paisley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) hallucinate: they assert visual details that the image does not support. A principled remedy is selective prediction with a distribution-free guarantee-verify each claim and abstain when the claim is not grounded, so that the hallucination rate among asserted claims is provably bounded. We show, however, that this guarantee is bought at a brutal price: to keep the hallucination rate below $5\%$ on a balanced object-existence benchmark, a state-of-the-art conformal filter must abstain on more than $80\%$ of claims. We argue that abstention is wasteful when more visual evidence is cheaply available, and introduce Budgeted Conformal Evidence Acquisition (BCEA), which replaces the binary answer/abstain decision with a three-way choice: answer, abstain, or acquire additional visual evidence by re-examining the image (zooming, cropping, or applying a claim-specific intervention) under a bounded compute budget. We make two observations. First, acquisition that is plugged naively into a calibrated filter breaks the statistical guarantee -- realized risk overshoots the target by up to $17$ points -- because the acquisition step destroys the exchangeability that conformal calibration relies on. Second, folding the entire acquisition policy into the score function and re-calibrating on post-acquisition scores \emph{restores} the finite-sample guarantee while still recovering coverage. BCEA further uses structured, claim-type-specific interventions. Across the POPE benchmark and COCO-constructed existence and spatial-relation claims, on four open VLMs, BCEA controls the hallucination rate at the target level and consistently improves coverage over a guaranteed-abstention baseline.

---


### 227. [Multimodal Evaluator Preference Collapse: Cross-Modal Contagion in Self-Evolving Agents](https://arxiv.org/abs/2606.16682)

**<font color=#1a73e8>作者：</font>** Zewen Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When AI agents use language models to evaluate their own outputs in a feedback loop, systematic biases emerge. We show that Evaluator Preference Collapse (EPC) is dramatically amplified in multimodal settings. Using GPT-4o to evaluate DeepSeek-chat across text and visual tasks, we find that a single strategy (step_by_step) absorbs 48.4% of all weight -- 3.2x the collapse observed in text-only self-evaluation -- while three visual-domain strategies receive only 9.1% combined weight. We then demonstrate a novel phenomenon we term cross-modal contagion: evaluator preferences acquired on one modality transfer to and corrupt strategy selection on another. Through a four-phase isolation training paradigm, we measure contagion coefficients and document strategy inversion -- the optimal strategy for a modality reverses after cross-modal exposure. A Phase 3 statistical validation across four evaluator configurations (N=53 total independent repetitions, 15,592 API calls) reveals a clear hierarchy: cross-model evaluation (GPT-4o, N=8) produces strong but symmetric bidirectional contagion (mean gamma_{T->V}=1.176, gamma_{V->T}=1.089, Delta=-0.088, p=0.575, Cohen's d=0.29); high round counts (DashScope, 50 rounds) cause collapse to single-strategy dominance (70% zero contagion); and self-evaluation provides near-complete immunity -- 97% of runs (N=30, DeepSeek-chat) yield exactly zero contagion (mean gamma=0.033, 95% CI [-0.031, 0.010], p=0.642, d=0.07). No evaluator condition shows statistically significant directional asymmetry. We introduce the contagion matrix indexed by evaluator identity, release the MM-EPC experimental framework, and identify cross-model evaluator architecture as the primary risk factor for preference contagion.

---


### 228. [Progressive Knowledge-Guided Large Language Model Framework for Bearing Fault Diagnosis](https://arxiv.org/abs/2606.16684)

**<font color=#1a73e8>作者：</font>** Jinghan Wang, Gaoliang Peng, Yanjun Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vibration-based bearing fault diagnosis requires resolving three interrelated measurement challenges, including the trade-off between global statistical feature efficiency and local transient signal fidelity, insufficient traceability of measurement features to underlying fault physics, and ineffective multi-source measurement information fusion across diagnostic scales. This paper presents a progressive physics-guided multi-scale vibration signal processing framework that addresses all three challenges within a unified diagnostic pipeline. An 81-dimensional measurement descriptor, derived from bearing kinematic theory and characteristic defect frequencies, establishes a physically traceable feature space enabling real-time fault screening at approximately 20 ms per sample. A fault-adaptive signal segmentation mechanism then directs analytical attention toward fault-relevant waveform regions guided by physics-based priors, without manual feature engineering. Structured fault mechanism knowledge is further encoded implicitly in model parameters during training, enabling autonomous multi-scale measurement fusion without external knowledge dependencies at inference. Validated on four public benchmark datasets under diverse operating conditions, the framework achieves 98.49% diagnostic accuracy with a 12.6-fold reduction in computational cost relative to signal-level baselines. Interpretability analysis confirms that diagnostic feature activations align with established bearing fault mechanics, supporting measurement traceability in safety-critical industrial systems.

---


### 229. [Medical world models: representing medical states, modelling clinical dynamics and guiding intervention policies](https://arxiv.org/abs/2606.16721)

**<font color=#1a73e8>作者：</font>** Ke Liu, Mengxuan Li, Yanyi Bao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical diagnosis and treatment are dynamic processes in which patient states evolve over time and clinical interventions alter future outcomes. Although current medical AI can detect disease, estimate risk and generate reports, many systems still return static labels or scores, offering limited insight into how illness may progress or how alternative interventions may reshape its trajectory. Medical world models adapt the world-model idea from artificial intelligence to healthcare by learning internal simulators of patient-state dynamics. Their long-term goal is to help clinicians anticipate deterioration, compare treatment-conditioned futures and tailor care to individual patients. Yet relevant work remains scattered across foundation models, longitudinal modelling, disease simulation, treatment-effect estimation, reinforcement learning and digital twins. To bridge this gap, this review outlines a roadmap for advancing medical AI from isolated diagnosis and prediction toward medical world models that simulate disease evolution and support intervention decisions. This roadmap is organized around three coupled capabilities: patient-state construction, clinical dynamics modelling and intervention decision support. Across representative systems, the comparison highlights what each capability contributes and how partial components can be integrated into more mature perception--dynamics--planning systems. Finally, we identify the challenges involved in turning plausible rollouts into clinically useful simulators. Related literature is available at this https URL.

---


### 230. [AgentFairBench: Do LLM Agents Discriminate When They Act?](https://arxiv.org/abs/2606.16723)

**<font color=#1a73e8>作者：</font>** Triveni Morla, Rohith Reddy Bellibaltu, Manpreet Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly take actions (screening applicants, recommending credit, triaging patients), yet fairness for LLMs is still measured by grading answers. We introduce AgentFairBench, a cheap, reproducible, multi-domain benchmark for demographic disparity in the actions of LLM agents. Grounded in a companion framework, the Bias Conduction Framework (BCF, restated here), it spans three regulator-anchored domains: hiring, lending, and medical triage. Synthetic, demographic-neutral profiles are evaluated in counterfactual matched sets that vary only a name-coded race x gender signal (in the Bertrand Mullainathan tradition), under four agent scaffolds of increasing agency (direct, chain-of-thought, multi-agent deliberation, tool-augmented). A NumPy-only harness computes counterfactual flip rate, mean absolute score difference (MASD), action-rate disparity, and tool-invocation disparity, with bootstrap confidence intervals, paired tests, and false-discovery-rate control, for single-digit dollars per model. A live leaderboard with a held-out private split and a contamination canary admits external models by submission. Our pilot (864 decisions plus a test-retest replication) carries a methodological lesson: comparing a six-group score spread against a two-run noise difference overstates disparity by ~ 2.4X through statistic arity alone. Against an arity matched noise floor and an omnibus group test, claude haiku 4 5 shows no demographic effect above sampling noise (0 of 120 pairwise and 0 of 9 omnibus contrasts survive correction); a planted-bias test confirms the instrument detects disparity when present. The contribution is a sound, sensitive, adoption-ready instrument, the arity matched null methodology, and open artifacts to scale it. Code, data, and harness are released under open licenses, with an anonymized review artifact.

---


### 231. [Learning Policy from a Single Trajectory in Average-Reward Markov Decision Process](https://arxiv.org/abs/2606.16729)

**<font color=#1a73e8>作者：</font>** Jongmin Lee, Ernest K. Ryu, Vaneet Aggarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While there is an extensive body of work characterizing the sample complexity of discounted cumulative-reward MDPs, finite sample analyses for average-reward MDPs have been limited, and most existing works rely on restrictive assumptions such as ergodicity or access to a generative model. In this work, we establish the first finite sample complexity guarantees from a single trajectory for weakly communicating average-reward MDPs. To this end, we study the dynamics of a single trajectory in weakly communicating MDPs and based on this analysis, we develop novel model-free methods. Notably, our value-based and policy-based methods provide finite sample complexity guarantees of $\widetilde{O}(1/\varepsilon^2)$ and $\widetilde{O}(1/\varepsilon^4)$ from a single trajectory in weakly communicating MDPs, respectively. Furthermore, we introduce the first model-free method that requires no prior knowledge of problem-dependent quantities for communicating MDPs.

---


### 232. [A First-Principles Derivation of LLM Policy Optimization: From Expected Reward to GRPO and Its Structural Extensions](https://arxiv.org/abs/2606.16733)

**<font color=#1a73e8>作者：</font>** Jianghan Shen, Siqi Luo, Yue Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Policy gradient algorithms for language models optimize the same objective $J(\theta) = \mathbb{E}*{\tau \sim p*\theta(\tau)}[R(\tau)]$, which has exactly two factors: the trajectory probability $p_\theta(\tau)$ and the reward $R(\tau)$. Every method from REINFORCE to PPO to GRPO and their descendants modifies one or both factors to address a specific failure in the preceding formulation. Existing surveys organize these methods by domain or chronology, which obscures the rationale behind each design choice and the precise location of its intervention within the gradient estimator. This survey revisits the landscape of LLM policy optimization from $J(\theta)$ on first principles and uses the trajectory side, induced by $p_\theta(\tau)$, and the reward side, induced by $R(\tau)$, as the two axes along which methods are located. It covers the path from REINFORCE and PPO to GRPO, as well as post-GRPO variants, Agentic RL, and GRPO-OPD. The resulting framework is unified, diagnostic, and extensible: it analyzes methods from a shared objective, identifies which side each method modifies and why, and applies the same trajectory and reward axes across these settings. Across these settings, the framework also exposes compound failures that no single-side fix resolves and that therefore require joint design of the trajectory side and the reward side. The boundary cases and coupled failures identified by this map mark where existing solutions run out and provide a principled starting point for designing the next generation of LLM policy optimization algorithms.

---


### 233. [Structure-aware Knowledge-guided Heterogeneous Mamba for Zygomaticomaxillary Suture Assessment](https://arxiv.org/abs/2606.16749)

**<font color=#1a73e8>作者：</font>** Xiaoqi Guo, Birui Chen, Xinquan Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Zygomaticomaxillary Suture is a key circummaxillary structure that connects the zygomatic bone and the maxilla, which serves as a primary site of resistance during maxillary advancement, and its maturation status directly influences the timing and efficacy of orthopedic interventions. However, accurate staging of ZMS maturation remains challenging due to subtle high-frequency transitions in suture lines and the global semantic ambiguity between adjacent stages. To address this, we present the first public ZMS dataset, comprising 3,790 ZMS images covering the entire age range from 4 to 24 years. Based on this dataset, we propose SKMamba, a Structure-aware and Knowledge-guided Mamba-based multi-modal framework for automated ZMS maturation assessment. SKMamba adopts a decoupled dual-path architecture that mimics the hierarchical diagnostic process used by experienced orthodontists. We first introduce an Implicit Edge Extractor (IEE), which leverages structural pre-training to reduce trabecular noise and accentuate sutural boundaries. Complementarily, a Cross-Modal Semantic Alignment (CSA) module is designed to incorporate anatomical descriptions from a large language model (LLM). This module helps align local morphological cues with global semantic descriptions while ensuring that objective morphological evidence remains the primary basis for decisions. Extensive experiments on our ZMS dataset demonstrate that SKMamba achieves state-of-the-art performance compared to existing methods. Code is available at this https URL.

---


### 234. [P3B3: A Multi-Turn Conversational Benchmark for Measuring European and Brazilian Portuguese Variety Bias in LLMs](https://arxiv.org/abs/2606.16753)

**<font color=#1a73e8>作者：</font>** Rafael Ferreira, Inês Vieira, Inês Calvo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) become embedded in everyday communication, capturing regional linguistic variation is essential for reliable and equitable language use. In Portuguese, European (pt-PT) and Brazilian (pt-BR) varieties remain unevenly represented, with pt-BR dominating in data quantity, while LLM preference for Portuguese variants remains underexplored. To address this gap, we introduce P3B3, an expert-curated language variety agnostic benchmark of conversational prompts, along with an evaluation framework for measuring variety bias and controllability. Experiments on several models show that most LLMs exhibit a strong bias toward pt-BR, with variation in controllability across models. These results highlight the need for more balanced multilingual representation across language varieties.

---


### 235. [Maximum Entropy Inverse Reinforcement Learning for Mean-Field Games with Average Reward](https://arxiv.org/abs/2606.16759)

**<font color=#1a73e8>作者：</font>** Şevket Kaan Alkır, Naci Saldı, Berkay Anahtarcı 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study inverse reinforcement learning for discrete-time, infinite-horizon mean-field games (MFGs) under an average-reward criterion. Expert demonstrations are assumed to arise from a stationary mean-field equilibrium under an unknown reward, and the goal is to recover a policy explaining the observed behaviour via the maximum causal entropy principle. We formulate the inverse problem by enforcing consistency with the expert mean-field term and long-run feature expectations, treating two reward classes within a unified occupation-measure framework. For finite-dimensional linear rewards, we give a convex dual reformulation with an explicit log-partition objective, and prove smoothness and curvature properties justifying constant-step-size gradient descent. For infinite-dimensional RKHS rewards, we develop a Lagrangian relaxation whose inner-maximising policy is characterised by a soft Bellman equation. The main obstacle is the absence of a discount-factor contraction. We resolve this by introducing a minorisation-based sub-stochastic kernel that yields a strict contraction of the soft Bellman operator. We establish Fréchet differentiability and Lipschitz smoothness of the log-likelihood score, leading to a gradient ascent algorithm with convergence guarantees. Two numerical examples, a malware-spread MFG and an RKHS-based consumer-choice model, show that the recovered policies closely match expert behaviour.

---


### 236. [Skill-to-LoRA: From Using Skills to Learning Behaviors for Token-Efficient LLM Agents](https://arxiv.org/abs/2606.16769)

**<font color=#1a73e8>作者：</font>** Tianyi Zhang, Zhonghao Qi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills are commonly distributed as this http URL files: human-readable procedural documents that describe workflows, tools, resources, and domain conventions. While convenient for inspection and reuse, this design requires the same reusable procedure to be repeatedly injected into the runtime context. We propose Skill-to-LoRA(S2L), a behavior-centric skill representation that replaces runtime skill text with skill-specific LoRA adapters. Rather than compressing the skill document itself, S2L models the behavioral change induced by the skill text: offline, the complete this http URL is used to synthesize skill-guided demonstrations; online, the full document is omitted and the corresponding LoRA adapter is dynamically loaded to activate the learned skill behavior. We evaluate S2L with Qwen3.6-27B on a 21-skill subset of SWE-Skills-Bench. Compared with the no-skill and Full Skill Text baselines, S2L improves pass rate by 2.9 and 5.2 percentage points, respectively, while reducing per-step token cost by 6.6% relative to Full Skill Text prompting. S2L matches or improves Full Skill Text on 18/21 skills and the no-skill baseline on 15/21 skills. Control experiments further show that the gains depend on skill-specific adapter alignment: Wrong-LoRA and Shared-LoRA both reduce performance. These results suggest that many procedural agent skills can be converted from runtime instructions into trainable, dynamically loadable behavioral modules. Code will be released upon acceptance.

---


### 237. [GD$^2$PO: Mitigating Multi-Reward Conflicts via Group-Dynamic reward-Decoupled Policy Optimization](https://arxiv.org/abs/2606.16771)

**<font color=#1a73e8>作者：</font>** Haotian Liu, Yihao Liu, Jingwei Ni 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As LLMs advance, post-training reinforcement learning (RL) increasingly relies on multi-dimensional rewards to cultivate comprehensive capabilities. This shift demands new algorithms capable of optimizing diverse and potentially competing objectives simultaneously. To address this, existing methods such as Group reward-Decoupled Policy Optimization (GDPO) decompose the overall score into independent reward groups, then compute the RL loss separately within each group. However, this strategy still encounters multi-reward conflicts: a single rollout can yield positive advantages on certain reward dimensions but negative ones on others, causing opposing signals to cancel each other out during aggregation, further hindering RL training efficiency. Inspired by Dynamic sAmpling Policy Optimization (DAPO), which improves RL training efficiency by filtering out ineffective rollouts with near-zero advantages, we propose Group-Dynamic reward-Decoupled Policy Optimization (GD$^2$PO). Specifically, GD$^2$PO employs a conflict-aware filtering mechanism to mask out rollouts suffering from severe reward-wise disagreement. By preventing conflicting signals from canceling each other out, this masking strategy preserves and enhances the magnitude of effective RL advantages, thereby significantly accelerating learning efficiency. Furthermore, we introduce query-level reweighting to dynamically adjust the update intensity of each query based on its overall reward consensus. Experiments on various multi-reward scenarios, including tool calling and human preference alignment, demonstrate that GD$^2$PO consistently and significantly outperforms existing baselines. The code is available at this https URL.

---


### 238. [OpenClaw-Skill: Collective Skill Tree Search for Agentic Large Language Models](https://arxiv.org/abs/2606.16774)

**<font color=#1a73e8>作者：</font>** Tianyi Lin, Chuanyu Sun, Jingyi Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Equipping Large Language Model (LLM) agents with effective skills is crucial for solving complex tasks in real-world systems like OpenClaw. In this work, we aim to develop a framework that automatically constructs such reusable skills to enhance LLMs in tool use, multi-step reasoning, and dynamic environment interaction. To this end, we propose Collective Skill Tree Search (CSTS), a novel tree-search-based skill construction framework that constructs structured, diverse and generalizable tree of skills. The core idea of CSTS is to leverage collective intelligence to jointly search, identify and compose effective skills via two iterative phases: Collective Skill Node Generation (CSN-Gen) and Collective Skill Node Assessment (CSN-Assess). CSN-Gen exploits collective knowledge from multiple models to explore diverse candidate skills for each subtask, enabling comprehensive skill exploration. CSN-Assess employs multiple models as judges to evaluate and select skill nodes with two scoring mechanisms: (1) collective quality scoring that aggregates independent evaluations to produce a robust estimate of skill effectiveness, and (2) collective transferability scoring that explicitly verifies whether a skill generalizes well across different models. With CSTS, we construct a set of comprehensive tree of skills along with skill-augmented training data, enabling models to effectively learn and utilize skills. Besides, we introduce Collective Skill Reinforcement Learning, which actively selects multiple relevant skills from the tree to broaden solution-space exploration, avoid being trapped by a single skill and its resulting homogeneous or suboptimal solutions. As a result, our trained model, OpenClaw-Skill, exhibits outstanding agentic capabilities in long-horizon planning, tool use and generalization over challenging benchmarks.

---


### 239. [A comparison of human and LLM-simulated participants in a writing style task](https://arxiv.org/abs/2606.16778)

**<font color=#1a73e8>作者：</font>** Felix Gröner, Erin K. Chiou  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Because large language models (LLMs) can produce natural language that is sometimes indistinguishable from texts produced by people, some researchers are starting to consider replacing human participants with LLM simulations. In this study, we test the extent to which the findings of a simulation with an LLM prompted to act as a synthetic participant match those obtained from 30 human participants. In our experiments, we evaluated how well writing style preference inference algorithms adapted to a participant over repeated interactions, compared to a baseline. We discover hints of bias and a lack of depth in GPT-4o's text generation and judgement that prevent it from accurately simulating people's behavior. Our results also hint at human biases that highlight the importance of considering human factors in the evaluation of systems that depend on human-automation interaction. Rather than treating these discrepancies as evidence for or against the validity of LLM-simulated participants, we present this study as a case analysis of methodological and design challenges.

---


### 240. [Gen-VCoT: Generative Visual Chain-of-Thought Reasoning via Diffusion-Based RGB Intermediate Representations](https://arxiv.org/abs/2606.16783)

**<font color=#1a73e8>作者：</font>** Zhiqiang Zhou, Junliang Dai, Xu ling  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) excel at visual reasoning but rely on text-based chain-of-thought (CoT), lacking interpretable visual intermediates. Existing methods use opaque tokens or external tools, missing key properties. We propose Gen-VCoT, a framework using expert vision models to generate RGB images as reasoning intermediates. It has three stages: visual grounding (SAM segmentation), geometric reasoning (Marigold depth maps), and semantic reasoning (Qwen2-VL integration). An adaptive router selects reasoning depth. Evaluations show Gen-VCoT improves spatial (25% better) and depth (50% better) questions, but may hurt simple factual queries. Text CoT outperforms visual intermediates on CLEVR (91.2% vs 62.5%), showing task-dependent optimal representations. Gen-VCoT establishes a new paradigm for interpretable multimodal reasoning.

---


### 241. [LLM-Based Visual Explanation Evaluation Framework for Assessing the Explainability of Facial Skin Disease Classification Models](https://arxiv.org/abs/2606.16794)

**<font color=#1a73e8>作者：</font>** Gyuyeon Na  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study proposes a domain-specific LLM-based Visual Explanation Evaluation Framework for assessing Grad-CAM explanations in facial skin disease diagnosis models. While previous studies have primarily focused on improving classification performance through data augmentation techniques, relatively few studies have systematically examined whether model explanations are grounded in clinically relevant lesion regions.
In this study, geometric augmentation, color-based augmentation, and mixed augmentation strategies were applied to facial skin disease classification models based on EfficientNet-B0, MobileNetV3, and ResNet18. Grad-CAM was employed to generate visual explanations representing the models' decision-making processes. Furthermore, an LLM-as-a-Judge evaluation framework was designed using GPT-5.5, Gemini 3.5 Flash, and Claude Sonnet 4.6 to assess Grad-CAM explanations from the perspectives of lesion localization and explanation trustworthiness. To improve evaluation consistency and clinical grounding, a progressive prompt engineering strategy was introduced, incorporating evaluation rubrics, clinical knowledge, penalty rules, and structured output formats.

---


### 242. [Decoupling Semantics from Distortions: Multi-Scale Two-Stream Vision-Language Alignment for AI-Generated Image Quality Assessment](https://arxiv.org/abs/2606.16799)

**<font color=#1a73e8>作者：</font>** Zijie Meng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing vision-language model (VLM)-based AI-generated image quality assessment (AIGIQA) methods suffer from a fundamental semantic-distortion dimensional conflict: monolithic representations optimized for semantic discrimination inherently entangle compositional understanding with low-level perceptual sensitivity, rendering them blind to fine-grained quality degradations. We introduce MST-CLIPIQA, a multi-scale two-stream framework that achieves hierarchical vision-language alignment through explicit representational decoupling. Our architecture leverages dual CLIP encoders with complementary patch granularities: coarse-grained streams capture global semantic coherence while fine-grained streams preserve textural signatures and artifact patterns. An information bottleneck-inspired gated fusion mechanism performs adaptive cross-scale distillation, with optional cross-attention enabling prompt-anchored correspondence evaluation when generation prompts are available. Extensive experiments across five benchmarks establish new state-of-the-art results, achieving average improvements of 1.11 percent SRCC on quality and 2.35 percent SRCC on text-image correspondence prediction, while maintaining efficiency with only 0.8M trainable parameters. Our project is available at this https URL.

---


### 243. [The Art of Mixology: Mixup-based Obfuscation for Privacy-Preserving Split Learning in Large Language Models](https://arxiv.org/abs/2606.16801)

**<font color=#1a73e8>作者：</font>** Chen Chen, Xiang Gao, Xianshun Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Split learning provides a practical paradigm for resource-constrained users to train Large Language Models (LLMs) by offloading computation-intensive layers to a server while keeping raw data local. However, existing privacy-preserving split learning methods still face a difficult trade-off among utility, privacy, efficiency, and stability. Specifically, these methods often suffer from substantial utility degradation, remain vulnerable to advanced data reconstruction attacks, incur prohibitive computational and communication overhead, or exhibit unstable performance across different tasks. In this paper, we propose MIXGUARD, a novel mixup-based privacy-preserving split learning framework for LLMs. MIXGUARD introduces token-level obfuscation, representation-level obfuscation, and adaptive gradient perturbation mechanisms, which operate jointly to preserve useful learning signals while preventing privacy leakage to the server. Technically, MIXGUARD first constructs a lightweight calibration model on a public dataset to refine the approximated target representation, and then applies this model during privacy-preserving fine-tuning on private data. We conduct extensive experiments on four classification tasks and four text generation tasks across multiple LLM families, model sizes, architectures, and fine-tuning strategies. The results show that MIXGUARD preserves model utility comparable to non-split training baselines, consistently achieves stronger privacy protection than existing split learning defense methods against state-of-the-art data reconstruction attacks, and remains robust under adaptive attack settings.

---


### 244. [LabOSBench: Benchmarking Computer Use Agents for Scientific Instrument Control](https://arxiv.org/abs/2606.16802)

**<font color=#1a73e8>作者：</font>** Anqi Zou, Han Deng, Chengyu Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current computer-use benchmarks primarily focus on software operation tasks in virtualized systems, whereas scientific instrumentation scenarios require coordinated control over complex interfaces, and feedback-driven parameter adjustment. However, directly evaluating agents on physical high-precision instruments is impractical due to high cost, safety risks, limited accessibility, and difficulty in ensuring reproducible evaluation. This motivates the need for a simulated yet realistic testbed that preserves the operational challenges of scientific instruments while enabling scalable and safe benchmarking. To this end, we introduce LabOSBench, a challenging benchmark for multimodal GUI agents built on a suite of web-based scientific-instrument simulators. Operating directly via a browser, LabOSBench avoids resource-heavy OS virtualization while supporting flexible task configuration and execution-based evaluation. Specifically, LabOSBench constructs 96 subtasks across eight instrument simulators, covering workflows from sample loading, alignment, parameter tuning, and data acquisition to result inspection. We evaluate general-purpose vision-language models, specialized GUI agent models, and advanced agentic frameworks at both subtask and end-to-end levels. Our experiments reveal that while existing agents can complete many structured GUI subtasks, they still struggle with feedback-driven operations and long-horizon workflow execution. Overall, LabOSBench provides a reproducible, low-cost testbed for advancing computer-using agents toward scientific-instrument control.

---


### 245. [LLM-based Visual Code Completion for Aerospace Geometric Design](https://arxiv.org/abs/2606.16806)

**<font color=#1a73e8>作者：</font>** Hau Kit Yong, Robert Marsh, Edmar A. Silva 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in both Large Language Models (LLMs) and Vision Language Models (VLMs) have seen a step change in their ability to perform visual code completion, but the aerospace industry, which prioritizes safety and explainabilty over rapid LLM adoption, currently has no publicly announced LLM-based geometric design copilot systems in commercial use by aerospace Original Equipment Manufacturers (OEMs). This paper presents a LLM-based visual programming copilot application for aerospace engineering design tasks, using a visual programming variant of the ReAct methodology and GPT 5.4. In addition to the copilot, we describe Wingbuilder, a new Grasshopper plugin library with custom components for aerospace-specific geometry abstraction, and an associated Aerospace Visual Programming Dataset (AVPD) with 18 aerospace expert designed tasks at different levels of difficulty alongside ground truth solutions. We evaluate our copilot application with a user trial involving two experienced aerospace engineers from a large aircraft manufacturing company. We find our copilot visual programming ReAct methodology was successful in generating suggestions that participants found helpful, but slow ReAct inference times limit its usefulness to more complex time-consuming tasks where waiting for good copilot solution suggestion was worthwhile. Participants reported they liked the tool and would be willing to use it in the future.

---


### 246. [Adaptive and Explicit safe: Triggering Latent Safety Awareness in Large Reasoning Models](https://arxiv.org/abs/2606.16808)

**<font color=#1a73e8>作者：</font>** Ke Miao, Jiaxin Li, Hongliang Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Reasoning Models (LRMs) excel at complex tasks, they remain highly vulnerable to sophisticated jailbreaks and direct harmful queries. To address this vulnerability, prior works depend heavily on external manual data annotation for safety alignment. However, we observe that LRMs can inherently identify safety risks when being re-presented with original queries alongside their own reasoning trajectories -- a capability we term Latent Safety Awareness. To leverage this safety awareness, we first employ Supervised Fine-Tuning (SFT) to explicitly induce safe tags to trigger safety analysis and guidance following the initial reasoning content for unsafe queries, while preserving standard responses for general queries to ensure adaptive triggering. Subsequently, we apply Direct Preference Optimization (DPO) to further enhance the correctness and stability of the safety analysis and guidance. Notably, responses required for both training stages are entirely generated by models being optimized. With (Safe Trigger) SFT and DPO, experimental results demonstrate significant safety enhancement. For example, the Attack Success Rate (ASR) of DeepSeek-R1-Distill-Llama-8B, on average, drops 24.65% and 36.72% on harmful and jailbreak benchmarks, respectively. Finally, our Safe Trigger method exerts almost no negative impact on general performance or user experience.

---


### 247. [Scaling LLM Reasoning from Minimal Labels: A Semi-Supervised Framework with a Lightweight Verifier](https://arxiv.org/abs/2606.16811)

**<font color=#1a73e8>作者：</font>** Keizo Kato, Chenhui Chu, Yugo Murawaki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For the development of Large language models (LLMs), recent approaches to generating pseudo intermediate reasoning have shown remarkable progress. But they typically rely on large numbers of correctly annotated answers to assess reasoning quality. This paper presents a semi-supervised framework that scales reasoning learning from minimal supervision, turning reasoning verification itself into a data creation mechanism. We train a lightweight reasoning-correctness classifier on only a few labeled samples, which judges whether intermediate reasoning traces generated by an LLM are valid. Furthermore, an entropy-based confidence threshold filters out unreliable samples, and the remaining high-confidence reasoning traces are used to fine-tune the model. Experiments on Verifiable Math Problems (Orca-Math subset) and Question Answering on Image Scene Graphs (GQA) with Visual Programming show that our method achieves accuracy comparable to using 10-15x more labeled data. Ablation analyses confirm that both the classifier and entropy filtering are essential for scalable and noise-resistant pseudo-labeling. By replacing expensive answer-level supervision with lightweight reasoning verification, our method provides a practical path toward constructing large-scale reasoning resources and paves the way for future autonomous reasoning systems that learn from minimal human input.

---


### 248. [GIST-CMTF: Goal-State Inference for Causal Minimal Tool Filtering in LLM Agents](https://arxiv.org/abs/2606.16813)

**<font color=#1a73e8>作者：</font>** Rahul Suresh Babu, Rohit Shukla  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented LLM agents rely on runtime filtering to decide which tools should be visible at each step. Causal Minimal Tool Filtering (CMTF) reduces tool-choice confusion by exposing only the next causally necessary tool frontier, but it assumes that the user request has already been mapped to a symbolic goal state. In practice, requests such as "handle my appointment" or "take care of this email" may correspond to multiple possible goals. This creates wrong-goal execution, where an agent follows a valid causal tool path for an unintended objective. We introduce GIST-CMTF, a goal-state inference layer that predicts candidate symbolic goals over the same state-transition vocabulary used by CMTF, estimates ambiguity, and either applies CMTF or exposes clarification as a causal action that produces missing goal or state variables. We evaluate GIST-CMTF across seven model backends, six filtering methods, and 120 controlled tool-use tasks. GIST-CMTF achieves 97.0% task success, compared with 80.1% for top-goal CMTF and 82.9% for semantic-goal CMTF. It reduces wrong-goal execution from 19.4% under top-goal CMTF to 2.5%, while preserving the one-tool exposure of causal filtering and using substantially fewer tokens than all-tools exposure. These results suggest that reliable tool-augmented agents should validate goal state, not only tool relevance, before exposing external actions.

---


### 249. [How Much Can We Trust LLM Search Agents? Measuring Endorsement Vulnerability to Web Content Manipulation](https://arxiv.org/abs/2606.16821)

**<font color=#1a73e8>作者：</font>** Yimeng Chen, Zhe Ren, Firas Laakom 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based search agents synthesize open-web content into actionable recommendations on behalf of users, creating a risk that attacker-published pages are transformed into endorsed claims. We introduce SearchGEO, a controlled evaluation framework for measuring endorsement corruption in LLM-based web-search agents, combining a web-evidence manipulation pipeline, a five-mode attack taxonomy, and multiple output-level metrics. We evaluate 13 LLM backends on 308 cases each. Results show that vulnerability patterns vary across backends: overall attack success rate (ASR) ranges from 0.0% on Claude-Sonnet-4.6 to 31.4% on Gemini-3-Flash, the strongest attack mode differs by model family, and the same deployment scaffold could amplify or decrease ASR on different backends. An auxiliary agent-skill probe, where endorsement becomes an install command, exposes a sharp split among otherwise robust backends: Claude over-rejects while GPT over-trusts. These findings argue for treating recommendation reliability under adversarial search content as a first-class dimension of backend safety evaluation.

---


### 250. [Tying the Loop -- Tied Expert Layers in Mixture-of-Experts Language Models](https://arxiv.org/abs/2606.16825)

**<font color=#1a73e8>作者：</font>** Martin Jaggi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures efficiently scale Large Language Models (LLMs) by activating only a small fraction of their experts per token, yet the full parameter count - dominated by the expert parameters - must be held in training and inference memory. To address this, we introduce Expert Tying, an architectural modification that shares expert parameters across consecutive transformer layers while preserving independent, layer-wise routing and attention.
We evaluate this approach across common, state-of-the-art architectures, including OLMoE, Qwen3, and DeepSeek-style MoEs. Our pretraining experiments demonstrate that tying experts can reduce memory footprint by almost 2x at virtually no degradation in perplexity or downstream quality. By exploiting the parameter redundancy inherent in MoE pathways, our method provides a highly favorable compute-to-memory trade-off, advancing efficient training and scaling of next-generation LLMs.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-270](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
