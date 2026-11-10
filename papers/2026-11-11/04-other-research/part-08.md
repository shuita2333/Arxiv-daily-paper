# 📦 其他研究 | 2026年11月11日

> 本类共 **520** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-520](./part-11.md)

---

### 351. [When Should AI Overturn a Human Decision? Controversy at the 2026 World Cup and a $\sqrt{2/π}$ Solution](https://arxiv.org/abs/2611.11819)

**<font color=#1a73e8>作者：</font>** Amir Ali Ahmadi, Parsa Alavi, Radeen Alavi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study how to combine a human binary call (a referee's offside or onside decision) with an AI numerical measurement (VAR's estimate of an attacker's position relative to the offside line). We derive an explicit maximum-likelihood rule that determines when the referee's call should stand and when a conflicting VAR measurement should overturn it. Our model treats the true offside margin as fixed and unknown and assumes independent additive Gaussian errors in the human's perception and the AI measurement. When both errors have zero means and known standard deviations $\sigma_H$ and $\sigma_{AI}$, respectively, the reversal threshold is $\sqrt{2/\pi}\,\sigma^2_{AI}/\sigma_H$. An onside call is overturned precisely when VAR's measured offside margin exceeds this threshold---not merely because VAR places the attacker beyond the offside line. We also derive the rule when either source has a systematic bias. We prove that the maximum-likelihood estimate of the true margin exists and is unique, while the final binary decision requires only a threshold comparison, without computing that estimate numerically. We illustrate the rule through numerical examples and show how to estimate the error parameters from calibration data. The same analysis applies beyond soccer to binary classification problems in which a human call and an AI measurement satisfy the stated model. This paper is intended for educational purposes: we aim to illustrate how undergraduate students and advanced high school students familiar with basic probability and calculus can investigate research questions in AI and its applications.

---


### 352. [Direct Trajectory Optimization for Inference-Time Alignment of Text-to-Image Diffusion Models](https://arxiv.org/abs/2611.11821)

**<font color=#1a73e8>作者：</font>** Huixuan Zhang, Xiaojun Wan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Alignment of text-to-image diffusion models with reward functions is a key challenge in controllable generation. Existing approaches typically rely on optimizing model inputs or fine-tuning denoising networks, which requires computationally expensive backpropagation through large denoising models. In this work, we propose Direct Trajectory Optimization (DTO), a training-free framework that performs alignment by directly optimizing the sampling trajectory of diffusion models. Specifically, DTO treats intermediate denoising scores and sampled noise as the optimization variables, eliminating the need for gradients through the denoising network. To mitigate the out-of-distribution problem, we introduce Reward-Optimized Score Guidance, which interpolates between the optimized scores and the pretrained model predictions to stabilize sampling, while providing a provable theoretical guarantee of reward improvement under constrained distributions. Empirically, DTO improves alignment performance across three diffusion models on two benchmarks, outperforming existing inference-time alignment methods while maintaining high efficiency. These results suggest that trajectory-level optimization is a promising direction for efficient and effective diffusion model alignment.

---


### 353. [ACROSSVAM3.0: Resource-Bounded 4D Scene Construction and Adaptive Surface Association](https://arxiv.org/abs/2611.11825)

**<font color=#1a73e8>作者：</font>** Nan Wu, Hong Yee Hung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Combining video generation, dynamic reconstruction and monocular SLAM requires consistent coordinates, explicit handling of missing outputs and predictable memory use. We present AcrossVAM3.0, an offline system that converts text, images or monocular RGB video into a versioned point representation. Frozen components run sequentially on one GPU; map corrections update cameras, points and trajectories together. The coordination layer adds no neural parameters. Three fresh input-mode runs completed with a maximum sampled task-process-tree GPU footprint of 17.14 GB. In a frozen 16-scene video suite, every scene yielded a 4D reconstruction and 15 yielded a non-empty SLAM map. Strict cross-window matching reduced local surface error but lost long-range track coverage on TAP-Vid-DAVIS. We therefore developed multi-hypothesis adaptive surface chaining (MHAC), which retains several candidate matches and an explicit missing state. After selection on disjoint development data, MHAC improved Average Jaccard over a position-only baseline by 0.1394 on a frozen ten-video holdout (95% bootstrap interval [0.1074,0.1689]). Across 265 RoboTAP videos, the mean paired gain was 0.0610 ([0.0510,0.0715]), with 215 wins, one tie and 49 losses. These results support resource-bounded scene construction and an external tracking gain under the tested protocol. They do not establish metric scale, semantic identity or high-fidelity novel-view rendering.

---


### 354. [KKT-Perturbation-Aware Communication for Fully Distributed Online Convex Optimization with Nonseparable Coupling](https://arxiv.org/abs/2611.11827)

**<font color=#1a73e8>作者：</font>** Zhaoye Pan, Tao Li, Yunjie Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nonseparable costs and coupled constraints in distributed online convex optimization often arise when system performance and operational constraints depend on the joint configuration of all agents and cannot be decomposed into individual contributions. Such nonseparability leads to fully distributed decision-making with challenging partial local information, where each agent evaluates its local primal-dual update using estimated global information via a local belief of the joint action and the shared Lagrange multiplier to be exchanged with neighbors. While the belief consensus established by prior works ensures no-regret learning, exchanging beliefs comprising full-dimensional primal and dual states at every round imposes a communication overhead that scales with both the joint decision dimension and the network size. Existing event-triggered schemes typically activate communication according to state variation or consensus error. Under nonseparable coupling, however, errors of equal magnitude can produce markedly different perturbations after passing through the KKT operator. We therefore propose a randomized KKT-perturbation-aware communication mechanism, where the triggering of each agent's primal and dual communication channels depends on their impact on the KKT operator. The proposed mechanism transfers the adaptive-sampling principle of coordinate descent from allocating computation across decision blocks to allocating communication across information channels: channels with larger estimated perturbations receive greater priority for refresh. Under standard regularity assumptions, the resulting algorithm achieves $O({T}^{2/3})$ expected static regret and $O({T}^{2/3})$ expected cumulative constraint violation. Numerical experiments demonstrate improved learning and constraint-enforcement performance per transmitted bit over belief consensus baselines.

---


### 355. [ROS2MR: Connecting ROS 2 Motion Planning to Mixed-Reality Trajectory Visualization](https://arxiv.org/abs/2611.11830)

**<font color=#1a73e8>作者：</font>** Santiago Berrezueta-Guzman, Habiba-Loai Khalil, Andrei Koshelev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mixed reality (MR) allows users to inspect planned robot motion within their physical surroundings, but displaying trajectories from robotics software requires converting their joint configurations and timing into a format the MR application can play back. This paper presents ROS2MR, an extension of the MR-Robotics LAB platform that converts YAML-serialized ROS 2 joint trajectories, including MoveIt motion plans, into the platform's existing JSON playback format. The converter validates the input, maps arm joints by name, and resamples the trajectory at a nominal rate of 30 Hz, using cubic Hermite interpolation when joint velocities are supplied and linear interpolation otherwise, while binary gripper commands are sampled separately using a zero-order hold. A Python export helper combines sequences of motion plans and gripper states into a single trajectory and checks positional agreement at segment boundaries. The MR application was also adapted for Apple Vision Pro in addition to Meta Quest 3. A technical evaluation showed that the converter preserved the normalized duration and endpoint configurations for dense, sparse, and irregularly timed inputs. With supplied velocities, the position RMSE was approximately 2.91x10^-5 degrees for all sampling patterns; without them, sparse input increased it to 0.85 degrees, and close positional agreement did not guarantee accurate velocity profiles. A pick-and-place sequence retained its open--closed--open gripper order, although off-grid transitions were shifted to the output sampling grid. The resulting file-based pathway enables inspection of ROS-generated trajectories in MR without a live ROS connection.

---


### 356. [End-to-End Joint Training of Super-Resolution and Compression Artifact Removal for Industrial Machine Vision](https://arxiv.org/abs/2611.11831)

**<font color=#1a73e8>作者：</font>** Dang BuiDinh, Sang NguyenQuang, Anh NguyenPhuong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In industrial machine vision, images captured by edge devices are often downsampled and compressed to reduce bandwidth, introducing resolution loss and compression artifacts that severely degrade the performance of downstream tasks, such as defect detection. Existing quality enhancement methods typically apply super-resolution (SR) or compression artifact removal (CAR) independently or in a sequential manner and are largely optimized for human visual fidelity rather than machine perception. This paper proposes an end-to-end quality enhancement framework that integrates SR and CAR with a unified training strategy that optimizes both human-perception and machine-perception objectives. We investigate fixed-weight and uncertainty-based dynamic-weight loss functions to balance reconstruction quality and machine vision task performance. Extensive experiments on PCB Defect, DeepPCB, and NEU-DET datasets show that the proposed jointly trained model generally outperforms standalone and separately trained SR-CAR pipelines. In particular, under severe JPEG compression, our method improves defect detection performance from 0.461 to 0.887 mAP@50 on PCB Defect over sequential SR-CAR baselines, with only a slight reduction in PSNR. These results demonstrate that joint optimization is critical for compression-aware industrial machine vision systems.

