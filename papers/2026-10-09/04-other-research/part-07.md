# 📦 其他研究 | 2026年10月09日

> 本类共 **324** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-324**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-324**

---

### 301. [Executing Causal Structure Learning with Linear-Attention Transformers](https://arxiv.org/abs/2610.10395)

**<font color=#1a73e8>作者：</font>** Amartya Roy, Sayar Karmakar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers can execute algorithms on data given in their input. We ask whether they can do the same for causal discovery. We study a standard continuous method that repeatedly updates a candidate causal graph while enforcing acyclicity. We explicitly construct a fixed-weight transformer whose forward pass exactly reproduces one update of this method, so repeated blocks reproduce its optimization trajectory. The transformer carries the current graph and the algorithm's multiplier between updates. We show that retaining the multiplier is essential for exact execution, since different multiplier values can lead to different next updates. We also give conditions under which, within a fixed stage, the number of updates needed to reach a target accuracy can be computed in advance and rounding errors stay bounded as depth grows. Experiments show that the constructed block agrees with a reference update to floating-point precision, while arithmetic replay on synthetic data and seven published benchmark network topologies inherits the reference solver's successes and failures. This separates accurate algorithm execution from accurate causal recovery. In contrast, the ordinary attention models tested under our training budgets do not reliably execute the update or transfer to larger graphs. Whether gradient training can learn an executor in the architecture class of the construction remains open.

---


### 302. [Gaussian Density Splatting Network](https://arxiv.org/abs/2610.10396)

**<font color=#1a73e8>作者：</font>** Miao Shang, Yabin Wang, Xiaopeng Hong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes a novel crowd counting approach, the Gaussian Density Splatting Network (GDSNet). Unlike methods that rely on conventional, grid-based density maps and are sensitive to spatial resolution, GDSNet represents a crowd as a superposition of continuous 2D Gaussian primitives. Our approach is built upon two key contributions. First, we introduce a control-point-based fitting mechanism to structure the prediction of the Gaussian parameters. We design a method to allocate a set of control points that define local regions, from which features are pooled to regress each primitive's parameters. Second, we adapt a differentiable Gaussian Splatting framework to the counting task by parameterizing each primitive with geometric parameters and a scalar density mass. This formulation allows the network to be trained end-to-end via spatial matching of differentiably rendered density maps, naturally providing both local density supervision and global count optimization. Extensive evaluations on four standard benchmarks show GDSNet consistently outperforms the state of the art.

---


### 303. [Cross-Domain Pretraining for Steady-State Neural CFD Surrogates](https://arxiv.org/abs/2610.10398)

**<font color=#1a73e8>作者：</font>** Anthony Zhou, Amir Barati Farimani, Shirley Ho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural surrogates for computational fluid dynamics (CFD) have the potential to greatly enhance engineering innovation through accelerating simulation. However, the primary limitation for neural surrogates is the lack of generalization to geometries and applications beyond the training set, which is significant given the diversity of engineering scenarios. Currently, this is addressed by generating a new dataset for a specific application; however, this requires running costly numerical solvers. In this work, we take a step toward addressing this by studying neural surrogates trained across different geometries, boundary conditions, and fidelities. We find that cross-domain pretraining improves zero- and few-shot performance on held-out datasets relative to both training from scratch and transferring from domain-specific experts. In particular, finetuning a pretrained, cross-domain model can achieve 2-3x lower errors at the same sample size and use 8x fewer samples to achieve the same error, compared to training from scratch. This benefit is architecture agnostic and improves with model size and pretraining dataset diversity. Furthermore, we study how and why cross-domain pretraining works in CFD surrogates, and find that simply pooling steady-state datasets is both sufficient and effective. Given the high cost of generating CFD data, leveraging existing datasets through cross-domain pretraining will likely be a valuable strategy as future surrogates expand to tackle new problems and use cases.

---


### 304. [Rubix: Global Correspondence-Free Point Set Alignment through Assignment Geometry](https://arxiv.org/abs/2610.10408)

