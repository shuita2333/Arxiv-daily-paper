# 📦 其他研究 | 2026年10月23日

> 本类共 **232** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-232](./part-05.md)

---

### 1. [Interaction-Gated Time-Frequency Learning for Parameter-Efficient PPG-Based Heart Rate Estimation](https://arxiv.org/abs/2610.28693)

**<font color=#1a73e8>作者：</font>** Anh Khoi Pham, Phat Lam, Thien Truong Nguyen Ly 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Photoplethysmography (PPG) enables low-cost and non-invasive heart rate (HR) monitoring but remains sensitive to waveform distortion, physiological variability, and measurement interference. Temporal waveform characteristics and frequency-domain periodicity provide complementary information for HR estimation; however, effectively exploring and integrating these representations within a compact model remains challenging. This paper proposes TF-IG, a parameter-efficient interaction-gated time-frequency learning framework for PPG-based HR estimation. TF-IG employs a dual-branch architecture in which a temporal branch captures pulse morphology via dilated depthwise-separable convolutions, while a frequency branch extracts cardiac periodicity information from bounded log-spectrogram representations. To combine the two domains, we introduce an interaction-gated fusion module that explicitly models feature agreement and discrepancy, while also learning feature-wise weights to balance temporal and spectral information. A parameter-shared regression head further maps the temporal, spectral, and fused representations into the final HR prediction space. Experiments on the benchmark BIDMC PPG and Respiration Dataset using a subject-exclusive training, validation, and test protocol show that TF-IG achieves a mean absolute error (MAE) of 1.227 BPM, a root mean square error (RMSE) of 2.060 BPM, a Pearson correlation coefficient of 0.9934, and 92.28 percent of estimates within 3 BPM, while remaining parameter-efficient with only 84.6K parameters. Ablation results further demonstrate the complementary contributions of the temporal and frequency branches, interaction-gated fusion, and shared regression head. These results indicate that explicitly modeling cross-domain interactions provides an effective accuracy-complexity trade-off for lightweight PPG-based HR estimation.

---


### 2. [Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds](https://arxiv.org/abs/2610.28698)

**<font color=#1a73e8>作者：</font>** Kuan Zhang, Yukun Chen, Zhihao Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling data, diversity and model capacity has improved embodied learning in physical environments, where diverse experiences remain grounded in shared physical laws. Whether these gains extend to virtual worlds with different visual styles, dynamics, controls, and objectives remains unclear. We investigate this question through a controlled study of continued pre-training (CPT) across three axes: data volume, diversity, and model size. Our 120 training configurations span four model sizes from 0.8B to 27B, six data budgets from 50 to 1,600 hours, and five mixtures ranging from Minecraft-only data to diverse multi-world corpora. We assess performance and generalization using three-level validation losses and gameplay benchmarks from in-corpus worlds to unseen worlds. Our results show: (1) more data improves in-corpus performance, diversity improves transfer to related worlds with limited gains in distant worlds, and model size improves data efficiency but generalizes worse to distant worlds under single-world training; (2) we observe an early interface phase with broad cross-world benefits and a later world phase with gains narrowed to in-corpus and related worlds, and fit an empirical scaling law relating validation loss to data volume, diversity and model size; and (3) our models are competitive with Minecraft specialists and frontier models in 3D worlds, and perform best in real-time settings. However, the limits of imitation and persistent gaps in distant worlds suggest that building generalist embodied agents requires richer training stages beyond continued pre-training.

---


### 3. [Reinforcement learning for hardware acceleration and system-level optimization on FPGA and integrated-circuit platforms: A survey](https://arxiv.org/abs/2610.28699)

**<font color=#1a73e8>作者：</font>** Hamza Kheddar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) enables adaptive and autonomous decision-making in embedded, edge, and heterogeneous computing systems. Field-programmable gate arrays (FPGAs) and integrated circuits (ICs) offer low latency, energy efficiency, and architectural flexibility for RL deployment, while introducing challenges in resource constraints, implementation complexity, and hardware-algorithm co-design. This review surveys more than 100 studies on RL implementations across FPGA and IC platforms, emphasizing architectures, implementation strategies, performance evaluation, and applications. The literature is organized by RL family, including model-based Markov decision processes, classical value-based methods, deep RL, actor-critic, policy-gradient, and multi-agent approaches. We further classify studies by abstraction level, hardware realization strategy, and application domain, examining how RL algorithms map onto reconfigurable and fixed hardware. Unlike surveys restricted to particular algorithms or platforms, this work provides a unified analysis of FPGA and IC implementations, covering acceleration, reconfigurable architectures, energy-aware control, and system-level optimization. Comparative assessments consider resource utilization, latency, throughput, power consumption, and reported performance gains. Finally, we identify recurring architectural patterns, practical limitations, open challenges, and research directions for efficient RL-driven hardware systems. The survey offers a consolidated reference for researchers developing and evaluating RL solutions on specialized hardware.

---


### 4. [Scalable Stress-Constrained Topology Optimization: A Super-resolution and Simultaneous Approach Based on Machine Learning](https://arxiv.org/abs/2610.28703)

**<font color=#1a73e8>作者：</font>** Xiangyu Sun, Shirin Hosseinmardi, Ramin Bostanabad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale topology optimization (TO) remains computationally demanding, especially for stress-constrained problems. To address this challenge, we propose the simultaneous neural topology optimization (SNTO) framework where we represent state, adjoint, and design variables with custom neural networks (NNs) whose parameters are jointly optimized within a single optimization loop that leverages continuous adjoint analysis and automatic differentiation. This optimization minimizes a multi-component loss function that combines the design objective, an aggregation of the local stress constraints, and the potential energy functionals. Our NNs have a unique architecture that accelerates convergence while enabling the networks to capture sharp gradients and boundaries which are critical to stress-constrained TO. To achieve scalability to millions of degrees of freedom (DoF), we develop a hardware-aware training scheme in which the design domain is partitioned into subdomains that are distributed across multiple GPUs. To control peak GPU memory usage, we further slice each subdomain into smaller regions whose loss gradients are evaluated sequentially and accumulated to update the NN parameters. Unlike domain decomposition approaches, our partitioning naturally ensures field continuity across the subdomains and does not require the introduction of additional terms into the loss function. For validation, we first evaluate the proposed framework on various 2D stress-constrained benchmarks and compare our results to a conventional finite element-based approach, showing that SNTO produces super-resolution designs with sharper boundaries, smaller gray areas, and lower volume fractions. We then consider large-scale 3D problems with up to eight million collocation points and distribute the training over up to eight GPUs.

---


### 5. [Translation and data ethics](https://arxiv.org/abs/2610.28710)

**<font color=#1a73e8>作者：</font>** Joss Moorkens, Monja Jannet  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This chapter introduces data ethics for translation and discusses a number of ethical issues regarding data. These include issues of copyright, ownership and bias, which apply to all types of data, whereas there are further issues particular to minoritised language communities and those on either side of the digital divide, as data is implicated in power imbalances and dynamics. We close with a discussion of responsibility and regulation, and reflect on the growing attention on data ethics from translation studies researchers.

---


### 6. [Offline Apprenticeship Learning for Human-Centric Environments](https://arxiv.org/abs/2610.28716)

**<font color=#1a73e8>作者：</font>** Md Mirajul Islam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective decision-making in human-centric environments such as Intelligent Tutoring Systems (ITSs) and clinical healthcare requires policies that are adaptive, data-efficient, and ethically deployable. Apprenticeship Learning (AL) infers policies directly from expert demonstrations by recovering the underlying reward structure, enabling strictly offline learning without environment interaction. This dissertation develops a progression of offline AL frameworks organized around two challenges: reward modeling and demonstration quality. For reward modeling, EM-EDM clusters demonstrations by latent reward functions and induces cluster-specific policies, and THEMES partitions trajectories into temporally coherent sub-trajectories guided by a hierarchically learned reward regulator; across one educational and three clinical datasets, THEMES outperforms flat and hierarchical AL baselines. For demonstration quality, HALIDE integrates continuous quality signals into hierarchical policy induction, enabling principled reuse of mixed-quality data under distribution shift. CCHAL further attributes quality to individual decisions via Bayesian credit assignment, dual-arm criticality scoring that contrasts expert and non-expert behavior, and a Bradley-Terry contrastive IRL objective over failure trajectories, outperforming baselines including HALIDE on three clinical EHR datasets and an ITS dataset. Finally, a real-world classroom evaluation of StuEDM, an EDM-induced policy that preserves student agency and intervenes only on disagreement, shows significant learning gains over an Expert baseline and a higher pretest-adjusted posttest score than a CQL policy trained on a far larger corpus, while overriding students less than half as often. Together, this work establishes offline AL as a practical, data-efficient, and ethically viable paradigm for human-centric environments.