---


### 357. [MDA framework: multi-architecture domain adaptation for unsupervised person re-identification](https://arxiv.org/abs/2611.11836)

**<font color=#1a73e8>作者：</font>** Wei Zhang, Peijun Ye, Dihu Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised person re-identification not only faces the challenge of domain gaps, but existing methods also rarely support multiple network architectures. To tackle both issues, this paper proposes a multi-architecture auto-adaptive domain adaptation method: Mamba augmented multi-architecture domain adaptation framework. Specifically, this paper constructs the multi-architecture domain adaptation capability at two levels. At the first level, we propose a composite operator(MDA operator) that encapsulates Mamba as a component for enhancing domain adaptation. At the second level, based on this operator, we propose a Mamba-enhanced multi-architecture Domain Adaptation framework(MDA framework). Comprehensive experiments on person re-identification benchmarks validate the consistency and flexibility of the proposed framework. The MDA framework supports versatile deployment strategies without being confined to a single integration point. Under a single deployment configuration, it surpasses several SOTA methods. Moreover, it demonstrates substantial performance improvements across both CNN and Transformer architectures. When embedded into a CNN backbone, the framework achieves a 10.2% mAP improvement on the adaptation task from CUHK03 to Market-1501. Integrated with a Transformer backbone, it yields a 19.8% mAP improvement on the same task.

---


### 358. [MOOD: Benchmarking Post-Hoc OOD Detection for Materials Property Prediction](https://arxiv.org/abs/2611.11839)

**<font color=#1a73e8>作者：</font>** Shirley X. Yu, Amey P. Pasarkar, Adji Bousso Dieng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Out-of-distribution (OOD) detection is essential for deploying machine learning models in high stakes scientific applications, yet methods that flag OOD inputs without retraining the model have been validated almost exclusively on image classification. We introduce MOOD (Materials Out-of-Distribution Detection), a benchmark for evaluating whether these post-hoc OOD detectors transfer to graph neural networks (GNNs) on materials property prediction. MOOD evaluates 15 post-hoc detectors and 2 supervised diagnostic probes across 4 GNN architectures, 5 MatBench tasks, and 15 physically motivated compositional and structural shifts, yielding 264 evaluation settings and over 13,000 AUROC measurements across three encoder training seeds. Our evaluation reveals three key findings. First, current post-hoc detectors perform near chance; all 15 detectors achieve an AUROC around 0.5. Second, detector failures decompose into two regimes: method bottlenecks and encoder bottlenecks. Method bottlenecks arise when supervised probes can separate in-distribution (ID) from OOD samples but unsupervised detectors fail, meaning that the embeddings contain OOD signal that current detectors do not extract. Encoder bottlenecks arise when even supervised probes fail to separate ID from OOD samples, indicating that the relevant shift is not accessible in the frozen GNN representation. Third, when OOD prediction error exceeds ID error, the AUROC of distance-based and density-based detectors correlates with the size of that gap. Collectively, these findings indicate that reliable OOD detection in scientific domains requires representation learning strategies that explicitly preserve OOD relevant signal, particularly for tasks where current GNN architectures encode no extractable signal at all.

---


### 359. [Aggregation-Induced Calibration Failure in Sum-Based Label Expansion for Multi-Label Facial Expression Recognition: A Diagnostic Study](https://arxiv.org/abs/2611.11843)

**<font color=#1a73e8>作者：</font>** Weihang Yuan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Label-space expansion - predicting a larger joint space and summing back to the original labels - is a natural design for multi-label facial expression recognition, but its failure modes have not been characterised. We evaluate Condition-Aware Label Expansion (CALE) on a self-built dataset (30,240 training images, 3,460 multi-label test images), on seven backbones, and on the public RAF-DB and RAF-ML benchmarks. The central finding is that the aggregation rule, not the representation, decides whether the method works. With a fixed threshold of 0.5, the aggregate score spans 28x across five backbones at 10% of the training data (0.24 to 6.79) and collapses to a 1.9x range at full data, while threshold-free mAP stays within 1.28x over the same backbones, which localises the fault to the summation step. The mechanism is the uncalibrated aggregation rule, which adds the main-branch score to half the sum of the three non-main branches; we verify it by measuring main- and non-main-branch activations. Two plain seven-dimensional sigmoid baselines (BCE, ASL) reach mAP 0.5055 and 0.5175; ASL exceeds three of the five CALE configurations and falls within 0.03 of the best. On single-label FER the gain over a seven-dimensional baseline is nominally significant (paired t-test, p = 0.0436) but does not survive Benjamini-Hochberg correction (p_BH = 0.2055) or a Wilcoxon test (p = 0.1250). We conclude that sum-based label expansion requires threshold calibration at the deployment data scale, or a learned aggregation, before it can support multi-label decisions.

---


### 360. [Severity-Controlled Prediction Sets for Medication Recommendation](https://arxiv.org/abs/2611.11847)

**<font color=#1a73e8>作者：</font>** Yu Gu, Zijun Yu, Chi-Kuang Yeh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medication recommendation is a multi-label prediction task. However, existing prediction-set evaluation and calibration methods rely mainly on exact-overlap metrics and therefore treat all missed medications as equally severe, overlooking how closely the prediction set matches them within the medication hierarchy. To address this, we introduce Conformal Severity Control (CSC), a post-hoc framework for calibrating medication prediction sets under hierarchy-aware mismatch severity. CSC uses the Anatomical Therapeutic Chemical (ATC) hierarchy to quantify mismatch severity and controls patient-level severity without retraining the predictor, supporting both average severity and upper-quantile severity for the highest-severity mismatches. Experiments on MIMIC-IV show that CSC tracks user-specified severity tolerances and shifts prediction sets away from distant mismatches toward exact or close matches.

---


### 361. [Identifiable but Hard to Estimate: Rotation in Equally Spaced Overcomplete ICA](https://arxiv.org/abs/2611.11852)

**<font color=#1a73e8>作者：</font>** Wenjun Xiao, Yinghao Fang, Hanxin Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How many observations are needed to estimate a common rotation in two-dimensional overcomplete independent component analysis? We study equally spaced mixing columns with known source count, common source law, and column norm. For a fixed non-Gaussian fourth-order Gram-Charlier source law, the rotation is identifiable modulo the column spacing. Yet the sample size for fixed relative angular accuracy grows exponentially with the source count. We characterize this sample size, up to absolute constants, by the reciprocal of the squared Hellinger distance between two rotations separated by half the column spacing. An explicit radially weighted phase estimator attains this scale uniformly over the rotation family, using the observation radius to prevent cancellation in the mean of an angular harmonic. We also determine the exact exponential decay rate of single-observation total variation for the same pair. This gives bounds on the sample size exponent; its exact value remains open. Finally, a noisy binary-source example shows how an exact zero line of the observed characteristic function can have an exponentially small normal derivative.

---


### 362. [Doubly-Efficient Private Information Retrieval from Modular Forms](https://arxiv.org/abs/2611.11859)

**<font color=#1a73e8>作者：</font>** Alexandra Henzinger, Seyoon Ragavan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present new information-theoretic protocols for $s$-server, doubly-efficient private information retrieval (PIR) in sublinear server time and one extra bit of space on the servers, for every constant $s \geq 2$. On an $n$-bit database, each of the $s$ PIR servers first builds and stores a preprocessing data structure consisting of $n+1$ bits (which is unique to each server, and after which the server may discard the original database). Then, each server answers a PIR query in time $T_s(n)$, by reading at most $T_s$ bits of its data structure and sending them to the user.
In the two server setting ($s=2$), our PIR protocols achieve $T_2 = n^{0.82}$, matching the server time of the state-of-the-art schemes of Henzinger and Ragavan (EUROCRYPT 2026) while shrinking their storage from $O(n\sqrt{\log n})$ to $n+1$ bits. With $s \geq 3$ servers, our PIR protocols retain the $n+1$ bits of storage and additionally improve on the server time of all prior information-theoretic $s$-server schemes with $n^{1+o(1)}$ storage: for example, achieving $T_3 = n^{0.74}$ and $T_{10} = n^{0.61}$ (previously $n^{0.79}$ and $n^{0.75}$). Asymptotically, as the server count $s$ grows, we shrink the number of servers required to achieve a given server-work exponent from $s^{3.9}$ to $s$.
Our results draw inspiration from matching-vector techniques (Efremenko, STOC 2009), which we generalize to handle degree-two computations in the exponent. Using this generalization, we build doubly-efficient PIR from the new intermediate abstraction of Fourier-sparse cone-delta functions. Then, we construct such Fourier-sparse cone-delta functions via a connection to modular forms and complex analysis: if a Fourier-sparse cone-delta function does not exist, then there exists a modular form which has too many roots, contradicting the valence formula.

---


