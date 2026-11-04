# 📦 其他研究 | 2026年11月05日

> 本类共 **280** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-280](./part-06.md)

---

### 201. [Attending to Memory Writes Reduces Seed Variability in Recurrent Length Generalization](https://arxiv.org/abs/2611.04902)

**<font color=#1a73e8>作者：</font>** Sungwoo Goo, Hwi-yeol Yun, Sangkeun Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent memory requires learning useful updates, but attention added to assist learning can also compromise length generalization. We study bounded delta attention: causal attention over uncorrected update proposals whose bounded correction enters the recurrent update. Its implementation in TraceRelay combines additive phase recurrence with attention computed before a parallel scan. On prefix-supervised modulo-5, trained at lengths 1--40, three findings characterize its behavior at length 80. First, upper delta attention attains $70.81\pm8.26$% accuracy across seven seeds, versus $69.21\pm22.42$% for the local-attention recurrent baseline (mean $\pm$ sample SD): a 63.2% reduction in SD with a similar mean. Upper state attention also reduces variation, reaching $74.75\pm6.24$%, so this benefit is not unique to update-level attention. Disabling the upper delta correction retains $70.62\pm8.60$%. Second, blocking gradients at the delta-attention inputs changes accuracy to $65.25\pm12.40$% in the matched seven-seed comparison, increasing SD by 50.2%. It also delays a 99% validation threshold on average among the same six seeds that reach it; the 95% threshold is reached earlier on average with input-gradient blocking across all seven seeds. Third, lower delta attention exhibits substantially less extrapolation degradation than lower state attention: 62.60% versus 19.40%, against a 71.06% baseline. Removing its correction reduces accuracy to 22.56%; its advantage over lower state attention also persists under input-gradient blocking. These observations motivate bounded update-level attention as a recurrent learning scaffold, combining reduced seed variation with less severe degradation in a placement where state attention fails.

---


### 202. [Cool Graphs: Active Property Search Towards Quantum Nano-Refrigerators](https://arxiv.org/abs/2611.04907)

**<font color=#1a73e8>作者：</font>** Sofia Blyufer, Amir Kleiner, Uri Peskin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nanodevices that absorb energy from their thermal environment can act as quantum refrigerators. Finding suitable configurations, however, is a needle-in-a-haystack problem: the many-body state space scales exponentially with the size of the device, where each candidate configuration requires an expensive quantum-chemical computation. We introduce a search framework that couples a Graph Variational Autoencoder (GVAE) with an uncertainty-driven Active Learning (AL) loop to efficiently identify energy-absorbing configurations in electronic junctions with a 2D "working material" to be optimized. The GVAE maps physical parameters - site energies, coupling matrices, temperature - into a smooth latent space that distinguishes cooling from dissipative parameter regimes, achieving a classification discriminability of $0.920 \pm 0.004$ on held-out configurations and $0.895 \pm 0.010$ on unseen extrapolation topologies. An AL pipeline based on Monte Carlo dropout then targets the decision boundary, iteratively selecting the candidates where the model is least certain for simulation. Over 32 AL cycles, the uncertainty-driven strategy discovers energy absorbing systems at rates consistently exceeding the random baseline across all tested topologies (where only 1.9-8.4% of configurations exhibit the desired property), providing a data-efficient pathway for navigating a combinatorically large design space. The learned latent space organizes configurations along physically interpretable axes, that correlate with underlying microscopic model parameters. This hints at the existence of "cooling coordinates" - low-dimensional, physically interpretable quantities separating cooling from non-cooling regimes. Our framework, thus, paves a new way towards effective cooling of nanoscale electronic information processing devices, to reduce the environmental footprint of high performance computing.

---


### 203. [MiCaDe: Online LiDAR-Camera Miscalibration Change Detection for Autonomous Driving](https://arxiv.org/abs/2611.04912)

**<font color=#1a73e8>作者：</font>** Carlo Sgaravatti, Riccardo Pieroni, Matteo Corno 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable multi-sensor perception in autonomous vehicles requires accurate calibration between cameras and LiDAR. However, calibration drift is often unavoidable in long-term deployments: vibrations, thermal effects, and minor mechanical shocks may alter the relative pose between sensors, leading to systematic errors in downstream fusion tasks. We propose MiCaDe (Miscalibration Change Detection), an online solution detecting when the extrinsic LiDAR-camera calibration parameters are no longer accurate by means of sequential change detection. MiCaDe requires no calibration targets, or modification of the perception stack, providing low false-alarm rates with negligible computational overhead. Our key insight is that 3D and 2D bounding boxes produced by standard object detectors should remain geometrically consistent under correct calibration. By matching cross-modal detections, we derive geometric consistency metrics that serve as sensitive indicators of extrinsic drift. These metrics are aggregated into fixed-size batches and scored against a reference distribution, producing a likelihood stream that is monitored by a Change Point Model (CPM). Crucially, the CPM accumulates statistical evidence over time, enabling detection of subtle drifts that would otherwise go unnoticed. Experiments on multiple long-sequence datasets and on a real-world dataset with physically induced miscalibration confirm reliable detection under diverse conditions. Code available at: this https URL.

---


### 204. [EP-LVMQA: Evidence-Preserving Coarse-to-Fine Localization for Low-Quality Long Video Moment Question Answering](https://arxiv.org/abs/2611.04913)

**<font color=#1a73e8>作者：</font>** Guoning Chen, Zhexun Hu, Yifan Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long instructional videos are increasingly used in medical education, industrial training, and procedural knowledge transfer, yet their evidence is often incomplete or unreliable: subtitles may be missing, ASR noisy, OCR sparse, and decisive actions briefly shown without narration. Existing VideoQA systems typically return labels or free-form text, making answer support difficult to inspect. We study Long Video Moment Question Answering (LVMQA), where a system returns timestamped answer-supporting evidence. We propose EP-LVMQA, an evidence-preserving coarse-to-fine framework comprising an Uncertainty-Aware Multimodal Evidence Timeline, a Coarse Evidence Planner, and an Evidence-Conditioned Fine Localizer. An evidence card transfers planner scores, matched cues, source-confidence proxies, modality-specific evidence, neighboring context, and a temporal prior between the latter two modules. On MedVidQA, EP-LVMQA achieves 26.1 R1@0.5 and 31.8 mIoU, improving the strongest non-ours results by 6.3 and 5.1 points. It raises Suff.@2 and Ver.@2 to 25.4 and 22.6, gains of 9.5 and 8.8 points. Under matched low-quality perturbations, average relative degradation is reduced from the strongest non-ours value of 14.6% to 11.1%. On Ego4D-NLQ and QVHighlights, EP-LVMQA remains broadly comparable to established task-specific localization methods.

---


### 205. [Modulating Merging Strengths via Joint Loss Estimation for LoRA-based Continual Learning](https://arxiv.org/abs/2611.04931)

**<font color=#1a73e8>作者：</font>** Kun Gu, De Cheng, Zhipeng Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning (CL) aims to adapt models to new tasks while preserving previously learned knowledge. Recently, Low-Rank Adaptation (LoRA), a representative Parameter-Efficient Fine-Tuning (PEFT) method, has gained increasing attention in CL due to its efficiency and scalability. Several LoRA-based merging methods maintain a single inference model by scaling the newly learned LoRA update with one coefficient and merging it into the previous weights after each task. However, they usually control the whole update with a shared scalar factor, although different update elements may affect previous and current tasks in different ways. To address this issue, we propose Merging Strength Modulation via Joint Loss Estimation (M2LE). It consists of Hessian Information-guided Adaptive Merging (HIM) and Task Simulation Perturbation for Merging (TSP). Instead of searching for a global merge coefficient, HIM directly solves for the target merged update under a joint objective over previous and current tasks. Solving this objective gives an analytic solution that naturally takes the form of element-wise modulation over the current task LoRA update. To improve the stability of the learned update under subsequent merging, we introduce TSP which simulates different tasks interference. Experiments on multiple benchmarks show that M2LE consistently outperforms existing PEFT-based continual learning methods. Code is available at this https URL.

---


### 206. [VISTA: Vision-Language Integrated Semantic Triage Architecture for Online Face Clustering in Long Videos](https://arxiv.org/abs/2611.04932)

