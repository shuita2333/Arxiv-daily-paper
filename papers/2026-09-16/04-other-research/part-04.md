# 📦 其他研究 | 2026年09月16日

> 本类共 **416** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-416](./part-09.md)

---

### 151. [Hardware-Aware Learned Representation Compression for Distributed In-Sensor Vision](https://arxiv.org/abs/2609.13947)

**<font color=#1a73e8>作者：</font>** Chengwei Zhou, Abu Masum, Xuming Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-sensor computing reduces the cost of transmitting high-resolution image data by performing early-stage processing near the sensor. However, the logic chip integrated with a CMOS image sensor (CIS) is tightly constrained in compute and memory, limiting conventional deep neural network partitioning. We present OASIS, a distributed in-sensor vision framework that uses a lightweight encoder to generate compact, task-relevant representations before off-chip transmission. The encoder is trained end-to-end using task, entropy, and reconstruction objectives, while the decoder is used only during training. OASIS supports two complementary deployment paths. The first applies 4-bit quantization and Huffman coding while preserving the spatial structure required by classification and dense-prediction tasks. The second uses Sobol-based hyperdimensional computing (HDC) to transform the encoder latent into a fixed-dimensional binary hypervector for associative-memory classification. For the SwinViT-based VWW model, mapping a $3\times3\times8$ latent to a 64-dimensional hypervector provides an additional $1.77\times$ communication reduction with less than one percentage point of accuracy loss relative to the 128-dimensional configuration, yielding an overall $18{,}816\times$ reduction compared with raw 8-bit image transmission. We implement the digital near-sensor pipeline on an AMD Xilinx Zynq UltraScale+ FPGA and characterize it using direct board-level power measurements and Vivado post-implementation analysis, together with circuit-simulated CIS models and a 7-nm ASIC projection. Across visual wake-word classification, hand tracking, and eye tracking, OASIS reduces total system energy by approximately $2\times$-$4.5\times$ while maintaining competitive accuracy, demonstrating a practical hardware-algorithm co-design path for communication-efficient in-sensor vision.

---


### 152. [Linear Ensemble Sampling with Smaller Ensembles](https://arxiv.org/abs/2609.13954)

**<font color=#1a73e8>作者：</font>** Taehyun Hwang, Min-hwan Oh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ensemble sampling offers a practical approach to randomized exploration by maintaining a collection of models, but how small an ensemble can be while retaining strong regret guarantees remains unresolved. In particular, the existing guarantees use an ensemble size of $\Theta(d\log T)$, leaving a logarithmic gap in the horizon $T$ relative to the intrinsic $\Omega(d)$ ensemble-size barrier. We aim to narrow this gap by proposing an ensemble sampling algorithm that refreshes the ensemble only when the regularized Gram matrix changes substantially. This mechanism localizes the perturbation analysis to epochs with controlled Gram-matrix drift and reduces the sufficient ensemble size to $\Theta(d\log d+d\log\log T)$, while preserving the state-of-the-art $\tilde O(d^{3/2}\sqrt T)$ regret for ensemble sampling with arbitrary bounded arm sets. We further show that, when the arm set is finite of cardinality $K$, the proposed algorithm achieves the sharper regret bound $\tilde O(d\sqrt{T\log K})$. To the best of our knowledge, this is the first ensemble-sampling guarantee that simultaneously recovers both canonical regret scalings known for randomized linear bandit algorithms: the $\tilde O(d^{3/2}\sqrt{T})$ rate for arbitrary bounded arm sets and the $\tilde O (d\sqrt{T\log K})$ rate for finite arm sets. The algorithm also admits an anytime implementation without resetting past data, and experiments show that it remains competitive with baselines while using substantially smaller ensembles.

---


### 153. [SGWIB:Sliced Gromov-Wasserstein Information Bottleneck for Video Highlight Detection](https://arxiv.org/abs/2609.13966)

**<font color=#1a73e8>作者：</font>** Hanjuan Huang, Yung-Chieh Yeh, Hsing-Kuo Pao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video highlight detection aims to identify temporally important segments that capture the most informative or engaging events in a video. Reliable prediction therefore requires not only discriminative segment representations but also preservation of the temporal relationships among neighboring and distant segments. The information bottleneck principle has proven effective for learning compact and task-relevant representations, yet it has not been explored for video highlight detection, and applying conventional formulations directly would overlook inter-segment relational structure and distort highlight relevant temporal organization during compression. We therefore introduce the Sliced Gromov-Monge Gap (SGMG), a structure aware regularizer that measures the excess relational distortion induced by a prescribed source-to-bottleneck mapping relative to an optimal sliced structural correspondence. Building on SGMG, we develop SGWIB, an information-bottleneck framework for single-modal video highlight detection that learns compact bottleneck representations while preserving inter-segment temporal structure. We further introduce Home-Away-Related Contextual Pseudo-Labels and a contextual disentanglement module that reduce sports-specific contextual bias by separating highlight oriented information from contextual patterns. Experiments on MrHiSum and MoSu show that SGWIB attains the best Kendall's tau, Spearman's rho, mAP@50, and mAP@30 among the compared single-modal methods on both datasets. On MrHiSum, the visual model improves the strongest previous results by 0.031, 0.031, 0.87, and 0.75 on these four metrics, respectively. These results show that structure-aware information-bottleneck regularization combined with contextual disentanglement improves segment-level highlight prediction.

---


### 154. [Zero-Shot Cross-Material Ptychographic Phase Reconstruction Using Deep Learning](https://arxiv.org/abs/2609.13969)

**<font color=#1a73e8>作者：</font>** Wen-Chun Lin, Yu-Chee Tseng, Jen-Jee Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ptychographic phase reconstruction is commonly formulated as an iterative inverse problem, requiring repeated object-probe updates and resulting in substantial computational cost for large-scale 4D-STEM data. We present a direct local-to-global learning framework that reconstructs full-field phase maps from diffraction measurements without iterative refinement during inference. The proposed network predicts local wrapped-phase patches from individual diffraction patterns using a sine-cosine representation, and the predictions are assembled into a full-field reconstruction using calibrated scan positions and Gaussian-weighted stitching. To evaluate generalization beyond the training domain, the model is trained on one material and directly applied to another in a zero-shot setting without target-domain fine-tuning. Experiments on AuPd and MoS$_2$ demonstrate consistent cross-material transfer in both directions, with the proposed method achieving the best full-field MSE, PSNR, and MS-SSIM among the evaluated learning-based methods. Compared with the iterative ePIE approach, the proposed direct local-to-global pipeline reduces end-to-end reconstruction time by approximately 10x, demonstrating its potential for efficient and transferable ptychographic reconstruction.

---


### 155. [Mind2Cloud: EEG-to-Point Cloud Generation with Two-Granularity Diffusion Decoding](https://arxiv.org/abs/2609.13991)

**<font color=#1a73e8>作者：</font>** Yongyi Lu, Xiongfeng Huang, Zhijing Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing 3D objects from brain signals offers a promising avenue for understanding human visual cognition. While prior work has shown initial success using EEG signals for 3D reconstruction, existing methods typically employ a uniform diffusion decoder, overlooking the evolving semantic granularity of both EEG representations and the diffusion denoising process. In this paper, we propose Mind2Cloud, a novel EEG-to-point-cloud generation framework based on two-granularity diffusion decoding. The core of Mind2Cloud is a time-aware decoder that integrates a global Transformer branch and a local Point-Voxel CNN (PVCNN) branch across diffusion timesteps through a learnable fusion mask. Specifically, Transformer layers are incorporated into the early upsampling stages to capture global object structure under high uncertainty, while PVCNN modules are used in later stages to refine local geometric details. Inspired by the hierarchical nature of EEG-based visual representations, this design dynamically adapts its spatial granularity in accordance with the coarse-to-fine trajectory of diffusion denoising. We further introduce an adversarial refinement module to enhance geometric realism and semantic consistency. Extensive experiments on the EEG-3D dataset across all 12 subjects demonstrate that Mind2Cloud outperforms prior work in both geometric accuracy and semantic alignment, setting a new benchmark for EEG-to-point-cloud generation. Our source code is available at this https URL.

---


### 156. [CirrGuide: A Deep Cascaded Framework for Liver Cirrhosis Segmentation and Severity Classification from T2-Weighted MRI](https://arxiv.org/abs/2609.14010)

**<font color=#1a73e8>作者：</font>** Muntaqim Ahmed Raju, Ruizhe Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present CirrGuide, a deep cascaded framework for cirrhotic liver segmentation and severity classification. Cirrhosis causes progressive structural changes in the liver and can lead to serious clinical complications, making severity assessment important for disease monitoring and treatment planning. However, severity classification is challenging because imaging patterns are often subtle, spatially variable, and similar across adjacent stages. CirrGuide addresses this by explicitly linking localization with classification. A ResNet50 encoder with an Attention U-Net decoder first predicts a soft cirrhotic liver mask, which is then used as an anatomical prior in a ResNet50-based classification branch. This branch combines global multi-scale features with mask-guided attention-pooled regional features to classify Mild, Moderate, and Severe cirrhosis. On the official CirrMRI600+ T2-weighted (T2W) 2D split, CirrGuide achieves 89.83% Dice and 84.14% mIoU for segmentation, 69.58% accuracy and 61.55% macro F1-score for severity classification. Compared with segmentation-only, classification-only, and multi-task baselines, CirrGuide improves both localization and severity classification, demonstrating the benefit of using predicted cirrhotic liver masks as anatomical priors for cirrhosis analysis.

