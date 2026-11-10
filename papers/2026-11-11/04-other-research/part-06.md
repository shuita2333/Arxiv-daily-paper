# 📦 其他研究 | 2026年11月11日

> 本类共 **520** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-520](./part-11.md)

---

### 251. [TEAM: Topology-Aware, Semantic-Sensitive, General Transformer for Multimodal-Attributed Graphs](https://arxiv.org/abs/2611.11189)

**<font color=#1a73e8>作者：</font>** Yushuo Li, Xunkai Li, Zhengyu Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal-Attributed Graphs (MAGs) organize heterogeneous data in graphs whose nodes are characterized by modalities such as text and images rather than traditional unimodal attributes. However, many representative MAG methods organize propagation around node-level states and topology-defined neighborhoods, which can obscure fine-grained modality contributions: a bounded neighborhood may contain semantically weak evidence, while compatible context need not be confined to it. To address both limitations, we propose TEAM, a modality-centric framework that constructs and encodes graph context with node-modality tokens rather than treating each node as a single interaction unit. Concretely, TEAM unfolds the local topology into a Modality Encoding Tree and performs tree-anchored semantic evidence acquisition, organizing local structural context while expanding the accessible evidence space outside the constructed local Tree. We further introduce the Modality-Source Context Transformer (MSCT), which encodes the selected node-modality tokens and coordinates interactions among modality-source groups. By retaining textual and visual attributes as separate interaction units until readout, it supports fine-grained cross-node cross-modal exchange without first collapsing them into whole-node features. Across the evaluated baselines, TEAM attains the highest reported mean on all graph-learning metrics, all three G2Text metrics, and both G2Image metrics. On Toys, it surpasses the strongest baseline by 3.37 and 2.93 percentage points in Accuracy and Macro-F1, respectively.

---


### 252. [Source-Anchored Visual Autoregression for Extreme Image Compression](https://arxiv.org/abs/2611.11200)

**<font color=#1a73e8>作者：</font>** Bingxin Wang, Yuan Lan, Yang Xiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the extreme-low bitrate range below $0.01$ bpp, image compression becomes a constrained generation problem: the reconstruction depends on inferring plausible missing details while staying close to the input image. Autoregressive token models provide an efficient coarse-to-fine prior for this setting, but the transmitted early-scale tokens often leave object identity and texture underdetermined, which can lead to source-inconsistent reconstructions. We introduce Source-Anchored Visual Autoregression (SAVAR), a generative codec built on Visual Autoregressive (VAR) modeling. SAVAR transmits early-scale tokens and a compact caption. The tokens provide image-specific layout information, while the caption supplies global semantics. SAVAR reconstructs a partial VQ-VAE latent from the retained scales, maps it to the start-of-sequence initialization, and uses the same latent to condition the caption embedding before adaptive layer normalization, separating two roles that are typically driven by a shared condition in VAR-style generation. On the Kodak and CLIC2020 datasets in the extreme-low range, SAVAR reduces perceptual distortion relative to matched ARPC retained-scale operating points, lowering LPIPS by about $8$--$9\%$ and DISTS by up to $22\%$ at a lower bpp. It reconstructs a $512 \times 512$ image in about $218$ ms on one NVIDIA L20X GPU, retaining fast autoregressive decoding in the evaluated setting.

---


### 253. [DynOLAT: OLAT Video Prediction for Controllable Dynamic Full-Body Relighting](https://arxiv.org/abs/2611.11210)

**<font color=#1a73e8>作者：</font>** Taoming Liu, Yinji ShenTu, Guangzhao He 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate lighting response is essential for realistic dynamic human relighting, because shadows, highlights, and color changes should follow the target illumination in both direction and relative strength. Current learning-based relighting methods can generate visually plausible videos, but they often exhibit imprecise lighting responses: shadows and highlights may drift away from the target direction, and the output brightness may not faithfully follow the relative intensities in the target environment, making the result closer to appearance harmonization than controllable relighting. To address this issue, we propose DynOLAT, a generalizable OLAT video prediction framework for dynamic full-body humans. Instead of directly synthesizing a single relit appearance, our method predicts temporally consistent One-Light-At-a-Time (OLAT) basis videos from flat-lit inputs, and then linearly combines the predicted bases according to the target environment map. This OLAT-based formulation makes the directional response explicit in the predicted bases, while the relative lighting strength is determined by the linear weights derived from the environment map. We further introduce a dynamic capture pipeline and the first large-scale dynamic full-body OLAT dataset, comprising over 24 million frames from 224 identity-outfit combinations, where different outfits of the same person define separate combinations. Experiments show that DynOLAT responds more faithfully to variations in target lighting direction and relative intensity than the tested baselines, enabling controllable video relighting while preserving fine appearance details and temporal coherence. The dataset and processing tools will be publicly released to foster future research.

---


### 254. [Disentangling Where and When:Factored Spatio-Temporal Explanations for Video Action Recognition](https://arxiv.org/abs/2611.11214)

**<font color=#1a73e8>作者：</font>** Bhavan Vasu, Giuseppe Raffa, Prasad Tadepalli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-hoc explanation methods for video action recognition typically conflate spatial appearance and temporal dynamics into a single saliency or importance map. We propose a perturbation-based framework that disentangles these contributions into a spatial appearance mask ($M_a$) and a temporal motion mask ($M_m$). The two masks are jointly optimized against a frozen action recognition model through factored perturbation architecture, with nearest frame replacement to identify important temporal dynamics. A separation penalty discourages the appearance mask from spending budget on frames that the motion mask has already discarded. A ReLU-based area constraint penalizes explanations larger than an assigned budget. To evaluate these explanations, we introduce a separation protocol that sweeps spatial pixels and temporal frames independently, backed by proofs characterizing the proposed method. Across EPIC-Kitchens-55, EGTEA Gaze+, and Something-Something V2, our method attains the lowest deletion AUC against leading baselines while producing masks roughly five times sparser.

---


### 255. [scBIG++: Learning Across Genes and Cells to Predict Single-Cell Perturbation Responses](https://arxiv.org/abs/2611.11217)

**<font color=#1a73e8>作者：</font>** Jiafa Ruan, Zican Qiao, Zongxin Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting single-cell transcriptional responses to genetic and chemical interventions supports gene-function discovery and regulatory analysis. Existing studies often focus only on highly variable genes, restricting the expression changes available for downstream analysis. Cells exposed to the same intervention can also show heterogeneous expression responses, with coordinated gene programs active to different degrees. We propose scBIG++, a full-gene perturbation prediction framework that models this heterogeneity by connecting expression-adaptive gene modules with population-conditioned generation. To preserve shared gene structure while accommodating cellular variation, Gene-Relation Clustering organizes genes into common windows, within which Dynamic SoftSub learns expression-dependent submodule memberships. This shared organization enables Set-GCAE to exchange information about corresponding gene groups across control cells, placing individual representations in their source-population context. The cell representations initialize a latent flow, while their pooled summary and the perturbation representation condition response generation. Generated states are decoded into expression profiles covering all assayed protein-coding genes retained after preprocessing, supporting comprehensive analysis of perturbation-induced expression changes. Experiments across six genetic and chemical settings spanning 6,539--19,451 genes demonstrate competitive perturbation-effect recovery and full-gene expression reconstruction under unseen targets and combinations, cross-cell-line transfer, and held-out compounds. Our implementation is available at this https URL.

---


### 256. [EbbFlow: PINN-Inspired Progressive Curriculum for MeanFlow Training](https://arxiv.org/abs/2611.11220)

**<font color=#1a73e8>作者：</font>** Mengfan Yuan, Xunheng Kuang, Jianbin Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> MeanFlow learns interval-average velocity for few-step generation, but its fixed temporal sampler mixes diagonal and interior supervision throughout training. We interpret temporal coordinates as collocation points: diagonal samples provide a stochastic boundary target, whereas finite intervals supply a differential-consistency target. The diagonal fraction controls how often the consistency component appears, while interval length enters its gradient through an explicit factor. Motivated by this distinction, EbbFlow uses Temporal Supervision Allocation (TSA) to schedule the diagonal fraction and interval geometry. It starts with diagonal supervision, then admits interior samples and expands their maximum interval; a left-anchored interval law preserves coverage across time. The per-sample loss, target, backbone, and inference procedure remain unchanged. In matched class-conditional ImageNet $256\times 256$ runs without classifier-free guidance (DiT-B/2, one training seed per method, 400k updates), EbbFlow achieves 50k-sample FID of 39.65 at one network evaluation and 36.02 at two-evaluation ODE sampling, versus 44.82 and 39.86 for MeanFlow. Gradient probes show a mid-training difference in component geometry. Ablations support allocation scheduling and left-anchored intervals, although a fixed full-horizon variant performs better at one evaluation. These results suggest that temporal sampling is a useful training control whose benefits depend on the inference protocol.