**<font color=#1a73e8>作者：</font>** Subhransu S. Bhattacharjee, Dylan Campbell, Rahul Shome  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Procrustes-Wasserstein alignment jointly estimates a matching and rotation without supplied correspondences, but alternating minimization can stop at suboptimal solutions. Rubix solves the equally weighted planar problem globally under squared Euclidean loss. Each matching $\sigma$ of two centered $n$-point sets defines a complex correlation $z_\sigma=\sum_i\bar x_i y_{\sigma(i)}$. Their convex hull is the permutation polygon: supporting vertices give optimal matchings at fixed rotations, and the farthest vertex gives the global alignment. We prove the sharp bound of $n(n-1)$ vertices for $n\ge2$, answering Rote's rotation-assignment open problem. In exact arithmetic, assignment queries recover the polygon in $\mathcal O(n^5)$ operations. Assignment-based bounds extend the approach to three-dimensional rotations and partial matching at a supplied translation through branch-and-bound. On timed MPEG-7 shape pairs, Rubix attains every numerical reference value in 12 ms on average, 50 times faster than a rotation grid at the same accuracy. Its distances improve gravity-aligned matching of real 3D scans, shape retrieval and noisy crystal classification over alternating minimization.

---


### 305. [GraphRectify: Graph-Based Transfer of Adversarial Example Detectors Across Neural Networks](https://arxiv.org/abs/2610.10423)

**<font color=#1a73e8>作者：</font>** Arash Vashagh, Roozbeh Razavi-Far  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial example detectors are often tied to the classifier backbone they were trained on, limiting reuse when the protected model is replaced or upgraded. Directly transferring such detectors across backbones is challenging because different networks generally produce incompatible internal representations. We propose GraphRectify, a graph-based framework for transferring adversarial image detectors across classifier backbones. GraphRectify learns a structured representation of intermediate classifier features and adapts representations from a new backbone to the detector learned on the original model, enabling detector reuse. We evaluate GraphRectify across multiple datasets, backbone architectures, and adversarial attacks, including detector-aware adaptive attacks that jointly target the classifier and detector. Across the complete evaluation matrix, GraphRectify achieves higher aggregate ROC-AUC than training a detector from scratch on the new backbone and the evaluated transfer ablations. The gains are particularly strong for transfers between different backbone families and when sufficient data are available. In contrast, training from scratch remains competitive in the most data-limited settings. These results show that adversarial detection knowledge can transfer effectively across heterogeneous classifier architectures rather than being relearned whenever the protected backbone changes.

---


### 306. [SGF+: Decoupling Gradient Flows for Autoregressive Video Generation](https://arxiv.org/abs/2610.10429)

**<font color=#1a73e8>作者：</font>** Zihan Su, Junhao Zhuang, Yaowei Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video generation requires denoising the current frames while writing their key-value representations as context for future predictions. However, these two roles typically share parameters, and we find that their gradients exhibit distinct patterns and systematic negative alignment, hindering the joint optimization of visual quality and temporal consistency. We introduce Self Gradient Forcing Plus (SGF+), which assigns separate parameters to context writing and denoising while preserving their interaction through causal attention. Both roles are jointly optimized using the original generation objective without auxiliary losses, with context writing supervised through its contribution to future predictions. This simple change improves visual quality and long-horizon consistency over the evaluated baselines in both framewise and chunkwise generation, without additional video training data or a longer training horizon. Trained on only 5s rollouts, SGF+ supports continuous generation for up to 24 hours without long-video fine-tuning. These results highlight role-specific parameterization as an effective design principle for high-quality autoregressive video generation and native long-horizon extrapolation.

---


### 307. [Q-Learning with Scalar Adjoint Matching](https://arxiv.org/abs/2610.10437)

