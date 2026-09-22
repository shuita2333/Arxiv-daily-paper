# 📦 其他研究 | 2026年09月23日

> 本类共 **463** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-463**（第 10/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-463**

---

### 451. [Anatomy-Decomposed Chest Computed Tomography (CT) Projections as Scalable Supervision for Bone Suppression in Chest Radiographs](https://arxiv.org/abs/2609.24937)

**<font color=#1a73e8>作者：</font>** Mrunmay Angaitkar, Piyush Kumar, Aarjav Satia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bone overlap can obscure abnormalities in chest radiographs, while scarce paired training data limit supervised bone suppression. We address this challenge with a digitally reconstructed radiograph (DRR) framework that converts chest computed tomography (CT) into paired supervision for component suppression. A novel bone segmentation algorithm enables CT decomposition into bone, non-lung soft-tissue, and lung components, which are projected separately. Their weighted combination yields synthetic radiographs with pixel-registered component images that sum exactly to the full DRR. Models trained on these data suppress bone or lung components by predicting the target component and recovering the remainder by subtraction, transferring to real radiographs without real paired training data. As an extension, their outputs on real radiographs provide target domains for unpaired, component-wise DRR translation, reducing the appearance gap while retaining anatomical details. Across multiple public datasets, downstream detection experiments demonstrate the utility of bone suppression, with gains concentrated on abnormalities with substantial bone overlap. Compared with open-source DRR engines applied to the same CTs, our unmodified DRRs achieve comparable realism and preservation of label-relevant anatomy, while translated DRRs achieve the best Fréchet inception distance (FID), lung-field sharpness, and agreement with source-CT anatomy among the evaluated methods. Models and inference code: this https URL Translated projections: this https URL.

---


### 452. [Exactness at Inference: A Representational Criterion for Out-of-Distribution Generalization](https://arxiv.org/abs/2609.24942)

**<font color=#1a73e8>作者：</font>** Filipe Marinho Rocha, Inês Dutra, Vítor Santos Costa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A model generalizes outside its training distribution only when it computes a representation structurally equivalent to the generating mechanism, not an approximation fitted to it. Such equivalence is necessary for exactness in and out of distribution, and extrapolation is governed by this exactness at inference, whatever its realization. Tensor Logic shows this: a zero-temperature contraction is equivalent to discrete logic, deducing in place with no artefact extracted, its tensors Boolean, its embeddings orthonormal, only its arithmetic continuous. Lacking infinite recursion it reaches Datalog, not Prolog, and though exact over closed domains it needs external memory to bind a novel entity. The criterion needs neither a discrete representation nor an extracted expression, and constrains inference, not training: an exact marginal in $[0,1]$ passes, a Neural Network thresholded to a hard label does not. Logic Tensor Networks fail it, while differentiable ILP and Tensor Logic at $T=0$ pass. Piecewise-affine extrapolation divergence and an inability to bind novel entities are two faces of a shortfall in exact representability. For hybrid architectures, a propagation rule follows: the output inherits the bounds of every fitted estimator on its path, explaining which axes fail in equivariant models and the ARC-AGI induction/transduction split. Only an exact hypothesis class certifies what the training data leave underdetermined: on a law-derived partition it finds the $56.3\%$ of distant queries that are answerable, which ensembles meet with false confidence and distance metrics rank backwards. Common inductive biases, from symmetries to memory, reach exactness only because humans inject them, an argument for inducing exact representations rather than fitting surrogates whose residuals, even at the arithmetic floor in training, diverge outside the data and compound under composition.

---


### 453. [Learning Physics from an Imperfect Ancestor](https://arxiv.org/abs/2609.24947)

**<font color=#1a73e8>作者：</font>** S. Mohammad Mousavi, Teeratorn Kadeethum, Nikolaos Bouklas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators evaluate parametric partial differential equations cheaply but degrade sharply outside their training distribution. Physics-informed neural networks avoid dependence on labeled data, yet their optimization can be basin-fragile: when the governing residual admits multiple solutions, a PINN trained from scratch may converge to a physically incorrect state despite achieving a small residual. We show that these failure modes can be addressed jointly: an imperfect NO provides the structural prior needed to place a PINN in the correct solution basin, while the PDE residual refines the solution beyond the operator's accuracy. We introduce a three-stage framework that freezes the spatial basis of a physics-informed NO, extrapolates its solution branch to an out-of-distribution parameter using a polynomial continuation prior, and distills the resulting field into a fresh PINN. The NO need not be accurate at the target; it transfers solution-branch information, while PDE residual minimization in the PINN governs convergence. We evaluate the framework on three nonlinear PDEs: 1D viscous Burgers, 2D steady Allen-Cahn near a pitchfork bifurcation, and 2D steady lid-driven cavity flow. For Allen-Cahn, where the trivial solution satisfies the PDE residual exactly, a standard PINN collapses to the trivial zero branch, whereas distillation from the crude extrapolated operator recovers the non-trivial branch that matches the finite-difference reference. For the lid-driven cavity, extrapolating to a Reynolds number of Re = 3200 accelerates convergence to the correct physical state, achieving competitive accuracy using fewer parameters and optimization steps than recent literature baselines. These results establish a simple principle: an NO need not accurately predict the solution to be useful; it only needs to identify the correct basin from which PINN optimization can recover it.

