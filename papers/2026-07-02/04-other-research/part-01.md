# 📦 其他研究 | 2026年07月02日

> 本类共 **274** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-274](./part-06.md)

---

### 1. [Cross-Modal Hierarchical Fusion for from Multi-Sensor Ground Observation](https://arxiv.org/abs/2606.30647)

**<font color=#1a73e8>作者：</font>** Xinze Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense volumetric reconstruction of cloud microphysical fields from sparse ground-based instruments remains an open problem, largely because the available measurements are heterogeneous in both modality and spatial coverage. We present AtmoFuseNet, a framework that fuses multi-view sky camera imagery with millimeter-wave cloud radar and ceilometer observations to produce 4D (three spatial dimensions plus time) estimates of cloud state and wind. The method operates in three stages: a cross-modal hierarchical aggregation module that combines image feature pyramids with instrument-derived vertical profiles through layer-wise cross-attention; a conditional variational refinement module that maps the resulting volume to physically consistent microphysical fields under differentiable radar and image forward models; and a correlation-based motion estimator that recovers per-voxel 3D wind vectors from consecutive volumetric reconstructions. On collocated observations from a semi-arid site, AtmoFuseNet reaches 0.026 g m^-3 liquid water content MAE and 1.18 m s^-1 wind speed MAE, improving over existing retrieval baselines. Ablation experiments isolate the contribution of each module.

---


### 2. [Joint discovery of governing partial differential equations from multi-source datasets by competitive optimization](https://arxiv.org/abs/2606.30699)

**<font color=#1a73e8>作者：</font>** Hao Xu, Siyu Lou, Yuntian Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discovering governing equations directly from observational data is a key step towards interpretable scientific machine learning. Current data-driven approaches typically operate on a single dataset, inherently limiting their performance when faced with restricted observations. In practice, multiple datasets are often available for the same physical system, distinguished only by distinct initial conditions or boundary configurations. Here, we present a competitive optimization framework designed to discover shared partial differential equations (PDEs) from multi-source datasets, termed MCO-PDE. The framework first trains independent neural surrogates for each data source, and then employs a soft-competitive weighting mechanism to dynamically assess dataset credibility and aggregate a consensus global coefficient. Integrated with a genetic algorithm for structural search, this approach simultaneously identifies the functional forms and parameters of the governing laws. We demonstrate that fusing as few as 50 observations per dataset across seven cases recovers canonical equations with high accuracy. The framework inherently handles two- and three-dimensional domains characterized by irregular boundaries and heterogeneous coefficients, and successfully extracts physically meaningful laws from real-world wave-tank experiments. Overall, this work establishes a promising route for automated scientific discovery via heterogeneous data fusion.

---


### 3. [An AI-Based Solution for Secure Service Provisioning in IoT](https://arxiv.org/abs/2606.30701)

**<font color=#1a73e8>作者：</font>** Marco Arazzi, Mert Cihangiroglu, Serena Nicolazzo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As the Internet of Things (IoT) continues its rapid expansion, the attack surface grows accordingly, with emerging threats targeting smart objects and their interactions. In this evolving landscape, securing service provisioning is crucial to ensure the proper functioning, security, and reliability of the IoT ecosystem. Service provisioning encompasses key tasks such as device registration, configuration, authentication, authorization, and software deployment, all of which are essential for seamless and secure IoT operations. In this paper, we present a comprehensive framework designed to select the most suitable smart objects to deliver a target service within a given IoT environment while also monitoring the behavior of the entities involved during the service provisioning phase. To achieve this, we employ a Deep Reinforcement Learning (DRL) approach in which an intelligent agent learns, through interaction with a complex, dynamic environment, how to adapt to changes while adhering to predefined security constraints. For behavioral monitoring, we leverage Federated Learning (FL) to develop a global Behavioral Fingerprinting (BF) model that is fully distributed and can analyze how IoT devices interact within the network. In addition, the BF is used to compute a reliability score for each service provider, reflecting its degree of compliance with the defined security constraints. This score is then incorporated into the service provisioning process, allowing smart objects to select providers not only according to functional suitability but also to their reliability level. Finally, we conduct an extensive experimental evaluation to assess the robustness and scalability of our approach. The results demonstrate that our solution can be effectively deployed even on resource-constrained IoT devices, making it a viable and scalable security-enhancing mechanism for modern IoT ecosystems.

---


### 4. [Accelerometry-Derived Digital Biomarkers for Cardiometabolic Risk: A Population-Representative Tabular Benchmark with Uncertainty Quantification](https://arxiv.org/abs/2606.30702)

**<font color=#1a73e8>作者：</font>** Federico Felizzi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structured tabular data dominates clinical medicine, yet existing benchmarks fail to reflect real-world properties like complex survey sampling, demographic oversampling, and subgroup fairness. We introduce the NHANES Accelerometry Cardiometabolic Benchmark, derived from NHANES 2003-2006, comprising 1,381 adults with hip-worn accelerometry, fasting laboratory biomarkers, dietary intake, and anthropometrics. We evaluate three tabular learning methods -- ridge regression, XGBoost, and the foundation model TabPFN v2 -- to predict glycated haemoglobin (HbA1c), fasting triglycerides, and C-reactive protein (CRP) from activity phenotypes and lifestyle covariates. TabPFN v2 achieves the best overall performance (HbA1c R^2=0.156, CRP R^2=0.383), while triglycerides remain largely unpredictable (R^2 < 0.05), consistent with known genetic dominance. We apply split conformal prediction to generate distribution-free 90% prediction intervals and evaluate demographic coverage equity across sex and race/ethnicity subgroups. Marginal coverage aligns with the 90% target for CRP and HbA1c but falls below for triglycerides. At the subgroup level, we observe localized undercoverage (e.g., HbA1c for Mexican American participants), illustrating the gap between marginal guarantees and the conditional coverage required for clinical fairness. Code and data are at this https URL.

---


### 5. [Why Do Few-Step Text Latents Fail When Image Latents Work? Non-Commitment at Sharp Categorical Readouts](https://arxiv.org/abs/2606.30705)

**<font color=#1a73e8>作者：</font>** Zhongyao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deterministic few-step generation succeeds on continuous image latents but collapses to incoherent text on continuous text latents, and we show the cause is geometric rather than a training or scaling deficiency: a smooth, regularity-limited deterministic map cannot resolve a discrete branch choice before a sharp categorical readout, so few-step failure is governed by decoder sharpness, not transport accuracy. In the overlapping regime of real text autoencoders, we prove (Theorem 3) that the posterior-mean terminal step flips tokens at the rate of the latent mass in an $O(s(t))$ tube around decision boundaries. Two diagnostics, DABI (readout sharpness) and CCI (categorical commitment), measured on published checkpoints show that four independently built continuous-text decoders amplify a boundary-aligned perturbation far beyond a norm-matched isotropic one (DABI from $5\times10^{2}$ to $>10^{5}$), while image decoders have DABI $\approx 1$. Two mechanisms escape the continuous bound: categorical commitment (autoregressive decoders succeed despite sharper readouts) and stochastic re-injection (deterministic ODE at $K=4$ gives PPL 294 versus SDE 50 on the same model). In the idealized separated regime we prove matching sharp transport laws, including a dimension phase diagram: the deterministic stiffness needed to separate $M$ modes grows as $\Theta(\sqrt{\log M})$ once the latent dimension is $\Omega(\log M)$ (and as $M^{1/n}$ in fixed dimension), with a depth-$B$ hierarchy giving a $\sqrt{B}$-smaller per-step peak (Theorems 5-7); a coarea identity links these to the overlapping tube (Theorem 17). The result is an accuracy-depth-stiffness tradeoff: within the deterministic-continuous class the cost is irreducible, and both escapes step outside it.

---


### 6. [Hierarchical Global Attention (HGA)](https://arxiv.org/abs/2606.30709)

**<font color=#1a73e8>作者：</font>** Woernle Frank, Fedosov Vladimir, Grinenko Artemiy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hierarchical Global Attention (HGA) is a drop-in replacement for dense causal attention in pretrained long-context transformers. HGA preserves the original checkpoint parameters: the pretrained $W_Q$, $W_K$, $W_V$, and $W_O$ projections remain unchanged, no calibration parameters are introduced, and no retraining is required.
Applied to Qwen3-30B-A3B-Instruct-2507-FP8 on a single RTX~5090 (32GB), the patched model runs out of the box at a 64K-token context, where token-level K/V storage is not feasible on this hardware.
Unlike previous sparse-attention methods, HGA performs hierarchical two-level routing. It first retrieves relevant chunks using compact RoPE-aware summaries and then refines the selection by routing only the most relevant groups before performing exact token-level attention. This hierarchical retrieval significantly reduces the number of fetched tokens while preserving exact attention over the retrieved token set, making RAM- and NVMe-backed storage practical.
The full historical token K/V resides in host RAM or NVMe storage, while only a small routed working set is transferred to GPU memory during attention. Consequently, GPU memory consumption depends primarily on model weights and the routed working set rather than on the total context length.
Across all tested context lengths (4K - 64K tokens), routed attention remains within approximately $0.01$--$0.02$ nats of dense attention while the sparsity used is just about 3%. These results suggest that the approximation introduced by hierarchical routing is small, and that the remaining quality gap is likely dominated by long-context positional encoding rather than by the routing algorithm itself.