---


### 7. [Different Defects, Different Effects: A Controlled Audit of Face Recognition Training Data](https://arxiv.org/abs/2610.28766)

**<font color=#1a73e8>作者：</font>** Ana Dias, João Ribeiro Pinto, Hugo Proença 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The development of face recognition has been strongly supported by the availability of large-scale training datasets. Among them, MS-Celeb-1M has played an important role by providing millions of facial images from nearly 100K identities. However, the size and heterogeneity of such datasets increase the likelihood of annotation errors, redundant samples, and other forms of data inconsistency. This motivated the introduction of refined versions, such as MS1MV2 and MS1MV3, aimed at improving the quality of the training data. Despite these cleaning efforts, we show that several types of training-data defects remain in MS1MV3. By proposing complementary data-auditing strategies, we identify five defect categories: exact and near-duplicate images, split identities, crop errors, multiple-face ambiguity, and invalid content. We then assess the effect of correcting these defects under a controlled face-recognition training protocol based on IResNet-50 and ArcFace. The results show that targeted interventions can preserve, and in some cases improve, recognition performance while requiring fewer optimization steps to reach the performance of the original training set. Duplicate removal provides the clearest overall benefit, while split-identity merging and invalid-content removal also improve training efficiency. Overall, the results indicate that the effect of dataset cleaning depends strongly on the type of defect being addressed and provide further evidence that training-data quality remains an important and comparatively underexplored factor in large-scale face recognition. The training manifests and code used in this work will be released upon acceptance.

---


### 8. [Motion Equivariant Convolutional LSTM: When Motion Becomes a Gauge Symmetry](https://arxiv.org/abs/2610.28771)

**<font color=#1a73e8>作者：</font>** Vahid Hosseinzadeh, T. Anderson Keller, Michael Puthawala  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Objects move, cameras pan, and weather drifts with the wind: much of what changes in sequential data is motion. Motion changes where things are, not what they are, and is therefore a symmetry of the data. Yet standard recurrent networks are not equivariant to it: their memory stays put while the input moves on. Flow equivariant recurrent networks first brought this symmetry into sequence models, for motions of constant velocity, or flows, by enumerating a bank of velocities. We extend this idea in three directions: from simple recurrent networks to convolutional LSTMs, from flows to motions whose velocity changes in time, and from enumerating velocities to estimating them. Treating a sequence as a field over time, we show that motion becomes a gauge symmetry: a global symmetry made local in time. Built on this view, our motion equivariant convolutional LSTM (MELSTM) uses its velocity model as the gauge field and is provably equivariant to every motion. Across future-frame prediction, classification of digits visible only through their motion, and action recognition under camera shake, MELSTM outperforms a convolutional LSTM and its flow equivariant counterpart with the same number of parameters: it is more accurate, generalizes to longer horizons and to unseen motions, and carries a fraction of the flow equivariant model's state.

---


### 9. [Second Thoughts: Exploring and Planning through Comparative Imagination in World Models](https://arxiv.org/abs/2610.28779)

**<font color=#1a73e8>作者：</font>** Hieu Tran, Hong Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models let agents compare imagined outcomes before acting, but an agent must still decide which alternatives to explore and when a proposed plan should replace its learned policy. We introduce SDI (Sibling Disagreement in Imagination), which connects these decisions through a shared actor-based reference. SDI compares action sequences imagined from the same model state, using repeated rollouts of the actor's own sequence to measure variation under fixed behavior. This reference scales both the spread across candidate returns, which provides an exploration signal, and a proposed plan's predicted advantage, which governs action acceptance. The agent executes a planned action when its advantage exceeds the reference variability by a fixed factor; otherwise, it follows the actor. SDI reuses the base agent's world model, actor, and critic without requiring an additional disagreement ensemble. Exploration and planning guide training data collection, while evaluation uses the learned actor alone. Across Meta-World, Adroit, and DM-Control, SDI achieves a higher observed task-average score than every compared baseline in each suite and matches or exceeds the strongest baseline's performance on 15 of 18 tasks. Component ablations and robustness analyses further examine the roles of exploration, planning exposure, and action acceptance. Paired evaluations from identical simulator states show that the gate improves both recovery from actor failures and preservation of successful behavior relative to ungated planning, while substantially reducing return degradation. Together, these results support comparing imagined alternatives against a shared actor reference as a unified approach to exploring and planning with world models.

---


### 10. [Extreme Low-State Quantized Transformer for Electricity-Load Forecasting](https://arxiv.org/abs/2610.28784)

**<font color=#1a73e8>作者：</font>** Muhammad Sabbir Alam, Harindra Sandun Mavikumbure, Victor Cobilean 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aggressive low-state weight quantization can substantially reduce neural-network representational flexibility, making predictive performance difficult to preserve when only a few discrete weight states are available. We investigate this regime for Transformer-based electricity-load forecasting using 3-, 5-, 7-, and 16-state weight quantization across feed-forward-only and attention-plus-feed-forward quantization. Two tasks predict either the next hour or the next 24 hours from the preceding 48 hours across two co-primary electricity-consumption datasets. Direct post-training quantization (PTQ) increased mean normalized root-mean-square error (NRMSE) relative to full precision by 6.25 and 7.04 percentage points in Datasets A and B, whereas quantization-aware fine-tuning (QAT-FT) recovered approximately 90.2% and 94.5% of these penalties. Quantization-aware training from random initialization (Scratch-QAT) also produced competitive low-state solutions, with particularly favorable behavior at three states. We further introduce accumulated-update thresholding, which accumulates optimizer-proposed weight changes before commitment. Relative to paired Scratch-QAT controls, this reduced committed shadow-weight updates by approximately 99.7% and discrete state transitions by approximately 77--80%, while mean NRMSE changed by only +0.042 and +0.197 percentage points. These results show that useful Transformer forecasting can be retained under highly discrete weight representations while strongly suppressing target-state activity, supporting a prospective route toward compact, low-activity edge forecasting using multilevel synaptic devices.

---


### 11. [ArcFlow: Training Flow Policies for Multiple Solver Budgets](https://arxiv.org/abs/2610.28788)

**<font color=#1a73e8>作者：</font>** Hieu Tran, Hong Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow-matching policies adjust inference cost through the number of solver steps, but reinforcement learning at a single fixed solver budget can hide degradation at cheaper deployment budgets and even erase useful one-step behavior present in a pretrained policy. We introduce Action-Ratio-Clip Flow (ArcFlow), a deployment-aware algorithm for training one flow policy across a specified range of solver budgets. ArcFlow combines action-aligned supervision, budget exposure, and worst-budget checkpoint selection. For reconstruction objectives, its bridge aggregates temporal probes into one surrogate ratio and one PPO-style clip per action, with a boundary residual exactly equal to deployed one-step reconstruction error. Cycling exposes the shared field to the deployment range, and selection optimizes its performance floor. For native velocity objectives, multi-budget endpoint supervision applies the same principle without replacing the native update. Both realizations preserve the architecture and deployment-time cost. Across DM Control, manipulation, and locomotion, ArcFlow attains the highest mean one-step return among five flow-policy baselines on 25 of 30 tasks under each method's reported training settings. Component studies identify complementary improvements from boundary supervision, the fixed-grid bridge, budget exposure, and deployment selection. These results establish deployment-budget-aware training as an effective route to strong low-step control with one policy serving multiple inference costs.

---


### 12. [Sign Here: Attributing a Source for a More Trustworthy Software Supply Chain](https://arxiv.org/abs/2610.28794)

**<font color=#1a73e8>作者：</font>** Derek Garcia  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software supply chain attacks continue to be on the rise, exploiting the trust that helps open source ecosystems thrive. Recent incidents like the Shai-Hulud worm and the Axios compromise demonstrate that a single malicious package can have wide reaching and devastating impacts overnight. These high profile attacks can be traced back to the same culprit: package registries. Although they are a useful convenience to pull prebuilt packages from, is such a commonly exploited component of the software supply chain worth the risk? In this paper, we investigate whether removing the registry from the developer workflow by building packages directly from source can serve as a malware prevention strategy - effectively removing an entire attack surface. Our hypothesis is that malicious packages avoid attributing a source to minimize visibility, while benign packages seek exposure and therefore link to their repositories. We evaluate this through three research questions: how effective is building from source at avoiding malware, how feasible is it to build from source in the current state of the supply chain, and how the building from source strategy compares to state-of-the-art security scanners. To do so, we (1) construct an aggregate dataset of 47,066 malicious packages from four academic and one industry malicious datasets source across npm and PyPI ecosystems, (2) build a snapshot index of all 3.9 million npm and 764 thousand PyPI packages, and (3) analyze all malicious samples alongside a statistically significant sample of 16,569 packages from each registry, totaling 33,138 packages. We find that simply checking for a source has a success rate between 87.7 and 99.9 percent of preventing malware, depending on the level of source vetting. Consequently, there is a significant lack of transparency within benign packages, with only 47.4 percent attributing a source an end user could build from.