---


### 257. [Do Feature Interactions Break Explainability? Provable Explanations for Any-Order Neural Additive Models](https://arxiv.org/abs/2611.11224)

**<font color=#1a73e8>作者：</font>** Idan Refaeli, Yizhak Yisrael Elboher, Guy Katz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc explanation methods for neural networks are often heuristic and lack provable guarantees. A common alternative to such methods that was studied in recent years is to compute a cardinally-minimal subset of input features that is provably sufficient to determine the model's prediction. For general neural networks, however, finding such explanations is computationally intractable. In contrast, recent work showed that this problem becomes more tractable for a particular family of neural networks, namely neural additive models (NAMs), though standard NAMs are highly restrictive because they exclude feature interactions altogether. In this work, we study the computation of provably minimal and sufficient explanations for neural networks with restricted feature interactions, bridging the gap between fully general neural networks and purely additive models. We first prove that even with constant-order interactions, the problem is $\Sigma_2^P$-hard, implying that worst-case exponential complexity is unavoidable. We then identify two provably tractable settings: one based on sparsity in the interaction structure and another based on a stronger interaction-aware notion of sufficiency. Under either of these settings, we develop algorithms that compute provable explanations for neural networks with any-order interactions while retaining much of the computational efficiency of additive models. Empirically, we show that these explanations are significantly smaller and faster to obtain than those produced by standard algorithms, while being derived from models that achieve much higher accuracy than standard NAMs. Overall, our results help expand the class of neural networks that admit efficient provable explanations, while clarifying the fundamental role of feature interactions in shaping their complexity.

---


### 258. [MCSA: Multi-Cutoff Spectral Aggregation in SO(3) Equivariant GNNs for Interatomic Potentials](https://arxiv.org/abs/2611.11226)

**<font color=#1a73e8>作者：</font>** Junfu Tan, Mengfan Wu, Yu Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine Learning Interatomic Potentials (MLIPs) based on Equivariant Graph Neural Networks (EGNNs) have achieved remarkable progress in atomistic modeling. However, accurately representing atomic interactions across different spatial scales remains challenging. In this work, we investigate the radial spectral properties of SO(3)-equivariant message passing and establish that the cutoff radius controls the characteristic spatial-frequency scale of radial interactions. Based on this analysis, we propose Multi-Cutoff Spectral Aggregation (MCSA), a plug-and-play module that aggregates radial kernels with different cutoff radii to enrich multi-scale geometric representations. To achieve efficient implementation, we exploit the compact support of radial kernels to fuse cutoff-dependent radial weights before angular tensor-product operations, avoiding redundant angular computations while preserving rotational equivariance. Extensive experiments across representative EGNN backbones demonstrate consistent improvements in energy, force, and stress prediction, as well as enhanced accuracy in higher-order properties, including phonon dispersion and lattice thermal conductivity. Further evaluations on layered materials with distinct interaction scales demonstrate the effectiveness of physically motivated cutoff selection. Code is available at: this https URL.

---


### 259. [Understanding When and Where Self-Supervised Speech Models Learn Phonemes and Prosodic Cues through Layer-Wise and Time-Resolved Probing](https://arxiv.org/abs/2611.11249)

**<font color=#1a73e8>作者：</font>** Masaru Tanibata, Shun Takahashi, Hiroki Ouchi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-supervised speech models (S3Ms) encode a rich hierarchy of acoustic, prosodic, and phonetic information, yet when and where it emerges during pretraining remains unclear. We train frozen-encoder probes on every Transformer layer across pretraining checkpoints of two matched models: HuBERT-Base, whose stage 2 is a separately initialized model trained on new pseudo-label targets, and single-objective wav2vec 2.0-Base. Our five tasks span an acoustic-to-abstract gradient: absolute pitch (F0), speaker-relative pitch, lexical stress, phoneme boundaries, and 38-way phoneme identity. Acoustic-prosodic cues and phone boundaries are decodable from the earliest checkpoints and barely shift across layers, whereas phoneme identity is constructed during pretraining, re-localizing to upper-middle layers under HuBERT's stage-2 targets at a matched update count. Acquisition order therefore tracks abstraction from the acoustic surface, not the segmental/suprasegmental distinction, extending to prosody an account established for phonetic, lexical and syntactic structure; the no-switch wav2vec 2.0 shows no comparable re-localization.

---


### 260. [ALETHEIA: A Multi-Frequency Eddy Current Pulsed Thermography Dataset for Neural Operator Learning in Nondestructive Testing](https://arxiv.org/abs/2611.11252)

**<font color=#1a73e8>作者：</font>** Changbin Sun, Jie Xiao, Xiaotian Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning neural solvers for spatiotemporal partial differential equations (PDEs) under real-world constraints remains a key challenge in scientific machine learning, especially for inverse tasks with sparse and noisy boundary observations. We present the Aletheia dataset, the first 3D benchmark for learning data-driven solvers in the context of nondestructive testing (NDT). The dataset simulates eddy-current-induced heating in conductive solids and models the resulting transient heat propagation governed by the heat equation. Aletheia contains over 4,700 high-resolution samples across 10 excitation frequencies (1-100,kHz), each providing volumetric heat source and temperature fields over time. It supports both forward prediction of temperature evolution and inverse reconstruction of internal heat sources or defects from surface infrared measurements. Real infrared thermography data from cracked rail specimens are included for calibration and comparison. We define four canonical tasks on both regular and irregular grids and benchmark them using various neural operators. Aletheia establishes a unified platform for evaluating neural PDE solvers under realistic NDT conditions, enabling progress in reliable, data-driven inverse modeling. The dataset and code are publicly available at this https URL.

---


### 261. [Auto-GlaKG: Automated Biomarker Reasoning for Explainable Glaucoma Detection](https://arxiv.org/abs/2611.11258)

**<font color=#1a73e8>作者：</font>** Cheng Huang, Zeyu Han, Yian Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interpretable glaucoma detection requires a transparent connection between fundus images, clinically meaningful biomarkers, and diagnostic predictions. Knowledge graph (KG) reasoning provides this structure, but performance measured using annotated biomarkers does not establish performance when only images are available. We present Auto-GlaKG, an automated framework that combines image-based biomarker prediction with fixed clinical-prior rules. A ResNet50 network predicts the cup-to-disc ratio (CDR) and six morphological signs using biomarker supervision, and a KG reasoner aggregates their signed rule contributions into a glaucoma score. On 689 fundus images evaluated using stratified, group-aware five-fold cross-validation, Auto-GlaKG achieves a pooled area under the receiver operating characteristic curve (AUC) of 0.951 (95\% confidence interval: 0.931--0.969), with sensitivity of 0.970 and specificity of 0.779. The matched image classifier also achieves an AUC of 0.951, while the rule stage adds 0.2~ms per image. Replacing predicted CDR with its annotation increases fold-mean AUC from 0.953 to 0.995. The framework provides an explicit rule-level account of image-based predictions and identifies CDR estimation as a priority for validation using independently measured biomarkers.

---


### 262. [Beyond Node Attributes: A Controlled Evaluation and Ablation of Local Interaction Statistics for Ethereum Phishing Detection](https://arxiv.org/abs/2611.11263)

**<font color=#1a73e8>作者：</font>** Thanh Dat Tran, Duy Loi Duong, Duy Luu Hoang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Methods for detecting phishing accounts on Ethereum are usually evaluated as complete pipelines that differ in features, architecture, and training protocol, which makes the contribution of interaction information hard to isolate. This paper evaluates the Unlabeled Feature Extension (UFE), a block of 12 local interaction statistics computed from each account's incoming and outgoing call and transfer edges without reading class labels. UFE is appended to the 14 source features of HEIG-Phish and tested with six model families: Logistic Regression, Random Forest, LightGBM, Graph Attention Network, GraphSAGE, and Meta-IFD. Within each pair of Baseline and Plus variants, the data partition, model configuration, random seed, decision threshold, and sampled neighborhoods are identical; only the input feature block changes. Across 20 predetermined stratified partitions of the same 2,763 labeled externally owned accounts, UFE increased test Macro-F1 by 1.0 to 9.1 percentage points across the six models. Every pair improved on all 20 partitions, all Nadeau-Bengio corrected 95% confidence intervals lie above zero, and the false-positive rate decreased for all six models. An exact-edge Random Forest ablation over 10 predetermined partitions associates most of the gain with the incoming transfer-edge sum attribute; once this feature is present, an incremental contribution of the remaining 11 UFE columns was not established. The results support reporting feature-augmented baselines alongside graph models, but they show stability under re-partitioning of one static, transductive benchmark rather than temporal or cross-dataset generalization.