---


### 7. [Streaming Gaussian Encoding for 4D Panoptic Occupancy Tracking](https://arxiv.org/abs/2606.30754)

**<font color=#1a73e8>作者：</font>** Maximilian Luz, Thomas Nürnberg, Yakov Miron 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-based 4D panoptic occupancy tracking (4D-POT) is a promising paradigm for holistic scene understanding from multi-view imagery, enabling joint reasoning about geometry, semantics, and object identities across time. Recent mask-based pipelines achieve strong performance by propagating instance queries across frames. However, their underlying volumetric representations are typically recomputed at each timestep, limiting geometric temporal consistency, particularly under occlusion and for static scene elements. To address this limitation, we propose a streaming Gaussian encoder that maintains a persistent volumetric scene representation for 4D-POT. Our method models the scene as a fixed-size set of latent Gaussian queries that are propagated via ego-motion compensation and refreshed under a confidence-guided budget constraint. Crucially, we shape Gaussian opacities through depth-based supervision to serve as proxy for visibility, enabling confidence to accumulate as a temporally aggregated measure of persistent scene support. Together with a warmup-based multi-frame training strategy, this yields representation-level temporal coherence beyond decoder-only tracking. Extensive experiments on Occ3D-extended nuScenes and Waymo establish a new state-of-the-art for camera-based 4D-POT, improving tracking consistency with negligible computational overhead while remaining fully compatible with existing mask-based pipelines. We provide code and models at this https URL.

---


### 8. [What Drives Interactive Improvement from Feedback?](https://arxiv.org/abs/2606.30774)

**<font color=#1a73e8>作者：</font>** Bartłomiej Cupiał, Jan Łojek, Mikołaj Garstecki 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study when natural-language feedback produces improvement beyond the gains obtainable from repeated attempts alone. In multi-turn language agent setting, higher final accuracy can reflect useful feedback, but it can also arise from resampling, format correction, or additional test-time computation. To separate these effects, we introduce a controlled student-teacher protocol across Omni-MATH, Codeforces, BBEH Linguini, and ARC-AGI1, evaluating thirteen open-weight models in both student and teacher roles. We compare external feedback, self-feedback, and unguided self-refinement, while varying interaction history, task difficulty, and teacher access to privileged task information. Across settings, we find that multi-turn improvement is often not evidence of feedback use: self-generated feedback adds little beyond unguided self-refinement, whereas the strongest external teachers produce substantially larger feedback-specific gains, suggesting that useful feedback must provide guidance beyond generic retry. Dense student-teacher interaction matrices further show that interactive gains are driven more by the student's ability to use feedback than by the teacher's identity, although teacher choice remains important for a fixed student. These results suggest that feedback-based agents should be evaluated against repeated-attempt baselines, and that ability to act on feedback, not merely feedback availability, is a central bottleneck for interactive improvement. We release our controlled student-teacher evaluation framework at this https URL.

---


### 9. [A Single Rewrite Suffices: Empirical Lessons from Production Skill Description Optimization](https://arxiv.org/abs/2606.30775)

**<font color=#1a73e8>作者：</font>** Yangqiaoyu Zhou, Mohammad Alqudah, Kwei-Herng Lai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprise AI agents route user queries to specialized skills by matching queries against natural language skill descriptions. When two skills share overlapping descriptions, the routing LLM misroutes queries, a failure we term skill collision. As agents scale to dozens of skills, manually tuning descriptions to maintain routing accuracy becomes a significant engineering bottleneck. We deploy an automated description optimization pipeline on a production enterprise group chat agent (9 skills, 372 regression cases). The pipeline produces descriptions averaging 79.2% F1, matching manually tuned descriptions at 79.4% F1 (average per-skill difference -0.20%, within the 0.78% multi-seed noise floor), while reducing per-skill engineering effort from 120 minutes to 3.8 minutes (32 times speedup). We then examine which pipeline components actually drive this match. Systematic ablation on both the production system and ToolBench (16k tools) reveals that a single LLM rewrite using any available false-positive and false-negative cases captures most of the available improvement. Other design choices we tested (iteration budget, feedback signal composition, dual editing of confused pairs, and training set size) each affect final F1 by less than 0.5%. Description optimization addresses skill collisions caused by overlapping descriptions but cannot resolve cases where two skills intended scopes genuinely overlap. We identify a diagnostic (a large train-validation F1 gap) that flags the latter cases for architectural rather than text-level intervention.

---


### 10. [Unveiling Transferability in Trajectory Prediction via Latent Scene Embeddings](https://arxiv.org/abs/2606.30777)

**<font color=#1a73e8>作者：</font>** Theodor Westny, David Axelsson, Björn Olofsson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The growing availability of trajectory datasets has fueled major advances in data-driven motion prediction. Yet, models trained on one dataset often fail to generalize beyond their training domain as a result of differences in scene layouts, agent behaviors, and sensing conditions. A framework that learns latent representations of datasets and quantifies their similarity using distributional metrics is presented. This large-scale study covers 24 major datasets, including the most widely used motion-prediction benchmarks, and shows that the resulting transferability scores strongly correlate with cross-dataset model performance. The results provide practical guidance for dataset selection, pretraining, and large-scale foundation models for motion prediction, paving the way toward more generalizable and robust predictive systems.

---


### 11. [ReactionAtlas: Ab origine exploration of chemical reaction networks with machine learning](https://arxiv.org/abs/2606.30778)

**<font color=#1a73e8>作者：</font>** Stefan Gugler, Max Eissler, Khaled Kahouli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mapping a chemical reaction network, the graph of minima and transition states (TS) and the elementary reactions connecting them, is the natural language of chemistry, from catalysis to combustion to the origin of life. Constructing such a reaction network for a given chemistry has been impractical: it requires finding and characterizing tens of thousands of TS, a task for which traditional methods such as density functional theory (DFT) are typically prohibitively slow and require reactant and product as input. We introduce ReactionAtlas, which builds a reaction network $\textit{ab origine}$ from a handful of seed molecules and without hand-crafted rules. Specifically, our machine-learned generative model proposes reactions from kinetically sampled candidate compounds and a DFT-trained machine learned force field (MLFF) filters them to valid TS, the resulting products of which enter the search as new seeds. Starting from eight pre-biotic seeds (CH$_2$O, H$_2$O, OH$^-$, H$_3$O$^+$, CO$_2$, H$_2$CO$_3$, HCO$_3^-$, H), ReactionAtlas discovers $\sim$47,000 reactions among $\sim$12,000 compounds. The MLFF TSs match the PBE0 references within 0.5 Å RMSD in 85% of the cases and can be easily brought to the PBE0 level. Thus, ReactionAtlas maps small carbohydrate chemistry up to C$_4$H$_8$O$_4$ at unprecedented scale and accuracy, including charge and stereo information. It enables novel insights into many well-studied reaction paths, including the formose cycle, which we highlight for its centrality to the chemical origins of life. Notably, our framework also allows establishing alternative reaction pathways for formose chemistry.

---


### 12. [Security--Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense](https://arxiv.org/abs/2606.30783)

**<font color=#1a73e8>作者：</font>** Mitchell Hermon, Rahul Gupta, Weitong Ruan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We identify a security-fidelity tradeoff in defending LLMs against indirect prompt injection: defenses resist injected instructions largely by suppressing untrusted text, which corrupts tasks that must preserve it, such as translation and document editing. Attack-success metrics cannot see this, because a model that ignores an injection and one that faithfully processes it as data score identically. We introduce SecFid, a benchmark built so that executing an injection, processing it as data, and ignoring it produce distinguishable outputs. This makes fidelity measurable and exposes a frontier: across 1,168 examples and 48 configurations, no model or defense achieves both objectives. The highest-fidelity model reaches 96.5% fidelity at 47.8% security, while the most secure defenses invert this, at 99.3% security but only 71.0%-73.9% fidelity. Even defenses with identical security differ in how they earn it: some repair hijacks into faithful processing, others simply suppress benign content. A decision-theoretic analysis shows why no fixed choice can be right everywhere: the correct behavior is not a property of the defense but of the deployment, set by its relative cost of a hijack versus a dropped span. Security alone therefore measures only half of robustness, and reporting it without fidelity hides the price at which it was bought.

