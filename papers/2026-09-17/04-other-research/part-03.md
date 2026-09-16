# 📦 其他研究 | 2026年09月17日

> 本类共 **219** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-219](./part-05.md)

---

### 101. [Beyond Episodic AI: Cognitive Field Networks for Biologically Inspired Persistent Cognition](https://arxiv.org/abs/2609.16752)

**<font color=#1a73e8>作者：</font>** Byung Gyu Chae  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cognitive Field Theory (CFT) proposes that cognition arises from memory-dressed collective dynamics that generate a persistent macroscopic cognitive field. Here we develop a Cognitive Field Network (CFN), a recurrent Transformer in which the organized hidden field re-enters subsequent inference through \[ \Phi_{n+1}=F_{\theta}(X_{n+1},\Phi_n). \] Rather than prescribing an explicit memory operation, the CFN allows new information to act on an already history-dependent collective state. We find that learning organizes persistent, content-dependent recurrent dynamics whose timescale increases systematically with the trained recurrent horizon. Semantic continuation propagates the recurrent state far beyond this horizon without replay of the target answer. Without content-specific support, the field exhibits finite passive relaxation, whereas periodic re-exposure to relevant input repeatedly renews the surviving state and drives it toward an approximately stationary nonzero regime. Unrelated-input and recurrence-off controls do not reproduce this behavior, while near-paraphrased re-exposure produces weaker renewal, demonstrating representation-sensitive persistence. These results distinguish three dynamical processes: collective memory dressing forms and sustains a history-dependent cognitive field, structured input reorganizes this field, and cross-cycle re-entry makes the resulting state causally available to subsequent inference. The CFN therefore provides a controlled computational platform for studying persistent, history-dependent cognitive dynamics without a separately prescribed memory system.

---


### 102. [De-GAN - Dynamic Parameter Tuned GAN for 3D Medical Image Segmentation: A Step Towards Generalisation](https://arxiv.org/abs/2609.16755)

**<font color=#1a73e8>作者：</font>** Zoha Usama, Azadeh Alavi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain tumor segmentation remains difficult because enhancing tumor (ET) has low contrast and overlaps surrounding tissue, while scanner and site variation causes domain shift. We propose DE-GAN, a contrast-enhancing conditional GAN that combines input-adaptive dynamic convolutions, style-aware feature mixing, and coordinate encoding to synthesize slice-adaptive FLAIR images. A label-guided, class-conditional target separates tumor-core (TC) and ET intensities while preserving anatomy. The generated FLAIR is concatenated with the original MR modalities and used to train a 3D U-Net. Across BraTS 2015, 2018, and 2019, DE-GAN improves segmentation over the baseline and static EnhGAN replacement on most reported TC/ET metrics, with the largest gains from retaining both original and enhanced FLAIR. Code and pretrained models are available at this https URL.

---


### 103. [EgoAsk: Egocentric Teaching of Personalized Object Knowledge for Household Robots](https://arxiv.org/abs/2609.16766)

**<font color=#1a73e8>作者：</font>** Yuanda Hu, Wenbin Zuo, Yiting Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Unlike users, who know their own belongings and routines, household robots cannot easily acquire such personalized object knowledge automatically and depend on users to teach them. User-initiated teaching requires users to arrange dedicated teaching sessions and decide what to teach, even when they are unsure what the robot needs to learn. We introduce EgoAsk, a smart-glasses-based system that proactively embeds personalized object teaching into everyday activities. EgoAsk shares the user's first-person view with the robot, identifies gaps in personalized object knowledge, and analyzes ongoing activity to ask context-relevant questions that support future household assistance. To examine how teaching initiative and question timing affect users' teaching experiences, we conducted a within-subjects study with 18 participants and found lower reported knowledge-gap monitoring burden with robot-initiated questioning and less need for context reconstruction with EgoAsk. These findings characterize teaching burdens and timing preferences, offering design implications for egocentric robot-teaching systems.

---


### 104. [Coverage-Aware Virtual IMU Augmentation for Low-Resource Human Activity Recognition](https://arxiv.org/abs/2609.16768)

**<font color=#1a73e8>作者：</font>** Jiayuan Gao, Yingwei Zhang, Ziyao Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> IMU-based human activity recognition (HAR) enables continuous, privacy-friendly monitoring of daily activities using wearable sensors. However, building reliable HAR models that generalize across diverse users and real-world conditions requires large amounts of labeled IMU data, which are expensive and difficult to collect. Existing approaches mainly rely on augmentation or synthesis to expand available data, but indiscriminately adding virtual samples may provide little new coverage and introduce unreliable supervision. To overcome these challenges, we propose a novel coverage-aware virtual IMU augmentation framework that decides where to supplement real data, how to generate and select virtual candidates, and how strongly to weight them during training. Specifically, we select diversity and scarcity anchors in a learned sensor embedding space, convert anchor dynamics into prompts, and generate virtual IMU candidates for each anchor. We then rank candidates by a selection cost combining anchor proximity and label consistency, and incorporate the selected candidates into HAR training with reliability-based weights. Experiments on public HAR benchmarks show that our method consistently improves recognition performance over competitive baselines, and ablation studies confirm the effectiveness of the proposed framework design.

---


### 105. [HLC-GS: Risk-Map-Guided Height-Layer Consistency Gaussian Splatting for DSM Reconstruction from Optical Satellite Imagery](https://arxiv.org/abs/2609.16772)

**<font color=#1a73e8>作者：</font>** Jie Yang, Yingdong Pi, Qiyan Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A Digital Surface Model (DSM) is a fundamental geospatial data product for representing the elevation of the Earth's surface. Recently, 3D Gaussian Splatting (3DGS) has shown considerable potential for DSM reconstruction from multi-view optical satellite imagery due to its explicit scene representation and efficient optimization. However, in 3DGS-based DSM generation, alpha-weighted aggregation of Gaussian altitudes may blend splats from different height layers at the same rendered pixel or DSM sampling location, producing non-physical intermediate elevations and height-layer mixing errors. To address this problem, we propose HLC-GS, a risk-map-guided height-layer consistency Gaussian Splatting method for DSM reconstruction from optical satellite imagery. HLC-GS consists of a risk map module, a dominant-layer reliability correction module, and a secondary-layer suppression module. The risk map localizes high-risk pixels with abnormal height dispersion and unreliable dominant-layer responses, while the latter two modules regularize unreliable dominant-layer responses and suppress weakly supported far secondary-layer responses. Extensive experiments are conducted on the DFC2019 and IARPA2016 datasets. Compared with six state-of-the-art DSM reconstruction methods, HLC-GS achieves better overall accuracy. Compared with the latest and precision-enhanced EOGS, HLC-GS reduces the average MAE from 1.46 m to 1.18 m and the average RMSE from 2.78 m to 2.58 m over the evaluated scenes, while improving PAG$_{2.5}$ from 86.09\% to 88.61\%. Overall, these results demonstrate that explicitly modeling per-pixel height-layer consistency alleviates height-layer mixing and improves the geometric quality of 3DGS-based DSM reconstruction from optical satellite imagery.

---


### 106. [FSANet: Frequency-Spatial Aware Network for Image Segmentation](https://arxiv.org/abs/2609.16773)

**<font color=#1a73e8>作者：</font>** Ruibo Wang, Ziyi Shen, Huaming Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image segmentation remains challenging due to occlusions, poor lighting, and irregular structures. Although transformer-based methods achieve high accuracy, they rely heavily on long-range spatial features, leading to high computational costs and neglecting prior knowledge or noise patterns, resulting in missing details and unclear boundaries. To address these issues, we propose Frequency Spatial Aware Network (FSANet), which integrates prior knowledge with a dual-domain solver to sequentially adapt to diverse segmentation tasks. Specifically, we design three key modules: (1) Structure Prior Module, which recovers overlooked details; (2) Dual-Domain Awareness Module, which captures salient features while disentangling noise; and (3) Edge Estimation Module, which enhances edge awareness for more precise segmentation. In addition, the limited availability of comprehensive segmentation datasets covering various real-world scenarios hinders the performance of existing methods. To address this, we introduce SceneX, a novel open-source dataset featuring 10 challenging non-ideal scenarios, establishing a new benchmark for evaluating and improving the robustness and real-world applicability of the segmentation models. Extensive experiments demonstrate the efficiency and effectiveness of FSANet.

---