---


### 454. [Generative Tutorial: Towards Live Contextualized Visual Instructions for Physical Tasks](https://arxiv.org/abs/2609.24955)

**<font color=#1a73e8>作者：</font>** Muzhe Wu, Zuchen Li, Xu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visual instructions for physical tasks are typically authored in one context and followed in another, requiring users to translate demonstrated tools, materials, and spatial relationships into their own environment. We introduce Generative Tutorial, a conceptual framework for live visual instruction that depicts intended outcomes and actions within the user's environment and task flow. A formative evaluation of state-of-the-art image and video generation identifies failures and potential benefits across 15 physical tasks. Drawing on these findings, we build an augmented-reality prototype system that proactively generates goal images and demonstration videos using observed workspace context and predicted visual outcomes of preceding actions. A 24-participant lab study found higher task performance quality, greater perceived workspace correspondence, and shorter step-confirmation intervals with the system than with pre-authored guidance. Qualitative findings highlighted how contextual resemblance shapes trust, how generation errors affect interpretation, and how guidance delivery should adapt to users' needs, informing future designs.

---


### 455. [Perception-Aware Communication Middleware for Distributed Visual Perception in UAV Swarms](https://arxiv.org/abs/2609.24964)

**<font color=#1a73e8>作者：</font>** Manveen Kaur, Kevin Loi, Ifunanya Okafor 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Unmanned Aerial Vehicle (UAV) swarms increasingly support safety-critical applications that rely on distributed visual perception. Meeting the low-latency requirements of these applications can require perception models to execute within the swarm on inference-capable UAVs, creating a need for efficient UAV-to-UAV transport of high-bandwidth perception data. However, the Quality-of-Service (QoS) requirements of perception differ from conventional packet-level QoS; successful delivery of individual packets does not ensure that a complete, timely, and usable image is available for inference. We present a novel perception-aware communication middleware that treats complete perception-data samples as the communication objects for which QoS must be satisfied. The middleware extends a lightweight UDP broker-based publish-subscribe architecture with perception-specific services, including image fragmentation and reconstruction, concurrent packet transmission, priority-aware scheduling, and image quality assessment. The middleware is evaluated on a heterogeneous hardware testbed emulating a UAV swarm using YOLOv8n object detection. Experimental results demonstrate low end-to-end application latency, substantially higher throughput than a lightweight UDP broker, effective prioritization of perception traffic under increasing background load, and mitigation of object-detection degradation through middleware-level image quality assessment. This work provides an initial framework for integrating AI-specific data handling into communication middleware to support emerging distributed AI applications in multi-agent mobile cyber-physical systems.

---


### 456. [Jev for Scientific Decisions: Evaluating Semantic Choices and Their Consequences](https://arxiv.org/abs/2609.24965)

**<font color=#1a73e8>作者：</font>** Boyuan Deng, Shuyi Fan, Hongyang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific workflows often require choosing among known relations before a deterministic calculation can proceed. Whether observations share a culture, treatment or reference standard can change the scientific meaning of the resulting count or comparison. We evaluate Jev as a semantic decision component using a harness that follows its documented guidance and assigns arithmetic to code. The study compares twelve model configurations on twenty source-grounded Choices across ten scientific cases, each repeated five times. We measure semantic selections, downstream outputs and final claim labels separately. Jev matched five other configurations at complete semantic correctness and achieved the lowest observed median latency among successful responses. Across three comparison models, seven wrong selections on one culture-history question changed downstream counts while preserving the correct final label. These results identify a useful role for Jev in prepared scientific decision tasks and show why evaluating that role requires checking the relations and quantities that a workflow will reuse.

---


### 457. [RRSI: Regularized Recursive Self-Improvement of Agent Harnesses](https://arxiv.org/abs/2609.24972)