**<font color=#1a73e8>作者：</font>** Jiashu Liao, Joanne Garde-Hansen, Sanjay Sharma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clustering faces by identity in long, continuous video streams is a challenging task that serves as a building block for human-centric video analysis. The majority of existing face clustering models are offline, i.e., they assume the entire data to be available altogether. In many practical scenarios, however, the entire data is either unavailable or poses computational challenges to be processed in its entirety. A handful of online methods that exist rely on geometric visual features and simple thresholding techniques, which fail when the faces exhibit significant appearance variations in long, unconstrained videos. To this end, we present VISTA, the first vision language framework for online face clustering in long videos. VISTA leverages semantic reasoning in a controlled, uncertainty aware fashion to maintain both high cluster purity and long range identity continuity. This makes it robust to the variations in illumination, pose, and costume changes that the faces and characters exhibit in long real world videos. Extensive experiments on the VPCD benchmark dataset (with 15 full episodes from The Big Bang Theory [2007-2019], Buffy the Vampire Slayer [1997-2003], and Sherlock [2010-2017]) demonstrate that VISTA achieves a robust precision and recall balance, consistently improving over the strongest matched online unsupervised baseline (COFC) under identical detector, embeddings, and evaluation protocol. Code and supplementary material: this https URL.

---


### 207. [Robustness Verification against Patch Attacks via Group-Lasso Semidefinite Relaxation](https://arxiv.org/abs/2611.04939)

**<font color=#1a73e8>作者：</font>** Yukina Nakagawa, Takami Sato, Ken Kobayashi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robustness verification is essential for ensuring the safety and security of neural networks, but current methods focus heavily on
norm-ball attacks, which do not adequately model typical real-world threats that present physical perturbations, known as patch attacks. A naive approach requires computationally prohibitive enumeration of all possible patch positions. To address the challenge, we propose a novel neural network verification method specialized to the patch-attack threat. Instead of enumerating patch locations, we first model the patch attack with group-wise sparsity and formulate its verification methods as a mixed-integer semidefinite program (MISDP) by applying SDP relaxation to the neural network. We then propose three relaxations, including Group-Lasso relaxation, that remove the integer variables while preserving the sparse, group-wise structure of the original attack, enabling substantially efficient verification. Our empirical analysis demonstrates that the proposed relaxations require less than 3% of the computation time of the original MISDP, while the Group-Lasso relaxation incurs only a 0.34\% average increase in the objective value over the original formulation. Furthermore, Group-Lasso achieves a verified rate of 91%, compared with under 70% for prior methods.

---


### 208. [HTNN-MSC: Multi-view Subspace Clustering with a Hyperbolic Tangent Tensor Low-Rank Surrogate](https://arxiv.org/abs/2611.04940)

**<font color=#1a73e8>作者：</font>** Yiwen Dou, Yiqiang Ding  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-order dependencies among views can be modeled by tensor singular value decomposition (t-SVD) in multi-view subspace clustering. However, the tensor nuclear norm often used with this framework assigns the same asymptotic marginal penalty to singular values of different magnitudes, which may excessively shrink dominant components that encode cluster structure. We propose HTNN-MSC, which replaces this norm with a bounded hyperbolic tangent tensor rank surrogate. The surrogate is strictly concave on the positive half-axis and has a Lipschitz continuous derivative. Its marginal penalty decreases as singular values grow. We develop an alternating direction method of multipliers solver in which the tensor subproblem decomposes into scalar frequency-domain shrinkage problems. Safeguarded multi-start Newton iterations and candidate-objective comparison implement the resulting hyperbolic tangent thresholding operator. The shape parameter is scaled by the input spectrum. We also establish o-minimal definability of the augmented objective. Under explicit boundedness, descent, relative-error, and exact-block conditions, the Kurdyka-Lojasiewicz framework guarantees convergence of the full sequence to a KKT point. On 23 datasets, HTNN-MSC achieves a mean clustering accuracy of 0.8404 and an average accuracy rank of 2.78 against nine representative methods. Friedman tests and Holm-adjusted Wilcoxon comparisons reveal significant overall differences, although several pairwise differences remain nonsignificant. HTNN-MSC records 19 wins, one tie, and three losses against the convex t-SVD-MSC skeleton. A same-skeleton ablation also shows that the proposed surrogate does not uniformly outperform alternative nonconvex penalties.

---


### 209. [Local Visibility Roadmaps in Continous Multi-agent Path Finding](https://arxiv.org/abs/2611.04944)

**<font color=#1a73e8>作者：</font>** Kristýna Janovská, Pavel Surynek  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We address the problem of smooth continuous multi-agent path finding (SC-MAPF), where agents move in a continuous environment along smooth curves in continuous time. The paths for individual agents are searched in local visibility roadmaps that consider obstacles and other agents. A new algorithm is proposed in this work, which combines the previous algorithm CE-CBS for high-level search with any-angle path finding for local single-agent planning, where agents are to avoid obstacles, both static and other agents. The new algorithm is tested and compared to CE-CBS, the algorithm building individual paths using RRT$^*$, and SMT-CCBS algorithm, an algorithm for MAPF$_R$. Experimental results show various advantages of the new algorithm over CE-CBS and SMT-CCBS in comparable settings.

---


### 210. [How Well Does Webcam Eye Tracking Work "in the Wild"? A Large-Scale Validation of Chiasm and a Comparison with WebGazer](https://arxiv.org/abs/2611.04946)

**<font color=#1a73e8>作者：</font>** Artem V. Belopolsky, Florian Perdreau  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Webcam eye tracking can greatly accelerate data collection in basic and applied research by reaching large, diverse samples of participants online. However, its spatial performance is considered well below that of hardware-based systems, limiting its use. We evaluated the first-generation Chiasm webcam eye tracker in a large online study ($N = 505$) spanning diverse participants, devices, and recording conditions. Chiasm achieved a mean spatial accuracy of 2.39 cm ($\approx 2.28^\circ$ at 60 cm), spatial precision (SD) of 1.05 cm ($\approx 1.00^\circ$ at 60 cm), and sample-to-sample precision (RMS-S2S) of 1.29 cm ($\approx 1.23^\circ$ at 60 cm). For the 91% of participants who met a 3 cm calibration criterion, spatial accuracy was 2.15 cm ($\approx 2.05^\circ$ at 60 cm). After three minutes of a task that encouraged head movement, spatial accuracy declined by 0.59 cm, while the gaze center at each target shifted by a mean distance of only 0.37 cm. On the validation block, the offset was 0.30 cm larger for men than for women. Age, region of residence, face luminance, and Michelson contrast showed no reliable relationship with spatial accuracy. A higher eye aspect ratio, a more open eye, was associated with a smaller offset. Wearing glasses decreased spatial accuracy on every validation block. In a comparison between a random subsample ($N = 101$) and a separate sample tested with the open-source tracker WebGazer ($N = 101$) using an identical protocol, Chiasm showed better spatial accuracy (2.18 vs. 4.51 cm) and spatial precision (SD; 1.01 vs. 1.55 cm). WebGazer showed better sample-to-sample precision (RMS-S2S; 0.79 vs. 1.26 cm), which likely reflects conservative, over-smoothed estimates rather than superior stability. These results suggest that Chiasm is narrowing the gap between webcam and hardware-based eye tracking, making large-scale gaze research "in the wild" a reality.

---


### 211. [DPAGait: Dynamic Pose-Knowledge-Aware Network for Robust Gait Recognition in the Wild](https://arxiv.org/abs/2611.04950)

**<font color=#1a73e8>作者：</font>** Zenan Lin, Junduan Huang, Kun Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gait biometrics aims at identity recognition by appearance or pose features captured during unconstrained human walking. Existing methods predominantly rely on binary silhouette images, inherently characterized by low information entropy, and fail to fully utilize the dynamic information in gait sequences, limiting their ability to handle cross-time variations effectively. Consequently, these methods encounter significant challenges in the wild. They are susceptible to variations in clothing, carried objects, and viewpoints, as well as dynamic environmental conditions, all of which lead to substantial degradation in recognition accuracy and robustness. To overcome these challenges, we propose a pose-knowledge-aware approach specifically designed for robust gait recognition in the wild. First, we propose a novel Dynamic Pose-Parsing enhanced Silhouette gait representation paradigm that substantially enhances the information entropy and effectively captures fine-grained behavioral cues by integrating pose-parsing cues with traditional silhouettes. Subsequently, we develop a dual-branch Dynamic Pose-Knowledge-Aware Gait network. The framework consists of two complementary branches: (1) a 2D dynamic pose-aware branch that extracts pose-enhanced features from our proposed DPPS representations, and (2) a 3D Skinned Multi-Person Linear branch that leverages the 3D SMPL model to capture rich and comprehensive 3D dynamic pose information. Finally, the features are integrated to facilitate accurate and robust gait recognition. Extensive experiments on four challenging in-the-wild gait datasets demonstrate the effectiveness and generalizability of the proposed DPPS representation. The complete framework is further evaluated on SUSTech1K, CCPG, and Gait3D, where SMPL information is available or can be consistently estimated, achieving competitive performance under diverse real-world conditions.

---


### 212. [Artifact-to-Capability: Diagnosing Breaks in Capability Formation of Self-Evolving Agents in a Controlled Environment](https://arxiv.org/abs/2611.04952)