---


### 13. [An Explicit Feedback Contract for Iterative ML-Agent Harnesses](https://arxiv.org/abs/2610.28798)

**<font color=#1a73e8>作者：</font>** Kehui Yao, Chuanbo Hu, Jiao Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Iterative ML agents develop models by editing code, running experiments, reading a validation score, and choosing what to try next. In current harnesses this loop is served by an exact validation score returned after every attempt, which leaves the validation split open to adaptive selection. In this work, we introduce an explicit feedback contract for ML-agent harnesses, which specifies what an agent may observe, when iteration should stop, and when the test split may be touched. The contract releases a validation score only when a submission clears a noise threshold computed from the paired standard error, so no margin has to be tuned. We ran experiments on click-through-rate prediction, learning to rank, and a control task with no signal to find. The control is the sharpest case, because the true gain there is zero by construction: an agent reading exact scores ended by reporting a gain of 0.0157, while under the contract it reported 0.0033. On both real tasks the contract narrows the validation-test gap, and test performance is slightly higher rather than lower. The largest difference is in when the agents stop. Exact feedback used its entire budget of thirty submissions on two of the three tasks, including the one where nothing can be learned, while the contract halted after four to twelve. A run that exhausts its budget is usually read as diligence. It is better read as a symptom: when the feedback channel is unbounded, noise keeps supplying improvements to chase.

---


### 14. [Towards Realistic Models of Change: A Causal Perspective on Decision-Making and Dynamical Systems](https://arxiv.org/abs/2610.28803)

**<font color=#1a73e8>作者：</font>** Isacco Beretta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While statistical learning has made remarkable progress in recent decades, driven by large datasets and data-driven protocols that have transformed scientific practice, it still faces a key limitation: it struggles to generalize beyond the data it has seen, often failing under distribution shift. Causality offers a promising solution: causal models focus on the underlying mechanisms of change rather than surface-level associations, enabling robust reasoning under external interventions. This allows systems not only to learn from data, but also to reason about hypothetical scenarios, adapt to new environments, and inform better decisions. This thesis explores how these approaches can inform each other, in two parts.
The first part examines algorithmic recourse, that is, identifying which changes an individual can make to overturn an unfavorable decision. We propose an alternative perspective to the established framework, arguing for a more realistic cost function, a reformulation of the problem in causal terms, and the inclusion of a temporal dimension in policy evaluation.
The second part focuses on dynamical systems, extending the notions of causal interventions and effects to discrete and continuous stochastic processes. We show that the equilibria of these processes, and how they change following an intervention, can be linked to Structural Causal Models (SCMs), viewed as compressed representations of the underlying temporal dynamics. We argue for the relevance of such temporal causal models, since in real-world scenarios actions take time to produce their effects.
The common goal of both parts is practical: the utility, robustness, and trustworthiness of these models depend critically on their ability to realistically represent the underlying phenomena.

---


### 15. [SAIL: A Learnable Generalisation of Spatial Autocorrelation over Graph-Structured Data](https://arxiv.org/abs/2610.28806)

**<font color=#1a73e8>作者：</font>** Piotr Keller, Fayyaz Minhas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In vision and scientific domains involving spatial data, a key question is whether node feature values vary independently across space or form coherent spatial structures. Classical spatial autocorrelation statistics such as Moran's $I$ and Geary's $C$ quantify this phenomenon but operate on a single scalar variable with fixed neighbourhood weights, limiting their use for high-dimensional graph-like data. We introduce SAIL (Spatial Autocorrelation Index Learner), a differentiable framework that generalises spatial autocorrelation into a learnable operator by jointly learning feature projections defining candidate scalar fields and inter-node neighbourhood affinities. SAIL produces interpretable local and global spatial coherence descriptors, enabling supervised prediction and unsupervised discovery of spatial autocorrelation modes and hotspots. We show that SAIL exactly recovers classical spatial statistics under appropriate parametrisations and, for tasks driven by latent spatial autocorrelation, can approximate the Bayes-optimal predictor with an inductive bias matched to such tasks. Experiments on synthetic data and large-scale biomedical graphs demonstrate statistical correctness and discovery of spatial coherence with applications across vision, geospatial analysis, and biomedicine. The code repository is available at: this https URL.

---


### 16. [Forging More Tasks into Better Harnesses: Agentic Harness Evolution via Successive Scale Racing](https://arxiv.org/abs/2610.28815)

**<font color=#1a73e8>作者：</font>** Jingzhe Liu, Jiliang Tang, Tong Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic harness evolution optimizes an agent's instructions, tools, and control flow by using its task execution experiences as evolving evidence. While more evolution tasks should intuitively improve performance, our preliminary study reveals a paradoxical failure mode: the performance of existing methods degrades as the task pool expands. Our further analysis demonstrates that this degradation stems from suboptimal evidence selection during optimization, as different evidence combinations lead to substantially different evolution outcomes. To address this issue, we propose Successive Scale Racing (SSR), a framework that adaptively searches for optimal evidence combinations in each evolution round. SSR constructs diverse evidence combinations based on the corresponding task quality and coverage, and efficiently races the resulting candidate harnesses under a small compute budget. Empirically, across three distinct benchmarks, SSR achieves state-of-the-art results in all six configurations. Notably, as the task pool grows from 40 to 200, SSR steadily improves the pass rate from 64.3% to 68.3%, while the baselines' performances all drop. Furthermore, its racing mechanism identifies near-optimal candidates while reducing validation executions by 60%.

---


### 17. [Register Anything Model for Generalizable and Robust Point Cloud Registration](https://arxiv.org/abs/2610.28821)

**<font color=#1a73e8>作者：</font>** Zheng Qin, Junhua Xi, Yan Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Register Anything Model (RAM), a unified model for generalizable 3D point cloud registration that robustly estimates 6-DoF transformations across diverse domains spanning sensors and environments. Existing registration methods are typically tailored to a single domain, with carefully tuned architectures and hyperparameters, and thus degrade markedly when applied to novel domains. We bridge this gap by training a single model on diverse data from indoor, outdoor, and object domains. A central challenge is the severe geometric discrepancy across domains, i.e., differences in scene scale, sensor noise, point density, and structural patterns, which hinders processing with a unified point-based model. To address this, we introduce a geometry-aware normalization strategy that jointly voxelizes and normalizes point clouds into a standardized geometric space, adaptively based on their geometric properties to preserve salient local structures while standardizing resolution. Built on this normalization, RAM follows a hierarchical coarse-to-fine paradigm, and employs an efficient geometric transformer that models local geometric consistency instead of globally over all points. This design mitigates discretization noise introduced by voxelization, and improves computational efficiency. Extensive experiments on 12 benchmarks demonstrate state-of-the-art performance in terms of inlier ratio and registration recall. Notably, our method outperforms the counterparts trained on each separate domain, showing superior generalization capability.

---


### 18. [WorldStream: Streaming Interactive 3D Worlds with Hierarchical Planning and Persistent State](https://arxiv.org/abs/2610.28827)

**<font color=#1a73e8>作者：</font>** Xiaoxiao Ma, Weiyang Jin, Yanwen Ma 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present WorldStream, an open-ended 3D world model with three simultaneous capabilities: it extends playable terrain beyond any pre-specified map, acts on open-ended language in the running world, and restores visited places with their edits. A hierarchical planner over a typed decision model emits structured decision state: Macro fixes settlement, ecology, transport, and hydrological structure across a group of tiles; Micro specializes that contract into tile semantics under measured terrain and accepted neighbor commitments. Deterministic local code compiles accepted plans into terrain, roads, settlements, vegetation, and entities. Streaming separates their reach: plans run ahead along the predicted corridor, compilation only where movement will soon need it, geometry behind the user released. One world record retains plans, seeds, object identities and mutable state, boundary commitments, and edits by attribute, revised as the user advances and edits; returning tiles recompile from it. The same record grounds interaction: the model acts on existing entities, including stateful NPCs that update as they act, edits the present region, or attaches intent to unplanned regions. Together they yield a world expanding under bounded budgets, connected across independently planned tiles, and interactive.

---


### 19. [HorizonComposer: Spatiotemporally Consistent Driving Video Editing with Enriched Traffic Semantics](https://arxiv.org/abs/2610.28829)

