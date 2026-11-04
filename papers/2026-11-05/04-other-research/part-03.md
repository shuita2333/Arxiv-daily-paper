# 📦 其他研究 | 2026年11月05日

> 本类共 **280** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-280](./part-06.md)

---

### 101. [Proper Agnostic Learning of Affine Halfspaces under Log-Concave Marginals](https://arxiv.org/abs/2611.04344)

**<font color=#1a73e8>作者：</font>** Zhijie Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We give a proper constant-factor agnostic learner for affine halfspaces under full-dimensional log-concave marginals. For arbitrary binary labels, the algorithm uses independent labeled samples and returns a single affine halfspace with error at most $C\mathrm{OPT}+\varepsilon$. Its sample and real-arithmetic complexity are polynomial in dimension, inverse accuracy, and the logarithm of the reciprocal failure probability. The mean and covariance of the marginal need not be known, and the sample complexity can be made linear in this logarithmic confidence factor. The main geometric result compares global disagreement with disagreement on a balanced restriction: for a minority halfspace of mass $p$, global disagreement is within universal constant factors of $p$ times conditional disagreement, provided the latter is sufficiently small. To construct the restriction from noisy labels, we estimate the minority cap's mean and covariance robustly, approximately minimize the classical zonoid-depth dual objective, and expand a superlevel set to a marginal quantile. The disagreement comparison cancels the noise amplification caused by conditioning and allows the learned halfspace to be used on the entire space. The analysis combines degree-four sum-of-squares moment bounds for log-concave laws with a translation-based reduction from balanced affine learning to homogeneous halfspace learning.

---


### 102. [When Is Fresh AI Stock Analysis Worth It? Allocating a Limited Research Budget Across Price Updates, Deep Forecast Refreshes, and Editorial Reviews of Top Stock Picks](https://arxiv.org/abs/2611.04348)

**<font color=#1a73e8>作者：</font>** Russlan Ramdowar  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Must long-horizon AI investment research be rewritten every time stock prices move? Using 8,120 production reports on the same 203 stocks across four iPulse AI batches, we compare repricing existing targets, guarding them against price shocks, mechanically resetting old forecast growth, and generating fresh multi-agent reports. Ten matched configurations represent seven investment frameworks.
Our primary economic evaluation selects Top 10 USD portfolios using one-year forecasts. Across two unchanged-model windows, guarded reuse averages 2.25%, versus 1.66% for SPY and 4.77% for fresh reports, after modeled trading costs and reference compute charges on a USD 100,000 account. Guarded reuse beats SPY in all three short windows, including the model-change transition. Extending the first holding window to nearly six months reverses the result: guarded reuse returns -11.26%, fresh reports +9.12%, and SPY +3.46%, motivating the thesis half-life question.
Supporting quarter-forecast diagnostics show that mechanically re-anchoring old growth paths closes 98% of the MAE improvement over fixed targets, yet Fresh and Reset share only 1-4 of their Top 10 stocks. At Top 30, the unchanged-model portfolio comparison instead favors guarded reuse (4.17% versus 1.88%). Endpoint and concentration tests reveal the influence of horizon choices and exceptional winners. Nine production editions show substantial between-edition turnover, while every final editorial screen retains its own incoming list.
Measured token workloads connect refresh costs to shared capital and realized break-even budgets. The resulting architecture separates continuous price monitoring from episodic thesis rebuilding and targeted editorial evidence checks.

---


### 103. [ReSMap: Recasting Satellite Priors for Robust and Accurate Online HD Map Construction](https://arxiv.org/abs/2611.04352)

**<font color=#1a73e8>作者：</font>** Kyungmin Kim, Sumin Lee, Sungoh Jeong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent advances in camera-based online HD map construction, these systems remain susceptible to sensor failures due to their reliance on onboard cameras. In contrast, satellite images remain available independently of real-time sensing conditions as they are cached offline. Existing methods utilizing satellite images, however, primarily leverage them under nominal conditions, without explicitly addressing them as redundancy when a sensor degrades. To address this gap, we propose ReSMap, a redundancy-aware camera-satellite fusion framework for robust online HD map construction. Our framework explicitly leverages satellite images as a complementary source to improve robustness against camera failures. A Predict-then-Fuse (PTF) module fuses camera and satellite BEV features by using each branch's own prediction confidence as a per-pixel reliability weight, with no learned router. An Object-Centric Cooperative Multi-modal Query (OCMQ) decoder then extends this per-modality separation to the query level: each modality cross-attends only to its own BEV, and per-modality updates are merged through a learned per-token gate. Our model achieves state-of-the-art performance on nuScenes across all splits and range settings. More importantly, it also sets the new state-of-the-art under camera-failure scenarios, demonstrating that satellite images serve not only as a strong prior but as practical redundancy for robust online HD mapping.

---


### 104. [EndoS3:Endoscopic Semantic Splatting SLAM](https://arxiv.org/abs/2611.04358)

**<font color=#1a73e8>作者：</font>** Mona Sheikh Zeinoddin, Benjamin Wright, Zafer Tandogdu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Despite advances in 3D surgical scene understanding, semantic simultaneous localisation and mapping (SLAM) remains under-explored for two key reasons. First, it requires solving three challenging tasks in parallel: camera pose tracking, high-fidelity deformable reconstruction, and semantic mapping, making progress particularly demanding. Second, the scarcity of datasets providing the necessary ground truth to evaluate all three tasks comprehensively under conditions that closely reflect real surgical procedures environments. Method: We propose EndoS3, a Gaussian Splatting-based semantic SLAM framework that uses instance masks to guide all three tasks. An instance-level motion decomposition module separates static and dynamic instances by evaluating residual flow after compensating for camera motion, accounting for flow noise and comparing motion across neighbouring instances. The camera is tracked against the static Gaussians, while an instance-aware warp field gives each dynamic instance its own control nodes and deformation network. A semantic node allocation module redistributes a fixed node budget across instances according to their size and non-rigidity. We also introduce CRCD++, an ex-vivo Cholecystectomy dataset with RGB-D frames, camera pose and instance annotations for full semantic SLAM evaluation. Results: EndoS3 surpasses all state-of-the-art general-purpose and surgical semantic SLAM methods in tracking, reconstruction and semantic mapping on the CRCD++ and SemSup datasets. Conclusion: Semantic-aware motion and deformation modelling is vital to surgical semantic SLAM. EndoS3 and CRCD++ offer a method and benchmark for improved geometric and semantic understanding in endoscopy.

---


### 105. [Benchmarking Unsupervised Jamming Detection in 5G Open RAN](https://arxiv.org/abs/2611.04369)

**<font color=#1a73e8>作者：</font>** Sneihil Gopal, Fernando J. Cintron, Richard A. Rouil  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Radio Frequency (RF) jamming threatens fifth-generation (5G) networks. Open Radio Access Network (Open RAN) telemetry enables jamming detection without dedicated spectrum monitoring equipment, but labeled attack data are rarely available across deployments, motivating unsupervised detectors. Comparing such detectors across algorithmic families, however, remains difficult without ground-truth labels. This paper benchmarks statistical and reconstruction-based unsupervised jamming detectors using a symmetric evaluation interface that combines detection confidence and temporal interval coherence into a detector-independent composite score. We compare a Statistical Ensemble Method (SEM) detector against Vanilla, Long Short-Term Memory (LSTM), and Variational Autoencoder (VAE) baselines on Key Performance Indicator (KPI) telemetry from ten heterogeneous 5G environments with fixed and variable jamming bursts and dynamic jammer gains. Under leave-one-out (LOO) evaluation, SEM achieves a mean composite score of 0.906, compared with 0.688 for the best autoencoder (AE) per fold. Ground-truth validation yields a mean F1-score of 0.918 for SEM, compared with 0.521 for the best AE variant. The composite ranks SEM first in all environments, consistent with F1 rankings. However, in both within-trace and cross-trace evaluation, it fails for detectors that flag far fewer samples than the jamming prevalence, indicating that rankings are reliable only when detection rate matches the expected prevalence.

---


### 106. [Distributed Marginal Return: A Communication-Efficient Algorithm for Multi-Agent Weapon Target Assignment](https://arxiv.org/abs/2611.04370)