### 107. [IMVS: Interactive Medical Volume Segmentation with Test-Time Adaptation - A New Method for Annotating Radiology Datasets](https://arxiv.org/abs/2609.16775)

**<font color=#1a73e8>作者：</font>** Abhilaksh Singh Reen, Kushal Borkar, Ritvik Mahapatra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Annotating large radiology datasets is bottlenecked by the manual effort of delineating structures slice-by-slice in 3D volumes. Interactive methods reduce this effort but stay interaction-inefficient: slice-wise methods (including many foundation models) ignore inter-slice continuity, while 3D and video-based methods propagate a prompt with a \emph{fixed} propagator that never adapts to the target volume, so it drifts on low-contrast or pathological structures and must be re-prompted. We present IMVS, a human-in-the-loop annotation framework that composes three components into a closed loop rather than a new segmentation primitive: a lightweight 2D Slice Mask Adapter (SMA) fine-tuned online from user scribbles, a frozen Volume Mask Tracker (VMT) that propagates corrected masks across adjacent slices, and a soft teacher--student alignment that limits forgetting. The SMA is backbone-agnostic (UNet++, DeepLabV3, TransUNet). Across 8 public CT/MRI datasets, IMVS matches strong interactive baselines in quality while sharply cutting annotation effort: $14.4\times$ faster than a proficient copy-based manual workflow ($22.3\times$ over naive manual), $4.6\times$ over slice-wise and $1.9\times$ over 3D interactive methods. MedSAM2 and ScribblePrompt stay competitive or stronger on well-delineated organs; IMVS's advantage is largest on challenging targets and on interaction efficiency. Source code and Demo Video: this https URL.

---


### 108. [PSMP-CLIP: Patch-Prompt SAM and Multi-Semantic Prompting for CLIP-Based Zero-Shot Anomaly Detection](https://arxiv.org/abs/2609.16785)

**<font color=#1a73e8>作者：</font>** Xuezhi Xiang, Guanghao Wu, Heqi Xiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot anomaly detection aims to localize anomalies without target-domain samples. Existing CLIP-based methods suffer from coarse anomaly maps and limited semantic prompts. We propose PSMP-CLIP, integrating patch-prompt SAM2 segmentation (PPSS) and multi-semantic guided prompt regularization (MSGPR). PPSS samples prompts directly from intermediate patch features, avoiding threshold drift and guiding SAM2 to produce precise masks. MSGPR uses multiple learnable prompts constrained by semantic anchors to preserve generalization. Experiments on 14 datasets show highly competitive performance, achieving the best pixel-level AUROC on MVTec AD, BTAD, DTD-Synthetic, CVC-ClinicDB, TN3K, Endo, and Kvasir.

---


### 109. [Noise2Noise Revisited: Training Pair Distributions Dominate Loss Choice in Self-Supervised Denoising](https://arxiv.org/abs/2609.16788)

**<font color=#1a73e8>作者：</font>** Dingyan Shang, Zhenyu Xu, Youting Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Noise2Noise (N2N) trains denoisers on pairs of independently corrupted observations, eliminating clean references. We stress-test two natural conjectures about why the L1 loss outperforms L2 here. First, the hypothesis that the L1 loss confers robustness via parameter sparsity confuses the loss with Lasso regularization: an explicit Lasso penalty produces the predicted sparsity yet fails to reproduce L1's cross-noise behavior, while L1- and L2-trained weight distributions are indistinguishable. Second, the population optima of the two losses coincide exactly for symmetric signal posteriors and nearly so for concentrated ones. Measured differences are therefore dominated by optimization dynamics (bounded-influence gradients), which we probe with gradient statistics and contaminated-target training. On Kodak24 with five synthetic noise families, the L1 loss holds a statistically significant edge over L2, below 1 dB PSNR, holding across three seeds on 13 of the 14 noise columns. On real camera noise the loss is not the decisive variable in distribution: on official SIDD validation blocks, synthetic-Gaussian-trained N2N models gain only 0.8 to 3.7 dB over the noisy input regardless of loss, while retraining on SIDD's own noisy pairs, never reading ground truth, gains 9.4 to 11.0 dB, far ahead of BM3D. All metrics are on raw network outputs, and the study makes no leaderboard claim. The training pair distribution, not the loss, carries the inductive bias. That design rule applies wherever clean references are unobtainable, from microscopy to industrial inspection sensors.

---


### 110. [TEDi: Temporal Memory-Enhanced and Denoising Transformer for Surgical Instrument Segmentation](https://arxiv.org/abs/2609.16797)

**<font color=#1a73e8>作者：</font>** Jiahong Yuan, Weiming Mi, Tao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Query-based segmentation methods have shown promising potential for surgical instrument segmentation and recognition, which is essential for scene understanding and downstream tasks in computer assisted surgery. However, most existing approaches predominantly rely on per-frame predictions and overlook cross-frame temporal priors as well as temporal-consistency constraints. This limitation often leads to unstable query representations and suboptimal category recognition. In this paper, we propose TEDi, a Temporal memory-Enhanced and Denoising transformer for surgical instrument segmentation that addresses these is sues through Memory Search Enhancement and Temporal Consistency Denoising. The former introduces a query-level memory bank and a memory search enhancement encoder to retrieve discriminative representations from historical frames, enriching current-frame features. The latter constructs a temporally consistent reference as a cross-frame semantic anchor to suppress temporally unstable predictions and promote semantic coherence across frames. Extensive experiments on two benchmark datasets, EndoVis 2017 and EndoVis 2018, demonstrate that TEDi consistently outperforms state-of-the-art methods, highlighting its potential to further advance computer-assisted surgery. Our code is available at this http URL.

---


### 111. [Geometry of learning dynamics: Gradient descent versus natural gradient on the ridge of optimization](https://arxiv.org/abs/2609.16805)

**<font color=#1a73e8>作者：</font>** Akira Tamamori  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-capacity associative memories based on Kernel Logistic Regression (KLR) exhibit a "Ridge of Optimization" characterized by extreme stability and a highly skewed weight spectrum. However, the dynamical process by which learning converges to this critical regime has remained unclear. This paper provides a geometric analysis of the learning trajectories on the statistical manifold of a KLR-trained Hopfield network. By comparing the paths of Gradient Descent (GD) and Natural Gradient Descent (NGD), we elucidate the mechanisms governing the optimization process. Our analysis reveals that learning on the Ridge proceeds in two distinct phases. We show that the extreme curvature of the Ridge causes standard GD to follow a highly oscillatory, non-geodesic path. In stark contrast, NGD explicitly corrects for this geometry, following the ideal geodesic path and completely overcoming the instabilities faced by GD. We demonstrate experimentally that NGD not only converges significantly faster but also achieves a solution with superior generalization performance. These results establish that the highly structured geometry of the Ridge is optimally suited for information-geometric optimization, providing a new perspective on the interplay between learning dynamics and emergent representation geometry.

---


### 112. [Hyper-RED: Scalable Event Pre-training via Semantic Hypergraph Distillation](https://arxiv.org/abs/2609.16811)

**<font color=#1a73e8>作者：</font>** Meisen Wang, Zhiqiang Tian, Wei Bao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras have shown great potential for robust visual perception, yet scaling event representation learning remains challenging due to the scarcity of large-scale annotated event data. Pretrained image models provide scalable semantic supervision, but existing image-to-event methods rely on rigid pixel-wise or token-wise alignment that overlooks modality discrepancies in texture, density, and appearance, potentially causing semantic collapse and limiting transferability. To address this issue, we propose Hyper-RED, a simple, painless, and scalable image-to-event pretraining framework that transfers high-order semantic structures from images to events. Hyper-RED uses hypergraphs to model and align high-order semantic associations among multiple image and event tokens, enabling cross-modal knowledge transfer while accommodating modality-specific differences rather than enforcing rigid one-to-one correspondence. Specifically, given a paired event--image sample, Hyper-RED leverages DINOv3 to extract spatial token representations and constructs image, event, and cross-modal semantic hypergraphs, where each hyperedge connects multiple semantically correlated tokens. We further introduce a hypergraph relational distillation loss that imposes complementary intra- and cross-modal constraints, enabling the event encoder to inherit image-derived semantic organization while preserving local relational consistency and event-specific characteristics. Experiments on three tasks across five event datasets demonstrate consistent scaling from ViT-S to ViT-L and state-of-the-art performance (Fig.1). The code is available at: this https URL.

---