### 363. [Are UFOs Real? Introducing Unified Factored Organizers](https://arxiv.org/abs/2611.11862)

**<font color=#1a73e8>作者：</font>** Thomas X. Sheppard, Alon Albalak, Joel Lehman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Implicit in much research in deep learning is the assumption that if a network achieves low loss, then it must have learned a good representation of its training data. Recent work by Kumar et al. (2025, arXiv:2505.11581) questions this assumption, arguing that networks trained with conventional gradient descent achieve low loss despite learning fractured entangled representations (FER), leaving related concepts disconnected and unrelated concepts entangled inappropriately. Kumar et al. further show that dramatically better representations are possible: a network evolved through an open-ended, human-in-the-loop process learned unified factored representations (UFR) that capture the regularities of the domain far better than a counterpart with nearly identical outputs trained with conventional gradient descent. Inspired by UFR, this paper introduces unified factored organizers (UFOs), networks trained to model regularities in the representations of other networks. A network can then be trained both to achieve low loss on its task objective and to align its representations with the model learned by the UFO. Networks trained with UFOs are shown to learn qualitatively superior representations in an image-regression domain where representations are easily interpretable. To provide quantitative evidence for the impact of UFOs on representation learning, a transformer is trained with and without UFO regularization to grok a modular arithmetic problem set. When combined with weight decay, UFOs can reduce the number of transformer training steps needed to grok by more than 10x relative to weight decay alone. Without weight decay, UFOs can reduce the number of transformer training steps needed to grok by more than 100x relative to an unregularized baseline. If UFOs are real, they suggest a new paradigm where loss functions themselves are trained to learn an effective model of good representation.

---


### 364. [Can Hindsight Critics Guide Delayed Actors?](https://arxiv.org/abs/2611.11863)

**<font color=#1a73e8>作者：</font>** Francisco M. López, Francisco Cruz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sensory delays create temporal misalignments between the state of the environment and the observations available to an agent, turning Markovian control problems into partially observable ones. In this work, we inquire whether such misalignments can be mitigated during training by using hindsight to recover aligned state-action transitions. We introduce Hindsight Critics, an asymmetric extension of the Soft Actor-Critic for reinforcement learning under partial observability. The critics are trained on hindsight-aligned transitions whereas the actor learns from the resulting privileged value estimates despite only having access to delayed observations. Comparisons against delay-aware and unaware baselines on the DelayBench suite show that Hindsight Critics can partially compensate for observation delays without requiring modifications to the agent's observations during deployment.

---


### 365. [Beyond Head Importance: Collective Computation in Video Transformers](https://arxiv.org/abs/2611.11875)

**<font color=#1a73e8>作者：</font>** Yi Yang, Siyuan Liu, Bingbing Nie  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Attention heads in video Transformers vary greatly in functional importance. Understanding their contributions requires examining not only which heads are important, but also how they participate in collective computation within the network. We study this collective computation from two perspectives: the downstream use of head outputs and the composition of interactions across layers. Ablation analyses of four video Transformers show that high-importance heads identified on a single task also support other video understanding tasks and help preserve the representational structure that distinguishes different videos. Representational responses to head ablation correlate weakly with head importance after the attention module, but more strongly after the MLP in the same block. Adapting this downstream processing through MLP-only fine-tuning further improves the use of lower-importance head outputs. Meanwhile, through composition across layers, sets of heads with shorter spatiotemporal attention distances support stronger perturbation responses at distant tokens than sets with longer distances. Their joint ablation causes even greater performance loss than ablating equally sized sets of high-importance heads, revealing collective contributions not fully captured by individual importance rankings. These findings highlight collective computation as a key perspective for understanding attention head function: functional contributions depend on both how head outputs are used downstream and how local interactions compose across layers.

---


### 366. [Tropical Gaussian Anticoncentration: Optimal Instance-Dependent Bounds for Online Learning in Extensive-Form Games](https://arxiv.org/abs/2611.11877)

**<font color=#1a73e8>作者：</font>** Ashkan Soleymani, Zhiyuan Fan, Lillian J. Ratliff 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the minimax regret of full-information online decision making in extensive-form games. For prediction with expert advice, the optimal regret is $\Theta(\sqrt{T\log K})$, where $K$ is the number of experts, or equivalently, the number of normal-form actions. For treeplex strategy spaces, existing efficient algorithms, including KOMWU and online mirror descent with the weight-one dilated entropy regularizer, achieve regret $\mathcal{O}(\sqrt{T\log|\mathcal{V}|})$, where $\mathcal{V}$ is the set of reduced normal-form strategies. We prove that this logarithmic dependence is minimax optimal in the worst-case full-information reward model. The main difficulty is that pure plans in a treeplex are not independent experts: their rewards are correlated through the recursive structure of decisions and observations. To capture this correlation, we introduce tropical Gaussian formulae, recursive Gaussian expressions built from maxima and normalized sums which preserve the variance. The index count of such a formula matches the number of reduced normal-form continuation plans in the corresponding subtree. Our main analytic result shows that every log-balanced tropical Gaussian formula with index count $N$ has Gaussian width $\Omega(\sqrt{\log N})$. While a direct approach struggles to recover this lower bound, our proof uses a spherical entropy profile to measure scale-dependent separation among the Gaussian directions, and then applies Turán's theorem and Sudakov minoration to obtain the width lower bound. Applying this result to treeplexes gives an oblivious hard distribution with valid transition outcome and Rademacher terminal rewards, establishing a regret lower bound of $\Omega(\sqrt{T\log|\mathcal{V}|})$. This matches known upper bounds up to universal constants and shows that the DilEnt/KOMWU dependence on the reduced normal-form complexity is unavoidable.

---


### 367. [When Does Physics Beat Data? Data-Efficient Traffic State Estimation with Amortized PINNs](https://arxiv.org/abs/2611.11881)

**<font color=#1a73e8>作者：</font>** Anna Lazareva, Alexander Tarakanov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic state estimation (TSE) reconstructs traffic density at unmonitored locations from a sparse set of sensors. Data-driven models work well when sensors are dense but degrade sharply as coverage thins. We show that imposing the Lighthill-Whitham-Richards conservation law as a physics-informed prior makes TSE more data-efficient. On four real corridors (NGSIM, I-80, PeMS04, PeMS08), physics-informed estimators generalise to held-out sensors where data-driven models, including classical and deep kriging, overfit the observed ones. On the two shock-rich corridors the effect is a clear crossover: as more sensors are held out, data-driven models collapse while the physics-informed estimator degrades gracefully, leading the no-physics network by about 26-38% at 85-90% held out and the strongest classical kriging by about 10-21% at 90%. A matched smoothness prior does not reproduce the gain, and an extended Kalman filter on the same LWR model is outperformed on the shock corridors, so the advantage comes from how the conservation law is imposed. Finally, one loss-conditional PINN removes the per-corridor loss-weight search, matching a 20-point search at about 5x lower cost.

---


### 368. [How Many Candidates Does a One-Step World Model Need? A Random-Codebook Account of Nearest-of-m Training on Frozen DINO Tokens](https://arxiv.org/abs/2611.11887)

**<font color=#1a73e8>作者：</font>** Yong Hwi Song, Keon Myung Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One-step stochastic world models avoid the mode averaging of deterministic feature predictors without the tens of network evaluations per step that diffusion and flow matching require. The simplest such objective is nearest-of-m matching (conditional implicit maximum likelihood estimation, IMLE): draw m candidate futures and pull only the one closest to the observed outcome. Recent work conjectures that a small m suffices for feature-space world models and that a strictly proper energy score should replace the hard minimum. We test both claims with one-step world models on frozen DINOv2/v3 patch tokens, using benchmarks whose futures can be enumerated. Under mode-like uncertainty, nearest-of-m with m=16 covers the enumerated futures better than 50-step flow matching (at about 1/30 of its latency), one-step flow generators and an energy-score generator at matched parameter counts, and its rollouts stay on the token manifold where flow rollouts drift. One quantity governs the choice of m: the nearest-of-m objective is the expected distortion of a random codebook of m draws from the generator. This view yields three predictions, recorded before the corresponding runs: (i) memorization of the realized outcome in contexts that never repeat, whose strength is governed by the codebook's miss distortion I(m) rather than its miss probability, and which an energy-score generator does not escape by raising m; (ii) a flattening of mode probabilities with m, matching a known optimum within 0.01; and (iii) under-dispersion on continuous high-dimensional outcomes, which bounds the method on real robot video. Per-step matching on self-rollouts cuts long-horizon error by a third on a stochastic Push-T variant; an ablation separates its manifold and coverage benefits. Planning success does not improve despite accurate risk estimates, a negative result we report with its diagnosis.

---


### 369. [Training Vision Transformers to Focus: Emergence of Spatial Attention Head Specialization](https://arxiv.org/abs/2611.11890)