**<font color=#1a73e8>作者：</font>** Peng Xia, Rujun Han, Zifeng Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An LLM agent's capability is largely magnified by its harness, namely the prompts, control flow, tooling, memory, and context management surrounding the frozen backbone model. Recent methods increasingly automate this process by iteratively proposing and selecting component-wise edits of an agent harness, practically establishing a form of recursive self-improvement (RSI) at the agent-system level. However, such recursive evolution may overfit by memorizing the training tasks, showing large in-distribution gains that shrink or even vanish on out-of-distribution benchmarks. We introduce Regularized Recursive Self-Improvement of Agent Harnesses (RRSI), which incorporates the principles of regularizations into harness self-improvement by constraining the evolution candidate proposal and selection. The proposer operates with a temporally annealed budget, limiting how many edits a candidate can bundle, and it encourages unexplored trajectories based on evolution history. The selector is equipped with a critic and a pruner: the critic screens benchmark-specific proposals, while the pruner, removes changes that are too small, too expensive, or no longer useful. Together these constraints favor reusable agent mechanisms over benchmark-specific ones or even noises. Across eight benchmarks spanning coding, agentic workspace and engineering design tasks, RRSI gains up to 14.1 points on the split it evolves against and up to 4.7 points on the five out-of-distribution benchmarks, while producing a harness that runs on 30% fewer policy tokens than the unregularized evolution. Code is available at this https URL and project page is this https URL.

---


### 458. [Residual Community Prototypes Under-Reject Held-Out Malware Families in FCG-MFD](https://arxiv.org/abs/2609.24980)

**<font color=#1a73e8>作者：</font>** Junru Zhu, Yixin Yang, Xiaoqing Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-set malware-family recognition must classify known families while rejecting families absent from training. We test whether Louvain-community summaries add rejection information beyond a graph neural network embedding and dimension-matched generic topology. The study uses a deduplicated, conflict-audited FCG-MFD corpus, five held-out families, and three optimization seeds. Community features are residualized against generic topology using known-family training data before nearest-prototype scoring. Residual community does not produce stable held-out-family rejection. Ranking effects reverse across families, the false-positive rate at 95 percent unknown recall worsens for every held-out family, and a validation-fitted threshold rejects only 4.48 percent of unknown samples. Accepted-known macro F1 improves in every family, but with five independent family units the exact two-sided sign-flip p-value is 0.0625, the smallest attainable value. The score remains associated with graph scale, while simple classifier uncertainty performs better on ranking, high-recall rejection, and OSCR. In this GIN/FCG-MFD setting, community-enriched prototypes change known-class geometry without creating a stable unknown margin. Graph open-set evaluations should pair structural features with matched topology controls, operational thresholds, and held-out-family analysis.

---


### 459. [GAE: Learning a Geometry-Native Latent Space for 3D-Consistent World Generation](https://arxiv.org/abs/2609.24981)

**<font color=#1a73e8>作者：</font>** Jiahao Lu, Minghao Yin, Wenbo Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a compact geometry-native latent space as a shared foundation for perception and generation. Visual generators can produce photorealistic frames without preserving a consistent 3D scene. We argue that this is not only a modeling problem but also a representation problem: generators typically evolve appearance-centric latents, while perception models recover geometry in a semantically rich space that encodes cross-view structure. Rather than adding geometry as another output, we reparameterize a geometry foundation model's features into a compact latent space for generation. We realize this shift with the geometry-native autoencoder (GAE), whose latent is jointly decodable to appearance, depth, cameras, and point maps. With this state, a standard conditional flow supports diverse generation tasks. In controlled comparisons that hold the generator and training protocol fixed, replacing the latent with GAE improves both visual quality and independently measured 3D coherence: FVD falls by $12.7\%$ and $23.1\%$ on RealEstate10K and DL3DV, and camera-trajectory error is halved on RealEstate10K. Together, these results show that the latent space is central to geometry-consistent generation and can serve as a shared interface between perception and generation.

---


### 460. [WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](https://arxiv.org/abs/2609.24984)

**<font color=#1a73e8>作者：</font>** Wangbo Yu, Kunhao Liu, Wenbo Hu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models enable interactive exploration of dynamic environments, yet struggle to respect prior observations over long horizons and across viewpoints. We present WorldCrafter, a video world model that learns a camera-queryable implicit 3D-aware memory for this purpose. The key insight is to let the requested viewpoint shape how multi-view evidence is compressed into the video generator's limited token budget. Trained jointly with the video generator, a memory encoder and pose-conditioned readout module integrate historical observations into a fixed set of target view-specific tokens before denoising, without explicit depth-based correspondences. By combining this memory with recent temporal context and few-step distillation, WorldCrafter enables streaming scene exploration from a single input image or text prompt. Experiments across static and dynamic scenes show substantial gains in long-horizon consistency and camera-control accuracy while preserving visual quality during minute-scale exploration.

---