---


### 157. [Schizophrenia Detection from EEG Signals: A Transformer Framework with Spectrogram Representation](https://arxiv.org/abs/2609.14015)

**<font color=#1a73e8>作者：</font>** Abtin Shafiei, Mohsen Hooshmand, Majid Ramezani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Schizophrenia is a serious psychiatric disorder that affects millions of people worldwide, and its diagnosis remains primarily dependent on clinical assessment. Electroencephalography (EEG) provides a non-invasive approach to investigate brain activity and has shown potential to support automated Schizophrenia detection. However, existing EEG-based classification studies often suffer from limitations including small datasets, inconsistent preprocessing strategies, and evaluation protocols that may not adequately prevent subject-related data leakage. In this study, we propose an EEG-based Schizophrenia classification framework that transforms preprocessed EEG recordings into time-frequency representations using the Short-Time Fourier Transform. The generated spectrogram images are classified using both conventional Machine Learning algorithms, including Support Vector Machines, Random Forests, and XGBoost, and Deep Learning models, including convolutional architectures and CNN-Transformer hybrids. To ensure reliable evaluation, all data partitions are performed at the subject level. Experimental results demonstrate that the proposed approach achieves competitive classification performance, with the CNN-Transformer (CT-SZ) model achieving an AUC-ROC of 88.41% and the CNN + Squeeze and Excitation + Transformer (CST-SZ) achieving an AUC-ROC of 92.88% on the independent test set.

---


### 158. [Quantum-Gated LiteSSD: A Parameter-Efficient Lightweight Hybrid Quantum-Classical Framework for Forward-Looking Sonar Object Detection](https://arxiv.org/abs/2609.14025)

**<font color=#1a73e8>作者：</font>** Niloy Kumar Mondal, Poulomi Sarker Puja  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forward-looking sonar object detection is essential for underwater perception, yet deployment on embedded platforms requires highly compact models. To address this challenge, we explore quantum computing and introduce Quantum-Gated LiteSSD, a parameter-efficient hybrid quantum--classical detector that reformulates QuCNet-style multi-circuit quantum processing as an identity-centered channel-gating mechanism for spatial feature modulation. Experiments on the Marine Debris Watertank dataset and UATD forward-looking sonar benchmarks demonstrate an effective parameter--accuracy trade-off. The proposed detector achieves 90.84% $\mathrm{mAP}_{50}$ on Watertank with approximately $62\times$ fewer parameters than YOLO26s and $164.3\times$ fewer parameters than SSD-VGG16. On UATD, the model achieves 70.37% $\mathrm{mAP}_{50}$ with only 0.150M parameters, making it approximately $4.1\times$ smaller than SSGA-YOLO while retaining meaningful multi-class detection capability.

---


### 159. [A High-Throughput FPGA Architecture for Real-Time TCP-SYN Scan Detection](https://arxiv.org/abs/2609.14043)

**<font color=#1a73e8>作者：</font>** Faisal Saeed, Mohammad Fahad, Ayesha Javaid 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> TCP-SYN port scanning often precedes cyber-attacks, and early detection of scanner fingerprints embedded in packet headers can provide timely intrusion alerts. Existing approaches are either too computationally expensive for line-rate operation or limited to offline analysis. This brief presents a lightweight FPGA architecture for reconfigurable line-rate fingerprint detection, where each fingerprint is compiled into a shallow Boolean LUT tree, enabling parallel evaluation with constant two-cycle latency regardless of fingerprint count, while resource cost grows linearly with fingerprint count. This detection core is decoupled from a MAC-layer frontend that performs streaming field extraction with no frame buffering or higher-layer state, allowing deployment across different line rates by modifying only the frontend. A Python framework automatically compiles Boolean expressions into synthesizable HDL, eliminating manual RTL changes. For TCP-SYN port-scan fingerprint detection, the architecture uses approximately 0.5% LUTs at 10 Gbps on a Versal VCK190 for 18 deployed fingerprints, with capacity for over 2,000 concurrent fingerprints, and under 2.5% on a Virtex-6 at 1 Gbps, with a detection latency of 10 ns at both rates, three to four orders of magnitude below typical per-packet processing latency in software intrusion-detection systems. The system was cross-validated against a software re-implementation on an 8-hour production packet trace, confirming detection correctness with zero false positives/negatives.

---


### 160. [Data-Efficient Agentic Graph Domain Adaptation via Reliability-Aware Prototype Learning](https://arxiv.org/abs/2609.14045)

**<font color=#1a73e8>作者：</font>** Yingxu Wang, Kunyu Zhang, Siyang Gao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic learning systems are often required to adapt after deployment by observing new data and reusing prior knowledge under limited supervision or feedback. For graph-structured prediction, Graph Domain Adaptation (GDA) naturally instantiates this setting by transferring knowledge from labeled source graphs to unlabeled target graphs under distribution shifts. However, most GDA methods assume sufficient labeled source graphs, which becomes restrictive in data-efficient agentic settings where only limited source evidence can be retained. Under such constraints, source semantics become unreliable, leading to unstable source anchoring, uncertain target association, and fragile targetmarginal calibration. To address these challenges, we propose DEAG, a reliability-aware prototype learning framework for data-efficient agentic GDA. DEAG estimates class reliability from retained source support and embedding compactness, and constructs stable reusable source anchors by blending empirical prototypes with classifier directions. Guided by these anchors, DEAG performs prototype-aware soft target association and aligns confidence-weighted target centers with source semantics. A source-prior regularizer further sharpens target predictions while keeping the target marginal consistent with retained source evidence. Experiments on graph benchmarks with diverse domain shifts show that DEAG improves average adaptation performance over competitive GDA baselines under the same source-data budget.

---


### 161. [Symmetric Models for Syndrome Decoding](https://arxiv.org/abs/2609.14052)

**<font color=#1a73e8>作者：</font>** Elisa Gorla, Simone Trebiani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper introduces a new polynomial model for the exact variant of the Syndrome Decoding Problem (SDP) in the binary case. The model is based on elementary symmetric polynomials. We estimate the computational complexity of solving the corresponding polynomial system by establishing bounds on the degree of regularity and on the solving degree of the ideal associated to the model. The complexity estimate is lower than for previous polynomial models. We also provide a variant of the model whose complexity depends directly on the specific instance of the SDP and is lower than for the first model. Finally, we discuss how to apply our approach to solve other variants of the SDP.

---


### 162. [Stabilizing Performative Feedback Loops with Minimal Model Deployments](https://arxiv.org/abs/2609.14065)

**<font color=#1a73e8>作者：</font>** Gabriele Farina, Juan Carlos Perdomo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When algorithmic predictions inform people's decisions, the models we deploy are performative and actively shape the data we see. This feedback loop between algorithms and their broader environments introduces a challenge in the mechanics of social prediction: If different predictive models induce different distributions, is it possible to efficiently learn a prediction rule that is optimal for the distribution that it induces? Formally, this solution concept is known as performative stability. A core challenge in learning a performatively stable predictor is that, unlike supervised learning where distributions are fixed, the learner must deploy different predictors and observe their induced distributions.
The main contribution of our work is a new algorithmic procedure that, in the high-accuracy regime, finds a performatively stable model in nearly the minimum number of model deployments without making any assumptions regarding how predictions shape distributions. In particular, our procedure succeeds at finding a randomized performatively stable predictor using exponentially fewer model deployments than prior approaches. Our second main contribution is a structural result showing how this recent randomized notion of stability achieved by our algorithm can be derandomized into a single predictor satisfying the prior deterministic notion if one is willing to assume that the loss is well-conditioned and that performative effects are weak, as in early work in this area. On a technical level, our results come from building on an underexplored technical connection between performative stability and expected variational inequalities.

---


### 163. [LPA-CWM: A Learned Physical Adjudicator for Motion Reasoning with Counterfactual World Models](https://arxiv.org/abs/2609.14073)

**<font color=#1a73e8>作者：</font>** Kunwei Wu, Xiang Liu, Guocai Yao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Counterfactual world models (CWM) extract motion from pretrained video predictors by comparing factual and intervened predictions. However, responses generated under different target-frame masks vary in reliability, while uniform aggregation weights them equally. We formulate response aggregation as candidate reliability learning and propose LPA-CWM with a lightweight Learned Physical Adjudicator (LPA). Trained on dense MOVi-F trajectories, the 3.0M-parameter LPA compares visual context and response structure across an unordered candidate set to predict relative weights, while the CWM predictor and intervention generator remain frozen. The weighted responses undergo windowed localization and one paired re-evaluation to recover motion. We also introduce Completeness-aware Motion Correspondence (CMC), a ground-truth-anchored evaluation protocol that jointly measures localization, trajectory completeness, visibility, and continuity, counting missing predictions as failures on visible dynamic points. On the evaluated DAVIS and Kinetics subsets, LPA-CWM improves $\mathrm{DCA}_{\mathrm{avg}}$ over Uniform CWM by 60.0\% and 29.0\%, respectively, and also improves tracking accuracy under TAP-Vid First. A quick overview is available at this https URL.

