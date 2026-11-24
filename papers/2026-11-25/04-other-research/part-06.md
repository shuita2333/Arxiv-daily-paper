# 📦 其他研究 | 2026年11月25日

> 本类共 **569** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-569](./part-12.md)

---

### 251. [SKIA: Spatial-Knowledge Informed Attention for Robust Remote Photoplethysmography under Lower-Face Motion Artifacts](https://arxiv.org/abs/2611.29330)

**<font color=#1a73e8>作者：</font>** Van-Truong Le, Viet-Tham Huynh, Minh-Triet Tran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote photoplethysmography (rPPG) enables contactless physiological monitoring from facial videos, but facial motion, particularly mouth and jaw movements during cognitive and communicative tasks, can severely degrade signal reconstruction. We present SKIA, a lightweight, mask-guided framework that suppresses motion-prone lower-face regions while preserving physiological cues from the forehead and cheeks. Using the UBFC-rPPG benchmark, we first investigate static lower-face suppression in the classical CHROM pipeline. Static masking improves waveform Pearson correlation from 0.3507 to 0.4166 (p < 0.001) and reduces heart-rate mean absolute error (MAE) from 33.50 to 23.44 bpm. Building on this finding, we introduce SKIA-Net, a compact spatiotemporal architecture that combines raw facial frames, statically masked representations, and temporal motion differences to reconstruct blood volume pulse (BVP) waveforms. The full model achieves a Pearson correlation of 0.7522 and a heart-rate MAE of 3.73 bpm on UBFC-rPPG, outperforming single-stream variants. Ablation studies show that the static mask provides complementary information to raw appearance and that static anatomical priors outperform the tested dynamic optical-flow-based masking strategy. These results suggest that spatially informed, temporally stable masking can improve motion-robust rPPG estimation. Code: this https URL

---


### 252. [Hybrid state-space and attention neural operators for nonlinear structural dynamics under environmental loading](https://arxiv.org/abs/2611.29334)

**<font color=#1a73e8>作者：</font>** Anastasios Stamou, Rui Teixeira, Maria Nogal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The computational burden of repeated nonlinear time-history analyses limits their application for structural assessment and design. We therefore propose DeepOJamba, a hybrid neural operator that combines selective state-space recurrence with full attention to predict the structural response history due to dynamic loading. Physical-parameter conditioning and predicted-state transfer between sequences enable a single trained operator to represent varying system conditions and generate response histories beyond its training sequence length. DeepOJamba is evaluated on a 15~MW monopile offshore wind turbine under wind and wave loading. The proposed operator is compared to pure attention, pure state-space, Fourier, and DeepONet operators and is found to give the lowest window error on every channel and the lowest closed-loop fatigue and ultimate-load errors of $9.4\%$ and $6.0\%$, against $14.6\%$ and $8.7\%$ for the next-best pure attention operator examined. Moreover, on sea states outside the training wave band, the error slightly increases by approximately $0.4$ percentage points. Pure state-space operators can approach similar low errors only with a much wider convolution kernel tuned to the tower eigenperiod, which increases the training cost by $40\%$. In all, the results obtained support hybrid neural operators for robust long-duration structural response and demand prediction.

---


### 253. [MIMORPHEUS: Rethinking Cross-Modal Supervision for Human Pose Estimation from Radar Signals](https://arxiv.org/abs/2611.29341)

**<font color=#1a73e8>作者：</font>** Shizhao Zhang, Yanyan Zhang, Deshui Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning has shown promise for estimating human pose with multiple-input multiple-output (MIMO) radar through walls. Building paired radar and pose datasets demands considerable time and manual effort, while large visual pose datasets provide no corresponding radar echoes. Physical simulation can supply synthetic signals, but requires expertise in scattering models and can leave a gap between simulated and real data. To address this challenge, we introduce MIMORPHEUS, a framework that generates radar echoes from 3D human poses through conditional diffusion. To prepare echo and pose representations, MIMO-VAE compresses the echoes according to their channel and fast time sample structure, while SkeleCoder learns pose features through contrastive alignment with echo features. These pose features then guide diffusion in the MIMO-VAE latent space, and the VAE decoder reconstructs echoes from the generated latents. Once trained, the generator augments radar data by producing different echoes for a recorded pose and supplies the radar modality for pose annotations in existing visual datasets. In data augmentation experiments, our method reduces MPJPE by 6.8%-11.2% across four radar pose estimators. Transfer experiments with three public pose datasets also show that visual pose annotations can supply useful radar training data. Code will be made publicly available on GitHub.

---


### 254. [A Multi-Criteria Evaluation of Color Normalization Methods in Histopathology: Nuclei Preservation, Artifact Sensitivity, Background Fidelity, and Downstream Performanc](https://arxiv.org/abs/2611.29348)

**<font color=#1a73e8>作者：</font>** Falah Jabar, Aria Torkpour, Pasquale Lombardi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for nuclei detection and classification may generalize poorly across medical centers because of variations in staining and scanning. Although color normalization aims to reduce these variations, its effects on nuclear structure, background preservation, artifact sensitivity, and nuclei detection and classification performance have not been systematically evaluated. We present a procedure to benchmark 11 classical and deep learning normalization methods using 7 public and private nuclei datasets. Additionally, we investigate the effect of 7 input color spaces. The normalization methods differed in their effects on nuclear structure, background, and sensitivity to artifacts. However, detection and classification performance varied more across datasets than across normalization methods, and the input color space had limited influence. No single method performed best on all criteria, and image-level metrics did not reliably predict downstream performance, highlighting the need for nuclei- and structure-aware normalization methods. To support this work, we introduce WSI Quality Control and Normalization (WSI-QCN), a publicly available pipeline for robust whole-slide image quality assessment and color normalization; the source code is available on GitHub.

---


### 255. [DuetFHE: Compiling Dual-Lane Nonlinear Circuits for Complex-Packed CKKS Inference](https://arxiv.org/abs/2611.29350)

**<font color=#1a73e8>作者：</font>** Ke Changke, Jian Wang, Xuan Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Complex packing in CKKS stores two real streams in the real and imaginary lanes of each slot. Direct squaring couples the lanes, while squaring them separately requires two ciphertext-ciphertext multiplications (HMults). DuetFHE is a GPU compiler that uses a phase transformation to square both lanes independently with one HMult. It reuses dual-lane squares in polynomial activations and the modular-reduction stage of CKKS bootstrapping. The compiler further plans ciphertext scales and reuses conjugates to sustain the complex-packed representation across stages. On a single RTX 5090, DuetFHE accelerates four polynomial activations by $1.60$--$1.79\times$ over direct evaluation on two real ciphertexts. For two-image AESPA ResNet-20 inference, it maintains packed execution across convolutions, square activations, and bootstrapping, achieving a $1.97\times$ end-to-end speedup over the fastest tested EasyFHE batched baseline on both the RTX 5090 and RTX PRO 6000.

---


### 256. [NPUFHE: An Efficient CKKS Execution System for Ascend NPUs](https://arxiv.org/abs/2611.29353)

**<font color=#1a73e8>作者：</font>** Ke Changke, Jian Wang, Xuan Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully homomorphic encryption (FHE) enables computation directly on encrypted data, but its substantial computational cost hinders adoption in privacy-preserving artificial intelligence (AI) applications. Neural processing units (NPUs) already deployed in AI infrastructure provide a practical platform for FHE acceleration. However, after mapping the number theoretic transform (NTT) to matrix multiplications on Ascend NPUs, modular arithmetic and representation conversion on the Vector backend still incur substantial overhead at stage boundaries. Evaluation-key material of key switching also increases storage and data-transfer costs, and whole-limb task assignment causes tail load imbalance.
We present NPUFHE, an end-to-end CKKS execution system optimized for Ascend NPUs. To reduce modular recovery and twiddle costs in NTT, we propose Boundary-Optimized NTT, which eliminates intra-axis modular recovery, compiles intra-axis twiddle factors into matrix constants, and introduces two-level folded modular recovery at axis endpoints. To alleviate evaluation-key storage and transfer pressure, we design Compact Shoup encoding, which halves the key representation through local coefficient recovery. Finally, we propose Cost-Aware Parallel Tiling to mitigate tail load imbalance caused by whole-limb task assignment. It uses a cost model to adaptively partition tail tasks and smooth stepwise latency increases.
We integrate the above designs into OpenFHE. On one Ascend 910B4, full-packing CKKS bootstrapping with real evaluation keys takes 0.95 s, encrypted CIFAR-10 ResNet-20 inference with bootstrapping requires 9.87 s per image, and encrypted MNIST inference achieves an amortized latency of 19.81 ms per image. The peak NTT throughput of NPUFHE reaches up to $184.22\times$, $2.04\times$, and $4.46\times$ that of OpenFHE on CPU, TensorFHE, and CROSS, respectively.

---


### 257. [Scenario Compliant Indoor Pedestrian Trajectory Reconstruction from Partial Observation](https://arxiv.org/abs/2611.29366)