**<font color=#1a73e8>作者：</font>** Yonghoon Dong, Minsung Yoon, Jaehyuk Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow policies capture rich and diverse action distributions, and fine-tuning them with off-policy RL to improve beyond the demonstrations has drawn growing interest. However, fine-tuning a flow policy against a learned value function is not trivial, because the policy generates its action over many flow steps. Adjoint matching offers a principled way to update the flow model itself by propagating value information from the final action back to each flow step, but it requires a vector--Jacobian product through the policy at every step, a cost that grows with the number of flow steps and the policy size. We observe that the batch-averaged velocity Jacobian of pretrained flow policies concentrates on its diagonal. Motivated by this finding, we derive a closed-form scalar adjoint that scales the value gradient at the final action by the flow time, eliminating the per-step vector--Jacobian products. We further find that controlling the critic's value at policy-generated actions is particularly important under the scalar adjoint. Based on these findings, we propose Q-learning with Scalar Adjoint Matching (SQAM), which combines the scalar adjoint with a value penalty at those actions. SQAM's gains concentrate on the four hardest OGBench domains, where its success rate exceeds that of the strongest baseline in each domain by 18 to 35 percentage points. To test whether SQAM extends to large pretrained policies, we also fine-tune a vision-language-action policy on a real bimanual robot. SQAM improves over supervised fine-tuning on all three tasks.

---


### 308. [ECHO: Embodied Camera Observations of Human Object Carrying](https://arxiv.org/abs/2610.10438)

**<font color=#1a73e8>作者：</font>** Xuefei Sun, Lorin Achey, Kali Hamilton 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied and assistive agents must do more than recognize objects: they must reason about where an object belongs given the layout of an environment and the habits of the people who live in it. Progress on this problem has been limited, in part because no dedicated benchmark or dataset exists to define and evaluate it. Existing RGB-D scan datasets reconstruct static rooms without human activity, while human-object-interaction datasets capture motion without a navigable, fully reconstructed scene or a ground-truth notion of an object's natural destination. We introduce contextual object placement as a benchmark task: predicting an object's destination during an observed object-carrying episode. To support this task, we present Embodied Camera observations of Human Object carrying (ECHO), a large-scale synthetic dataset that pairs dense RGB-D scans of indoor scenes with recordings of an embodied human carrying everyday objects to context-appropriate destinations. ECHO is the first publicly available dataset to combine reconstructed scenes, human activity, natural language, and contextual-placement annotations. It comprises 3,805 human-annotated episodes across 159 floors of 115 HM3D scenes, involving 198 distinct objects. Each floor includes a complete RGB-D scan with human-annotated room labels and a surface list. Each episode provides synchronized RGB-D encounter clips; 6-DoF camera, human, and object trajectories; start and destination surfaces; an action caption; and a human-written context: a single sentence describing the inhabitant's routine that implies the destination without naming it. We evaluate contextual object placement using input-masked probes and an end-to-end baseline. Results show that no single input modality is sufficient, highlighting the need to jointly reason over scene structure, human activity, and contextual knowledge.

---


### 309. [Seq-Flow: Efficient Probabilistic Forecasting with Self-Rollout Error Control](https://arxiv.org/abs/2610.10440)

**<font color=#1a73e8>作者：</font>** Yinan Huang, Shitij Govil, Bo Dai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many scientific forecasting tasks require updating a distribution over future trajectories as new observations arrive. Conventional diffusion and flow models generate each forecast from Gaussian noise, often at the cost of many sampling steps. Warm-start methods reuse earlier predictions to reduce this cost, but their models are not trained to perform the forecast update itself, which can compromise quality under few-step sampling. In this work, we introduce Seq-Flow, a conditional flow model whose ODE transports samples from the previous forecast distribution to the updated one. Because successive forecasts often differ only modestly, this transport starts from an informative distribution and can produce accurate updates with few flow evaluations. Recursive reuse also creates a challenge: errors in one forecast become errors in the initial states of subsequent flows. We address this with self-rollout training, in which a moving average copy of the model generates forecasts that initialize later training updates. Unlike self-forcing methods, which reuse generated outputs as conditioning context, Seq-Flow reuses them as the source of the next flow. Experiments On particle-accelerator beam spill forecasting show Seq-Flow reduces CRPS by 65% under a few-NFE sampling budget, while remaining competitive with strong baselines on fluid-dynamics forecasting tasks. Although trained on self-rollouts of at most four updates, Seq-Flow remains accurate over more than 400 consecutive updates. Our code is available at this https URL.