**<font color=#1a73e8>作者：</font>** Yuji Nozawa, Yu-Chieh Lin, Youyang Ng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning in Vision Transformer models, such as DINO, enables robust visual perception without requiring labeled data by leveraging large-scale image datasets. However, these models lack a focusing mechanism during training, resulting in perceptual representations that are often ambiguous or overly similar. In this work, we introduce two visual focusing loss functions designed to establish correspondence between the model's attention and specific regions within images. Specifically, we leverage the multi-head attention mechanism within the model to selectively steer the model's focus, leading to the emergence of spatial attention head specialization, characterized by diverse and spatially focused perceptual capabilities without requiring annotations. Through both qualitative and quantitative evaluations, we demonstrate that our method substantially increases the spatial selectivity and diversity of attention heads, improving both interpretability and performance on dense prediction tasks such as zero-shot image segmentation.

---


### 370. [A Large-Scale Dataset for Cross-Lingual Multi-Jurisdiction Patent Drafting from Patent Cooperation Treaty Applications](https://arxiv.org/abs/2611.11891)

**<font color=#1a73e8>作者：</font>** Trung Phuong Le, Hirofumi Nonaka, Koji Marusaki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Securing patent protection across countries requires drafting claims separately for each national patent office, in the relevant language and according to its legal and stylistic conventions. Patent claims can therefore differ across languages and jurisdictions because of translation, target-office drafting practices, and prosecution-stage changes. We formulate cross-lingual patent drafting as generating plausible candidate claim sets for a specified target language, jurisdiction, and prosecution stage from a source claim set in another language. The task models jurisdiction- and stage-specific transformations beyond content-preserving translation. We construct a large-scale Japanese-English dataset by linking Japan Patent Office (JPO) and United States Patent and Trademark Office (USPTO) records through 884,179 Patent Cooperation Treaty (PCT)-derived patent families. Across six released configurations, these families yield 4,067,168 directional claim-set instances; four core configurations form the main benchmark. Commercial machine translation and zero- and few-shot prompting capture part of the task, while supervised adaptation provides the strongest overall baseline, showing that task-specific patterns can be learned from linked cross-jurisdictional claim sets.

---


### 371. [Developing a Street View Imagery Processing Pipeline for Building-Level Vacant House Assessment](https://arxiv.org/abs/2611.11893)

**<font color=#1a73e8>作者：</font>** Dongjoon Park, Sunjae Lee, Jung Woo Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Street view imagery (SVI) is widely used to audit urban environments remotely. Automated assessments usually assume that each image shows the target building clearly. In practice, an image may lack task-relevant evidence or show a neighboring house. If this goes unchecked, a model's score cannot show whether it judged the correct building. We present a reproducible SVI processing pipeline that makes image suitability and target identity explicit and checkable. We apply it to vacant house assessment in South Korea, using 10,311 images of 1,609 detached-house parcels. Task-suitability filtering adapts its criteria to image composition and administrative area. This keeps coverage even across areas. While keeping as many images as a single uniform filter, our filtering left 101 more parcels with a usable image. Target-house alignment identifies the parcel's house from camera metadata and parcel boundaries. It needs no building footprints or additional training. Alignment matched human labels for 85.6% of images, compared with 79.8% for the best simple rule. In vacancy classification, filtering and alignment raised AUROC from 0.684 to 0.719, but marking a different house in the same image still gave 0.709. Grad-CAM showed that the model often looked at areas outside the target house. Image suitability, target identification, and model evidence are therefore separate problems, and scores alone do not resolve them. Recording which images were used and which house was selected lets reviewers verify each assessment and can support human virtual audits.

---


### 372. [Disagreement-Aware Distribution Matching Distillation for Few-Step Diffusion Models](https://arxiv.org/abs/2611.11898)

**<font color=#1a73e8>作者：</font>** Zikai Zhou, Zhengpeng Xie, Shitong Shao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Distribution Matching Distillation~(DMD) enables strong few-step diffusion generation by matching the student distribution to a pretrained teacher. Existing improvements to DMD often augment its supervision or modify its optimization machinery. We ask a complementary question: \emph{can DMD diagnose its own updates using signals already produced during training?} DMD inherently computes the discrepancy between a pretrained teacher and a fake model tracking the student distribution, but conventionally uses it primarily to determine the distribution matching direction. We find that the magnitude of this teacher--fake disagreement provides additional diagnostic information. Across extensive experiments, large disagreement in the high-noise regime consistently coincides with substantially higher-energy DMD updates. This reveals a dual role of disagreement: it determines not only \emph{where} the student should move, but also provides an intrinsic signal of \emph{how aggressively} the update should be applied. Based on this observation, we introduce Disagreement-Aware Distribution Matching Distillation (DA-DMD), which activates only in the high-noise regime and continuously modulates the update strength according to teacher--fake disagreement. DA-DMD reuses quantities already available during DMD training and requires no additional model, evaluator, or inference-time modification. We show that it exactly recovers vanilla DMD outside the selected region, reduces update energy only through selected samples, and exhibits redescending influence under extreme disagreement. Across multiple diffusion backbones, DA-DMD consistently improves few-step generation at the same inference cost. On SD3.5-L, DA-DMD improves HPSv2 from $28.23$ to $30.93$, while achieving a $64.4\%$ average win rate over DMD2.

---


### 373. [On the Global Convergence of Stochastic Adam for Physics-Informed Neural Networks](https://arxiv.org/abs/2611.11905)

**<font color=#1a73e8>作者：</font>** Yihang Gao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Adam optimizer is widely used to train neural networks with highly nonlinear and nonconvex objective functions. Remarkably, Adam often drives the empirical training loss nearly to zero. This phenomenon has been partially explained by neural tangent kernel (NTK) analyses of gradient descent (GD) and stochastic gradient descent (SGD). However, analyzing Adam presents additional challenges. Its first-moment momentum couples stochastic gradients across iterations, while its adaptive second-moment preconditioner depends on the same stochastic gradient used in the update. In this paper, we establish linear convergence guarantees for Adam in training sufficiently wide two-layer neural networks with either full-batch or minibatch gradients. For full-batch Adam, we construct a Lyapunov function to control the effect of historical momentum. For minibatch Adam, our analysis builds on an exact virtual-iterate representation, a conditional analysis of the dependence between stochastic gradients and adaptive preconditioners, and uniform concentration bounds for the second-moment estimates. We prove geometric decay of the empirical loss for full-batch Adam and geometric decay in restricted expectation on a high-probability event for minibatch Adam. Beyond regression, we extend our convergence analysis to physics-informed neural networks (PINNs) for solving the Poisson equation, where differential operators and separate sampling of interior and boundary points introduce additional challenges. We establish analogous global convergence guarantees for both deterministic and stochastic Adam under explicit conditions on network width and Adam's parameters, characterizing the effects of minibatch size on convergence. These results help bridge the gap between Adam's empirical success and its theoretical understanding, providing sharper convergence guarantees for PINNs than existing analyses.

---


### 374. [RBA: A Read-out Basis Adapter for Parameter-Efficient Interactive OCTA Vessel Segmentation with SEEM](https://arxiv.org/abs/2611.11906)

**<font color=#1a73e8>作者：</font>** Jaafar M. Al-Ghabban, Mohammad Reza Mohammadi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retinal disease monitoring with optical coherence tomography angiography (OCTA) relies on segmentation of vessels and the foveal avascular zone (FAZ). Promptable models such as SEEM (Segment Everything Everywhere All at Once) allow click-based refinement, but without adaptation SEEM segments thin vessels poorly and needs many clicks. Fully fine-tuning its 342 million parameters on a few hundred images is costly and risks overfitting, and parameter-efficient methods such as low-rank adaptation (LoRA) usually adapt only the encoder. Yet SEEM reads every candidate mask from one feature map at quarter resolution, too coarse for vessels one to three pixels wide. This study introduces the Read-out Basis Adapter (RBA), whose read-out branch generates 32 image-specific basis maps at half resolution. Each candidate accesses them through its own vector and a zero-initialised projection, so the model starts exactly as SEEM. The encoder branch, a standard rank-1 LoRA, supplies the information needed to tell arteries from veins. RBA adds 0.47 million trainable parameters. Under simulated error-driven clicks, with the ground truth used only to place them, RBA outperforms LoRA, Conv-LoRA andAdaptFormer on OCTA-500 3mmlarge vessels. Averaged over three seeds, it reaches an intersection over union (IoU) of 85.16% and a Dice score of 91.93%, 2.90 and 1.72 percentage points above Conv-LoRA. On the 6 mm subset, one run gives margins of 4.35 and 2.76 points. The gain extends to arteries, veins and ROSE-O but not to the FAZ. In SEEM, adaptation capacity pays more at the mask read-out than in the encoder.

---


### 375. [LO-World: Unified BEV Latent Modeling for Joint 4D Occupancy and LiDAR Forecasting](https://arxiv.org/abs/2611.11912)