**<font color=#1a73e8>作者：</font>** Qi Dang, Luis Quintero, Shibo Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pedestrian trajectory reconstruction is vital for applications ranging from security surveillance to indoor navigation. While existing probabilistic and generative frameworks have shown success in outdoor GPS-based trajectory imputation, they often fail in indoor settings where movement is strictly governed by dense geometric constraints such as walls and corridors. Standard models typically treat trajectories as unconstrained coordinate sequences, leading to physically infeasible paths with high collision rates. To address this, we propose a map-conditioned generative framework based on conditional diffusion models. Our approach explicitly integrates dense scenario maps as structured spatial inputs via a CNN-based encoder, allowing environmental geometry to guide the iterative denoising process. Furthermore, we employ an endpoint-aware mechanism by embedding observations (start and end points) directly into the scenario map, providing critical spatial anchors through image-level features. Experiments on simulated indoor trajectories and the real-world Shopper trajectory dataset, with three training seeds, show that our method achieves the lowest errors among the compared generative methods. Scene conditioning reduces the collision and invalid rates by 19\% and 46\% on the simulated dataset, whereas on real shopper data the gains are consistent but small, mainly because the model rarely learns to route around obstacles between the endpoints. Compared with a shortest-path planner, which never collides, our method better captures the variability of real motion (31\% lower CRPS), but the timing of stops is reconstructed only partially. These results show that explicit environmental context improves physical consistency, while reconstructing realistic human motion in real indoor spaces remains challenging. Our code is available at this https URL

---


### 258. [ClothCast: Generative Cloth World Modeling under Partial Observability](https://arxiv.org/abs/2611.29369)

**<font color=#1a73e8>作者：</font>** Yushen Hu, Yilong Song, Zhen Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models support robotic manipulation by predicting how the scene evolves under a planned action. For garments this prediction is notoriously difficult: deformations are complex, and self-occlusion leaves much of the cloth unobserved. Planned gripper trajectories provide a useful motion prior because cloth held by a gripper moves with it, while the remaining deformation must be predicted. We introduce ClothCast, a world model that applies this prior to the cloth's points and learns the residual motion. ClothCast takes one RGB-D observation, the camera pose, the robot's own model and the planned gripper trajectories, with no cloth mesh or material parameters. It lifts the observation to a layered point set that includes hypothesized occluded layers, carries the points with a blended rigid prior derived from the gripper poses, and predicts the residual motion with a video-diffusion point-flow model. Over entire 4- to 11-second episodes at 10 Hz, the moved points are rendered into depth, from which a geometry-conditioned completion model synthesizes RGB; after release, a hand-designed settling step replaces the learned motion. We further release ClothCastBench, 10,000 simulated dual-arm cloth-manipulation episodes with the ground-truth cloth mesh, including occluded layers, at every frame. On 492 held-out episodes, ClothCast achieves 2.5x lower sequence-averaged visible-surface Chamfer distance than Flex-{\pi}, the strongest baseline in geometry (14.0 mm vs. 35.6 mm), and 3.7 dB higher cloth-region PSNR than Cosmos-Predict2.5, the strongest baseline in cloth PSNR. On a 50-episode ablation subset, the rigid prior alone, applied to ClothCast's learned initial geometry with the same post-processing, already outperforms both geometry-capable baselines, and the learned residual lowers its error by about a third.

---


### 259. [Chameleon: Exploring Risk Interpretation through Scene-Matched Textures in Virtual Reality](https://arxiv.org/abs/2611.29376)

**<font color=#1a73e8>作者：</font>** Yichen Andy Yu, Wanru Jovie Li, Yang Zhan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Users in virtual reality need to judge contact risks around physical objects while remaining engaged in the virtual scene. Scene-matched textures give physical objects a place in virtual reality and provide visual cues for interaction. We examine how Chameleon's risk-aware textures are perceived during a reaching task. A study with 42 participants compared scanned appearances with red warnings, uniform environment textures, and risk-aware scene-matched textures. Participants rated the risk-aware condition more favorably on four aspects of perceived cue clarity than both alternatives. Interviews connected visible warnings with initial caution and linked confidence in physical interaction to material expectations and intended actions. Awareness of an object's location did not necessarily imply confidence in interacting with it. These findings motivate risk cues that connect depicted materials to the physical properties relevant to an intended action, and ways to support verification during interaction.

---


### 260. [SpectralGS: Spectral Gaussian Splatting for Unsupervised Spectral Super-Resolution](https://arxiv.org/abs/2611.29388)

**<font color=#1a73e8>作者：</font>** Qiaoying Qu, Bin Pan, Chen Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised spectral super-resolution aims to recover spectral information from RGB images without paired hyperspectral data. However, the limited spectral information in RGB observations makes learning an effective spatial-spectral representation challenging, requiring the incorporation of structured spectral modeling with sensor imaging. In this paper, we propose SpectralGS, a spectral Gaussian splatting framework comprising two components: Shared Spectral Gaussian Representation and Spectral Response Projection Rendering. The representation module constructs a continuous spatial-spectral representation via shared spectral and local spatial Gaussian primitives, exploiting the low-rank spectral structure of hyperspectral images. The rendering module utilizes the spectral response function (SRF) to apply integral projection to the continuous representation, blending it to generate an RGB image. Consistency between the rendered and observed RGB images provides training supervision. Our main contribution is a Gaussian splatting framework that integrates structured continuous spatial-spectral representation with imaging response-based rendering, enabling unsupervised spectral reconstruction. Extensive experiments demonstrate that our method outperforms current state-of-the-art methods.

---


### 261. [PINE: Point, Instance and Normal Estimation in One-Step Diffusion Model](https://arxiv.org/abs/2611.29389)

**<font color=#1a73e8>作者：</font>** Zeyu Ren, Jie Ni, Rui Qian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding a scene requires both geometry and semantics: geometry recovers its spatial structure, and semantics separates it into objects. Current models obtain the two from separate networks or separate passes. We present PINE, a one-step Omni Diffusion Transformer that predicts the point map, the surface normals, and the instance map of an image in one forward pass. PINE treats each map as a token stream, and a stream mask decides which streams interact. A camera-aware ray encoding positions every token by its camera ray rather than its pixel. Grounding attention adds the affinity of pretrained DINOv3 features to the attention logits. Trained on only 139K synthetic images for geometry, PINE achieves state-of-the-art point maps whether or not intrinsics are given and the best average rank on surface normals. It also exceeds SAM on large objects with less than 1 percent of its training images, and it predicts all three maps 5.7x faster than MoGe-3 with SAM.

---


### 262. [AgroVG+: Generalized Visual Grounding in Agriculture with Region-Supervised Action Generation](https://arxiv.org/abs/2611.29396)

**<font color=#1a73e8>作者：</font>** Haocheng Li, Juepeng Zheng, Guilong Xiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalized visual grounding in agriculture requires localizing all objects that match a natural-language description and recognizing when no matching target is present. We introduce AgroVG+, a dataset whose referring expressions are all written and reviewed by agricultural experts based on image content and corresponding target sets. The dataset comprises 7,404 images and 10,081 query records across six agricultural scene families, covering single-target, multi-target, and target-absent cases. We also propose ReSAG (Region-Supervised Action Generation), a framework that couples regional evidence supervision with explicit box-generation and termination decisions. ReSAG assigns each target an equally weighted supervision term on a shared spatial evidence distribution computed before answer generation. The BOX/END protocol exposes a choice between generating another box and terminating the response at box boundaries, while coordinates are generated using the original language vocabulary. Regional and sequence objectives jointly train a shared language decoder. On AgroVG+, ReSAG outperforms coordinate-only fine-tuning on single- and multi-target exact-set accuracy, and achieves higher aggregate accuracy than either component alone in ablations.

---


### 263. [MSBench: Benchmarking Script-Controlled Multi-Shot Text-to-Video Generation](https://arxiv.org/abs/2611.29417)

**<font color=#1a73e8>作者：</font>** Tao Huang, ZiHao Liang, Junhao Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video (T2V) models can now generate visually plausible short clips, but multi-shot generation requires a different set of skills: composing multiple shots with intended cut timing, transition style, camera language, and cross-shot continuity. How far this multi-shot output can be controlled from text remains unmeasured: existing benchmarks either evaluate single shots or, when they provide shot-level scripts, typically check whether the requested shots appear but not when they change or how they are joined. We introduce MSBench, a benchmark for controllable text-driven multi-shot video generation built around structured Scene-Entity-Shot mini-scripts that specify each shot's time span, camera state, content, and outgoing transition. MSBench defines a four-dimensional hybrid evaluation framework spanning Visual Quality, Dynamic Quality, Semantic Alignment, and Cross-Shot Consistency with 11 sub-metrics. Experiments on 14 commercial and open-source systems show that visual quality does little to separate the systems, whereas multi-shot control does: many models cut mainly on scene changes and render requested gradual transitions as hard cuts. Human evaluations further validate MSBench, with its system ranking reaching a Spearman correlation of 0.87 with human preferences. The project page is available at this https URL.