**<font color=#1a73e8>作者：</font>** Mauricio Soroco, Yuqiu Liu, Zaid Tasneem 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-guided video generative models offer a scalable solution for stress-testing autonomous driving systems by simulating diverse environmental conditions. However, driving scenes operate within a dense Operational Design Domain (ODD) governed by strict traffic semantics. When applied to global driving-condition edits, general-purpose instruction-guided video editors frequently corrupt these semantics, leading to structural hallucinations and ``temporal shock.'' This work distills and protects traffic semantics during video editing at three levels. First, we construct a hybrid dataset by combining temporally aligned real-world videos with synthetic edits, balancing foundational scene structure with unambiguous appearance signals. Second, during training, we adapt advantage conditioning from offline reinforcement learning to align the model using dense rewards. We extract dense, pixel-level rewards from the hybrid data to serve as a localized signal and actively steer generation toward structurally reliable pixels. Finally, our model mitigates temporal shock by introducing thinking frames, a transition mechanism that seamlessly reconciles static image conditioning with dynamic video context. Extensive experiments demonstrate that our method prevents the corruption of multi-actor dynamics, establishing state-of-the-art spatiotemporal consistency, yielding consistent user preference (39% relative improvement in content preservation and 12% in temporal consistency), and achieving a significant 5% gain in downstream road line segmentation and 7% gain in downstream multi-object detection.

---


### 20. [Conditional Imaging for Privacy-Preserving Visual Sensing](https://arxiv.org/abs/2610.28835)

**<font color=#1a73e8>作者：</font>** Hengyu Lian, Debabrata Mandal, Anzhou Wen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional visual sensing faces a fundamental dilemma: information that should remain private today may need to be recovered tomorrow. This challenge is becoming increasingly important as cameras become pervasive in our daily surroundings. Existing safeguards either protect visual content only after an image is formed or suppress information during capture in ways that prevent its later recovery. Here, we show through an information-theoretic analysis that privacy and recoverability cannot be achieved simultaneously in static optical systems. Information preserved in a measurement for later reconstruction also remains available to an observer of that measurement, limiting the privacy such systems can provide. To overcome this limitation, we introduce conditional imaging, an imaging approach that changes the optical state for every captured frame. The measurement alone conceals the scene, while knowledge of the corresponding physical system state enables its reconstruction. We analyze how the optical parameters determine the information that can be recovered and use this analysis to guide the design of a camera prototype. We evaluate the system on a captured dataset of human faces using increasingly powerful attempts to recover the scene, from direct visualization and computational inversion to learned reconstruction and identity recognition. Our experiments show that conditional imaging preserves identity in authorized reconstructions while withholding visual information from observers without access to the system state. By making the physical state of the camera part of the information needed for reconstruction, conditional imaging enables visual information to be protected at the point of capture while remaining recoverable for future authorized use.

---


### 21. [Sketch2Sim: an end-to-end modular framework for hand-drawn circuit analysis](https://arxiv.org/abs/2610.28836)

**<font color=#1a73e8>作者：</font>** Mohammad Kawsar, Al Amin Islam Ridoy, Md Rakib Hossain 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study proposes a sketch-to-simulation system to solve handwritten circuit diagrams. The system converts raw images into a Simulation Program with Integrated Circuit Emphasis (SPICE)-compatible netlist and automatically calculates the circuit's nodal voltages and currents. Another objective is to propose a holistic framework that benefits students and educators by enhancing the teaching and learning experience of electric circuits and expediting engineering design reviews. This article presents a multistage pipeline that converts raw photographs of handwritten electric circuits into executable SPICE-like netlists, providing a solution. A dataset of 1,000 hand-drawn Resistor-Inductor-Capacitor (RLC) circuits was curated and annotated for components, text regions, and character recognition. The proposed system decomposes a circuit diagram into three stages: (i) dual You Only Look Once (YOLO)-based detectors for components and text regions, (ii) a Convolutional Recurrent Neural Network (CRNN) with Connectionist Temporal Classification (CTC) and Optical Character Recognition (OCR)-based domain-aware symbol value extraction, and (iii) image processing with thresholding, skeletonization, and Density-Based Spatial Clustering of Applications with Noise (DBSCAN) to automatically identify nodes and map them with corresponding components. The proposed system produces the netlist and solves the circuit. The qualitative and quantitative ablation studies on modular stages, as well as end-to-end tests, demonstrate robust performance across various handwriting styles, lighting conditions, and this http URL study serves as an interactive learning aid and practical tool for professionals, providing a comprehensive user interface (UI), enabling rapid digitization of circuit sketches for study, design, prototyping, or troubleshooting.

---


### 22. [How to Use Parallel Data for Multilingual Pretraining](https://arxiv.org/abs/2610.28838)

**<font color=#1a73e8>作者：</font>** Zhihong Huang, Yao Lu, Derek F. Wong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> High-quality human-translated parallel corpora can improve cross-lingual transfer, but are typically too small for large-scale pretraining. Machine-translated web corpora help overcome this limitation, making parallel data available at pretraining scale. Standard multilingual pretraining, however, samples source documents and their translations independently, without explicitly using their parallel structure. We investigate how to use the parallel structure of the data to improve multilingual pretraining by concatenating each document with its translation in the same training sequence. We compare this parallel pretraining (PPT) approach with standard pretraining (SPT), training models from scratch at matched token budgets. Surprisingly, despite the benefits of parallel data reported in prior cross-lingual work, PPT alone does not consistently improve language understanding over SPT. Our further analysis suggests that although PPT builds a strong cross-lingual foundation, as shown by its better use of shared information across languages, the mismatch between parallel training contexts and single-language task inputs limits its gains in general language understanding. This finding motivates a two-stage approach following the pretraining-fine-tuning paradigm: we first use PPT to build a cross-lingual foundation, then continue with SPT to adapt it to standard language modeling. In both high-resource and low-resource settings, the two-stage approach consistently improves general language understanding and cross-lingual task performance over standard pretraining alone at matched training budgets.

---


### 23. [KIRA: A Full-Stack Reading Screening System with Dual-Pathway Analysis for Children](https://arxiv.org/abs/2610.28840)

**<font color=#1a73e8>作者：</font>** Maggie Dong, Rohit Mekkoth, Zixuan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Early-grade reading screening is critical for identifying children at risk of reading difficulty. Existing AI-based screeners are often limited in the scope of their analyses and evaluation metrics, or are proprietary systems that lack transparent model specifications and evaluation. We present KIRA, a dual-pathway screening system that pairs word-level fluency scoring with detailed phoneme-level error detection. We adapt pretrained word and phoneme recognizers to children's speech, reducing word error rate from 13.88% to 8.84% and phoneme error rate from 41.66% to 23.00%. Powered by these child-adapted models, we implement Word Reading (WRE) and Oral Reading Fluency (ORF), two foundational tasks in K-2 screening. The system integrates these recognizers with a web-based teacher-facing interface presenting fluency scores alongside phoneme feedback for potential targeted intervention. KIRA brings modern child-speech recognition into a full-stack, deployable, classroom-ready reading screener.

---


### 24. [When Do Gaussian Priors Fail? A Latent Geometry Investigation of RL Fine-Tuning](https://arxiv.org/abs/2610.28849)

**<font color=#1a73e8>作者：</font>** Wang Ru  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent diffusion models almost universally place a Gaussian prior on the VAE latent space. For base generation this default is unproblematic; under reinforcement-learning fine-tuning, however, it carries a structural limitation. The standard VAE's KL term does not merely ignore mode structure - it actively taxes separation and tightness. When data are multimodal, the ELBO optimum compresses distinct modes into an overlapping latent. RL fine-tuning amplifies this overlap: the score network is under-resolved on the saddle region between modes, dynamic-to-variational amplification rises sharply, and the collapse boundary beta_c is pushed far above its variational scale. On the real alanine-dipeptide Boltzmann distribution, a Gaussian-prior VAE collapses at beta_c = 0.224 while a mode-tracked Gaussian-mixture prior collapses at 0.00316, a 71x gap from the same pipeline.
We trace this gap to a single geometric mediator, d_min/(2 sigma_0), and verify the causal chain through controlled interventions: moving geometry at fixed prior, and switching prior at matched geometry (full mediation; prior-label coefficient 0.995x, 95% CI [0.79, 1.25]). A three-source decomposition localises the amplification to the learned policy (zero ODE-solver contribution, bounded anchor mismatch); the coverage plateau is an unconditional benefit of mode-separating priors that no amount of RL capacity recovers. The remedy is conditional: a non-Gaussian prior is necessary precisely when the latent geometry would fall into overlap and the task is coverage-sensitive. A machine-checked theory skeleton supports the KL pricing structure - a divergent compactness tax under a Gaussian prior versus a finite assignment fee under a mixture - and the position-versus-plateau distinction delimits what is finite-resource from what requires changing the prior.