**<font color=#1a73e8>作者：</font>** Kamal Mammadov, Glen Pearce, Helen Krause 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The Weapon-Target Assignment (WTA) problem in distributed multi-agent systems is challenged by limited situational awareness and communication constraints. Existing distributed methods, such as auction-consensus algorithms, typically assume task-value independence, a simplification that fails to capture the coupled effects of multi-weapon assignments. This paper introduces the Distributed Marginal Return (DMR) algorithm, a novel decentralized approach that generalizes auction-consensus frameworks. DMR enables agents to compute bids based on marginal return and uses a consensus protocol to resolve conflicts, allowing multiple non-conflicting proposals to be accepted in parallel for cooperative optimization with minimal communication. A key theoretical contribution is our proof that the marginal returns of non-conflicting bids are additive, a property that ensures global consistency and validates our parallel acceptance mechanism. Extensive simulations demonstrate that DMR significantly outperforms baseline algorithms in both solution quality and communication efficiency, offering a scalable and robust solution for real-world distributed command and control applications.

---


### 107. [Embodied AI for Scientific Discovery: From Physical Action to Scientific Evidence](https://arxiv.org/abs/2611.04371)

**<font color=#1a73e8>作者：</font>** Wenhao Xu, Changwei Wang, Shunpeng Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific experiments are increasingly selected, executed and interpreted by learned systems that act through physical interfaces. Robot learning builds physical competence, whereas AI for science chooses which experiment to run, each reporting different endpoints. This review treats their interface as one problem, embodied AI for science, where the experiment itself is partially observed: specimen state, apparatus state and measurement processes are latent, actions are costly and irreversible, and missingness depends on execution and outcome. We organize the literature by three closures operating at distinct levels: operational closure (the experiment realized is the one intended), epistemic closure (the result updates beliefs or selects subsequent experiments) and evidential closure (the record supports a claim). We analyze workflows through a record-linked evidence cycle - Record, Diagnose, Calibrate, Confirm - as analytic functions with feedback. A taxonomy crosses these closures with six delegated decisions and five embodiment classes. Our formulation separates commanded, realized and observed conditions and models diagnosis with explicit resource, risk and sample-change costs. We compare experiment-selection methods by terminal decision, review perception, protocol compilation, visuomotor policies, world models, recovery and transfer by evidence emission requirements, and compare chemistry, materials, biology, microscopy and field workflows by what their records establish. An appendix provides an evidence map of 28 workflows (26 physical, two software-boundary), characterizing validation pathways and claim confirmation requirements. We propose evaluation that separates actions, valid experiments, campaigns and confirmed claims, framing open challenges as controlled comparisons with measurable failure conditions.

---


### 108. [IGSW: Multi-Weather Urban Scene Reconstruction with Intrinsic-Decoupled Gaussian Splatting](https://arxiv.org/abs/2611.04374)

**<font color=#1a73e8>作者：</font>** Zhongquan Wang, Long Cao, Peijia Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity weather editing of 4D scenes can support end-to-end training and closed-loop simulation for autonomous driving. Combining generative image editing with dynamic Gaussian representations enables multi-weather scene reconstruction, but weather-edited images often contain structural distortions. Directly fitting their appearance may propagate errors from teacher images into the reconstructed 4D scene, compromising the original scene structure and temporal continuity. To address these challenges, we propose IGSW, a two-stage framework that combines intrinsic-decoupled 4D Gaussian scene modeling with structure-preserving weather refinement. In Stage I, background Gaussian appearance is decomposed into weather-shared albedo and normals and weather-specific irradiance and residuals. Weather teacher images generated by a diffusion-based image editing model and intrinsic maps estimated by a diffusion-based inverse renderer provide feature-level soft supervision for stable structure and illumination changes. In Stage II, a structure-preservation gate combines semantic conflicts with cross-weather intrinsic discrepancies to suppress unreliable teacher regions. Per-Gaussian weather transport variables and target-weather branches then strengthen the desired weather appearance over the intrinsic-decoupled scene. Experiments on nuScenes and Waymo show that IGSW achieves the highest content similarity and semantic consistency and the lowest temporal error among the compared methods, while retaining pronounced weather-dependent illumination and atmosphere. The project page is available at this https URL .

---


### 109. [Understanding Backdoor Attacks in Scene Graph Generation via Global Context Pathway](https://arxiv.org/abs/2611.04379)

**<font color=#1a73e8>作者：</font>** Xiaoguang Chang, Tuo Chen, Chengze Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene Graph Generation (SGG) produces structured scene representations, yet its training-time backdoor risk remains unexplored. Unlike classification, SGG exposes a pair-level attack surface that enables selective corruption of relations involving a designated object category. However, because SGG largely relies on localized evidence, globally placed triggers may face difficulty in manipulating such predictions. Recent SGG architectures increasingly incorporate global context to improve scene modeling, which may in turn facilitate such attacks. In this paper, we systematically study this backdoor risk and investigate the role of the global context pathway in backdoor behavior. Concretely, we first instantiate this attack with an effective method, and propose a three-axis evaluation protocol to characterize backdoor behavior. Experiments on Visual Genome with representative open-vocabulary and closed-set SGG models demonstrate the effectiveness of the attack. Mechanistic analyses reveal that the explicit global context pathway serves as a major carrier of the backdoor effect across the evaluated SGG models. In particular, replacing the poisoned global context representation with its clean counterpart during inference sharply suppresses the attack, yielding 100% and 97% reductions in attack success for the OvSGTR family and RelationFormer, respectively. Moreover, training-time interventions in the OvSGTR family show that suppressing trigger signals in this pathway either reduces attack success or substantially degrades utility. Together, these findings suggest that explicit global context designs may pose a backdoor risk in SGG architectures.

---


### 110. [Spin Spherical Fourier Neural Operators: Efficient Equivariant Learning for Vector and Spin Fields on the Sphere](https://arxiv.org/abs/2611.04389)

**<font color=#1a73e8>作者：</font>** Kevin Mulder, Matthew A. Price, Eirini Leftaki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many fields of physical interest on the sphere, such as wind, the polarisation of the cosmic microwave background and the shear of weak gravitational lensing, are spin fields, whose values change phase when the local frame rotates. We extend spherical Fourier neural operators (SFNOs) to fields of any spin, through lifted spherical convolutions that are exactly rotationally equivariant. Lifting spin fields to Mackey functions on the rotation group provides the conceptual framework, while computation is performed exactly and efficiently through their harmonic representation and by appealing to sampling theorems on the sphere and rotation group. We construct spin SFNOs (S$^2$FNOs) from these building blocks. We demonstrate empirically that rotational equivariance holds to machine precision for these layers. We achieve state-of-the-art performance on existing benchmarks, and introduce new benchmarks on which spin-aware models outperform their scalar counterparts.

---


### 111. [Auditing Targetless Camera-LiDAR Extrinsic Correction before Recursive Use](https://arxiv.org/abs/2611.04397)

**<font color=#1a73e8>作者：</font>** Bo Ma, Weiqi Yan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-LiDAR fusion repeatedly uses an extrinsic transform in projection, association, and recursive state estimation. We study whether a targetless correction should be admitted to a downstream consumer only after separate audits of correction quality, confidence ranking, and recursive risk. Our log-disjoint protocol evaluates these stages under synthetic extrinsic drift on Argoverse 2 and treats cross-dataset and odometry experiments as bounded diagnostics.
On 27 test-split logs, single-frame Canny alignment is harmful in the mild tier. Multi-frame alignment improves severe-tier rotation by 2.52 degrees but worsens translation by 0.177 m; its declared joint error-magnitude improvement is also negative (-0.158, 95% CI [-0.223, -0.098]), so the rotation gain is not a six-degree-of-freedom correction success. A zero-injection check moves away from the true extrinsic, and solver-disagreement AUROC on selected splits does not yield a validated nonzero-coverage risk-coverage operating point.
In a 15-log final system role, the locked conservative policy admits no candidate and equals Raw, whereas Always-correct increases trajectory error. These results support an auditable separation of correction, confidence, and recursive contamination; they do not establish a deployable calibration gate, positive odometry or SLAM improvement, map consistency, or closed-loop safety.

---


### 112. [Silent Instrument Errors Reorder Agent Leaderboards](https://arxiv.org/abs/2611.04399)

**<font color=#1a73e8>作者：</font>** Yangze Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On a public agent leaderboard, a general-purpose agent trails a scaffold built for an airline customer-service benchmark by 13 points on the tasks that touch its database, and a reader could conclude that generality costs accuracy. The gap comes from the grader. The general agent often ends its conversations in a way that never triggers grading, so only about half of its episodes were scored and the rest were stored as failures. Grading the ungraded half under the benchmark's own rule closes the pooled gap, without rerunning any agent. We audit two carefully maintained public leaderboards, HAL and tau2-bench, from their published artifacts alone and find three more instrument errors. A cost column counts nested model calls twice, unevenly across rows. Archived trajectories record grader-written actions as agent actions. Re-grading saved trajectories under a newer evaluator is itself a new measurement: a correct and announced fix reorders a leaderboard, and a mode check that misreads four files collapses their scores by 59 to 82 points while printing no error. Each produced a plausible number, and the HAL maintainers confirmed their three within five weeks. Together the cases show that the infrastructure of agent evaluation, meaning the code that grades, logs, replays and versions an evaluation, is part of the measurement and fails silently, so scores and orderings can move with no visible sign. These failure modes follow from how agent evaluation pipelines are built, and those pipelines change as fast as the agents they measure, so we expect more of them elsewhere. We propose cheap checks that expose the instrument: report the graded fraction, aggregate cost from root spans, tag the provenance of every recorded action, and pin evaluator versions with a published re-grade diff.