**<font color=#1a73e8>作者：</font>** Ziqian Ban, Haoxiang Yang, Yanfei Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents write interaction experience into artifacts and reuse them in later tasks. Most work supports such methods with three proxy signals: artifacts accumulate, behavior changes once they are loaded, and metrics rise. We call this signal-based evaluation. What these signals are meant to indicate, however, has not been defined. To fill this gap, we define capability formation from artifacts as five sequentially dependent properties, two of which form a checkpoint for capability formation, and introduce three-scale diagnosis, which judges these properties at the state, game, and lineage levels. In freestyle Gomoku, Reflexion, Voyager, and DGM evolve with the same base model and all show the three signals, yet each exhibits a distinct capability-formation break. Reflexion shows a legalization gain: its pass rate rises only because more of its moves are legal. Voyager shows a compositional override: components that are sound on their own combine to miss all 20 available one-move wins. DGM shows loss-only drift: after passing the checkpoint, later versions only lose passing states. These counterexamples show that signal-based evaluation cannot determine whether a capability has formed.

---


### 213. [Deep Neural Operator Learning for stochastic heat equations and applications](https://arxiv.org/abs/2611.04955)

**<font color=#1a73e8>作者：</font>** Hengrong Du, Qi Feng, Weinan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we establish a universal approximation theorem for solution operators of semilinear stochastic heat equations in spatial dimension \(d\ge2\), extending deep neural operator approximation results to SPDEs with distribution-valued Gaussian forcing. A smooth Fourier cutoff reduces the forcing to finitely many measurements, while Besov and Schauder estimates control the resulting solution error. The finite-dimensional solution map is then approximated by ReLU branch networks together with grid-based trunk functions, yielding explicit bounds on the numbers of forcing measurements and trunk functions and approximation in every finite stochastic moment. For linear equations, the reduction coincides with truncation of the first Wiener chaos. Lastly, as an application, we prove a high-probability local-in-time approximation theorem for stochastic Navier--Stokes equations, with finite measurements of both the initial condition and forcing and an explicit sensing rate.

---


### 214. [Lightweight graph transformers for clutter and target classification in automotive radar](https://arxiv.org/abs/2611.04959)

**<font color=#1a73e8>作者：</font>** Adrian Gheorghiu, Tunc Alkanat, Ashish Pandharipande  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radar is a core sensor modality for scene perception to achieve higher levels of autonomy in automotive driving. A common occurrence in automotive radars is clutter - detections of non-existent moving objects, that can adversely impact target detection and classification performance and subsequent driving actions. We propose lightweight tiny graph transformer network (TGTNet) models for classifying clutter from stationary and moving targets in the scene. Performance evaluation on the public RadarScenes show that our proposed TGTNet models achieve similar classification performance in precision and recall metrics in comparison to state of the art models, with one to two orders of magnitude lower model size and significantly faster inference.

---


### 215. [ProAlign: Progressive Positional and Prototype-Guided Alignment for Aerial-Ground Person Re-Identification](https://arxiv.org/abs/2611.04980)

**<font color=#1a73e8>作者：</font>** Qiao Li, Jing Chen, Cong Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial-Ground Person Re-Identification (AG-ReID) aims to match pedestrian images captured by unmanned aerial vehicles (UAVs) and ground-based surveillance cameras. The task remains highly challenging due to severe viewpoint discrepancies, frequent occlusions, and substantial domain gaps between aerial and ground imagery. Beyond these observable factors, existing methods often overlook two fundamental structural issues: cumulative positional drift during hierarchical feature extraction and semantic inconsistency across cross-view feature distributions. To address these challenges, we propose ProAlign, a Progressive Positional and Prototype-Guided Alignment Network for AG-ReID. ProAlign comprises two key components: a Layer-wise Progressive Positional Embedding (LPPE) module and a View-Aware Prototype Contrastive Learning (PCL) module. LPPE performs adaptive positional calibration throughout transformer layers by employing conditional positional encoding in shallow layers to mitigate local spatial distortions, while introducing learnable static positional embeddings in deeper layers to reinforce global semantic priors. Meanwhile, PCL maintains view-specific aerial and ground prototypes for each identity and enforces cross-view semantic consistency via a dual-prototype contrastive objective. Extensive experiments on CARGO and two real-world AG-ReID benchmarks demonstrate the effectiveness of ProAlign, achieving state-of-the-art overall retrieval performance on CARGO with improvements of 1.60% in Rank-1 accuracy and 5.01% in mAP over the strongest competing methods.

---


### 216. [ZEMA: confidence-calibrated signed descent with only one state](https://arxiv.org/abs/2611.04987)

**<font color=#1a73e8>作者：</font>** Ali Dadsetan, Domenic Rosati, Frank Rudzicz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work characterizes the Adam optimizer as sign descent modulated by gradient uncertainty: the update is the sign of the batch gradient, scaled by how strongly the batch supports that sign. We apply this view directly and introduce ZEMA (Z-score Evidence Momentum Adaptation), which measures that support with a per-coordinate $z$-score computed from the per-example gradients in the current batch, converts it into a sign probability, and smooths the resulting update with a single exponential moving average. Because the probability is formed before smoothing rather than after, ZEMA keeps one state per parameter instead of Adam's two, at a $4.6$ increase in per-step time; the per-example variance it requires can also be estimated from a small fraction of the batch. In fine-tuning and pretraining experiments, ZEMA is competitive with Adam, reduces the variability of the validation loss, and in some settings recovers the sign of the full-dataset gradient more consistently. We close with two directions this opens: extending confidence adaptation beyond the sign geometry, to methods such as Muon, and to differentially private training.

---


### 217. [Exact Selective Inference for Spectral Clustering via Piecewise-Constant Graph Perturbation](https://arxiv.org/abs/2611.04995)

**<font color=#1a73e8>作者：</font>** Naotoshi Nakamura  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cluster labels are often used twice: first to discover groups, and then to test whether the discovered groups differ. This double use of the data makes ordinary two-sample $p$-values anti-conservative. Selective inference fixes this by conditioning on the clustering event, but for spectral clustering the event appears difficult because the algorithm combines an affinity map, an eigendecomposition, and a rounding step.
We show that, for spectral clustering based on unweighted $\varepsilon$- or $k$-nearest-neighbor graphs, the obstruction is the affinity construction rather than the eigendecomposition. Along the one-dimensional perturbation used by the truncated-$\chi$ selective test, graph changes occur only at finitely many real roots of data-dependent quadratic distance comparisons. Between these breakpoints, the graph, Laplacian spectrum, embedding, rounding, and reported cluster pair are deterministic functions of a finite graph state. Consequently, in real arithmetic and under a known-scale spherical Gaussian model, the selection set is an exact finite union of intervals, yielding finite-sample selective $p$-values for selected spectral-cluster pairs. The same argument gives feature-wise truncated-normal tests. We also record direct extensions to known feature covariance, eigengap-selected $K$, and auxiliary-coordinate graphs. We validate null and partial-null calibration, operational power, numerical sensitivity, and model-scope diagnostics, and give a working-model PBMC algorithmic illustration. Smooth kernels such as RBF affinities fall outside the finite-state guarantee.

---


### 218. [For You, Not for Everyone: Bystander-Aware Delivery of Critical Feedback in Robot Tutoring](https://arxiv.org/abs/2611.05001)

**<font color=#1a73e8>作者：</font>** Atikkhan Faridkhan Nilgar, Manuel Dietrich, Kristof Van Laerhoven  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Robots in shared settings may expose information intended for an individual user to nearby bystanders. Robot tutoring makes this concern particularly salient: critical feedback is directed at an individual learner, yet bystanders may overhear or see it. To address this, we compared context-invariant and context-adaptive robot behaviors in a between-subjects study with 40 participants. Following an initial phase without a bystander, a bystander entered the setting. Participants then received two scripted critical feedback messages concerning their pronunciation and handwriting, independent of their actual performance. With the context-invariant behavior, the robot tutor delivered both messages aloud. With the context-adaptive behavior, the robot tutor scanned for the bystander, turned its body and display away after detecting them, gave a spoken attention cue, and presented the same feedback messages silently on its display. Participants rated the robot tutor higher in perceived privacy awareness and perceived social competence in the context-adaptive condition than in the context-invariant condition, while evidence for reduced experienced embarrassment was inconclusive. These findings inform the design and evaluation of robots that respond to bystander presence by adapting how they communicate potentially sensitive information.

---


### 219. [ScoreDial: Precise Control of Visual Attributes in Image Generation via Regressor Guidance from Limited Human Ratings](https://arxiv.org/abs/2611.05004)