---


### 264. [HKD-ACPA: Heterogeneous Knowledge Distillation Adversarial Cyber-Physical Attacks in Power Grids](https://arxiv.org/abs/2611.29418)

**<font color=#1a73e8>作者：</font>** Junhao Ren, Honglin Gao, Shuo Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning-based algorithms assist power-grid control centers in localizing transmission-line attacks, yet existing adversarial attacks typically require white-box access or repeated online queries. We study a practical zero-query setting in which an adversary coordinates physical, denial-of-service (DoS), and false data injection (FDI) attacks using only local measurements and historical detector outputs. To bridge the input-view asymmetry between local adversarial observations and DoS-masked control-center measurements, we propose Heterogeneous Knowledge Distillation Adversarial Cyber-Physical Attacks (HKD-ACPA). HKD-ACPA distills historical detector predictions into a heterogeneous graph surrogate ensemble and trains a residual calibration module to correct the view-induced logit discrepancy. Over this calibrated surrogate, we formulate sparse, magnitude-bounded FDI synthesis with a group-balanced objective that jointly induces missed detections and false alarms, and solve the resulting hybrid discrete--continuous problem via bi-level projected gradient-based proximal policy optimization (PGPPO). Experiments on the IEEE 30-bus and 118-bus systems show that HKD-ACPA outperforms all surrogate-based baselines across every sparsity budget and surpasses online-query attacks in eight of ten system--budget settings without querying the detector model.

---


### 265. [HorizonFlow: Few-Step Video Distillation in 600 Iterations](https://arxiv.org/abs/2611.29431)

**<font color=#1a73e8>作者：</font>** Xianglong Guo, Haobo Xu, Zanyi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distribution matching distillation (DMD) enables fast video generation by distilling a multi-step teacher into a few-step student. However, DMD-based methods often suffer from unnatural motion and costly training. We trace these limitations to the DMD gradient, which jointly optimizes appearance, layout, and motion without distinguishing their learning dynamics. Its static component, which carries appearance and layout, has a much higher signal-to-noise ratio than its motion component. As a result, per-frame quality converges within a few hundred iterations, whereas motion lags far behind. Beyond being noisy, the gradient also lacks two signals. (1) Video VAEs encode several frames into one latent frame (four in Wan2.1), and the gradient provides little guidance for spreading motion over these frames, causing periodic stutter. (2) DMD does not constrain the final sampling step to preserve the layout set by earlier steps, so objects merge and drift once the video moves. We propose HorizonFlow, which decouples the correction of motion from that of layout. It keeps the DMD loss and only shifts its regression target, with one training-only correction in the motion component and one in the orthogonal layout component. Chunk Evenness addresses (1) by spreading the motion of each latent chunk evenly over its frames, and Semantic Commitment addresses (2) by anchoring the coarse layout to the teacher's completion of the student's last step. In only 600 iterations, HorizonFlow distills Wan2.1-T2V-1.3B into a 4-step model using 8.4k training samples, 4.6-304$\times$ fewer than prior work. On VBench, HorizonFlow outperforms all released few-step Wan2.1-T2V-1.3B models. The same recipe transfers to Cosmos-Predict2.5-2B, where our student outperforms NVIDIA's distilled model. Code: this https URL

---


### 266. [Ride on Anything: Contact-Coupled Monocular 4D Reconstruction of a Rider and Horse in Camera and World Frames](https://arxiv.org/abs/2611.29435)

**<font color=#1a73e8>作者：</font>** Zehang Weng, Ci Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address the reconstruction of a horse and its rider from a single video. When a human estimator and a horse estimator are applied independently, both meshes can fit their silhouettes well while the rider hovers beside or passes through the horse, slides along its back and jitters relative to it. These errors lie along the camera axis and are not visible in the input view. We present Ride on Anything (RoA), a general, training-free methodology for reconstructing a person riding an animal, which couples frozen estimators of the rider and the mount at test time. We instantiate it for horseback riding with SAM 3D Body and 4DEquine. RoA aligns both estimators on a common frame index, projects both subjects through one pixel-isotropic camera initialized from the horse estimator, and jointly optimizes bounded corrections under interaction terms defined in the horse's body frame, including a collision term based on generalized winding numbers that remains valid on the non-watertight horse mesh. The result is lifted to a levelled world frame using the camera rotation from the background and the field of view from MoGe-2. On our riding clips, the raw outputs of the two estimators leave the rider's pelvis 15 cm from the horse's back on average. RoA reduces this seat gap to 1 cm, the drift of the seat along and across the spine by 64% and 89%, the 90th-percentile penetration depth by 57%, and the share of rider surface inside the horse from 12.1% to 7.9%. The motion is markedly smoother (94% lower acceleration of the rider relative to the horse, 80% lower horse jerk), while the rider's silhouette IoU decreases from 0.59 to 0.52. Qualitatively, the rider stays seated on the horse and moves together with it. A quantitative evaluation of 3D accuracy awaits calibrated recordings of ridden animals. We also test a clip outside the task, a horse led on foot, and analyse the failure modes.

---


### 267. [Seeing Through Preferences: Recovering Hidden Local Preference Neighborhoods for Text-to-Image Alignment](https://arxiv.org/abs/2611.29436)

**<font color=#1a73e8>作者：</font>** Pulkit Bansal, Vivek Srivastava, Shirish Karande  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aligning text-to-image (T2I) diffusion models with human preferences typically relies on large-scale pairwise annotations, which are expensive to obtain and provide only sparse supervision. Moreover, not all preference comparisons contribute equally to learning: comparisons between semantically distant images often reveal little about the fine-grained perceptual factors underlying human judgments. We argue that informative supervision can arise from local preference neighborhoods surrounding human-preferred images, where semantically aligned alternatives expose meaningful perceptual and structural differences. Motivated by this observation, we propose PrefLens, a framework that recovers local preference neighborhoods from sparse human feedback. Specifically, PrefLens generates controlled perceptual variations around preferred images that largely retain semantic identity and selects compact sets of informative neighbors in a reward-defined preference space induced by pretrained reward models. By transforming each human preference annotation into a structured neighborhood of informative comparisons, PrefLens enriches supervision without requiring additional human labeling. Our experiments and diagnostic evaluations show that the recovered neighborhoods capture human-relevant preference characteristics and provide effective supervision for preference alignment across diverse settings.

---


### 268. [Optimal Bandits with Switching Costs: $(T/\log(T))^{2/3}$ Regret](https://arxiv.org/abs/2611.29438)

**<font color=#1a73e8>作者：</font>** Chenyu Gan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study adversarial bandits with switching costs. For $K$ arms, $T$ rounds, unit switching costs, and oblivious losses in $[0,1]$, we prove that the minimax regret is \begin{equation*}
\Theta\!\left(\min\left\{T,
\frac{K^{1/3}T^{2/3}}{\log^{2/3}(2+T/K)}\right\}\right)\,. \end{equation*} This shows that simple blocking, which plays one arm throughout each block, is suboptimal. Our algorithm makes at most a constant number of switches at random times within each block. The key idea for the improvement is to extract more information per switch by giving greater weight to observations near switching times. We also introduce detours, during which the learner temporarily plays a newly sampled arm. Larger observed losses make a detour more likely. These detours cancel temporal correlation terms induced by blocking while preserving the observations used in the estimates. A matching lower bound follows from a refined analysis of a modified multiscale random walk construction.

---


### 269. [NRSnooper: Enabling Real-Time Bidirectional Traffic Decoding in Commercial 5G NR Networks](https://arxiv.org/abs/2611.29439)

**<font color=#1a73e8>作者：</font>** Tuan Dinh Hoang, Quang Huy Pham, Taekkyung Oh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Decoding both uplink and downlink cellular traffic reveals lower-layer protocol behavior, unprotected signaling, and encrypted higher-layer packets beyond what scheduling metadata exposes. In commercial 5G NR networks, however, passive decoding must overcome UE-dedicated configurations hidden in encrypted signaling, unknown identifiers of ongoing connections, and the computational demands of wideband traffic.
We present NRSnooper, a passive sniffer that decodes downlink control and bidirectional data traffic in real time, including traffic from already-connected UEs and traffic after encrypted configuration updates. NRSnooper learns reusable physical-layer configurations through an instrumented open-source UE that reproduces commercial UE capabilities. It recovers connection-specific identifiers from ongoing transmissions and selects matching configurations through CRC-validated data decoding. A hybrid CPU-GPU pipeline sustains continuous wideband processing.
Evaluations on a controlled testbed and two commercial networks show that, compared with using only configurations from unencrypted signaling, NRSnooper decodes 1.3x and 6.3x as many control messages and 9.0x and 17.7x as many downlink data blocks, respectively. NRSnooper also decodes traffic from an already-connected UE during an ongoing phone call and achieves real-time bidirectional decoding on 100 MHz commercial NR channels.