---


### 113. [DR-LiteNet: A Lightweight Explainable Hybrid CNN Framework for Imbalanced Diabetic Retinopathy Grading via Adaptive SMOTE Fusion](https://arxiv.org/abs/2611.04405)

**<font color=#1a73e8>作者：</font>** Nishi Kanta Paul, Md Shihabul Islam Shovo, Audrija Chowdhury 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated diabetic retinopathy (DR) grading from colour fundus photographs is held back by two compounding challenges: severe class imbalance across five severity grades and the heavy computational cost of large scale architectures in resource constrained clinical settings. We introduce DR-LiteNet, a dual branch hybrid convolutional neural network that tackles both problems at once. The CNN branch extracts 1,280 dimensional deep features through EfficientNetB0, while the handcrafted (HC) branch produces a compact 51 dimensional lesion descriptor capturing vessel density, exudate intensity, texture entropy, and HSV colour histograms. Concatenating both branches yields a 1,331-d hybrid embedding, on which Adaptive SMOTE (ADASYN) is applied during training to synthesise minority class feature vectors, correcting distributional skew without touching the image space. A two phase training protocol first warms up the classification head on balanced features, then fine tunes the full network end to end. Grad CAM saliency maps deliver post-hoc clinical explainability. Tested on APTOS 2019 under five fold stratified cross validation, DR-LiteNet reaches 88.77% +/- 0.61 accuracy, a quadratic weighted kappa (QWK) of 0.884 +/- 0.010, and a macro F1 of 0.792 +/- 0.008 with only 4.69 M parameters beating ResNet50 (23.5 M) by DeltaQWK = 0.022 while staying practical on a single Google Colab T4 GPU. The source code of this project is available at: this https URL.

---


### 114. [LCM-UNet: Scale-Selective Mamba with Reparameterizable Multi-Basis Local Modeling for Lightweight Skin Lesion Segmentation](https://arxiv.org/abs/2611.04409)

**<font color=#1a73e8>作者：</font>** Md Shihabul Islam Shovo, Nishi Kanta Paul, Dip Kumar Saha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate lesion segmentation underpins automated dermoscopic analysis: masks enable measurements of asymmetry, border and size. Deployment in primary care or on mobile devices requires a compact network. Existing ultra-light Mamba U-Nets offer global context, but global-modeling cost depends on each Mamba block's resolution, while their local branches rely on a single square kernel. We introduce LCM-UNet, a 33,474-parameter U-shaped network that fuses every skip at its native resolution, restricts bidirectional Mamba to stages at one-sixteenth of the input resolution or coarser, and uses local convolutions at finer scales. A multi-basis reparameterizable adapter augments each local branch during training with dilated, horizontal and vertical depthwise kernels, then folds them into the host kernel before inference. Each skip connection also learns a stage-specific gain. Nine networks were retrained on the official ISIC 2017 and ISIC 2018 partitions under a harmonized protocol, with PH$^2$ reserved for external validation and ablations run on a development split. LCM-UNet achieved Dice scores of 88.62%, 89.73% and 90.46% on ISIC 2017, ISIC 2018 and PH$^2$, respectively, ranking first on both ISIC test sets and second on PH$^2$ among the compared models. In the native-resolution host, removing Mamba from the one-eighth-resolution decoder stage eliminated 63% of Mamba operations, corresponding to 5.3% of all operations, with a Dice change of $-0.03$ percentage points. The adapter improved Dice by 0.48 percentage points over a single host kernel without adding deployed parameters or operations. With latency so far measured only on a GPU, LCM-UNet is a candidate for resource-constrained deployment.

---


### 115. [CaliSplat: Sparse Gaussian Fitting and Calibrated Rate Allocation for Image Compression](https://arxiv.org/abs/2611.04413)

**<font color=#1a73e8>作者：</font>** Zhenbang Zhang, Zhengquan Luo, Kai Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> 2D Gaussian representations provide an explicit and lightweight alternative for image representation, enabling fast deterministic decoding without a heavy neural synthesis network. However, existing per-image Gaussian codecs still require costly image-specific optimization to determine how limited Gaussian capacity should be distributed across heterogeneous regions. We introduce CaliSplat, an optimization-efficient Gaussian image codec that selectively explores candidate representations and globally allocates a constrained Gaussian budget. We exploit the closed-form reconstruction error of the single-Gaussian case as an inexpensive measure of local difficulty, fitting higher-capacity candidates only in regions where additional Gaussians are likely to be useful. To reduce selection errors caused by mismatched convergence rates across candidate sizes, a small set of longer-horizon fits is used to calibrate short-horizon distortion estimates before global budget-aware selection. The selected representation is then compressed into a bitstream. Across standard and large image datasets, CaliSplat achieves competitive or superior rate--distortion performance while reducing per-image fitting time by $3.0\times$--$15.7\times$ compared with representative Gaussian codecs. It further maintains high-throughput deterministic decoding at $175.9$--$478.2$~MP/s. These results demonstrate that content-adaptive Gaussian compression can substantially reduce per-image optimization cost while preserving strong reconstruction quality and efficient explicit decoding.

---


### 116. [SphereFlow: Missing Modality Imputation via Geometric Transport on Hypersphere](https://arxiv.org/abs/2611.04414)

**<font color=#1a73e8>作者：</font>** Huihan Wang, Juncheng Wang, Yuxiang Feng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Missing modality imputation aims to synthesize unobserved modalities from observed ones. Existing methods treat each modality as living on its own latent manifold, forcing the generator to learn a long, unstructured jump between them. We present SphereFlow, which takes a fundamentally different view: by projecting all modalities into a shared hyperspherical latent space via a frozen self-supervised encoder, cross-modal imputation reduces to short-range geometric transport between nearby points on the sphere. Realizing this idea with flow matching, however, exposes two geometric conflicts: the standard Gaussian noise source is catastrophically mismatched with the unit-norm data manifold, and the linear interpolation path departs the sphere surface into a region where the decoder has no training signal. We resolve both with simple, geometry-aware modifications: replacing the noise source with the observed-modality latent so that the velocity field learns only the cross-modal displacement, and training the decoder with a time-weighted loss that extends its domain to the near-surface region traversed by the flow. We prove that this data-as-source formulation reduces the worst-case off-manifold deviation from a quantity that grows with the latent dimension to a small, dimension-independent bound governed by inter-modality similarity. Experiments on BraTS multi-modal MRI imputation and CT-MRI translation demonstrate state-of-the-art generation fidelity across all settings, while downstream brain tumor segmentation with our imputed data closes roughly eighty percent of the gap to the full-modality oracle. Code is available at this https URL.

---


### 117. [Efficient and Faithful High-Resolution Image Editing with Sparse Cross-Resolution Denoising](https://arxiv.org/abs/2611.04416)

**<font color=#1a73e8>作者：</font>** Maosen Zhao, Xianfang Zeng, Pengtao Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-based image editors still primarily operate at 1K, whereas practical editing increasingly requires faithful 2K/4K outputs. Dense high-resolution adaptation preserves the editing trajectory but incurs expensive target-source attention; editing at 1K followed by external refinement is cheaper but can separate detail restoration from the editing trajectory. We introduce FLASH, a native high-resolution editor based on sparse cross-resolution denoising. A frozen 1K branch provides a semantic and structural anchor, while a target-resolution branch reconstructs local detail within the same Transformer. An asymmetric topology retains full 1K attention, guides high-resolution queries with spatially aligned low-resolution noisy-target states, and confines high-resolution target-reference interaction to local Halo neighborhoods. Resolution-specific diffusion-state mapping and spatial YaRN adapt the pretrained editor to larger grids. An optional, training-free progressive path replaces early high-resolution denoising with a 1K prefix and completes refinement in the same editor. On VINS-4KEval, the direct model achieves the strongest structural fidelity among the compared methods at both 2K and 4K. A separate 4K forward benchmark with R = 1 records 4.2x faster total forward execution and 25.3x faster attention than dense target-reference attention. Progressive inference reduces end-to-end 4K latency by 30.5%, with a modest quality cost.

---