**<font color=#1a73e8>作者：</font>** Zhimin Liao, Ping Wei, Kai Mao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR point clouds and 3D semantic occupancy represent two distinct modalities capturing fine-grained metric geometry and dense volumetric semantics, respectively, holding natural potential for mutual complementarity. However, existing world models typically forecast these modalities independently or cascade them heuristically, missing the opportunity for reciprocal cross-modal regularization. To address this, we propose \textbf{LO-World}, a unified 4D world model that forecasts both modalities within a shared BEV latent space. This single-stream formulation enables dense semantics and metric geometry to mutually reinforce each other, while eliminating multi-pipeline redundancy. Specifically, LO-World couples an efficient hybrid range-voxel autoencoder with a flow-matching generator that caches historical context to reduce iterative sampling latency. Extensive experiments demonstrate that LO-World outperforms prior state-of-the-art baselines, improving occupancy forecasting IoU by 10.9% and reducing LiDAR Chamfer Distance by 30.1%. Meanwhile, it sustains a real-time throughput exceeding $25$~FPS on a single RTX 4090. Our code is available at this https URL.

---


### 376. [CHORD: Multi-resolution Compression for Multimodal Time Series](https://arxiv.org/abs/2611.11913)

**<font color=#1a73e8>作者：</font>** Bibhus Luitel, Payal Mohapatra, Subrata Biswas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wearables, mobile devices, and IoT platforms generate multimodal time-series data continuously and at scale, making efficient storage and transfer a primary concern. The same recordings are reused after collection by many downstream models, often at different temporal resolutions, so a compressed representation should be small, useful across resolutions, and produced at a bit rate known in advance. Prior work meets parts of this: symbolic and error-bounded compressors reconstruct accurately but fix resolution at compression time, learned codecs target one signal domain, and discrete tokenizers reconstruct without accounting for rate. We introduce CHORD, a coarse-to-fine compressor for heterogeneous multimodal time series. A residual cascade orders each payload from broad to fine temporal scales and synthesizes corrections through learned shapelet-inspired atoms. A shared pathway supplies a reusable synthesis basis across modalities, while private pathways retain capacity for sensor-specific morphology. Finite scalar quantization fixes the bit width of every modality and scale, so payload size is known before encoding, and scale dropout trains each coarse-to-fine prefix to be a valid reconstruction operating point. Across seven wearable-sensing and forecasting benchmarks, CHORD stays within 0.62 points of uncompressed classification accuracy on average at the 8x target, the smallest gap of any compressed method, with all resolutions decoded from one payload.

---


### 377. [CRAFT-GBM: Selecting Best Features for Gradient-Boosted Machine Learning](https://arxiv.org/abs/2611.11914)

**<font color=#1a73e8>作者：</font>** Basil Kuok, Yi Zhou, Yao Xuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feature subsampling is used to accelerate gradient-boosted trees, yet standard approaches fix the feature count in advance and largely ignore the split-gain evidence accumulated during training. We introduce CRAFT-GBM (Confidence-Ranked Adaptive Feature Tracking), a native LightGBM extension that uses this evidence to adapt which---and, by default, how many---features are searched each boosting round. CRAFT-GBM transforms root-split gains into bounded observations and constructs joint time-uniform bounds valid under adaptive, non-stationary training histories. In its default endogenous mode, after initialization, CRAFT-GBM retains exactly the features that cannot yet be ruled out as best, letting the selected feature-set size $K_t$ emerge from training history rather than a pre-specified fraction. With probability at least $1-\delta$, every feature with the largest expected gain is retained jointly across all rounds after initialization. When a feature fraction $f$ is specified instead, CRAFT-GBM ranks features by their interval point estimates and provides an approximate top-$K$ guarantee for feature budget $K_f$. We implement CRAFT-GBM within LightGBM while preserving its native feature-bundling representation, and evaluate it across 14 public and synthetic dataset families and four noise-augmented settings. In the fully endogenous setting, CRAFT-GBM reduces per-fit training time by 39.74\% with 1.04\% lower test loss in the geometric mean across all 18 RQ1 experiments. Under pre-specified feature fraction $f$, Exogenous CRAFT-GBM also yields aggregate training-time reductions up to 13.52 percentage points larger than random feature subsampling, with no increase in aggregate test loss relative to full-feature LightGBM. Accumulated training evidence can thus support adaptive feature search with statistical guarantees while retaining the practical advantages of native gradient boosting.

---


### 378. [LBSNet: Lightweight Brain State Modeling via Learnable Spectral Prototypes for EEG-Based Fatigue Detection](https://arxiv.org/abs/2611.11916)

**<font color=#1a73e8>作者：</font>** Kun Jia, Zhenyu Cao, Hanlin Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG-based fatigue detection requires modeling spectral information across bands and its temporal variation. Recent methods combine multi-band modeling with adaptive temporal processing, yet how spectral structure across bands should influence the contribution of each temporal interval remains insufficiently explored. We propose LBSNet, a lightweight network that uses prototype-based brain-state modeling to link local spectral structure with temporal aggregation. LBSNet extracts compact multi-band features through band-specific temporal convolution, shared spatial projections, and cross-band recalibration. Within each window, relative spectral activity is encoded as a normalized descriptor and softly matched to learnable spectral prototypes. Prototype assignments and learned prototype importance jointly determine temporal weights for power aggregation, allowing the spectral pattern of each window to guide its contribution to the prediction. Subject-independent experiments on SEED-VIG and SADT show that LBSNet outperforms seven baselines while maintaining low computational cost. Ablation and visualization analyses support prototype-guided temporal weighting, while the learned prototypes reveal a gradual redistribution of relative cross-band spectral states with increasing fatigue. The code is publicly available at this https URL.

---


### 379. [Text Alone Predicts Which Classes a Segmentation Readout Keeps](https://arxiv.org/abs/2611.11926)

**<font color=#1a73e8>作者：</font>** David Yan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An open-vocabulary segmentation readout silently loses a class deployed beyond its training categories. It still emits masks with high confidence, but the class never wins a single pixel. The training loss falls anyway, and mIoU can even rise while classes die. We show that which classes collapse is written in the class-name list alone. Before any image is seen, we rank each class's collapse risk from its text similarity to the training vocabulary alone. The ranking holds at AUROC 0.69-0.96 across nine model families, twelve backbones and eight pretraining recipes. Two further families, measured only after the predictions were written down, land in the same band. What the list writes, it can rewrite. With identical images and a class's counterpart moved in or out of the training list, retraining flips that class's gain over the frozen baseline by 21 IoU points; swapping in unrelated names changes nothing. We find a vocabulary-distance mechanism behind the collapse. Collapsed classes lose every vote to near-name neighbors, but in the frozen features they survive. Turning down the readout's amplitude, or stopping training early, brings them back, up to +16 points, without retraining; trained with its amplitude held down, the readout never collapses.

---


### 380. [Scale-Consistent Monocular Fisheye Visual Odometry via Spherical Bundle Adjustment-Guided Unsupervised Depth Learning](https://arxiv.org/abs/2611.11934)

**<font color=#1a73e8>作者：</font>** Wanhui Luo, Hongbo Zhao, Yi Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The wide field of view of fisheye cameras and the simplicity of a monocular setup make monocular fisheye visual odometry (VO) attractive for robotic localization and mapping. Nevertheless, scale drift remains a major challenge over long trajectories. Unsupervised depth learning can help to mitigate this issue, but the pronounced distortion of fisheye images poses challenges for accurate depth estimation. This article presents S$^2$D-FVO, a monocular fisheye VO framework integrating spherical bundle adjustment (SBA)-guided unsupervised depth learning to improve scale consistency and depth estimation accuracy. Given that pixel reprojection residuals do not uniformly reflect angular deviations between viewing rays and that the first-order linearization of a scalar angular reprojection residual is insensitive to perturbations along one tangent direction, SBA employs tangent-space angular reprojection residuals derived from the spherical logarithmic map. These residuals retain sensitivity along both tangent directions, with their norms equal to the corresponding scalar angular residuals. A median depth-based scale regularization term is further integrated into SBA to constrain the reconstruction scale. Building on these formulations, SBA replaces the pose estimation network during unsupervised depth learning, providing more reliable relative poses for view synthesis. In turn, depth estimates from the well-trained depth estimation network provide scale references for SBA, improving scale consistency while allowing individual 3-D landmark positions to be refined. Extensive experiments conducted on multiple public datasets, as well as two newly collected large-scale datasets, demonstrate that the proposed framework outperforms representative existing approaches in both depth and trajectory estimation accuracy and is applicable to different camera models.

---


### 381. [Constrained Variational Policy Optimization for Hybrid Action Spaces](https://arxiv.org/abs/2611.11936)