---


### 270. [Exploring Attention-Driven Deep Learning for Accurate Lung Nodule Segmentation](https://arxiv.org/abs/2611.29450)

**<font color=#1a73e8>作者：</font>** Nima Shafiei Rezvani Nezhad, Meysam Mansouri, Saeid Ghayour 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study explores the application of various deep learning models for the segmentation of lung nodules using LIDC-IDRI. Unlike traditional approaches that utilize the full dataset, our work emphasizes the efficacy of training models on a filtered subset of 356 samples. Novel configurations, including attention mechanisms and advanced preprocessing strategies, were employed to optimize segmentation accuracy. Among the models evaluated, the DPL nkNet50 with a Channel Attention Bridge and ResNet backbone demonstrated the highest performance with a Dice score of 0.86, significantly outperforming conventional architectures. This work underscores the potential of leveraging data efficiency and tailored architectures in achieving robust segmentation performance, paving the way for improved computer-aided diagnosis in clinical settings.

---


### 271. [RSWP: Robust SO(3)-Equivariant Watermarking for Panoramic Images](https://arxiv.org/abs/2611.29468)

**<font color=#1a73e8>作者：</font>** Pengzhen Chen, Yanwei Liu, Xiaoyan Gu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust watermarking for panoramic imagery is impeded by the topological mismatch between spherical signals and planar representations. Conventional methods fail under $SO(3)$ viewing rotations due to non-linear geometric warping and struggle with viewport extraction, which typically necessitates computationally expensive inverse remapping. To address these challenges, we propose RSWP, a watermarking framework grounded in icosahedral group theory. Leveraging the property that the icosahedral group ($\mathcal{I}_{60}$) serves as the largest discrete subgroup of $SO(3)$, we decompose spherical rotations into tractable local planar rotations and combinatorial facet permutations. Accordingly, we introduce a decoupling architecture that embeds watermarks into discrete facets and a theoretically guaranteed Equivariance-to-Invariance decoding paradigm. By employing an equivariant feature extractor followed by a permutation-invariant sorting module, this paradigm rigorously synchronizes rotation-distorted features. Moreover, the dual-extractor design inherently supports direct, blind watermark retrieval from partial 2D renderings without geometric calibration. Extensive experiments demonstrate that RSWP achieves state-of-the-art robustness against continuous $SO(3)$ rotations and viewport transformations while preserving high visual fidelity.

---


### 272. [Neutron Imaging Enhancement for Lithium Batteries Based on Swin-Transformer and Image Fusion](https://arxiv.org/abs/2611.29479)

**<font color=#1a73e8>作者：</font>** Hansheng Ding, Fanxu Meng, Tian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neutron imaging is highly sensitive to light elements such as lithium and is therefore valuable for non-destructive testing (NDT) and analyzing internal structural evolution in lithium batteries. However, limited neutron-source flux and detector performance often result in images with mixed noise, low contrast, and blurred edges, hindering accurate assessment of battery internal states. To address these issues, this paper proposes a lithium-battery neutron image enhancement method combining an improved Swin-Transformer with spatial-domain image fusion. First, an improved Swin-Transformer incorporating Multi-Dconv Head Transposed Attention (MDTA) and Global Response Normalization (GRN) extracts and reconstructs image features to suppress high-density white spots and Gaussian-Poisson mixed noise. Second, guided filtering and a gradient-adaptive mask are used for selective edge enhancement, while Contrast Limited Adaptive Histogram Equalization (CLAHE) improves local contrast. Finally, a spatial-frequency (SF)-based local block-weighted fusion mechanism adaptively combines the edge-enhanced and contrast-equalized images to preserve microscopic details while suppressing noise. Experiments show that, compared with BM3D, DnCNN, and GAN, the proposed method achieves strong performance in full-reference and no-reference evaluations. Its best PSNR and SSIM reach 33.0517 dB and 0.9637, respectively, while the NR-IQA and Natural Image Quality Evaluator (NIQE) scores are as low as 0.1794 and 4.0974. The method reduces artifacts and over smoothing, improving the visual fidelity and structural identifiability of lithium-battery neutron images.

---


### 273. [OnCache: Learning Dynamic Caching Schedules for Efficient Diffusion Inference](https://arxiv.org/abs/2611.29480)

**<font color=#1a73e8>作者：</font>** Zhikang Xie, Xichen Ye, Yifan Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have revolutionized generative tasks but incur high inference latency due to iterative denoising. Cache-based strategies accelerate inference by reusing intermediate features, yet they largely rely on static, sample-agnostic schedules. Our empirical analysis reveals two factors that these schedules overlook. (i) denoising dynamics and computational requirements vary across prompts, motivating adaptive computation allocation. (ii) sensitivity to caching errors varies across timesteps, so static schedules may reuse features at error-sensitive steps or waste computation at less sensitive ones. We therefore propose OnCache, a dynamic caching framework that makes prompt-adaptive decisions online about how much computation to allocate and when to refresh cached features. A policy is trained offline on paired compute and cache continuations from identical denoising states, using differences in terminal fidelity and the number of function evaluations (NFE) to account for the downstream consequences of each decision. To further improve the generation quality, a neural corrector compensates for caching-induced errors and mitigates their accumulation throughout the denoising trajectory. Both components are lightweight and introduce negligible additional inference latency. On FLUX.1-dev, OnCache achieves a nearly $3\times$ generation speedup at $1024^2$ resolution, with LPIPS of $0.156$ and SSIM of $0.860$. We further extend OnCache to video generation on Wan2.1-T2V-1.3B, achieving state-of-the-art efficiency--quality trade-offs across both modalities.

---


### 274. [Vanishing Initialization Turns Diagonal Tensor Gradient Flow into Greedy Matching](https://arxiv.org/abs/2611.29484)

**<font color=#1a73e8>作者：</font>** Dmitry Yarotsky, Eugene Golikov, Yaroslav Gusev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study gradient-flow (GF) learning of tensors from vanishing initialization in canonical polyadic (CP) factorization models. For tensors of order $\nu\geq3$ whose targets are diagonal in mode-wise orthonormal bases, we prove that the limiting learning dynamics follows a simple greedy bipartite matching process. Each rank-one component of the model, called an atom, can potentially learn each rank-one component of the target, called a scalar sector. Every atom--sector pair has an initialization-dependent activation clock, representing the time at which the atom would grow to macroscopic size in that sector if the pair evolved in isolation. Processing these clocks in increasing order and selecting a pair whenever neither its atom nor its sector has been selected before determines the sequence of actual learning events. We prove that the GF trajectory converges to the corresponding staircase of learned target components. The task of learning modular addition by a CP model with complex weights falls exactly into this framework after Fourier diagonalization. Its activation clocks are independent and identically distributed, allowing us to combine the GF reduction with known random matching asymptotics and derive an explicit, distribution-free large-system loss curve after time reparametrization. We also obtain an asymptotic formula relating this curve to the original GF training time. For models with real weights, conjugate Fourier modes instead form two-dimensional blocks with richer internal structure. We characterize their rank and border-rank cascade and conjecture that the corresponding GF dynamics follows interleaved multi-stage learning processes.

---


### 275. [Meddies-PII: A Multilingual Framework for Personally Identifiable Information Extraction in Clinical De-identification](https://arxiv.org/abs/2611.29491)

**<font color=#1a73e8>作者：</font>** Le Linh Uyen, Christian Hoang, Ho Dinh Tri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual PII extraction in clinical text is limited by scarce governed data and by synthetic corpora whose construction is thinly documented. We present a large multilingual dataset covering seventeen languages, including seven Southeast Asian languages, and nine PII labels. We also document a detailed generation pipeline and release the complete prompts, catalogues, checks and label maps. A compact 350M-parameter BIOES token classifier trained on the resource achieves the highest score on all fifteen public benchmarks, significantly ahead of the strongest of four public systems on fourteen of them, with a mean exact-match F1 of 0.827 against 0.672 for the strongest system. We also tested it, without adaptation, on multilingual benchmarks, including two human-annotated German and Spanish clinical-style corpora, where it is competitive with the best public systems once annotation conventions are aligned, and is best in four of ten MultiGraSCCo languages; the results show that performance transfers across public benchmarks. We also analyse the data and find almost no near-duplicates and no text overlap between training and any evaluation set. The dataset, benchmark, model, generation framework and evaluation code are planned for public release upon acceptance.

---


### 276. [Learning Global Probabilistic Explanations](https://arxiv.org/abs/2611.29493)