### 118. [VidUEU-Agent: A Data-Curation Agent for Multimodal Understanding, Editing, and Unified Tasks](https://arxiv.org/abs/2611.04418)

**<font color=#1a73e8>作者：</font>** Tengju Ru, Weitong Lian, Zecong Tang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The advancement of multimodal learning is heavily constrained by the scarcity and high annotation cost of high-quality instruction data. While raw videos offer an abundant and dynamic source of visual knowledge, transforming them into precise instruction data remains highly challenging. To bridge this gap, we present VidUEU-Agent, an automated pipeline that synthesizes instruction data from raw videos for multimodal understanding, editing, and unified tasks. VidUEU-Agent follows a four-stage pipeline: it performs global perception to filter low-quality shots, mines keyframes and multimodal signals, constructs metadata and routes the metadata to synthesize instruction samples. More importantly, our agent framework can autonomously iterate the data distribution based on downstream training results, thereby optimizing data quality, balance, and training effectiveness. Scaling this pipeline, we construct VidUEU-100K, a large-scale dataset of 100K training samples spanning multiple domains and tasks, providing a robust foundation for developing comprehensive multimodal capabilities. Extensive experiments demonstrate that fine-tuning baseline models on VidUEU-100K yields significant and consistent performance gains across diverse representative benchmarks, validating the effectiveness of our proposed agent framework and dataset.

---


### 119. [GVT3D: Gesture-Vision-Text Token Enrichment for 3D Embodied Reference Understanding](https://arxiv.org/abs/2611.04422)

**<font color=#1a73e8>作者：</font>** Vimarsh Shah, Dulanga Weerakoon, Ajinkya Deshpande 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Natural human-robot interaction requires robots to interpret language and gestures within a 3D environment to support tasks such as pick-and-place and object retrieval. 3D Embodied Reference Understanding (3D-ERU) supports this by identifying the 3D location of a target object from a scene (point-cloud) containing a human pointing gesture and an accompanying language description. However, current 3D-ERU models lack alignment of cross-modal representations and incur high processing costs that increase with the point-cloud's size. To address this, we propose GVT3D, which employs an Embodied Fusion module that jointly models language, gesture, and vision inputs within a shared embedding space, promoting cross-modal alignment. We additionally introduce a foveation approach that selectively processes the point cloud within a coarse region around the estimated pointing direction to reduce computations. GVT3D achieves ~8% higher accuracy and foveation enables 2.95x faster execution while maintaining comparable accuracy, relative to prior 3D-ERU models.

---


### 120. [SWAP-INR: Implicit Neural Representation with Switchable Attention Paths for Time-varying Multivariate Scientific Data Compression](https://arxiv.org/abs/2611.04423)

**<font color=#1a73e8>作者：</font>** Hyunsoo Son, Jeonghyun Noh, Chaoli Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visualizing multivariate scientific simulation data is essential for understanding complex physical phenomena, yet the massive scale of such data imposes a severe storage bottleneck in high-performance computing environments. Implicit neural representations (INRs) have emerged as a promising continuous alternative to traditional lossy compressors, but existing methods struggle to explicitly capture cross-variable interactions and to adapt to the diverse spectral characteristics of physical variables. To address these limitations, we propose SWAP-INR, an architecture for high-fidelity compression of multivariate, time-varying simulation data. SWAP-INR introduces two key components: (1) The switchable attention path (SWAP) module explicitly models cross-variable interactions through a cross-variable attention layer, then routes each variable to an attention or non-attention path by a deterministic, loss-driven criterion, and prunes the inactive layers for structural compression. (2) The adaptability amplification SIREN (A2-SIREN) replaces rigid frequency scaling with channel-wise learnable modulation, adapting to heterogeneous physical features with negligible overhead. Combined with post-training 16-bit quantization, SWAP-INR achieves state-of-the-art performance on small modular reactor (SMR) datasets and remains competitive on public physics simulation datasets, while maintaining a constrained memory footprint. Our code is this https URL.

---


### 121. [A Systematic Point Cloud Edge Detection Framework for Automatic Aircraft Skin Milling](https://arxiv.org/abs/2611.04435)

**<font color=#1a73e8>作者：</font>** Zijie Wu, Yaonan Wang, He Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The edge detection technique is an essential step for aircraft skin milling in aviation manufacturing. Most of the current detection methods focus on traditionally defined edge extraction tasks but disregard the crucial systematic requirement of edge milling. In this paper, we proposed a novel edge detection framework for automatic edge milling of aircraft skins. First, an edge probability detector is proposed by the spatial tangent continuity (STC) to provide the essential reference. Second, we propose a hierarchical branch searching (HBS) method to hierarchically strip the desired milling edges from the raw point cloud, which consists of three graded progressive steps: branch backbone generation, branch extension, and branch pruning. We demonstrate the performance of the proposed method on both synthetic models and aircraft skin workpieces. The proposed method outperforms the other baselines and shows accurate edges for the edge milling task.

---


### 122. [DynOSeg: Dynamic Object Segmentation via Motion-Geometry Fusion](https://arxiv.org/abs/2611.04452)

**<font color=#1a73e8>作者：</font>** Xu Han, Yiduo Wang, Yiran Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Moving Object Segmentation (MOS) detects and separates dynamic objects from the static background in a video, which plays a fundamental role in dynamic-scene understanding. Most MOS methods rely on pure visual motion cues alone, such as optical flow or point tracks, which is inherently ambiguous due to the compounded camera and object motions as well as motion-induced appearance changes, e.g. shadows and reflections. Naive fusion of additional information such as depth and semantics, however, cannot leverage their complementarity to the fullest extent. We therefore propose DynOSeg, a novel MOS approach that takes on a two-stage fusion structure. DynOSeg first combines a geometry-aware residual map and depth encoding into a geometric representation of motion, delineating camera motions and object dynamics. We then further incorporate semantic features to refine object understanding. We have additionally curated a diverse training corpus including CARLA-MOS, a new synthetic urban-driving dataset for MOS training. Our experiments show that DynOSeg consistently outperforms published state-of-the-art MOS methods across a diverse range of datasets. Our code and pretrained models can be found at this https URL

---


### 123. [A Security Analysis of Verifiable Credential Verification Pipelines: Attack Surface Arising from JSON-LD/RDFC Canonicalization Compared with SD-JWT VC and mdoc](https://arxiv.org/abs/2611.04461)

**<font color=#1a73e8>作者：</font>** Naohiro Fujie, Shigeya Suzuki  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We evaluate, at implementation level and under an explicit threat model, the verification pipelines of three Verifiable Credential (VC) formats: SD-JWT VC; the W3C Verifiable Credentials Data Model 2.0 with the Data Integrity cryptosuite eddsa-rdfc-2022 (W3C VCDM); and mdoc (ISO/IEC 18013-5). For W3C VCDM we identify and exercise three structural attack surfaces from remote context resolution and RDFC-1.0 canonicalization: denial of service (DoS) via poison graphs, context injection through @context, and server-side request forgery (SSRF) reachable via malicious URLs, all at default settings. A poison graph, whose blank-node references are symmetric enough to force RDFC-1.0 into deep recursion, raises it to 278x the baseline from five blank nodes in 527 bytes, and to 13.5 s from eight. Every experiment ran in four environments sharing runtime and library versions; the multiple moves with the machine (251--424x for one input), not with its speed. Cost tracks that symmetry rather than the node count: an acyclic input with 1,500 blank nodes stays at 462--714x. A call limit separates the two: every attack family aborts at 16 or below, every legitimate credential completes at 1, but a shallow, wide recursion, such as the acyclic control, passes whatever the bound. DoS does not presuppose adversarial input: with production education schemas, canonicalization costs 23--34x a simple credential in one environment, 16--49x across four. Effective mitigations are a static document loader, which removes the retrieval latency and both remote-context surfaces; a context allowlist; and a call limit with a size bound. SD-JWT VC and mdoc need neither canonicalization nor external references, and our verifiers resisted every vector evaluated. These are not format-specific defects but properties of the pipeline and its configuration.

---


### 124. [SaMA: Morpho Adaptation via Asymmetric Expansion of Kronecker Product](https://arxiv.org/abs/2611.04462)

**<font color=#1a73e8>作者：</font>** An Nguyen, Anh Tong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) has attracted significant attention in the parameter-efficient fine-tuning (PEFT) landscape. However, its design suffers from two fundamental limitations. First, its invariance manifold induces flat directions in the loss landscape, creating an optimization bottleneck for adaptive optimizers. Second, its effective rank scales only linearly with the parameter budget. In this paper, we propose Scalable Morpho Adaptation (SaMA), a PEFT method grounded in a principled generalization of the Kronecker product. By relaxing the shared-block constraint in the perfect-shuffle factorization, SaMA spans from low to full rank and achieves a practical rank that scales quadratically with the parameter budget, up to full-rank. Furthermore, we show that its invariance manifold collapses to a diagonal group, making it structurally more optimizer-friendly. Empirically, SaMA consistently outperforms strong PEFT baselines on commonsense and arithmetic reasoning benchmarks while being more parameter-efficient.