**<font color=#1a73e8>作者：</font>** Jianbo Tang, Keita Ishii, Hiroki Sakamoto 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Requested-value control is stricter than continuous steering: given $c$ on a human-rating scale, the generated image should attain that value from only limited ratings. We present ScoreDial, which fits a differentiable regressor $R$ to 100-479 human-rated images; once $R$ is fixed, a requested value $c$ is defined on its output scale, and learned target conditioning is paired with error-adaptive guidance that repeatedly reduces $|R(\mathbf{x})-c|$ during sampling. Across tire slip resistance, interior visual complexity, food desire-to-eat, and soap translucency, using one set of sampler settings shared across all four, ScoreDial reaches requested values and achieves, on all four attributes, $R$-MAE at most 0.013 over a range of width 0.8 and Spearman $\rho=0.980$, the maximum attainable under our evaluation protocol. Because $R$ also drives sampling, we evaluate agreement with $R$ separately from matched sweeps, an independent auditor fitted to the same ratings on a backbone none of the deployed regressors uses, and blinded human judgments. MPGD-flow also reaches the requested values under $R$, but ScoreDial has larger auditor displacement on every attribute, the largest among all compared methods, and a stronger MPGD-flow setting gives up target agreement without closing this gap. On every attribute, removing target conditioning leaves low $R$-MAE but more than halves auditor displacement, separating precise score correction from attribute movement. Blinded rating studies with 15 raters per attribute show that mean human ratings track $c$ on tire and soap, with linear $R^2=0.665$ and $R^2=0.786$, and in forced-choice comparisons of matched sweeps, raters chose ScoreDial's as the clearer progression in at least 84% of judgments against every baseline.

---


### 220. [Learned Smartphone ISP on Mobile GPUs: Mobile AI 2026 Challenge Report](https://arxiv.org/abs/2611.05008)

**<font color=#1a73e8>作者：</font>** Andrey Ignatov, Georgy Perevozchikov, Radu Timofte 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the increasing importance of mobile camera quality in modern smartphones, growing attention has been directed toward computational photography and advanced image signal processing (ISP) algorithms aimed at enhancing various perceptual attributes of captured images. This creates a need for efficient deep learning models for this problem that are not only performant but can also be deployed on constrained mobile hardware. In this Mobile AI challenge, we address this problem and propose the participants to design fast solutions that can reconstruct RGB photos from RAW Bayer camera data while running on popular smartphone GPUs from Qualcomm and Arm. For this, the participants were provided with a large-scale Fujifilm UltraISP dataset consisting of RAW-RGB image pairs captured with the Sony IMX586 Quad Bayer mobile sensor and a professional 102MP medium format FujiFilm GFX100 camera. The runtime of all models was evaluated on the Snapdragon 8 Elite Gen 5 and Dimensity 9500 chipsets with the Adreno and Mali GPUs, respectively. Top solutions proposed in this challenge are able to reconstruct high-quality 5MP RGB image from raw data on both platforms under 100 milliseconds. A comprehensive description of the models developed in the challenge is provided in this paper.

---


### 221. [Can saliency maps flag chest radiograph classifier errors at a new hospital? An external validation study](https://arxiv.org/abs/2611.05011)

**<font color=#1a73e8>作者：</font>** Aashish Chapagai, Angad Singh Gurtatta, Erik Cambria  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Saliency maps are offered as a safeguard for medical image classifiers, but whether they reveal individual errors at a new hospital remains largely untested. We trained a convolutional network and a vision transformer on NIH ChestX-ray14 and evaluated 303,768 decisions per model at the training hospital and at two external sites, in the USA and Vietnam, with radiologist-consensus labels. We scored each explanation by its anatomical enrichment, the area-normalized concentration of attribution in a segmented thoracic region, and tested whether it detects errors beyond the model's confidence. Grad-CAM localized findings less often than radiologists (hit rate at most 0.575 versus 0.888). Adding enrichment to a confidence-based error detector calibrated at the training hospital never raised its area under the curve by more than 0.011, and for the convolutional network the relation between enrichment and correctness reversed between hospitals, degrading the transferred detector. Model confidence, not saliency, should anchor deployment monitoring.

---


### 222. [Rethinking GA2Ms: performance and out-of-distribution generalisation](https://arxiv.org/abs/2611.05012)

**<font color=#1a73e8>作者：</font>** George Dimitriadis, Damian Machlanski, Paul Clarke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generalised Additive Models (GAMs) are a cornerstone of interpretable machine learning, offering transparent predictions through structured additive decompositions. Despite advances from classical GAMs to modern neural and spline-based variants, two notable gaps remain. First, comprehensive benchmarking of spline-based GAMs on large-scale tabular learning tasks, the dominant modality in applied settings, is lacking. Second, their robustness under distribution shift, a setting where structured inductive biases should confer advantages, remains unexplored. We propose a multi-resolution, higher-order Composite Generalised Additive Model (CoGA2M) and evaluate it on the TALENT benchmark suite. CoGA2M ranks in the top third across all baselines (29 for regression, 32 for classification), establishing competitive performance with state-of-the-art tabular methods. We further extend TALENT with out-of-distribution (OOD) splits exhibiting train-test distributional shift and benchmark CoGA2M against LightGBM, a consistently top-performing model on TALENT. Under distribution shift, CoGA2M outperforms LightGBM, demonstrating a clear structural advantage. Our results position spline-based GAMs as strong contenders for tabular prediction and reveal a previously unrecognised benefit of additive structure in the OOD regime.

---


### 223. [Finite Spectral Depth Controls Gaussian Entrance Rank and Avoidance of the First Gradient-Flow Saddle](https://arxiv.org/abs/2611.05022)

**<font color=#1a73e8>作者：</font>** Yanlin Long  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Matrix factorization provides a simple model for studying the training dynamics of neural networks. Recent studies of gradient flow under small initialization have analyzed how trajectories escape from a neighborhood of the origin and approach their first nonzero stationary point. In this paper, we study continuous-time dynamics that applies a finite number of Newton-Schulz iterations to the normalized matrix gradient (Muon). We show that the number of Newton-Schulz steps can change the rank selected during the early stages of training and allow the resulting trajectory to bypass the first nonzero stationary point approached by gradient flow. Under an additional residual-inertia condition, we prove that bypass occurs for all sufficiently large finite Newton-Schulz depths and provide an explicit sufficient threshold. We also construct an example in which the bypass threshold is four.

---


### 224. [RGB Photo Enhancement with Deep Learning on Smartphone GPUs: Mobile AI 2026 Challenge Report](https://arxiv.org/abs/2611.05024)

**<font color=#1a73e8>作者：</font>** Andrey Ignatov, Georgy Perevozchikov, Radu Timofte 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-device RGB photo enhancement is a popular task that is needed for quality improvement of photos captured with mobile devices as well as for retouching of images acquired through other sources. This creates a need for efficient deep learning models for this problem that are not only performant but can also be deployed on constrained mobile hardware. In this Mobile AI challenge, we address this problem and propose participants to design fast solutions that can perform comprehensive enhancement of RGB photos while running on popular smartphone GPUs from Qualcomm and Arm. For this, the participants were provided with a large-scale DPED dataset consisting of RGB image pairs captured with an old iPhone 3GS smartphone and a professional Canon 70D DSLR camera. The runtime of all models was evaluated on the Snapdragon 8 Elite Gen 5 and Dimensity 9500 chipsets with the Adreno and Mali GPUs, respectively. Top solutions proposed in this challenge are able to enhance Full HD resolution RGB images on both platforms under 300 milliseconds. A comprehensive description of the models developed in the challenge is provided in this paper.

---


### 225. [DRAP: Dynamics-Risk Adaptive Plasticity for Continual Learning in Physical AI](https://arxiv.org/abs/2611.05029)

**<font color=#1a73e8>作者：</font>** Oswaldo Ludwig  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning in physical AI differs from conventional continual learning because small per-step policy errors can accumulate over a trajectory. Each deviation may move the agent outside the training distribution, increase subsequent prediction errors, and ultimately cause closed-loop task failure. This work introduces Dynamics-Risk Adaptive Plasticity (DRAP), a replay-free method that estimates the historical importance of adaptable model tensors from sample-level action gradients weighted by local trajectory-amplification risk. A ridge-regularized local linear model is fitted to expert state-action transitions, and the largest singular value of its state-transition matrix provides a policy-independent, Lyapunov-inspired estimate of one-step perturbation amplification. After each task, risk-weighted squared gradients are accumulated in a tensor-level importance memory. During subsequent tasks, DRAP uses normalized cumulative importance to scale the effective AdamW learning rate of each tensor, immediately reducing the plasticity of components that supported previous behavior at dynamically sensitive trajectory points. We instantiate DRAP on a fixed KappaTune-selected subnetwork of OpenVLA and evaluate replay-free sequential adaptation across the LIBERO Spatial, Object, and Goal suites. Compared with standard AdamW fine-tuning and EWC, the results show substantially improved retention of previously learned behaviors while preserving strong new-suite acquisition.