---


### 310. [MORCA: Offline-to-Online Reinforcement Learning for Adaptive Cache Reuse in Video Diffusion Acceleration](https://arxiv.org/abs/2610.10457)

**<font color=#1a73e8>作者：</font>** Yuxiang Xiong, Ruiyan Wang, Wenqiang Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) achieve remarkable performance in video synthesis, but their iterative denoising process suffers from high inference latency. To address this, caching has emerged as an effective acceleration strategy by capitalizing on inter-step redundancy during denoising. Existing dynamic caching methods typically estimate the error that cache reuse would introduce at each denoising step (step error) to guide cache decisions, whereas our concern is how much quality loss cache reuse would cause in the final generated video (terminal error). We show that step error does not directly correspond to terminal error and that latent information helps capture their relationship, thereby informing cache decisions. Moreover, existing threshold-based methods cannot provide precise speedup control, making it difficult to meet practical requirements for user-specified acceleration targets. To address these limitations, we introduce MORCA, a cache scheduling framework trained through offline-to-online reinforcement learning to make latent-aware reuse/recompute decisions under user-specified acceleration targets. Extensive experiments on different video generation models across multiple target acceleration ratios demonstrate that MORCA achieves better generation fidelity than state-of-the-art caching methods under comparable computational budgets. Code is available at this https URL.

---


### 311. [NeuralBES: A Differentiable, Control-Aware Emulator for Scalable Building Energy Modeling](https://arxiv.org/abs/2610.10459)

**<font color=#1a73e8>作者：</font>** Ting-Yu Dai, Takuya Kurihana, Wing Yee Au 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Demand-side flexibility i.e. forecasting, shifting, and curtailing residential energy loads, depends on thermal models trusted across millions of heterogeneous buildings. Existing tools force a hard tradeoff: high-fidelity physics simulators such as EnergyPlus are accurate but sequential and require per-building calibration, while purely data-driven sequence models scale but abandon the physical structure that makes their predictions trustworthy.
We introduce NeuralBES (Building Energy Simulation), a differentiable emulator that resolves this tradeoff by parameterizing a resistance--capacitance (RC) based thermal model with a shared neural encoder: static building metadata such as floor area, vintage, and HVAC type is mapped to physically bounded capacitances, conductances, and equipment coefficients, which become the coefficients of a scalar linear recurrence solved via a log-space parallel scan, and a predictor--corrector loop closes the thermostat--temperature nonlinearity while preserving full-horizon gradient flow. Trained on the ResStock dataset across three climate zones, NeuralBES handles heterogeneous building archetypes, vintages, and climate zones within a single trained encoder, while black-box baselines produce statistically plausible but physically inconsistent trajectories. On the annual full-year rollout, NeuralBES is the only data-conditioned model that is simultaneously physics-valid and accurate to within 4 MAPE points of the strongest raw-error baseline, while operating at roughly an order of magnitude fewer parameters than the transformer and recurrent baselines; among physics-valid baselines at parameter parity it more than halves the MAPE of the grey-box RC alternative.

---


### 312. [How assigned AI use before class shapes active student engagement in class](https://arxiv.org/abs/2610.10463)

**<font color=#1a73e8>作者：</font>** Dan J. Wang, Neelam Modi Jain, Vanessa Burbano 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI learning tools are rapidly entering classrooms, but evidence about whether they help students learn is mixed and rests mostly on test scores. Comparatively less research addresses whether the use of AI changes students' live learning behaviors in class. Here, we report the results of a preregistered field experiment with 759 MBA students enrolled in ten sections of a course, in which each student was randomly assigned two of ten class sessions to prepare for with a purpose-built voice-based AI discussion partner. After two uses of the AI discussion partner, students made about 31% more voluntary contributions in each later class session. Students who used the AI discussion partner more also reported greater comfort speaking up and greater perceived learning, but not greater focus or motivation. These findings suggest that repeated practice with a voice-based AI partner can meaningfully increase students' engagement in class discussion, enhancing a critical intermediate learning outcome.