---


### 263. [DuSS-PET: Self-Supervised Low-Dose PET Reconstruction Using Pseudo-Dual-Domain Consistency Without Paired Data](https://arxiv.org/abs/2611.11265)

**<font color=#1a73e8>作者：</font>** Shuijin Lin, Yuzhu He, Yongbo Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Positron emission tomography (PET) is pivotal in medicine and healthcare, but requires high radiation doses for quality imaging. Although deep learning has shown promise for low-dose PET reconstruction/enhancement, existing methods primarily rely on fully supervised learning, which requires paired low- and full-dose scans that are clinically impractical to obtain. To overcome this fundamental limitation, we propose DuSS-PET, a novel self-supervised PET reconstruction framework that operates without any paired low- and full-dose data. Our method is built upon a computational Noisier2Noise (Nr2N) paradigm, featuring a Bernoulli corruption strategy that serves as an image-space approximation to emulate low-count noise patterns in image-derived pseudo-sinogram representations. The DuSS-PET framework integrates three core components: an adaptive Swin transformer for pseudo-sinogram restoration, a plug-and-play module for image enhancement, and a consistency-constrained SSL strategy that enforces agreement between the pseudo-sinogram and image representations. Extensive experiments on multi-center datasets demonstrate that DuSS-PET achieves superior reconstruction performance, outperforming state-of-the-art SSL methods and achieving comparable or even better results than fully supervised approaches across various dose levels. In particular, it exhibits exceptional generalization across different scanner vendors. This work is among the first self-supervised low-dose PET reconstruction framework that enforces consistency between reconstructed images and pseudo-sinograms, where the pseudo-sinogram generated in the image space serves as a solid computational consistency constraint for enhanced imaging without full-dose training scans. The source code will be publicly available at this https URL.

---


### 264. [BiRefNet-V2: Rethinking Bilateral Reference for High-Resolution Dichotomous Image Segmentation](https://arxiv.org/abs/2611.11272)

**<font color=#1a73e8>作者：</font>** Peng Zheng, Deng-Ping Fan, Binglu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dichotomous image segmentation requires pixel-accurate foreground-background separation while preserving fine structures such as thin filaments, sharp edges, and intricate textures. BiRefNet addressed this challenge through bilateral references, combining image patches and gradient information, but its inward reference loses local spatial structure and lacks semantic guidance, while its outward reference relies on single-channel gradient attention. We recast this paradigm as controlled information recovery - locality determines what spatial information survives, semantic selectivity what information enters, and focused boundary supervision where refinement occurs - and propose BiRefNet-V2 to implement it: (1) locality-preserving and semantically guided detail injection through space-to-depth transformation, overlapping patches, and a Semantically Guided Gate; (2) a learned boundary stream with focused supervision that generates full-channel residual attention without requiring boundary annotations; and (3) a dual-branch decoder integrating depth-wise boundary convolutions with large-kernel attention. A modernized framework - LayerNorm, GELU, the Lion optimizer, and a DINOv3 backbone - cuts training from 600 to 50 epochs. Extensive experiments demonstrate state-of-the-art performance on DIS5K, camouflaged object detection, and high-resolution salient object detection across all 13 evaluation sets. Code is available at this https URL.

---


### 265. [A Unified Framework for License Plate Identification and Character-Recognition](https://arxiv.org/abs/2611.11289)

**<font color=#1a73e8>作者：</font>** Saurabh Kumar, Dewant Katare, Prakriti Jain  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a unified framework for license plate detection and character recognition on low-power edge hardware. The proposed network uses a shared CSP-Darknet and PANet feature encoder with an anchor-free localization head and a RoIAlign-based sequence-recognition branch. Character decoding is performed directly on aligned feature maps, avoiding image-space plate cropping and a second recognition backbone. The model is trained on an AI-assisted dataset of approximately 37,000 manually verified images covering license plate layouts from all 50 United States. The dataset includes variations in illumination, viewpoint, weather, blur, occlusion, and plate design. The framework is converted to an INT8 TensorRT engine and evaluated on an NVIDIA Jetson Orin Nano with 8 GB memory. The INT8 model shows an mAP50 of 97.8% and a full-sequence accuracy of 90.7%. It records 147 FPS at 6.8 ms end-to-end latency, with 315 MB inference memory and 9.4 W average power consumption. Relative to the YOLOv8s+CRNN baseline, the proposed deployment provides a 7.1x throughput increase and a 77.8% reduction in allocated inference memory

---


### 266. [TransArt3D: From Two States to Articulated 3D Reconstruction with Video Transition Priors](https://arxiv.org/abs/2611.11304)

**<font color=#1a73e8>作者：</font>** Chenhao Guan, Liying Yang, Xinxing Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing interactable articulated assets from a few images is key to robotics and simulation, yet highly underconstrained. Existing optimization-based methods fit an articulated asset under a static 3D prior that scores each state independently, so per-state reconstruction errors leak into the estimated moving part and joint as false motion. Video diffusion models capture how objects move between states, but only implicitly in 2D. To this end, we present TransArt3D, an optimization-based framework that reconstructs an articulated 3D asset from two endpoint images by translating this video transition prior into explicit part structure and joint kinematics. It first lifts frames generated between the endpoints with a transition-coupled 3D consensus that applies the static 3D prior jointly across frames, stabilizing unchanging regions and initializing the parts and joint. A rectified-flow kinematic refinement then lets the video prior supervise a 3D motion field over the whole transition, while part assignment and a shared joint constrain the field throughout optimization, keeping per-state errors out of the articulation. Finally, a motion-aware canonical appearance fusion uses the recovered articulation to map both endpoint images onto one canonical surface, texturing regions that only one state reveals. On PartNet-Mobility, TransArt3D outperforms methods given the same two endpoints in geometry and joint accuracy, and surpasses methods given six observed states in articulated-state geometry, joint localization and appearance.

---


### 267. [Shape-Adaptive Subspace-Constrained Quadratic Matrix Factorization](https://arxiv.org/abs/2611.11313)

**<font color=#1a73e8>作者：</font>** Zheng Zhai, Zhuan Liang, Sujun Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quadratic manifold fitting provides a flexible framework for modeling nonlinear low-dimensional structures embedded in high-dimensional spaces. However, existing methods typically employ prescribed noise models or fixed loss functions, limiting their adaptability to varying noise characteristics. To address this limitation, we propose an alternating maximum likelihood estimation method for subspace-constrained quadratic matrix factorization, termed AMLE-SQMF, which jointly estimates the quadratic manifold and the underlying noise distribution. Specifically, we model the residuals using a generalized Gaussian distribution (GGD), whose shape parameter controls the tail behavior and determines the associated fitting loss. By exploiting the closed-form maximum likelihood estimator of the scale parameter, we eliminate the scale variable and derive a profile negative log-likelihood. Based on this formulation, we develop an alternating optimization algorithm that iteratively updates the manifold parameters and estimates the noise shape parameter. This enables adaptive loss selection within a unified likelihood-based framework, without requiring prior specification of the noise characteristics. Experiments on synthetic and real-world datasets demonstrate the effectiveness of AMLE-SQMF in quadratic manifold fitting and its robustness to diverse noise distributions.

---


### 268. [PROLA: Principal-Orthogonal Low-rank Adaptation for Predictive Spatiotemporal Weather Downscaling](https://arxiv.org/abs/2611.11318)

**<font color=#1a73e8>作者：</font>** Minseo Yoon, Minseong Bae, Sojin Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-resolution weather prediction is important for resolving local atmospheric patterns missed by coarse global forecasts. Large pretrained weather backbones have improved global forecasting, but adapting them to produce future high-resolution fields from recent coarse states remains challenging and costly. We formulate this setting as Predictive Spatiotemporal Weather Downscaling (PSWD), a task that jointly refines spatial and temporal resolution while predicting future high-resolution trajectories. To this end, we propose a framework that decomposes prediction into spatial and temporal stages using a shared pretrained backbone, fixed numerical scaffolds, and lightweight residual heads. For backbone adaptation, we introduce PROLA (PRincipal-Orthogonal Low-rank Adaptation), which allocates a fixed low-rank budget between pretrained weights' principal directions and their orthogonal complement. PROLA further rescales rank-1 optimizer updates using gradient signals, improving adaptation without increasing trainable rank. Experiments in the PSWD setting show that PROLA outperforms representative low-rank adaptation baselines. Further experiments across diverse datasets and tasks support the broader applicability of PROLA, showing that its benefits extend beyond the primary weather downscaling setting.

---


### 269. [Beyond Similarity Entropy: A Rank-Guided Data-Free Quantization Framework for Vision Transformers](https://arxiv.org/abs/2611.11320)