---


### 226. [Federated Transfer Learning for Medical Image Classification under Mixed Skew](https://arxiv.org/abs/2611.05035)

**<font color=#1a73e8>作者：</font>** Alexandre G. Leclercq, Sébastien Bougleux, Aurélien Corroyer-Dulmont 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning in medical imaging is constrained by data scarcity and by privacy regulations that make centralizing patient data across institutions impractical. Federated Learning (FL) addresses these constraints by keeping data local, but its distributed nature exposes training to strong statistical heterogeneity. Multicentric medical data is particularly affected, exhibiting a mixed skew that combines feature, label, concept, and quantity shifts across centers. Personalized FL mitigates heterogeneity by tailoring a model to each client, yet most methods assume training from scratch, which is unrealistic given the high dimensionality of medical features relative to the limited data available. We propose the Personalized Aligner Federated Pretrained (PAFP) framework, a personalized FL approach built on a pre-trained backbone. PAFP inserts client-specific Feature Alignment modules before the fine-tuned blocks to realign hidden feature distributions toward a server-aggregated target. On the FedISIC benchmark, PAFP attains the highest unweighted balanced accuracy while reducing inter-client performance variance roughly six-fold relative to the strongest baseline, yielding accuracy and cross-client equity jointly. Our code is publicly available at this https URL.

---


### 227. [Positional Encoding is All You Need for Scalable Equivariance Constraint Relaxation](https://arxiv.org/abs/2611.05041)

**<font color=#1a73e8>作者：</font>** Hagay Michaeli, Haggai Maron, Daniel Soudry  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equivariant neural networks incorporate known symmetries of the data, such as permutations, rotations, or translations, directly into their architecture, often improving sample efficiency and generalization. However, strict equivariance can make optimization difficult, for example, when the data only approximately satisfy the assumed symmetry, or when the equivariance constraints induce a challenging loss landscape. Recent studies have shown that relaxing equivariance during training by introducing non-equivariant dense linear layers can ease optimization in such cases and improve the performance of the resulting strictly equivariant model, after removing the relaxation layers at test time. While effective, this approach incurs a significant computational overhead, limiting its applicability in scalable architectures. In this work, we propose a more efficient constraint-relaxation method based on positional encoding (PE). Our framework injects a positional encoding with learnable scale that breaks the model's original symmetry. This positional signal is gradually annealed to zero, recovering the original equivariant model by the end of training. Empirically, we demonstrate significant improvements for translational and rotational equivariant models with only marginal compute and memory overhead.

---


### 228. [Effects of Parton Pair Correlations on Direct-Photon Yields and Elliptic Flow in Heavy-Ion Collisions](https://arxiv.org/abs/2611.05042)

**<font color=#1a73e8>作者：</font>** Xingjian Lu, Shuzhe Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct photons escape heavy-ion collisions with little rescattering, carrying information from the full emission history. Yet describing the measured direct-photon yield and the sizable elliptic flow $v_2$ together remains a long-standing challenge. Here we explore how correlations between emitting partons may affect both observables. The local $2\to2$ photon rate depends on the joint distribution of incoming partons, so a connected correlation between them can change photon emission without changing the one-particle distribution of medium particles. Once folded over the evolving medium in Au+Au and Pb+Pb collisions, the correlation raises the photon yield toward the fitted PHENIX and ALICE data and increases $v_2$ mainly at intermediate $p_T$. The fitted temperature dependence accounts for most of the net flow increase in this region, suggesting that the correlation changes the relative contributions between hotter and cooler regions.

---


### 229. [On the Learnability of Footwear Robustness: Footstep Recognition Under Unseen Conditions](https://arxiv.org/abs/2611.05049)

**<font color=#1a73e8>作者：</font>** Robyn Larracy, Erik Scheme  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Footstep patterns, captured using pressure or force-sensitive walkways during natural walking, offer a convenient and passive approach to biometric recognition. However, footwear variability poses a major challenge to practical deployment, as it impacts both the foot-sensor interface and the user's underlying gait mechanics. This study considers the particularly difficult scenario where users enroll under one fixed footwear condition but must later be recognized in arbitrary, unseen footwear. Using the StepUP-P150 dataset, we show that footwear-induced shift, while substantial and heterogeneous across individuals, contains shared structure that can be learned from a training population and transferred, zero-shot, to previously unseen users and footwear styles. We do this using BiStepNet, a novel architecture that decomposes spatial and temporal identity cues into independently trainable streams and outperforms compact 3D spatiotemporal baselines for cross-footwear recognition. We demonstrate that cross-footwear recognition performance scales systematically with the volume and diversity of footwear representation in the training set, with gains transferring to footwear styles not directly observed during training. Moreover, we show that auxiliary gait datasets with only partial modality overlap (incorporated through the architecture's decomposed design) can be leveraged to further improve robustness to unseen footwear conditions.

---


### 230. [FloMo: 3D Scene Flow as a World Action Model Intermediate for Learning from Human Video](https://arxiv.org/abs/2611.05062)

**<font color=#1a73e8>作者：</font>** Jeremy Collins, Namra Patel, Ayush Agarwal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained video generation models distill internet-scale motion priors into robot policies, but full video is a redundant signal for action prediction. We argue that dense 3D motion is the medium through which video pretraining best transfers to robot actions, and that predicting motion rather than video affords better sample-efficiency for action prediction. FloMo is a 5B video-generation model fine-tuned to predict 3D scene-flow and action tokens. Rendering scene flow as RGB and encoding it into the same latent space as video enables a pretrained video generation backbone to efficiently adapt to predict 3D scene flow. Co-trained on action-free human video and action-labeled robot teleoperation data, our model benefits from human-video pretraining and generalizes to unseen objects, motion primitives, and tasks. Replacing motion prediction with a video prediction objective degrades out-of-distribution generalization, while adding a video prediction target alongside motion lowers policy success rather than improving it. When motion, video, and action are predicted jointly, action tokens attend far more to motion than to video, suggesting that predicting video wastes model capacity. Together, these results indicate that motion effectively mediates the transfer from video pretraining to action. More information can be found at this http URL.

---


### 231. [Manifold Embedding of Deep Image Features for Image Matching via Neural Adjoint Maps](https://arxiv.org/abs/2611.05083)

**<font color=#1a73e8>作者：</font>** Nafie El Amrani, Moritz Heep, Florian Bernard  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating semantic correspondences between different object instances of similar categories in real-world images is a fundamental challenge in computer vision. While the recent progress in foundation models has significantly advanced solutions for such difficult image correspondence problems, respective methods are often insufficiently regularised. For example, common nearest-neighbour matching with foundation model features often results in noisy correspondences, which is particularly prominent when solving for dense correspondences. In this work, we tackle image matching via functional maps, which have been popularised for 3D shape matching due to their powerful spectral formalism utilising an efficient low-dimensional linear representation. However, functional maps require that domains (in our cases the rectangular image grids) are equipped with an informative and non-trivial geometry. To define a meaningful manifold structure for images, we use Galerkin's method from finite elements to derive a discrete Laplace-Beltrami operator (LBO) based on a manifold embedding of deep image features. Further, we leverage a neural adjoint map that allows to represent non-linear mappings. We demonstrate that our method sets the new state of the art among zero-shot image correspondence methods on multiple dense correspondence benchmarks of real-world images. Our code is publicly available: this https URL

---


### 232. [Sparse Anchors for Visual Multi-Session Registration in Changing Environments](https://arxiv.org/abs/2611.05084)

**<font color=#1a73e8>作者：</font>** Yunus Talha Erzurumlu, Niklas Trekel, Saurabh Gupta 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Repeated robotic monitoring requires localization across visits to the same environment, even if the environment changes. Such changes can substantially reduce persistent visual content, and repetitive structures can lead to incorrect cross-session correspondences. In this paper, we address visual multi-session registration of a new data recording (the query session) to a previously reconstructed reference map. Under substantial visual and structural changes, cross-session localization may be possible only for parts of the trajectory. In our approach, we therefore rely on a sparse set of reliable absolute pose constraints and combine them with within-session relative-pose information to register the complete trajectory to the reference map. We first estimate absolute alignment hypotheses through visual place recognition, local feature matching, and geometric verification. We then use sequence consensus to reject hypotheses that are inconsistent with a common query-to-reference alignment and retain the remaining poses as absolute anchors. These anchors are refined through featuremetric alignment against a Gaussian feature field and combined with within-session relative-pose constraints in a robust pose-graph optimization. We evaluate our approach on 15 cross-session experiments from the challenging HILTI26 construction-site dataset, covering substantial scene changes and difficult-to-match environments. Our method achieves 94.4% recall within 1m and 100.0% within 5m, outperforming independent image localization, which peaks at 65.3% and 70.7%, respectively, as well as direct registration of independently reconstructed Structure-from-Motion geometry. Our results show that sparse, reliable absolute anchors can provide accurate and complete trajectory registration even when reliable cross-session correspondences are available only for part of the query session.