---


### 125. [Is Forgetting Unified? Exploring Concept Unlearning in Unified Multimodal Models](https://arxiv.org/abs/2611.04467)

**<font color=#1a73e8>作者：</font>** Zhongkai Xue, Junkai Chen, Mingcong Lei 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) integrate image generation and visual understanding, but are existing single-pathway unlearning methods sufficient to suppress target concepts across both? In this work, we study cross-pathway concept unlearning. Our goal is to prevent a model from both generating images of a target concept and identifying it in input images, while preserving other capabilities. To this end, we introduce UUBench, a diagnostic benchmark covering 30 target concepts and 60 semantically related neighboring concepts. Experiments on representative UMMs show that the evaluated single-pathway methods achieve limited joint forgetting: generation-side editors strongly suppress target generation but yield limited forgetting in visual understanding, while understanding-side baselines struggle to achieve substantial forgetting even in their own pathway. Their direct composition also yields limited joint forgetting. We therefore propose UniForget, achieving joint forgetting rates of 80.0% on BAGEL-7B-MoT and 92.7% on Janus-Pro-7B, outperforming representative baselines. Further analysis reveals trade-offs between joint forgetting and capability preservation.

---


### 126. [Using GeoAI and machine learning tools for consistent high-resolution land cover mapping based on time-series NAIP imagery](https://arxiv.org/abs/2611.04470)

**<font color=#1a73e8>作者：</font>** Jie Liu, Xusheng Tang, Chao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution land-cover maps support ecological monitoring, but consistent historical time series remain scarce because aerial imagery varies across years and sensors. We developed a dual-track workflow to produce temporally coherent 1-m land-cover maps from National Agricultural Imagery Program (NAIP) imagery without historical training samples. For higher-quality imagery from 2009-2017, we used a pretrained U-Net/ResNet-34 model and refined boundaries with the Segment Anything Model (SAM). For lower-quality imagery from 2004-2008, we reconstructed land cover through an NLCD-based spatiotemporal bridging and label back-casting pipeline. Evaluation across six counties in North Carolina and Pennsylvania yielded overall accuracies of 0.887 (2014), 0.886 (2017), and 0.733 (2004). Structure, Water, Wetland, and Cropland consistently achieved high F1-scores. The workflow integrates GeoAI and multiple data sources to address temporal heterogeneity in historical aerial imagery, supporting high-resolution land-change analysis and landscape planning across the conterminous United States.

---


### 127. [KeyWise: Efficient Video-Only Piano Transcription with a Lightweight Per-Key Architecture](https://arxiv.org/abs/2611.04476)

**<font color=#1a73e8>作者：</font>** Anastasios Chatzigiannis, Natalia Panagou, Maria Koziri  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-based piano transcription is hampered by the sustain pedal and by noisy or missing soundtracks, problems that video-only transcription avoids, since a top-view video shows directly when each key is pressed and released. Most visual transcription networks, however, describe the whole keyboard with one global feature vector and must learn where each key is. In this paper, we propose KeyWise, a lightweight per-key architecture that exploits the known geometry of the keyboard instead of learning it. The rectified keyboard is divided into 88 equal tiles that serve as regions of interest (ROIs), and one small recurrent network, shared by all keys, follows each key over time. On PianoVAM, KeyWise reaches the onset accuracy of the state-of-the-art V2N (95.0% vs. 94.7% onset F1 at 50 ms and 97.8% vs. 97.0% at 100 ms) with 1.3 M instead of 28.2 M parameters, and it runs 4.7 times faster on the same GPU. At 100 ms, it is also significantly more accurate when the key releases (97.0% vs. 95.5% F1) or the velocities (89.4% vs. 84.5% F1) must be correct as well. On PianoYT, KeyWise pre-trained on PianoVAM reaches 69.4% onset F1 at 100 ms, comparable to the best published result, although it needs fine-tuning for new recording conditions.

---


### 128. [A Parametric Linear Conic Projection for Structured Sparse Attention](https://arxiv.org/abs/2611.04479)

**<font color=#1a73e8>作者：</font>** Michel Barlaud, Clement Genninasca, Maxime Zanella 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce the Cone Alignment Index (CAI), a scale-invariant sparsity measure associated with a Lorentz-cone geometry. We provide a probabilistic analysis of the distribution of the CAI score, including a general theorem and explicit corollaries for Gaussian and uniform distributions. As a consequence, we show that, in the high-sparsity regime, the probability that the samples lie within the convex cone tends to one. Building upon this formulation, we derive two complementary projections: the \emph{Parametric Linear Conic Projection} (PLCP), an efficient closed-form approximation, and the \emph{Parametric Euclidean Conic Projection} (PECP), the exact Euclidean projection onto the cone boundary.
Our analysis establishes several fundamental theoretical properties. We prove that PLCP and PECP are collinear, differ only by a positive radial scaling factor, and induce exactly the same sparsity threshold, thereby preserving an identical active support. Furthermore, we derive a support-identification theorem showing that, for any prescribed sparsity level $l<n$, the number of coefficients discarded at each iteration is theoretically controlled.
Building on this theoretical foundation, we develop a bilevel PLCP framework for structured matrix sparsification. The proposed method naturally generates hardware-friendly structured sparsity patterns, including row-wise, column-wise, and diagonal masks, making it particularly well suited for accelerating Transformer attention mechanisms.

---


### 129. [Goal-Driven Autonomous Optical Experimentation via a Self-Recursive Hardware-Software Harness](https://arxiv.org/abs/2611.04481)

**<font color=#1a73e8>作者：</font>** Tianxing Zhu, Huacheng Lu, Ming Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose goal-driven self-recursive optical research in which agents use physical evidence to revise the hardware, software, models, and protocols used to pursue a scientific goal. The framework can be instantiated with different stimulus systems and measurement devices. We formalize its updates and derive a relation between physical attainability, command access, and model approximation error. We demonstrate the concept in an optical see-through color-matching case study using an iPad, RayNeo X3 glasses, and a TOP 300 probe coupled to a CAS140D spectroradiometer, both from Instrument Systems. A revised glasses application adds USB-controlled RGB holds and frame acknowledgements, keeping model-generated colors displayed during spectral acquisition. The interface passes 12 live control checks. Spectral feedback reduces one target color difference from 19.756 to 1.211 {\Delta}E_76^*; all five targets improve in a separate comparison. These measurements demonstrate the concept in one configuration. The resulting software and protocols remain available for subsequent investigations.

---


### 130. [Reconstruction-Based Diagnosis through Gödel-Regularized Virtual Observability](https://arxiv.org/abs/2611.04487)

**<font color=#1a73e8>作者：</font>** Oliver Niggemann, Jonas Ehrhardt, Alexander Diedrich  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Not every component in a technical system can be equipped with sensors. Hence, when a fault occurs, available sensors often detect it only after its effects have propagated. This makes the isolation of faults difficult. We approach this problem by introducing virtual sensors. For each combination of component and fault type, we let external knowledge describe the fault-sensitive variables. We introduce a novel neural observer that is only trained on normal data. For fault isolation, it uses available sensor measurements where it is possible and reconstructs missing variables as virtual sensors to predict normal behavior. It detects deviations between current values and nominal predictions and computes local symptoms, which are then compared by onset time. The result is a set of root causes describing the faulty behavior. We use Gödel logic to encode physical knowledge and guide training. We evaluate our approach on synthetic networks, the Tennessee Eastman Process, and datasets of two modular production plants.

---


### 131. [Polarimetric Scattering-Structure Contrastive Learning for Few-Shot HRRP Recognition](https://arxiv.org/abs/2611.04490)

**<font color=#1a73e8>作者：</font>** Fangyi Wang, Peng Zhao, Haipeng Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot high-resolution range profile (HRRP) recognition is challenged by strong aspect-dependent variation and sparse novel-class support. We propose polarimetric scattering-structure contrastive learning (PSS-CL), which supplies an episodic HRRP encoder with a structured physical training view. Dominant local responses are represented by their soft affinities to canonical polarimetric mechanisms, normalized range locations, and energy contributions. A symmetric cross-view objective transfers this scattering structure to the learned HRRP representation, while episodic prototype learning supports novel-class inference without the physical branch. We conduct Random-aspect and Cross-aspect experiments on a six-class measured dataset. In Cross-aspect 1-, 3-, and 5-shot recognition, PSS-CL achieves 81.73%, 86.92%, and 90.98% mean class accuracy (MCA), respectively, outperforming the best competing results by 5.62%, 3.09%, and 3.56%.