**<font color=#1a73e8>作者：</font>** Runqing Jiang, Ye Zhang, Pengpeng Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) have demonstrated remarkable performance, yet their computational and memory demands pose significant challenges for deployment on mobile devices. Data-free quantization (DFQ) enables the compression of ViTs without access to their original training data. Existing DFQ methods often synthesize calibration samples by maximizing the entropy of patch similarity. However, similarity entropy describes the dispersion of similarity values without ensuring that the generated samples cover diverse feature directions, potentially limiting their effectiveness for quantization calibration. To address this limitation, we propose RankQ-ViT, a rank-guided DFQ framework for ViTs. We first observe that patch similarity matrices derived from Gaussian noise tend to have lower ranks than those derived from real images. Motivated by this observation, we introduce a block-aware self-contrastive objective that promotes feature diversity during synthetic data generation without explicitly computing matrix rank at each optimization step. We then select calibration samples based on their rank and semantic consistency and use them for block-wise reconstruction of the quantized model. Experiments on ImageNet, COCO, ModelNet40, and ShapeNet demonstrate the effectiveness of RankQ-ViT across multiple architectures and tasks, particularly under low-bit quantization. The code is available at this https URL

---


### 270. [When Sensors Fail: Coverage Auditing with Incomplete Sensor Records](https://arxiv.org/abs/2611.11324)

**<font color=#1a73e8>作者：</font>** Chung-I Huang, Wen-Yi Chang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sensor outages can conceal prediction-interval coverage deficits behind acceptable marginal performance, while unavailable future readings leave some issued forecasts unscorable. We present a measurement-record audit that links issue-time outage duration, original target availability, and time-uniform statistical evidence. The audit retains complete forecast keys, batches all sensors and overlapping horizons at each measurement tick, and projects simultaneous covered-count and scored-count bounds onto a cumulative conditional expected coverage ratio. This target is distinguished from empirical coverage and outage-conditional population coverage. Selected traffic and air-quality results illustrate the gap between pooled and long-outage coverage; in METR-LA, only 7.6% of issued long-gap forecasts have originally observed targets. Of 30 primary sequential outage-state audits, 26 are inconclusive and four lack scored support. This concise presentation gives the core construction and selected aggregate evidence without the full experimental supplement.

---


### 271. [Linking Event-sequence Data Claims to Analytic Provenance in Chatbots: Technique and Evaluation](https://arxiv.org/abs/2611.11325)

**<font color=#1a73e8>作者：</font>** Po-Ming Law, Jianheng Ouyang, Nguyen-Truong Thinh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Chatbots are increasingly used to analyze temporal event sequences of which website clickstreams are among the most common. Explanations are essential for understanding claims about event-sequence data. However, existing systems often require programming expertise to interpret these explanations and fail to explain the data processes underlying the data claims. We introduce a technique for linking a data claim to its analytic provenance (i.e., the analytic steps and results that produced it). It has two components: a reference table that records analytic steps and results in addressable cells, and a citation format that binds each claim to one or more cells. To operationalize this technique for clickstream analysis, we curated a set of analytic operations for clickstream analysis, organized them through a pivot-table abstraction, and developed tools that an AI agent can invoke to create a reference table and assemble a natural language response with cited data claims. To evaluate how citations affect users' assessment of data claims, we conducted two crowdsourced experiments with 90 participants each. The experiments showed that participants perceived correct data claims to be more accurate with citations when compared with no explanations, and that they perceived incorrect data claims to be less accurate with citations when compared with code and no explanations.

---


### 272. [Conditional Diffusion-Based Proxy Representation Recovery for BCVA Prediction with Missing SLO Modality](https://arxiv.org/abs/2611.11326)

**<font color=#1a73e8>作者：</font>** Chuyi He, Hua Zou, Fei Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Preoperative prediction of postoperative best-corrected visual acuity (BCVA) can support prognosis assessment and individualized decision-making in cataract surgery. Multimodal learning can integrate preoperative optical coherence tomography (OCT) images, scanning laser ophthalmoscopy (SLO) images, and clinical text to characterize patient status. However, SLO images are often missing in real-world clinical data due to acquisition or data-management issues, resulting in incomplete multimodal inputs. To address this problem, this paper proposes a conditional diffusion-based method for SLO proxy representation recovery and fusion prediction. Instead of reconstructing raw SLO images, the proposed method formulates SLO missingness as proxy representation recovery in the latent feature space. Specifically, OCT image features and clinical text features are first fused to construct an OCT-text conditional representation, which guides the reverse denoising process of the diffusion model to estimate sample-specific SLO proxy representations. The recovered SLO proxy representation is then used as a substitute for the unavailable SLO modality and incorporated into the downstream multimodal fusion prediction network for postoperative BCVA prediction. Experiments were conducted on 2,141 preoperative multimodal cataract samples, with an SLO missing rate of 58.80%. The proposed method achieved an accuracy of 0.9714 under the criterion of an absolute prediction error within 0.1 LogMAR and a mean absolute error of 0.0423, outperforming representative postoperative visual acuity prediction and missing-modality learning methods. These results indicate that representation-level proxy recovery can alleviate the impact of SLO modality missingness on postoperative BCVA prediction.

---


### 273. [MoT3DVG: A Benchmark for Outdoor 3D Visual Grounding with Motion-Aware Descriptions and Temporal Cues](https://arxiv.org/abs/2611.11334)

**<font color=#1a73e8>作者：</font>** Shijia Zhao, Xusheng Guo, Qiming Xia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D visual grounding (3DVG) localizes language-referred objects in 3D scenes, with broad applicability in both indoor and outdoor environments. However, existing 3DVG research focuses on static indoor objects, limiting its use in dynamic outdoor autonomous driving. Motion descriptions, which capture the temporal dynamics of moving objects, offer a promising way to address this challenge. We therefore introduce MoT3DVG, a large-scale dataset for dynamic-aware outdoor 3DVG with temporally evolving motion descriptions. It contains 850 scenarios with 31,128 frames from nuScenes dataset, and provides 144,568 language prompts with motion-aware descriptions for dynamic objects across time. We further propose DynaVG, a novel framework that effectively leverages temporal cues for outdoor 3DVG. In addition to the standard modality-specific encoders, DynaVG introduces a Short-Long Integrated Dynamic Encoding (SLIDE) module before the language-point cloud alignment. SLIDE models both local motion cues and global temporal context via short-term window encoding and long-term window shifting. Extensive experiments demonstrate its state-of-the-art performance on MoT3DVG, validating the effectiveness of motion-aware encoding. Our work reveals open challenges and promising directions for future research in outdoor 3DVG.

---


### 274. [Where Should a Gate Look? Input vs. State Gating in Diagonal State Space Models](https://arxiv.org/abs/2611.11336)

**<font color=#1a73e8>作者：</font>** Riccardo Zattra, Giacomo Baggio, Leonardo De Marchi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern state-space models owe much of their computational efficiency to their linear, often diagonal, dynamics. Classical recurrent neural networks instead allow nonlinear state-to-state interactions, which can be beneficial when memory updates need to depend on the past context. In this paper, we ask whether state feedback through a simple gate regulating memory updates can enhance the expressivity of diagonal state-space models. To investigate this question, we compare gates that depend on the current input, the recurrent state, or both. We establish a strict expressivity separation: for scalar models, state gating solves induction-head tasks for arbitrary vocabulary size and sequence length, whereas input gating fails on a finite instance under standard stability assumptions on the state transition matrix. Experiments show that state gating retains its advantage on induction-head tasks in higher-dimensional models, whereas input gating performs better on selective copying tasks. Together, our results show that even a simple, diagonal form of state-feedback gating can unlock capabilities unavailable to input-controlled models, while input and state gating offer complementary strengths and achieve the strongest overall performance when combined.

---


### 275. [OPSRL-SSP: Optimistic Posterior Sampling for Stochastic Shortest Path with Minimax-Optimal Regret](https://arxiv.org/abs/2611.11337)

**<font color=#1a73e8>作者：</font>** Yiming Xu, Xian Wei, Cheng Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online reinforcement learning for the stochastic shortest path (SSP) problem with unknown transition dynamics. Although existing posterior-sampling methods perform well empirically on SSPs, their regret guarantees do not achieve the minimax-optimal order. We address this limitation by proposing OPSRL-SSP, an optimistic posterior-sampling algorithm for the SSP setting. The algorithm operates in epochs and uses a logarithmic, time-dependent schedule for the number of posterior samples. To induce optimism, we augment the transition model with a pseudo-state assigned an optimistic boundary value. We establish a high-probability regret bound of $\tilde{O}(B_\star \sqrt{SAK} + B_\star S^2 A)$, where $B_\star$ is an upper bound on the expected cost of the optimal policy, $S$ and $A$ are the numbers of states and actions, respectively, and $K$ is the number of episodes. In addition, we extend the analysis to general zero-cost SSPs using a universal cost-perturbation argument. The leading term matches the minimax lower bound $\Omega(B_\star \sqrt{SAK})$, thereby addressing the open problem raised by Jafarnia-Jahromi et al. [19] for posterior sampling in the SSP setting.