---


### 313. [Label-free cell counting and viability prediction with brightfield imaging and deep learning](https://arxiv.org/abs/2610.10473)

**<font color=#1a73e8>作者：</font>** Amir Reza Vazifeh, Christian Zeigler, Sornanathan Meyyappan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cell viability assessment is a core requirement in cell culture systems, with critical applications in biopharmaceutical manufacturing and drug development. Conventionally, it is measured by adding membrane-impermeable dyes to a sample (a process called staining), which allows compromised cell membranes to be distinguished from intact ones. However, staining has several limitations: (a) chemical agents can perturb normal cellular processes of the cells being measured, (b) it is often ambiguous to assign viability to individual cells whose membrane integrity is only partially compromised. (c) photobleaching can undermine measurement accuracy over time when using fluorescent stains, and (d) staining cannot be performed in situ or in real time. Here, we show that (1) stained cells captured under brightfield imaging contain sufficient information to distinguish live and dead cells, and (2) cells captured under unstained brightfield imaging exhibit similar image features to their stained counterparts, enabling models trained on stained cells to generalize to unstained ones. We then report the development and validation of ViabiLens, an AI-assisted software for label-free cell viability analysis. The ViabiLens combines a cell detection model for localizing individual cells with a convolutional neural network (CNN) classifier for live/dead prediction, paired with an interactive UMAP-based viewer for visualizing and exploring individual cells across the sample. Evaluated on Chinese Hamster Ovary (CHO) cells spanning a wide range of viability conditions, ViabiLens achieves a mean absolute error of 2.68\% on unstained samples against fluorescence-based reference measurements. We also release a benchmark dataset for label-free cell viability analysis to facilitate future research, available at this https URL.

---


### 314. [Two-Level Softmax Sampling Done Right: Correcting Bias from Size Imbalance and Dispersion](https://arxiv.org/abs/2610.10483)

**<font color=#1a73e8>作者：</font>** Walid Bendada, Guillaume Salha-Galvan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling from a softmax distribution is a fundamental operation in machine learning, but its linear complexity in the number of items makes exact sampling impractical at scale. Two-level softmax (2LS) sampling is a popular alternative enabling sublinear-time sampling. Assuming items are partitioned into clusters, 2LS first samples a cluster and then an item within it. In this paper, we show that, despite its advantages, 2LS introduces systematic and undesirable sampling biases, which arise from misweighting clusters by ignoring both cluster size imbalance and intra-cluster similarity dispersion. We propose two sampling methods, Size-Corrected 2LS (S-2LS) and Size- and Dispersion-Corrected 2LS (SD-2LS), which correct these biases and provide provably better softmax approximations with negligible to non-existent computational overhead. In-depth experiments on five large-scale datasets validate the improved sampling properties of our methods. We recommend their consistent use in place of standard 2LS in future work.

---


### 315. [EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution](https://arxiv.org/abs/2610.10498)

**<font color=#1a73e8>作者：</font>** Python Song, Zhixuan Liang, Kelsey Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Robot foundation models provide strong visuomotor control, yet their performance can degrade when object positions or task instructions change. Further improvements often require post-training on substantial robot data, which can be costly to collect through methods such as teleoperation. Agentic harnesses can adapt around the model, but current self-evolving harnesses use robot trials inefficiently when deciding which code and skill changes to pursue. We introduce EmbodiedRSI, a self-evolving agentic harness that autonomously decides where to explore next and turns the resulting physical interaction into improved code and skills. EmbodiedRSI realizes this through a Fast-Slow Dual-System Architecture, in which competing code and skill hypotheses are maintained in a Hypothesis Graph. Value-of-Information Experiment Selection chooses physical experiments that can distinguish these hypotheses. Their outcomes guide Code-Skill Co-Evolution. The Slow System builds Hierarchical Memory, and Reward-Grounded Memory Learning selects effective memory according to their value for later Fast-System improvement. On RoboCasa365, EmbodiedRSI reaches 77.0% overall success and 71.3% on Composite-Unseen, compared with 40.1% for the best baseline. EmbodiedRSI also reaches 86.8% overall success on LIBERO-Pro. Beyond benchmark performance, EmbodiedRSI transfers zero-shot to real-world robot, achieving 71.3% overall success across multiple challenging tasks.