**<font color=#1a73e8>作者：</font>** Shuchang Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constrained reinforcement learning in hybrid action spaces must coordinate discrete modes and mode-conditioned continuous controls under long-horizon cost constraints. Existing constrained hybrid-action methods typically optimize factorized policies directly in parameter space, whereas Constrained Variational Policy Optimization (CVPO) separates nonparametric improvement from parametric projection in its original continuous-action formulation. We introduce Hybrid Constrained Variational Policy Optimization (H-CVPO), extending this variational framework to hybrid action spaces. Under boundedness and strict feasibility, its constrained E-step has zero duality gap and, when the dual optimum is attained at positive temperature, yields a closed-form joint target distribution over hybrid actions through exponential reward-cost reweighting. Using the exact hybrid KL decomposition, we formulate a factorized M-step that fits both policy components to this target under separate discrete and conditional-continuous trust regions. For exact E/M updates, we prove fixed-reference surrogate improvement and conditional reward-cost bounds with a sufficient feasibility-margin condition. For approximate updates, we establish the existence of a dual minimizer under continuity on a compact domain and use residual-based admissibility to determine whether to project the target. Ablations identify cost-aware reweighting as an important contributor to constraint control. Extensive experiments in simulated hybrid-control environments show that H-CVPO achieves favorable reward-cost trade-offs compared with hybrid-action baselines.

---


### 382. [Attention Is Only as Good as Its Witnesses: When Higher-Order Layers Help, and When They Do Not](https://arxiv.org/abs/2611.11937)

**<font color=#1a73e8>作者：</font>** Mostafa 'Neo' Mohsenvand  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers stop learning graph search as graphs grow, and learn the card game SET only after many distinct questions, although attention can represent both. We read these failures, and the uneven record of higher-order attention, from what a layer sums over: each layer we study computes the partition function of a family of witnesses and reads it at a temperature. Two laws follow. The depth law is a known result of logic, which we state for these layers: L layers over two-step walks reach exactly 2^L - 1 steps, just as a logical statement with L nested clauses of the form "there is a vertex such that" sees exactly that far. We build a construction that reaches this far, checked in Lean, and, when vertices carry no names, no such network reaches further. The size law is the cost of reading at a temperature, which logic does not have: existence is read correctly at every size, in the worst case, if and only if inverse temperature times margin is at least the logarithm of the number of candidates. Layers built on these laws, and on two principles that we test, learn where Transformers fail. One propagator layer trained on 49-vertex graphs answers every question at every search depth on 250-vertex graphs. Given the modulus 3, exponential Newton computes the softmax of 2-simplicial attention over pairs exactly in 3^d n operations for d clocks; with six clocks it learns SET from as few deals as 2-simplicial attention and transfers from 8- to 20-card tables. On CLRS-30 without hints, a 186,000-parameter block of OR-join and power-mean channels matches (within half a point) or beats a model of at least 73 million parameters on 9 of 12 graph tasks of the official test set, and on 8 of 12 with freshly drawn test graphs. The same account explains where pair layers did not help and where parallel layers must loop.

---


### 383. [Decision Aware Origin-Destination Demand Estimation with Structurally Constrained Data](https://arxiv.org/abs/2611.11946)

**<font color=#1a73e8>作者：</font>** Xianzhe Wang, Yueyue Fan, Johannes Royset  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Origin-destination (OD) demand plays an important role in transportation system design and management applications. Conventional OD estimation methods typically judge estimation quality based on how estimated demand aligns with observed traffic data and historical demand patterns. We argue that data alignment alone is insufficient; how errors in OD estimates influence downstream decision quality should also be considered. This paper develops a decision aware OD demand estimation framework that leverages structurally constrained traffic data to characterize an admissible demand region, within which we identify OD estimates that would lead to least regret in the downstream decision. Therefore, our OD estimates are both data-consistent and decision-relevant. Methodologically, we approximate the admissible demand region induced by physical network constraints through a geometric representation, which regularizes the search over feasible OD estimates. Within this regularized region, we use a convex surrogate of downstream regret to obtain a tractable decision aware optimization problem. Numerical experiments show that the proposed framework consistently reduces decision regret relative to conventional estimation benchmarks, demonstrating the value of aligning OD demand estimation with downstream decision quality.

---


### 384. [UltraVoxelGS: Voxel-First Feed-Forward Gaussian Splatting for 3D Ultrasound Reconstruction](https://arxiv.org/abs/2611.11951)

**<font color=#1a73e8>作者：</font>** Yue Wang, Haoxin Chen, Xiaoqing Guo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present UltraVoxelGS, a 3D ultrasound reconstruction method that achieves both fast reconstruction and physically faithful rendering for the first time, bringing live spatial feedback during 2D ultrasound scanning within reach. This is made possible by a feed-forward design that predicts a complete Gaussian scene representation from posed ultrasound images directly, entirely bypassing the per-scene optimization bottleneck that has confined prior methods to offline use. Realising such feed-forward prediction in this setting is non-trivial: unlike natural images, ultrasound slices share at most one-dimensional intersections and exhibit view-dependent appearance due to acoustic propagation and attenuation, violating the dense overlap and photometric consistency assumed by existing feed-forward Gaussian methods. Hence, to achieve fast reconstruction, we introduce a feed-forward voxel-to-Gaussian pass that decouples representation size from input count by lifting all posed slices into a fixed-size voxel support and predicting Gaussian parameters directly. For faithful rendering, we propose ultrasound-aware appearance rendering strategy factorize reflection from cumulative attenuation during training and exploit appearance continuity among spatially adjacent slices for efficient Render-time Appearance Adaptation. On both real-world and simulated datasets, UltraVoxelGS achieves best PSNR/SSIM compared with per-scene optimization baselines while reducing inference from 10-20 minutes to approximately 10 seconds (over 35 times faster) and scales to sequences exceeding 1,000 frames. Code is available at this https URL.

---


### 385. [Shaping Useful Noise: Energy Distributions Predict Visual Pretraining Quality](https://arxiv.org/abs/2611.11962)

**<font color=#1a73e8>作者：</font>** Ching Lam Choi, Antonio Torralba, Phillip Isola 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic data can scale visual pretraining, but current selection criteria only partially explain which datasets train strong representations. We propose using the energy profile of a dataset--the distribution of log-probability levels it occupies under a normalised real-image density model--as an audit and curation principle for synthetic data. To operationalise this view, we introduce Energy-Level Distribution Distance (ELD), which compares real and synthetic energy distributions. Real images span sparse high-likelihood scenes and dense low-likelihood textures, so useful synthetic data should cover this energy range rather than collapse to likely but low-variation samples. Across diverse synthetic datasets, ELD exposes mismatches missed by FID and predicts pretraining performance beyond FID, LPIPS variation, and feature-space recall, including across CNN and ViT self-supervised settings. We then use ELD to resample and mix synthetic sources, matching the real-image energy histogram while preserving diversity and improving downstream transfer.

---


### 386. [3R-Adapter: Retrieval, Rewiring, and Refinement for Efficient Adaptation of 3D Reconstruction Model](https://arxiv.org/abs/2611.11964)

**<font color=#1a73e8>作者：</font>** Zixiang Ai, Zhenyu Cui, Xu Zou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D reconstruction models have demonstrated strong generalization under large-scale pre-training, yet they struggle in long-tail scenarios such as low-light reconstruction, joint human-scene reconstruction, and test-time adaptation. We observe relational attention structure collapse, manifested as the failure of cross-view correspondences, as a primary cause of these limitations. While adaptation offers a practical way to bridge this gap, existing parameter-efficient fine-tuning (PEFT) approaches mainly perform channel-wise feature adjustment and lack mechanisms to explicitly adapt relational structures, leaving correspondence failures unresolved. In this work, we formulate adaptation of 3D reconstruction models as a problem of correspondence recovery under domain shift and propose 3R-Adapter, a PEFT paradigm for long-tail 3D reconstruction scenarios. Our method consists of three components: Deformable Retrieval for task-adaptive relation candidate retrieval, Relational Rewiring for reconstructing cross-view relational structures, and Consistency Refinement for injecting the rewired relations into stable predictions. Extensive experiments on low-light reconstruction, joint human-scene reconstruction, and test-time adaptation demonstrate that our approach significantly improves robustness over existing PEFT methods while maintaining efficient lightweight adaptation. Our code is released at this https URL.

---


### 387. [Pairwise distortion distribution for compression and quantization](https://arxiv.org/abs/2611.11967)

**<font color=#1a73e8>作者：</font>** Carl Nuzman, Jeongmin Chae, Kursat Rasim Mestav 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Choosing the latent dimension is a critical challenge in data compression, where conventional hyperparameter optimization is costly and ad hoc. Intrinsic dimension provides a good alternative, which connects information-theoretic notions such as Renyi information dimension (RID) to rate-distortion dimension and random codebook compression. In this work, we introduce the pairwise distortion distribution (PDD) and its asymptotic limit, pairwise dimension (PD), which generalize the correlation integral to general distortion measures. We show that PD bounds RID, and PDD provides a lower bound for random codebook quantization performance, which can guide a practical use for compression, quantization, and dimensionality reduction applications.

---


### 388. [ShiftCache: Fast and Exact Indel Effect Prediction by Reusing Shifted Reference Encodings](https://arxiv.org/abs/2611.11976)