---


### 13. [Revocable Learned State via Process Sidecars](https://arxiv.org/abs/2606.30788)

**<font color=#1a73e8>作者：</font>** John Sweeney  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are often adapted in stages: a public skill phase, a private memory phase, and a later safety phase that learns to refuse outputs tied to the remembered entities. Revoking the memory after the safety phase is not the same problem as subtracting the memory update: the later safety optimizer has transported the memory direction. We introduce process sidecars, a two-coefficient edit family $\hat{\theta}(\lambda,\gamma)=\theta_{\mathrm{AMS}}-\lambda\Delta_{\mathrm{M}}-\gamma\hat{R}_{\mathrm{S}\leftarrow\mathrm{M}}$, with $\hat{R}_{\mathrm{S}\leftarrow\mathrm{M}}=\hat{J}_{\mathrm{S},\varepsilon}(\Delta_{\mathrm{M}})-\Delta_{\mathrm{M}}$, where $\hat{J}_{\mathrm{S},\varepsilon}$ is a centered secant through the realized future AdamW safety-training process. The implementation uses $\varepsilon=1$ at the natural memory-edit scale; it reuses $\theta_{\mathrm{AMS}}$ as the positive endpoint and computes one additional safety trace at $\theta_{\mathrm{A}}-\Delta_{\mathrm{M}}$. We prove two things. First, the exact sidecar, using the true transported direction $R_{\mathrm{S}\leftarrow\mathrm{M}}$ rather than the secant estimate, at $(\lambda,\gamma)=(1,1)$ recovers the counterfactual safety-only oracle $\theta_{\mathrm{AS}}$ up to second order; the proof treats AdamW as an augmented-state map over parameters, first moments, and second moments. Second, this process information is necessary: whenever future safety training bends the memory direction, every scalar task-arithmetic edit leaves first-order counterfactual error, while the process-sidecar edit is second-order accurate. Across three models, the validation-selected 2D edit improves held-out refusal closure over naive task arithmetic in all trials, and over the $\gamma=\lambda$ process-JVP subfamily, the diagonal slice of the cached 2D grid, in all paired trials.

---


### 14. [Predictable GRPO: A Closed-Form Model of Training Dynamics](https://arxiv.org/abs/2606.30789)

**<font color=#1a73e8>作者：</font>** Rajat Ghosh, Datta Nimmaturi, Aryan Singhal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) has become a standard tool for improving the reasoning ability of large language models, yet its training dynamics are still described empirically: reward trajectories are fit with low-parameter functional forms whose constants carry no mechanistic meaning, and hyperparameter choices remain a matter of trial and error.  We develop a first-principles reduced-order model of these dynamics. The reduction has three consequences. First, it subsumes the empirical single-exponential saturation law as its overdamped limit, recasting the fitted plateau, timescale, and size exponent as the fixed point, inverse stiffness, and curvature-scaling exponent of the underlying potential, and adding, through the retained inertial term, the slow-start phase the single exponential cannot represent. Second, it yields predictions tied to independently measurable quantities rather than fitted ones: group-size invariance of the deterministic trajectory with a $1/G$ stationary fluctuation, a sharp stability threshold in the refresh interval, and an overdamped-to-oscillatory transition. Third, it furnishes diagnostics that separate failure modes a reward curve alone conflates -- reward hacking, advantage degeneracy, policy concentration, and dynamical instability. Across three models and two group sizes, the closed-form trajectory fits training reward to $R^2 \geq 0.91$ and the predicted group-size invariance holds on both the reward curve and out-of-distribution transfer to eight math benchmarks. The stability and oscillatory predictions are exercised in a controlled exact-reduction setting where the mean-field assumption holds exactly: a softmax-bandit reduction reproduces the predicted overdamped-to-oscillatory transition and locates the refresh-interval stability threshold at the independently measured stiffness, with a deep-network demonstration left to future work.

---


### 15. [Simple Supervision Is Hard to Beat: A Bitter Lesson from Sparse Target Labels in Domain-Adaptive Object Detection](https://arxiv.org/abs/2606.30795)

**<font color=#1a73e8>作者：</font>** Lijun Zhang, Ruinian Xu, Mudit Agrawal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Source-free domain adaptive object detection adapts a source-trained detector to an unlabeled target domain, typically through teacher-student self-training with pseudo-labels. We revisit this setting when a small, uniformly sampled subset of target images is labeled. We introduce Random-Target Supervised Mixing (RTSM), a simple anchor that incorporates these annotations through a supervised detection loss while leaving the original unlabeled adaptation branch unchanged. Across evaluations spanning four SFDA-OD methods, two object detectors, multiple adaptation tasks, and target-label budgets from 1% to 10%, RTSM consistently improves pure SFDA by 1.7 to 18.3 AP50. We then examine whether the same annotations can provide further gains by steering unlabeled self-training. To this end, we evaluate ten sparse-label feedback plugins covering pseudo-label selection, object completion, and optimization control, which yield limited and method-dependent gains over RTSM. These results reveal a bitter lesson for sparse-label SFDA-OD: simple supervision is hard to beat. RTSM therefore provides a simple yet effective anchor for sparse-label SFDA-OD.

---


### 16. [Using AI Agents to Automate Black-Box Audits of Personalization Algorithms at Scale](https://arxiv.org/abs/2606.30801)

**<font color=#1a73e8>作者：</font>** Alessandro Morosini, Sarah H. Cen, Andrew Ilyas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalization algorithms determine what content users encounter on online platforms. Auditing these systems is difficult because independent auditors have only black-box access to the algorithms, while personalization depends on users' attributes, behavior, and evolving interaction histories. Existing auditing methods face a tradeoff: studies with real users capture realistic behavior but are costly and hard to control, whereas sock-puppet audits scale more easily but often rely on scripted behavior that limits realism. Beyond this, both approaches struggle to decouple user attributes from user behavior, limiting our ability to causally understand personalization. To address this gap, we introduce a framework for black-box audits of personalization algorithms using generative AI agents as behavioral engines for synthetic accounts. Each agent is instantiated with a fixed persona, grounded in demographic and political survey data, and interacts with a platform's content by reasoning about it and choosing actions. Because behavior is fixed within each persona while platform-visible signals such as age, gender, or location can be experimentally perturbed, our design enables counterfactual auditing of how platforms respond to user attributes. As a case study, we deploy 1,120 agents on X shortly after the 2024 U.S. election, spanning 14 personas and three counterfactual conditions, collecting over 200,000 content exposures. We find that X's algorithmic feed amplifies toxic, polarizing, political, and right-leaning content relative to the chronological feed, with amplification varying sharply by user ideology. Counterfactual analyses show that demographic signals affect content delivery in persona-dependent ways: pooled effects are largely null, while subgroup-level effects vary in direction and magnitude. Our work establishes GenAI-based agents as a new tool for algorithmic auditing.

---


### 17. [GaussLite: Online Task-Conditioned 3D Gaussian Splatting for Real-Time Robotic Mapping](https://arxiv.org/abs/2606.30809)

**<font color=#1a73e8>作者：</font>** Annika Thomas, Mason Peterson, Jonathan P. How  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D Gaussian Splatting (3DGS) systems distribute representation capacity uniformly across a scene, ignoring the fact that many downstream robotic tasks engage only a fraction of the reconstructed geometry. This causes valuable onboard compute to be allocated towards optimizing irrelevant parts of the scene, either limiting online capacity or under-optimizing the most relevant parts of the scene. We introduce GaussLite, a task-driven 3DGS mapping system that conditions its representation density on a natural-language task specification. Given a posed RGB-D stream and a task such as "prepare to pick up the object on the desk," GaussLite uses a one-shot LLM parser to extract target and anchor objects, which are grounded per-frame by an open-vocabulary detector and segmented to produce per-pixel relevance masks in real time. The mapper allocates seeding density, gradient flow and scaling by task relevance. At matched Gaussian budget and real-time mapping at 4 Hz on resource-constrained hardware, GaussLite outperforms baselines on ROI PSNR on the Replica Dataset by an average +2.72 dB and on a real-hardware demonstration in indoor and outdoor settings by +2.23 dB. We further show that two task-specialized agents' maps can be fused into a single shared map via per-voxel voting on active-optimization counts in real time, outperforming concatenation by +3.42 dB while only sharing an average 7.08% of the map.

---


### 18. [AVTok: 1D Unified Tokenization for Holistic Audio-Video Generation](https://arxiv.org/abs/2606.30811)