### 461. [Critical-State RL: Diagnosing Trainable States for Multi-Turn Tool Use](https://arxiv.org/abs/2609.24985)

**<font color=#1a73e8>作者：</font>** Zixiang Chen, Wenting Zhao, Zhepeng Cen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-turn tool-use failures can hinge on a single model call, yet reward variation alone does not reveal which call would benefit from training. When rewards depend on later interactions, their variation can reflect downstream randomness rather than differences between the current actions. We introduce Critical-State RL to identify trainable states in multi-turn interactions. Given task-defined candidate calls and local rewards, the method assesses whether each reward captures the action's effect on task success and whether improvement over a reference policy is possible. It then uses nested sampling to separate action-dependent reward variation from continuation noise and optimizes the policy at the selected states using contextual-bandit training. Experiments on the Berkeley Function Calling Leaderboard (BFCL) v4 compare training at diagnostic-selected states with training at alternative states. For missing-function tasks, the diagnostic selects the response after the tool becomes available; for missing-argument tasks, it selects the response before the missing argument is supplied. Training the selected responses improves performance, including about 14 percentage points on the missing-function task, while training the alternatives leaves performance flat or worse. We further apply the recipe across models and tasks, including logged repeat-call avoidance and memory management.

---


### 462. [GameHorizon Suite: Multi-Horizon Data and Evaluation in Gameplay](https://arxiv.org/abs/2609.25001)

**<font color=#1a73e8>作者：</font>** Yiran Wang, Xingyilang Yin, Junfu Pu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern video games provide a measurable testbed for AI models, combining abilities of visual understanding, instruction decomposition, goal planning, and precise action control over multiple temporal horizons. Existing datasets and benchmarks, however, either cover a narrow range of games, lack language instructions, or rely on high-variance online rollouts. To address these challenges, we introduce GameHorizon, a unified data and evaluation suite that measures gameplay capabilities at different horizons for diverse model families. GameHorizon Suite consists of three components. First, GameHorizon-Annotator is a scalable and automated annotation pipeline for multi-horizon instructions. Second, utilizing the pipeline, we construct GameHorizon-Data, the first large-scale AAA gameplay dataset with temporally aligned videos, player actions, and multi-horizon instructions. It comprises 5,000 hours of recordings from 21 games, collected by 100 human expert players. Third, we build GameHorizon-Bench with reproducible offline and stepwise online testing. The offline track enables reproducible evaluation using thousands of standardized questions organized into three primary tasks and a series of diagnostic variants, while the online track tests whether offline scores reflect actual gameplay capabilities and localizes failures to specific steps within long-horizon gameplay. Based on our GameHorizon Suite, we evaluate 47 models through more than one million model invocations, revealing a meaningful hierarchy of task difficulty and pronounced differences in model capabilities. Our work can provide a standardized yardstick for evaluating gameplay capabilities across horizons and model families. We will release our dataset, annotator, and benchmark to facilitate future research.

---


### 463. [Passthrough Rigidity: The Behavioral and Visuomotor Costs of Mediated Perception](https://arxiv.org/abs/2609.25002)

**<font color=#1a73e8>作者：</font>** Markus D. Solbach, Mohit Goyal, Sakar Khattar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Broad public adoption of head-mounted displays using video passthrough remains elusive despite significant market investment. A precise understanding of why users experience persistent discomfort even as hardware factors such as resolution and latency have dramatically improved remains an open issue. This paper investigates the impact of viewing the world through video passthrough systems on human behavioral and physiological patterns through a large-scale multimodal study. We developed a novel protocol to capture synchronized oculomotor, kinematic, and physiological data during a block assembly task requiring complex hand-eye coordination. Using a within-subject design (N=110), we evaluated both natural and passthrough viewing conditions. Our results reveal a four-fold suppression of rotational head velocity and a pronounced decoupling of head-gaze coordination. This suggests motor caution being employed as an adaptive strategy - which we term "Passthrough Rigidity". This phenomenon appears to shift the information-gathering burden to the oculomotor system, resulting in significantly longer fixation durations and restricted visual search patterns. These kinematic shifts directly correlate with poorer task performance and measurable physiological cost, evidenced by a significant reduction in blink duration and increased reports of ocular strain and cognitive load. We conclude that current passthrough implementations induce a measurable shift from flexible exploration to motor caution, where task performance is preserved at the cost of user comfort and biomechanical efficiency. These findings provide a novel quantitative framework for evaluating and improving future XR devices, establishing that resolving "comfort" for passthrough requires addressing the deep-seated biomechanical compensations caused by mediated perception. Data available at this https URL

---


> [!TIP]
> 当前位于：**451-463**（第 10/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-463**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