**<font color=#1a73e8>作者：</font>** Sina Barazandeh, Arth Banka, Jose Lugo-Martinez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequence-to-function models such as AlphaGenome and Borzoi read up to a megabase of DNA and score a genetic variant by comparing their predictions for the reference and alternate sequences. Insertions and deletions (indels) are costly to score, because an indel usually shifts the unchanged DNA after it onto a different pooling grid, which prevents direct reuse of the reference's encoder activations. The AlphaGenome Atlas scored more than 100 million indels with three full model passes each, although the DNA after an indel matches the reference shifted by the indel's length. We present ShiftCache, an exact reuse system that encodes each shifted reference once and shares it among all variants scored in the same window with the same shift. ShiftCache copies every encoder output a variant can reuse and recomputes the rest in batched tiles. On held-out AlphaGenome windows shared by many indels, in strict fp32 on one A6000, ShiftCache is 3.5 to 6.5$\times$ faster than deduplicated dense execution and 1.6 to 2.7$\times$ faster than our adaptation of layer-by-layer reuse to indels. It is 3.5 to 4.1$\times$ faster than dense reimplementations of two published analyses with Borzoi and AlphaGenome, and 2.6$\times$ faster than dense execution with Enformer. Scoring each variant in its own centered 131 kb window makes ShiftCache only 1.36$\times$ faster than deduplicated dense execution, and highly diverse insertion lengths or many dispersed edits can make it slower than layer-by-layer reuse or dense execution. For encoders that meet our conditions, ShiftCache computes the same predictions as dense execution in exact arithmetic. On an A6000, every checked output of the default AlphaGenome and Borzoi runs matches dense execution within an absolute and relative tolerance of $10^{-5}$. With larger tile batches, with Enformer or on an H100, a small fraction of values exceeds this tolerance.

---


### 389. [MixRoute: Rethinking Single-Distribution Training for Generalizable Neural Routing](https://arxiv.org/abs/2611.11977)

**<font color=#1a73e8>作者：</font>** Hang Yi, Ziwei Huang, Yining Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Combinatorial Optimization (NCO) is a promising paradigm for solving routing problems, yet its generalization across diverse data distributions remains a critical bottleneck. Existing methods typically tackle cross-distribution generalization through complex multi-distribution training or intricate meta-learning schemes, implicitly presuming that single-distribution training yields a weak zero-shot baseline. In this paper, we demonstrate that the potential of single-distribution training has been substantially underestimated and can be unlocked by a simple architectural inductive bias: Mix Normalization. To approach this, we first construct a comprehensive benchmark spanning three representative routing problems and 179 fine-grained datasets, capturing diverse shifts in node coordinates, customer demands, capacity and time windows. Building on this benchmark, we propose MixRoute, a neural framework that adaptively combines normalization statistics at different granularities to mitigate varying distribution shifts. Trained exclusively on uniform distributions, MixRoute generalizes effectively to a wide range of unseen distributions without any distribution-specific adaptation. Extensive experiments demonstrate that MixRoute consistently achieves state-of-the-art zero-shot generalization. Our work revisits normalization as a parsimonious alternative for zero-shot generalization against complex training-adaptation schemes.

---


### 390. [HyInv Technical Report](https://arxiv.org/abs/2611.11997)

**<font color=#1a73e8>作者：</font>** Haowei Lin, Cai Zhou, Xiangxin Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse folding designs amino-acid sequences for a given protein backbone, and screening needs many candidates that are both diverse and well folded. We present HyInv, a 1.96-million-parameter backbone-conditioned graph network with an encoder-decoder architecture, trained by Hyra 2.0, the research agent developed by our team: pretrained with random-order autoregressive sequence modeling, followed by structure-reward reinforcement learning. At inference, a grouped draft-and-rewrite sampler that uses separate draft and rewrite temperatures improves refolding TM-score at matched diversity. An optimized implementation with BF16 numerics designs 128 sequences for a 402-residue backbone in 50.6 ms on a single NVIDIA H20 GPU, about 52 times faster than the reference sampler, and an exact FP32 path that returns the reference sequences is 8.7 times faster. Across five benchmark datasets and seven dataset-predictor combinations, HyInv reaches a higher average scTM than all ten external baselines at comparable or higher sequence diversity, with large margins over ProteinMPNN and ProteinZero V2. The same default setting supports de novo backbones, pocket-constrained libraries, enzyme redesign with the catalytic site kept, and loop redesign. We have released our code and model at this https URL.

---


### 391. [Reward-Estimated Hypergradient for Bilevel Reinforcement Learning with Black-Box Follower](https://arxiv.org/abs/2611.11998)

**<font color=#1a73e8>作者：</font>** Shigeki Kusaka, Mikoto Kudo, Takumi Tanabe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hypergradient (HG) methods for bilevel reinforcement learning (RL) typically assume a white-box follower whose reward is known. In practice, however, the leader rarely knows the follower's reward function and can only observe its trajectories. We address this black-box setting and propose Reward-Estimated Hypergradients (RE-HG), which recovers the follower's reward from these trajectories via inverse RL (IRL). Yet IRL identifies the reward only up to potential-based shaping, a transformation that leaves the follower's behavior unchanged but biases the HG. We prove that, for linear rewards, this bias cancels when IRL estimates are aggregated across sufficiently diverse dynamics, which the leader's own updates naturally supply. To handle finite samples, RE-HG truncates small eigenvalues of the aggregated feature covariance, restoring the identifiable subspace and stabilizing the estimation. Experiments show that RE-HG estimates gradients aligned with a white-box Oracle and achieves comparable performance; empirically, the truncation also suppresses HG explosions, letting RE-HG avoid local optima that trap the Oracle in sharp reward landscapes.

---


### 392. [Scalable Bayesian Optimization for Efficient Exploration of Moire Patterns](https://arxiv.org/abs/2611.12010)

**<font color=#1a73e8>作者：</font>** Panagiotis Krokidas, Christos Lazaridis, Vassilis Sioros 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large materials design spaces often contain rare high-performing configurations that are difficult to identify through trial-and-error exploration or purely representative machine-learning (ML) sampling. In this work, we present FruBO, a flexible Bayesian Optimization framework for accelerating the discovery of optimal configurations in computationally demanding materials design problems. As a case study, we investigate multilayer Moiré patterns generated by the superposition of six rotated hexagonal lattices, where the objective is to identify the rotational conformation that maximizes pore-size uniformity, quantified using the Jain fairness index. The resulting benchmark contains 600,000 unique configurations and exhibits a highly skewed objective distribution, making the global optimum difficult to locate by random sampling. We compare random exploration, Gaussian Process-based Bayesian Optimization, and Bayesian Optimization using a lightweight CatBoost surrogate with committee-based uncertainty estimation. Random sampling identifies the global optimum only after 533,012 evaluations, requiring approximately 31 hours, while Gaussian Process-based BO becomes impractical due to GPU memory exhaustion after 290 acquired samples. In contrast, FruBO with CatBoost identifies the global optimum after 1,470 acquired samples and approximately 1.15 hours. These results demonstrate that scalable surrogate models can substantially improve the feasibility and efficiency of BO in large nanomaterials design spaces.

---


### 393. [HIST3R: Decomposing and Rectifying State Updates with History for Streaming 3D Reconstruction](https://arxiv.org/abs/2611.12011)

**<font color=#1a73e8>作者：</font>** Kenneth Yang, Yu-Chiang Frank Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming 3D reconstruction with recurrent states enables long-video scene understanding under bounded memory, but turns reconstruction into a state-evolution problem: each incoming frame updates a compact scene memory on which all subsequent predictions depend, so unreliable updates overwrite historical context and accumulate into long-horizon geometric drift. We analyze CUT3R-style recurrent updates through a direction--magnitude decomposition, in which the magnitude sets the update gain, i.e., how strongly an observation is written into the state, and the direction encodes the geometric intent, i.e., where the update drives the state. This decomposition provides a unified view of CUT3R and its variants, revealing that existing training-free extensions perform magnitude-only control: they can attenuate an unreliable update but cannot correct its direction. We propose HIST3R, a training-free framework built on CUT3R that controls both components using history. HIST3R rectifies the update direction using locally consistent historical states, and modulates the update magnitude according to the visual discrepancy between the current observation and its history, suppressing redundant updates while preserving complementary evidence. Across camera pose estimation, 3D reconstruction, and video depth estimation, HIST3R consistently improves long-horizon performance while retaining the memory footprint and inference speed of CUT3R. With 1000 input frames, it reduces ATE by 23.87% on ScanNet and 33.65% on TUM-Dynamics relative to the strongest competing method; with 500 frames, it improves median reconstruction accuracy over the strongest CUT3R-based variant by 56.52% on 7-Scenes and 33.96% on NRGBD.

---


### 394. [A generalized transition framework for identifying reduction domains in non-binary constituency parsing](https://arxiv.org/abs/2611.12020)