### 113. [Execution Flexibility in Automated Planning: A Comparative Evaluation of Deordering and Reordering Strategies](https://arxiv.org/abs/2609.16822)

**<font color=#1a73e8>作者：</font>** Md. Monjurul Islam, Sabah Binte Noor, Fazlul Hasan Siddiqui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study covers foundational concepts for enhancing plan-execution flexibility, including partial-order planning, the producer-consumer-threat formalism, and a range of deordering and reordering strategies. Creating a partial-order plan from a sequential one by removing unnecessary ordering constraints is a practical way to improve execution flexibility, and several methods have been proposed for this task. This study analyzes their capabilities across ordering, action handling, parameter handling, plan structure, concurrency, and complexity, and evaluates them against each other on a shared benchmark. The central finding is that block deordering-based approaches, which restructure causal dependencies through block-level grouping and subplan substitution, substantially outperform MaxSAT-based approaches despite the latter's theoretical guarantees of minimum reordering. The reason is structural: minimum reordering optimizes within the causal structure already present in the plan, whereas block deordering-based methods change that structure, exposing orderings that would otherwise appear necessary. A further distinction is practical: block deordering-based methods are anytime algorithms that always return a valid result, while MaxSAT-based methods fail entirely on a substantial portion of plans and offer no partial solution when they do. Block substitution further extends the parallel execution by formalizing non-concurrency constraints, though its impact is limited to domains with resource-based interactions. On efficiency, block deordering-based approaches achieve the highest flex gain per unit of computation time, while MaxSAT-based encodings incur large computational overhead.

---


### 114. [LCAP: Population-Informed Latent Chip Adaptation from Few Output Probes for Photonic Neural Networks](https://arxiv.org/abs/2609.16823)

**<font color=#1a73e8>作者：</font>** Tianyu Gao, Guantian Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Photonic neural networks (PNNs) offer efficient analog inference, but parameters optimized under ideal device models can degrade after fabrication, creating a persistent simulation-to-hardware (sim-to-real) gap. When many identically designed chips are deployed, calibrating each device from scratch compounds this cost. We propose Latent Chip Adaptation from Probes (LCAP), a population-informed framework that decomposes hardware adaptation into a transferable population correction and probe-inferred latent personalization. LCAP first learns a shared correction from 80 historical chips, then extracts a low-dimensional correction space from device-specific refinements. At deployment, 32 fixed unlabeled output probes infer an unseen chip's latent correction coordinates, enabling feed-forward personalization without target-device optimization. On a three-layer 64-mode MZI simulator with phase variation, beam-splitter errors, quantization, and crosstalk, accuracy improves from 80.4147% under direct deployment to 92.6860% after shared calibration and 93.3617% with LCAP. LCAP improves 27/30 unseen chips and raises worst-device accuracy from 89.18% to 90.54%.

---


### 115. [Adapting to Decision-Relevant Non-Stationarity in Decentralized Heterogeneous Bandits](https://arxiv.org/abs/2609.16824)

**<font color=#1a73e8>作者：</font>** Zhaojun Peng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized bandit systems often contain heterogeneous agents: rewards can change at individual agents even when the best action for the network stays the same. These local changes may cancel when rewards are averaged across agents, so the number of local changes $\Stloc$ can be much larger than the number of changes in the best common arm $\Stdec$. We introduce Decision-Relevant Fresh Comparison (DRFC), which uses new, balanced samples from all agents to compare arms at the network level and switches only when fresh global evidence indicates that the common best arm has changed. We prove a high-probability dynamic regret bound with no adaptation term depending on $\Stloc$, and show that every algorithm must still pay for identifying genuine decision switches and propagating them through the communication graph. Under a distinct time-average benchmark, an anytime-valid sliding-window extension handles gradual drift; experiments on synthetic, semi-real, and MovieLens-1M replays show that DRFC ignores decision-irrelevant local changes while the extension avoids false switches.

---


### 116. [Information Geometric Self-Organization at the Edge of Stability in High-Capacity Kernel Associative Memories](https://arxiv.org/abs/2609.16827)

**<font color=#1a73e8>作者：</font>** Akira Tamamori  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-capacity associative memories based on Kernel Logistic Regression (KLR) exhibit exceptional storage capabilities and robustness. Previous empirical studies identified a hyperparameter regime, the "Ridge of Optimization," where attractor stability is maximized. However, the geometric nature of this regime and the optimization dynamics required to reach it have remained unclear. In this paper, we investigate the static geometry of the parameter space and the learning trajectory of Gradient Descent (GD) in KLR-trained Hopfield networks. Using the eigenvalue spectrum of the Hessian, we reveal that the Ridge corresponds to a phase boundary located adjacent to a rank-1 spectral collapse, acting as a geometric singularity where the principal curvature is massively amplified. Furthermore, we demonstrate that the learning dynamics exhibit a transient self-stabilizing behavior driven by the Edge of Stability (EoS) phenomenon. Rather than seeking flat regions, the network parameters are driven toward a state where the local curvature dynamically equilibrates near the stability limit dictated by the learning rate, allowing the optimization to survive the initial instability. We provide analytical derivations for both the rank-1 asymptotic collapse and the dynamic feedback loop governing this equilibration. These findings suggest that optimal, high-capacity memory representations are not formed in flat minima, but are dynamically sculpted at the highly curved boundaries of geometric singularities.

---


### 117. [What Breaks Local Watermarks? A Robustness Benchmark for Local Invisible Image Watermarking](https://arxiv.org/abs/2609.16832)

**<font color=#1a73e8>作者：</font>** Kai Yao, Bence Szilágyi, Sebestyén Kamp 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Local image watermarking embeds an invisible signal into selected image regions rather than spreading it across the entire image, enabling payload recovery from specific objects or regions without perceptibly altering the image. Existing studies evaluate the robustness of payload recovery and localization under image transformations, but they often focus on their own proposed method, resulting in narrow evaluations with inconsistent choices of transformations, datasets, and metrics. These inconsistencies across studies limit direct comparisons across methods and muddle the overall picture of local watermark robustness. To address this gap, we present the first systematic robustness benchmark for local watermarks across 55 image transformations, including (i) signal distortions, (ii) changes in image coordinate alignment, (iii) indirect local edits, and (iv) direct watermark edits. The benchmark evaluates MaskWM, WAM, OmniGuard, TrustMark, and PixelSeal, all methods that either provide native localization or require minimal adaptation to support it. Our results show that all evaluated methods are vulnerable to some transformation, with MaskWM standing out as offering the strongest payload recovery and localization, although it has the lowest image quality in the clean setting. Synchronization further improves MaskWM's payload recovery under several geometric transformations, albeit at an additional cost to image quality. A key finding is that local watermark robustness depends strongly on the nature of the transformation: signal distortions are often tolerated by the strongest methods, while geometric misalignment and generative local edits, such as inpainting and outpainting, can completely impair payload recovery. We observe that payload recovery and localization are related but not interchangeable, and both strongly depend on the transformation's impact on the watermark region.

---


### 118. [FAHCD-Net: Frequency-Adaptive Heatmap-Conditional Diffusion Networks for Robust Facial Landmark Detection](https://arxiv.org/abs/2609.16842)

**<font color=#1a73e8>作者：</font>** Jun Wan, Jiwei Hu, Shengkai Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial Landmark Detection(FLD) is a crucial task in various applications and has achieved significant advancements in recent years. However, current FLD methods still struggle under challenging conditions, where facial structural variations, information loss, and noise interference severely compromise the integrity and accuracy of learned facial features. To address these issues, we propose Frequency-Adaptive Heatmap-Conditional Diffusion Network (FAHCD-Net), which integrates a Frequency-Adaptive Heatmap-Conditional Diffusion (FAHCD) model with a Smoothness Regularization (SR) loss in a cascaded framework. Specifically, the FAHCD model incorporates a Hierarchical Frequency Adaptation (HFA) module designed to suppress redundant high-frequency noise through multi-layer frequency decomposition and adaptive reconstruction, thereby preserving essential facial structures. Additionally, the SR loss is proposed to further mitigate the interference of high-frequency noise and enhance the smoothness of the generated landmark heatmaps. By cascading the FAHCD model with the SR loss, FAHCD-Net effectively leverages both statistical and frequency-based distribution characteristics of the data to progressively generate more accurate landmark heatmaps from noisy inputs. Extensive experiments on popular benchmarks demonstrate the effectiveness and robustness of the proposed method, achieving state-of-the-art performance in FLD tasks under challenging scenarios. The source code is available at this https URL.