---


### 276. [Agentic Attribution of Cloud Resource Ownership](https://arxiv.org/abs/2611.11340)

**<font color=#1a73e8>作者：</font>** Tiltan Gilat, Gal Engelberg, Ariel Zadok 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security tools raise findings across cloud environments, and AI agents now investigate and prioritize them. A finding is still resolved by people: it has to reach the people responsible for fixing it and accountable for the resource it concerns. Ownership is the organizational context that decides who that is. Where recorded, it is declared by hand in configuration management databases or owner tags and goes stale unless kept current; accounts are shared, and automation creates much of the infrastructure. The knowledge sits in work records, code history, audit logs and identity directories, encoded in each organization's own conventions. Recovering it poses four challenges: the signal is scattered across sources, none of them authoritative; the conventions that carry it differ between organizations; reaching an owner takes multi-hop links; and those related to a resource differ in the strength of their relation. We define ownership as a set of entities, people or teams, each related to the resource by one of five patterns ordered by strength. We present a reference architecture for agentic ownership attribution that derives ownership from these records instead of declaring it: it profiles an organization offline into tested signal procedures and an ownership playbook, then attributes each resource with a coordinator agent and parallel investigators, with confidence computed by rules. On 100 resources of 50 Amazon Web Services (AWS) resource types in one organization, we pool the architecture's candidates with those of an unprimed general-purpose agent and verify every evidence piece against the records. The architecture reaches 92.1% weighted recall and 86.6% weighted precision, against 54.8% and 77.4%, at 0.55 times the agent's cost per unit of coverage. The difference lies in people who build and change resources without an explicit owner, found through work records and code history.

---


### 277. [Agent Self-Improvement with Frozen Weights: The Added Value and Limits of Failure Traces](https://arxiv.org/abs/2611.11342)

**<font color=#1a73e8>作者：</font>** Arkid Mitra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We evaluate whether an AI agent's harness, the notes around its model, can learn from the agent's failure traces beyond a matched search that never sees them. It can, but less than it looks. We tested an open 9-billion-parameter model with fixed weights; a larger teacher model wrote its notes. On generated customer-service decisions, where both note writers were told the target rules, notes based on the agent's mistakes improved accuracy by 4.0 percentage points over notes from the same process with the mistakes withheld. That process alone, trying and keeping better-scoring notes, reached about 60% of the total improvement. In full customer-service conversations the same notes showed no demonstrated improvement. Separately, a strict screen of single lessons admitted two customer-service lessons, still awaiting tests on new data, and one tool-use lesson, written without seeing the agent's mistakes, which showed no demonstrated gain on new tool-use tasks. A neutral note with no procedure scored higher than the learned lessons (exploratory). A blind audit judged 146 of 240 tool-use test items defective.

---


### 278. [Attacking Slide Puzzle CAPTCHAs Based on Time and Space Generative Adversarial Networks](https://arxiv.org/abs/2611.11355)

**<font color=#1a73e8>作者：</font>** Rui Guo, Xuelian Xie, Botao Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> CAPTCHAs can protect websites from malicious attacks. As a typical representative of behavior CAPTCHAs, slide puzzle CAPTCHAs have become increasingly popular in recent years due to their user-friendliness and high security. Previous attack methods on slide puzzle CAPTCHA mainly face challenges in the following four aspects. (1) The defense mechanisms of previous slide puzzle CAPTCHAs were relatively simple. The current slide puzzle CAPTCHAs have added complex interferences, detected slide trajectory features in the two-dimensional space, and added other defense mechanisms. (2) The previous notch detection methods were difficult to accurately locate the notch positions. (3) Previous attack trajectories were limited to the horizontal dimension, making them impossible to pass the existing detection. (4) The previous attack trajectories were generated by fitting functions, which were relatively simple and could not well simulate the slide characteristics of human users. In response to the above challenges, firstly, we systematically analyze the defense strategies of six most popular slide puzzle CAPTCHAs: Capy, Dingxiang, Geetest, Kyger, Shumei and Tencent. Secondly, for each type of CAPTCHA, we construct a notch detection dataset and a slide trajectory dataset separately. Thirdly, we use advanced YOLOv11 to detect the notch positions and train generative adversarial networks (GAN) to generate attack trajectories. As far as we know, we are the first to generate attack trajectories by directly learning human slide trajectory characteristic. According to the experimental results, this method cracked six most popular slide puzzle CAPTCHAs with success rates of over 90\%, and the attack time is only about 5 seconds, indicating that the security of existing slide puzzle CAPTCHAs is facing challenge. At the same time, we propose various methods to enhance the security of slide puzzle CAPTCHAs.

---


### 279. [MG-Cache: Multi-Granularity Caching for Accelerating Diffusion Transformer Inference](https://arxiv.org/abs/2611.11365)

**<font color=#1a73e8>作者：</font>** Zesen Chen, Youxuan Xu, Shigang Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformer (DiT) models, while having become a powerful backbone for generative synthesis, suffer from high inference cost on generating high-resolution images. Diffusion caching has emerged as a promising acceleration technique to reduce inference cost. However, existing caching strategies fail to accurately identify the varying importance of different computational modules and rarely coordinate cache reusing across the timestep and layer granularities, making it difficult to control error accumulation. To address these limitations, we propose multi-granularity caching (MG-Cache) for DiTs, a novel and fully training-free approach to exploit computational redundancy both on timesteps and Transformer layers. Our core innovation contains a two-stage caching strategy: an offline timestep profiling analysis that identifies redundant timesteps for cache reuse, followed by an adaptive layer-wise caching strategy that combines input stability with importance of each Transformer layer to selectively cache stable Attention and MLP submodules. Extensive experiments on mainstream open-source DiT models validate the effectiveness of our approach, achieving significant acceleration while maintaining high fidelity to the uncached output, with up to a 4.18x acceleration on HunyuanVideo.

---


### 280. [D3Tree: Learning to Prune Block-Diffusion Draft Trees for Efficient Verification](https://arxiv.org/abs/2611.11371)

**<font color=#1a73e8>作者：</font>** Hong Nie, Zhangchi Gao, Jun Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Block-diffusion drafters propose a whole block of tokens in one forward pass, and draft trees built from their position-wise marginals increase the expected accepted length of speculative decoding. Every tree node occupies a query row in target verification, so under concurrent serving low-yield branches compete with other requests for verification capacity. Existing tree methods select verified nodes by draft probability under a fixed or cost-selected per-request budget, and thus always retain a prefix of the drafter's ranking. We present D3Tree, which learns which nodes of a block-diffusion draft tree are worth verifying. A tree-size head with 2H+2 parameters predicts each candidate's conditional survival from the draft state, the candidate embedding, and its draft log-probability. Thresholding the product of these scores along parent chains yields an ancestor-closed subtree whose size adapts to each request and decoding round. The head is trained on a frozen drafter with conditional labels on the full candidate tree; an optional joint mode also steers the drafter toward the retained reference path. At serving time, D3Tree verifies whole trees under light load and, under heavy load, allocates one batch-wide node budget by predicted survival, sized to the target's matrix-multiplication tiles. Retained trees share one ancestor-masked target pass, while construction, pruning, and scheduling run on the GPU and overlap with the host. Across six vision-language verifiers and 17 text and multimodal benchmarks, D3Tree is fastest in 70 of 72 load settings, with 3.2-4.0x speedup over autoregressive decoding for one request and 1.3-1.8x at 64 concurrent requests, where fixed-budget trees fall below autoregressive speed. Under a time-varying arrival trace, it has the lowest mean end-to-end latency in every arrival phase.

---


### 281. [SegDis: Foreground Segmentation Followed by Type Discrimination for Salient and Camouflaged Object Detection](https://arxiv.org/abs/2611.11378)

**<font color=#1a73e8>作者：</font>** Dingning Luo, Shuo Dou, Tong Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Salient and camouflaged object detection (SOD and COD) both recover foreground support, yet most joint methods output only a binary mask and therefore cannot distinguish the type. USC12K distinguishes the two types, but its baseline USCNet still binds foreground existence to the type within a single normalization, so the failure source cannot be attributed. Our cross-task study shows that foreground localization transfers between SOD and COD, whereas type discrimination does not: a COD-only model recovers foreground on SOD images but its type judgement follows the training distribution rather than the foreground-background relation, so the two decisions require separate mechanisms. SegDis factorizes the output into an explicit foreground probability and a conditional type probability given foreground: FLR provides high-quality task-agnostic support, and RTA refines the SOD/COD assignment from the foreground-background relation without a task identifier. Because support is explicit, each ground-truth foreground pixel is classified as correct-type, type-swapped, or missed, so foreground-recovery and type-assignment errors are diagnosed separately. With PVT-v2-B2, SegDis attains 68.98% FG-mIoU and 78.35% mIoU on USC12K at about one-eighth of USCNet's parameters; CSCS is 5.75.