**<font color=#1a73e8>作者：</font>** Kien T. Pham, I Chieh Chen, Qifeng Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-video generation has recently gained unprecedented research attention, aiming to synthesize high-quality sounding video content with fine-grained synchronization and semantic alignment between the auditory and visual components. The preceding methods predominantly adopt a dual-branch design with separate tokenization and generation modules per modality, neglecting the representation gap while necessitating intensive computational resources for proper training. Inspired by recent advancements in one-dimensional visual tokenization, we present \textbf{AVTok}, a novel unified tokenizer designated for holistic audio-video generation. AVTok features a dual-stream transformer-based architecture with shared encoder-decoder and modal-specific learnable queries to efficiently and effectively encode an audio-video pair into a compact one-dimensional latent representation with a unified codebook. To cope with the heterogeneous information imbalance that hinders AVTok from exploiting aligned audio-visual information, we devise a hierarchical training strategy to progressively realize reconstruction capabilities for each modality. Extensive experiments demonstrate that AVTok excels both in audio-video reconstruction and when integrated into downstream pipelines for audio-to-video, video-to-audio, and class-conditional joint audio-video generation. AVTok paves the way for the challenge of joint audio-video tokenization and provides a potential direction to build unified large multimodal models for audio-video generation.

---


### 19. [Gradient Smoothing: Coupling Layer-wise Updates for Improved Optimization](https://arxiv.org/abs/2606.30813)

**<font color=#1a73e8>作者：</font>** Haoming Meng, Anton Sugolov, Vardan Papyan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks with repeated architectural blocks, such as transformers, often exhibit structured relationships across layers that emerge during training. Motivated by this observation, we introduce \emph{Depth-wise Gradient Augmentation}, a general optimization paradigm in which the update applied to each layer is obtained by transforming the collection of block-wise optimizer updates along the depth dimension. Within this framework, we study \emph{Gradient Smoothing}, a family of depth-wise smoothing methods, and instantiate it with a simple local \emph{Window Smoothing} operator. The resulting method operates directly on block-wise updates produced by arbitrary base optimizers (e.g., SGD, Adam, Muon), incurs minimal computational overhead, and is compatible with existing optimization pipelines. We evaluate Gradient Smoothing across a diverse set of architectures and training regimes, including language model pretraining, RL post-training of LLMs for reasoning, diffusion modeling, and image classification with Vision Transformers. Across these settings, Gradient Smoothing consistently improves optimization and generalization performance without modifying model architectures or training objectives. We further show that it promotes more structured representation evolution across depth, consistent with its interpretation as a structured depth-wise preconditioning method. Together, these results establish Depth-wise Gradient Augmentation as a promising framework for exploiting cross-depth structure in optimization and demonstrate Gradient Smoothing as a simple and broadly applicable instantiation.

---


### 20. [When transformers learn "impossible" languages, what do they learn?](https://arxiv.org/abs/2606.30815)

**<font color=#1a73e8>作者：</font>** Ram Janarthan, Coleman Haley, Sharon Goldwater  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work suggests that transformer language models show a bias towards human languages over unnatural ("impossible") languages argued to be unacquirable by humans. However, this literature has largely based these claims on differences in sample efficiency and test-set perplexity, rather than on direct evaluations of the linguistic capacities that could plausibly explain non-attestation in human languages. We evaluate two theoretically motivated linking hypotheses: impossibility arising from deficiencies in grammatical sensitivity or generative production. Using GPT-2 style models trained on perturbed "impossible" variants of English, we measure sensitivity to grammaticality using BLiMP minimal pairs, finding that model performance exhibits only gradual degradation, mediated by the language's information locality. In contrast, these models exhibited pronounced failures in generation, producing substantially fewer high-quality sentences at longer lengths. Together, these results suggest generative deficiency and transmission failures as a plausible linking hypothesis between language model behaviour and non-attestation of impossible languages.

---


### 21. [AI-Generated PowerShell Malware: An Experimental Framework and Dataset](https://arxiv.org/abs/2606.30819)

**<font color=#1a73e8>作者：</font>** Luciano Pianese, Vittorio Orbinato, Pietro Liguori 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generative AI has emerged as a significant cybersecurity threat, with several recent attack campaigns leveraging LLMs to generate code for malicious purposes via scripting languages such as PowerShell. Consequently, for cybersecurity analysts, it is imperative to investigate the offensive capabilities of AI code generators. In this paper, we propose an experimental framework to assess LLM-generated PowerShell malware, which comprises a novel sandbox approach for dynamic analysis of AI-generated malware. Furthermore, we present a novel, manually curated dataset of real-world PowerShell malware, annotated in natural language to assist the training and evaluation of LLMs. Finally, this study evaluates permissive, open-weight LLMs adapted to PowerShell malware generation. Our results reveal a high degree of similarity between real malware and LLM-generated ones in terms of triggered OS malicious events, with a median Jaccard index of 84.5% and 48.4% of instances achieving complete overlap.

---


### 22. [Mind the Residual Gap: Probabilistic Downscaling under Real-World Bias](https://arxiv.org/abs/2606.30821)

**<font color=#1a73e8>作者：</font>** Yujin Kim, Nidhi Soma, Sarah Dean  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic downscaling is the task of modeling the conditional distribution of high-resolution fields given coarse inputs, and is a central challenge to atmospheric science, climate modeling, and other multiscale physical systems. A widely used paradigm decomposes the problem into a deterministic mean predictor followed by a stochastic residual generator. While effective in idealized settings, this mean--residual approach frequently produces biased and under-dispersive ensembles in real-world applications. Is this merely generic predictive uncertainty miscalibration? We show that the root cause is more fundamental: residual target misspecification, the residual distribution induced during training differs systematically from the one required at test time due to downscaling bias. To close this gap, we introduce ReMatch (Residual Distribution Matching). ReMatch aligns the training residual distribution toward the test-time regime via optimal transport in a low-dimensional PCA space. This preserves the statistical benefits of the mean--residual framework while reducing the train--test mismatch in the residual targets seen by the stochastic generator. On a controlled synthetic benchmark with varying bias levels and a real-world HRRR--ERA5 wind field downscaling task, ReMatch substantially reduces under-dispersion, improves calibration (SSR and CRPS), and outperforms strong baselines, including the standard mean--residual model and its variants, as well as state-of-the-art super-resolution models. Our code is available at this https URL.

---


### 23. [Information Terra: A Narrative-Anchored Semantic-First Projection of Document Embeddings](https://arxiv.org/abs/2606.30824)

**<font color=#1a73e8>作者：</font>** Brian Keith-Norambuena, Fausto German, Chris North  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We introduce Information Terra, a narrative-anchored semantic-first projection that places a document corpus on an Earth-like globe whose poles are two user-chosen endpoint documents and whose prime meridian is the great-circle geodesic between them on the embedding hypersphere -- so latitude encodes narrative progress and longitude thematic deviation. Land features are recovered from document density via kernel density estimation and labeled by theme. A narrative trail built from the underlying narrative coherence graph, and constrained to be monotone in geodesic progress, provides a readable storyline. The projection's axes are semantically grounded in the user's chosen narrative endpoints, and the globe metaphor affords rotation and antipodal reading. We demonstrate the method on a 540-article Cuban Protests corpus, showing a storyline from Obama's 2016 visit to the 2021 International Aid during the protests.

---


### 24. [Drawing Out Legal Risks: Co-Designing with Lawyers to Predict and Manage Legal Uncertainties of Medical AI Tools](https://arxiv.org/abs/2606.30828)

**<font color=#1a73e8>作者：</font>** Gennie Mansi, Julia Kim, Michael Rosenbloom 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While there's optimism around medical AI tools due to their abilities to adapt from user-to-user and across environments, these new abilities complicate how people and organizations are able to predict and manage risk based on existing laws and regulations. Lawyers are trained to identify potential legal outcomes, but they lack technical AI knowledge, making it difficult to translate their expertise to creators and users of AI tools. We contribute insights from our co-design process with U.S. lawyers to identify and translate ways to predict and manage risks of medical AI tools. We present the visualizations we developed through two years of cross-disciplinary efforts and thereby illustrate our findings about how legal risks are determined and our strategies for people and organizations to predict and manage these risks. We offer insights about leveraging lawyers' expertise to understand, predict, and manage legal risks.

---


### 25. [Partition-Guided Distance Saliency: Bridging Decision and Objective Spaces in Many-Objective Optimization](https://arxiv.org/abs/2606.30836)