---


### 233. [Dual-VaDE: Efficient and Robust Prototype Learning via Variational Dual-Domain Mixture Priors](https://arxiv.org/abs/2611.05099)

**<font color=#1a73e8>作者：</font>** Wugeng Zheng, Song Wang, Jian Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose Dual-VaDE, an unsupervised generative framework for learning interpretable anatomical prototypes from unlabeled medical images. In contrast to previous variational methods that rely on a single spatial latent code, which often entangles global geometry with local textures and fails to capture their cross-domain dependencies, Dual-VaDE introduces a dual-domain Gaussian mixture prior that explicitly couples spatial anatomy with phase-preserving Fourier spectral representations. We derive an exact, closed-form variational lower bound that fuses this joint prior into the decoder and optimizes the entire network end-to-end via an alternating EM formulation, avoiding heuristic two-stage clustering while ensuring superior training stability and robustness. Evaluated on OASIS-3 brain MRI, Dual-VaDE delivers substantially sharper and more plausible prototypes, achieves superior cluster separation with improvements of up to 94% over spatial-only baselines, exhibits markedly reduced variance across random seeds, and incurs negligible inference overhead (0.28 ms per image).

---


### 234. [Characterizing the vertical continuity of fuel strata based on TLS point clouds Gaussian decomposition and overlap metrics](https://arxiv.org/abs/2611.05102)

**<font color=#1a73e8>作者：</font>** Jesús Torralba, Luis Á. Ruiz, Pablo Crespo-Peremarch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vertical forest structure influences fire behavior by regulating understory-to-canopy fuel connectivity, yet operational fuel-type models represent this complexity through discrete classes that only indirectly capture vertical continuity. High-density point clouds offer an opportunity to characterize vertical fuel connectivity in a more explicit and continuous manner, but specific methodological approaches are still required. We applied Gaussian decomposition to vertical height profiles derived from terrestrial laser scanning (TLS) point clouds across 25 permanent forest plots to characterize geometric vertical fuel continuity. A multiscale analysis spanning from the plot scale to ~0.5 $m^2$ units was used to evaluate geometric, probabilistic, and overlap metrics for characterizing fuel strata. The method reproduced the vertical transition between shrub and tree strata, with median Pearson correlations ranging from 0.83 to 0.96 across analysis levels. Probability density overlap metrics and separability indicators, such as the Jeffries-Matusita distance, provided complementary descriptors of vertical continuity. Intermediate spatial scales (3-6 m cells) provided a useful compromise between spatial detail and the consistent representation of shrub-canopy interaction patterns. Finer scales increased variability due to point density reduction and profile irregularity, and low mean squared error values were found insufficient as sole performance indicators. Gaussian decomposition applied to TLS point clouds enables explicit quantification of vertical fuel continuity, a limitation of current discrete classification systems. Continuous vertical connectivity metrics derived from this approach offer a pathway for improving ladder fuel characterization and strengthening decision-making support in wildfire risk assessment.

---


### 235. [Molecular Prior Networks](https://arxiv.org/abs/2611.05103)

**<font color=#1a73e8>作者：</font>** Pawel Gomoluch, Anthony Bradley  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting affinity between small molecules and their protein targets remains one of the central problems in drug discovery. Due to the substantial cost of wet-lab experiments, machine learning models of drug-target affinity are usually trained on relatively small datasets, ranging from tens to hundreds of molecules. Given the inherent difficulty of generalization between different targets and chemical series, existing datasets of protein-ligand affinities are typically not used for new projects. At the same time, tabular foundation models, including Prior-data Fitted Networks, have recently shown how transformers can be used to solve machine learning problems in a single forward pass of the network, after being trained over a large corpus of, typically, synthetic datasets. Inspired by that line of work, we propose a novel affinity modelling approach, in which the labels of the query molecules are predicted from the labelled support molecules in a single forward pass of a transformer model. The model is trained on thousands of existing affinity datasets, enabling it to capture the general patterns of molecular activity across different targets, chemical series and dataset sizes. For the smallest support sets, our model matches the state of the art on the regression variant of the FS-Mol benchmark, while being faster than existing methods, thanks to the lack of task-specific training. A comparison against a reduced variant of our architecture, which amounts to kernel regression in a meta-learned feature space, shows that the predictive performance of the transformer model is only partially explained by simple molecular similarity.

---


### 236. [From AutoResearch to Continual AutoResearch: Do Agents Learn Across Tasks?](https://arxiv.org/abs/2611.05108)

**<font color=#1a73e8>作者：</font>** Jeremy Qin, Ruizhi Deng, Mohamed Osama Ahmed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoresearch has shown that agents can autonomously write code, run experiments, and iteratively improve machine learning solutions. Yet most evaluations start a new agent session from scratch for each new problem, making them costly and leaving unclear whether agents can retain and apply prior insights when adapting to new tasks. We introduce CONTINUAL AUTORESEARCH, an open-ended environment that compares persistent and reset instances of the same agent under matched task streams, data, and time budget. Continual AutoResearch covers nine task families, spanning synthetic tasks, symbolic regression, time-series forecasting, and tabular AutoML. Across five frontier agents, we measure first-solution quality, research efficiency, and final held-out performance. To distinguish insight transfer from session continuity, we run a memory ablation that vary what information agents retain from prior tasks. We show that persistent state improves research efficiency of all five agents, allowing them to find stronger solutions sooner. However, these gains do not consistently translate into better final solutions. Overall, our findings suggest that retaining experience and utilizing it effectively are distinct capabilities.

---


### 237. [Beyond Multi-Index Models: Learning Intersections of Degree-2 PTFs](https://arxiv.org/abs/2611.05114)

**<font color=#1a73e8>作者：</font>** Ilias Diakonikolas, Daniel M. Kane, Mingchen Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We give an algorithm for PAC learning intersections of $k$ degree-2 polynomial threshold functions over $R^d$ under a Gaussian distribution. Our algorithm achieves classification error $\epsilon$ using $d^{O(k)}2^{O_k(\log^3(1/\epsilon))}$ time and samples, improving over the $d^{O(k^2/\epsilon^2)}$ running time of the polynomial regression approach. To our knowledge, our result is the first to obtain a dimension exponent independent of the accuracy parameter, even for $k=2$. We complement our algorithmic result with an SQ lower bound showing that the complexity dependence of $d^{\Omega(k)}$ is unavoidable.
Lifting the input to polynomial features turns the target into an intersection of $k$ halfspaces. This suggests using the first two labeled moments for subspace recovery. In the lifted space, however, these moments can reveal nothing. Our starting point is a Gaussian comparison theorem showing that, for sufficiently regular defining quadratics, the labeled moments needed for subspace recovery are approximately preserved. To handle arbitrary defining quadratics, we establish a new structural result showing that every direction with significant resampling influence can be detected through degree-$O(k)$ moments. These results yield an initial $d^{O(k)}2^{\mathrm{poly}_k(1/\epsilon)}$-time learner using adaptive restrictions.
To improve the exponential dependence on $1/\epsilon$, we develop a two-stage dimension-reduction approach that avoids the costly adaptive partitioning. After identifying a subspace containing all directions with large influence, we use generalized regularity and Gaussian comparison to recover the remaining relevant quadratic features through a new derivative-based moment operator. The recovered features support an intersection close to the target. Combining them with robust hinge-loss minimization gives our quasipolynomial-time learner.

---


### 238. [Towards an Optimal Control Foundation of Early Exits - Turnpikes and ResNets](https://arxiv.org/abs/2611.05120)

**<font color=#1a73e8>作者：</font>** Jens Püttschneider, Simon Heilig, Asja Fischer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The feed-forward propagation through neural networks is crucial for training and inference. To trade off efficiency and accuracy, it has been proposed to consider intermediate outputs of hidden states as data-dependent regularization during training and, ultimately, as early-exits during inference. In this work, we analyze the joint optimization of loss functions computed for the output layer and intermediate layers using optimal control theory. We prove that ResNets trained in this joint fashion exhibit the so-called turnpike phenomenon, this implies that the number of layers required to reach a prescribed loss level is bounded from above independently of the overall network depth. This induces a similarity property across the internal representations of early-exiting networks of varying depths. We connect the turnpike to the overthinking phenomenon, and provide theoretical insights into the success of early-exit criteria derived from softmax probabilities, specifically entropy and max-probability. In a range of experiments, we demonstrate the existence and effect of turnpikes and the resulting similarity in the early-exit performance for ResNets of varying depths.

---