---


### 282. [Self-Supervised Collapse Prevention with Score-Based Entropy Maximization](https://arxiv.org/abs/2611.11379)

**<font color=#1a73e8>作者：</font>** Adarsh Kappiyath, Silpa Vadakkeeveetil Sreelatha, Xiatian Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have demonstrated the effectiveness of score-based objectives for generative modeling, yet their potential for self-supervised representation learning remains underexplored. We introduce Entropy-Based Regularization (EBReg), a framework that uses latent score estimation to regularize the latent distribution during self-supervised training. EBReg jointly learns an encoder and a latent score model, and utilizes the learned score to provide a diversity-preserving signal that prevents representational collapse. Motivated by a mutual-information lower bound, we formulate the objective as view alignment with smoothed marginal entropy maximization and optimize the marginal entropy without explicit density evaluation. The same score model can additionally be used at test time to refine corrupted representations toward the training latent distribution. Empirically, EBReg learns competitive representations on ImageNet-1K, achieving 75.57% linear-probe accuracy with ViT-L. Across diverse architectures, score-guided test-time adaptation further improves robustness on ImageNet-C, yielding an average relative accuracy gain of approximately 5%.

---


### 283. [The comparison of density estimation for transfer learning in Banach, Hilbert, Euclidean spaces](https://arxiv.org/abs/2611.11382)

**<font color=#1a73e8>作者：</font>** Maryam Alsadat Kazemian, Azam Bastanfard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Domain adaptation or DA methods are indispensable when target labels or computational resources are scarce, yet the domain kernel density and subspace alignment approaches completely assume a Hilbertian geometry.
They measure distributional discrepancy with symmetric L2 divergences over Euclidean feature spaces or reproducing kernel Hilbert spaces (RKHS). This preprint summarizes the manuscript Non-Hilbertian Domain Adaptation. Total Variation Alignment via L1 Density Regularization on Feature Manifolds, which proposes Banach Manifold Transfer Learning or BMTL. BMTL makes two coupled design decisions. The first one is that features are embedded on a geodesic manifold rather than treated as points of a flat Euclidean space, and the second one is that the density matching regularizer is formulated in an L1 Banach norm, whose minimization is equivalent, by Scheffe's theorem, to contracting the Total Variation or TV distance between domain densities, a bounded metric that weights all regions of the sample space uniformly. The L2 formulation, by contrast, squares deviations and therefore amplifies errors in the tails, over emphasizing density outliers that do not reflect meaningful distributional shift. Experiments on MNIST-USPS, COIL20, and Office+Caltech10 show consistent gains; the L1 variant beats an otherwise identical L2 ablation on every task, for example 92.44% vs. 89.80% on USPS->MNIST and surpasses the strongest baseline DMDA by +3.68% on average over twelve Office+Caltech transfers. This document situates the contribution with an explicit comparison of Euclidean, Hilbert, and Banach geometries.

---


### 284. [What Travels Across Languages? Reading, Transfer and Erasure of Cross-Lingual Concept Subspaces in Bangla Idioms](https://arxiv.org/abs/2611.11386)

**<font color=#1a73e8>作者：</font>** Syed Rifat Raiyan, Yousuf Ibne Kamal Niloy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual concept analysis requires distinguishing the information that a subspace retains from the classifiers and erasers that transfer through it. We study these operations in six frozen encoders using 10,359 Bangla (Bengali) idiom senses, eight input conditions, and figurative-class and sentiment labels. Class-mean directions provide the most consistent evidence of shared coarse meaning: in post hoc analyses, they outperform random-subspace, permuted-label and covariance-matched nulls in all 12 model-label tests under balanced accuracy. A prospective internal re-split supports idiom-alone sharing in 10 of 12 tests, spanning five encoders. The original confirmatory logistic-regression family rejects both planned nulls in 4 of 12 tests, where English directions gain only a few accuracy points above the majority-class floor (3.0-7.3). Classifier transfer depends on the input map and regularization: English-trained class-mean readouts beat both zero-shot nulls in 8 of 12 discovery tests, and stronger source-selected penalties improve transfer through logistic and LEACE directions. These readouts use Bangla-validation-selected layers and unlabeled target preprocessing. Input controls show greater coarse-class sharing for explicit glosses than for idiom counterparts. Reading, however, does not imply effective erasure: English-fitted LEACE removes less than one percentage point of Bangla figurative-class accuracy, compared with 4-11 points for Bangla-fitted LEACE; INLP shows a similar asymmetry. Pattern-filter analysis, covariance-weighted input maps and a binary Gaussian overlap bound explain how these operations can diverge. The analogous multiclass ordering is an empirical diagnostic, observed in 11 of 12 cells. The results support an estimator-sensitive account of cross-lingual concept sharing and motivate evaluating reading, classifier transfer, erasure and overlap separately.

---


### 285. [Orthogonal Updates for the Win: Towards Accelerated Adaptive Minimax Optimization](https://arxiv.org/abs/2611.11387)

**<font color=#1a73e8>作者：</font>** Zhiwei Zhai, Xinyu Wang, Wenjing Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-loop minimax methods are appealing for modern machine learning, but standard stochastic gradient updates can be unstable and oscillatory under tightly coupled primal-dual dynamics, making performance notoriously sensitive to stepsizes. To fundamentally improve stability, we develop an orthogonal update framework tailored to minimax optimization, which applies updates along orthogonalized directions to reduce update anisotropy. However, orthogonalization reshapes the optimization geometry and makes coordinating primal-dual stepsizes even more delicate. To overcome this challenge, we develop AdaSGDA, which equips orthogonal updates with an adaptive stepsize rule driven by accumulated gradient norms. This mechanism automatically balances coupled primal-dual progress under orthogonalization, yielding an effectively parameter-free method for nonconvex-strongly-concave minimax optimization. We prove that AdaSGDA avoids problem-dependent tuning while attaining the state-of-the-art $\mathcal{O}\left(T^{-1/4}\right)$ convergence rate. We further propose AdaSGDA-VR, which incorporates a carefully designed variance reduction scheme and achieves the faster $\mathcal{O}\left(T^{-1/3}\right)$ rate. Extensive experiments demonstrate that our methods deliver competitive performance compared to existing minimax optimization methods.

---


### 286. [Let the Gallery Learn Itself: Training-Free Iterative Side-View Face Recognition](https://arxiv.org/abs/2611.11391)

**<font color=#1a73e8>作者：</font>** Zijun Huang, Suncheng Xiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> What if a face recognition system could learn from every encounter without a single gradient update? We present Gallery Self-Evolution (GSE), a training-free framework where the gallery itself adapts at test time. The core mechanism---dedup-FIFO curation---archives novel appearance samples after successful recognition while permanently locking the enrollment template, bounded at 30 embeddings per identity. On CFP-FP and IJB-C benchmarks, GSE closes the side-view gap by +23 points at 45° yaw and boosts TAR@FAR=0.001 by +9.4 points, all at CPU-level cost. No retraining. No GPU. Just a gallery that grows smarter every time it meets you.

---


### 287. [Self-Healing by design: Immune-system inspired autonomous cyber resilience](https://arxiv.org/abs/2611.11394)

**<font color=#1a73e8>作者：</font>** Shari Finner, Swarna Kumarswamy-Das, Bart Gijsen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Digital innovations have strongly improved ship capabilities, including command, control & communication, navigation and combat management. In the wake of digitisation and geopolitical stress, resilience against cyber-attacks has become a key challenge. Autonomous Cyber Resilience (ACR) methods, inspired by features of the human immune system, provide a promising perspective. Proofs of concept of autonomous self-healing and self-protecting software have been realised in cloud environments using containerisation, monitoring and deployment technology. However, developing a suitable "cyber immune system" for more complex digital systems is still an intricate challenge. In this paper, we share insights on how ACR methods can be combined with resilience mechanisms present in critical naval and aeronautical manoeuvring systems. Using TNO's "OpPic" application, we show how TNO's Self-Healing for Cyber Security software can provide autonomous mission- and threat-adaptive resilience. On this basis, six guidelines for the design of autonomous cyber resilient systems are derived. The ultimate goal is to enable operators to oversee and control their system's "cyber immune response", to be able to continuously adapt to evolving threats and mission priorities.