---


### 132. [SPA-Q: Structure-Preserving Adaptive Post-Training Quantization for Monocular Depth Estimation](https://arxiv.org/abs/2611.04491)

**<font color=#1a73e8>作者：</font>** Jaemin Choi, Jincheol Yang, Nahyun Lim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth estimation (MDE) has advanced rapidly with the emergence of foundation models such as Depth Anything. Their transformer-based architectures provide strong generalization across diverse scenes and domains, but also incur high computational and memory cost, making efficient deployment challenging. Post-Training Quantization (PTQ) provides an efficient and practical solution for model compression, yet low-bit PTQ remains challenging for MDE models. When applying PTQ to Depth Anything, we identify two key challenges: (i) independently minimizing the quantization error of the query and key projections fails to preserve the attention maps induced by their interaction, and (ii) quantization errors accumulate across layers, resulting in intermediate feature distribution shifts. To address these issues, we propose SPA-Q, a Structure-Preserving Adaptive PTQ framework for MDE, consisting of two main components. First, Attention-Preserving Calibration (APC) determines query and key quantization parameters by matching the full-precision attention distribution. Second, Channel-Wise Distribution Alignment (CWDA) learns channel-wise affine transformations to mitigate quantization-induced distribution shifts, and the learned parameters are absorbed into the weights after training. Experimental results show that SPA-Q consistently outperforms existing PTQ methods under 4-bit quantization, achieving an average 25.9% reduction in AbsRel and a 17.3% improvement in $\delta_1$ across NYUv2 and KITTI datasets.

---


### 133. [Spatial Memory for AR Glasses: Hierarchical Visual Acquisition and Source-Linked Recall](https://arxiv.org/abs/2611.04494)

**<font color=#1a73e8>作者：</font>** Tianxing Zhu, Dan Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a spatial-memory system that enables optical see-through AR glasses to recall earlier physical encounters. The dual-camera prototype combines hierarchical visual acquisition with source-linked storage and staged retrieval. Quality screen-ing, global and regional appearance novelty, and temporal support select monochrome observations for detailed RGB cap-ture. Semantic observations retain links to their source images, allowing retrieval to answer indexed historical questions direct-ly or inspect visual details omitted from scene descriptions. The architecture separates capture acceptance, interpretation out-come, and support for a particular question. This distinction motivates two core control mechanisms: bounded reassessment of familiar views when earlier processing leaves an evidence gap, and retention guided by source dependencies. In a 131.35 s egocentric replay, the implemented acquisition policy selected six RGB views from 648 monitoring observations, while feature extraction ran on 97.7% of observations. These results demon-strate selective RGB acquisition and identify frequent local inference as a remaining cost. Exposure duration and cross-view timing further constrain the evidence preserved from se-lected encounters. The system provides a practical acquisition-to-recall architecture for persistent AR assistance, with explicit boundaries between captured evidence, indexed interpretations, and supported historical claims.

---


### 134. [3DGS-VBench+ and 3DGSV-Assessor: A Multi-Dimensional Subjective Benchmark and a Reference-Flexible Objective Model for 3D Gaussian Splatting Video Quality Assessment](https://arxiv.org/abs/2611.04498)

**<font color=#1a73e8>作者：</font>** Yuke Xing, William Gordon, Jiarui Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) enables real-time novel view synthesis (NVS), but its heavy storage makes compression essential, and both training and compression introduce representation-specific distortions. Since generative compression in many methods treats geometric and color attributes via different parameters, it can induce dimension-specific distortions, motivating multi-dimensional assessment. Moreover, real-world captures generally lack an aligned ground-truth video for a synthesized, continuous camera trajectory, leaving only sparse captured views as references. To enable multi-dimensional quality assessment of 3DGS videos with scarce aligned references, we first present 3DGS-VBench+, a large-scale subjective video quality assessment (VQA) benchmark comprising 3{,}036 3DGS reconstructions, each paired with a rendered video, across 11 real-world and 22 synthetic scenes, generated by 6 representative compression algorithms at systematically designed levels and annotated with 9{,}108 MOSs covering overall, geometry, and color quality. Based on 3DGS-VBench+, we propose 3DGSV-Assessor, a reference-flexible, large multimodal framework that scores all three dimensions in one generation pass and fuses a ranking-based reference cue into the frozen regressor through a bounded gate, supporting both reduced-reference (RR) and no-reference (NR) assessment. Extensive experiments demonstrate state-of-the-art correlation with human perception on 3DGS-VBench+ and strong zero-shot generalization to other NVS benchmarks. The dataset and code will be released at this https URL.

---


### 135. [Sample-Grained Approximate Unlearning with Provable Per-Sample Bounds](https://arxiv.org/abs/2611.04501)

**<font color=#1a73e8>作者：</font>** Yaxin Xiao, Yulin Jin, Li Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to erase the influence of a designated forget set from a trained model while preserving strong utility on the retain set. Approximate unlearning methods efficiently achieve this goal without full retraining, but their effectiveness is primarily assessed using dataset-level aggregate metrics. These aggregate metrics can mask deviations from retraining at the level of individual samples. In this work, we focus on per-sample unlearning effectiveness. We introduce SALA (Sample-grained Likelihoods ALignment), a plug-in optimization framework that enables approximate unlearning methods to operate at the level of individual samples by steering each example toward its correct target distribution. To quantitatively assess this behavior, we further propose the sample-grained distribution gap, a metric that captures per-sample discrepancies between approximate unlearning and exact retraining output distributions. We provide theoretical guarantees showing that SALA contracts this gap and yields a bounded per-sample discrepancy to retraining. To make this framework practical, we develop a low-cost estimation method for the member and non-member target distributions. Extensive experiments on classification and generation tasks demonstrate that SALA reduces the sample-grained distribution gap by up to $86.67\%$ when paired with existing approximate unlearning baselines, while also improving robustness to unlearning hyperparameters.

---


### 136. [Variational Learning with Lie Group Exponential Families](https://arxiv.org/abs/2611.04513)

**<font color=#1a73e8>作者：</font>** Eren Mehmet Kıral, Thomas Möllenhoff, Koichi Tojo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Variational Bayesian learning for deep neural networks offers many potential benefits. The difficulty in implementation arises from constraints on the parameters of the variational distributions, as well as the need for low-variance gradient estimators. Our recent work proposes Lie group methods for multiplicative or affine groups that naturally overcome such difficulties. Lie groups are essentially parameter spaces with a binary operator such as addition or multiplication, which allows for natural updates within the parameter space. In this article, we streamline and extend our Lie group framework to any general Lie group, and give an explicit relation to standard natural-gradient variational learning methods such as the Bayesian learning rule (BLR). In particular, we prove that linear approximations of the Lie group algorithm give generalizations of the BLR. The key ingredient is the harmonic exponential family, a general class of Lie group exponential families associated to representations of Lie groups. Our work provides a systematic method to construct from such representations efficiently implementable algorithms for variational learning.

---


### 137. [E2I-Flow: EEG-to-Image Reconstruction via Wavelet-Temporal Cross-Attention and Conditional Flow Matching](https://arxiv.org/abs/2611.04524)

**<font color=#1a73e8>作者：</font>** Haowei Pan, Hwa Hui Tew, Junn Yong Loo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG)-based visual decoding and reconstruction aims to recover visual information from non-invasive brain signals. But there are challenges due to the complex temporal-frequency characteristics of EEG signals and the difficulty of discrete denoising framework in mapping neural activity to meaningful visual representations. Here, we propose E2I-Flow, an EEG-to-image decoding and reconstruction framework that combines a novel EEG encoder for time-frequency representation learning from EEG features, and conditional flow matching for visual decoding. A stationary-wavelet frequency branch and a temporal-mixing branch are integrated through bidirectional cross-attention and adaptive fusion, with the resulting EEG representations aligned to ground-truth image embeddings using contrastive and mean-squared-error loss supervisions. The aligned EEG representation is then used as a condition for a Transformer-based flow-matching model to predict the corresponding visual embedding for image synthesis. Experimental results show strong zero-shot EEG-to-image retrieval and improved visual reconstruction performance, outperforming several state-of-the-art baselines.

---


### 138. [Learning to Falsify: Hierarchical Multiple Instance Learning for High Resolution AI-Generated Image Detection](https://arxiv.org/abs/2611.04529)