---


### 119. [Can Deep Learning Achieve Cross-Physics Mapping?](https://arxiv.org/abs/2609.16853)

**<font color=#1a73e8>作者：</font>** Pengfei Zhu, Julien Lecompagnon, Mathias Ziegler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can deep learning translate physical fields governed by fundamentally different equations? We address this question by introducing Cross-Physics Mapping (CPM), an operator-learning framework for mappings between heterogeneous physical domains. We formulate sufficient conditions for such mappings through compatible latent representations and propose a dimensionless scaling principle that aligns the characteristic evolution scales of the source and target systems without assuming their dynamical equivalence. As a representative test, paired diffusion and wave fields are generated independently from their respective parabolic and hyperbolic equations while sharing the same latent geometry, material heterogeneity, excitation, and dimensionless scale. Seven architectures-ResUNet, DeepONet, Fourier, latent, wavelet, U-shaped, and Galerkin neural operators-are evaluated for both diffusion-to-wave and wave-to-diffusion mappings. The results reveal a strong directional asymmetry. Diffusion-to-wave reconstruction is more challenging because it requires recovering wavefront, phase, and time-of-flight information attenuated by diffusion; U-NO performs best in this direction, achieving a relative $\ell_2$ error of $0.307$ and an $R^2$ of $0.905$. Wave-to-diffusion mapping is considerably more stable, with GNO attaining a relative $\ell_2$ error of $0.154$ and an $R^2$ of $0.935$. Neural operators generally outperform the conventional convolutional baseline, highlighting the nonlocal nature of cross-physics transformations. These findings demonstrate that deep learning can establish useful mappings between distinct physical modalities on a shared latent manifold, while the achievable accuracy remains fundamentally constrained by the direction-dependent information content of the governing physics.

---


### 120. [Measuring Annotation Efficiency for Handwritten Devanagari Recognition: Sample-Complexity Curves for Four Pretraining Regimes](https://arxiv.org/abs/2609.16859)

**<font color=#1a73e8>作者：</font>** Manglesh Kumar Pandey, Sumit Kumar Banshal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To train handwritten text recognition systems we need word images and their corresponding transcriptions, and these transcriptions are produced manually. For a script that can be read by only a small number of specialists, this manual transcription is a limitation, because the trained models are supposed to save the time of those same specialists. A relevant question therefore arises: how many transcriptions are needed before a recogniser becomes useful, and how much of that cost can pretraining remove? In this study the answer is measured directly for handwritten Devanagari. We keep the recogniser, optimiser and evaluation protocol the same and change only the number of real transcribed words used for fine-tuning across nine budgets from 10 to 4,000 and four initialisation regimes, with six seeds at every point. The resulting curves are then converted into annotation-equivalent terms. A CER of 0.50 is reached by supervised synthetic pretraining using only 81 transcribed words, whereas random initialisation requires 355, which gives a label multiplier of 4.40 [3.56, 4.99]. There is a zero-shot reference point as well: with no real transcribed words at all, this pretraining is worth about 136 of them. This advantage gets smaller as the target accuracy improves, and at the most demanding target we measure, it cannot be distinguished from no saving at all. A fourth arm in which only the encoder is transferred separates the effect of the pretraining method from that of transfer scope, and masked image modelling is observed to transfer negatively over a bounded range of budgets. We emphasise that the scarcity in this study is constructed by subsampling a large corpus.

---


### 121. [Reduplicative constructions in Mandarin: Socio-emotional profiling through distributional semantics](https://arxiv.org/abs/2609.16860)

**<font color=#1a73e8>作者：</font>** Chaoyi Wu, Yu-Hsiang Tseng, R. Harald Baayen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mandarin Chinese has two productive reduplicative constructions that repeat either two-character base words or their constituents (e.g., `in good health', `discuss a bit'). Their varied meanings have been described as realizing plurality, valence coloring, sound symbolism and pragmatic functions. The aim of this study is twofold. A first goal is to clarify whether it is possible to come to a more precise understanding of the variegated semantics of Mandarin reduplication by using word embeddings from distributional semantics. A second goal is to explore how useful embeddings are for understanding the details of a semantically complex word-formation process. We show that the embedding space recovers the semantic and grammatical properties of reduplications previously identified in the literature, validating Tencent embeddings for morphological investigation. Semantic profiling revealed that reduplicative constructions are often strongly represented on multiple dimensions. The two patterns exhibit clear semantic and pragmatic differentiation in distributional space. Procrustes analysis clarified that the overall organization of the base-word space is largely preserved in the reduplication space, with local mismatches highlighting regions of discourse-pragmatic reorganization. Taken together, these results show that high-dimensional word embeddings can recover established linguistic generalizations, and capture the semantic versatility of Mandarin reduplication and constructional transparency.

---


### 122. [tcnerv:dual-domain temporal context modeling for implicit neural video compression](https://arxiv.org/abs/2609.16870)

**<font color=#1a73e8>作者：</font>** Xuezhi Xiang, Yixin Zhao, Heqi Xiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video compression aims to minimize reconstruction distor tion under a constrained bit rate. Existing video implicit neural representations (INRs) often decode frames independently, leaving intermediate features unconditioned on previous reconstructions and content embeddings without explicit temporal prediction. We propose TCNeRV, which exploits reconstructed context in both feature and embedding domains. Its multi-scale temporal-context fusion (MTCF) module injects gated historical features at multiple decoder scales, while temporal embedding-residual coding (TERC) predicts each content embedding and codes only its residual. With approximately 3M parameters, TCNeRV achieves an average PSNR of 36.08 dB on the UVG dataset, outperforming HNeRV-Boost by 2.20 dB. It reduces BD-rate by 22.06%, 66.73%, and 29.85% relative to HM, DCVC, and HiNeRV, respectively, demonstrating competitive rate-distortion performance with limited model capacity.

---


### 123. [SPEAR NeXT Causal Latent Forecasting Across Multiple Horizons for Spectral Temporal Earth Representation Learning](https://arxiv.org/abs/2609.16871)

**<font color=#1a73e8>作者：</font>** Rajiv Ranjan, Udaiveer Singh, Shashank Tamaskar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth observation is inherently dynamic, yet temporal information in many foundation models is learned through reconstruction, invariance, or retrospective sequence summarization. SPEAR NeXT is introduced as a compact pixel-wise multimodal spectral temporal foundation model in which temporal self supervision is formulated as past only, multi horizon latent Earth state prediction. Instantaneous states are first encoded by the pretrained SPEAR model from optical, radar, and environmental observations into compact 32 dimensional embeddings. Their temporal evolution is then modeled by a causally masked Trans former that predicts multiple future latent states from pre ceding observations. Relative temporal order is represented using Rotary Position Embeddings, while month and year embeddings encode seasonal phase and interannual con text.

---


### 124. [GRACE: Geometry- and Ray-Aware Camera-Efficient Multi-View Pedestrian Tracking](https://arxiv.org/abs/2609.16872)

**<font color=#1a73e8>作者：</font>** Taigo Sakai, Kazuhiro Hotta, Hiroki Kouno 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reducing the number of cameras reduces the deployment cost but removes views that correct BEV responses stretched away from true pedestrian positions by projection and short score drops that can split tracks} in Bird's-Eye View (BEV) tracking. We introduce GRACE, a camera-efficient multi-view tracker with three components. Volumetric-Guided Fusion combines homography-based BEV features with features lifted through 3D space. Ray Conditioning exposes each camera's viewing direction to the fusion network. Its tracking component, BEV Track Recovery (BTR), uses low-confidence detections only to continue existing tracks. The same detections cannot start new tracks. With two WildTrack cameras, GRACE improves MOTA from 83.54 for TrackTacular, our baseline, to 91.07.

---


### 125. [NeuroTS-Net: Multi-Class Semantic Segmentation of Pediatric Brain Tumors in Multi-Modal MRI](https://arxiv.org/abs/2609.16873)