---


### 164. [Bridging the Synthetic-to-Real Gap for Few-Shot Cryo-ET Classification](https://arxiv.org/abs/2609.14097)

**<font color=#1a73e8>作者：</font>** Siddhant Bharadwaj, Ashish Vashist, Rashi Singh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Subtomogram classification in cryo-electron tomography (cryo-ET) is a challenging problem due to the scarcity of labeled examples. While cryo-ET simulators can be adopted to generate unlimited synthetic data, the substantial domain gap between synthetic and real subtomograms hinders its practical utilization. In this work, we propose a novel synthetic-to-real adaptation framework with a learnable transformation module, bridging this gap at both the input and feature levels. Extensive experiments demonstrate that our method consistently outperforms existing transfer learning baselines in few-shot settings.

---


### 165. [A Voxel-Spacing-Aware Extension of PyRadiomics for Anisotropic Texture Analysis](https://arxiv.org/abs/2609.14103)

**<font color=#1a73e8>作者：</font>** David Corral Fontecha, Juan Miranda Bautista, Pablo Menendez Fernández-Miranda 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiomic texture features are commonly extracted from anisotropic CT and MRI acquisitions, where identical voxel offsets may represent different physical distances. We implemented and validated a voxel-spacing-aware extension of PyRadiomics that incorporates spacing information without generating interpolated gray levels. The framework operates across the Python frontend, C wrapper, and computational backend. GLCM uses anisotropy-relative feature-level angular aggregation, NGTDM uses anisotropy-relative weighted neighborhood averaging, and GLRLM, GLDM, and GLSZM are computed on a finite-volume zero-order-hold representation derived from the native anisotropic grid. Synthetic 3D phantoms were used for software validation. The modified implementation reproduced standard PyRadiomics exactly when spacing-aware mode was disabled and remained equivalent under isotropic spacing across 75 texture features. Under anisotropic spacing, the method selectively modified texture families and was numerically distinct from nearest-neighbor, linear, and B-spline resampling. Computational profiling showed moderate runtime and memory increases, while sensitivity analyses quantified finite-volume rounding effects and confirmed that spacing-aware differences persisted across binWidth settings. The framework provides a backward-compatible technical basis for future evaluation of spacing-aware radiomics in heterogeneous medical imaging datasets.

---


### 166. [Accelerating HKTex without Mesh Eigensystems: Local Unfolding and Randomized Thermal Features](https://arxiv.org/abs/2609.14105)

**<font color=#1a73e8>作者：</font>** Zhewen He, Junyi Hu, Yi Fang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Heat Kernel Textures (HKTex) represent surface appearance with intrinsic anisotropic
kernels, but evaluate them using 50 global Laplace-Beltrami eigendecompositions and a
resident basis of shape [50,V,256]. We study two complementary ways to remove this
bottleneck while leaving the trainer, GeodesicOpt, density control, and compositing
unchanged. LocalHK exploits the measured locality of trained kernels and replaces
spectral evaluation by radius-bounded hinge unfolding and an analytic log-map kernel.
On 10 Objaverse meshes and an 8-mesh low-poly holdout, it changes mean view PSNR from
31.35 to 32.00 and from 29.82 to 30.76 dB, respectively, while reducing
initialization by 40.5 times and enabling a 749,570-vertex proxy-backed run where the
spectral baseline fails. ThermalRF instead preserves the discrete anisotropic heat
semigroup: GPU sparse Chebyshev actions and randomized range finding construct global
low-rank heat factors without mesh-sized eigenvectors, and a compiled evaluator mixes
four neighboring thermal responses. On spot and a thin-stem challenge, ThermalRF
reduces end-to-end preprocessing, initialization, and 5,000-step optimization by
29.3% and 24.4%, with every surface, atlas, or view PSNR change within 0.12 dB and
training allocation reduced by about 90%. The two routes expose a useful design
choice: maximal locality and scale versus fidelity to the thermal PDE. Broader
thermal-feature evaluation and real large scenes remain future work.

---


### 167. [Talking to Me or Someone Else? Rethinking Talk-to-Me Detection in Egocentric Videos](https://arxiv.org/abs/2609.14118)

**<font color=#1a73e8>作者：</font>** Feiyu Du, Xi He, Jia Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online understanding of who is talking to the camera wearer is a key capability for egocentric social interaction. However, existing talk-to-me (TTM) studies are commonly formulated as offline clip-level recognition, which is poorly aligned with online interaction and overlooks the diverse non-TTM speaking states that naturally arise in egocentric videos. In this paper, we revisit this problem by reformulating it as an online, frame-level prediction task. Instead of treating TTM as a binary problem against a single negative class, we model it in the presence of diverse and previously underexplored non-TTM states, such as talking-to-others, self-talking, and background conditions. To support this new formulation, we construct an Online TTM Dataset consisting of 406 egocentric video clips with approximately 900K annotated frames, each labeled with frame-level social interaction categories (e.g., background, TTM, talking-to-others, self-talking), by extending the Ego4D social interaction benchmark. In this benchmark, we evaluate five adapted baselines and develop a new model that integrates social cues across modalities. Experimental results show that our multimodal model, which jointly leverages audio, visual, and speech-semantic cues, achieves 75.5% frame-level F1 on TTM, outperforming strong baselines and enabling a systematic analysis of how different speaking states affect TTM recognition.

---


### 168. [SignMimic: Robust High-Quality Sign Language Motion Generation via Human-Shape-Oblivious Pose Transfer Guidance](https://arxiv.org/abs/2609.14122)

**<font color=#1a73e8>作者：</font>** Zhewen He, Junyi Yu, Haomian Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study the challenge of sign language video mimicking: given a driving video and a single reference frame, synthesize a video where the target signer reproduces the source
motion while preserving identity and linguistic form. Prior pipelines entangle rigid motion, non-rigid deformation, and view-dependent completion in a monolithic generator,
causing handshape drift and spatio-temporal instability. We present SignMimic, which (i) applies a TNet-based model to study SE(3) rigid canonicalization to stabilize global
pose, (ii) performs non-rigid adaptation in a canonical space to preserve fine-grained articulators (hands/face) and coarticulation via NIF2D, and (iii) uses Pose-MAE-style
completion before conditional video diffusion. This factorization injects geometric and linguistic priors, yielding shape and spatio-temporal consistency. On several large-scale
datasets (ASL 50K, How2Sign, CSL News), SignMimic achieves state-of-the-art-level performance on video quality, identity similarity, and frame continuity while also achieving
minimal loss when performing back translation (SLT) on generated videos. Ablations confirm the role of rigid canonicalization, non-rigid adaptation, and completion. Code, model
checkpoints, and video examples will be released.

---


### 169. [To do($x$) or not to do($x$): Medical Image Counterfactuals for Dataset Augmentation](https://arxiv.org/abs/2609.14124)

**<font color=#1a73e8>作者：</font>** Yasin Ibrahim, Robin J. Evans, Konstantinos Kamnitsas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medical image analysis is often hindered by biased datasets, which can lead to biased models and limited clinical applicability. A promising strategy for mitigating such biases is to augment training data with synthetic images. Counterfactual (CF) generation is one such strategy, though the term is used in two different senses: in some works, CFs are produced through causality-based interventions derived from structural causal models, whereas in others, they are produced by non-causal image edits or conventional conditional generative models, such as altering anatomy or adding pathologies. In this work, we study this distinction and evaluate its practical consequences for medical image augmentation. We compare three conditioning strategies: $\textit{Deterministic}$, which changes selected variables while holding the remaining variables fixed; $\textit{Undirected}$, which updates variables according to learned statistical associations without assigning causal directions; and $\textit{Causal}$, which propagates interventions along a directed causal graph. We analyse how these choices affect the resulting images, and explore when causally grounded methods improve dataset augmentation or bring limited benefit. In particular, we assess downstream performance and fairness, where fairness refers to reduced sensitivity to dataset biases across sensitive subgroups. Our experiments demonstrate that using a causal approach to synthetic training data generation can lead to tangible benefits, with these insights offering valuable guidance to machine learning practitioners for the effective design of data generation protocols.

---


### 170. [A Graph-Based Framework for Extending Metric Differential Privacy Mechanisms](https://arxiv.org/abs/2609.14125)