---


### 288. [Computationally Efficient Offline Policy Optimization with All-Policy Linear Realizability](https://arxiv.org/abs/2611.11423)

**<font color=#1a73e8>作者：</font>** Zhijie Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study offline policy optimization in finite-horizon Markov decision processes where every deterministic Markov policy has an action-value function linear in known features, with coefficient norm at most $B$. From independent complete trajectories of one unknown Markov behavior policy, and under all-policy occupancy coverage, we give an algorithm with $\widetilde O(\varepsilon^{-2})$ sample dependence and computational complexity polynomial in $\log(2+B)$. The algorithm performs exactly one convex regression per layer. Its stopped-return targets are the values of a single consistent Markov witness policy. A shared reference design and bounded prediction constraints convert fast clipped-regression error into pointwise confidence for the raw linear predictions. Truncated leverage controls the performance loss without requiring empirical covariance approximation at scale $B^{-2}$. Rounding confidence radii upward preserves the exact witness and yields a polynomial-time bit implementation for rational numerical inputs. The guarantees allow any fixed initial-state distribution; realizability and coverage need only be checked for deterministic policies. We also establish a covariance-coverage variant with uniform approximate realizability and polynomial dependence on $B$. A two-action lower bound shows that the accuracy exponent $2$ is necessary.

---


### 289. [Vietnamese Legal Ontology: Every legal answer, traced to the article that grounds it](https://arxiv.org/abs/2611.11426)

**<font color=#1a73e8>作者：</font>** Khac-Hoai Nam Bui, Quan Tran Minh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A legal answer is only as good as the article it rests on. Vietnam's largest open legal corpus pairs 109,543 published questions and answers with 573,851 legal documents, yet its citations are free text: "Khoan 3 Dieu 101 cua Bo luat nay" ("Clause 3, Article 101 of this Code") names neither the code nor its version. Following the five stages of NVIDIA Auto Ontology, Discover, Ground, Validate, Expose and Learn, we turn four open datasets into a knowledge graph of 11.5 M nodes and 16.0 M edges in which every node and edge carries its source record and method, with no duplicate keys, dangling edges or schema violations. Of 67,868 cited provisions, 61,487 resolve to a dated law version, 51,694 to a parsed article, clause or point, and 19,012 are confirmed word for word. The ontology then shows what flat records hide. 36% of the 78,361 answers whose citations resolve now cite a law that is no longer in force; 2,525 verified citations point to an article number that says something else in the current law; 2,520 citations were re-versioned because their words match a different version than their date suggests; and 5,575 document numbers are shared by several local authorities, one of them by 72. Every number in this paper is computed from the graph.

---


### 290. [Flex-DDCM: Zero-Shot Task-Oriented Image Compression via Diffusion Trajectory Guidance](https://arxiv.org/abs/2611.11427)

**<font color=#1a73e8>作者：</font>** Yixin Gao, Runsen Feng, Xin Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent zero-shot image compression methods exploit the powerful priors of pretrained diffusion models to produce perceptually pleasing reconstructions without compression-specific training. However, image compression serves not only human viewing but also machine analysis, while existing zero-shot codecs have limited flexibility in meeting the diverse reconstruction requirements of these applications. In this paper, we propose Flex-DDCM, a framework for zero-shot task-oriented image compression via diffusion trajectory guidance. Building on Turbo-DDCM, we adapt the coded diffusion trajectory through task-guided noise selection, embedding the effects of task guidance into the compressed representation. Guidance terms can be applied individually or combined, with timestep-dependent strengths controlling their influence throughout denoising. This design enables task adaptation without introducing additional decoding complexity. Experiments demonstrate flexible trade-offs among pixel fidelity, perceptual quality, and downstream task performance, with competitive performance against trained task-oriented codecs and faster decoding than Diff-ICMH.

---


### 291. [Unlearning at Speed: Rapid Activation Dampening for Efficient Machine Unlearning in Real-World Face Recognition](https://arxiv.org/abs/2611.11433)

**<font color=#1a73e8>作者：</font>** Rouqaiah Al-Refai, Leo Scheubel, Philipp Terhörst  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine unlearning has become increasingly important in face recognition, where regulations like the GDPR empower users to request the removal of their personal data from deployed models. However, most existing unlearning methods are designed for closed-set classification with small-scale models and training data, and therefore do not generalize to real-world face recognition systems, which operate in an open-set setting with large-scale models and data. In this work, we propose Rapid Activation Dampening (RAD), a fast and targeted unlearning method tailored specifically for large-scale open-set face recognition. RAD approximates differences in average neuron activations between forget and retain identities, identifying and selectively suppressing neurons that are most associated with the targeted identity through a sensitivity-controlled dampening mechanism. We further propose the Forget Score (FS), which addresses the mismatch between existing unlearning metrics and open-set problems by providing a probabilistic interpretation of forgetting directly in the representation space. Experiments across several recent large-scale face recognition architectures and datasets show that RAD achieves strong forgetting while preserving overall model utility and substantially improving unlearning speed. These findings establish RAD as a scalable and practical approach to machine unlearning in face recognition systems.

---


### 292. [Learning to Rank Propagators in Constraint Programming](https://arxiv.org/abs/2611.11447)

**<font color=#1a73e8>作者：</font>** Matija Lojović, Mladen Nikolić  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The order in which propagators are executed can substantially affect the performance of constraint programming solvers, yet propagator priorities are typically determined by fixed, manually designed heuristics. In this work, we explore learning instance-dependent propagator priorities from static problem features. We formulate the task as a learning-to-rank problem, addressing the challenge that the quality of a priority assignment can be measured through solver runtime, while the desired priorities of individual propagators are not directly observable. A self-attention-based model jointly scores the propagators present in an instance and is trained using pairwise preferences derived from solver runtimes measured under randomized propagator priority assignments, with a Plackett-Luce-based ranking objective. Predicted rankings are mapped to the discrete priority levels of the Choco solver before search begins, without modifying its propagation or search procedures. We evaluate the approach on XCSP3 instances and demonstrate that propagator ordering can have a substantial impact on solving time. On a test set of 698 instances, picked out as most difficult by problem class, the learned priorities increase the number of solved instances from 634 to 654, reduce median solver runtime by 27.93%, and reduce aggregate penalized runtime (PAR1) by 12.65% compared with Choco's default priorities. We further observe that improvements vary across problem classes and show that a simple policy selecting between learned and default priorities further increases the number of solved instances. These results demonstrate the potential of learning instance-dependent propagator priorities to improve constraint programming performance, particularly on difficult instances.

---


### 293. [MOMENT-DP: Momentum Aware Evaluation of Correlated Noise for Differentially Private Training](https://arxiv.org/abs/2611.11457)

**<font color=#1a73e8>作者：</font>** Sunny Gupta, Raja Viswanadha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporally correlated noise can substantially improve the utility of differentially private optimization, yet candidate mechanisms are commonly designed or evaluated using only partial information about the optimization process, such as workload structure, learning-rate schedules, or local curvature. We study whether persistent optimizer state provides additional information that can change the relative utility of privacy-valid correlated-noise mechanisms.
We introduce MOMENT-DP, an optimizer-state-aware framework that models how temporally correlated privacy noise propagates through momentum-based optimization. For locally quadratic objectives, MOMENT-DP expresses privacy-induced final loss through an optimizer transfer operator that jointly captures curvature, learning-rate scheduling, momentum, and temporal noise covariance. NoiseCurve's curvature-aware quadratic criterion is recovered exactly as the zero-momentum, constant-learning-rate special case.
Changing only momentum while holding curvature, schedule, privacy calibration, and candidate mechanisms fixed induces genuine mechanism-ranking reversals. The effect persists outside exact quadratic dynamics in per-example-clipped private logistic regression, while remaining unresolved in the neural regime we study. These results establish optimizer state as an under-modeled, decision-relevant axis in evaluating temporally correlated privacy noise.

---


### 294. [Robust and Private Swarm Learning via Zero-Knowledge Validator Admission and Consensus Aggregation](https://arxiv.org/abs/2611.11477)