---


### 25. [Depth-guided Geometric Adaptation for Few-shot Image Classification](https://arxiv.org/abs/2610.28856)

**<font color=#1a73e8>作者：</font>** Zhiqi Miao, Estefanía Talavera, Weichuan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot image classification (FSIC) frequently suffers from visual ambiguity, where background clutter and RGB appearance similarities hinder discriminative feature matching in data-scarce settings. To mitigate this, we propose DAFIC, a geometry-guided framework that incorporates monocular depth into representation learning, episodic adaptation, and dense support-query matching. DAFIC first learns geometry-aware token representations through RGB-D self-supervised pre-training. Subsequently, the Depth-guided Geometric Adaptation (DGA) module uses depth-derived geometry to refine patch representations with geometry-enriched class context while suppressing background interference. Spatial Bidirectional Patch Matching (SBiM) then performs bidirectional dense matching on the refined features, reducing sensitivity to spurious correspondences and background clutter. Extensive experiments on four benchmarks show that DAFIC achieves strong performance against existing methods, with ablation and robustness analyses supporting the effectiveness of coupling geometry-conditioned episodic adaptation with bidirectional matching for few-shot visual recognition.

---


### 26. [DualHeads: Reward-tilted few-step diffusion made simple](https://arxiv.org/abs/2610.28858)

**<font color=#1a73e8>作者：</font>** Yuanzhi Zhu, Eleftherios Tsonis, Simo Alami Chehboune 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distilled diffusion models generate high-quality images in a few sampling steps, but aligning them with task requirements and human preferences is difficult. Methods developed for multi-step diffusion models rely on differentiable rewards, or on score fields and stochastic trajectories that distilled generators may lack. We ask whether a few-step generator can be adapted using only external reward evaluations and reference samples, and show that two binary classifiers suffice. Our method, DualHeads, implements them as lightweight heads on a frozen diffusion backbone. The reward head learns which samples of the same prompt score higher, the reference head separates reference images from generated ones, and the generator maximizes a weighted sum of their logits. When the heads are optimal, this objective is KL-regularized maximization of the learned reward, and the ratio of head weights sets the regularization strength. Empirically, with both rule-based and model-based rewards, a few-step DualHeads generator reaches task rewards close to those of 40-step reinforcement learning methods while preserving image quality, at no extra inference cost. We hope that this simple and elegant dual-head formulation will help advance few-step reward-tilted generation.

---


### 27. [AI Security Literacy: Ecosystem-based Competency Framework and K-12 Learning Platform](https://arxiv.org/abs/2610.28859)

**<font color=#1a73e8>作者：</font>** Eric Yocam, Varghese Vaidyan, Paris Kalathas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Adoption of artificial intelligence in K-12 schools has outpaced guidance for students, teachers, and administrators. Existing AI-literacy frameworks emphasize understanding and use; cybersecurity frameworks predate AI-specific threats, and neither defines AI security literacy as a competency domain in its own right. We propose an AI Security Literacy (AISL) framework of six dimensions spanning the school ecosystem, ground its technical dimensions in public AI-safety benchmarks and a reproducible multi-seed adversarial evaluation, and ground its attitudinal dimensions in nationally representative survey micro-data from U.S. teachers and adults. Only 34.5% of teachers report a school AI policy, and teachers see their own AI use as easing their work but students' use as complicating it; on the technical side, a reported robustness figure depends as much on the attack and the particular trained model as on the system evaluated. NeuralFortify, a browser-based K-12 platform built on real AI models, is presented as an illustrative operationalization.

---


### 28. [A General Topological Symmetry Index for Critical Orbits In Neural Network Loss Landscapes](https://arxiv.org/abs/2610.28864)

**<font color=#1a73e8>作者：</font>** Jingzhou Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A systematic understanding of the global structure of neural-network loss landscapes remains challenging due to their high dimensionality. Symmetries arising from network architectures and learning objectives provide a way to investigate aspects of this structure. Although a growing number of studies have drawn attention to these symmetries, a systematic characterization of them, as well as of the critical orbits they give rise to, remains incomplete. To address this gap, in this work we establish a topological symmetry index, based on the methodologies from the family of equivariant degree theories, to decode these symmetries. The frameworks apply to arbitrary network architectures and include methods applicable to degenerate critical orbits. The index detects the isotropy of the critical points and quantifies the corresponding net topological contributions. Several examples, including softplus MLPs, Transformers, and equivariant neural networks, are presented to illustrate the computations.

---


### 29. [Actually, All Learnable Distribution Classes Are Privately Learnable](https://arxiv.org/abs/2610.28878)

**<font color=#1a73e8>作者：</font>** Mohammad Afzali, Hassan Ashtiani, Alex Bie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that every class of distributions that is learnable up to arbitrarily small target error in total variation distance with finitely many samples is also learnable under ($\varepsilon, \delta$)-differential privacy up to arbitrarily small target error with finitely many samples. This proves a conjecture of Ashtiani. Previous work by Bun, Kamath, Mouzakis, and Singhal [arXiv:2402.00267] gave a weak refutation of this conjecture, showing that this implication is not true when learnability is defined with respect to a fixed target error. In contrast, we show that, under the standard definition of learnability, the conjecture is true.

---


### 30. [Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures](https://arxiv.org/abs/2610.28887)

**<font color=#1a73e8>作者：</font>** Yujian Liu, Li An, Zelin He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autonomous agents can increasingly propose ideas, modify code, and run experiments, creating an opportunity to accelerate scientific discovery using teams of collaborative AI researchers. To escape local minima in the discovery, we propose to encourage orthogonal exploration by constructing the team using agents with varying expertise. However, realizing this design requires more than diverse backgrounds. When experiments are costly, a team can test only a limited number of ideas, thereby creating the need to balance exploration and exploitation when selecting a subset of researchers to propose and execute new experiments. Furthermore, each result should shape what the team tries next. We therefore ask how AI researchers with different scientific backgrounds can build on one another's findings and sustain progress under a limited experimental budget. To address these challenges, we build a team of persistent AI researchers, each grounded in a different discipline, who keep private research histories, share experimental evidence, and receive research opportunities through adaptive allocation. We demonstrate the effectiveness of this design by deploying the team to search for linear attention architectures, where it outperforms GDN2 at 1.3B scale on language modeling, common-sense reasoning, and synthetic and real-world retrieval tasks. In controlled comparisons, removing any single organizational component from our design yields markedly weaker discoveries: without disciplinary backgrounds, the search plateaus early; without private histories, researchers make less progress despite identical shared evidence; and uniform selection falls short of adaptive allocation within the same budget. These results suggest that sustained autonomous discovery depends not only on stronger agents, but also on who explores, what they remember, and how research effort is allocated.

---


### 31. [Policy-Mask: Budget-Aware Adaptation of Diffusion Features to Discriminative Tasks](https://arxiv.org/abs/2610.28889)

**<font color=#1a73e8>作者：</font>** Ivan Listopadov, Maksim Nakhodnov, Aibek Alanov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Selecting intermediate features from a frozen diffusion model for discriminative tasks is non-trivial because the useful signal is distributed across the denoising trajectory, network depth, and channels. In practice, this requires choosing a timestep, a block, and a channel subset. Existing methods either fix these choices by hand or optimize only a few extraction hyperparameters, most often the timestep, then reuse the same rule across inputs and budgets. We introduce Policy-Mask, a budget-conditioned policy trained on the downstream objective that jointly selects all three under a prescribed channel budget. Without normalization, the channel-score contribution grows with the number of selected channels and dominates the timestep and block updates. We normalize it by subset cardinality, keeping the three policy heads on comparable scales and stabilizing joint training. At matched budgets, Policy-Mask improves over fixed extraction and feature-filter baselines across segmentation, classification, and semantic correspondence, reaching 38.9 mIoU on ADE20K, 75.4% top-1 on CIFAR-100 at 128 dimensions, and 76.3 PCK@0.1 on SPair-71k. Component-wise ablations show that block selection materially affects downstream accuracy, and the highest recorded channel-budget score occurs at 256 retained channels, identifying a practical operating point for compact diffusion representations. We further adapt Policy-Mask to diffusion transformers, including PixArt-$\Sigma$ and SD3.5 MMDiT, by replacing U-Net channels with image-token hidden dimensions.

---


### 32. [Fig: Automated Multiagent Behavior Elicitor](https://arxiv.org/abs/2610.28891)