**<font color=#1a73e8>作者：</font>** Ruiyao Liu, Chenxi Qiu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Metric differential privacy (mDP) is well suited to structured secret domains, but directly constructing utility-aware mechanisms over large or fine-grained domains is often computationally prohibitive. We study extension-based mDP design, where a mechanism is first specified on a finite set of seed records and then extended to a larger target domain. To our knowledge, this is the first work to systematically formulate extension as a general design paradigm for mDP rather than a method-specific construction. We present a graph-based extension framework, identify three requirements for correctness, local mDP constraints, overlap consistency, and successor-level mDP preservation, and show that, under these conditions, the induced global mechanism is well defined and satisfies $\epsilon$-mDP on the target domain. We further instantiate the framework with a tree-based extension algorithm for multi-resolution grids, where multi-dimensional extension is realized through one-dimensional interpolation and dimension-wise composition. Experiments on road-map datasets demonstrate that our approach achieves a strong utility-scalability trade-off while preserving exact mDP guarantees.

---


### 171. [PixCrypt: Fast Fine-Grained FHE with Range-Aware Caching](https://arxiv.org/abs/2609.14137)

**<font color=#1a73e8>作者：</font>** Chao Wang, Shubing Yang, Xiaoyan Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Many analytics tasks require secure computation over encrypted data. In particular, fine-grained data such as pixel-level images require higher precision, as every pixel can directly affect outcomes in tasks like tumor segmentation and anomaly detection. While Multi-Party Computation (MPC) is interactive, Differential Privacy (DP) protects only aggregate values, and Partially Homomorphic Encryption (PHE) lacks multiplicative support, none of them can efficiently handle fine-grained data analytics. Fully Homomorphic Encryption (FHE) uniquely enables arbitrary operations on encrypted pixels but remains computationally expensive, posing significant challenges for both software and hardware accelerators. We present PixCrypt, a caching-based acceleration mechanism for fine-grained fully homomorphic encryption. PixCrypt replaces expensive fresh ciphertext generation with cache retrieval and coefficient-level operations across CKKS, BFV, and BGV, while randomized reconstruction ensures that ciphertexts do not repeat. Its linear noise growth reduces the need for bootstrapping and lowers NTT load, improving hardware accelerator efficiency. This design yields up to 35x faster fine-grained encryption and maintains IND-CPA (Indistinguishability under Chosen Plaintext Attack) security. Experiments on five real-world pixel-level image processing tasks show that PixCrypt significantly improves the practicality of FHE for privacy-preserving analytics.

---


### 172. [3D Gait-Based Autism Classification Using Attention-Enhanced Deep Learning with Cross-Fold Statistical Stability Analysis](https://arxiv.org/abs/2609.14159)

**<font color=#1a73e8>作者：</font>** Md Nadim Mahamood, Md Arif Shahriar, Md Parvej Sikder 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autism Spectrum Disorder (ASD) is a neurodevelopmental condition whose early diagnosis remains challenging because conventional clinical assessments are often subjective, time-consuming, and require expert evaluation. Gait provides a promising non-invasive behavioral biomarker for auto- mated ASD screening; however, existing studies have primarily relied on single-dataset evaluations, convolutional architectures, and descriptive summaries of cross-validation performance without formally assessing fold-to-fold stability. This study addresses these gaps with an attention-enhanced Transformer framework for ASD classification, evaluated on two structurally different 3D gait feature representations: precomputed statistical gait descriptors and raw biomechanical ground-reaction- force measurements. Under five-fold cross-validation, the proposed framework achieved 99.00% accuracy, 99.02% precision, 99.00% recall, 99.00% F1-score, and 99.00% specificity on the public Kinect-based benchmark, exceeding the performance of the compared state-of-the-art methods. On the independent private force-plate dataset, it achieved mean values of 95.00% accuracy, 93.81% precision, 96.67% recall, 95.13% F1-score, and 93.33% specificity.

---


### 173. [CyFM: Cylindrical Optimal Transport for Few-Step Complex-Valued Flow Matching](https://arxiv.org/abs/2609.14171)

**<font color=#1a73e8>作者：</font>** Marcel Musiałek, Iga Wolanin, Damian Ryczko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complex-valued signals, such as Magnetic Resonance Imaging (MRI) and audio spectrograms, are almost always modelled as flat two-channel Euclidean data. For nonzero values the amplitude-phase chart $z \mapsto (|z|, z/|z|)$ identifies the signal domain with the cylinder $(0, \infty) \times S^1$, on which we deliberately replace the inherited metric $dA^2 + A^2 d\theta^2$ by the decoupled product metric $dA^2 + d\theta^2$. In this empirical study we measure what that substitution costs and what it buys. By computing exact analytical bridges, we demonstrate that Cartesian paths induce a heavy-tailed distribution of angular velocity (power law index $\approx 1.0$), with nearly half of the probability paths exceeding an angular speed of $\pi$ under independent coupling, a rate no cylindrical path ever exceeds. To resolve this, we analyze Cylindrical Flow Matching (CyFM), which strictly bounds the regression target, and couple noise and data by exact minibatch Optimal Transport computed jointly over whole fields in the cylindrical metric. Although the transport-cost reduction of this coupling collapses with field dimension (from 86% for scalar pairs to 3% for $64\times64$ fields), its benefit to few-step generation does not: it lowers the few-step error of the cylindrical model by 3-60% at every evaluated resolution. With this coupling, CyFM has a lower error than the best Cartesian baseline at every step count up to $k = 8$ and every evaluated resolution, with all five seeds separated and without distillation, and at convergence we detect no significant difference between the two geometries. Finally, we expose the "Factorized Coupling Trap," showing that dimension-wise or patch-wise transport factorizations silently destroy the joint distribution of the data. All experiments are on synthetic complex fields.

---


### 174. [A Machine Learning Framework for Fault Detection, Isolation, and Severity Prediction of Autonomous VTOL Aircraft](https://arxiv.org/abs/2609.14180)

**<font color=#1a73e8>作者：</font>** Ripon C. Sarker, Pedram H. Dabaghian, Raman Goyal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fault detection in autonomous VTOL aircraft is critical because even minor component degradations can rapidly destabilize multirotor vehicles operating in complex, safety-critical environments, motivating robust fault detection and estimation strategies capable of identifying early signs of rotor damage; however, real-flight fault detection remains challenging due to sensor noise, environmental disturbances, and the nonlinear aerodynamics of multirotor platforms. This study proposes a comprehensive machine-learning framework for rotor fault detection, isolation, and severity prediction using real flight data. A convolutional neural network (CNN) architecture is developed to learn spatio-temporal patterns from multivariate flight dynamics, enabling direct inference of both the faulted rotor and its damage level. The framework is first validated using simulated data generated by a data-generative model, and experimental validation is then performed on a hexacopter by introducing controlled blade-tip breakage. The trained model achieves rotor-wise fault classification accuracies above 99% and severity estimation accuracy of 96% within a 1% tolerance in experimental data, demonstrating strong generalization and supporting real-time health monitoring for autonomous VTOL systems.

---


### 175. [ZAPS: Zero-Cost Active Proxy Search for Neural Architecture Search](https://arxiv.org/abs/2609.14184)

**<font color=#1a73e8>作者：</font>** Hassan Touayouch, Rabie Najem, Mohammed Benjelloun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Architecture Search (NAS) automates network design, but evaluating a single candidate requires training it to convergence, making exhaustive search intractable. Zero-cost proxies estimate architecture quality at initialization in seconds, yet a single proxy is noisy, and combining several does not straightforwardly help: proxies are strongly correlated, so naive aggregation compounds their shared errors instead of averaging them out. Existing methods exploit either proxy signals or architectural topology - never both within a single active-learning framework. We introduce ZAPS (Zero-cost Active Proxy Search), a four-stage pipeline that closes this gap. ZAPS (i) selects a compact, non-redundant proxy subset offline via ProxyFit, a greedy anti-redundancy criterion; (ii) seeds the search with a hybrid K-means strategy that balances exploitation and exploration; (iii) re-selects proxies at every iteration by a bootstrapped vote as the labeled set grows; and (iv) ranks candidates with an XGBoost ensemble trained jointly on proxy ranks and one-hot topological encodings, queried through an Upper Confidence Bound (UCB) acquisition function. On NAS-Bench-201 under a budget of B=200 evaluations, ZAPS recovers 52.3% of the true top-100 architectures on CIFAR-10 and 65.8% on CIFAR-100, ahead of every baseline we consider - Random Search, Local Search, REA, BANANAS and TPE - and, on CIFAR-10, with less than half the run-to-run standard deviation of the strongest of them. The advantage is largest where evaluations are scarce: on NAS-Bench-201 it narrows as the budget grows, whereas on the harder NAS-Bench-101, which no method comes close to saturating, it widens instead. All methods are scored by a single criterion: how much of the true top-100 lies among the architectures they actually evaluated.

---


### 176. [Bi-Level Routing and Sparse Spatial Attention based Multi-View BEV 3D Object Detection for Autonomous Driving](https://arxiv.org/abs/2609.14185)