**<font color=#1a73e8>作者：</font>** Haoran Chen, Daiqi Gao, Xinyuan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative models have made synthetic images increasingly photorealistic, posing growing challenges to reliable and generalizable detection of AI-generated images. Existing methods typically rely on holistic image-level classification, which may overlook local artifacts, especially in high-resolution images. To address this limitation, we formulate this task as a falsification-driven multiple instance learning problem, where a single fake patch can falsify the whole image, while a real image requires all patches to be authentic. Based on this formulation, we propose \textit{Learning to Falsify (LTF)}, a hierarchical multiple instance learning framework that models an image as multiple bags of instances across different spatial levels and aggregates their predictions under the falsification-inspired principle. We further introduce Cross-Shuffle during training to encourage the model to learn local artifact evidence rather than image-level shortcuts. Furthermore, we propose the \textit{Falsification-driven Test-time Aggregation Strategy (FATAS)}, a plug-and-play module that extends the same falsification-inspired principle to existing detectors by aggregating patch-level predictions. Extensive experiments demonstrate that LTF achieves strong generalization and robustness across multiple benchmarks, while FATAS substantially improves representative detectors in high-resolution scenarios without retraining. Code is available at this https URL

---


### 139. [The Price of List Replicability: Tight Bounds for Bias Estimation](https://arxiv.org/abs/2611.04532)

**<font color=#1a73e8>作者：</font>** Michael Chen, Atieh Bastan, A. Pavan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the sample complexity of list replicable algorithms for estimating the biases of $d$ coins. An algorithm is $(k,\varepsilon,\delta)$-list replicable if for every bias vector $\mathbf{p}\in[0,1]^d$, there is a set of outputs $L_{\mathbf{p}}\subseteq \mathbb{R}^d$ of at most $k$ elements such that every $\mathbf{y}\in L_{\mathbf{p}}$ satisfies $\lVert\mathbf{y}-\mathbf{p}\rVert_\infty\leq\varepsilon$, and the algorithm output is in $L_{\mathbf{p}}$ with probability at least $1-\delta$. Prior work gave a $(d+1,\varepsilon,\delta)$-list replicable algorithm with sample complexity $\widetilde{O}\left(\frac{d^3}{\varepsilon^2}\right)$, but no nontrivial sample complexity lower bound was known.
We establish the first non-trivial sample complexity lower bound for this problem and give an improved algorithm that matches it up to polylogarithmic factors. Together, these results determine the optimal sample complexity for list size $d+1$ to be $\widetilde{\Theta}\left(\frac{d^2}{\varepsilon^2}\right)$, showing that the quadratic dependence on dimension is inherent up to polylogarithmic factors. More generally, for every $k\in[d+1,2^d]$, we establish matching upper and lower bounds of $\widetilde{\Theta}\left(\frac{d^2}{\varepsilon^2\log k}\right)$ on the total sample complexity.

---


### 140. [A Universal Raw-IQ Radar Encoder for Cross-Sensor Human Sensing](https://arxiv.org/abs/2611.04534)

**<font color=#1a73e8>作者：</font>** Jonas Leo Mueller, Dario Zanca, Sebastian Hoefler 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radar-based human sensing typically relies on end-to-end task-specific models trained on hand-chosen signal projections, which generalize poorly across unseen users, tasks, and hardware. We argue that the dominant signal processing choice, the micro-Doppler spectrogram, is a poor starting point for transfer because it keeps the Doppler axis, which carrier frequency rescales, and discards the angular axis, which carrier frequency leaves unchanged. We instead pretrain a convolutional beta-VAE without labels on clutter-removed raw radar measurements from four platforms spanning 60 and 77 GHz and 4 to 12 virtual antennas, aligned by a unified spectral interpolation grid. For every downstream benchmark the encoder stays frozen, and only a small supervised temporal classifier is trained on its embeddings. We compare against supervised models trained end to end on each benchmark and a pretrained radar foundation model across ten settings covering activity, gesture, sign-language, and gait recognition. When the test users and the radar are seen during training, our encoder is best on all five benchmarks. For users never seen in training, it leads on three of four benchmarks, by 4.8 to 23.2 points. On subject-disjoint gait recognition, it is best for each of the four held-out subjects and 8.3 points above the strongest baseline on average, even though its pretraining excluded every recording of this radar. Excluding the test radar from pretraining costs at most 5.3 points on any benchmark. Code is available at this https URL.

---


### 141. [CANDO: Conservative Action-Noise Directional Optimization for Residual Reinforcement Learning](https://arxiv.org/abs/2611.04543)

**<font color=#1a73e8>作者：</font>** Zeyu Gao, Chengkai Hou, Chaoyue Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained generative policies provide strong behavior priors for robot control, but adapting them efficiently with online reinforcement learning remains difficult. A central challenge is how to improve a frozen generative policy without destroying the structure learned from offline demonstrations. Noise-space residual methods address this by modifying the policy's input noise, but existing noise-space methods typically regulate adaptation through fixed latent feasible regions, which may exclude valuable noise edits. In contrast, action-space residual methods are more sample-efficient, but their efficiency can still be further improved. We propose Conservative Noise Directional Optimization (CNDO), a noise-space residual RL method that improves a frozen generative policy by learning state- and noise-conditioned directions around Gaussian latent samples. CNDO removes predefined latent feasible regions and instead regulates noise-space adaptation through the soft conservative constraint, which consists of conservative value estimation and gated execution. We further introduce Conservative Action-Noise Directional Optimization (CANDO), which adds an action-space residual, combining structured latent-space improvement with local action correction. Experiments show that, once CNDO narrows the gap between noise-space and action-space residual learning, CANDO further improves over single-space optimization, achieving 76.1 NAUC and a 91.4% final success rate, surpassing the best single-space results by 6.6 NAUC and 4.1% success rate. More demos and info are available on this https URL.

---


### 142. [Predicting Void Points in Self-Occluding Forest Volumes](https://arxiv.org/abs/2611.04548)

**<font color=#1a73e8>作者：</font>** Benjamin Bachmayr, Mohamed Youssef, Oliver Bimber  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic Aperture Imaging (SAI) enables drones to observe forest canopies by warping and averaging multiple displaced views at a common depth. However, occlusion is suppressed rather than eliminated, causing poorly observed regions to appear occupied and leading to systematic biomass overestimation. The Deep Forest project cannot distinguish reconstruction artifacts from real vegetation because its training data relies on measured reflectance points, excluding empty space and preventing the network from learning explicit occupancy boundaries.
This thesis addresses the problem by modifying training labels rather than the imaging process. Each simulated scene is rendered twice: as a 9x9 grid of top-down captures for focal-stack generation and as 550 depth-clipped slabs derived from scene geometry to provide occupancy labels, explicitly representing void space as a negative class. A Gazebo pipeline generates procedural forest stands containing 80-200 trees across three species. A pretrained Pix2Pix model translates rendered RGB images into a synthetic near-infrared band, and Light Field Rendering produces aligned focal stacks of 550 planes across three channels.
Four architectures were evaluated on a held-out scene. The plain 2D U-Net achieved an IoU of 0.6290, outperforming the volumetric 3D U-Net (0.5707). Established reconstruction methods performed substantially worse: COLMAP achieved 0.3446 and DepthAnything3 0.2959, both after their respective optimal dilation sweeps. An RGB-input variant of the volumetric architecture achieved the highest IoU of 0.6514 without dilation or per-scene calibration. These results highlight the limitations of conventional reconstruction methods, which recover visible surfaces but struggle to infer occupancy within closed canopies.

---


### 143. [SEEK-VAU: Towards Evidence-Faithful Video Anomaly Understanding via Agentic Search](https://arxiv.org/abs/2611.04554)

**<font color=#1a73e8>作者：</font>** Minghe Wang, Weijun Zeng, Dapeng Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most video anomaly understanding (VAU) systems still infer anomaly judgments from evidence collected in a feed-forward way under predefined rules, typically sampled frames, or events clustered from such frames. This protocol fails when the collected evidence is incomplete under imperfect predefined rules, because once reasoning begins the model can no longer search for the missing evidence. We address this limitation with SEEK-VAU, which reframes VAU as an agentic search-and-verify interaction protocol under a bounded search budget: instead of passively reasoning over pre-collected evidence, the policy actively gathers evidence across the three stages of an anomaly event chain (precursor, trigger, and aftermath) and verifies its sufficiency before finalization, turning event-chain completeness into an explicit design rather than an outcome of predefined rules. A bounded budget caps the cost of this search, but does not by itself teach the policy where to look or when to stop. To make this behavior learnable, we introduce evidence-faithful counterfactual verification (EFCV), which rewards selected evidence that remains supportive, compact, and necessary under counterfactual verification. We further introduce SEEK-Bench, featuring video-level episodes with temporal interval annotations, semantic QA and event-chain stage labels. Together, SEEK-VAU and SEEK-Bench establish a strong foundation for evidence-faithful and actively verifiable VAU.