**<font color=#1a73e8>作者：</font>** Darius Peteleaza, Razvan-Gabriel Dumitru, Bogdan Neamtu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pediatric brain tumors are a leading cause of cancer-related mortality in children, and their small, rare, and often low-contrast subregions make accurate manual delineation challenging. Reliable automated segmentation is therefore needed to support diagnosis, treatment planning, and response assessment. Accordingly, we introduce NeuroTS-Net, a three-dimensional encoder-decoder convolutional neural network architecture for multi-class semantic segmentation that incorporates a dual-scale raw-detail stream, adaptive low-resolution context selection, and detail-preserving multipath downsampling. These components preserve fine intensity and boundary information while efficiently modeling broader tumor context. NeuroTS-Net was trained on the BraTS 2026 pediatric dataset without external data or pretrained weights and evaluated against nnU-Net and MedNeXt under the same experimental protocol. NeuroTS-Net outperformed the baseline methods, achieving whole-tumor and tumor-core Dice scores of 0.938 and 0.937 on the internal validation set and 0.927 and 0.926 on the official challenge validation set. The code is open-sourced at: this https URL.

---


### 126. [Accelerated Decoding of Centroid Positional Encoding for Instance Segmentation](https://arxiv.org/abs/2609.16874)

**<font color=#1a73e8>作者：</font>** Carmelo Scribano, Filippo Muzzini, Nedyalko Prisadnikov 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Beyond model inference, the decoding stage, which converts raw network outputs into task-level representations, constitutes a significant portion of the execution cost. Despite its practical impact, prediction decoding has received comparatively little attention and is often implemented using generic CPU routines or inefficient GPU kernels, limiting the benefits of advances in model efficiency. In this work, we investigate the decoding overhead associated with a recent sinusoidal centroid encoding for Instance Segmentation, in which each pixel regresses a positional embedding of its instance centroid. This approach allows flexible segmentation without predefined proposals, but extracting instance masks from dense embeddings incurs a high computational cost. We present an optimized CUDA-based implementation of the decoding algorithm tailored to this encoding, explicitly addressing challenges related to parallelization, synchronization, and memory access on modern GPUs. Our solution significantly reduces decoding overhead and improves End-to-End inference latency, outperforming both CPU-based approaches and naive GPU implementations. The results demonstrate that efficient decoding is essential to fully exploit the advantages of advanced output representations and highlight the importance of jointly designing encoding schemes and their decoding algorithms for real-time computer vision systems.

---


### 127. [Temporally Consistent Graph Extraction and Matching for Longitudinal Angiographic Images](https://arxiv.org/abs/2609.16889)

**<font color=#1a73e8>作者：</font>** Linus Kreitner, Laurin Lux, Carmen Baumann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in angiographic imaging have enabled longitudinal visualization of the microvasculature. Image processing pipelines based on vessel graphs are able to resolve subtle temporal changes at the level of individual blood vessels. However, current strategies for graph extraction, refinement, and matching are highly sensitive, with even minuscule differences in the underlying segmentation map resulting in substantially different vessel graphs. These artifacts severely inhibit the ability to accurately match sequential vessel graphs of the same subject over time. To address this problem, we propose a strategy that matches graphs before jointly refining them. Specifically, we perform an early matching after basic graph extraction before removing spurious bulges and merging junctions in both graphs using joint information. In experiments with complex retinal vessel graphs, we demonstrate that this strategy results in a higher matched area without graph fragmentation compared to separate or no refinement, respectively.

---


### 128. [Disrupted Companionship: A Risk Assessment Framework and Cross-Platform Quantitative Analysis of Psychosocial Responses to AI Companion Disruptions](https://arxiv.org/abs/2609.16907)

**<font color=#1a73e8>作者：</font>** Chau Do, Yunhao Yuan, Koustuv Saha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI companions can provide meaningful relationships, yet these relationships remain vulnerable to platform-initiated changes. We study AI companion disruptions: platform changes that alter or terminate users' ongoing companionship with an AI. We compile 30 disruption events across major platforms, develop a taxonomy of six disruption types, identify three broad reasons for disruption, and propose a risk-assessment framework comprising four dimensions: relational discontinuity, population vulnerability, communication deficit, and transition-support deficit. Using longitudinal Reddit data, we estimate community-level psychosocial responses with a hierarchical Bayesian interrupted time-series model incorporating predictive controls. Across events, disruption onset was associated with immediate increases in anxiety, stress, suicidal expression, and grief activation, with relational discontinuity and transition-support deficit being associated with more adverse immediate responses across several outcomes. Our findings provide a cross-platform characterization of AI companion disruptions, quantitative evidence of their psychosocial impacts, and a prospective framework for assessing their potential risks before implementation.

---


### 129. [PiPS: Post-Hoc Prototypical Explanations for Interpretable Semantic Segmentation](https://arxiv.org/abs/2609.16909)

**<font color=#1a73e8>作者：</font>** Miłosz Adamczyk, Tymoteusz Zapala, Piotr Borycki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the increasing deployment of deep neural networks in critical systems, such as medical diagnostics and autonomous vehicles, ensuring their interpretability is crucial to building trust in decision-making systems. In the field of explainable artificial intelligence, prototype-based reasoning has gained particular popularity, as it mimics human cognitive processes by explaining model decisions based on visual similarity under the looks like this paradigm. While this paradigm has been thoroughly investigated in the context of global image classification, the interpretability of dense predictions, particularly semantic segmentation, remains largely unexplored despite its immense importance in tasks requiring precise object localization. Existing prototype-based interpretable segmentation models rely on ante-hoc architectures, which entails significant limitations because they require costly training from scratch and modifications to the network structure, ultimately leading to a noticeable drop in predictive performance compared to standard black-box models. To address this issue, we propose PiPS (Post-hoc interpretable Prototypical Segmentation), the first fully post-hoc solution for generating prototypical explanations for semantic segmentation models. Our method enables the extraction of intuitive, spatially localized explanations from any pre-trained network without modification or fine-tuning, thereby preserving 100% of the model's original predictive performance. This approach opens a new avenue for the safe and cost-effective deployment of transparent systems in advanced computer vision tasks. Codebase available at this https URL.

---


### 130. [Multi-Agent Learning with Cooperation-Driven Optimization Dynamics](https://arxiv.org/abs/2609.16917)

**<font color=#1a73e8>作者：</font>** Jarod Ketcha Kouakep, Sreyvi UANN, Timoteo Carletti  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multilayer Artificial Neural Networks trained via backpropagation are the basic blocks of many, more complex, classification algorithms. Their strength lies in the possibility of realizing, with arbitrary precision, any function. This result comes at the cost of the large number of involved parameters to be optimized. In this work, we propose a mechanism for cooperation, i.e., information exchange among several artificial neural networks, with the goal of reducing model complexity while maintaining performance. More precisely, we consider several "small" agents, i.e., containing fewer parameters than a reference "large" one, that during training share their predictions by incorporating this information into the loss function and thus directly influence weight updates. We consider several strategies for implementing cooperation, e.g., the voter model, majority model, and weighted average model based on an agent's confidence in its prediction. We numerically compare the accuracy of those strategies on several standard benchmarks. Our results support the claim that several small agents can outperform a single large model on a given classification task; the shared signals affect each agent's optimization algorithm by modulating both the descent direction and the step size, converging toward a global consensus. The proposed proof-of-concept significantly reduces the number of parameters to be trained while preserving comparable performance, thereby limiting computational resource usage.

---


### 131. [NeuroSymbEAD: A Large Scale Neuro-Symbolic Caption Dataset for Omni-Directional Embodied Autonomous Driving](https://arxiv.org/abs/2609.16919)

**<font color=#1a73e8>作者：</font>** Muhammad Ahmed Ullah Khan, Mohammed Elamine, Sheikh Talha Uddin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces NeuroSymbEAD, a large-scale neuro-symbolic caption dataset featuring an ego-centric knowledge graph (KG) of static and dynamic objects annotated with classes, categories, heading directions, orientations, and distances from the ego-vehicle. These annotations are used on the KITTI-360 dataset to generate multilevel textual captions representing a lightweight version of an ego-centric scene map. Outdoor scene-map reconstruction, visual recognition, and object grounding establish baselines for driving common sense and traffic/scene understanding. For these purposes, natural language-based grounded captioning of objects and their complex relationships is a widely adopted contextual representation for indoor scene tasks. Neuro-symbolic representations have proven effective in handling structured information for various computer vision and language applications. Our data annotation pipeline allows the generation of varied map segments, populating simulated or real objects within the bounding boxes predicted by any 3D object detection network, and building hierarchical text captions. We benchmark our neuro-symbolic and ontological caption generation using pre-trained grounding and learned auto-regressive captioning networks. By converting 3D driving scenes into structured ego-centric language, NeuroSymbEAD provides a benchmark for vision-language and foundation models for traffic-scene explanation, 3D reasoning, and interpretable autonomous-driving perception.