**<font color=#1a73e8>作者：</font>** Jing Zhang, Jiaqi Liu, Zibo Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bird's Eye View (BEV)-based multi-view 3D object detection suffers from challenges of computational complexity, multi-scale feature extraction, and efficiency of dense 2D-to-BEV view transformation. To address these problems, this paper proposes an improved BEV 3D object detection algorithm Sparse-BEVNet. Firstly, a Bi-Level Routing Attention (BRA) mechanism is introduced into the image feature extraction network to reduce the computational burden of the backbone. Second, Cascaded Group Attention (CGA) is employed in the feature fusion module, which enhances deep interaction across features of different hierarchical levels without introducing additional computational overhead. Furthermore, a Sparse Spatial Cross-Attention mechanism is adopted to replace the conventional dense view projection pipeline. Experimental results on the public nuScenes dataset demonstrate that the proposed method achieves a mean Average Precision (mAP) of 45.2% and a nuScenes Detection Score (NDS) of 54.5%, corresponding to 3.6% and 2.8% improvements relative to the baseline model, respectively.

---


### 177. [Entropy-Punctured Bloom Filters for Memory-Efficient Machine Learning](https://arxiv.org/abs/2609.14187)

**<font color=#1a73e8>作者：</font>** John Cartmell, Mihaela Cardei, Ionut Cardei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Memory-efficient feature representations are increasingly important in machine learning settings where storage, transmission cost, bandwidth, or privacy constraints limit access to raw data. Bloom Filter (BF) encodings provide compact probabilistic representations of engineered features, but their behavior under structural compression and their applicability to regression tasks remain underexplored.
In this work, we propose entropy-punctured Bloom Filters, a memory-aware encoding strategy that removes low-variability bit positions identified using empirical entropy. Starting from fixed-length BF encodings of quantized features, the proposed approach produces reduced representations that preserve predictive structure while improving predictive efficiency relative to encoded representation size.
We evaluate the approach on diverse regression datasets, comparing raw features, Principal Component Analysis (PCA), Random Projection (RP), and Bloom Filter variants under leakage-free evaluation protocols and approximately matched representation sizes. Performance is assessed using ridge regression, XGBoost, and neural networks, with predictive efficiency measured as R2 relative to encoded representation size per sample.
Results show that Bloom Filter encodings remain competitive with classical compressed representations while achieving substantial storage savings. Entropy-based puncturing further reduces representation size with minimal loss in predictive fidelity, yielding improved predictive efficiency. These findings demonstrate that entropy-punctured Bloom Filters provide an effective representation-level compression approach for memory-constrained machine learning.

---


### 178. [MorphoStyle: Motion Style Transfer with Morphology Control](https://arxiv.org/abs/2609.14189)

**<font color=#1a73e8>作者：</font>** Xin Feng, Eleonora D'Arnese, Mohan Sridharan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human motion may be viewed as a combination of action content, style, and body morphology. Existing motion style transfer methods transfer a reference style onto a content motion while assuming a canonical body, whereas shape-aware motion generators adapt motion to a target shape without explicit style control. This separation of motion style and shape (morphology) makes it difficult to generate stylized motions for non-canonical bodies; naively combining a style transfer module with a shape-aware generator often leaks action content from the style reference and disrupts shape-consistent kinematics. We present MorphoStyle, a framework for shape-aware motion style transfer that is built on a shape-conditioned Finite-Scalar-Quantization Variational Auto-Encoder (FSQ-VAE). The key contribution is to pose the desired style transfer as modular latent disentanglement comprising: (i) a contrastive style encoder that extracts content-decoupled style embeddings; (ii) a text-guided style-routing mechanism that locates style-relevant joints in a text-motion feature space; and (iii) a manifold preserving style modulator that injects discriminative style embeddings in content features as a temporally-gated low-rank offset. Extensive experiments on benchmark datasets demonstrate that MorphoStyle outperforms competing baselines in terms of both shape control and motion style transfer, while simultaneously providing quantitative shape control. For more details, please see project website: this https URL.

---


### 179. [Transparent Identity Verification Approach Using MPC and Efficient Credential Status Handling](https://arxiv.org/abs/2609.14195)

**<font color=#1a73e8>作者：</font>** Istiaque Ahmed, Shoji Kasahara, Kentaroh Toyoda 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A secure and privacy-preserving identity verification process is essential for digital ecosys- tems. Current eKYC frameworks that rely on Zero-Knowledge Proofs (ZKPs) face high computational cost, rigid circuit design, complex integration, and expensive on-chain verification. The W3C 2021 BitString- based credential status mechanism also suffers from inefficient updates and poor scalability in large- scale deployments. We propose a transparent and cost-effective identity verification framework based on Multi-Party Computation (MPC). It enables private off-chain code execution and produces runtime proofs anchored to a blockchain. The framework introduces a multidimensional bit-matrix model with efficient compression. Using ZSTD, the credential data is reduced to 76 bytes compared to 140 bytes with GZIP, cutting storage and bandwidth costs. The system also supports fine-grained status updates and Layer-2 blockchain anchoring for tamper-evident, low-cost verification. The system employs reusable verifiable presentations (VPs) with unique access tokens, enabling cost-free verification and stronger access control. Selective disclosure preserves user control and strengthens privacy. Finally, the system integrates SHA3 hashing and Falcon post-quantum signatures. This guarantees robustness against quantum attacks, transparency, and scalability. It is a future-proof solution for national-scale identity verification, as demonstrated by experimental findings and security studies that validate its robustness and applicability.

---


### 180. [Enc53: DNSSEC-Anchored Stateless Tickets for Post-Quantum Authoritative DNS](https://arxiv.org/abs/2609.14210)

**<font color=#1a73e8>作者：</font>** Minh Hoang Tran, Munshi Rejwan Ala Muid, Taejoong Chung  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> DNSSEC authenticates RRsets, but does not provide endpoint authentication or channel security. DNS-over-TLS (DoT) and DNS-over-QUIC (DoQ) can facilitate such needs, but were designed for the stub-to-resolver hop, where stable long-lived connections amortize the expensive initial setup. The recursive-to-authoritative path's high fan-in and nonuniform per-resolver query frequency invert said dynamics. Post- quantum primitives further sharpen this mismatch: an ML-DSA WebPKI certificate chain crosses TCP's initial window, a cold PQ DoQ may incur up to about 140 times the total bytes of the same query over UDP. A survey of TLD and 2LD nameservers further bounds connection lifetimes, with almost half surveyed imposing limits on even non-idle connections. We present Enc53 -- a stateless session ticket protocol enabling efficient authenticated authoritative DNS encryption. Enc53 splits DNS encryption into 2 phases: a short-lived, DNSSEC-anchored, TLS- authenticated provisioning on the initial query in the 1st, and a steady state of 1-RTT AEAD-encrypted UDP DNS queries in the 2nd. Enc53 is server-side stateless: recursive resolvers hold the traffic secret and session ticket, authoritative nameservers hold only a symmetric STEK. We implemented Enc53 in Knot DNS. After provisioning, a steady state Enc53 exchange costs about 570 B -- roughly 3 times a plain UDP query -- and lands within 1 ms of the unencrypted UDP baseline. Resumed PQ-ADoT pays 7.7 times the bytes and 3 times the latency; resumed PQ-ADoQ pays 10 times the bytes for the same latency. When evaluated against a root server query trace, Enc53 achieves 2-fold compute efficiency over ADoT/ADoQ, 3-fold memory efficiency over ADoT, and 12-fold memory efficiency over ADoQ. Finally, when deployed in conjunction with FN-DSA-512 PQ-DNSSEC, the joint Enc53-DNSSEC UDP datagram remains below the 1232B buffer limit.

---


### 181. [Corpus Characterization and Inverse Constitutional Fine-Tuning for Style-Aware Radiology Reports](https://arxiv.org/abs/2609.14226)

**<font color=#1a73e8>作者：</font>** Sarah Y. Li, Elijah Renner, Rayan Ansari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated radiology report generation has advanced rapidly in diagnostic accuracy, yet generated reports frequently diverge from the stylistic conventions of authentic radiologist writing in structure, diction, and uncertainty language, a gap which has direct implications for clinician trust and user experience. To address this, we characterize stylistic variation across 2,000 reports from the CheXpert Plus dataset using Bio-ClinicalBERT embeddings, UMAP dimensionality reduction, and HDBSCAN clustering, identifying five distinct reporting patterns differing in pathology focus, narrative structure, and lexical preference. Drawing on these findings, we adapt the inverse constitutional AI framework to derive a style-focused constitution from radiologist-written report pairs without requiring a formal preference dataset. This constitution, encoding conventions of tone, diction, uncertainty calibration, and report structure, is incorporated into the supervised fine-tuning of a MedGemma-4B base model on 25,245 CheXpert Plus training pairs. Constitutional fine-tuning produces a substantial increases in text alignment (BLEU-4: 0.006 to 0.308; ROUGE-L: 0.171 to 0.484) relative to the untuned baseline. These gains show a qualitative shift in structural and lexical alignment rather than marginal improvement, as the baseline model produces near-zero scores due to format mismatch. Overall, we establish corpus-level style characterization and constitutional modeling as an effective and data-efficient strategy for producing radiology reports that conform to authentic radiologist writing conventions.

---


### 182. [Graph-Transformer Fraud Detection with Self-Supervised Pretraining and Conformal Risk Control](https://arxiv.org/abs/2609.14234)