---


### 316. [Oracle-Efficient and Parameter-Free Agnostic Smoothed Online Learning](https://arxiv.org/abs/2610.10499)

**<font color=#1a73e8>作者：</font>** Sasha Voitovych, Adam Block, Alexander Rakhlin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online learning is an attractive framework in many domains because it permits well-defined learning even when data are dependent or chosen adversarially. This generality, however, comes at a steep price, introducing significant statistical and computational barriers. Recently, smoothed online learning has emerged as a promising framework that interpolates between the fully adversarial and fully stochastic settings by assuming that the conditional law of each covariate has density at most $1/\sigma$ with respect to some fixed base measure $\mu$, and it is known to match the statistical and computational guarantees of classical learning while still allowing for much of the flexibility of online learning. However, existing oracle-efficient algorithms require either (i) sampling access to the base measure $\mu$ or (ii) labels that are perfectly predicted by a fixed hypothesis. Both assumptions limit the applicability of these algorithms, in contrast to statistical learning, where empirical risk minimization (ERM) learns efficiently in the agnostic setting without any knowledge of the data distribution. We show that neither assumption is necessary, giving the first oracle-efficient algorithm that achieves sublinear regret in the agnostic setting without knowledge of $\mu$. Our algorithm, based on Gaussian Follow-The-Perturbed-Leader, is parameter-free: it requires no knowledge of $\mu$, the smoothing parameter $\sigma$, or the horizon $T$, and it achieves regret $\widetilde O(d\sqrt{T/\sigma})$ for binary classes of VC dimension $d$ with a single call to an ERM oracle per round, which is optimal up to a $\sqrt{d}$ factor. En route to establishing the regret bound, we introduce several new techniques that may be of independent interest.

---


### 317. [Your Prompt Should Do More: Effects of Retrieval Instructions in Embedding Models](https://arxiv.org/abs/2610.10508)

**<font color=#1a73e8>作者：</font>** Amanda Myntti, Jenna Kanerva, Veronika Laippala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompted embedding models have recently received increasing attention, particularly for retrieval, where detailed retrieval instructions are provided as part of the retrieval prompt. Several new datasets and studies have examined this setting, showing that the current embedding models often struggle to follow such instructions reliably. In this paper, we study the mechanism of how instructions actually affect the representations of retrieval queries in asymmetric retrieval tasks. We show that models can fail to follow even simple task instructions when query-side distractors are included in the evaluation. We hypothesize that this behavior is driven by the training setup of current embedding models and their evaluation, and show that fine-tuning with added query-side distractors leads to substantial improvements, with minimal effect on other tasks.

---


### 318. [Video-Conditioned Generative Joint 2D-3D Hand Motion Recovery](https://arxiv.org/abs/2610.10512)

**<font color=#1a73e8>作者：</font>** Chen Xu, Yunqi Li, Binbin Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering faithful 3D hand motion from video remains challenging due to frequent occlusions and incomplete visual observations, which make frame-wise pose estimates unreliable and temporally inconsistent. To address this problem, we propose JoHan, a unified generative framework that recovers hand motion directly from video sequences without relying on intermediate per-frame pose predictions. Trained from scratch, our model jointly generates aligned 2D and 3D local hand pose sequences by learning their temporal dynamics and cross-representation correspondence. The generated 2D trajectories exploit direct spatial and temporal cues from the 2D images to guide the following generative 3D motion reconstruction, while the learned motion prior promotes temporal consistency. Their learned 2D-3D correspondence further enables recovery of the hand's global position and orientation relative to the camera. Extensive experiments on challenging benchmarks demonstrate significantly improved accuracy and speed in local hand-pose and camera-space reconstruction. Notably, our method captures much better hand-motion dynamics, producing significantly smoother motion than previous methods while maintaining high per-frame pose accuracy.