---


### 132. [Evaluating Mesh Reconstruction Methods for Crop Phenotyping](https://arxiv.org/abs/2609.16926)

**<font color=#1a73e8>作者：</font>** Karanvir Singh, Theo Morales, Binh-Son Hua 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Phenotyping an agricultural crop is crucial for studying its entire life cycle, as it provides vital insights to improve yield and, ultimately, food production. Doing the same for crops grown on remote sites is a challenge for the specialists who cannot be available on-site. 3D reconstruction techniques offer a promising solution to this problem by enabling crop digitization, allowing specialists to access the resulting 3D crop models from anywhere at any time. In this work, we evaluate recent 3D reconstruction pipelines for crop phenotyping. We focus on 7 mesh reconstruction pipelines and measure the fidelity and consistency of their outputs qualitatively and quantitatively. Our results suggest that the meshes produced by the GGGS, PGSR, and 2DGS are preferable to the other pipelines, owing to their quantitative metrics and visually pleasing outputs. The GGGS pipeline is better than the second-best pipeline (2DGS) by about 27\% on the radar chart with 5 dimensions, namely, User ratings, Chamfer distance, LPIPS, PSNR, and SSIM.

---


### 133. [Verbalizing Subliminal Learning Effects Using Text Optimization](https://arxiv.org/abs/2609.16927)

**<font color=#1a73e8>作者：</font>** Nathan Hu, Sanmi Koyejo, Christopher Potts  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Subliminal learning is a phenomenon in which a distillation dataset transmits traits from the teacher model that are not legibly encoded in the dataset itself. This introduces a new challenge for model development and creates new risks from data poisoning. In this work, we use text optimization to detect subliminal learning effects and describe them as legible prompts. Subliminal learning from a prompted teacher motivates our approach. We observe that this is a special case of context distillation and leverage this observation to show that, in theory, the prompted subliminal learning dataset identifies the teacher's prompt. We reduce recovering this prompt to a text optimization problem and present a method to approximately solve it. Our method, SALVE (Search-Aided Latent Verbalization), optimizes a soft prompt, queries the same model to verbalize it as text, and uses beam search to make the verbalization reliable. In the standard subliminal learning setting, SALVE reliably recovers legible prompts that name the teacher's trait, while common text optimization methods fail to do so. In addition, we find that there are settings in which SALVE recovers the teacher's trait from a dataset even when subliminal learning fails, but that modifying student training to improve context distillation can create subliminal learning effects. We lastly show that SALVE detects subliminal learning effects in three additional settings: (1) mixtures of subliminal learning data and unrelated data, (2) data generated when the teacher is biased via activation steering, and (3) subsets of real preference data selected via Logit-Linear Selection. Overall, our results deepen our understanding of subliminal learning and present SALVE as a method to proactively detect subliminal learning effects.

---


### 134. [Cybersecurity in Power Grids: Standards and Research Challenges](https://arxiv.org/abs/2609.16928)

**<font color=#1a73e8>作者：</font>** Ferran Bohigas-Daranas, Hamid Latif-Martinez, Nicolas Llorens 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper examines Smart Grid cybersecurity, emphasizing the critical distinctions between IT and OT environments. It analyzes grid architecture, substation threats, and key international standards, specifically IEC 62351, IEC 62443, and ISO 27001. Finally, it overviews latest research trends, including AI-driven threat detection.

---


### 135. [Repurposing Deep Limit Order Book Forecasting for Scenario-Conditioned Market Impact Modeling](https://arxiv.org/abs/2609.16930)

**<font color=#1a73e8>作者：</font>** Eljas Linna, Kestutis Baltakys, Derrick Manoharan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Limit Order Book forecasting models capture nonlinear market dynamics, but their ability to quantify the effects of counterfactual order book messages has not been systematically validated. We introduce a model-agnostic framework that compares a trained forecaster's predictive distributions before and after injecting mechanically valid counterfactual messages, defining short-horizon model-implied market impact. A Transformer-based forecaster recovered scenario rankings with a Spearman correlation of 0.99 and 97.2% directional agreement with realized historical outcomes among non-neutral scenarios. Observation-level analysis further showed that estimated impacts captured incremental sequence-dependent variation beyond scenario identity and the pre-event forecast. These results provide evidence that pretrained Limit Order Book forecasters can be repurposed for scenario-conditioned response modeling without retraining.

---


### 136. [MedPCFM-TED: One-Step Point Cloud Flow Matching for Implant Generation via Teacher-Guided Endpoint Distillation](https://arxiv.org/abs/2609.16934)

**<font color=#1a73e8>作者：</font>** Kamil Kwarciak, Marek Wodzinski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cranial implant generation is an important task in medical imaging. Recent point cloud based generative methods, particularly flow matching, offer strong reconstruction quality and efficient sampling, but still require multiple neural function evaluations during inference. This limits rapid generation of multiple plausible implant candidates. We propose Teacher-guided Endpoint Distillation (TED), a simple one-step distillation framework for conditional cranial implant generation on point clouds. TED trains a one-step student using teacher-guided endpoint supervision and geometric matching losses, while avoiding explicit path straightening. We evaluate TED on the SkullFix and SkullBreak benchmarks. TED achieves the best overall performance on the SkullBreak dataset, remains competitive on SkullFix, and provides the strongest Chamfer distance performance among the compared one-step methods. In addition, TED generates implants in approximately 0.04s per sample. These results show that one-step distillation can substantially accelerate conditional point cloud implant generation without sacrificing reconstruction quality.

---


### 137. [High-Fidelity Video Quality Assessment with VQA-Specific Saliency](https://arxiv.org/abs/2609.16946)

**<font color=#1a73e8>作者：</font>** Hakan Emre Gedik, Shashank Gupta, Alan Bovik  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> No-reference video quality assessment (NR VQA) has recently seen promising progress with deep learning. However, video data is inherently large, and processing them with deep models incurs high computational cost. This challenge is particularly acute in VQA, where preserving original-resolution cues and dense temporal information is critical for accuracy. Existing efficiency-driven preprocessing strategies, such as fragmenting, reduce computation but alter the input data distribution, limiting effective reuse of pretrained video foundation models (ViFMs). To address these challenges, we propose \textbf{H}igh-\textbf{F}idelity \textbf{V}ideo \textbf{Q}uality \textbf{A}ssessment (\textbf{HFVQA}), a framework built on fixed-size spatio-temporal (ST) patches that is fully compatible with pretrained ViFMs. HFVQA samples ST patches across multiple scales, including the original resolution, with minimal temporal subsampling to preserve low-level quality cues and semantic context. To limit computation, HFVQA introduces a lightweight auxiliary network trained end-to-end with the ViFM encoder to learn \textit{VQA-specific saliency}. Distilled directly from quality supervision, this saliency captures task-specific importance patterns, reflecting that video quality perception is dominated by a small subset of spatio-temporal regions. By combining high-fidelity spatio-temporal cues with learned, task-specific saliency, HFVQA achieves SOTA performance on standard NR VQA benchmarks while processing as little as 12\% of candidate ST patches, making high-fidelity ViFM-based VQA computationally tractable.

---


### 138. [AntennaFlow: A Generative Flow Model for Offset Correction in Phaseless Antenna Testing](https://arxiv.org/abs/2609.16948)

**<font color=#1a73e8>作者：</font>** Yongzhi Li, Chongting Shen, Menglin Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Near-field to far-field transformation is central to large-aperture antenna testing, yet two coupled challenges remain: costly phase acquisition at millimeter-wave bands and violations of the centering assumption under offset mounting. Existing methods address these issues separately, requiring either dense full-field data or offset vectors. We tackle both jointly by exploiting a key observation: amplitude fields under different offsets are coordinate-transformed views of the same near field. The challenge is to recover the center-aligned field from offset amplitudes without a phase or offset vector. We propose AntennaFlow, a three-stage framework: a contrastively learned encoder that maps offset views to an offset-invariant embedding, a deterministic flow-matching transport that maps offset amplitudes to center-aligned ones, and the Simplified Extrapolation Technique, whose Green-function Taylor expansion is valid only for centered fields. Experiments show that AntennaFlow enables fast, phaseless, offset-vector-free NF--FF reconstruction from sparse amplitude-only measurements, consistently outperforming existing baselines while preserving physical consistency.

---