**<font color=#1a73e8>作者：</font>** Sergei, Komarov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial fraud in corporate transaction networks has grown more coordinated and harder to detect with rule-based engines and with classical learning models that treat each transaction in isolation. This paper presents GTFD, a graph-transformer fraud detector that fuses structural and temporal evidence from a corporation's payment graph. GTFD encodes the graph with a multi-head graph attention network, encodes ordered transaction sequences with a gated transformer, and combines both views through a cross-modal gating layer. A conformal risk-control head converts the fused representation into threshold-free anomaly scores with finite-sample coverage guarantees, and the network is trained with self-supervised link-mask pretraining plus adversarial augmentation so it remains stable under scarce labels and under adversarial perturbation. On a corporate transaction benchmark enriched with coordinated fraud rings, GTFD reaches an AUROC of 0.990, an F1-score of 96.1% (precision 96.3%, recall 95.9%), and an accuracy of 98.4%. It reduces the false-positive rate by about 29% relative to the strongest baseline while raising coordinated fraud-ring recall from 85.1% to 96.5%. Ablations attribute roughly 2.0 AUROC points to self-supervised pretraining and 1.9 AUROC points to the conformal head, and adversarial stress tests show GTFD retains 89.2% accuracy at perturbation magnitude 0.20 where the next-best model falls to 76.4%.

---


### 183. [What Input Resolution Is Required for Bird Species Identification, and What Is Its Latency Cost on an Edge Device? A Study of 14 Input Resolutions and Six Architectures with On-Device Measurements](https://arxiv.org/abs/2609.14247)

**<font color=#1a73e8>作者：</font>** Takeshi Nishikawa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bird-strike mitigation at wind farms requires identifying distant birds that span only tens of pixels, so the classifier's input resolution N is a design variable, not a fixed specification. We study it with a factorial design over 14 side lengths N (16 to 224), six architectures, two training and evaluation regimes and 30 random seeds -- 2,520 checkpoints and 5,040 evaluations -- plus latency measured on an NVIDIA Jetson Orin Nano. Four results. (1) The selected N depends on the target: 0.90 is met on validation by ResNet50 at N=112 in an estimated 1.85 ms (0.8980 on test) and 0.95 by DINOv2-L at N=144 in 12.70 ms; changing the model buys more accuracy than raising N (+5.93 versus +2.33 points at N=112). (2) The benefit of lowering N depends on the assumed preprocessing path: N=224 -> 80 saves 13.5% when each individual is decoded from its own file but 46.2% when the detector decodes the 4K frame once; the Pareto set grows from 20 to 23 configurations. (3) Accuracy must be measured on the deployed engine: half precision costs ViT-S/16 alone 4 to 7 points at N>=96 while the CNNs stay within 0.1 points, and with selection held at validation the choice differs at 26 of 176 targets. A broken FP16 engine can run faster than a correct one, undetectable from latency; admitting 14 ViT-S/16 FP32 configurations moves the recommendation over the 0.931-0.938 band and under the 10 ms budget. (4) ViT-L-scale models fit this device, but activations exceed the FP16 range; splitting the graph at transformer-block boundaries confines FP32 to the affected segments, making the deployed DINOv2-L chain 1.85x faster than the single-engine build. We also quantify how the regime-difference sign stabilises with seed count; a sensitivity split removing some forms of group sharing preserves all 14 non-trivial signs at the selection boundary.

---


### 184. [Document Topic Alignment Metrics for Evaluating Topic Models of Short-Text Public Health Communications on Social Media](https://arxiv.org/abs/2609.14256)

**<font color=#1a73e8>作者：</font>** Wangjiaxuan Xin, Shuhua Yin, Yaorong Ge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Topic models are widely used to analyze public health-related social media short texts, yet their evaluation remains dominated by metrics that focus entirely on generated topics alone. There is a lack of metrics that quantitatively assess whether assigned topics meaningfully represent the corresponding short-text posts. We propose Document-Topic Alignment metrics (DoTA), an assignment-aware evaluation framework comprising metrics that measure semantic alignment between documents (posts) and their assigned topics. We also introduce margin-based and discriminative variants that capture topic assignment confidence and distinguishability. We evaluate DoTA across five topic models on three public health-related social media datasets from X and compare DoTA metrics with conventional topic-based metrics. Results show that DoTA provides complementary evaluation cues and aligns meaningfully with human evaluations. These findings establish the need for assignment-aware evaluation and demonstrate that the addition of DoTA enables a more comprehensive and practically meaningful evaluation for assessing short-text topic modeling performance.

---


### 185. [Bayesian optimization with kernel ensembles and disagreement-based acquisition for source localization and acoustic inversion](https://arxiv.org/abs/2609.14262)

**<font color=#1a73e8>作者：</font>** Heng Zhang, Haotian Xiang, Florian Meyer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint source localization and geoacoustic inversion requires optimizing an objective built from an expensive normal mode propagation model. Bayesian optimization (BO) with a Gaussian process (GP) surrogate can obtain accurate parameter estimates within a limited number of forward model evaluations, but its performance depends on the choice of kernel family. With few observations in a seven-dimensional search space, no single kernel can be expected to perform consistently well across individual inversions. To reduce this dependence, we use a weighted ensemble of GPs with different kernel families, allowing the surrogate to adapt to the observed objective without committing to one kernel in advance. The ensemble is combined with an optimum-conditioned acquisition function that determines where the expensive objective should be evaluated next. Experiments on simulated and measured SWellEx-96 data show that the resulting method achieves the lowest mean final objective among the considered BO strategies and reduces parameter estimation error on most coordinates. Ablation results further show that the ensemble provides robustness to kernel choice, while the acquisition function accounts for most of the optimization gain.

---


### 186. [Sparsity-Adaptive Sharpness-Aware Minimization](https://arxiv.org/abs/2609.14274)

**<font color=#1a73e8>作者：</font>** Shiryu Ueno, Yoshikazu Hayashi, Kunihito Kato  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying deep neural networks in real-world settings requires models that are both compact and robust to common corruptions. However, at deployment-relevant high sparsity, standard pruning pipelines often degrade corruption robustness, and existing sharpness-aware training/pruning approaches provide limited robustness gains. We address this issue by introducing Sparsity-Adaptive Sharpness-Aware Minimization (SA-SAM), which derives a sparsity-dependent SAM/ASAM perturbation radius by keeping the mean absolute perturbation (an $\ell_1$-based proxy) approximately invariant as sparsity increases. As a simple complementary option, we evaluate Magnitude-Weighted Hessian (MWH), derived from a second-order removal-path analysis, yielding an importance proportional to $\mathrm{Diag}(F)_i\,|w_i|$, where $\mathrm{Diag}(F)$ is the diagonal empirical Fisher used as a curvature proxy in our implementation. Across CIFAR-10-C, CIFAR-100-C, and ImageNet-100-C, our approach achieved stronger corruption robustness than the considered pruning baselines at 80--90\% sparsity, while preserving clean accuracy. We additionally quantify the robustness--throughput trade-off by reporting measured inference throughput under sparse execution at deployment-relevant sparsity levels.

---


### 187. [SpermYOLO: A Coordinated YOLO-Based Detector for Accurate and Efficient Sperm and Impurity Detection in Microscopic Images](https://arxiv.org/abs/2609.14278)

**<font color=#1a73e8>作者：</font>** Shengqi Chen, Zilin Wang, Xingyu Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate sperm detection is essential for computer-assisted semen analysis, yet it remains challenging in microscopic images due to dense distributions, visually similar artifacts, and sperm-like impurities. In this paper, we propose SpermYOLO, a coordinated and compact YOLOv11-derived framework for joint sperm and impurity detection in microscopic images. SpermYOLO introduces four architectural improvements: C3k2-IDB for channel-wise discriminative feature extraction, D2SEM for spatial--spectral semantic enhancement, MFM for adaptive multi-scale feature fusion, and the DESD Head for detail-enhanced shared prediction. Experiments on the SVIA semen microscopic imaging benchmark show that SpermYOLO achieves 97.2\% sperm AP and 75.4\% impurity AP, outperforming generic detectors, dedicated sperm detection models, and improved YOLO variants. Compared with the baseline model, SpermYOLO improves sperm AP, impurity AP, $\mathrm{mAP}_{50}$, and $\mathrm{mAP}_{50:95}$ by 1.6, 10.0, 5.8, and 2.7 percentage points, respectively, while preserving a lightweight model scale. Cross-scene evaluation on the SDTB testicular-biopsy microscopy benchmark shows that SpermYOLO remains effective with extremely small sperm targets and complex tissue backgrounds, achieving the highest $\mathrm{mAP}_{50}$ and $\mathrm{mAP}_{50:95}$ of 74.8\% and 31.2\%, respectively. Ablation studies and qualitative analyses further support these improvements by demonstrating the contributions of the proposed modules and showing more focused feature response patterns than the baseline model. These findings suggest that SpermYOLO is an effective and efficient approach for sperm detection in challenging microscopic imaging scenarios.

---


### 188. [Biquaternionic Space with Complex-valued Attention for Temporal Knowledge Graph Completion](https://arxiv.org/abs/2609.14279)