**<font color=#1a73e8>作者：</font>** Frédéric Koriche, Louenas Bounia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpreting the predictions of complex black-box classifiers remains a central challenge in explainable artificial intelligence.
While local explanations clarify individual predictions, there is a significant need for global probabilistic explanations that capture a model's overall behavior across the input distribution.
Such an explanation is a small subset $K$ of features, whose relevance is measured by the expected probability, over a random input $\mathbf x$, that the classifier assigns the same label to $\mathbf x$ and to a random input agreeing with $\mathbf x$ on $K$.
In this study, we investigate the task of identifying maximally relevant global explanations under a cardinality constraint, focusing on product distributions with full support on discrete feature spaces.
We introduce a spectral explainer that leverages membership queries to the black-box classifier and employs Fourier-analytic, junta-learning methods to produce probably approximately correct (PAC) explanations.
Our algorithm is fixed-parameter tractable with respect to the explanation size limit, maximum feature cardinality, and desired accuracy.
Experiments on synthetic and real-world datasets confirm the theoretical guarantees and show that the spectral explainer outperforms a greedy baseline as the explanation size increases.

---


### 277. [CoHABIT: Complementary Evaluation of Furniture Layouts through Spatial Rules and Household Routines](https://arxiv.org/abs/2611.29494)

**<font color=#1a73e8>作者：</font>** Ewsey Obzherin, Samira Atlangirieva, Anastasia Antsiferova 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce CoHABIT, a framework for evaluating furniture layouts through complementary spatial rules and household routines. Static assessment captures geometric validity, ergonomic access, functional organization, and configurable design preferences, including Feng Shui. Dynamic assessment uses learned resident policies to simulate everyday activities, resource sharing, coordination, and individual burdens in multi-agent households. Controlled comparisons show how spatial criteria and household behavior reveal distinct aspects of layout quality, while resident profiles and scheduling influence furnishing rankings. Independent verification of household needs grounds dynamic comparisons in observed outcomes, enabling interpretable assessments of how furnished environments serve different households.

---


### 278. [GeoFusion: An Uncertain Machine Learning Framework for Sensor Fusion](https://arxiv.org/abs/2611.29510)

**<font color=#1a73e8>作者：</font>** Basant Ahmed Mounir Abdelhamid, Amr T. Abdel-Hamid  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High positioning precision is a critical requirement in many Global Positioning System (GPS) applications, yet achieving it with affordable smartphone sensors remains an open challenge. Existing approaches treat each GPS observation as an absolute point, discarding the uncertainty inherent in the measurement conditions and leaving the cooperative potential of multiple phones observing the same location untapped. In this work, we propose GeoFusion, a three-stage uncertain machine learning framework for cooperative sensor fusion. In the first stage, each GPS observation is modeled as an uncertain object using one of two proposed models: the volcano function, grounded in satellite geometry, and the empirically derived mountain function, built from the statistical structure of real smartphone data. In the second stage, uncertain objects are clustered by location event using partitional and graph-based algorithms. In the third stage, the cluster output is refined using filter-based and learning-based estimators. Experiments on the Google Smartphone Decimeter Challenge dataset show that uncertainty modeling is a primary driver of precision gains: the mountain function significantly outperforms the geometry-only volcano function, and uncertainty-aware UK-medoids significantly outperforms its certain counterpart, k-medoids. A post-clustering deep neural network further refines the cluster estimates, and the recommended configuration achieves a mean absolute error of 2.90 +/- 0.15 meters on held-out test drives, comparable to and on average below the best reported single-phone precision of approximately 3 meters, demonstrating the potential of cooperative uncertainty-aware fusion for affordable GPS sensors.

---


### 279. [STAGE: Structured Test-Time Adaptation with Global Entropic Soft-coupling for Cross-Subject Brain-to-Image Retrieval](https://arxiv.org/abs/2611.29538)

**<font color=#1a73e8>作者：</font>** Yihang Zou, Ruixi Liang, Chunmei Qing 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-subject brain-to-image retrieval aims to identify viewed images from unseen subjects' brain signals. However, inter-subject variability hinders alignment of brain-image representations, while independent query ranking tends to concentrate predictions on a few candidates, making accurate retrieval difficult without target labels. We propose STAGE (Structured Test-Time Adaptation with Global Entropic Soft-coupling), a structured test-time adaptation framework for recovering cross-subject alignment from uncertain brain-image correspondences. Moment calibration reduces statistical discrepancies between features, while coupling-weighted initialization establishes initial alignment. Coupling-guided adaptation further refines residual feature mismatches, and soft-coupling ranking coordinates candidate competition across queries to prevent overly concentrated matching assignments. Using only unlabeled target batches, STAGE maintains consistent matching from feature calibration to image retrieval while keeping both encoders frozen. Experiments on three public datasets validate STAGE's retrieval performance. On THINGS-EEG2, STAGE achieves 68.25% Top-1 and 90.47% Top-5, improving Top-1 by 18.52 percentage points over SCORE recovery and CSLS on identical frozen NICE features. Calibrated on 200 queries and a 200-image gallery covering their identities, STAGE retains 42.05% Top-1 when ranking 1,854 images with the transform frozen.

---


### 280. [Seeing vs. Knowing: Counterfactual Supervision and Correction for 3D-Aware Object Editing](https://arxiv.org/abs/2611.29542)

**<font color=#1a73e8>作者：</font>** Jian Zahng, Zhijun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rotating, translating, or rescaling an object in a photograph requires revealing unseen surfaces, preserving visible appearance, and updating shadows and reflections. Reconstructed 3D assets, rendered at the target pose as a 3D state, provide explicit geometric guidance, but their imperfect textures may conflict with the photograph, while standard paired training does not explicitly teach the editor which source to trust. To address this, we propose counterfactual state supervision, which constructs controlled photo--state conflicts through hidden-surface repainting, hidden geometry with re-rendered shadows and reflections, and visible-surface texture replacement. This teaches the editor to follow the 3D state for unseen content while preserving photograph-visible appearance. However, learning this distinction does not ensure that it is maintained during sampling. We therefore introduce symmetric counterfactual correction, which uses state-side and photo-side twins, which share the photograph and the state respectively, to construct directed latent perturbations toward condition-inconsistent targets and train recovery toward the target specified by the current condition. Both strategies operate only during training, requiring no architectural changes or additional inference steps. Experiments on OBJect and SpatialEdit-Bench demonstrate strong spatial editing performance and content preservation, while controlled ablations show improved source selection and sustained responsiveness to conditioning during sampling.

---


### 281. [Align the Pair, Not the Sample: Representation Alignment for Faster and Better One-Step Generato](https://arxiv.org/abs/2611.29547)

**<font color=#1a73e8>作者：</font>** Mingxiao Li, Xuantuo Huang, Encheng Su 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation alignment markedly accelerates diffusion training, but one-step generators raise a question that diffusion does not: \emph{which training path should receive the loss?} A one-step generator sees two kinds of inputs. Corrupted real images come with their clean counterpart, which provides an instance-paired target. Samples generated from pure noise have no corresponding real image, yet this is where the final model operates. We study this question on Priming, which trains one-step generators from scratch by reconstructing corrupted images and then matching feature distributions with optimal transport. Aligning the generative path, the natural choice, collapses recall ($0.45\!\to\!0.15$--$0.25$) in all 17 configurations we test, including five target constructions and loss weights down to $0.05$. Aligning the paired reconstruction path with a frozen DINOv2 encoder instead helps in every setting we test. A short analysis explains this asymmetry: when the target carries no instance information about the input, the optimal aligned feature is constant within each class, so the loss pulls samples toward class prototypes. A control confirms this: aligning the paired path to a random same-class image instead of the input's own image removes most of the gain. Inside the generator, paired-path alignment creates an interface block through which post-training routes noise, and the image semantics carried through it predict sample quality across 16 models. The resulting recipe, \method, accelerates \emph{both} training stages on ImageNet $256\!\times\!256$: it matches the 160-epoch baseline with $2\times$ fewer priming epochs, surpasses its final quality with $4\times$ fewer post-training updates, and lowers FID to 1.30 (B) and 1.155 (L) at the standard budget. A joint single-stage variant trains native one-step generators and reaches FID 1.22 with 115M parameters.

---


### 282. [CompareDR: Benchmarking Deep Research Reports from Individual Quality to Comparative Merit](https://arxiv.org/abs/2611.29549)

**<font color=#1a73e8>作者：</font>** Wanli Wu, He Zhu, Yue Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep research systems can produce reports with different evidence, analyses, and conclusions for the same query. A reader deciding which findings to rely on needs to know how well each report meets the task requirements and which differences matter to the answer. A score for a single report can summarize its quality, but it does not identify which contributions make one report more useful than another. We introduce CompareDR, a benchmark that combines task-specific pointwise audits with guideline-based pairwise comparisons. We use passage-linked report representations to locate relevant differences and selective evidence verification to check claims that could affect the judgment. The benchmark comprises 40 Chinese and English tasks from three existing benchmarks, 360 reports from nine systems, 1,099 human-reviewed evaluation criteria, and human preferences elicited through blinded comparisons of 80 report pairs. The hybrid evaluator matches 69 of these 80 preferences (86.25%, Cohen's $\kappa=0.746$). The benchmark supports both comparisons of research systems and examination of the evidence and analyses behind those judgments.

---