**<font color=#1a73e8>作者：</font>** Anrui Gu, Zhichao Wang, Nicolai Ouporov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many social evaluations for multiagent systems study behaviors as they emerge from environments instead of systematically intervening in the environment to elicit such behaviors. We introduce Fig (Finding Interactions in Games), an agentic system that performs targeted elicitation interventions on game environments. It takes a natural language behavior description, decomposes it into sub-behaviors, generates new social games or selects existing ones, and executes single or combined interventions to the games' engine, opponents, instructions, and context. To evaluate model behavior, it combines built-in mechanical checks and synthetic rubric judgments. We validate the interventions, generated games, and evaluation mechanisms via human review. Models attempt the target behavior in 45.2% of episodes on average for valid scenarios generated by Fig for six test behaviors -- cooperation, exploitation, deception, covert coordination, betrayal, and sabotage. For game-behavior pairs with available controls, Fig's interventions increase attempt rates by 10.9% on average compared to matched control games. Fig shows that multiagent environments can serve as programmable test beds for intentional, controllable, and reproducible behavior evaluation. Code is available at this https URL.

---


### 33. [Minimax-Optimal Predictive Flow Matching under Distribution Drift](https://arxiv.org/abs/2610.28898)

**<font color=#1a73e8>作者：</font>** Aadithya Srikanth, Vaneet Aggarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching learns a generative velocity field by regression, but under distribution drift a field must be deployed before the current data arrive. We study this predictive problem for a fixed, possibly nonconvex, neural class, with dynamic regret against the best represented field of each round. We propose DyProd-FM, which refits flow matching on dyadic historical prefixes and selects among the fits with a sleeping Prod master. Without knowing any drift budget, it attains regret $\widetilde{O}(\min\{N_\omega+1,1+\sqrt{T\Omega}\})$ in the relative velocity risk variation $\Omega$ and $\widetilde{O}(\min\{N_\mu+1,1+T^{1/3}V_\mu^{2/3}\})$ in the target-law variation $V_\mu=\sum_t W_2(\mu_{t+1},\mu_t)$, up to approximation and fitting costs. Matching lower bounds for fixed classes show that both rates are optimal in $T$ and in the budgets up to logarithmic factors. Prior optimal dynamic-regret guarantees rely on a convex decision set with strongly convex or exp-concave losses, whereas our class may be nonconvex and no curvature in its parameters is assumed. The target-law rate rests on a second-order link between the two variations, which the base noise of flow matching provides.

---


### 34. [Data-Driven Glyph Positioning for Handwritten Music Synthesis](https://arxiv.org/abs/2610.28899)

**<font color=#1a73e8>作者：</font>** Elona Shatri, Jiří Mayer, Jan Hajič jr  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesised data is a common strategy to address the lack of annotated handwritten music scores in Optical Music Recognition (OMR). Smashcima is a recent synthesis framework that assembles pages of handwritten scores by sampling glyph images from MUSCIMA++ and positioning them with hard-coded rules. In this work we ask whether these rules are grounded empirically and whether a learned model for context-dependent positioning can further improve synthesis quality. We extract inter-glyph distributions from around 285 thousand annotated relationships across MUSCIMA++ and OmniOMR, finding that several key parameters deviate systematically from real handwriting. Replacing these constants with empirical means reduces positioning RMSE by up to 60%. We then train a Graph Neural Network (GNN) on the Music Notation Graph structure to predict context-dependent offsets, achieving an additional 50 to 85% RMSE reduction on stems and beams by modelling how neighbouring glyphs constrain placement. Cross-dataset analysis shows that spacing differences between the two corpora are explained by note density (3.3), not style, and that duration-proportional spacing does not hold in handwriting (R2 = 0.001). In downstream evaluation, a YOLOv8 detector pretrained on GNN-positioned synthetic data achieves +30% mAP50 over the baseline and +11% over empirical means when fine-tuned on 200 real handwritten staves, showing that positioning accuracy matters for downstream OMR.

---


### 35. [JaxMARL-BC: Multi-Agent Reinforcement Learning for Macroeconomic Modelling, in Seconds](https://arxiv.org/abs/2610.28907)

**<font color=#1a73e8>作者：</font>** Daniele Montagnani, Andrea Coletta, Antonietta Mira 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent reinforcement learning (MARL) offers a principled way of populating simulated economies with many heterogeneous decision makers. Its adoption, pioneered in finance, has nonetheless been slow in macroeconomics because of two main limitations: the lack of a shared frame of reference connecting MARL systems to dynamic stochastic general equilibrium (DSGE) models the profession already trusts, and the very long training times. The first limitation was recently addressed by the Multi-Agent Reinforcement Learning Business Cycle (MARL-BC), which places deep RL households in a real business cycle economy and reduces to classic DSGE models in specific limits. Here we address the second limitation. We present JaxMARL-BC, a JAX-accelerated simulator that trains MARL-BC economies in seconds (between 75x and 724x faster than the reference implementation), and scales to 200,000 independent learning households. We verify its correctness against the known DSGE limits, characterise its scaling through a simple cost law, and demonstrate its value by a proof-of-concept calibration of an extended model with heterogeneous returns on capital, in a two-hour experiment that would previously have taken over a month. We release JaxMARL-BC as open source.

---


### 36. [Simply Logical -- The First Three Decades](https://arxiv.org/abs/2610.28912)

**<font color=#1a73e8>作者：</font>** Peter Flach, Kacper Sokol, Jan Wielemaker  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper charts the evolution of the Prolog textbook Simply Logical -- Intelligent Reasoning by Example from print with runnable programmes on a 3.5-inch diskette published in 1994, via various intermediate online versions, to the fully interactive online edition available today. Our aim is to investigate -- from both the writer's and the reader's perspectives -- the potential impact of technology on educational materials. The three authors of this paper present three distinct and complementary points of view, which come together to shape an interactive online book that offers an immersive learning experience. Peter describes the philosophy behind the original book and experiences teaching from it. Jan demonstrates how contemporary web programming has enabled a fully interactive realisation of the book's philosophy. Kacper reports how different technologies can be adopted to build a versatile authoring toolkit that underpins the interactive online edition of the book. Collating these distinct yet coherent perspectives allows us to reflect on future opportunities for interactive Prolog teaching materials arising from the continuous development of web technologies. The insights we offer should be of interest to teachers of Prolog as well as those wanting to find out about the latest educational technologies.

---


### 37. [A Model-Free Continuous-Time RL Algorithm from Discrete-Time Off-Policy Data with End-to-End Guarantees](https://arxiv.org/abs/2610.28915)

**<font color=#1a73e8>作者：</font>** Chaorui Yao, Yuming Paul Zhang, Lin Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we study continuous-time reinforcement learning, where the state follows an unknown stochastic differential equation but only a fixed off-policy batch of discrete-time transitions is available. Standard discrete-time Q-learning becomes problematic as the sampling interval shrinks, because differences between action values vanish. Continuous-time alternatives, such as Deep Advantage Updating and martingale q-learning, preserve the action signal but jointly learn a value function and an action-dependent critic. Building on the PhiBE-Q formulation (arXiv:2606.21925), we develop a model-free PhiBE policy iteration (PhiBE-PI) framework that uses a single state-action critic while preserving the continuous-time action-ranking scale. At each iteration, the framework learns the critic directly from sampled increments and uses it to improve the policy. The same batch is reused throughout, without explicitly estimating the drift or diffusion. We further develop an implementation under linear function approximation and establish a local end-to-end suboptimality guarantee for the learned policy. Our analysis quantifies how errors from time discretization, function approximation, and finite-sample policy evaluation propagate through policy iteration. It accounts for the dependence of successive policies on the reused data, so the guarantee does not require a fresh batch at each iteration. Moreover, we identify a bias-variance trade-off: smaller sampling intervals improve the approximation to the continuous-time problem but can increase statistical error at a fixed sample size. Thus, finer time discretization does not necessarily lead to better policy performance.

---


### 38. [Query Feedback and Teaching for Stable and Certifiable Language Generation](https://arxiv.org/abs/2610.28918)

**<font color=#1a73e8>作者：</font>** Farnam Mansouri, Alireza F. Pour, Grigoris Velegkas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language generation in the limit studies whether a learner observing an enumeration of an unknown target language can eventually generate only valid, previously unseen elements. We study stability, introduced by Kalavasis, Mehrotra, and Velegkas (2025), which requires the generator's infinite output set to eventually remain unchanged, and introduce the stronger notion of certifiability, which requires the generator to determine from its observations that its current output is valid. Drawing on teaching sets in learning theory, we introduce a hierarchy of teaching dimensions for generation under three increasingly strict success criteria: correctness, stability, and certifiability. These dimensions measure the minimum number of selected examples whose appearance guarantees the corresponding success condition. We also study stability and certifiability in the membership-query model of Charikar and Pabbaraju (2025). We characterize stable and certifiable generation, both with and without query feedback, and establish their relationships with uniform generation and identification in the limit. In particular, we give a finite-witness characterization of stable generation, analogous to Angluin's tell-tale characterization of identification, resolving a gap left open by Kalavasis, Mehrotra, and Velegkas (2025). We further compare these generation notions with identification in the limit and contrast their teaching requirements on well-studied language families, including regular and erasing pattern languages.