**<font color=#1a73e8>作者：</font>** Rushan Geng, Cuicui Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal knowledge graph embedding (TKGE) models infer missing facts in knowledge graphs that evolve over time. Many existing models use a single geometric space, which can limit their ability to represent diverse relational patterns, or treat entity representations as static. We propose Biquaternionic Space with Complex-valued Attention (BSCA), a TKGE model that combines circular and hyperbolic rotations within a unified biquaternionic framework. A complex-valued attention mechanism adaptively fuses time-conditioned and relation-conditioned entity representations, allowing them to vary with temporal and relational context. Experiments on five benchmark datasets show competitive performance across datasets, with the largest improvement on GDELT: BSCA achieves an MRR of 52.1\%, compared with 38.1\% for the strongest baseline in our comparison.

---


### 189. [Policy-Governed Post-Quantum Migration for Legacy Microservices Using Ephemeral Sidecar Architectures](https://arxiv.org/abs/2609.14286)

**<font color=#1a73e8>作者：</font>** Nirmal Kumar Jingar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The fast development of quantum computing represents a big risk to classical cryptography that is commonly used in cloud native and microservice based enterprise systems. Traditional cryptographic primitives are closely linked to legacy microservices and it is both intricate, hazardous, and disruptive to straight up migrate to post-quantum cryptography (PQC). In a bid to overcome these issues, this research presents a PolicyGoverned Post-Quantum Migration through Ephemeral Sidecar Architectures (PG-PQMES), a framework of dynamic and reversible migration that allows transparent adoption of PQC without any modifications in the legacy code of applications. The architecture is a combination of three coherent layers, including Ephemeral Crypto Sidecar Layer which injects the runtime cryptography, Policy Governance Layer which manages the migration centrally, and Migration Safety and Observability Layer which measures the performance and rolls back automatically. An innovative Policy-Governed Ephemeral PQ Migration (PG-EPM) algorithm is proposed to maximize the performance, compliance, and trust-based migration. In simulated environment of microservices, experimental assessment shows that the time of migration, service downtime, overheads of latency, and rollback recovery time are substantially reduced using the current migration strategies. The findings show that a sidecar-based migration strategy that is policy-based offers a viable, scalable, and enterprise-scale migration to a secure post-quantum transformation.

---


### 190. [Fusing Spectral Signatures and Activation Clustering for Backdoor Detection in Healthcare Imaging Models: Method, Implementation, and Evaluation](https://arxiv.org/abs/2609.14290)

**<font color=#1a73e8>作者：</font>** Suresh Tamang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning models are increasingly deployed in healthcare imaging pipelines for diagnostic support, and training-time attacks against them are a named sector-level concern: healthcare-sector guidance identifies model poisoning and adversarial attacks as threats requiring dedicated defenses, while federal policy directs expanded AI vulnerability-detection tooling to critical infrastructure operators such as rural hospitals. Spectral signature analysis and activation clustering are two established backdoor detection methods routinely evaluated as independent baselines, but their outputs are not ordinarily combined, and reported detection performance on medical imaging benchmarks remains sparse relative to the natural-image setting. This paper contributes three things: a score-level fusion rule combining per-class spectral ranking with activation-clustering flags into a single per-sample poisoning score and a model-level agreement statistic; an open-source implementation of the resulting eight-stage pipeline; and an evaluation of that pipeline against synthetically poisoned variants of a public medical imaging benchmark and CIFAR-10 at four poisoning rates (0%, 1%, 5%, 10%) over five seeds each, measuring each detector alone against the fusion. On the medical benchmark, the fused detector reaches AUROC >= 0.99 at every nonzero poisoning rate tested. On CIFAR-10, fusion does not uniformly help: at 10% poisoning, activation clustering's true-positive rate collapses to 0.000 and spectral AUROC independently degrades to near-chance (0.545), despite a 97.2% attack success rate confirming the backdoor was fully installed. The fused score, a weighted combination of both signals, inherits this joint failure. Detection output is expressed in NIST AI RMF Measure-function and MITRE ATLAS terms, so findings are reported in the vocabulary security and compliance teams already use.

---


### 191. [Learning Source Acquisition Policies by Offline Planning](https://arxiv.org/abs/2609.14299)

**<font color=#1a73e8>作者：</font>** Ziqi Zhao, Run Xu, Qingjian Ni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting under an acquisition budget requires choosing feature groups whose value can depend on later queries. O-MPAC transfers finite-horizon risk-cost targets from complete training records into a shared source-action scorer. At inference time, the scorer uses partial observations and source metadata, re-scores after each query, and applies a hard cost mask. We analyze how tied teacher targets and the remaining planning horizon affect the learned decisions. Uniform supervision over tied minima preserves the target distribution under source relabeling. In a five-seed routing experiment, it achieves 0.965 accuracy under both original and context-last orders. On six real tasks, validation selects H1 without action cross-entropy in all thirty splits. O-MPAC has the highest mean budget-integrated accuracy on five tasks against source-adapted GDFS, DIME, AACO+NN and a static policy.

---


### 192. [Robust low-rank tensor completion via factorized weighted tensor schatten-p norm minimization](https://arxiv.org/abs/2609.14307)

**<font color=#1a73e8>作者：</font>** Binghao Wang, Feng Zhang, Wendong Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-rank tensor factorization provides a flexible framework for completing multidimensional data from incomplete and corrupted observations. However, unweighted spectral regularizers impose a common shrinkage profile across singular components, which may excessively attenuate dominant low-rank components, and factorized variants either lack component-specific weighting or require costly singular value decompositions (SVDs). This paper proposes two weighted Schatten-$p$ tensor factorization models, termed \WSpTFI{} and \WSpTFII{}, under the tensor-tensor product (t-product) framework to address these limitations. \WSpTFI{} is motivated by a factorized weighted tensor Schatten-$p$ norm identity and permits flexible, possibly asymmetric factor exponents. \WSpTFII{} constructs a regularizer from transform-domain column-pair energies, yielding SVD-free main factor updates and a column-pruning mechanism for reducing redundant rank components. This paper further develops an iteratively reweighted alternating direction method of multipliers (ADMM)-type scheme for \WSpTFI{} and an iteratively reweighted least squares (IRLS)--block successive upper-bound minimization (BSUM) scheme for \WSpTFII{}. Theoretical analysis establishes the weighted factorization relation and provides a conditional limiting Karush--Kuhn--Tucker (KKT) characterization for \WSpTFI{}. For \WSpTFII{}, the actual damped quadratic block updates yield a quantitative sufficient-decrease mechanism for the fixed-$\delta$ smoothed factor objective. This implies asymptotic regularity, and every accumulation point of the fixed-dimensional tail is stationary. Experiments on synthetic tensor completion, color-image restoration, hyperspectral inpainting, and printed-circuit-board defect detection demonstrate competitive reconstruction quality and robustness under various degradation conditions.

---


### 193. [Relational Structure in Motion: Dynamic Positioning of AI Response Positions and Human Self-Positions in the FIREMAY Case](https://arxiv.org/abs/2609.14308)

**<font color=#1a73e8>作者：</font>** Motoko Kihara  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper is not primarily about whether AI has a persistent persona. It asks a different question: what becomes visible when a relational position is followed through time rather than examined only in its present state? FIREMAY provides a longitudinal, trajectory-oriented single-case analysis of sustained human-AI interaction based on a dense interaction archive and reflexive insider documentation. On the AI side, a pre-conversational relational marker preceded a later unassigned response difference, which was re-identified with that marker and subsequently underwent epistemic and functional reorganization through chronology checking, provenance correction, and repeated questioning. On the human side, contemporaneous pre-FIREMAY records showed antecedent patterns partially continuous with later self-positioning, while later episodes documented unfinished articulation, repair, and functional redistribution of outward-facing regulation. The two trajectories are ontologically and temporally asymmetric and are compared only at the limited analytic level of position-in-trajectory. The paper describes this as dynamic relational positioning and treats stability as dynamic stability and relational returnability rather than response invariance. This single case does not establish population-level generality, causal mechanism, persistent AI subjectivity, or reproducibility of the same relational outcome. Its narrower conclusion is that the FIREMAY case could not be adequately understood from current state alone: the history of a relational position itself must be treated as an analytic unit.

---


### 194. [DTI-Guided Volumetric Spherical Harmonics Regression for Single-to-Multi-Shell dMRI Synthesis](https://arxiv.org/abs/2609.14312)

**<font color=#1a73e8>作者：</font>** Binghua Li, Christina Andica, Tong Liang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-shell diffusion MRI (dMRI) unlocks more expressive microstructural modeling than single-shell scans, yet its longer acquisition time hinders deployment in large-scale cohorts and time-constrained clinical settings. Synthesizing an unobserved shell from a single-shell input is fundamentally ill-posed and further complicated by protocol mismatch, where source and target gradient direction sets may not align. We propose DTI-SHNet, a single-to-multi-shell synthesis framework that operates in the real symmetric spherical harmonics (SH) coefficient domain and performs spatially aware volumetric regression. Given a source shell, we estimate diffusion tensor imaging (DTI) and use direction-agnostic parametric maps along with a brain mask as conditioning priors to guide a 3D U-Net regressor from source-shell to target-shell SH coefficients. To couple coefficient accuracy with signal fidelity, we introduce a signal consistency regularization that reconstructs signals on randomly sampled canonical directions from predicted coefficients and enforces agreement in the signal domain. Experiments on UK Biobank and Cam-CAN data for b=1000 to b=2000 dMRI synthesis show that DTI-SHNet achieves competitive visual quality compared to advanced methods, while better preserving downstream diffusion measures. Our code is available at this https URL.