### 139. [HUMAID-NER: A Disaster Tweet Dataset for Joint Named Entity Recognition and Event Classification via Uncertainty-Weighted Multitask Learning](https://arxiv.org/abs/2609.16964)

**<font color=#1a73e8>作者：</font>** Aijaz Ali, Nazish Basir, Sarfaraz Nawaz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rapid extraction of structured information from social media is important for humanitarian response, yet existing disaster tweet resources mainly provide document-level category labels without span-level entity annotations. We introduce HUMAID-NER, the first named entity recognition dataset built on the HumAID benchmark, containing 60,000 English disaster tweets annotated in BIO format across ten operationally motivated entity types and yielding approximately 175,000 labelled entity spans. Annotations are generated through a reproducible three-stage hybrid pipeline combining a spaCy transformer model, disaster-domain EntityRuler patterns, and structured regular expressions with priority-based overlap resolution. We also propose a joint multitask learning framework that performs disaster-specific named entity recognition and humanitarian event classification using a shared RoBERTa-large encoder. To reduce task conflict during joint training, the model uses homoscedastic uncertainty weighting with learnable task parameters and a two-stage training schedule that freezes the lower 18 of 24 encoder layers in the second stage. On the HUMAID-NER validation set, the proposed system achieves NER span micro-F1 of 0.841 and classification macro-F1 of 0.761 simultaneously. A real-time web dashboard demonstrates end-to-end deployment. The dataset, models, and pipeline code are released to support reproducibility and future crisis informatics research.

---


### 140. [Structural Negative Transfer in Federated Graph Neural Networks: Diagnosis, Causal Investigation, and the Limits of Divergence-Aware Mitigation](https://arxiv.org/abs/2609.16977)

**<font color=#1a73e8>作者：</font>** Chethana Prasad Kabgere, Shylaja SS  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning lets multiple participants train a shared model without pooling raw data, by exchanging locally trained model updates instead. Federated averaging assumes that averaging local models is a reasonable way to solve one shared problem when participants' data are broadly similar. Work on non-IID federated learning has shown that this assumption can withstand differences in label and feature distributions. We ask whether it survives a different strain specific to graph neural networks, where client graphs differ not in label or feature distribution but in structure itself, requiring the same shared weights to operate over fundamentally different topologies. We call the resulting harm structural negative transfer. In a federation of real citation networks and synthetic structural proxies, a structurally atypical client lost more than half its achievable accuracy simply by joining. In an initial six-client federation, two label-free structural statistics computable before training were strongly associated with this harm. Expanding to twenty clients showed that degree divergence remained associated with harm, although more weakly, and survived removal of domain contrast. Spectral divergence did not replicate, which we trace to a confound caused by the composition of the reference pool used for leave-one-out statistics. A causal intervention isolating topology found no significant effect. A degree-normalization mechanism held across twenty-four seeds but did not explain the harm when corrected. The best of five candidate fixes beat a tuned baseline only until a matched, structurally blind control was applied, after which the gain disappeared. What survives is a modest, partially replicated, degree-specific signal that is not yet a validated predictor at scale.

---


### 141. [PaperDoctor: Evidence-Grounded and Actionable Feedback for Scientific Papers in Progress](https://arxiv.org/abs/2609.16995)

**<font color=#1a73e8>作者：</font>** Kevin Qinghong Lin, Siyuan Hu, Pan Lu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoresearch agents are reshaping the research ecosystem, but they can also let flawed claims enter the literature at scale. Human advisors catch such issues in drafts through careful, traceable feedback, yet advisor-style assessment requires extensive manual effort and does not scale. To shift automated paper assessment from a judge to a diagnostician, we introduce PaperDoctor, an agent framework for pre-submission feedback with three key innovations. First, a holistic hierarchical framework evaluates writing, layout, references, code, theory, prior work, and experiments through three layers: L1 surface screening, L2 typed verifiers that route each claim to the appropriate evidence, and L3 reproducers that rerun experiments by priority. Second, each finding contains an observation, a pointer to specific evidence such as a sentence, equation, or code line, and a revision suggestion, making critiques auditable and actionable. Third, PaperDoctor selectively rebuilds and reruns experiments based on claim importance and compute budget, surfacing reproducibility gaps and quantitative limitations that are invisible from the manuscript alone. We evaluate PaperDoctor on 30 in-progress papers, yielding 70.6% agreement and all positive holistic scores, and on 40 manuscripts across machine learning, natural science, and social science, covering human- and AI-authored papers with code. Overall, PaperDoctor produces more auditable feedback than human and other agentic reviewers, pairs critiques with concrete suggestions by design, and complements dimensions often overlooked by human reviewers. We also develop an interactive interface that lets authors browse findings grounded in their paper. PaperDoctor reframes automated paper assessment as diagnosis rather than verdict, taking a concrete step toward AI advisors for more rigorous AI-assisted scientific discovery.

---


### 142. [ThinkFlow: Self-Evolving Probabilistic Latent Memory for Lifelong Conversational Agents](https://arxiv.org/abs/2609.17010)

**<font color=#1a73e8>作者：</font>** Cai Ke, Xin Liu, Han Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Lifelong conversational agents rely on memory systems to maintain deep, context-aware interactions with users. However, existing explicit textual memory pipelines suffer from a severe information bottleneck, often losing subtle behavioral patterns and emotional shifts. Furthermore, being typically static post-deployment, they cannot autonomously adapt to personal habits and preferences without manual feedback. Cognitive science, however, suggests that humans maintain mental models purely in a latent space and continuously refine them through predictive coding. Inspired by this, we propose \textbf{ThinkFlow}, a novel end-to-end latent memory framework for lifelong conversational agents. ThinkFlow bypasses the text bottleneck by dynamically compressing conversational flows into probabilistic latent memory skills, autonomously consolidating complex user states into disentangled, continuous vectors without semantic interference. To break this barrier, we introduce a test-time evolution paradigm. By coupling teacher-guided latent alignment to bootstrap the initial state with a self-supervised next-user-utterance prediction task for continuous refinement, the framework successfully overcomes cold-start challenges and achieves label-free lifelong personalization. Extensive experiments on long-term conversation benchmarks demonstrate that ThinkFlow significantly outperforms prevailing memory systems, providing highly personalized and contextually accurate responses over extended multi-session interactions.

---


### 143. [BeWater: Effective Protesters Navigate Watersheds in Street Networks](https://arxiv.org/abs/2609.17017)

**<font color=#1a73e8>作者：</font>** Guillaume Moinard, Matthieu Latapy  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> During social movements, protesters need to gather with limited communication means and limited knowledge other than what they observe in their direct surroundings. We propose BeWater, a fully distributed walking protocol that achieves gathering thanks to city information like street length, number of restaurants, number of lanes, or street names. Even though using only one of these observables performs poorly, we show that combining them in more advanced tactics rapidly leads to groups of significant sizes. To do so, our work leverages OpenStreetMap data to perform experiments on several real-world cities.

---


### 144. [CLARE: Scalable Class-Incremental Continual Learning via a Sparsity-Based Framework](https://arxiv.org/abs/2609.17026)

**<font color=#1a73e8>作者：</font>** Yunxiang Fu, Meng Lou, Zicheng Liao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning must balance the learning of new knowledge with the retention of previously learned knowledge to incrementally learn tasks from a data stream without catastrophic forgetting. While leveraging pretrained models has significantly advanced continual learning, existing methods exhibit a scalability bottleneck when trained sequentially on many tasks, suffering from performance degradation due to inter-task interference and loss of plasticity. Inspired by evidence that sparse fine-tuning achieves performance comparable to full fine-tuning, this paper presents a novel sparsity-driven continual learning framework. Our continual learning method, termed CLARE, operates in two stages: it first identifies a sparse, task-critical parameter mask via a sparsity-inducing objective, then performs mask-constrained fine-tuning by only optimizing parameters selected by the mask. This two-stage sparse adapter mechanism enables all tasks to be accumulated within a shared adapter space while reducing destructive interference across tasks. Extensive experiments demonstrate the scalability of CLARE. On the long task-sequence benchmark Omnibenchmark-1k, CLARE outperforms strong baselines in final accuracy by a large margin, e.g, improving EASE by 4.64% and 13.34% after learning 100 tasks, respectively.

---


### 145. [Distributed JEPA: A Self-Supervised Framework for Energy Forecasting](https://arxiv.org/abs/2609.17029)