---


### 39. [The Data Differentiator Framework (DDF): Quantifying Marginal Data Value with Information-Theoretic and Game-Theoretic Measures in an Agentic Evaluation Pipeline (SDSAE)](https://arxiv.org/abs/2610.28933)

**<font color=#1a73e8>作者：</font>** Sukesh Kumar, Dilip Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In data-rich enterprises the hard question is not whether a candidate dataset is good in isolation, but whether it adds information beyond what the organization already holds, and whether that increment is worth its price. We present the Data Differentiator Framework (DDF), a composite scoring method for candidate data assets that combines (i) a mutual-information-based redundancy penalty against the existing portfolio, (ii) a cost-normalized, significance-gated marginal utility score derived from an ablation study, and (iii) explicit governance inputs (trust, identity resolution quality, strategic weights) set by the business. The framework is executed by a staged pipeline, the Strategic Data Sourcing Agent Ecosystem (SDSAE), that short-circuits expensive model-retraining steps for assets failing governance or redundancy gates. Conceptually, the DDF extends the relevance-minus-redundancy principle of mRMR feature selection from the feature level to the asset level, and adds cost normalization, a statistical significance gate, and governance terms that per-sample valuation methods such as Data Shapley do not model. We validate the framework on the public credit-card fraud benchmark (284,807 transactions) with five constructed candidate assets spanning the redundancy spectrum. Only the genuinely differentiated asset passes the significance gate ($\Delta$AUC = +0.0029, DeLong $p = 1.4\times 10^{-9}$, Holm-corrected $p = 7.2\times 10^{-9}$) and receives an acquire recommendation (DDS = +0.663); the fully redundant asset scores lowest (DDS = -0.135). The recommendation is stable across 19 of 22 admissible strategic-weight configurations and across all decision thresholds in [0.15, 0.66]. We state clearly which quantities in the case study are computed from data and which are simulated governance inputs, and we discuss the design limits of a single-dataset evaluation.

---


### 40. [MINER: Modeling Inter- and Intra-Person Variance for Reidentification](https://arxiv.org/abs/2610.28941)

**<font color=#1a73e8>作者：</font>** Oron Nir, Eliyahu Strugo, Ariel Shamir  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clothes-Changing Person Re-Identification (CC-ReID) remains challenging due to drastic appearance shifts across outfits. Most prior works devise biometric signal-extraction heuristics to enhance inter-person variance, e.g., using segmentation masks, while leaving intra-person variance uncontrolled. We present MINER, a simple model-agnostic framework that suppresses garment bias by contrasting hard examples and adaptively balancing dataset-dependent intra- and inter-person variance. Extensive experiments show that MINER improves retrieval across CC-ReID benchmarks, achieving state-of-the-art performance on four datasets and ranking among the leaders in all three tracks of the open TVRID RGB-Depth ReID challenge.

---


### 41. [Multi-Objective Protein Optimization via Modular Diffusion Steering](https://arxiv.org/abs/2610.28943)

**<font color=#1a73e8>作者：</font>** Meir Roketlishvili, Felix Huber, Wenda Chu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein engineering often requires improving several properties simultaneously, motivating the search for high-performing sequences that represent useful fitness tradeoffs. Discovering these sequences is challenging because the design space is combinatorially large and experimental campaigns often permit only a few rounds of batched measurements. We introduce \textit{MODS}, a modular framework for multi-objective protein optimization via inference-time diffusion steering. For each proposal, MODS samples augmented Chebyshev scalarization weights and a fitness-surrogate ensemble member to define a scalar steering reward. Varying the weights directs generation toward different objective tradeoffs, while varying ensemble members diversifies the predictions used for guidance. Because MODS expresses multi-objective acquisition through scalar rewards, it can be paired with different diffusion models and compatible steering procedures. After each evaluation batch, MODS updates the surrogates without retraining the generative model. We evaluate MODS on six protein optimization tasks using predictive oracles trained on experimental assay data, with two diffusion models and two steering procedures. MODS achieves competitive final hypervolume across all six tasks with both diffusion models, and substantially outperforms the best evaluated baseline on several tasks. Our results demonstrate a flexible and effective approach to multi-objective protein optimization with limited feedback.

---


### 42. [Guilt by Association: Semantic Leakage Drives Associative Gender Bias](https://arxiv.org/abs/2610.28944)

**<font color=#1a73e8>作者：</font>** Hazel Chen, Peter West, Hila Gonen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic leakage occurs when a concept in the prompt steers model generation about an entity, even though the concept is irrelevant to it (e.g., a person who likes yellow is said to work as a school bus driver). It has mostly been studied in settings where the concept is directly attributed to the entity the model is asked about. This leaves open whether leakage is a flawed heuristic, where the model builds a profile of that entity, or a much broader associative tendency, e.g., working across seemingly unrelated entities. We argue for the latter: even after removing the attribution of the concept to the specific entity, leakage persists. Next, we extend this idea to gender bias. While work on gender bias in LMs typically looks at cases where the stereotyped concept is attributed to an entity, our findings suggest that a concept may steer outputs with its mere presence in the scene. We show this using gendered concepts under two conditions: when the subject engages with the concept, and when the concept just sits in the scene. We find that both shift model generation toward the stereotype to a similar extent. Together, our results suggest that semantic leakage drives a form of bias that is overlooked by current evaluations.

---


### 43. [Online Open-World Wafer Defect Discovery using Hyperdimensional Computing](https://arxiv.org/abs/2610.28949)

**<font color=#1a73e8>作者：</font>** Quanling Zhao, Ava Emami, Tsuyoshi Idé 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional wafer defect analysis relies on offline, closed-world classifiers that fail to detect novel, unseen defect signatures emerging during continuous semiconductor manufacturing. To address this, we propose WaferHDC, an online open-world wafer defect discovery framework based on hyperdimensional computing (HDC). The memory-centric architecture of WaferHDC enables rapid anomaly detection and grouping of recurring failures into compact hypervector representations. This allows the memory space to dynamically scale with new defect modes without retraining a static classifier or archiving entire raw wafer history. WaferHDC first models normal spatial distributions, then dynamically groups recurring failures into persistent defect memory without labels or predefined class counts. It outperforms the strongest online baseline by 13.3 p.p. in adjusted Rand index and 10.5 p.p. in normalized mutual information on the industry-standard WM-811K dataset. These results demonstrate the effectiveness of WaferHDC for continuous and open-world wafer defect analysis.

---


### 44. [Pair-Free Coarse-to-Real Video Generation via Real-to-Coarse Image Supervision](https://arxiv.org/abs/2610.28954)

**<font color=#1a73e8>作者：</font>** Gonzalo Gómez-Nogales, Daohan Lu, Peiye Zhuang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coarse-to-real (C2R) video generation converts coarse animation, simulation, or game-rendered videos into photorealistic videos while preserving scene layout, camera motion, and dynamics. Training such models requires aligned (coarse, realistic) video pairs, which are expensive to create and confine prior systems to narrow synthetic domains. We exploit a simple asymmetry: paired videos are hard to obtain, but paired real-to-coarse images are easy to construct with existing editing and 3D reconstruction tools. Using these image pairs, we train the DINO-R2C model to transfer realistic images to coarse images in DINO feature space, and apply it frame-wise to ordinary real videos to synthesize pseudo-coarse videos. The C2R# model then learns to generate each real video from its pseudo-coarse counterpart, free from needing (coarse, realistic) video pairs. At inference, the DINO-R2C model is discarded and actual coarse videos drive the C2R# model directly. Thus, our pair-free training scales with any real-video corpora rather than with paired synthetic videos. We will release the model and project webpage at this https URL.

---


### 45. [Transformers as Generic Deep Neural Networks: Exact Compilation, the Cost of Removing Activation-Activation Products, and Multi-Agent Attention Clustering](https://arxiv.org/abs/2610.28958)