**<font color=#1a73e8>作者：</font>** Marco Arazzi, Mert Cihangiroglu, Antonino Nocera  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Swarm Learning improves resilience and removes the need for a single trusted coordinator by distributing model aggregation and validation across participating nodes. However, it also delegates the validation of model updates to peers whose private data may be biased, unrepresentative, or adversarial, and existing Swarm Learning protocols generally do not attest that data, leaving decentralized validation as an attack surface. We present a robust, privacy-preserving Swarm Learning framework that makes verifiable data quality the condition for admission to the learning task. A validator joins only after a zero-knowledge attestation proves, without revealing any raw sample, that a reference model ran correctly on its private data. The attested outputs also yield a label-free class profile, so the network assembles a collectively IID validator pool from individually skewed validators as accurately as an oracle with the true labels (total-variation distance to uniform 0.025, against 0.021 for the oracle and 0.21 for random selection). Admitted validators score client updates and, through a Tendermint-style Byzantine Fault Tolerant consensus, agree on a gradient mask and a quality-derived aggregation weight for each submission, replacing dataset-size weighting with a quality-aware signal. Adapting the cut-layer idea of Split Learning, a challenge-based audit lets peers re-verify that a mask was computed on the attested data without an expensive end-to-end zero-knowledge proof. Across four benchmarks under non-IID partitions the framework matches FedAvg on clean data; under a gradient-scaling attack that collapses FedAvg to random chance, it retains 94% of clean accuracy on CIFAR-100 and over 99% on FashionMNIST, where FedAvg achieves only 2.1% and 11%. The result is a private, robust, and auditable foundation for decentralized learning.

---


### 295. [One-Shot Hierarchical Federated Clustering for Distributed Non-IID Biomedical Data Analysis](https://arxiv.org/abs/2611.11481)

**<font color=#1a73e8>作者：</font>** Shenghong Cai, Yiqun Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In multi-institutional biomedical data analysis, comprehensive disease profiles are often fragmented across different data silos. Furthermore, local data distributions typically exhibit varying levels of granularity or even complex nested structures. Although Hierarchical Clustering (HC) is a powerful tool for exploring such data topologies, its cumbersome recursive process incurs prohibitive computational overhead and renders it highly susceptible to privacy leakage. This paper, therefore, introduces an efficient one-shot hierarchical FC framework that performs client-end (institutions) distribution exploration and server-end distribution aggregation through one-way prototype-level communication from clients to the server. Although the designed one-shot prototype transmission guarantees minimal computational overhead and mitigates privacy risks, it inevitably incurs information loss. To counteract this, a multi-granular competitive learning mechanism is proposed on the server to fuse the clusterlets, effectively maximizing the retention and mining of global distribution topologies under limited, one-way communication constraints. It turns out that the complex cluster distributions across clients can be efficiently explored, and extensive experiments comparing state-of-the-art methods on public datasets demonstrate the superiority of the proposed framework in balancing robust clustering, privacy preservation, and computational efficiency.

---


### 296. [Learning through Capacity Awareness to Minimize Hospital Readmissions](https://arxiv.org/abs/2611.11493)

**<font color=#1a73e8>作者：</font>** Lydia T. Liu, Kara Schechtman, Pengyi Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive algorithms are increasingly used to guide hospital discharge decisions, yet these models can exhibit censoring bias for vulnerable patients due to insufficient historical data or past discharge decisions. When biased readmission risk predictors are used to inform discharges, the training data generated by discharge decisions may perpetuate similar biases when predictors are re-trained, leading to a vicious cycle. We extend a queueing-based Markov decision process for hospital discharge to incorporate periodically retrained readmission risk predictors. Our key insight is that cost-optimal, "capacity-aware" operational decision policies can naturally diversify the lengths of stay at which patient outcomes are observed, enabling consistent estimation of readmission risk without explicit fairness constraints. We prove that repeated retraining under discharge-up-to policies converges to unbiased risk estimates under well-specification. In synthetic experiments and calibrated simulations based on patient-level data from a partner hospital, we find that where commonly used threshold-on-risk policies can remain persistently biased, discharge-up-to policies reduce learning error over status quo decision policies (such as thresholding on risk) by 24%-25%. These improvements to estimation also mitigate some forms of bias, reducing readmission cost disparities (adjusted for baseline risk differences between demographic groups) by 38%-63%. Our results demonstrate how capacity-aware decision policies can improve both predictive performance and fairness by addressing censoring bias.

---


### 297. [Regret without Optimal-Arm Feedback under Reward-Dependent Delays](https://arxiv.org/abs/2611.11494)

**<font color=#1a73e8>作者：</font>** Zhong Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study stochastic bandits with reward-dependent delays, possibly infinite, whose reports omit the originating round. For each $c\in[0,1)$, Balanced Historical Optimism (BHO) has a delay term controlled by the largest suboptimal-arm quantile at level $1-c\Delta_i$, without requiring optimal-arm reports. Lower bounds give an inverse-square slack cost in the logarithmic statistical regime and linear minimax regret at $c=1$. A family with growing $K$ forces worst-case regret $\Omega(G\log K)$ for every learner, where $G=\max_i\Delta_i h_i$ is the largest gap-weighted suboptimal cutoff. Pending-triggered balance preserves BHO's weighted-cutoff bound for $c<1$ and attains the historical-greedy exploration coefficient with deterministic rewards, a unique optimum and fixed bounded delays. Gap-weighted comparisons and experiments show when shared waiting helps and what balanced exploration costs.

---


### 298. [TID System for Speech-COSER Challenge 2026: ASR Track](https://arxiv.org/abs/2611.11497)

**<font color=#1a73e8>作者：</font>** Fernando López, Jordi Luque  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe the system submitted by Telefónica Innovación Digital to the Speech-COSER Challenge 2026, which features spontaneous speech from elderly speakers recorded in rural Spain. For ASR, we perform CTC-based pseudo-forced alignment scores audio-text match quality to guide a two-stage LoRA curriculum, followed by post-hoc magnitude pruning of the LoRA matrices to enhance generalization. An ensemble of seven systems combined via ROVER achieves 36.25\% unnormalized and 22.17\% normalized WER.

---


### 299. [EVAX: Towards a Practical, Pro-active & Adaptive Architecture for High Performance & Security](https://arxiv.org/abs/2611.11498)

**<font color=#1a73e8>作者：</font>** Samira Mirbagher Ajorpaz, Daniel Moghimi, Jeffrey Neal Collins 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper provides an end-to-end solution to defend against known microarchitectural attacks such as speculative execution attacks, fault-injection attacks, covert and side channel attacks, and unknown or evasive versions of these attacks. Current defenses are attack specific and can have unacceptably high performance overhead. We propose an approach that reduces the overhead of state-of-art defenses by over 95%, by applying defenses only when attacks are detected. Many current proposed mitigations are not practical for deployment; for example, InvisiSpec has 27% overhead and Fencing has 74% overhead while protecting against only Spectre attacks. Other mitigations carry similar performance penalties. We reduce the overhead for InvisiSpec to 1.26% and for Fencing to 3.45% offering performance and security for not only spectre attacks but other known transient attacks as well, including the dangerous class of LVI and Rowhammer attacks, as well as covering a large set of future evasive and zero-day attacks. Critical to our approach is an accurate detector that is not fooled by evasive attacks and that can generalize to novel zero-day attacks. We use a novel Generative framework, Evasion Vaccination (EVAX) for training ML models and engineering new security-centric performance counters. EVAX significantly increases sensitivity to detect and classify attacks in time for mitigation to be deployed with low false positives (4 FPs in every 1M instructions in our experiments). Such performance enables efficient and timely mitigations, enabling the processor to automatically switch between performance and security as needed.

---


### 300. [ForeAct: Geometry-Guided Action Learning from World Representations](https://arxiv.org/abs/2611.11500)

**<font color=#1a73e8>作者：</font>** Wei Lu, Jiaxi Zhang, Yunheng Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robotic manipulation requires representations that capture both scene geometry and its evolution during interaction. Existing approaches have largely treated these two aspects separately. World action models capture such dynamics by coupling action prediction with future video generation, but their reliance on iterative diffusion or rectified-flow inference leads to high computational cost, while their representations lack explicit spatial structure. Explicitly modeling scene geometry typically requires auxiliary modules that increase both parameter count and computational cost. Conversely, geometry-centric policies primarily recover observed spatial structure and often lack explicit supervision for anticipating future geometric changes during interaction. To address these limitations, we introduce ForeAct, which repurposes a pretrained video world model as a single-pass representation backbone for low-latency control. ForeAct directly processes the clean latent of the current observation in one forward pass, eliminating future-frame synthesis and iterative denoising while retaining the backbone's pretrained spatiotemporal priors. Rather than introducing a separate geometry backbone, ForeAct uses learnable tokens supervised by next-frame relative depth to shape the shared video representation through bidirectional self-attention. This compact interface turns the spatial knowledge already encoded in the backbone into a future-aware representation for action generation, with little parameter overhead. The lightweight geometry readout is used only during training and removed at deployment, enabling low-latency, geometry-aware control without depth input or an external geometry backbone. Without additional large-scale pretraining, ForeAct achieves 96.6% average success on LIBERO, 63.5% on SimplerEnv-Bridge, and a 74.4% success rate across 90 real-world rollouts.

---


> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-520](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