---


### 319. [RoboJEPA: Scaling Robotic Latent World Models](https://arxiv.org/abs/2610.10515)

**<font color=#1a73e8>作者：</font>** Artem Zholus, Nicolas Beltran-Velez, Jianhao Yuan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent world models have shown a remarkable ability to predict future states and to plan in the real world. In practice, however, we lack a principled way to estimate how their capabilities scale with model size, data, and compute, an open problem that slows progress in the field. In this work we present RoboJEPA, a world model based on the Joint Embedding Predictive Architecture (JEPA) and trained on a large-scale dataset spanning 12 robotic embodiments. We show that RoboJEPA's imagination error, the error of its latent rollouts, follows a second-order power law in compute, allowing us to predict model quality well beyond the scale at which the law is fit. We further show that downstream robotic planning performance improves predictably with compute, and that imagination error is strongly correlated with it, making it a reliable proxy for real-robot evaluation. Finally, we demonstrate that latent world models can be deployed zero-shot as robotic agents, planning toward a single goal image to solve tasks requiring long-horizon planning on real hardware. We release all model checkpoints together with our training and robot deployment code. To our knowledge, this is the first work to establish scaling laws for multi-embodiment robotic world models trained on real robot data, and RoboJEPA, at 8B parameters, is the largest JEPA predictor model trained to date.

---


### 320. [Why Forget-Only Unlearning Needs Memorization](https://arxiv.org/abs/2610.10519)

**<font color=#1a73e8>作者：</font>** Luka Radić, Vikrant Singhal, Amartya Sanyal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning asks for a deletion algorithm whose output is close to retraining from scratch without the selected forget examples. In this work, we study forget-only unlearning, where the deletion algorithm receives only the trained model and the examples to forget, with no retained data or extra training information. We ask whether forget-only unlearning is always possible. We first show that this depends on the learning method: different datasets can produce the same trained model but require very different outputs after the same examples are removed. Using this observation, we derive lower bounds on how accurately unlearning can match retraining and instantiate them for several standard learning algorithms. We then ask what must be true when forget-only unlearning succeeds. To this end, we derive lower bounds on what an algorithm must memorize about the training data to handle arbitrary deletion requests. For simple threshold learners, the required information can be as large as the entire dataset, even though ordinary training keeps only one boundary point. Overall, our results show that information discarded during ordinary learning may be needed later for deletion, so models designed for forget-only unlearning may need to retain more information than standard training does.

---


### 321. [Distilling Graph Geometry: Knowledge Gap from GNNs to MLPs](https://arxiv.org/abs/2610.10520)

**<font color=#1a73e8>作者：</font>** Zhewei Chen, Hao Zhu, Jiaojiao Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> GNN-to-MLP distillation aims to retain the predictive accuracy of a message-passing teacher while deploying a graph-free MLP at inference. Existing methods mainly transfer node-wise predictions or use confidence-based reweighting, but they do not specify where the student should preserve the teacher's graph-induced geometry. We show that this omission leads to two spectral failure modes in the student's representation space. On sparse graphs, the student suffers from spectral underfit, missing high-energy teacher directions concentrated near boundary regions. On dense graphs, it suffers from spectral overfit, retaining spurious directions that the teacher has collapsed through aggregation. Motivated by an energy-weighted teacher-student alignment objective, we propose Graph Geometry-aware MLP (G^2MLP), a training-time distillation framework guided by Ollivier-Ricci curvature. Curvature identifies where the two spectral errors concentrate and is used to allocate supervision between prediction-level and representation-level alignment. The deployed model remains a standard MLP and requires no graph access at inference. Across node-classification benchmarks, G^2MLP consistently improves over graph-free distillation baselines, reduces the teacher-student rank gap in both regimes, and transfers without architectural changes to Graph Transformer teachers and link prediction.

---