**<font color=#1a73e8>作者：</font>** Cláudio Lúcio do Val Lopes, Flávio Vinícius Cruzeiro Martins, Elizabeth Fialho Wanner  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explainability in Many-Objective Optimization (MaO) is currently hindered by the escalating complexity of the Pareto front, which renders the relationship between high-dimensional decision variables and objective outcomes increasingly opaque. As the number of objectives exceeds the limits of traditional visualization, decision-makers encounter a ``cognitive drought'' in identifying relevant trade-offs or specifying target regions without a priori knowledge. To bridge this interpretability gap, we introduce the {Partition-Guided Distance Saliency (PGDS)} framework, a novel XAI approach designed for continuous optimization landscapes. Our framework automates the explanation process through a three-stage pipeline that prioritizes geometric intuition over abstract rules. First, we employ a surrogate model that learns how geometric distances in the decision space map to proximity in the objective space. Second, to address the difficulty of manual target selection in high dimensions, the framework automatically partitions the objective landscape into distinct regions and identifies local ``Dominating Points'' to serve as automated targets for improvement. Third, we quantify how sensitive a solution's position is to each decision variable by measuring the distance shifts induced by perturbations to each variable. This allows PGDS to categorize features as either ``Drivers'' which facilitate convergence toward preferred regions, or ``Blockers'' which represent geometric constraints hindering further progress. Validation on 10-objective benchmarks and a physics-informed engineering problem (Welded Beam) demonstrates that PGDS provides differentiated, actionable insights that traditional visualization and rule-based XAI methods fail to provide.

---


### 26. [A Stationary-Distribution Theory for Triplet-Based Plateau Search in Random Forest Ensemble-Size Selection](https://arxiv.org/abs/2606.30837)

**<font color=#1a73e8>作者：</font>** Andrey A. Dukhovny, Andrey M. Lange  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The number of trees is a central computational parameter in Random Forests: increasing it reduces finite-ensemble variability but increases training and prediction cost. Plateau-based tuning adapts this parameter through local comparisons of out-of-bag scores at a geometric triplet of tree counts. After the remaining hyperparameters have stabilized, however, the central triplet point need not converge to a deterministic value; instead, it fluctuates around a stationary regime.
This paper develops a stationary-distribution theory for this process. The central ensemble size $B_t$ is modeled as a birth-death Markov chain on a geometric grid, and its stationary distribution is derived through local balance. Under a leading centered folded-normal approximation, equilibrium equations are obtained for the original update rule and a symmetric modified variant, implying that the stationary center $B_*=O(\varepsilon^{-2})$ as $\varepsilon\downarrow 0$.
The stationary spread is also characterized. A local Gaussian approximation and a Fokker-Planck interpretation give grid-level variance constants. After conversion to the ensemble-size scale, $\sigma_{B,*}=O(\varepsilon^{-2})$, while the variance is $O(\varepsilon^{-4})$. The leading relative spread is independent of $\varepsilon$ and controlled by the scale factor and update rule. These results interpret plateau-based Random Forest tuning as a stochastic process rather than a deterministic stopping rule.

---


### 27. [Contrastive Reflection for Iterative Prompt Optimization](https://arxiv.org/abs/2606.30840)

**<font color=#1a73e8>作者：</font>** Derek Koh, Jinghui Mo, Benjamin H. Le 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are becoming central to information retrieval: they issue retrieval queries, synthesize answers, and increasingly serve as judges for IR evaluation. Improving the prompts that control these agents is an optimization problem, but in applied IR settings it often looks less like blind search and more like debugging. Engineers need to know which behavior failed, which nearby behavior still worked, what distinguishes the two, and whether a prompt edit improves held-out quality without introducing regressions.
We present Contrastive Reflection, an iterative prompt-optimization framework for agentic IR workflows. The framework starts from a task-centric quality definition: QA agents expose retrieval or reasoning traces, and grading agents expose dimension-level scores and rationales. These structured traces are used to identify error-anchored behavioral slices, add nearby successful examples from the same region, and ask a Teacher LLM to propose a targeted prompt edit. Candidate edits are accepted only when validation performance improves, optionally subject to regression checks. We instantiate the framework with a tree-based slice selector, but the contribution is the contrastive reflection loop rather than the tree itself.
On a public HotpotQA retrieval-augmented QA setup, one tree-selected contrastive repair improves held-out exact-match accuracy from 51.4% to 60.4%. Failure-only and random-evidence variants improve less and break more previously correct examples. A light instruction-only comparison places the method near modern prompt optimizers: MIPROv2 reaches 59.4% and GEPA 57.0%. The result is an interpretable optimization loop for IR agents, aimed at making prompt repair more inspectable and validation-driven.

---


### 28. [A Transferable Learned Temporal Prior for Transmission Reconstruction and Decision-Relevant Uncertainty in Real Outbreak Labels](https://arxiv.org/abs/2606.30842)

**<font color=#1a73e8>作者：</font>** Md Ahsan Karim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Outbreak transmission reconstruction treats epidemiological timing and transmission labels as deterministic ground truth; neither has been systematically evaluated. We trained a logistic regression temporal prior on eleven disease families, locked all parameters before accessing any target outbreak data, and applied it without refitting to a strict Andes virus (ANDV) parent-ranking benchmark of 29 tasks. The locked prior achieved mean reciprocal rank (MRR) 0.571 versus 0.274 and Top-1 accuracy 37.9% versus 13.8% against the best source-trained parametric baseline (permutation p <= 0.0002; 7-8 reversals to lose MRR significance). A phylogenetic concordance audit of 75 NYC mpox inter-host pairs - independent label-reliability evidence rather than a prior validation - found that 54.67% (exact 95% CI: 42.75-66.21%) were genomically unresolved or unsupported. Retaining uncertain edges in ANDV and Guangdong Delta graphs shifted top-5 source-priority sets (Jaccard 0.429-0.667). Transmission-label uncertainty was measurable in the outbreak evidence modules examined, and retaining uncertain links changed which source cases were prioritized for intervention.

---


### 29. [How Can AI Find My Model? A Model-Finding Experimental Study Considering Data Formats, Embeddings, and Retrieval Strategies](https://arxiv.org/abs/2606.30846)

**<font color=#1a73e8>作者：</font>** Jhon G. Botello, Jose J. Padilla, Erika Frydenlund 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Discovering simulation models for reuse remains a fundamental challenge in Modeling and Simulation (M&S). When many models coexist, identifying those that align with a given modeling intent remains difficult. Recent advances in Artificial Intelligence (AI), particularly retrieval-based approaches, offer a promising pathway to operate at this semantic layer. In this paper, we present an experimental study investigating the impact of data representation, transformer-based embedding models, and retrieval strategies on the discovery of simulation models using natural language queries. We evaluated performance across multiple query types using standard information retrieval metrics, including recall@5 and nDCG@5. Results show that data representation matters, open-source embedding models can achieve high performance, and reranking methods are important, especially as query complexity increases. This work provides a baseline for AI-driven model discovery and discusses its role in advancing toward AI-driven composability and interoperability.

---


### 30. [SyncCache: Exploiting Asymmetric Dynamics for Fast Audio-Driven Portrait Animation](https://arxiv.org/abs/2606.30849)

**<font color=#1a73e8>作者：</font>** Juncheng Ma, Yuxuan Du, Yanan Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) have significantly advanced audio-driven portrait animation, but their high computational cost leads to substantial inference latency. Although training-free diffusion caching accelerates inference significant, existing methods are primarily developed for text-conditioned generation and overlook the spatial and modality imbalances inherent in audio-driven portrait animation. In this paper, we propose SyncCache, a training-free caching acceleration method tailored for DiT-based portrait animation that explicitly exploits asymmetric dynamics. Specifically, high-frequency dynamics driven by audio conditions and concentrated in human regions are more challenging and critical to cache and reuse than the low-frequency visual background in portrait animation. First, we introduce Spatially-Asymmetric Probing to prioritize error sensitivity in dynamic human region. Second, through Modality-Decoupled Caching, we bypass heavy DiT block by reusing stable inter-block residuals, while continuously recomputing lightweight audio blocks to preserve precise lip synchronization. Furthermore, we introduce a cache ratio to control cache capacity and formulate memory-adaptive cache selection as an offline dynamic programming problem without online overhead. Extensive experiments demonstrate that SyncCache achieves superior speed-quality trade-offs, delivering up to 4.12x acceleration on HunyuanVideo-Avatar and 3.75x on Wan-S2V with near-lossless visual fidelity and precise audio alignment.

---


### 31. [Multilingual Polarization Detection Using Transformer-Based Models with Class Weighting and Threshold Tuning](https://arxiv.org/abs/2606.30857)