### 239. [Do Ray-Traced Cities Make a Better Channel Prior for an Unseen Site? A Pre-Registered Study in Simulation, and a Test on Measured Channels that Reverses It](https://arxiv.org/abs/2611.05128)

**<font color=#1a73e8>作者：</font>** Krish Patel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Channel estimators at a newly deployed base station usually start from 3GPP stochastic channel models, which describe no particular street. We ask whether a channel prior pooled from many ray-traced cities serves an unseen site better than the 3GPP CDL models, and whether learned estimators make the difference. With Sionna RT on 14 city scenes, LMMSE estimation from covariance priors, leave-one-city-out evaluation, and pass/fail bars written down before each main experiment, we find in simulation that the pooled prior sits about 0.6 dB from a site-trained estimator with no site measurements, about what CDL reaches after 50 measurements. Learned models added little: at most 0.65 dB in estimation, and in channel prediction a simple classical method beat CNN predictors by 1.8-12 dB from 2 ms ahead. On measured channels from the DICHASUS outdoor dataset (1.272 GHz, three 2x8 arrays on one building) the result reversed: the pooled ray-traced prior was 3.2-4.1 dB worse than CDL. The simulated channels were too clean; with users at the real distances, even a scattering level tuned from 50 site measurements left the prior about 2 dB behind CDL. A pre-registered follow-on on two more measured environments found the generic CDL prior 2.1-4.7 dB from a site-trained one: no further in a factory hall than on the street, furthest in a small lab room. Finally, a hallway model calibrated to measurements by differentiable ray tracing reproduced delay spread, but as a prior in an unmeasured part of the hallway it was 4.5 dB worse than CDL on the full array. All measured results come from one sounder.

---


### 240. [High-fidelity training-free photovoltaic module mapping from multi-view UAV imagery](https://arxiv.org/abs/2611.05131)

**<font color=#1a73e8>作者：</font>** WenHao Duana, Qi Chena, Penglei Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity photovoltaic (PV) module mapping requires complete instance recovery and accurate delineation. Vision foundation models offer zero-shot segmentation, but converting incomplete and inconsistent predictions across views into a complete, geometrically accurate map of individual modules remains challenging. We propose the Multi-View PV Module Mapper (MV-PVMapper), a training-free framework coupling vision foundation models with unmanned aerial vehicle (UAV) photogrammetry. First, Segment Anything Model 3 (SAM 3) generates candidates from original images using text prompts. Their contours are then transferred into object space through per-module slope correction to limit distortion from surface-model noise, and verified against representative module dimensions to guide cross-view instance selection. Finally, accepted instances return to all covering images as box prompts for SAM~3, supplementing text prompts with spatial cues for iterative segmentation, verification and fusion. On five-direction surveys of three operational rooftop PV plants at approximately 1 cm nadir ground sampling distance, two feedback iterations recover 7,710 of 7,711 reference modules with no false positives at an intersection-over-union (IoU) matching threshold of 0.5. Macro-averaged area precision and recall reach 99.00 % and 98.52 %, respectively. Averaged across sites, the aggregated Jaccard index reaches 97.55 %, compared with 60.73 % and 41.24 % for orthomosaic segmentation and multi-view pixel-voting baselines, respectively; average precision at the stricter IoU threshold of 0.95 reaches 95.67 %. Ablation studies show that module-size constraints are critical for instance separation, while slope correction and feedback to all covering views improve boundary accuracy. These results are achieved without task-specific image annotation or segmentation-model weight updates.

---


### 241. [PAC Learning with Multiple Correct Answers](https://arxiv.org/abs/2611.05133)

**<font color=#1a73e8>作者：</font>** Steve Hanneke, Farnam Mansouri, Alireza F. Pour 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study PAC learning when each example comes with a set of at most $\ell$ correct labels and a prediction is correct if it belongs to this set. Training may reveal the full set, only whether a proposed label is correct (bandit feedback), or one correct label chosen by a demonstrator (emonstrations).
Our main finding is that demonstrations can be much harder than full sets, and even than bandit feedback, both in which classes can be learned and in how many examples are needed. For finite label spaces, a generalized Natarajan dimension characterizes learnability from full sets and from bandit feedback, in both the realizable and the agnostic setting. From demonstrations, however, a class is realizably learnable if and only if the intersections of at most $\ell+1$ of its hypotheses are learnable from full sets. Already with three labels, this condition can fail for a class learnable from a single full-set example or even a single bandit answer. When the condition holds, we show that $\widetilde O(\varepsilon^{-\ell})$ demonstrations suffice, and the exponent $\ell$ cannot be improved in general, even for classes learnable from $\widetilde O(1/\varepsilon)$ full sets or bandit answers.
For countable label spaces and $\ell \geq 2$, our packed dimension, which asks for many disjoint groups of at most $\ell+1$ hypotheses with no common label, characterizes full-set learnability, and demonstrations still reduce to intersections. Agnostic learning from demonstrations, already for finite label spaces, is not determined by the dimensions of the intersection class that characterize realizable learning.
Finally, we show that the uniform bound $\ell$ on the number of correct labels is essential. Without this bound, it is impossible to characterize learnability by any dimension determined by finite subclasses.

---


### 242. [When Cell Crops Share a Parent: Measuring and Isolating Acquisition Leakage in Cervical Cytology Benchmarks](https://arxiv.org/abs/2611.05145)

**<font color=#1a73e8>作者：</font>** Snehasish Ghosh, Soham Mitra, Antareep Majumdar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Public cervical cytology benchmarks release many cell crops cut from far fewer microscope fields or slides and are often split at the crop level, so test cells share acquisition parents with training cells. In a preregistered study, crop-level splitting raised SIPaKMeD accuracy by 0.97 percentage points across twelve architectures and twenty seeds (95% CI 0.59-1.39), and CRIC accuracy by 12.08 points (11.16-12.99). On SIPaKMeD, a factorial that fixes training crop and parent counts attributes the gain to sibling exposure (1.73 points, 0.95-2.51), not to the extra parent diversity of crop-level splits (0.00). Parent identity is decodable at about 100 times chance, yet erasing 82% of its above-floor linear recoverability left the gap unchanged, and Grad-CAM did not distinguish leaking from clean models; matching test cells' color statistics to an unseen same-class field removed most of the advantage. Decodability and saliency cannot substitute for a parent-disjoint split.

---


### 243. [Macrocanonical Generator Networks: Data-Efficient Neural Surrogates for Amortized Physics Simulation](https://arxiv.org/abs/2611.05157)

**<font color=#1a73e8>作者：</font>** Niall Jeffrey, Benjamin D. Wandelt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many scientific simulations are computationally expensive, limiting their use in simulation-based inference, uncertainty quantification, and decision making. We introduce macrocanonical generator networks, a framework for learning fast, data-efficient neural surrogates for amortized simulation of stationary physical processes by matching multiscale statistics of a target process. Inspired by microcanonical maximum-entropy synthesis, which matches feature statistics per sample by inner-loop optimization, our approach instead trains a neural generator to satisfy the same constraints in expectation, preserving physically realistic sample-to-sample fluctuations. We prove that gradient-descent training induces preconditioned gradient-descent dynamics in sample space that inherit the symmetry-preservation properties of the microcanonical gradient descent of Bruna and Mallat, amortizing its per-sample inner-loop optimization into a single training run after which every sample is generated in one forward pass. We further show that residual generator parameterizations initialized near the identity, trained with a small learning rate, preserve entropy locally during early optimization and mitigate mode collapse. Experiments on cosmology and fluid simulations show that macrocanonical generators recover realistic samples from extremely small training sets, in some cases a single training example, while generating new realizations more than $10^6$ times faster per sample than the reference simulator and more than $10^3$ times faster than microcanonical gradient descent. The trained generators can be reused for downstream pretraining, including simulation-based inference, providing a data-efficient route to multi-fidelity scientific machine learning workflows.

---


### 244. [Perturb, Repair, Verify: Self-Play Vision-Language Verifiers for Compositional Understanding](https://arxiv.org/abs/2611.05158)

**<font color=#1a73e8>作者：</font>** Zijun Huang, Yingjun Du, Cees G. M. Snoek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language verifiers judge whether an image faithfully matches a textual description, yet existing training pipelines typically rely on static supervision from stronger external judges or curated hard-negative data. Such supervision requires external generation or annotation, is teacher-bounded, and is difficult to adapt as model failures evolve. We introduce PROVE (Perturb-and-Repair Optimization for Vision-Language Evaluation), a self-play framework that trains verifiers through a closed perturb-verify-repair-verify loop. Starting from a known-correct image-caption pair, a Mutator introduces a typed perturbation over objects, attributes, counts, or relations. The verifier then judges the perturbed caption and provides textual feedback, which a Repairer uses to recover a faithful caption for re-verification. These two verification rounds produce structured rewards for informative mismatches and visually grounded repairs. Since perturbation, verification, and repair are role-conditioned behaviors of the same evolving multimodal backbone, updating the shared parameters also improves the verifier itself. Experiments show that PROVE improves fine-grained compositional verification across model scales and families and strengthens visual-detail robustness on the reference backbone, with limited, benchmark-dependent changes on broader multimodal tasks.