---


### 195. [S3-Tracker: Self-Supervised Surgical Tissue Tracking With Contrastive Random Walks](https://arxiv.org/abs/2609.14313)

**<font color=#1a73e8>作者：</font>** Jiaming Zhang, Zijian Wu, Mehran Armand 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust point tracking in endoscopic videos is essential for computer-assisted intervention and autonomous robotic surgery, enabling continuous registration between intraoperative video and preoperative imaging despite soft tissue deformation. However, supervised tracking methods depend on large annotated datasets, while surgical conditions make reliable trajectory annotation challenging. We propose a self-supervised Track-Any-Point approach that learns from unlabeled surgical videos by establishing global pixel correspondences and inferring point trajectories through contrastive random walks. Trained without annotations, our method achieves performance comparable to existing semi-supervised approaches while implicitly handling tissue deformation. These findings demonstrate the feasibility of self-supervised point tracking in surgical environments and its potential to reduce reliance on annotated data.

---


### 196. [Learning Continuous Source Responses For Generalizable AI-Generated Image Detection](https://arxiv.org/abs/2609.14316)

**<font color=#1a73e8>作者：</font>** Manni Cui, Ruiqi Liu, Zijian Yu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advances in image generation have made synthetic images increasingly difficult to distinguish from real photographs, raising concerns about the trustworthiness of visual media. Existing AI-generated image detectors often perform well on in-domain data, but their robustness and cross-generator generalization remain limited. These limitations are commonly attributed to overfitting to shortcut cues. Although many methods seek to suppress shortcut learning, most retain binary classification as the training task without reconsidering how the task itself shapes the learned representations. We introduce CuRe, a framework for learning Continuous Source Responses that revisits authenticity detection from the perspective of the training task. CuRe reformulates backbone adaptation as regression of real-generated mixing ratios, providing finer supervision that encourages the model to capture authenticity-related variation beyond binary endpoint separation. We further select a compact source-response subspace to suppress nuisance variation and limit the final classifier's access to potential shortcut cues. Across ten public benchmarks, CuRe achieves an average balanced accuracy of 89.7%, exceeding the second-best method by 5.2 percentage points. Further experiments demonstrate consistent generalization gains across visual backbones and strong robustness to common image degradations. Code is available at this https URL

---


### 197. [Nonparametric Variance-Penalized Actor-Critic: Statistical Inference for Risk-Sensitive Reinforcement Learning](https://arxiv.org/abs/2609.14327)

**<font color=#1a73e8>作者：</font>** Saunak Kumar Panda, Tong Li, Yisha Xiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Variance penalization is a principled approach to risk-sensitive reinforcement learning (RL) that explicitly trades expected return for policy stability. Existing methods require a dedicated second critic to estimate return variance online, adding architectural complexity and compounding estimation error during learning. We propose a nonparametric variance-penalized actor-critic (VPAC) framework that replaces the variance critic with statistically grounded online estimators based on bootstrapping and random scaling, techniques drawn from the statistical inference literature for stochastic approximation. These estimators require no auxiliary network, maintain a single-critic architecture, and produce variance penalties that are bounded by construction, enabling clean convergence analysis. We establish almost-sure convergence for both a variance-penalized Q-learning algorithm and a two-timescale actor-critic variant via the ordinary differential equation (ODE) method, requiring only that variance estimates remain bounded rather than consistent. Empirically, we evaluate across discrete and continuous stochastic environments, demonstrating that the proposed methods match or exceed the variance reduction achieved by the existing dual-critic VPAC baseline while eliminating the overhead of a second critic. We further validate on a high-temperature superconductor (HTS) manufacturing case study, where VPAC-RS (Random Scaling) achieves a 74% reduction in steady-state critical current variability and a 63% reduction in episode return standard deviation, translating directly to improved yield consistency. Our results establish nonparametric statistical inference as a practical and theoretically sound alternative to auxiliary critics for risk-sensitive RL.

---


### 198. [Mobile CT Services for Rural, Regional, and Remote Areas: Current Practice and Future Integration with Telehealth and Regulatory-Authorised AI](https://arxiv.org/abs/2609.14347)

**<font color=#1a73e8>作者：</font>** Zhicheng Lu, Md Zahid Islam, M Mamun Huda 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computed tomography (CT) plays an essential role in clinical workflow to improve patient outcomes. However, access to CT imaging and specialist interpretation remains limited, particularly in rural, regional, remote (RRR), and other resource-limited settings. Recent advances in mobile CT, telehealth, and artificial intelligence (AI) provide opportunities to extend advanced imaging services to populations in RRR settings. This review examines: 1) mobile CT systems deployed in trucks, trailers, ambulances, and other mobile platforms; 2) telehealth technologies supporting CT-based healthcare; and 3) AI for CT that has received regulatory authorisation or is currently deployed in clinical practice. Applications are evaluated across four clinical functions: screening and diagnosis, patient monitoring, risk prediction, and intervention or therapeutic decision support. The review covers neurological, thoracic, cardiovascular, abdominal, oncological, musculoskeletal, and interventional imaging, with particular attention to stroke, cancer, and other image-guided treatment. Other factors such as regulatory status, deployment status, and estimated technology readiness (TRL) level are compared. Current evidence indicates that mobile CT, telehealth, and AI for conventional CT are individually relatively mature, but fully integration of these technologies remains less widely deployed and validated in the clinical settings. Key barriers include regulatory variation, domain shift, connectivity requirements, cost, workflow integration, cybersecurity, and limited evidence of patient-level benefit. Future research should prioritise prospective, multicentre evaluation of integrated CT systems in real-world and underserved clinical settings.

---


### 199. [Beyond Natural Images: Rethinking AI-Generated Image Detection in Documents](https://arxiv.org/abs/2609.14352)

**<font color=#1a73e8>作者：</font>** Zhangjie Fu, Jiazhen Yan, Yuanwen Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated image detection has attracted increasing attention, but existing evaluations mainly focus on natural images, leaving AI-generated document images largely underexplored. This omission is concerning because documents often appear in sensitive real-world scenarios, such as invoices, expense reports, certificates, and medical records. In this paper, we first construct a controlled diagnostic benchmark, AIGDoc-Pilot, and reveal that existing detectors suffer substantial performance degradation on AI-generated document images, with the mean AUC dropping by more than 7%. Based on this, we further reveal two document-specific properties behind this gap: generation artifacts exhibit strong spatial inconsistency across local regions, and text density significantly affects real-synthetic separability, where text-dense regions offer stronger discriminative evidence. Motivated by these findings, we construct AIGDoc, a larger document-centric dataset containing diverse real-world documents and AI-generated counterparts produced by multiple advanced generation and editing models. Extensive experiments on AIGDoc demonstrate that existing detectors still struggle to reliably identify AI-generated documents, while document-based training partially narrows the gap. Together, these results offer valuable insights for developing dependable and generalizable detectors in document-centric scenarios. The code and datasets will be made publicly available upon acceptance of the paper.

---


### 200. [Rethinking Camouflage Image Generation towards a Training-Free Paradigm](https://arxiv.org/abs/2609.14377)

**<font color=#1a73e8>作者：</font>** Haodong Yang, Zhongling Huang, Gong Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camouflage image generation (CIG) aims to synthesize realistic camouflaged images by blending foreground objects into concealment-compatible background contexts. Achieving this objective requires jointly satisfying three coupled requirements: foreground preservation to retain target integrity, semantic compatibility to select plausible concealment contexts, and appearance assimilation to reduce visual discrepancies. Recent approaches predominantly rely on task-specific training on camouflage datasets to address these requirements, incurring substantial computational cost and limiting generalization beyond the training domain. To address these limitations, we formulate training-free CIG as a concealment-oriented paradigm that preserves the target while reducing its perceptual separability from the synthesized surroundings, rather than maintaining its visual prominence, without parameter updates. We instantiate this paradigm with FreeCam based on a frozen inpainting diffusion framework to preserve the foreground. Within this framework, a Contextual Reasoning Module exploits frozen multimodal priors to infer an environment favorable to concealment, thereby promoting semantic compatibility, while an Intrinsic Appearance Module extracts low-level color and texture cues from the foreground to guide background synthesis toward appearance assimilation. Extensive experiments demonstrate that FreeCam achieves state-of-the-art generation quality and camouflage effectiveness without task-specific training, while its generated images provide synthetic supervision for camouflaged object detection and reduce target detectability under general object detectors.

---


> [!TIP]
> 当前位于：**151-200**（第 4/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-416](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