**<font color=#1a73e8>作者：</font>** Sergey Salishev, Zeev Volkovich, Oleg Granichin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers are deployed as a special model class. Neural processing units (NPU) add dedicated operators for attention and normalization, and quantization relies on Transformer-specific algorithms. We show the computation does not force this. Every Transformer block, with attention, LayerNorm and a GELU MLP, compiles exactly into a generic deep neural network built from fixed affine maps, routing and the square, sigmoid and inverse square root, plus GELU or its sigmoid approximation. Without activation-activation products, every transform-wise compilation adds at least $N^2$ scalar nonlinear evaluations per head for dense scores. Keeping that one operation type removes this cost; its elementwise form, present on every surveyed NPU, suffices with the sigmoid and inverse square root. For top-$k$ attention with exchangeable tail scores, we prove that exact or conditional-mean tail mass gives an unbiased, minimum-mean-square-error estimate of the attention distribution, while tail drop is conditionally biased. When queries or agents cluster, centroids choose the keys first, reducing the number of computed scores from $N^2$ to $Nk$ per head. On DeiT-Tiny, MambaIRv2-Light and Pythia-70M the compiled models match their references with all keys, standard post-training quantization applies, and the exact tail-mass estimate beats tail dropping with half as many keys on DeiT-Tiny and, for $k\le8$, on Pythia-70M.

---


### 46. [RoPT: Robust 6DoF Object Pose Tracking in Video](https://arxiv.org/abs/2610.28962)

**<font color=#1a73e8>作者：</font>** Yongqing Liang, Yuzhong Chen, Sihang Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 6-DoF object pose tracking is essential for robotic interaction, yet conventional monocular pipelines frequently suffer from catastrophic divergence under rapid object motion. We present RoPT, a robust tracking framework engineered to overcome this limitation by unifying visual perception, temporal kinematics, and global re-localization into a tightly coupled closed loop. Unlike existing open-loop trackers, RoPT delivers three critical capabilities that fundamentally alter system resilience. First, the visual perception component tracks object masks to robustly handle partial and severe occlusions. Second, a kinematic factor graph regularizes frame-to-frame updates, forecasts forward pose predictions, and drives a parallel multi-hypothesis verification scheme to bypass local minima. Finally, an active re-localization module transforms the pipeline into a closed-loop system, making it failure-aware and capable of deterministic self-recovery. We demonstrate the effectiveness of our framework across challenging benchmarks alongside real-world robotic demonstrations, achieving significantly higher tracking survivability under rapid motion.

---


### 47. [Unit-Aware Differentially Private Quantum Machine Learning for Clinical and Wearable Health Data](https://arxiv.org/abs/2610.28968)

**<font color=#1a73e8>作者：</font>** Md Khalid Syfullah, Alvi Ataur Khalil  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical registries and wearable sensors support early health-risk assessment, yet models trained on these records may leak sensitive information when released. Differential privacy (DP) bounds this leakage by injecting noise whose total magnitude grows with the number of trainable parameters, a cost especially severe for small health cohorts. This motivates parameter efficient models including quantum machine learning (QML), whose variational circuits can represent complex decision boundaries with few trainable parameters. It raises a question: at matched input dimensionality and privacy budget, does a quantum model retain more utility than a classical one? We investigate this question on three clinical cohorts and one wearable cohort, treating each clinical record or participant as a privacy unit. We compare capacity-matched quantum, multilayer perceptron, and logistic regression models across five privacy budgets and five seeds. The quantum model leads on three clinical cohorts by up to 0.104 ROC AUC averaged across budgets; however, trails on the wearable cohort, where the small number of participants requires substantial noise. No difference survives Holm correction across 24 tests, so these results indicate a trend rather than a quantum advantage. An analytic gradient bound shows that lower clipping thresholds can improve utility by reducing noise despite clipping bias. Finally, an experiment on IBM quantum computer (ibm_fez, a 156-qubit superconducting processor) using eight fixed test cases yields mean absolute probability errors of 0.046 (private) and 0.063 (non-private) relative to simulation, supporting the feasibility of inference on noisy intermediate-scale quantum (NISQ) hardware. Code is publicly available at this https URL.

---


### 48. [TEMPL: A Resource-Efficient and Transparent Model-Free Framework for Pseudo-Label Generation in Material CT Scans](https://arxiv.org/abs/2610.28974)

**<font color=#1a73e8>作者：</font>** Ashiqur Rahman, Venkata Devesh Reddy Seethi, Austin Yunker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The scarcity of large annotated datasets limits deep learning (DL) segmentation in material CT analysis. DL-based pseudo-labeling can help, but it is often computationally expensive and hard to interpret. We introduce a multi-stage, model-free framework that generates pseudo-labels directly from grayscale CT scans. It combines thresholding, morphological dilation, and a custom breadth-first search region-growing algorithm to produce polygonal annotations without pre-trained weights, labeled data, or a GPU. We compare it against the zero-shot Segment Anything Model (SAM), a fully supervised 3D U-Net, and classical baselines. On a dendrite dataset with ground truth, our method reaches 63.19% IoU versus 10.74% for zero-shot SAM, with four times the instance recall at 0.5 IoU (33.3% versus 8.3%). The supervised 3D U-Net serves as a reference ceiling that requires expert labels. On a silica sand specimen, YOLO models trained on our labels performed comparably to models trained on SAM labels in a qualitative comparison. Across 1,053 extracted grains, the median equivalent diameter was 163.8 micrometers, near the specimen's known 106 to 150 micrometers sieve range, compared with 219.5 micrometers for SAM, whose labels merge adjacent particles and add spurious detections. A sensitivity analysis shows a stable operating range for the key threshold and a sharp, predictable failure point linked to phase contrast. Our method needs 15s per image on a standard CPU versus 28s for SAM on a GPU. These results support our transparent approach as a tool for annotation bootstrapping and microstructural quantification in resource-limited settings.

---


### 49. [MedBOE: Optimization-Based Estimation of Complete Patient Body Models from Whole-Body Medical Imaging](https://arxiv.org/abs/2610.28985)

**<font color=#1a73e8>作者：</font>** Hoijoon Jung, Yuhao Wei, Mingxiao Tu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> True whole-body medical imaging captures a patient from head to toe and provides comprehensive anatomical and/or functional information. This coverage enables reconstruction of the external body surface, yielding patient body models. However, scanner geometry (e.g., bore diameter), patient characteristics, and positioning can leave body regions missing (e.g., lateral arms/torso, hands, forearms, elbows), producing incomplete patient body models. Such incompleteness limits downstream medical analyses, including derivation of body-habitus metrics (BHMs), such as body volume and surface area, for injected radiotracer activity regimens, cardiometabolic risk assessment, and computational anatomical modeling for medical imaging simulation and radiation dosimetry. We present the Medical Body model Optimization-based Estimator (MedBOE), an automated, training-free framework for estimating complete patient body models from whole-body images with missing body regions. Our innovation is to leverage the Skinned Multi-Person Linear (SMPL) template, a parametric body mesh representing a broad range of body shapes and poses, in medical imaging. MedBOE aligns the SMPL template to the incomplete patient body models via attribute-guided optimization and estimates missing body regions through geometrically and volumetrically constrained deformation. We evaluated MedBOE using two public datasets: AutoPET (91 whole-body PET-CT images) and Human Implicit Tissues (HIT; 40 whole-body segmentations from MRI images). MedBOE achieved the best overall volumetric and geometric performance among evaluated methods. BHMs derived from MedBOE were within 2% error, suggesting low percentage errors for downstream analyses. MedBOE offers an automated, training-free method for estimating complete patient body models from whole-body images with missing body regions.

---


### 50. [AgentPolicyForge: From Executable Environments to Policy Benchmarks and Adaptive Guards](https://arxiv.org/abs/2610.28989)

**<font color=#1a73e8>作者：</font>** Chao Shang, Wanyu Du, Yi Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Customized agent deployments define policies over tools, resources, and execution conditions. Providing these policies in the task agent's prompt does not reliably prevent violations. Training a guard requires examples of tool calls that comply with or violate those policies. We introduce AgentPolicyForge, a framework that uses executable environments to construct policy benchmarks and iteratively train policy guards. With this framework, we construct PolicyGym, a dataset across ten policy families using 698 scenarios for training data generation and 254 separate held-out scenarios for human-reviewed test sets. Tool calls are executed and their outcomes recorded to help determine whether they comply with the policy. Every violating case uses a permitted tool, requiring checks of arguments, resources, and context rather than tool identity alone. The case construction process supports iterative guard training: an attacker generates requests using retrieved strategies, and the guard is fine-tuned on balanced, environment-verified examples. Training improves policy enforcement even with a fixed archive. Updating the archive further reduces in-domain attack success compared with keeping it fixed. We compare policy-aware task agent self-regulation with a trained policy guard. On PolicyGym, the final guard-based configuration achieves a 40-44% relative reduction in attack success rate and fewer benign rejections than policy prompting alone.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-232](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