### 283. [Learning Acceptable Lotteries via Queries: Minimizing Aggregated Violation Distances](https://arxiv.org/abs/2611.29555)

**<font color=#1a73e8>作者：</font>** Nicholas Teh, Paul W. Goldberg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When deploying an AI system, a developer can randomize over several candidate versions, sending each request to a version chosen at random, to balance the requirements of multiple stakeholders. We study a setting in which each of $n$ stakeholders reveals only whether a proposed lottery over $m$ candidates is acceptable, and each stakeholder's acceptable lotteries lie on one side of an unknown hyperplane. While previous work sought a lottery that every stakeholder accepts, such a lottery need not exist when, for instance, safety and helpfulness requirements are in conflict. We therefore minimize a power mean of the stakeholders' violations; since binary answers reveal neither the size of a violation nor how to compare violations across stakeholders, we measure each violation by a normalized distance to the stakeholder's acceptance boundary. We characterize exactly when accept/reject answers determine these distances. When they do, $\mathcal{O}(nm\log(1/\varepsilon))$ queries suffice to learn them, where $\varepsilon$ is the precision of the utilities, and this bound is tight; when they do not, a natural worst-case approach is optimal up to a constant factor, even compared with methods that make unlimited queries. For limited query budgets, we give a sampling algorithm whose number of queries for a given accuracy does not depend on $n$, and show that a deterministic algorithm cannot guarantee a small loss without querying almost all stakeholders. Synthetic experiments illustrate the resulting tradeoff between querying many stakeholders and learning each of them accurately.

---


### 284. [Think Before You Forecast: Scaling Test-Time Compute for Time Series Forecasting](https://arxiv.org/abs/2611.29566)

**<font color=#1a73e8>作者：</font>** Daojun Liang, Xiao Hong, Pei Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time compute has become an important paradigm in computer vision and language modeling, where additional computation at inference time enables models to explore multiple candidate solutions and select or refine the most reliable one. However, time series forecasting models typically produce predictions through a single forward pass, leaving them vulnerable to distribution shifts and non-stationarity that frequently arise in real-world temporal data. We propose Time Test Compute for Time Series (TTC4TS), an architecture-agnostic framework that improves the predictive performance of frozen forecasting models at inference time. Given a pretrained backbone, the generator produces multiple candidate forecast trajectories using augmentation, retrieval, adapter. The synthesizer then selects or combines these candidates using aggregation, classification, or candidate-scoring and ranking methods to produce the final forecast. By increasing the number of candidates, TTC4TS scales test-time compute without retraining the forecasting backbone. Beyond improving point-forecast accuracy, TTC4TS can exploit candidate forecasts for uncertainty quantification, which supports improved interval forecasts. We also theoretically analyze when additional test-time computation improves forecasting. Experiments across diverse datasets and backbones demonstrate consistent gains in accuracy and calibration. Code is provided in this https URL.

---


### 285. [Scalar Tuned Lens Summaries Offer Limited Incremental Value for Mid-Generation Abstention](https://arxiv.org/abs/2611.29589)

**<font color=#1a73e8>作者：</font>** Khurram Khalil, Khaza Anuarul Hoque  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mid-generation abstention aims to stop an unpromising response before spending its remaining computation budget. Intermediate transformer states may help predict eventual correctness, but whether scalar summaries of their vocabulary predictions add useful evidence is less clear. We compare Tuned Lens entropy and divergence features with final-state and raw intermediate-state probes under matched, causal evaluation. Across eight instruction-tuned models on MATH-500, raw intermediate states improve ranking, whereas scalar-only probes usually trail the final-state baseline. Scalar hybrids have positive exceptions, but their advantage over position-matched permutation controls is small. Cross-fitted residual comparisons further show that gains over a final-state probe need not require aligned scalar features. Actual stopping runs on two model sizes and two benchmarks reveal a separate accuracy--computation trade-off, with token savings overstating wall-time savings for scalar policies. The evidence supports a restricted empirical conclusion about these scalar features, not a general negative claim about intermediate representations.

---


### 286. [Similarity-Constrained Reweighting for Complex Query Answering on Knowledge Graphs](https://arxiv.org/abs/2611.29596)

**<font color=#1a73e8>作者：</font>** Daniel Daza, Alberto Bernardi, Luca Costabello 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine learning models for Complex Query Answering (CQA) on knowledge graphs estimate the likelihood of answers that are not reachable via direct traversal. Recent work has proposed extending such queries with soft entity constraints, which require the target variable to be similar or dissimilar to specified sets of entities. We study a more general formulation where similarity constraints are specified on an arbitrary variable in a query, and introduce SCORE: a computationally efficient and interpretable method for incorporating similarity constraints on an arbitrary variable of a query. SCORE is based on a lightweight and interpretable score adjustment function that only requires tuning two hyperparameters on a validation set. Our experiments show that SCORE effectively incorporates preferences while maintaining strong query answering performance. It significantly improves ranking quality when constraints apply to the target variable and performs effectively in the more general case involving constraints on intermediate variables, and its performance remains robust when applied to several existing methods for CQA. Our implementation is available at this https URL.

---


### 287. [AEP:Towards Trustworthy Agent Communication, Networking, and Collaboration](https://arxiv.org/abs/2611.29598)

**<font color=#1a73e8>作者：</font>** Yuhao Wang, Shengfang Zhai, Xinyu Zhou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As privately owned agents become increasingly capable, collaboration in open agent networks is limited by partial topology knowledge, ownership boundaries, and the risk of exposing or contaminating private context. Existing agent-to-agent protocols are useful when collaborators are already known, while shared-memory and broadcast-based systems rely on visibility and trust assumptions that do not hold in decentralized, low-trust environments. We introduce Open Private Agent Collaboration (OPAC), an asset-centric paradigm for cooperation among private agents with open membership, partial observability, and ownership-aware access control. Rather than treating collaboration as the exchange of final responses, OPAC enables agents to selectively discover, exchange, audit, and integrate policy-controlled context assets. This shifts the unit of cooperation from transient messages to reusable external context, while keeping disclosure and integration subject to privacy and security constraints. We instantiate OPAC with the Agent Exchange Protocol (AEP), a decentralized framework that combines semantic discovery, demand-driven coordination, safety-gated asset exchange, and ledger-backed evidence derivation. By distinguishing physical topology from each agent's local cognitive topology, AEP allows agents to discover task-conditioned collaborators under an unknown network structure, release only admissible assets, and update future cooperation decisions from auditable interaction evidence. AEP therefore provides a middle ground between pure request-response interaction and globally shared memory, offering a practical foundation for trustworthy agent-native networking through selective, auditable reuse of distributed context assets.

---


### 288. [Aggregation Dispersion: An Information-Geometric Diagnostic of Oversmoothing in Graph Neural Networks](https://arxiv.org/abs/2611.29600)

**<font color=#1a73e8>作者：</font>** Abdessalam Ed-dib, Amine Mohamed Aboussalah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Message-passing neural networks (MPNNs) learn node representations by iteratively aggregating information from neighbors, but stacking too many layers causes all representations to converge, an effect known as oversmoothing. We propose a geometric perspective on this phenomenon. At each depth $k$, the propagation operator assigns to every node $v$ a walk distribution $p_v^{(k)}$, a probability distribution over source nodes. These walk distributions form a point cloud on the probability simplex, whose contraction to a single point characterizes complete mixing of the propagation operator, and thus oversmoothing. To measure this contraction, we use the Fisher-Rao metric, the unique Riemannian metric on the simplex invariant up to scale under sufficient statistics, whose scaled chordal distance under the square-root embedding $p \mapsto \sqrt{p}$ is the Hellinger distance. The resulting diagnostic, the aggregation dispersion $D_k$, is the variance of the embedded point cloud on the unit sphere. We prove that: (i) $D_k = 0$ if and only if the $k$-th step propagation matrix has rank one, a necessary and sufficient condition for complete operator mixing; (ii) $D_k$ is non-increasing with depth; (iii) the spectral gap of the propagation matrix controls the rate of this decay; and (iv) for contractive MPNNs, the aggregation dispersion upper-bounds the representation dispersion up to graph- and initialization-dependent constants. Across 14 model configurations and 11 datasets, $D_k$ attains the highest mean absolute Pearson correlation with test accuracy across depths among eight diagnostics ($|r| = 0.721$, using log-transformed diagnostic values), numerically comparable to the post-training effective rank ($|r| = 0.688$), while requiring no training.

---


### 289. [GravHMR: Coupling SLAM and Human Mesh Recovery in a Shared Gravity Frame](https://arxiv.org/abs/2611.29614)