**<font color=#1a73e8>作者：</font>** Jungyeul Park, Zihao Huang, Eunkyul Leah Jo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Direct non-binary constituency parsing must identify an ordered sequence of children at each phrase-level reduction. We extend our earlier delimiter-guided bottom-up construction to a common calculus for top-down, in-order, and bottom-up parsing. At reduction, the rightmost delimiter marks the left boundary, the nonterminal marker supplies the mother label, and the completed items in the delimited segment determine the children and arity. We use a stack invariant to prove soundness and completeness and derive the exact length of the static oracle's action sequence. A projection-and-lifting theorem shows that each delimiter-guided system and its canonical counterpart generate the same set of trees under both the structural and grammar-licensed transition relations. In controlled experiments on PTB and CTB, the delimiter-guided parsers achieve similar labeled accuracy to their canonical counterparts across all traversal orders. For bottom-up parsing, delimiter guidance reduces the number of action classes and increases the number of supervised decisions per tree.

---


### 395. [TIRAD: Text-guided Image Residual Learning for Generalist Anomaly Detection](https://arxiv.org/abs/2611.12023)

**<font color=#1a73e8>作者：</font>** Seongsu Lee, Seunghyun Oh, Seungjae Moon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent anomaly detection studies have shown that residual features, which model the discrepancy between normal and abnormal patterns, provide strong generalization to anomalies unseen during training. However, existing residual-based approaches mainly rely on visual discrepancies derived from image representations, while semantic discrepancies that can be explicitly expressed through language remain largely underexplored. To address this problem, we propose TIRAD, Text-guided Image Residual Learning for Generalist Anomaly Detection, a multimodal residual learning framework that defines the discrepancy between textual representations of normal and abnormal states as a Text Residual Feature and uses it to guide the Image Residual Feature. Specifically, a Text Fusion Module converts patch-level text residuals into a gate that modulates the image residual of each patch. The gate retains the visual discrepancies that the text residual identifies as defect-related and attenuates the others, leading to more discriminative anomaly representations. Extensive experiments on industrial benchmarks and industrial-to-medical transfer demonstrate that the proposed method outperforms existing image-centric residual learning methods.

---


### 396. [FocusBranch: Combinatorial Branch-and-Bound for $\ell_0$ Neural Network Robustness Verification](https://arxiv.org/abs/2611.12024)

**<font color=#1a73e8>作者：</font>** Renwei Deng, Yang He, Linyi Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Verifying the local robustness of neural networks under $\ell_0$ perturbations is inherently combinatorial, as it must reason over all sparse subsets of $\epsilon$ perturbed pixels. This paper presents FocusBranch, a combinatorial branch-and-bound framework for $\ell_0$ robustness verification. The key insight is to make the $\ell_0$-ball decomposable and branchable using a node abstraction, which consists of a focus pixel set $\mathcal{S}$ and a level $l$, permitting at most $\epsilon-l$ pixels outside $\mathcal{S}$. This abstraction unifies two branching mechanisms: concrete nodes branch through upper shadows to fix additional perturbed locations, while super nodes branch through covering designs to cover many perturbation cases with fewer child nodes. FocusBranch proves node safety by concretizing linear relaxations over node-constrained $\ell_0$-balls and recursively branches on unknown nodes. Rather than relying on a fixed verification plan, it samples nodes across levels to estimate safe rates and costs, then selects a starting level and branching strategy predicted to minimize verification time. Experiments on fully connected and convolutional classifiers for MNIST, Fashion-MNIST, and CIFAR-10 show that FocusBranch verifies $\ell_0$ robustness effectively across architectures and outperforms state-of-the-art verifiers. The code is available at: this https URL.

---


### 397. [Single Image Super-Resolution via Semantic Prompt and Cross-Modal Training on Content Area](https://arxiv.org/abs/2611.12025)

**<font color=#1a73e8>作者：</font>** Xiao Tan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Enhancing image quality through super-resolution is crucial in image and video processing. While contemporary deep learning models, such as CNNs and Transformers, excel in pixel-level enhancements, they often overlook the rich semantic context within images. To address this, we introduce a novel approach that synergizes pixel intensity with semantic information for superior detail recovery. Our method involves extracting semantic data, including textual descriptors and spatial positioning, and encoding this information. We also present a Cross-Modal Feature Fusion module for generating semantic feature maps via multimodal training, and a Prompt Traction Head to augment the backbone network with semantic insights, thereby refining image details. Our empirical results across various datasets validate the superiority of our approach.

---


### 398. [MambaPD: Bidirectional Selective State Space Model for Parkinson's Disease Detection from Resting-State EEG](https://arxiv.org/abs/2611.12026)

**<font color=#1a73e8>作者：</font>** Ayesha Zulfiqar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Typical diagnosis of Parkinson's disease (PD) occurs only after significant dopaminergic loss, while resting-state EEG abnormalities like alpha slowing and reduced coherence occur earlier. While many published EEG-based PD detectors claim accuracy greater than 95%, many use epoch-level splits which leak subject identity. I introduce MambaPD, a bidirectional selective state space model for resting-state EEG-based PD detection, blending the channel mixing, patch tokenization and bidirectional Mamba encoder. It is compared with four baselines (TCN, BiLSTM with attention, EEGNet and a patch Transformer) in two public datasets (UNM, SanDiego) using subject-independent 5-fold cross-validation (checkpoints were selected on the held-out fold, so absolute estimates are optimistic). On UNM the accuracy is between 0.67 and 0.71, and MambaPD (0.714) is not statistically distinguishable from the Transformer (0.715), and TCN (0.708), with the highest sensitivity (0.82), while the lowest specificity (0.52). For the smaller SanDiego cohort, accuracy is in the range of 0.60 to 0.70, with the highest scores (0.703) from TCN and the lowest (0.601) from EEGNet, while MambaPD scores 0.631, with the lowest specificity (0.46) among the five models. The differences among the models on UNM are minor compared to the differences among folds. I report the whole pipeline, per-fold results, and the shortcomings of the protocol.

---


### 399. [Scale-Invariant Empirical-Bayes Laplace Approximation for ReLU Networks](https://arxiv.org/abs/2611.12031)

**<font color=#1a73e8>作者：</font>** Shivam Pal, Piyush Rai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> ReLU networks are well-known to have continuous scale symmetries; infinitely many reparameterized weight vectors that represent the same function. Dinh et al. (2017) have shown that, by reparameterizing, the geometry of the loss landscape (e.g., curvature) of these networks can be changed arbitrarily without affecting the underlying function. Thus, any quantity that depends on the network's geometry should be defined with care. In this paper, we show that the Empirical Bayes (EB) Laplace's approximation is not well-defined for ReLU networks, mainly due to Hessian dependence in computing the marginal likelihood, which is not invariant under ReLU scale symmetries. Thus, we can get different prior precisions, posterior covariances, and predictive uncertainties for a network having identical predictions under ReLU scaling. We define family of prior precision fields indexed by $\gamma$ and introduce $\gamma$-canonicalization, which first converts the network to its canonical representation by balancing the ratio of incoming to outgoing weights, and then fits the Empirical Bayes (EB) Laplace to the canonical representation. This procedure is equivalent to transporting the isotropic Gaussian prior from the canonical representation to the original coordinates, by producing a ReLU-scale-compatible precision field. This makes the marginal likelihood invariant under ReLU scaling, while allowing $\gamma$ to be selected by maximizing the marginal likelihood. The resulting EB Laplace approximation is well-defined on ReLU scale-equivalence classes and yields consistent prior precision selection and predictive uncertainties across functionally identical parameterizations.

---


### 400. [SAFE-Hair: Scalp-Anchored Fields for Exportable Single-View Hair Reconstruction](https://arxiv.org/abs/2611.12037)

**<font color=#1a73e8>作者：</font>** Yucheng Wang, Zedong Wang, Yuetong Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-view 3D hair reconstruction has progressed rapidly, but many methods optimize for visual plausibility rather than producing strand assets that can be directly used in grooming, editing, or simulation pipelines. We propose SAFE-Hair, a framework that reconstructs explicit strand grooms from a single portrait by decoding hair from persistent follicles in a canonical scalp-UV domain. Given a fitted template head, SAFE-Hair projects self-supervised image features onto the scalp, uses a conditional Rectified Flow model to generate latent scalp fields, and decodes occupancy, segment directions, length allocation, and total length at a fixed set of scalp follicles. This representation enforces scalp-rooted strand identities by construction and enables direct export with follicle IDs and guide-family metadata. We further introduce attachment, collision, and bending priors to improve geometric validity without per-subject test-time optimization. To evaluate both reconstruction fidelity and asset usability, we introduce HairBench-3D, a benchmark built from public 3D hair assets with standardized alignment, rendering, resampling, and metrics for geometry, direction consistency, invisible-region completion, silhouette agreement, and collision. SAFE-Hair improves Chamfer distance from 3.74 mm to 3.28 mm, F-score from 77.9 to 81.7, invisible-region F-score from 66.1 to 69.8, and penetration ratio from 4.8% to 3.9% over the strongest baseline.

---


> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-520](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