### 322. [GRACE: Generation-aware latent compression for efficient video generation](https://arxiv.org/abs/2610.10524)

**<font color=#1a73e8>作者：</font>** Jiyoung Kim, Paul Hyunbin Cho, Jisu Nam 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Highly compressed video autoencoders offer an effective way to accelerate video diffusion models, as the Diffusion Transformer (DiT) operates on far fewer tokens. However, such autoencoders are challenging to train, since a higher compression ratio degrades reconstruction quality and recovering it requires more channels, which is known to slow the convergence of the DiT. The compressed latent also differs from the one the DiT was trained on, so the pretrained DiT must be either retrained from scratch or adapted at considerable cost. Compressing the autoencoder the DiT was trained with appears to preserve compatibility, yet optimizing it for reconstruction alone still shifts the latent away from the distribution the DiT has learned. To address this, we propose Generation-Aware Latent Compression for Efficient Video Generation (GRACE), a two-stage framework that compresses a pretrained video autoencoder while keeping it compatible with the pretrained DiT. Specifically, we keep a frozen base latent from the pretrained encoder and learn a residual latent for the information lost under stronger compression, while aligning the compressed latent with the pretrained latent in the feature space of the frozen DiT so that the autoencoder is optimized for generation. We then adapt the DiT with lightweight fine-tuning and asymmetric denoising, where the base is denoised ahead of the residual. GRACE reduces the token count of Wan2.1-I2V-14B by 8x and its latency by 11.1x at 480x832x81, while matching the generation quality of the pretrained pipeline before compression on VBench.

---


### 323. [Never Look Back: Understanding Persistence in 3D Object Memory from Egocentric Videos](https://arxiv.org/abs/2610.10538)

**<font color=#1a73e8>作者：</font>** Shravan Chaudhari, William Paul, Suchi Saria 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As we move through the world and carry out everyday tasks, we encounter objects that may become relevant only later. We are capable of recalling where we left something or what was inside a container, even without knowing we would need it later. Here, we study how an embodied assistant can build a similar memory from egocentric videos, by observing a person's day-to-day activities. We present Ledger, a persistent 3D object memory that combines object locations, their histories, and contextual descriptions. It associates observations across the recording and retains objects after they leave the view, including those the person never touches. It clusters each object's observations by resting locations and records a move only after repeated evidence, reducing the effect of localization noise. Short descriptions preserve details such as an object's contents or supporting surface. It saves these records to later answer spatial questions without having to access the original images or video. Our memory raises HD-EPIC accuracy from 29.7% to 42.6%, UCS-Bench accuracy from 33.8% to 38.5% and localizes Ego4D objects with a 0.99 m median error on returned predictions. Our analyses identify complementary roles for temporal persistence, contextual descriptions, and retrieval. Our study on 100 stitched streams of multiple scenes each further exposes failures in both retrieval and construction. Per-scene construction partially recovers the performance lost across scene changes compared to that of single scene streams.

---


### 324. [Tetris3D: 3D Scene Generation With Objects That Fit Together](https://arxiv.org/abs/2610.10539)

**<font color=#1a73e8>作者：</font>** Jaeyeong Kim, Jinhyuk Jang, Jongmin Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose Tetris3D, a generative framework for single-image 3D scene reconstruction that recovers objects which are physically and geometrically coherent as a scene. Existing methods often generate objects independently or couple them implicitly, providing limited guidance for ensuring fine-grained spatial compatibility between neighboring objects that interact with one another. To address this, we explicitly condition the generation of each object on the geometry of surrounding objects and their physical relationships, guiding its shape and pose to remain geometrically and physically plausible within the scene. Moreover, we introduce ComOb, a physics simulation-based dataset of 1.2M scenes featuring physical interactions across diverse object categories, with per-object meshes and pairwise physical relation annotations. Comprehensive experiments on synthetic and realworld scenes show that Tetris3D recovers coherent object shapes and poses even when interacting regions are occluded, and achieves state-of-the-art performance in both generation quality and physical stability.

---


> [!TIP]
> 当前位于：**301-324**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-324**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