**<font color=#1a73e8>作者：</font>** Liana Toderean, Tudor Cioara, Vasilis Michalakopoulos 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional energy forecasting solutions rely on task-specific supervision and energy asset representations, limiting transferability and the ability to capture general temporal dynamics across heterogeneous assets. We address this by proposing a distributed Joint Embedding Predictive Architecture (JEPA) for self-supervised learning from heterogeneous energy time-series. The framework predicts latent representations of masked temporal segments while integrating temporal observations and contextual information within a shared embedding space. To prevent representation collapse, training combines a latent-space predictive objective with covariance and temporal variance regularization. The evaluation was conducted on energy consumption and generation datasets under data-degradation scenarios and compared with a Transformer forecasting baseline. The learned representations remained stable (cosine similarity $\approx 0.98$; effective rank 185-235). JEPA achieved performance comparable to a Transformer on building energy data, higher $R^2$ in 3/5 consumer clusters, and outperformed the baseline on 9/10 unseen PVs ($R^2$=0.73-0.88 vs. <0.45), while showing greater robustness to missing data.

---


### 146. [Bi-FlowGS: Bridging Generative View Completion and Gaussian Geometry through Bidirectional Flow Co-Refinement](https://arxiv.org/abs/2609.17039)

**<font color=#1a73e8>作者：</font>** Yuetong Wang, Jinsheng Quan, Yi Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-view 3D scene reconstruction with 3D Gaussian Splatting (3DGS) is inherently underconstrained. Plausible renderings can also coexist with erroneous Gaussian geometry, as errors in positions or depths may be concealed by opacity, scale, and appearance; we term this failure mode Geometry Cheating. Existing regularization methods constrain geometry but remain limited to observed views, while video-diffusion-based methods complete unseen views yet mainly use them as RGB pseudo-supervision, underusing motion and temporal priors and lacking explicit geometry supervision. We present Bi-FlowGS, which uses optical flow to bridge generative view completion and Gaussian geometry regularization. Our plug-and-play Video-to-Geometry Flow Distillation (V2G) distills temporal correspondence priors from restored videos into Gaussian geometry to alleviate Geometry Cheating. Conversely, Geometry-to-Video Flow-Guided Restoration (G2V) uses the current 3DGS geometry to guide temporally consistent video restoration, providing more reliable generative supervision. Together, V2G and G2V form an implicit bidirectional co-refinement process, enabling restored videos and the optimized 3DGS scene to iteratively improve each other. Experiments demonstrate improved rendering quality and geometric consistency across wide-baseline and unbounded 360° benchmarks.

---


### 147. [Learning Options for Compositional Motor Control with Adapter Banks](https://arxiv.org/abs/2609.17042)

**<font color=#1a73e8>作者：</font>** Sreejan Kumar, Marcelo Mattar, Lea Duncker  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning flexible motor primitives is a hallmark of skilled motor control. Recent neuroscience theory proposes that motor primitives may be implemented as low-rank perturbations of a shared recurrent network, but leaves open how such a system is learned. We translate this principle into a novel architecture for learning motor skills end-to-end: a shared recurrent core modulated by a bank of residual adapters, each selected by a discrete latent code. Trained on closed-loop biomechanical control, the adapters develop emergent low-rank perturbations of the recurrent dynamics despite no architectural rank constraint, placing task representations in disparate subspaces of the shared core network. A simple high-level policy over the learned options, optimized while the whole network is frozen, sequences the low-rank adapters to produce novel out-of-distribution movements. We demonstrate the ability to generalize to novel motor sequences within the closed-loop control setting, improving on the generalization error of a task-input-conditioned multitask baseline by upto order of magnitude.

---


### 148. [Diagnosing the Fact-Grounding Gap in Multi-Hop Question Answering](https://arxiv.org/abs/2609.17043)

**<font color=#1a73e8>作者：</font>** Kevin Mo, Nathan Mo, Richard Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-hop question answering requires combining information from multiple documents to answer complex questions. These systems have grown increasingly capable, yet when they fail, the error is typically attributed to not finding the right documents. Whether this holds at the level of individual reasoning steps remains largely unexamined. We investigate this across three standard multi-hop QA benchmarks and find that failures decompose into two distinct modes: retrieval failures, where the needed passage was not retrieved, and extraction failures, where the passage was retrieved but the needed fact could not be extracted - a phenomenon we term the fact-grounding gap. Extraction failures account for nearly half of all per-hop deficiencies and are invisible to standard retrieval metrics. They remain unresolved by every retrieval intervention we test, establishing a ceiling for retrieval-only improvements. The gap's severity varies across benchmarks and question types, but extraction failures appear on every dataset we measure. Our findings reveal that retrieval failures and extraction failures are fundamentally different bottlenecks requiring different solutions - a distinction absent from current evaluation practice.

---


### 149. [Repurposing Unified Topological Signatures for Graph Representation Learning](https://arxiv.org/abs/2609.17061)

**<font color=#1a73e8>作者：</font>** Sanyam Sanjay Jain, Anshika Krishnatray, Aditya Sharma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Message-passing Graph Neural Networks (GNNs) iteratively propagate and aggregate local neighborhood information followed by global readout to learn graph representations. However, their discriminative power is upper-bounded by the Weisfeiler--Lehman (1-WL) graph isomorphism test. This prevents GNNs from distinguishing certain non-isomorphic graphs with identical local neighborhood structures, often leading to similar graph representations. Unified Topological Signatures (UTS) capture compact, multi-scale representation of global graph topology derived from persistent homology. We introduce two complementary UTS signatures: Graph_UTS- a static signature of the input graph topology, and Embedding_UTS- a dynamic signature of the evolving embedding topology. They encode structural information inaccessible to 1-WL-based message-passing GNNs, yet their capabilities are explored solely for post-hoc embedding-space analysis. We integrate UTS into GNN training across three architectural interventions: (i) UTS-Aug: augmenting with standard readout feature that encodes graph's true topology; (ii) UTS-Reg: topological regularizer that constrains representation collapse; (iii) UTS-Pool: topology-guided pooling that retains structurally critical nodes. We further leverage UTS as a layer-wise diagnostic to quantify oversmoothing during GNN training. Theoretically, we show that integrating UTS into GNN optimization strictly extends GNN expressivity beyond the 1-WL hierarchy. Experiments on three graph classification benchmarks show consistent benefits: Graph-UTS, Dual-UTS, and UTS-Pool improve accuracy across all three datasets, Embedding-UTS provides smaller but similarly consistent gains, and UTS-Reg's benefit varies across graph domains. Accuracy improves by up to 5.8% with Graph-UTS augmentation, by up to 1.9% with UTS-Reg, and achieves comparable performance to TOGL with UTS-Pool.

---


### 150. [Neuro-Symbolic Hierarchical Intention Anticipation in Human Behavior](https://arxiv.org/abs/2609.17064)

**<font color=#1a73e8>作者：</font>** Farnaz Soleimani, Abdelghani Chibani, Yacine Amirat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Assistive autonomous systems must anticipate human goals before an observed behavior is complete. This article formulates anticipation as goal inference from a partially observed multimodal episode together with structured prediction of the remaining behavior, rather than exact motor forecasting. A compact Hierarchical Planning Decoder (HPD) is attached to a frozen neuro-symbolic recognition encoder and predicts, at four ontological levels, the next actions, the remaining activities and low-level intentions, and the episode high-level intention(HLI). The decoder is trained with soft neuro-symbolic regularization combining transition-coherence and hierarchical continuity losses, and is decoded with hard reachability masks that enforce ontological validity at inference. On a compositional four-level benchmark of 15,002 multimodal episodes built over NTU RGB+D 120 features, three headline properties are observed together. The advantage over the strongest sequential baseline grows with the anticipation horizon, from +1.7 points at step 1 to +7.3 points at step 3 (top-5). Under compositional generalization, where one parent association per multi-parent low level intention is held out, this advantage widens to +4.9 points at step 1. At the episode level, 96.8% of anticipated trajectories satisfy the joint logic constraints, above the 88.1% strongest-baseline value and the 73.9% ground-truth floor; soft logic terms alone account for a 59.8 to 71.1% relative reduction of HLI-reachability violations, and the hard masks then eliminate them entirely. Neural generation supplies predictive ranking, symbolic constraints supply onto logical validity, and their combination yields coherent hierarchical anticipation while exposing remaining challenges in compositional goal generalization and unordered set prediction.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-219](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