---


### 144. [Curriculum unlearning in humans and neural networks](https://arxiv.org/abs/2611.04565)

**<font color=#1a73e8>作者：</font>** Jirko Rubruck, Alice Zhang, Andrew Saxe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> During learning, humans often benefit from curricula that teach simple rules before exceptions. However, we lack a computational explanation for this phenomenon. Here, using a canonical behavioural task and modelling with neural networks, we develop and test a theory for why simple-to-complex curricula succeed. We show that during learning, both humans and neural networks show simplicity biases, a tendency to learn simple rules that are underfit to the data. In neural networks this bias is accompanied by compression of neural representations. Simple-to-complex curricula help both types of learners overcome this compression, developing representations (and policy) with appropriate dimensionality for the task. We test and confirm a further prediction from this theory: learners that have been pre-exposed to simple tasks and with more compressed initial representations benefit more from curricula. These findings suggest that curricula help with ``unlearning'' of simple rules.

---


### 145. [Setting the Stage: Enhancing Music Recommendations with Spoken Introductions to Stimulate Serendipity](https://arxiv.org/abs/2611.04570)

**<font color=#1a73e8>作者：</font>** Brett Binst  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People like to keep their music listening fresh and interesting, but recommender systems often struggle to support this need. Even when a recommended song is potentially refreshing and enriching, listeners may not perceive it as such. Building on Silvia's appraisal theory of interest, this paper studies whether enhancing recommendations with spoken introductions, immersive or informative, can stimulate two distinct flavors of experienced serendipity: taste-broadening (sparking interest in music outside one's typical preferences) and taste-deepening (deepening interest in music within one's typical preferences). Results from a large-scale user study show that both introduction types stimulate taste-broadening and taste-deepening serendipity. Taste-broadening is most effectively stimulated through transportation (absorption in a narrative world), whereas taste-deepening is most effectively stimulated through cognitive elaboration (learning something new about the artist or the social context in which the music emerged). We discuss how these findings could be translated into practice through curated taste-broadening playlists, where both introduction types appear promising, and taste-deepening playlists, where informative introductions seem particularly effective.

---


### 146. [Ground-Wing: A Parametric 3D Wing-in-Ground-Effect Dataset for Benchmarking Neural Surrogate Models](https://arxiv.org/abs/2611.04571)

**<font color=#1a73e8>作者：</font>** Andrea Cenzato, Lukas Karch, Andre Luckow 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a CFD dataset of a highly parametrized 3D wing operating in ground effect, designed for benchmarking neural surrogate models for aerodynamic prediction, using a wing shape and flow conditions typically encountered in motorsport applications. The dataset comprises 770 RANS simulations of 194 unique wing configurations, sampled across 27 airfoil profile variants and 4 distances from the ground, spanning variations in wing sweep, chord, taper, angle of attack, and tip twist. Six neural network architectures representing distinct paradigms --- convolutional (DoMINO), graph-based (X-MeshGraphNet), transformer-based (AB-UPT, GeoTransolver, GAOT), and JEPA-based (AeroJEPA) --- are evaluated on their ability to predict surface pressure coefficient and wall shear stress distributions, from which integral drag and lift coefficients are recovered. The dataset is intended to be used as a challenging benchmark for surrogate CFD models, due to the uniqueness of the ground effect being absent from other wing and airfoil datasets.

---


### 147. [Multi-Path Mamba Diffusion for 3D Point Cloud Semantic Scene Completion](https://arxiv.org/abs/2611.04583)

**<font color=#1a73e8>作者：</font>** Li Liang, Naveed Akhtar, Jordan Vice 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D semantic scene completion plays a critical role in enabling various downstream tasks within autonomous systems by estimating both missing geometric structures and semantic information in scene data. In this work, we introduce a unique neural framework that integrates state space modeling with diffusion-based generative approaches to enhance 3D point cloud semantic scene completion. We propose \textit{MPath Mamba} diffusion network, leveraging a skip-triple Mamba structure, dimensional decomposition residuals, and multi-directional dilations within multi-path data to efficiently process long-sequence data for feature extraction. The proposed method operates in the conditioned latent space of a variational autoencoder, enhanced by a state-space mechanism to improve 3D point cloud representation and reconstruction. Extensive experiments conducted on the SemanticKITTI benchmark demonstrate that our approach achieves highly competitive performance for 3D point cloud semantic scene completion.

---


### 148. [Can Network Models of Science Do Without Pluralist Agents?](https://arxiv.org/abs/2611.04590)

**<font color=#1a73e8>作者：</font>** Jonas Hallgren, David Hyland, Mahault Albarracin  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Science is a process of useful models being proven wrong time and again, but despite its many flaws, it somehow works. Why is this? Paul Feyerabend argued that it works because people dare to hold and defend incompatible rival theories against the accepted one, since a theory's failures often lead to its abandonment in the presence of a more accurate or simpler alternative. He called this view theoretical pluralism. We introduce a theoretical and experimental model in which this can be examined. It compares communities of pluralist agents, which can hold rival theories side by side and maintain beliefs within and between those theories, with communities of monist agents, which can only incorporate what they hear or observe into a single model of their own. In a multi-agent variational inference setting, our experimental demonstrations illustrate how communities with rival theories can go through periods of uncertainty followed by a shift in the theories they hold true, how the information that is communicated between communities affects beliefs when those communities make different observations about the world, and how sharing support for theories and sharing beliefs within them contribute differently to collective belief dynamics.

---


### 149. [SparseGraph-I2P: Consistency-Guided Hypothesis Selection for Efficient Image-to-Point-Cloud Registration](https://arxiv.org/abs/2611.04591)

**<font color=#1a73e8>作者：</font>** Ziyang Yu, Xiang Li, Qiong Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coarse-to-fine image-to-point-cloud (I2P) registration risks discarding correct but ambiguous patch pairs, while retaining more candidates repeats fine matching over overlapping patches. SparseGraph-I2P aims to improve registration recall by increasing the inlier ratio at the pose solver, using sensor or monocular depth. A Coarse Hypothesis Graph combines appearance with depth-derived first- and second-order compatibility to select a fixed budget of patch pairs. Sparse Fine Matching decodes each queried pixel once and skips pixel--point comparisons covered by an ancestor patch paired with the same point-cloud region. With sensor depth, depth-aware filtering ranks correspondences by SC2 spectral support for a single EPnP solve. With monocular depth, depth or inverse depth is calibrated from correspondence geometry before filtering. SparseGraph-I2P achieves the highest registration recall and lowest latency among the compared methods on RGB-D Scenes V2 and 7-Scenes with sensor depth. With predicted depth, it retains the highest recall on RGB-D Scenes V2 at an additional calibration cost. Code will be released.

---


### 150. [SCANO: Restoring Boundary-Condition Completeness in Sampled Meshes with a Sliced-Cross-Attention Neural Operator for 3D Thermal Fields](https://arxiv.org/abs/2611.04603)

**<font color=#1a73e8>作者：</font>** Tianyu Li, Zhiwei Cao, Qingang Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training neural operators on million-cell meshes can exceed GPU memory limits. Models are therefore trained on subsamples and deployed on whole meshes or selected regions. However, subsampling can distort boundary information, degrading accuracy. We ask when boundary conditioning under sampling stays consistent with whole-mesh training, and how to aggregate and inject boundary data. Representing the solution as an integral of boundary data against type-dependent measures, we show that subsampling distorts this conditioning in three ways: incomplete boundary coverage or a sample-dependent global state, face weighting by count rather than area, and compression of boundary inputs into a low-dimensional vector. This analysis yields four measurable consistency conditions checkable before training. We satisfy them with two backbone-agnostic modules. Boundary Quadrature Attention (BQA) aggregates all boundary faces, typed and area-weighted, into slice tokens that every query point reads at every layer. Anchored Global State (AGS) estimates the global state from anchors independent of the sampled points. Adding both to a scalable message-passing and slice-attention backbone yields SCANO. We evaluate the approach on controlled and public benchmarks and a data-centre thermal simulation dataset (DCTS) containing million-cell meshes. On both benchmarks, BQA improves every backbone, reducing whole-mesh error up to 15-fold. On all three datasets, AGS aligns regional with whole-mesh predictions, cutting regional error at least tenfold for most backbones on the public benchmark. Together, the modules nearly halve the best original backbone's whole-mesh error on both benchmarks. SCANO predicts a room-scale field in under one second, over 100 times faster than whole-room anchor self-attention.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-280](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