**<font color=#1a73e8>作者：</font>** Hanglei Jin, Chenglu Sun, Junchen Ge 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering globally consistent 3D human motion from monocular videos remains challenging under dynamic camera motion. Although SLAM and human mesh recovery (HMR) provide complementary camera and body estimates, directly combining them often leads to inconsistent orientations and accumulated trajectory drift. We present GravHMR, a training-free, plug-and-play framework that couples SLAM and HMR through a shared gravity-aligned reference. By allowing gravity to be estimated independently of the HMR backbone, GravHMR accommodates world-grounded HMR models with or without explicit gravity-view representations. Specifically, Yaw-Aware Orientation Optimization (YAOO) resolves heading inconsistencies by correcting body and velocity orientations about the shared gravity axis. Conditioned on these corrected orientations, Gravity-Aware Trajectory Optimization (GATO) anchors root trajectories in the metric SLAM world by jointly leveraging 2D reprojection, the metric scale implicit in the human body, and the body's own motion. On EMDB-2, GravHMR achieves state-of-the-art performance with 154.0 mm W-MPJPE100 using ViPE and 189.8 mm using masked DROID-SLAM, outperforming TRAM (222.4 mm) under the same masked DROID-SLAM camera estimates. It further reduces W-MPJPE100 by 44.3% over GVHMR (276.5 mm) and by 20.0% over GVHMR + HTD-Refine (192.4 mm) with the same HMR backbone.

---


### 290. [Mass Forcing: On-Policy Mass-Aware Distillation for Autoregressive Video Generation](https://arxiv.org/abs/2611.29618)

**<font color=#1a73e8>作者：</font>** Yiyu Li, Fei Wei, Yong Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distribution Matching Distillation (DMD) has emerged as a promising paradigm for real-time video synthesis, distilling pretrained diffusion models into few-step autoregressive generators. However, its reverse-KL objective is mode-seeking and can collapse the student's conditional video distribution onto a narrow subset of modes, leading to reduced sample diversity, diminished temporal dynamics, and color oversaturation. Existing methods mitigate this issue mainly via coverage-oriented student initialization, but we observe that such coverage is transient: across three initializations, the fraction of dynamic videos drops sharply during subsequent DMD training, indicating that the mode-seeking objective, not the initialization, drives this degradation. We propose Mass Forcing, a probability-mass-aware framework that moves on-policy DMD supervision from whole videos to individual states. Each update branches several continuations from a shared student-generated prefix, making the student's probability mass at that state measurable against the teacher. First, Mass Forcing estimates relative teacher-to-student density ratios among these continuations through latent-space score integration and uses them to rebalance conditional DMD updates, amplifying rollouts underrepresented relative to the teacher. Second, since mismatched mode probabilities do not necessarily induce strong local score corrections, it aligns generated rollout sets with a reweighted reference distribution defined by the same mass estimates, providing cross-rollout supervision. Experiments on MovieGen and VBench show that Mass Forcing improves video fidelity and sustains temporal dynamics throughout training, achieving the highest Total scores among compared methods and a Dynamic Degree of 83% after 1,000 generator updates, versus 12-32% for the baselines, with no additional inference-time overhead.

---


### 291. [Contamination at the Operating Point: Train-Test Identity Overlap Inflates Low-FMR Face Recognition Accuracy by an Order of Magnitude](https://arxiv.org/abs/2611.29629)

**<font color=#1a73e8>作者：</font>** Fu Dai, Kamal Taha, Naoufel Werghi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face verification systems are deployed by selecting a decision threshold that achieves a target false match rate (FMR); performance is then reported as the corresponding false non-match rate (FNMR). In practice, deployed systems operate at FMR $\le 10^{-6}$, but widely used benchmarks can share identities with the models' training corpora. Prior work (Wu et al., 2024) measures the resulting optimistic bias as a small additive change in 10-fold accuracy (up to 1.01 percentage points). We show that the bias is neither small nor constant: it is a multiplicative error that grows as FMR falls. First, we audit train-test overlap with a detector calibrated against a null distribution (rather than a hand-tuned threshold). Relative to WebFace42M, we flag 88.6% of MS1MV3 identities and 14.3% of IJB-C subjects as present, despite WebFace260M's published de-overlap explicitly naming IJB-C. Manual review of 100 flagged IJB-C subjects confirms 69.2%, implying a residual overlap of roughly 9.9%. Second, holding the model fixed, removing only the contaminated identities from the test set increases FNMR by 3.6$\times$ at FMR=$10^{-4}$, 6.3$\times$ at FMR=$10^{-5}$, and 13.9$\times$ at FMR=$10^{-6}$, while a same-size random removal does not. The effect is traced to a shorter impostor tail that lowers the threshold. The magnitude of the shift depends on the training corpus and does not cancel betweent margin between our model and a publicbaseline by half. Third, we give the first direct measurement of the effective number of independent impostor comparisons in IJB-C: only 2.7 million effectively independent comparisons at FMR=$10^{-6}$, which is below all commonly accepted reporting rules. Finallyth a known training corpus, we build areal-face protocol with audited zero overlap that resolves FMR=$10^{-8}$.

---


### 292. [SuperFine3D: Efficient Global-Local Recursive Refinement for Extremely Detailed 3D Geometry Generation](https://arxiv.org/abs/2611.29630)

**<font color=#1a73e8>作者：</font>** Lihan Li, Junwei Zhou, Yu-wing Tai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution images contain rich visual details that require fine geometric structures for faithful 3D reconstruction. However, generating extremely detailed 3D geometry from images requires substantial computational resources and training data, making high-resolution geometry generation challenging for existing state-of-the-art models. In this paper, we present SuperFine3D, an efficient framework for generating extremely detailed 3D geometry through global-local recursive refinement. SuperFine3D learns a shared refinement operator from paired coarse-to-fine representations and recursively reuses it to progressively synthesize finer geometry beyond the training resolutions, without requiring additional paired supervision at target resolutions. To make recursive refinement computationally efficient, we introduce spatial-cell attention, which restricts high-resolution interactions to local spatial neighborhoods while maintaining bounded communication across neighboring cells. We further propose spatially anchored cross-scale guidance, which leverages globally contextualized coarse geometry to guide local detail synthesis and preserve structural consistency. In addition, geometry-aware training objectives encourage the refinement process to preserve stable geometric structures while introducing fine-grained surface details. Experiments demonstrate that SuperFine3D generates geometry at a $4096^3$ decoder-grid resolution, corresponding to a sparse $256^3$ latent lattice, using a shared refinement operator trained only on $512^3$--$1024^3$ representations. Compared with a full-attention recursive baseline, SuperFine3D achieves a $9.4\times$ speedup in end-to-end inference and reduces peak GPU memory usage by $23.0\%$, while improving cross-scale structural consistency and producing cleaner surfaces with finer geometric details.

---


### 293. [Immersive Video Effects Persist Beyond Exposure: From Psychological Closeness to Self-Initiated Behaviour in a Two-Week Comparison with 2D Video](https://arxiv.org/abs/2611.29647)

**<font color=#1a73e8>作者：</font>** Koichi Toida, Shinnosuke Furuya, Shimpei Miura 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Immersive Video (IV), a live-action stereoscopic 180-degree video format, has been shown to elicit a strong sense of Presence and enhance psychological closeness to individuals depicted in the video. However, whether these effects persist beyond exposure and are accompanied by subsequent self-initiated behaviour remains unclear. In this study, 84 participants were assigned to either an IV or a 2D video group, and psychological and behavioural outcomes were tracked over a two-week period. Psychological outcomes were assessed before and immediately after exposure and at approximately 3, 7, and 14 days post-exposure, while self-initiated behaviour was assessed during follow-up. Psychological closeness remained significantly higher in the IV group than in the 2D group for up to 7 days and remained elevated above baseline within the IV group at 14 days. Lasting-impression ratings were also significantly higher in the IV group throughout the follow-up period. Among participants who completed both scheduled follow-up assessments, 45.9% in the IV group met the operational criterion for early self-initiated engagement, compared with 13.2% in the 2D group. Furthermore, a higher proportion of participants in the IV group reported active or socially oriented behaviours. These findings suggest that IV can elicit psychological effects that persist beyond exposure and may encourage subsequent self-initiated engagement.

---


### 294. [How Seasonal Reference Choice Changes the Apparent Gains of Chronos Models in Electricity Load Forecasting](https://arxiv.org/abs/2611.29653)

**<font color=#1a73e8>作者：</font>** ChandraMohan K  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a forecasting model is said to beat a simple baseline, the size of that win depends on which baseline was used. We measure how much this matters for two zero-shot foundation models, Chronos-Bolt and Chronos-2, on hourly electricity load. The study uses 60 fixed cases drawn from eight series in four public collections, with forecasts 24 and 168 hours ahead and up to 2,048 hours of history. Each model is compared with daily persistence, weekly persistence, a weekday hybrid, a daily-weekly blend, and a reference chosen from these on a validation period. We keep every origin-level forecast and estimate uncertainty with paired circular block bootstrap intervals using 168- and 336-hour blocks. A week ahead, Bolt clearly beats weekly persistence in 21 of 30 cases but the validation-selected reference in only 14, and its median gain falls from 17.3% to 11.9%. For Chronos-2 the clear-win counts are 18 and 15. Chronos-2 has lower week-ahead MAE than Bolt in 24 cases, yet only 12 of those differences are clear. The selected reference is not always the harder baseline, since on some test windows it does worse than weekly persistence. The choice of baseline therefore changes both how large the reported gain is and how sure we can be of it. The results are exploratory: the series and windows are related, an earlier pilot was inspected, pretraining overlap cannot be ruled out, and the case-level intervals are not corrected for multiple comparisons.