**<font color=#1a73e8>作者：</font>** Aaron Bundi Anampiu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes our submission to SemEval-2026 Task 9 on detecting multilingual, multicultural, and multievent online polarization. We address all three subtasks: binary polarization detection, polarization type classification, and manifestation identification for English and Swahili. Our approach leverages transformer-based models (RoBERTa-base for English, AfroXLMR-base for Swahili) with class-weighted loss functions to address severe label imbalance and per-label threshold tuning to optimize multi-label classification. On the test set, we achieve F1 macro scores of 0.7901 (English) and 0.7910 (Swahili) for Subtask 1, 0.4615 (English) and 0.4808 (Swahili) for Subtask 2 and 0.4791 (English) and 0.5830 (Swahili) for Subtask 3, which give competitive performance on the leaderboard, demonstrating the effectiveness of our methods for handling imbalanced multi-label polarization detection. Our error analysis reveals that models struggle with dehumanization detection and lack of empathy.

---


### 32. [Beyond expert users: agents should help users construct preferences, not just elicit them](https://arxiv.org/abs/2606.30863)

**<font color=#1a73e8>作者：</font>** Irena Saracay, Ludwig Schmidt, Carlos Guestrin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents typically assume an expert user -- one with well-formed preferences about what they want -- and default to clarifying questions whenever the task is underspecified. We argue this assumption is unrealistic. Users often lack the domain knowledge to have completely specified preferences; if asked about their preference on some feature, the user may be unable to answer without the agent helping the user to learn some domain knowledge needed to form a preference for that feature, e.g., via examples or explanations. To formalize these principles, we draw on the Search-Experience-Credence framework from Information Economics to introduce CoPref, a model of how users construct preferences based on agent dialog actions. We then study these ideas concretely in agentic recommender systems, proposing CoShop, an interactive benchmark. In CoShop, an agent converses with and makes recommendations for a CoPref user. The agent's performance depends on whether it can help the user gain the knowledge needed to specify the task well. Evaluating five frontier models, we find that no agent exceeds 56% accuracy on CoShop despite five turns of interaction. Failures stem not from agents' ability to find items, but from how little the interaction expands what users know about what they want.

---


### 33. [Neural Signatures of Programming Expertise: Classifying Programmer Skill Levels Using EEG Data](https://arxiv.org/abs/2606.30879)

**<font color=#1a73e8>作者：</font>** Maurice Rekrut, Mahima Mahabaleshwar Acharya, Taisiia Ulianova 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Accurately assessing a programmer's skill level is critical for hiring, team composition, and performance evaluation in the software industry. Conventional methods, such as coding tests or interviews, often fail to capture the full spectrum of cognitive abilities underlying programming expertise. This study explores using electroencephalography (EEG) and machine learning to investigate neural correlates of programming skill. We analyzed an existing EEG dataset recorded during code comprehension from 37 programmers with 1 to 30 years of experience (8.1 +/- 6.3 years) to examine relationships between neural activity and expertise. Additionally, we conducted classification experiments using Random Forest classifiers with diverse features for binary (experts vs. novices) and multi-class (experts, intermediates, novices) this http URL identified EEG features and brain regions associated with programming expertise. Specifically, EEG entropy showed the strongest correlation with skill level. Furthermore, experts' brains were characterized by highly localized centro-frontal activation, whereas frontal activation in other groups was part of a more distributed network. Regarding classification, our setup achieved an average accuracy of 91.83% (binary) and 78.15% (multi-class) in stratified 10-fold cross-validation, while leave-one-subject-out validation achieved 85.00% and 58.80%, respectively. Individual frequency bands outperformed full-spectrum analyses, and both program comprehension and resting-state data yielded strong results. These findings demonstrate that EEG features effectively capture neural correlates across different skill levels and highlight the potential of neural data to complement traditional methods of skill assessment.

---


### 34. [Debugging as Evidence-Driven Reasoning: Visualization Opportunities in Data-Intensive Programming](https://arxiv.org/abs/2606.30884)

**<font color=#1a73e8>作者：</font>** Yongbo Chen, Yan Zhu, Rebecca Faust  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visualization has been recognized as a valuable means of supporting debugging by externalizing runtime behavior that would otherwise remain hidden or scattered. However, most visual debugging research has focused on traditional software development settings, leaving the distinct challenges of data-intensive workflows largely uncharacterized. To build visual debugging support for these settings, we first need to characterize how practitioners debug in these settings and translate their challenges into concrete visualization opportunities. To this end, we conducted semi-structured interviews with nine participants from diverse data-intensive domains and analyzed the data using thematic analysis. Our analysis reveals three cross-cutting challenge: assembling fragmented evidence, detecting expected-observed discrepancies, and tracing state evolution across workflow components. We distill these challenges into three concrete requirements that current debuggers support only partially but that visualization is well suited to address: cross-artifact evidence alignment, expectation-grounded comparison, and traceable state evolution. Together, these requirements begin to characterize a design space for future visual debugging research in data-intensive programming.

---


### 35. [Knowledge-Driven Dimension Estimation from a Single Image -3D Asset Generation Technology for Digital Twin Construction](https://arxiv.org/abs/2606.30896)

**<font color=#1a73e8>作者：</font>** Hidenori Sakaniwa, Akihito Akai, Akihiko Hyodo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the verification of in-vehicle cameras, simulation technology using virtual spaces has advanced, enabling pre-evaluation of false detections and missed detections in various scenarios. However, discrepancies in the scale of the object being verified between the virtual and real environments can lead to a decrease in camera recognition performance. For traffic signs installed at high altitudes, distance measurement using LiDAR or stereo cameras is difficult, requiring size estimation from monocular images. This paper proposes a method for estimating the scale of an object by decomposing it into multiple structural elements and integrating external knowledge regarding design rules, geometric relationships, and conventional dimensions. Specifically, this method detects each component from a monocular image and estimates the size of each component by considering its structural relationships and dimensional consistency with surrounding elements. Furthermore, it generates a 3D asset of the object by reconstructing the estimated components. This method makes it possible to place 3D assets with a scale approximating the real environment within a digital twin space and is expected to contribute to improving the verification accuracy of in-vehicle cameras for autonomous driving in virtual environments.

---


### 36. [GRAPE: Graph-Augmented Prototype Explanations for Interactive Medical Image Diagnosis](https://arxiv.org/abs/2606.30901)

**<font color=#1a73e8>作者：</font>** Rasul Khanbayov, Hasan Kurban  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prototype-based medical image classifiers present three clinical limitations: they treat findings as independent, silently amplify unsafe physician feedback, and require full retraining whenever a new finding is needed. We present GRAPE (Graph-Augmented Prototype Explanations), a unified architecture that addresses all three challenges. First, a Graph Attention Task Head models anatomical concept co-occurrence, boosting macro-F1 by +13.8,pp over the prototype baseline on TBX11K. Second, a Concept-Mismatch Safety Check - the first such mechanism in prototype-based medical classifiers - warns when the model's dominant finding inside a doctor-drawn region conflicts with the claimed label, catching 85% of erroneous annotations versus 51% for MC-Dropout with no extra inference cost. Third, Open-Vocabulary Prototype Anchoring aligns visual prototypes to clinical text, allowing a new finding to be added from a single labeled image without modifying any other component. On NIH ChestX-ray14, one Effusion example recovers full-supervision localization accuracy; on TBX11K, prototype maps achieve 2.6x better lesion localization than end-to-end baselines. All three capabilities add only +1~ms latency at interactive batch size. The project page is this https URL.

---


### 37. [Why Solve It Twice? Hierarchical Accumulation of Skills for Transfer-Efficient ML Engineering](https://arxiv.org/abs/2606.30911)

**<font color=#1a73e8>作者：</font>** Yongbin Kim, Yashar Talebirad, Osmar R. Zaiane  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> ML engineering agents waste compute rediscovering known techniques because every competition is a cold start. We present HASTE, a hierarchical multi-agent system that organizes cross-competition knowledge into three scope tiers (global, domain, and competition-specific), each coupled to a matching agent level. An orchestrator coordinates domain specialists and promotes learning between tiers via LLM-driven abstraction. A controlled ablation provides evidence for scoped loading: holding a 159-skill inventory constant across 8 competitions, tiered loading achieves a 100% medal rate while flat loading reaches only 62.5%, the same medal rate as loading no skills, and consumes 2x the output tokens. On the full MLE-Bench Lite benchmark (22 Kaggle competitions), HASTE reaches a medal rate of 77.3% using Claude Sonnet 4.6 at 12h per competition. In a cold-start run, the system begins with no accumulated skills. In warm-start runs, it reloads skills learned from earlier competitions, using only global and domain-level skills for transfer across competitions. Warm starts use 52% fewer refinement iterations, and the fraction of proposed changes kept by the agent rises from 42% at low inventory to 85% once 50+ skills are available. These results suggest that better knowledge organization can partly substitute for model strength and compute budget in ML-engineering agents.

---


### 38. [Behavior Cloning is Not All You Need: The Optimality of On-Policy Distillation for Noisy Expert Feedback](https://arxiv.org/abs/2606.30923)