---


### 245. [Basin2Vec: Learning Basin-Centric Embeddings for Scalable Hydrological Modeling](https://arxiv.org/abs/2611.05164)

**<font color=#1a73e8>作者：</font>** Muhammad Talha, Xiaofeng Liu, Yuan Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable streamflow prediction across time and in ungauged basins requires representations that capture hydrologically relevant basin characteristics. Existing methods rely on either fixed handcrafted attributes or general-purpose Earth observation embeddings not tailored to basin structure. We introduce \textbf{Basin2Vec}, a self-supervised framework that learns compact basin representations from hydroclimatic and physiographic data without observed streamflow. Basin2Vec organizes representation learning around basin scale and relationships across space and time. Across multiple forecasting architectures, it consistently outperforms predefined attributes and general-purpose geospatial embeddings in temporal generalization and zero-shot spatial transfer. Basin2Vec provides average relative gains of up to 8.3% temporally and achieves 3.5x the median predictive performance of the strongest baselines on unseen basins. These results demonstrate the effectiveness of basin-centric pretraining for transferable hydrologic prediction. Code is available at this https URL

---


### 246. [When Self-Verification Hurts: Calibrated Answer Repair for Financial Question Answering](https://arxiv.org/abs/2611.05166)

**<font color=#1a73e8>作者：</font>** Celine Guo, Weida Liang, Yujian Fu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial question answering can fail even when a model extracts a plausible number from the supplied evidence: the answer may attach it to the wrong entity, period, unit, or accounting concept. Asking the model to verify and revise its draft can help, but open-ended revision may alter content that was already correct or inspect the wrong relation and reinforce the original error. We formulate repair as a decision that balances the information it may recover against the correct content it may damage. Based on this trade-off, we introduce Calibrated Answer Repair (CAR), which first estimates whether a draft is likely to benefit from repair, then selects a targeted check, localizes the relevant evidence or draft span, and limits the permitted edit. Across FinRank, Fin-RATE, and FinQA with three open-weight models, CAR outperforms generic verification in all dataset-model settings. At the system level, it recovers 14.6% of initially missed answer requirements while damaging 2.1% of initially correct ones. Its post-draft token cost is over 30 percent lower than the iterative revision alternatives. Ablations on two dataset-model settings show that evidence localization and bounded editing are the main contributors to CAR's gains.

---


### 247. [Learning Behaviorally Relevant Dynamics in Multimodal Neural Recordings](https://arxiv.org/abs/2611.05167)

**<font color=#1a73e8>作者：</font>** Parastoo Azizeddin, Eray Erturk, Maryam M. Shanechi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal neural data can enable a more complete understanding of brain dynamics underlying behavior. Modalities such as spiking activity, local field potentials (LFPs), and behavior capture diverse spatiotemporal aspects of brain processes, yet prior neural-behavioral models that separate sources of variability rely on a single neural modality. By leveraging these complementary strengths, multimodal neural fusion can provide a unified, rich representation of brain-behavior processes and address the limitations of single-modality analyses. Here we develop BREM-NET, a nonlinear multimodal dynamical model that integrates behavior with multiple neural modalities having distinct statistical characteristics and temporal resolutions. BREM-NET performs multimodal neural fusion during inference while separating behaviorally relevant and residual neural dynamics via a structured learning framework. In a public multimodal non-human primate dataset with simultaneous spiking and local field potential recordings during a 2D reaching task, BREM-NET separates these two types of dynamics and learns them more accurately, as reflected in better behavior decoding, better neural prediction, and stronger latent alignment with behavior, and it retains these capabilities when neural modalities are asynchronous or suffer dropouts, which are major challenges in real-world recordings. This framework provides a new tool for studying behaviorally relevant neural computations across spatiotemporal scales of brain activity.

---


### 248. [PadLoc: Training-Free Floor-Plan Localization by Sparse Geometric Matching](https://arxiv.org/abs/2611.05172)

**<font color=#1a73e8>作者：</font>** Marian Bookhahn, Frank Neumann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose PadLoc, a training-free localization back-end that places a moving sensor within a known floor plan. Floor plans are cheap, persistent, and robust to appearance change, but recent learned-depth methods localize against them by filtering per-frame depth through dense $(x,y,\theta)$ pose grids. PadLoc keeps the swappable depth front-end and replaces the dense grid back-end with sparse geometric matching: dominant wall orientations define a small pose-candidate set, masked normalized cross-correlation scores observed free space against the plan, and a moving-pose Gaussian-mixture Bayes filter plus consensus readout decodes the trajectory. Holding each competitor's depth fixed, PadLoc matches or beats UnLoc's forward filter and the F3Loc filter at every Gibson trajectory length, and UnLoc's offline refinement from $T=35$ on; it exceeds Z-FLoc's published results with a shared MapAnything front-end. On Bonn LiLocBench, PadLoc improves pooled SR@1m over UnLoc by 23-32 pp under wheel odometry and 35-43 pp with ground-truth motion; with full-FOV LiDAR plus wheel odometry the same readout reaches 100% SR@1m at 9-10 cm median error on the static sequence. On the Hilti-Trimble Localization Challenge PadLoc localizes a camera-only fisheye rig on construction floors hundreds of metres across at 0.90-0.98 online SR@2m on three of five sessions; adding learned wall isolation, applied to every session, covers all five at 0.67-0.92 with the localizer unchanged throughout. PadLoc thus matches or outperforms dense grid back-ends while preserving sensor modularity and a compact state that does not grow with trajectory length.

---


### 249. [Stepsize modulation for cross entropy from local quadratic optimization](https://arxiv.org/abs/2611.05191)

**<font color=#1a73e8>作者：</font>** Bruno Bauwens, Viacheslav Krivodub, Bingyu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two methods are presented that perturb a given learning rate schedule in stochastic gradient descent with cross entropy loss.
Both methods use an extra forward pass to estimate various derivatives of the minibatch loss.
The first method selects a value $\eta$ by linearising the softmax values and minimizing the squared error $\tfrac 1 2 ||y - q - \eta q'||_F^2$, where $q$ is the matrix representing the softmax values of the minibatch and $y$ is the matrix with one-hot encodings of the labels. The second method considers a quadratic Taylor approximation of the minibatch loss under the outer approximation of the Hessian. Thus, it minimizes $L(0) + \eta L'(0) + \tfrac 1 2 \eta^2 L''(0)$. Here, the derivatives $L'$ and $L''$ are computed from the derivatives of the logits (using the outer approximation of the Hessian of the loss).
We observe that both methods give very similar values of $\eta$.
Finally, these estimated $\eta$ are used to slightly increase or decrease the learning rate of an existing schedule. The method is evaluated on Cifar10 and Cifar100 datasets for training Resnets, where they decrease the loss faster than the schedule that is perturbed and increase monotonicity. For Cifar10 it also leads to a small improvement of test accuracy, but in Cifar100 test accuracy remains the same.

---


### 250. [From Natural Images to Medical Scans: Transferability of Diffusion Models for Medical Image Generation](https://arxiv.org/abs/2611.05192)

**<font color=#1a73e8>作者：</font>** Efthymios Georgiou, Ioannis Kakogeorgiou, Sarah Brüningk  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transfer learning from natural images is standard in supervised and increasingly adopted in self-supervised medical image analysis, but its role in generative modelling, and in particular diffusion denoisers, remains underexplored. Medical diffusion models typically train the denoiser from scratch, with no systematic evaluation of natural-image transfer. We analyse this across latent and pixel paradigms, model sizes (131M-952M) and two radiology datasets (RadImageNet, BraTS), and ask which aspects of transfer support generation. We find that: i) Natural-image initialisation consistently improves generation, by 21-34% relative gFID in pixel space against 14% in latent space, where the tokeniser supplies much of the prior. gFID gains mirror downstream pathology classification and radiomic-feature FD, both proxies for clinical fidelity. ii) Benefits reflect spatial structure, not semantics: semantic probing does not predict generation quality, whereas a spatial-structure metric adapted to internal denoiser representations tracks gFID at $|r|=0.85$, positioning spatial organisation as a channel through which pretraining manifests. iii) Mixed-domain denoiser training shows that natural and medical images share similar layer-wise representations up to the late blocks, and mixing natural images into medical training improves fidelity. iv) Transfer benefit is tied to natural image initialisation, outperforming in-domain medical pretraining and several reinitialisation schemes. Overall, natural image denoisers transfer positively to medical ones in our setup. Code is available at this https URL

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-280](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