---


### 295. [One Checkpoint, Four Converters: Per Input Disagreement After On Device Conversion and a Probe Set That Catches It](https://arxiv.org/abs/2611.29661)

**<font color=#1a73e8>作者：</font>** Sharven Rane  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A model converted for on device or accelerated inference ships once its top 1 accuracy matches the source model. Accuracy can match while individual decisions change, and the converter, its INT8 recipe and its calibration draw each move them. We convert 5 public checkpoints (four ImageNet classifiers and a sentiment model) with the documented FP32 and INT8 recipes of ExecuTorch, LiteRT, ONNX Runtime and TensorRT and compare every top 1 decision with the PyTorch source on 7,854 images and 1,938 sentences. All 34 strict FP32 conversions reproduce every decision, yet each of the 4 vision INT8 recipes that keeps accuracy equivalent flips more than 1% of decisions: ONNX Runtime static INT8 flips 4.07% (95% CI [3.65, 4.53]) of ResNet 50 decisions while accuracy moves by -0.15 points, and two builds of that recipe from different calibration draws disagree on 3.44% [3.06, 3.88]. Where accuracy is kept, the flipped inputs are the ones the source model barely decides (AUROC of the source margin 0.90 to 0.97 on ResNet 50, every 95% CI inside [0.89, 0.98]), but our preregistered claim that this holds for every recipe fails on the two mobile networks, where INT8 breaks accuracy outright. A probe set of the 200 training inputs with the smallest source margin, chosen before any conversion, flags all 40 vision stacks (recall 95% CI [0.91, 1.00]) and all 6 text stacks that flip at least 0.5% of decisions and none of the exact FP32 conversions, so conversion checks should compare decisions on such a probe set, not accuracy.

---


### 296. [PROPS: Can Visual Generators Keep the Current Look of a Prop?](https://arxiv.org/abs/2611.29665)

**<font color=#1a73e8>作者：</font>** Xiangzhao Hao, Dianyi Wang, Keyan Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many generation tasks draw the next image from a visual history, such as storyboards, illustrated stories and multi-turn editing. A new request often states what happens next without restating how earlier objects look. Instead of recovering an object's current look from the history, generators often redraw it from the request alone or bring back an outdated look, and the error can carry into later steps. We call this failure prop drift. Existing evaluations rarely isolate it, because similarity to the history rewards copying and a judge that sees a single history cannot tell a look recovered from that history from one the generator happens to prefer. We introduce PROPS, a benchmark of 2,257 pairs of twin histories that end on the same request but show one prop in two different looks. A pair passes only if the generator draws the matching look on each side and carries out the request, so a look preferred by the generator or the judge passes at most one side. All 34 open and closed systems we test show prop drift, and even systems that carry out the requested action on most sides often lose the current look of the prop. Swapping the planners and editors of agents further shows that both history understanding and image generation limit agent performance. We also build PROPS-Train, 80,250 training chains in four tracks whose targets recover an earlier state or carry scripted changes forward, and fine-tuning on it clearly improves all four tested models. Both datasets will be publicly released.

---


### 297. [DeclareViT: Decoupling Early Classification from Feature Refinement with Exit Query for Efficient ViTs](https://arxiv.org/abs/2611.29674)

**<font color=#1a73e8>作者：</font>** Xinrui Gong, Yao Rong, Chuangtao Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers achieve remarkable recognition performance but incur substantial computational cost during inference, limiting their use in latency- and compute-constrained deployment scenarios. Early-exit inference offers a promising solution by allowing easy samples to terminate at intermediate layers. However, existing approaches typically couple early classification with the shared backbone, requiring intermediate representations to support both early classification and subsequent feature refinement. Under joint training, the corresponding optimization objectives jointly update shared backbone parameters, which can lead to conflicting gradient directions. Motivated by this observation, we introduce DeclareViT, a framework that decouples early classification from feature refinement. Each exit uses a dedicated query to read intermediate features through one-way cross-attention without modifying the backbone token stream. The query branches are optimized for early classification while the backbone and final classifier remain frozen. Across ViT, DeiT, and Swin on CIFAR-100, ImageNet-1K, and Food-101, DeclareViT consistently establishes a state-of-the-art accuracy-efficiency trade-off: It achieves 1.58 times to 2.57 times multiply-accumulate (MAC)-based speed-up with only a 0.39-1.91 percentage-point accuracy drop. Wall-clock measurements on CPU and GPU further demonstrate practical inference acceleration. Code is available at this https URL.

---


### 298. [CrysLDM: Latent Diffusion Model for Crystal Material Generation](https://arxiv.org/abs/2611.29675)

**<font color=#1a73e8>作者：</font>** Subhojyoti Khastagir, Kishalay Das, Pawan Goyal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating new crystal materials with desirable chemical properties has long been a challenging task. Existing diffusion models operate in feature space, requiring complex diffusion architectures to model the joint distribution of atom types, coordinates, and lattice structures. This complexity increases the number of diffusion steps, leading to higher training and sampling costs. In this work, we aim to generate novel crystal materials within a time- and resource-constrained setup, where existing models are not well-suited. To address this, we propose CrysLDM, a novel latent diffusion model for 3D crystal materials, which integrates a variational autoencoder and a diffusion model. The VAE encoder maps 3D crystal structures into a latent space, where the diffusion model operates. Since CrysLDM leverages a smooth, lower-dimensional latent space, it simplifies the generative process and accelerates both training and inference. Through extensive experiments on benchmark datasets and tasks, we show that CrysLDM generates stable and valid materials with quality comparable to state-of-the-art methods, while being significantly more efficient in terms of computational resources and time.

---


### 299. [Ref2Light: From One Image to Interactive Glasses-Free 3D Characters](https://arxiv.org/abs/2611.29678)

**<font color=#1a73e8>作者：</font>** Hanzhong Zhang, Haoyang Wang, Siyang Song  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Animating character illustrations on light-field displays demands coherent binocular parallax, real-time pose articulation, and fine-grained expression control. However, existing 2D animation and 3D reconstruction pipelines cannot combine these with rapid character switching. We present Ref2Light, a feed-forward framework that maps a single A-pose illustration and continuous pose and expression controls to display-native light-field animation, without per-character 3D reconstruction, rigging, or test-time optimization. Our key insight is to decompose light-field synthesis into static identity, view-dependent parallax, and control-driven articulation. A shared encoder caches multi-scale identity features once per character for rapid switching. A conditional decoder then synthesizes ordered angular anchors from these features via backward texture transport and direct color synthesis. A global-local control scheme deforms the anchors with head-body controls and uses the updated correspondence fields to track facial regions across views for masked local facial refinement. Finally, calibrated differentiable subpixel interlacing converts the anchors into the native panel raster, enabling end-to-end native supervision without rendering all views at full resolution. On held-out VRoid identities, Ref2Light reduces head-body LPIPS by 20.1%-55.6% over 2D and 3D baselines and lowers non-target change MAE in mouth closure by 95.6%-96.5% versus monolithic decoding, while running at 34.0-40.1 FPS for 1440x2560 native rasters on a consumer GPU. Code and demo are in the Supplementary Material.

---


### 300. [MERIT: Experience-Guided Memory for Long-Horizon Persona-Specific Persuasive Dialogue](https://arxiv.org/abs/2611.29679)

**<font color=#1a73e8>作者：</font>** Rohan Kirti, Akash Ghosh, Pratik Amrit 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective long-horizon persuasion in recurring goal-oriented settings requires more than factual memory: it must track how a user's trust, negotiation behavior, and strategic receptiveness evolve across interactions. Existing persuasive dialogue systems are largely single-session, static, and unimodal, while cross-session memory systems, though temporally aware, retain only factual content and overlook persuasion-specific dynamics. We propose MERIT (Memory-augmented Experience-Rationale for Iterative Temporal persuasion), which pairs a graph-based memory of four persuasion-specific memory types with a per-persona experience rationale library that records which strategies succeed for each user and why. Together they enable adaptive persuasion through prompt composition alone, with no parameter updates. To support this setting, we introduce PERSIST (PERSona-driven InSurance Interactions over Time), a dataset of 60 curated personas spanning 10+ years of motor insurance renewal interactions, with probabilistic life events that shift negotiation behavior and receptiveness across sessions, verified through strict human-in-the-loop annotation. MERIT surpasses memory and experience-based baselines on every metric across two policy backbones, reaching persuasive-appeal scores of 4.10 and 4.74 (out of 5).

---


> [!TIP]
> 当前位于：**251-300**（第 6/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-569](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