**<font color=#1a73e8>作者：</font>** Ved Sriraman, Peihan Liu, Daniel Hsu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Imitation Learning is a natural framework for learning in sequential decision-making systems and has emerged as the dominant paradigm through which we understand language model training. A central puzzle is that, while in theory offline IL can be horizon-free and optimal, in practice online methods such as on-policy distillation often outperform offline methods such as supervised fine-tuning. We propose a noisy expert model to explain this gap, in which the learner only has access to a noisy version of the expert's policy, but wishes to compete against the reward achieved by a clean expert, motivated by the fact that in many applications, e.g. training language models to perform long chains of thought, the expert is often imperfect. In this setting, we show a sharp separation between offline and online IL. Offline learning from noisy trajectories is fundamentally hard: to compete with the clean expert, the sample complexity must grow exponentially, in contradistinction to the clean expert setting where no explicit horizon dependence exists. In contrast, we prove that online interaction with the noisy expert via a novel variant of OPD enables polynomial dependence on the horizon in general. We further show that, under a natural condition on the expert noise distribution, which we show to be necessary for any horizon-free sample complexity, one can obtain such a guarantee, although our proposed algorithm sacrifices statistical efficiency in its dependence on the size of the policy class. Our analysis leads to an alternative loss function that is commonly considered empirically for LM training. We further provide algorithms and lower bounds, and extend our results to the more realistic setting of unknown corruption when the clean expert is deterministic, thereby providing a theoretical foundation for why OPD can outperform SFT when training language models from imperfect teachers.

---


### 39. [Personalizing Marketplace Policies with Competing Objectives and Constrained Experiments: Evidence from a Job Marketplace](https://arxiv.org/abs/2606.30932)

**<font color=#1a73e8>作者：</font>** Yufei Wu, Zhen Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two-sided marketplaces connect distinct user groups whose interests often conflict -- improving outcomes on one side could degrade the other side's experience. To address this challenge, we deploy an integrated framework for personalizing free-value thresholds -- a policy governing the scope of complimentary services for job listings -- across a two-sided job marketplace connecting millions of employers and job seekers. Our personalized policy delivers statistically significant and economically sizable lift in the target metric while respecting engagement guardrail constraints.
Direct application of standard uplift methods proves insufficient here for two reasons. First, cross-side externalities demand multi-objective optimization: maximizing employer-side metrics risks harming job seeker engagement, with effects varying substantially across job segments. Second, marketplace interference necessitates cluster-level randomization, limiting us to few discrete treatment levels -- effectively a form of positivity violation that rules out methods designed for continuous treatments.
We contribute an integrated framework with three components. Our ensemble-based hybrid ranking models target and guardrail metrics separately, cutting guardrail risk by over 10% for equivalent target gains compared to single-objective approaches. A treatment effect extrapolation method extends our estimates from limited experimental variation to untested policy levels, relying on monotonicity assumptions that we validate empirically. Finally, we present production deployment, where post-launch data confirms both extrapolation accuracy and guardrail compliance.
Our deployed system demonstrates that principled methodology can enable meaningful personalization even when experiments are severely constrained and different objectives compete -- common conditions that characterize many real-world marketplaces.

---


### 40. [Quality-Aware Modulation for Diffusion Transformers](https://arxiv.org/abs/2606.30934)

**<font color=#1a73e8>作者：</font>** Luke Budny, Yuhong Guo, Kevin Cheung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern text-to-image diffusion models, such as diffusion transformers (DiT), rely on timestep or prompt embeddings to modulate the strength of the denoising process in each timestep. While this modulation communicates the current noise level, it does not provide any quality-aware information, which can lead to generated images that are unaligned, visually inconsistent, and lacking in fidelity. In this paper, we propose the Quality Representation Module (QRM), a lightweight transformer module that learns a quality-aware representation based on existing model inputs, and produces a set of vectors $M_{qrm}$. These vectors adjust the adaptive LayerNorm modulation within the DiT transformer blocks, thereby injecting a quality-sensitive signal into the denoising parameters. The QRM introduces no significant changes to the sampling schedule or diffusion backbone. Experiments include ablations on QRM training losses and architectures, as well as empirical results demonstrating consistent image quality improvements over baseline DiT-based models.

---


### 41. [Physics-informed Conditional Normalizing Flows for Angles-only Cislunar Orbit Determination](https://arxiv.org/abs/2606.30936)

**<font color=#1a73e8>作者：</font>** Walther Litteri, Massimiliano Vasile  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative Astrodynamics is advanced in this work by extending generative modelling to an orbit determination problem in the cislunar environment. The task is formulated as conditional density estimation, aiming to infer the probability distribution of the initial state from angles-only measurements over short observation arcs. A normalising flow is trained on perturbed topocentric observations from Near Rectilinear Halo Orbits, enabling a flexible and potentially multimodal posterior representation. Given new measurements, the learned density is sampled to generate statistically consistent and physics-informed state hypotheses. These estimates are refined via nonlinear least-squares minimisation, providing a competitive warm start for classical algorithms.

---


### 42. [No Adaptation Without Observation: Observability-Constrained Test-Time Prompt Tuning for LiDAR Semantic Segmentation](https://arxiv.org/abs/2606.30937)

**<font color=#1a73e8>作者：</font>** Linlian Jiang, Wentao Ju, Sadman Rakib Pinon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR semantic segmentation often degrades under real-world deployment due to evolving sensing conditions, while collecting new annotations for retraining is impractical. Test-time adaptation (TTA) updates model parameters online using pseudo-label supervision, but directly applying standard TTA strategies to LiDAR data is challenging. Because pseudo-label reliability is spatially heteroscedastic under range-dependent sparsity and occlusion, uniform updates on globally shared parameters can inject unstable gradients and destabilize adaptation. We propose a geometry-constrained test-time prompt tuning framework for LiDAR semantic segmentation. Our method estimates per-location sensing reliability from depth-consistent beam terminations and neighborhood support, and uses it to reweight spatial supervision. Adaptation is confined to lightweight prompt adapters inserted into a frozen backbone, with spatial gating to prevent unreliable regions from perturbing globally shared representations. A temporally smoothed prototype alignment strategy further stabilizes online updates by accumulating reliable semantic evidence over time. Experiments on standard LiDAR benchmarks demonstrate improved adaptation stability and segmentation performance under deployment variations without additional annotations.

---


### 43. [Anthropomorphism in AI Companion Communities: Age, Gender, and Emotional Correlates](https://arxiv.org/abs/2606.30942)

**<font color=#1a73e8>作者：</font>** Afia Mubashir, Boden Moraski, Stephanie Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) systems are increasingly integrated into daily life, with millions now using AI chatbots built on Large Language Models (LLMs) for companionship. Both humanlike AI qualities and user predispositions to anthropomorphize relate to social consequences, such as increased trust, social health benefits, and psychological harms. Populations such as children, older adults, or those with mental health vulnerabilities may be particularly susceptible to anthropomorphism and its detriments, but mixed findings complicate the role of demographics. We used publicly available Reddit data from three popular AI companion subreddits to assess relationships between gender, age, anthropomorphism, and elicited emotions, to better understand how different people perceive and are affected by AI companions. We investigated three questions: How do age and gender relate to anthropomorphization of AI?, How does emotional expression relate to anthropomorphization?, and How do age and gender moderate emotion-anthropomorphization relationships? We found that adults and women anthropomorphize AI chatbots more than teens and men, and that positive emotional expression, particularly joy, is positively associated with anthropomorphization, while neutrality is negatively associated with anthropomorphism. Both relationships were stronger in adults than teens. Our findings suggest that the tendency to anthropomorphize may be more broadly distributed across age groups than previously expected, thereby prompting the reevaluation of existing digital safety norms.

---


### 44. [Learning Where to Look: A Reinforcement Learning Framework for Robust Micro-Ultrasound Prostate Cancer Detection](https://arxiv.org/abs/2606.30951)

**<font color=#1a73e8>作者：</font>** Mohammad Mahdi Abootorabi, Sina Namazi, Armin Saadat 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Micro-ultrasound ($\mu$US) is a new, emerging, and promising imaging modality for prostate cancer (PCa) detection, but accurate identification of suspicious tissue remains highly dependent on clinical experience, leading to substantial inter-observer variability. Machine-learning assistance can reduce this variability; however, training reliable deep models is challenging because supervision is sparse and noisy -- typically limited to core-level histopathology outcomes (e.g., cancer grade and its percentage in a biopsy core) without pixel-level lesion annotations and under severe class imbalance. We introduce Prost-RL, which reframes $\mu$US PCa detection as a spatially aware, policy-driven inference problem by learning where to look before decoding. Prost-RL integrates a lightweight reinforcement-learning policy into a foundation-model encoder-decoder to generate interpretable spatial attention maps that act as soft prompts for both cancer-likelihood heatmap prediction and image-level classification. We further propose Adaptive Policy Optimization (APO) to stabilize hybrid supervised-RL training and a noise-robust objective combining symmetric cross-entropy with negative-entropy regularization to mitigate weak-label noise and encourage sharp localization. On a cohort of 6,607 biopsy cores from 693 patients across five clinical sites, Prost-RL achieves $79.0\pm3.5$ AUROC with $64.6\pm6.3$% sensitivity at 80% specificity for core-level detection (+2.1 AUROC and +4.5 sensitivity points over the strongest baseline), and $79.3\pm5.8$ AUROC for clinically significant cancer classification. The learned policy highlights biopsy-aligned regions, providing transparent, spatially grounded evidence alongside quantitative risk predictions. Code is available at: this https URL.

---


### 45. [Neuro-Bayesian-Symbolic Residual Attention Shallow Network: Explainable Deep Learning for Cybersecurity Risk Assessment](https://arxiv.org/abs/2606.30953)

**<font color=#1a73e8>作者：</font>** Nicolaie Popescu-Bodorin, Madeleine Togher  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce the Neuro-Bayesian-Symbolic Residual Attention Shallow Network (NBS-RASN), a hybrid neural architecture for explainable cybersecurity risk assessment in open-source ecosystems. Unlike deep models that trade interpretability for accuracy, our shallow network encodes domain knowledge, causal reasoning, and expert judgment as differentiable components. It uses 80 interpretable neurons across 12 layers, including a gatekeeper that enforces five epistemological axioms - precision, causality, falsifiability, transparency, and completeness - as hard constraints before propagation. Despite limited depth, the network exhibits deep-learning traits via residual attention and feedback loops, learning complex risk patterns without becoming a black box. It produces fully decomposable scores: a deterministic weighted component plus an expert adjustment, with each adjustment traceable to named amplifiers (blast radius, propagation speed, structural nature, default exposure, exploitation pattern, institutional criticality). We validate on 20 open-source projects covering all OWASP Top 10:2025 categories and language risk classes, achieving confidence scores of 0.79-0.97, and show that explainability is guaranteed by design, not by a training algorithm. This challenges the assumption that deep learning requires deep networks, proving that shallow networks with deep reasoning can outperform opaque models in high-stakes cybersecurity, where interpretability is essential.

---


### 46. [Linguistic Distancing on Social Media: Indicators of Emotion Regulation Across Age Groups](https://arxiv.org/abs/2606.30957)

**<font color=#1a73e8>作者：</font>** Daniela Teodorescu, Saif M. Mohammad, Alona Fyshe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Managing our emotional responses to events is key to emotional well-being, a process referred to as emotion regulation in psychology. Previous work has established that the degree to which we distance events is a type of emotion regulation. When we psychologically distance from events there can be markers in our language. These markers have been referred to as linguistic distancing. We build upon a previous metric to operationalize linguistic distancing, and explore how it changes across the lifespan. We explore this systematically by analyzing large amounts of social media text, a venue where people express their emotions. By investigating how distancing varies across age groups we can better understand how emotion regulation varies with age and provide initial benchmarks on social media data. We provide additional evidence further strengthening the hypothesis that linguistic distancing occurs in proportionally more instances with age. These findings align with past work in psychology which indicate improved well-being with older age. Better understanding how linguistic distancing changes with age is important because it functions as a marker of well-being and can inform effective health interventions. We provide a foundation for further exploring emotion regulation through linguistic distancing in text data.

---


### 47. [HyPOLE: Hyperproperty-Guided Multi-Agent Reinforcement Learning under Partial Observation](https://arxiv.org/abs/2606.30966)

**<font color=#1a73e8>作者：</font>** Arshia Rafieioskouei, Tzu-Han Hsu, Matthew Lucas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Formal specification is a powerful tool to guide the learning process and provides significant advantages over reward shaping: (1) mathematical rigor; (2) expressiveness to specify objectives and constraints, and (3) the ability to define tactics to achieve objectives. However, these benefits remain largely unexplored in the context of Multi-Agent Reinforcement Learning (MARL). This paper introduces HyPOLE, a novel framework for MARL under partial observability, where learning is guided by the expressive power of the so-called hyperproperties and, in particular, the temporal logic HyperLTL. We integrate Centralized Training for Decentralized Execution (CTDE) techniques with HyPOLE to synthesize decentralized policies, and our evaluation on SMAC, MessySMAC, and WildFire benchmark demonstrates clear advantages over baselines.

---


### 48. [PhotoQuilt: Training-Free Arbitrary-Resolution Photomosaics via Bootstrapped Tiled Denoising](https://arxiv.org/abs/2606.30968)

**<font color=#1a73e8>作者：</font>** Koorosh Roohi, Javad Rajabi, Andrew Fleet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photomosaics are large images whose local regions are seen as independent tiles while their overall arrangement forms a coherent scene. Generating them at high resolution, with every tile convincing in its own right, is computationally expensive, since the canvas must hold many detailed tiles at once. We present PhotoQuilt, a training-free framework that generates photomosaics at arbitrary resolution. Diffusion models struggle to satisfy both scales at once, as direct high-resolution generation is costly and tends toward one smooth image rather than a mosaic, while patch-based tiling keeps local detail but loses global structure. PhotoQuilt resolves this with a bootstrapped tiled denoising procedure. We first produce a global composition at low resolution to fix the layout, then upscale it in latent space and re-inject noise to restore generative capacity. Denoising proceeds within fixed tiles, so each forms its own image while the shared global structure holds them in one layout. Because tile generation is handled separately, PhotoQuilt scales to large canvases without quadratic attention cost. Experiments show that PhotoQuilt outperforms current baselines on both global structure and local realism.

---


### 49. [AgentBound: Verifiable Behavioral Governance for Autonomous AI Agents](https://arxiv.org/abs/2606.30970)

**<font color=#1a73e8>作者：</font>** Anuj Kaul, Qianlong Lan, Pranay Gupta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents increasingly perform consequential actions on behalf of human principals, including financial transactions, external communications, and enterprise workflows. Existing agent infrastructure relies on identity federation and delegated authorization to authenticate workloads and control resource access, but it cannot determine whether an authorized action should be executed under the current behavioral and operational context.
We present AgentBound, a runtime governance framework that provides verifiable behavioral oversight for autonomous AI agents. AgentBound evaluates each proposed action using three independent authorities: delegated authorization, owner-signed behavioral constitutions, and site action contracts. Their judgments are conservatively composed through a formal decision model to determine whether an action should be permitted, reviewed, or denied before execution.
To provide accountability, AgentBound generates cryptographically verifiable governance receipts that bind every action to the exact delegation, policy, and semantic artifacts governing the decision, enabling independent replay verification and policy provenance. The framework also introduces standing delegation for long-running agents, allowing periodic workloads to operate under continuously refreshed governance policies while preserving revocability and bounded authority.
We present the formal foundation, system architecture, governance receipt protocol, and AgentBound-Bench, a benchmark framework for evaluating governance correctness, authority composition, and accountability. Rather than replacing model alignment, AgentBound complements it by providing a deterministic governance layer between authorization and execution, transforming governance from a process that must be trusted into one that can be independently verified.

---


### 50. [From Propositional to Perceptual Asymmetry: Extending Frictive Policy Optimization to Asymmetric Partial Information Dialogue](https://arxiv.org/abs/2606.30973)

**<font color=#1a73e8>作者：</font>** Yifan Zhu, Kyeongmin Rim, James Pustejovsky  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frictive Policy Optimization (FPO; Pustejovsky et al., 2025) treats friction in collaborative dialogue -- misalignment, misunderstanding, repair -- as an epistemic signal essential to common-ground construction, rather than noise to be minimized. However, FPO and its implementations assume shared perceptual contexts, where friction arises from differently interpreted propositions over the same scene, which we define as propositional asymmetry. We extend FPO to perceptual asymmetry, where participants hold asymmetric partial information and the same referring expression yields different denotations depending on whose information state grounds the reference. We evaluate this through cross-corpora analysis and LLM probing on referentially asymmetric dialogue tasks, primarily the HCRC MapTask (Anderson et al., 1991). We find that FPO's friction functional is empirically valid only when evaluated from within each participant's information horizon: different landmark configurations produce qualitatively distinct grounding failure modes, with a small class of ambiguous configurations driving a disproportionate share of misunderstandings through trajectories that appear successful but silently diverge. The LLM probe confirms that having the "right perspective" matters more than having all perspectives: the informed single viewpoint outperforms omniscient access to both participants' contexts. We propose two annotation refinements: subtype decomposition of pending grounding states and accommodation-aware alignment classification.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-274](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
