# 📦 其他研究 | 2026年07月08日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 1. [Learning 3D Affordances for Blade Insertion in Cluttered Stowing](https://arxiv.org/abs/2607.02549)

**<font color=#1a73e8>作者：</font>** Tianyu Li, Harpreet Sawhney, Minju Jung 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many manipulation tasks require reasoning about free-space affordances: discovering volumes where an extended rigid tool can safely navigate, complementary to surface contact affordances for grasping. Robotic stowing is a canonical instance, where a blade must sweep items aside inside cluttered fabric bins to create insertion space. Production stow systems generate millions of such episodes, but standard approaches with unimodal data infer affordances as SE(3) pose distributions, a geometric question asked in the wrong domain. VulcanVoxel keeps inference spatial: a masked autoencoder over 3D occupancy fields reconstructs blade occupancy conditioned on scene geometry, computing feasibility locally at each voxel and recovering multi-modal predictions from unimodal data. Blade affordances are spatial objects, subsets of 3D space defined by geometric feasibility. Pose parameters carry no structure for reasoning whether unobserved placements are feasible, and standard generative objectives including flow matching faithfully learn the unimodal distribution produced by execution policies and cannot recover geometric alternatives. Trained on 10,000 real warehouse stow episodes without human annotation, VulcanVoxel achieves top-5 coverage of 0.89 versus 0.71 for the best pose-based baseline, with a distilled student providing RGB-to-voxel inference in 30 ms. vs. 1.4 s. for voxel-to-voxel. We have released a dataset of real blade insertion cycles with RGB-D observations and pose trajectories at this https URL. html.

---


### 2. [Interpretable machine learning predicts Parkinson's disease severity using motion-corrected QSM MRI and multiband multiecho fMRI features](https://arxiv.org/abs/2607.02553)

**<font color=#1a73e8>作者：</font>** Aixa X. Andrade  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Introduction: Objective neuroimaging biomarkers may improve Parkinson's disease motor assessment by capturing brain variation not directly observable from clinical examination. We used interpretable machine learning to predict current motor severity, measured by MDS-UPDRS Part III, from QSM and multiband multi-echo resting-state fMRI-derived ReHo features.
Methods: Regional QSM and ReHo features were extracted from 28 participants, including 24 individuals with Parkinson's disease and 4 controls. Thirteen feature-set experiments evaluated imaging-only, clinical-only, imaging-plus-clinical, full, reduced, and multimodal inputs. Support vector regression, Elastic Net, Random Forest, and XGBoost models were trained using nested cross-validation. Performance was assessed using pooled held-out R^2, RMSE, MAE, Pearson correlation, permutation testing, and the proportion of participants predicted within +/-5 MDS-UPDRS Part III points.
Results: Imaging-only models carried meaningful predictive signal, whereas the clinical-only model performed weakly. Full fMRI, full QSM, and clinical variables provided the strongest global fit, explaining 45.4% of variance in motor severity. Selected QSM plus clinical variables produced the most clinically close predictions, with 75.0% of participants predicted within +/-5 points and the lowest MAE among top-performing models. SHAP highlighted cerebellar, thalamic, striatal, insular, and motor cortical features.
Conclusion: QSM and multiband multi-echo fMRI-derived ReHo capture distinct, interpretable dimensions of Parkinson's disease motor severity. These findings show that structural and functional imaging contribute differently depending on the clinical prediction goal.

---


### 3. [Reliability-Aware Monocular Depth Supervision for Sparse-View Neural Reconstruction](https://arxiv.org/abs/2607.02554)

**<font color=#1a73e8>作者：</font>** Wei-Teng Chu, Yashasvini Gopalan, Changju Yuan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-view neural reconstruction is challenging in outdoor driving scenes, where cameras usually move along a narrow forward-facing trajectory and provide limited multi-view overlap. Although monocular depth estimators can provide dense geometric priors, their predictions are noisy, and not uniformly reliable across image regions. In this work, we study monocular depth supervision for sparse-view neural reconstruction. We use Depth Anything V2 as a dense monocular depth prior, align its predictions to metric depth using scale-shift fitting, and apply depth supervision selectively through photometric masks generated from an RGB-only baseline model. We evaluate this strategy on two representative scene representations: Mip-NeRF-360 and Splatfacto. On KITTISeq02 under an every2 sparse-view setting, masked monocular depth supervision gives only marginal rendering gains for Mip-NeRF-360 and does not improve metric geometry. In contrast, Splatfacto benefits more clearly, improving PSNR from 14.903 to 15.932 and reducing RMSE from 0.542 to 0.100. Additional KITTISeq05 experiments and matched-ratio mask ablations further show that the gains for Splatfacto come from selecting reliable low-error regions rather than simply reducing the number of depth-supervised pixels. Additional experiments on the Bicycle scene show that depth supervision can improve geometry while hurting RGB rendering quality when multi-view coverage is already strong. Overall, our results suggest that monocular depth priors are useful for under-constrained sparse-view reconstruction, but should be applied selectively and with moderate weighting.

---


### 4. [Do Diabetic Foot Ulcer Segmentation Models Generalize? A Cross-Dataset Benchmark of CNN and Transformer Architectures](https://arxiv.org/abs/2607.02555)

**<font color=#1a73e8>作者：</font>** Abderrahmane Benfatah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for diabetic foot ulcer (DFU) segmentation routinely report high accuracy, but they are almost always trained and tested on the same dataset, leaving their behaviour on data from a different clinical source largely unmeasured. We benchmark three representative segmentation architectures -- U-Net and DeepLabV3+ (convolutional) and SegFormer-B2 (Transformer) -- under an identical, leakage-screened protocol: training on the combined FUSeg/AZH wound data and evaluating, without fine-tuning, on two independent external datasets (DFUC2022 and Medetec). All models achieve strong in-domain performance (Dice 0.80--0.83) but degrade substantially across datasets. The degradation is, however, architecture-dependent: SegFormer-B2 generalizes best on both external sets (DFUC2022 Dice 0.557, Medetec Dice 0.786), outperforming both convolutional models, while the more complex DeepLabV3+ generalizes worse than the simpler U-Net. Per-image failure analysis on 2,160 images across both external test sets confirms that SegFormer-B2 produces the fewest catastrophic failures on DFUC2022 (31.1%), compared with U-Net (38.5%) and DeepLabV3+ (43.0%). The consistent ranking across two independent external sources, confirmed by Wilcoxon signed-rank tests (p < 0.001 on both datasets), indicates that architecture family, not model complexity, drives cross-hospital generalization.

---


### 5. [How many labels do you need? A decision framework for cross-habitat marine species recognition](https://arxiv.org/abs/2607.02559)

**<font color=#1a73e8>作者：</font>** Alzayat Saleh, Mostafa Rahimi Azghadi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated image recognition is increasingly used to scale ecological monitoring beyond manual annotation, yet ecologists lack evidence-based guidance on how much labelling effort reliable deployment at new sites requires. We present a decision framework quantifying the trade-off between labelling effort and recognition accuracy when transferring vision systems across marine habitats. The benchmark spans five datasets, three oceans, and three taxonomic groups (fish, corals, invertebrates), from tropical reefs in the Great Barrier Reef and French Polynesia to a temperate Danish fjord. We evaluated four recognition models (DINOv2, CLIP, ResNet-50, EfficientNet-B4) under four adaptation strategies (linear probing, LoRA, Visual Prompt Tuning, full fine-tuning) across three protocols: within-habitat transfer across 20 reef sites (240 runs), cross-dataset geographic transfer along a difficulty gradient (40 runs), and few-shot adaptation curves with 0-100 labelled samples per class (648 runs). Frozen self-supervised foundation features (DINOv2 + linear classifier, 1,538 trainable parameters) generalised to unseen reef sites at least as well as fully fine-tuned convolutional baselines four orders of magnitude larger; they learned species-diagnostic, habitat-invariant representations, whereas baselines encoded habitat-specific shortcuts that fail at new sites. As few as 10-20 labelled images per species sufficed to deploy reliable recognition at a new site, cutting annotation effort by roughly an order of magnitude.
Solution. Programmes expanding to new sites can deploy reliable recognition by pairing a frozen, open foundation model (DINOv2) with a simple linear classifier and annotating only 10-20 images per species - roughly 1-4 hours per site. The framework lets programmes budget labelling effort against expected accuracy across sites, ecosystems, and platforms.

---


### 6. [Inpainting U-Net for seamless pedestrian-level wind prediction across urban morphologies](https://arxiv.org/abs/2607.02560)

**<font color=#1a73e8>作者：</font>** Jingzi Huang, Claire E. Heaney, Tao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pedestrian-level wind prediction is essential for urban design and wind-comfort assessment, but high-fidelity simulations such as LES remain computationally expensive for rapid evaluation. This study develops a two-stage U-Net framework for efficient prediction of time-averaged pedestrian-level wind speed over realistic urban morphologies. The model is trained and evaluated using the UrbanTALES dataset, which contains realistic city configurations under different approaching wind directions. In the first stage, a baseline U-Net model (M1) predicts wind fields patch-by-patch from normalised building height and fetch information. This formulation allows application to urban domains of arbitrary size, but independent patch inference can introduce discontinuities at patch boundaries. To address this, a second U-Net model (M2) is introduced as an inpainting-based refinement model. M2 uses a larger contextual window containing the initial M1 prediction and local morphology to reduce discontinuities using neighbouring flow information. During full-field inference, M2 is applied iteratively using a Gauss-Seidel scheme until convergence. Results show that M1 captures the main spatial distribution of pedestrian-level wind speed and performs well in low- and moderate-velocity regions, although high-velocity peaks are less accurate. M2 substantially reduces patch-boundary artefacts and improves spatial coherence. Across unseen urban cases, the framework reproduces mean velocity and spatial variability reasonably well, while maximum velocities remain underestimated. Overall, the proposed framework provides an efficient and flexible surrogate model for high-resolution pedestrian-level wind prediction across realistic urban morphologies.

---


### 7. [Double-Helix Active Geometry: LiDAR-Anchored Multi-View Depth with Selective Abstention](https://arxiv.org/abs/2607.02561)

**<font color=#1a73e8>作者：</font>** Jinwen Wen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Consumer depth sensors such as the LiDAR scanner on recent iPhones provide metric range, but their useful range is short and their returns are sparse. We present DH-Active, a lightweight, training-free geometry back-end that treats the sensor as a metric ruler rather than the sole source of depth. Near-field returns anchor the metric relative pose of two views through PnP; visually trackable samples without a valid depth return are then triangulated under that pose. A parallax/reprojection gate abstains wherever the geometry is ill-conditioned, leaving an explicit hole and a selective score instead of forcing an estimate. The measured core front end, including spiral sampling, sparse back-projection, and hole taxonomy but excluding preprocessing and multi-view recovery, runs at 1.11 ms median latency on CPU (OpenCV using 14 threads), about 38 times faster than a DINOv2-L visual branch on GPU in our timing setup. Across two iPhone captures and the public TUM RGB-D and ARKitScenes benchmarks, held-out depth is recovered at 1.4 to 6.7 percent median relative error. In a controlled ARKitScenes protocol that uses only returns within 2 m to set scale and an independent laser scan as ground truth, DH-Active achieves 64.2 percent scene-median coverage of evaluable far-field candidates at 13.4 percent scene-median relative error; direct triangulation from the device trajectory is not usable. We also report the alternatives that failed in our tests: single-frame defocus, classical focus-stack depth, defocus-LiDAR fusion, point-to-point ICP over a good visual-inertial track, and attention-to-holes resampling. A 1.26 B learned model remains more accurate after oracle scale alignment. The contribution here is narrower: metric sparse depth, explicit abstention, zero learned parameters, and near-millisecond CPU cost.

---


### 8. [Entropy-Coded MS-VQ-VAE with Learned Priors for Ultra-Low Bitrate Video Compression](https://arxiv.org/abs/2607.02562)

**<font color=#1a73e8>作者：</font>** Manikanta Kotthapalli, Banafsheh Rekabdar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learned video codecs based on continuous latent representations struggle to operate reliably below 0.1 bits per pixel~(bpp): without a differentiable rate signal, Lagrangian optimisation cannot effectively trade reconstruction quality for bitrate at extreme compression ratios. We demonstrate that discrete latent representations sidestep this limitation entirely. In a vector-quantized~(VQ) codec, the codebook size~$K$ imposes a hard information ceiling of $\log_2 K$ bits per symbol; a learned autoregressive prior then exploits the non-uniform distribution of code usage -- which we show follows a power law -- to push actual bitrates well below this ceiling, without any rate-penalty tuning.
Building on the MS-VQ-VAE architecture introduced in~\cite{kotthapalli2026msvqvae}, we sweep $K \in \{128, 256, 512, 1024\}$ under a uniform training protocol to trace four operating points on the rate-distortion~(RD) curve. We identify and resolve a critical training instability: gradient-based VQ collapses catastrophically at $K \leq 512$, whereas EMA-stabilised codebook updates with dead-code restart maintain full utilisation across all configurations. On 500 UCF101 test clips ($64\!\times\!64$, 32~frames), our models operate at 0.043-0.064~bpp -- 3.3-5$\times$ below H.264's practical floor and $5$-$7.6\times$ below H.265's floor at this resolution. Every MS-VQ-VAE configuration outperforms H.265 CRF\,36 on perceptual quality (LPIPS) despite using $5$-$7.6\times$ fewer bits. At $K{=}1024$, the model surpasses H.265 CRF\,36 on LPIPS by a margin of 0.072 absolute while using $5.1\times$ fewer bits. Codebook analysis confirms power-law index distributions and 70-85\% entropy efficiency, establishing the pipeline as a principled learned entropy coder.

---


### 9. [Attention Dynamics in Diffusion Models: A Visual Analytics Framework for Human-AI Collaboration](https://arxiv.org/abs/2607.02563)

**<font color=#1a73e8>作者：</font>** Yiran Xiao, George Legrady  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based text-to-image models can synthesize complex and highly structured visual content, yet the emergence and evolution of semantic structure remain difficult to interpret. Many existing workflows rely on aggregated attention or scalar summaries that separate temporal change from image-space evidence. To address this gap, we present a visual analytics framework for exploring attention dynamics in diffusion models: the step-indexed evolution of token-level cross-attention maps, their temporal concentration, and their spatial relationships. Our approach enables structured analysis of attention behavior across generation steps by integrating quantitative measures with data-driven stage identification in an interactive workflow. Case studies on a structured 60-prompt Stable-Diffusion-class benchmark illustrate recurring, interpretable patterns within this setting and show how linked temporal and spatial views facilitate the observation and discussion of generative processes, supporting more effective human-AI collaboration.

---


### 10. [From Raw Segmentations to Simulation-Ready Cardiac Meshes: An Automated Framework for Anatomical Reconstruction and Virtual Cohort Generation](https://arxiv.org/abs/2607.02564)

**<font color=#1a73e8>作者：</font>** Francesco Fabbri, Martino Andrea Scarpolini, Paolo Ciancarella 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computational models of the human heart are widely used to study electromechanical and fluid-dynamical cardiac function and to support applications such as in silico clinical trials. However, most studies remain limited to single or patient-specific anatomies, restricting the inclusion of population-level variability required for uncertainty quantification. A key challenge is translating medical-image segmentations, which may contain artifacts, mesh defects or disjoint domains, into topologically coherent geometries suitable for multiphysics simulations.
In this work, we present a semi-automatic pipeline that converts CT-based segmentations into simulation-ready cardiac meshes within a few minutes while preserving anatomical and topological consistency. Building on modern deep learning segmentation methods, the framework incorporates a template-based registration stage to regularize artifacts and enforce mesh-quality constraints. A Chamfer-distance morphing strategy deforms a high-quality template toward each segmented heart, matching individual chambers while preserving topology.
The resulting meshes are watertight, isotopological, and endowed with consistent point-to-point correspondence. The pipeline is validated on 58 healthy cardiac CT scans, including all cardiac chambers and proximal vessel segments. The resulting meshes can be represented in a unified shape space, enabling the construction of a statistical shape model of the heart and major vessels. Principal Component Analysis shows that a low-dimensional latent space efficiently captures population variability, while Gaussian Mixture Modeling enables synthetic anatomy generation. Overall, the proposed framework (released open-source) provides a pathway from raw segmentations to simulation-ready cardiac geometries, enabling anatomically consistent virtual cohorts for large-scale in silico studies.

---


### 11. [Uncertainty-Aware Last-Layer Adaptation of RETFound for Referable Diabetic Retinopathy Screening Under Dataset Shift](https://arxiv.org/abs/2607.02569)

**<font color=#1a73e8>作者：</font>** Karim Mardhani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a safety-centered empirical evaluation of uncertainty-aware last-layer adaptation for referable diabetic retinopathy screening using RETFound, a self-supervised vision-transformer retinal foundation model used here as a frozen feature encoder, and the public APTOS 2019 and DDR diabetic retinopathy fundus image datasets. We compare a cached-feature softmax head, post-hoc temperature scaling, variational Bayesian last-layer heads, a diagonal Laplace last-layer approximation, and an SNGP-style cached-feature head. On APTOS, uncertainty-aware operating points improved sensitivity and selective-referral behavior. The strongest APTOS selective-referral result deferred approximately 20 percent of cases and reduced accepted-case false negatives to zero while preserving high accepted-case specificity. However, threshold tuning also reduced false negatives at high false-positive cost, so false-negative reduction alone was not unique to Bayesian modeling. On DDR, native Bayesian heads qualitatively reproduced the APTOS direction but with weaker tradeoffs, while the APTOS-trained SNGP checkpoint transferred poorly and failed to provide useful external selective-referral behavior. These results highlight the value of safety-centered evaluation beyond aggregate accuracy: uncertainty-aware last-layer heads can improve internal safety-oriented operating points, but trustworthy retinal screening claims require explicit safety-coverage evaluation and second-dataset validation under shift.

---


### 12. [Additive Causal Construction for Transferable and Reconfigurable Cross-System Learning in Multi-Source Image Fusion](https://arxiv.org/abs/2607.02572)

**<font color=#1a73e8>作者：</font>** Zhizhong Fu, Wei Zhou, Zhaoyang Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In multi-source image fusion scenarios, heterogeneous inputs are typically driven by distinct generative mechanisms and can be viewed as a composition of multiple causal systems. However, cross-system discrepancy (CSD) and cross-system entanglement (CSE) commonly arise during the fusion process, often leading to significant performance degradation under out-of-distribution (OOD) predictions. To address the CSD and CSE issues, we propose the additive causal construction (ACC) framework, which characterizes information fusion at two levels: firstly, it establishes causal "anchors" shared among multiple systems through intervention consistency to enable causal graph transferability (CGT); and secondly, it formalizes the fusion process as causal construction and models the reliability of constructed paths through uncertainty quantification to ensure causal graph reconfigurability (CGR). Building upon this, we revisit the traditional causal representation learning (CRL) with ACC and propose ACC-CRL as a learnable instantiation of the framework. The method explores joint causal content representations across systems via content-mechanism decoupling, and performs response alignment under shared anchors to mitigate CSD. Furthermore, it incorporates structural uncertainty to adaptively regulate the fusion process, thereby suppressing unstable CSE. We conduct systematic experiments on synthetic data (ColorMNIST) and real-world multi-center medical imaging tasks (microvascular invasion (MVI) prediction). The results demonstrate that the proposed method significantly improves OOD generalization while maintaining in-distribution (ID) performance, validating the effectiveness and robustness of the ACC-CRL strategy based on mechanism alignment and uncertainty modeling in open environments.

---


### 13. [Symmetry-Structured Neural Completion of Islamic Geometric Patterns from Sparse Control Geometry](https://arxiv.org/abs/2607.02573)

**<font color=#1a73e8>作者：</font>** Hassan Ugail, Irfan Mehmood  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Islamic geometric patterns are governed by exact rotational symmetry and strict construction rules. This paper treats these rules as formal geometric knowledge and embeds them in a neural completion framework, rather than leaving them to be learned statistically from data. Given sparse control geometry and a target symmetry order, the system completes the pattern as a vector graph by predicting edges and refinements of bounded curves over a candidate lattice whose edges are organised into rotational orbits under the cyclic group. Symmetry is enforced either by constraining predictions within these orbits or by projecting them onto them during inference. The orbit-tied variant provides a constructive guarantee: for any input and any orbit-level selection rule, it produces exact N-fold symmetry, preserves anchor points, and keeps all refinements within prescribed bounds. These properties are verified numerically. The study focuses on rotational symmetry, and all quantitative results are obtained from procedurally generated graphs inspired by Islamic geometric design rather than from a historical corpus. On clean inputs, enforcing exact validity produces no measurable loss in fidelity. When control geometry is missing, an unstructured decoder loses fidelity and breaks symmetry; retraining on corrupted inputs recovers much of the fidelity but not exact validity. Symmetry-structured inference, by contrast, keeps violations at zero throughout. The results show that augmentation and symmetry structure address distinct failure modes: augmentation improves fidelity under corruption, while symmetry structure guarantees validity. The framework therefore provides a knowledge-constrained, guarantee-backed approach to neural completion for scalable vector ornaments whose validity depends on exact geometric structure.

---


### 14. [Classroom Behavior Monitoring with YOLO An Empirical Study in Higher Education Settings](https://arxiv.org/abs/2607.02580)

**<font color=#1a73e8>作者：</font>** Sinh Vu Trong, Dung Nguyen Manh, Hieu Hoang Minh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classroom behavior monitoring plays a vital role in evaluating student engagement and improving teaching effectiveness. Traditional observation methods remain subjective and lack scalability. This study introduces a real-world dataset of classroom videos collected at the Banking Academy of Vietnam (BAV-Classroom dataset), annotated with nine distinctive behavioral categories. State-of-the-art Computer Vision models were evaluated and compared, with YOLOv11 achieving the best performance. Experimental results indicate that students' concentration often decreases notably during the final part of lectures, highlighting challenges in sustaining engagement. Our findings demonstrate the feasibility of applying computer vision for automated classroom monitoring, providing valuable insights for academic quality management.

---


### 15. [Evaluating Intellectual Property Guardrails of Generative Image Models: A Technical Report](https://arxiv.org/abs/2607.02582)

**<font color=#1a73e8>作者：</font>** Austin T. Hoag, Apostolos Modas, Yunhao Ba 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative image models are capable of producing images that bear a strong resemblance to, or replicate, recognizable intellectual property (IP). In this technical report, we present a benchmark and automated evaluation pipeline to test for evidence of IP guardrails in generative image models along with the propensity for these models to generate images with recognizable IP. The IP categories we tested include fictional characters, celebrity likeness, and commercial logos and do not encompass the full range of IP which may be implicated by image generation models. We evaluated fourteen widely used text-to-image models, including three self-hosted open weights models and eleven private models. While all of the private models were observed to refuse generations at some level due to IP guardrails, the frequency of generation refusals varied substantially among models. The refusal rates also varied considerably across the different IP categories tested. Commercial logos were refused least frequently and were successfully generated at the highest rate, on average. Though the rate varies, all models tested readily generated images containing recognizable IP as of March 2026.

---


### 16. [RotateAttention: RoPE-Aware Rotation and Range Rectification for INT4 Quantized Attention in Video Generation](https://arxiv.org/abs/2607.02584)

**<font color=#1a73e8>作者：</font>** Yaofu Liu, Wanli Lan, Jinxi Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In \textbf{DiT-based video generation models equipped with 3D Rotary Position Embeddings (3D RoPE)}, the attention mechanism remains a primary computational bottleneck due to its quadratic complexity with respect to sequence length. While quantized \textbf{FlashAttention} offers a promising path toward hardware acceleration, existing low-bit quantization methods overlook two critical challenges in this setting: \textbf{1)} applying online rotation matrices -- a widely used technique for mitigating outliers in Queries ($Q$) and Keys ($K$) -- is difficult to reconcile with \textbf{RoPE}; and \textbf{2)} the non-negative attention matrix $P = \exp(QK - \max(QK))$ makes symmetric quantization waste half of the 4-bit dynamic range. In this work, we observe that the outlier distributions of $Q$ and $K$ are strongly affected by the dimensional partitioning of \textbf{3D RoPE}. Based on this finding, we propose \textbf{RotateAttention}, an efficient \textbf{mixed-precision INT4 FlashAttention} framework tailored for \textbf{DiT-based video generation models with 3D RoPE}, using selective \textbf{FP16 fallback} for accuracy-sensitive attention blocks and denoising steps. RotateAttention introduces two core techniques: \textbf{1) RoPE-aware Rotation}, which employs either mergeable rotation matrices that can be fused into RoPE or negligible-overhead matrices to mitigate RoPE-induced outliers in $Q$ and $K$; and \textbf{2) Range-optimized $P$ Quantization}, which uses fixed scales and zero-points to fully exploit the \textbf{INT4 numerical range} with minimal computational overhead. Experiments show that \textbf{RotateAttention} preserves video generation quality nearly identical to full-precision baselines while achieving up to 1.68$\times$ end-to-end speedup and 2.2$\times$ kernel-level acceleration.

---


### 17. [Reliability-Aware CT-MRI Registration: A Quality Engineering Framework with Stability Analysis and Risk Classification](https://arxiv.org/abs/2607.02585)

**<font color=#1a73e8>作者：</font>** Nisreen Albzour  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal CT-MRI registration is central to image-guided radiotherapy, surgical navigation, and diagnostic workflows, but most pipelines report only aggregate quality metrics without per-case reliability signals. We propose a reliability-aware framework that converts registration quality into Green/Yellow/Red risk categories using data-learned thresholds. CT images were registered to T1-weighted MRI using rigid and affine transformations on 90 paired slices from 18 patients across brain, abdominal, and neck anatomies. Reliability was assessed using Delta NMI, Delta SSIM, Dice overlap, registration stability, and inverse consistency error, combined into a single score R. Thresholds learned from training patients were applied unchanged to held-out test patients. Affine registration outperformed rigid registration on NMI and SSIM, yielding 44% Green classifications versus 33% for rigid. Reliability-filtered registrations improved the average alignment profile compared with unfiltered methods. Per-anatomy analysis showed substantial variation, with stronger reliability for abdominal registrations than brain registrations. Weight sensitivity analysis identified Dice overlap as the dominant reliability component. The proposed framework provides an interpretable quality-control layer for multimodal registration, while risk thresholds reflect statistical rather than clinical validation.

---


### 18. [Auditing the Audit: Five Failure Modes in Benchmark-Validity Audits](https://arxiv.org/abs/2607.02586)

**<font color=#1a73e8>作者：</font>** Yanhang Li, Zhichao Fan, Zexin Zhuang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Governance frameworks ask AI providers and auditors for documented evaluation evidence, and perturbation-based construct-validity audits are a common form of that evidence. We argue the audits are themselves fragile: their conclusions can be silently manufactured by implementation details that readers cannot see in the reported numbers. We name five classes of pipeline failure and demonstrate each in a self-audit over safety benchmarks and open-weight instruction-tuned models. Under a unified six-point due-diligence gate, every cell lands in a non-confirmatory bucket, and no cell reaches confirmatory. The evidence here is a single two-model, five-benchmark case study, and F1--F5 is an illustrative, deliberately non-exhaustive starting taxonomy -- not a comprehensive partition of audit failures. We position the gate as a withholding and disclosure protocol for assurance-grade evidence, supplementary to (not a replacement for) classical construct-validity evidence, and not as a route to benchmark-validity verdicts.

---


### 19. [CPR: Chained Perceptual Refinement for Coarse-to-Fine Medical Image Classification](https://arxiv.org/abs/2607.02591)

**<font color=#1a73e8>作者：</font>** Si-Yuan Lu, Hanruo Zhu, Ziquan Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High resolution medical images contain fine grained, spatially sparse cues that are critical for diagnosis, yet preserving full resolution incurs substantial computational and memory costs. Most deep models process images uniformly, leading to redundant computation or loss of diagnostic detail under downsampling. We propose Chained Perceptual Refinement, CPR, a coarse to fine framework that formulates medical image analysis as a sequential global to local decision process. Starting from a low resolution global view, CPR dynamically predicts the location and spatial extent of refinement regions, extracts high resolution evidence from the original image, and incrementally integrates it with global context. By keeping the backbone input size fixed while contracting the perceptual field, CPR preserves diagnostic fidelity with constant peak GPU memory. Extensive experiments on five medical imaging datasets and multiple backbone architectures demonstrate that CPR consistently outperforms both fixed resolution and multi scale state of the art baselines, achieving improvements of up to 2.27 percentage points over the second best method. It also achieves up to a 19.6 fold reduction in GFLOPs at matched accuracy, establishing a superior accuracy and efficiency trade off for high resolution medical image analysis. The code is available on GitHub.

---


### 20. [An automated method of identifying incorrectly labelled images based on the sequences of loss functions of deep learning networks](https://arxiv.org/abs/2607.02594)

**<font color=#1a73e8>作者：</font>** Zhipeng Zhang, Wenhui Shou, Wengting Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning is widely applied in medical image analysis, but up to 10% of manually labelled images may be incorrect, degrading model performance. This paper proposes an automated method to identify incorrectly labelled medical images by analyzing sequences of loss functions from deep learning classification networks over multiple training epochs. Identified images can be reviewed and relabelled by experts, improving dataset quality and model performance. Two experiments validate the method on a fundus image dataset for referable diabetic retinopathy screening. In the first, 6% (648) of 10,788 gold-standard labels were intentionally flipped. The method identified 75.31% (488) of the flipped samples, with only 4.85% (492) false positives among correctly labelled samples. In the second, reviewing and correcting the 980 identified samples (9.1% of the dataset) and retraining the model improved best accuracy on an independent test set from 95.93% (with 6% label noise) to 96.50% (with 1.5% noise), approaching the ideal 96.57% (with 0% noise). The results demonstrate the method's effectiveness in improving model performance through automated label quality control.

---


### 21. [CIPHER: Causal Intervention Pathways for Healthcare Equity and Robustness](https://arxiv.org/abs/2607.02596)

**<font color=#1a73e8>作者：</font>** Xinyu Jia, Weidong Guo, Wangyuan Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for medical diagnosis frequently exhibit substantial performance disparities across sensitive subgroups (e.g., race, sex), even when average accuracy is high. While generative data augmentation offers a route to mitigate this, existing strategies are suboptimal; they typically address only one or two dependency channels between sensitive attributes and image features. We formalize the medical image formation process via a structural causal model, revealing that sensitive attributes actually influence image content through four distinct pathways-a structural complexity neglected by prior works. Based on this insight, we introduce CIPHER (Causal Intervention Pathways for Healthcare Equity and Robustness), a framework designed to systematically intervene on all four causal paths. To achieve this, CIPHER utilizes a diffusion backbone equipped with classifier-free guidance and null-text inversion. This technical design enables the faithful reconstruction of patient-specific anatomy while allowing for the precise, editable synthesis of counterfactuals required to break sensitive dependency chains. We tested CIPHER using chest X-ray and dermoscopy benchmarks across both standard and shifted data distributions. By employing a multi-pathway intervention strategy, our model reduced worst-group disparities by an average of 35.8% compared to disease-conditioned synthesis baselines, while also improving total diagnostic accuracy

---


### 22. [CV-DCLR: Causal-Visual Dynamic Label Refinement for Robust Zero-Shot Learning](https://arxiv.org/abs/2607.02601)

**<font color=#1a73e8>作者：</font>** Can Wang, Jiangnan Li, Mingyu Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-Shot Learning (ZSL) facilitates knowledge transfer via shared semantic spaces. However, a critical bottleneck in this paradigm is Semantic Entanglement, where visual representations are inevitably conflated with visually similar semantic concepts, such as distinguishing the intrinsic traits of a Wolf from the shared features of a Husky. Existing global alignment methods often indiscriminately maximize correlations between visual and semantic modalities, leading models to overfit spurious similarities rather than capturing distinctive class identities. To address this fundamental limitation, we propose the Causal-Visual Dynamic Label Refinement (CV-DCLR) framework. Unlike traditional approaches that rely on superficial visual statistics, CV-DCLR recalibrates visual-semantic associations via a Dual-Stream Mutual Correction Mechanism. This includes a Visual Likelihood Stream to model observational patterns and a Causal Importance Stream that verifies the structural necessity of candidate prototypes through Counterfactual Intervention. Acting as a logical filter, our adaptive gating mechanism dynamically modulates feature responses to amplify genuine causal traits while suppressing visually plausible but structurally irrelevant distractors. Extensive experiments on the CUB, SUN, and AWA2 benchmarks under a rigorous Semantic Entanglement Injection protocol demonstrate that CV-DCLR significantly outperforms state-of-the-art methods in high-ambiguity scenarios. Specifically, while existing models suffer catastrophic degradation under entanglement, our framework maintains robust performance, effectively disentangling true class identities from semantic confounders.

---


### 23. [Privacy-Preserving Industrial Ergonomics: mmWave-Based Automated REBA Scoring and Pose Estimation](https://arxiv.org/abs/2607.02611)

**<font color=#1a73e8>作者：</font>** Xuhan Zhang, Zhuangzhuang Dai, Luis J. Mans 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Work-related Musculoskeletal Disorders (WMSDs) require continuous ergonomic assessments. While Rapid Entire Body Assessment (REBA) is a gold-standard observation tool, manual monitoring is labor-intensive, and vision-based automation leads to privacy concerns. This paper proposes a novel end-to-end multi-task learning framework for privacy-preserving ergonomic assessment using millimetre-wave (mmWave) radar. A spatio-temporal backbone reconstructs 3D human skeletons, which serves as the biomechanical foundation for a subsequent regression head to generate REBA risk scores. To overcome the sparsity of radar point clouds, we utilise a multi-objective loss function incorporating biomechanical limits and temporal smoothness constraints. Furthermore, we implement an oversampling strategy to address the imbalance of high-risk postures in existing datasets. Experimental results on MMFi dataset demonstrate that our framework achieves a Categorical Accuracy of 77.78% and real-time performance with an inference latency of 5.70 ms. Our method reaches a High-risk REBA MAE of 0.93, which significantly outperforms both direct regression and two-stage pipelines in high-risk scenarios, providing a robust solution for non-invasive industrial ergonomic assessment.

---


### 24. [Fusion: A Framework for Unified Sequential Token AdaptatIon in VisiOn TraNsformers](https://arxiv.org/abs/2607.02612)

**<font color=#1a73e8>作者：</font>** Aravind Pradeep, Samira Nazari, Mahdi Taheri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers achieve strong image classification accuracy but process all image regions with nearly the same computation, even when many regions are redundant or uninformative. Recent adaptive inference methods reduce this cost by selectively compressing tokens or terminating inference early, but combining these mechanisms often causes unstable intermediate representations and accuracy degradation. We introduce Fusion, a unified adaptive inference framework that coordinates token merging, early exiting, and token pruning through a simple staged design: tokens are merged first, confidence is evaluated next, and pruning is applied only to samples that continue inference. This ordering allows the three mechanisms to operate cooperatively rather than competitively. Fusion further includes lightweight routing modules that adapt compression strength to each input and support inference-time adjustment of the accuracy--latency trade-off without retraining. On ImageNet-1k with DeiT-S, Fusion matches or surpasses state-of-the-art adaptive ViT methods at comparable compute budgets while reducing calibration error by up to $4\times$ and inference energy by $48\%$. Experiments across ImageNet-100, CIFAR-100, and ImageNette with multiple ViT backbones demonstrate consistent transferability without dataset-specific tuning.

---


### 25. [SE-UNet: Singular Equivariant Imaging for Real-World Constrained Generation](https://arxiv.org/abs/2607.02628)

**<font color=#1a73e8>作者：</font>** Kanishk Awadhiya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While diffusion models have revolutionized image synthesis, their application to real-world inverse problems is often hampered by the need for massive datasets and the difficulty of imposing strict physical constraints. In this work, we introduce \textbf{SE-UNet} (Singular Equivariant UNet), a framework designed to solve ill-posed imaging tasks without extensive pre-training. By treating generation as an optimization problem constrained by geometric equivariance ($D_4$ group) and singular value gating, SE-UNet effectively standardizes the solution space. We demonstrate that these strong inductive biases allow for state-of-the-art zero-shot inpainting results (80\% missing pixels) on CIFAR-10. Our method surpasses Deep Image Prior (DIP) baselines by over 4 dB in PSNR and exhibits a characteristic "singular snap" convergence -- rapidly locking into the signal manifold. SE-UNet thus offers a data-efficient pathway for constrained generation, aligning with the ReALM-GEN goal of bridging theoretical priors with practical deployment.

---


### 26. [GRAFT: Grafted Reference Audio for Fine-grained Pronunciation in Zero-shot Text-to-Speech](https://arxiv.org/abs/2607.02633)

**<font color=#1a73e8>作者：</font>** Antonis Asonitis, Francesco Verdini, Aref Farhadipour 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present GRAFT, a per-word pronunciation conditioning mechanism for text-to-speech neural codec language modeling. Existing systems reach high intelligibility and naturalness but inherit the ambiguity of text and mispronounce rare proper nouns, loanwords and technical terms. Even phoneme-conditioned models offer no direct acoustic handle for per-word pronunciation. GRAFT controls the pronunciation of a chosen word from a short spoken sample of it, encoded with the model's own speech tokenizer and bound to the word's position in the prompt. Voice conversion during training-data construction disentangles the hint speaker from the target speaker, so the hint may come from any voice while the output stays in the target voice. In a blind English listening study, human raters rank GRAFT first by a clear margin, judging its rendering of the difficult word closest to a reference recording of that word. On a five-language objective benchmark, GRAFT reduces target-word phoneme error rate by 22-39% over the identical text-only backbone and outperforms competitive open-source zero-shot systems, both phoneme- and text-conditioned, on target-word pronunciation, while preserving speaker similarity and naturalness.

---


### 27. [Federated Learning for Object Detection: Enabling Collaborative Drone Learning Without Centralizing Data](https://arxiv.org/abs/2607.02636)

**<font color=#1a73e8>作者：</font>** Daniel M. Jimenez-Gutierrez, Enrique Zuazua, Georgios Kellaris 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Object detection is a fundamental capability for AI-driven perception in safety-critical drone and edge-vision systems, including disaster response, operational security environments, infrastructure monitoring and defense applications. Robust model performance in such environments depends on large, continuously updated datasets. However, training high-performing detectors typically requires centralizing aerial imagery, which raises privacy, regulatory, storage, and bandwidth challenges. This is especially problematic in distributed drone deployments, where visual data is generated onboard and is often impractical or undesirable to transfer to a centralized infrastructure.
In this work, we apply Federated Learning (FL) for object detection, enabling drones to improve a shared model while keeping image data local and private. We implement a federated object detection pipeline using the this http URL FL platform on the KIIT-MiTA dataset, and compare it with Single-drone and Centralized baselines using mean Average Precision (mAP) at IoU thresholds of 0.50 and 0.50-0.95. In our experiments, the proposed FL approach remains close to Centralized training while dramatically improving over Single-drone training, with the best lightweight model (YOLO26 nano), suitable for deployment even on very limited edge infrastructure, achieving relative gains of 52.89% and 67.80% in mAP@0.50 and mAP@0.50:0.95, respectively. These results show that FL enables scalable, high-performing, and privacy-preserving object detection across distributed drone fleets without data centralization.

---


### 28. [Post-Generation Curation of Synthetic Images via Homogeneous-Heterogeneous Splitting](https://arxiv.org/abs/2607.02637)

**<font color=#1a73e8>作者：</font>** Disheng Liu, Tuo Liang, Chaoda Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent generative models can produce high-quality synthetic images, offering scalable training training data for data-hungry models. Existing approaches to exploiting this potential typically involve 1) training or fine-tuning generators, or 2) using lightweight post-hoc adaptation like prompt engineering or inference-time guidance, making them generator-specific and expertise-intensive. We study a complementary question: given a fixed pool of generated images, can downstream utility be improved purely by selecting an informative subset? The answer is yes. We show that effective selection must counter a structural bias of modern generators: they tend to over-produce canonical modes of each class while underrepresenting intra-class variation. Building on this insight, we split each real class into a canonical Homogeneous (HO) subset and a non-redundant Heterogeneous (HE) subset, then score synthetic images by a fidelity-diversity criterion that rewards semantic alignment while penalizing canonical redundancy. The method is generator-agnostic and requires no retraining. Across multiple benchmarks, it consistently outperforms state-of-the-art data selection baselines and matches the real-data performance with up to 40% fewer synthetic samples. The same criterion remains effective when applied on top of stronger task-tuned generators, with gains on both classification and segmentation tasks. Post-generation selection is therefore not a substitute for better generators, but a complementary mechanism for improving the utility of synthetic data.

---


### 29. [CLABTOOLKIT: An Open-Source Toolkit for Routine Processing, Manipulation, and Visualization of Neuroimaging Data](https://arxiv.org/abs/2607.02638)

**<font color=#1a73e8>作者：</font>** Yasser Alemán-Gómez, Nino Hervé, Patric Hagmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neuroimaging research requires manipulating heterogeneous data structures, including raw MRI volumes, volumetric parcellations, cortical surface meshes, tractograms, and connectivity matrices, across tools with incompatible interfaces and file formats, forcing researchers to repeatedly re-implement routine but technically demanding operations. We present CLABTOOLKIT, an open-source Python package that consolidates these operations into a single, coherent framework by representing volumetric, surface, and streamline data as interoperable Python objects. Five core data structures (Parcellation, Surface, AnnotParcellation, Tractogram, and Connectome) encapsulate common neuroanatomical entities and provide consistent methods for loading, processing, and exporting data across standard neuroimaging formats (e.g., NIfTI, GIFTI, FreeSurfer annotations, TCK/TRK), including connectome generation from a parcellation and scalar-map projection onto tractogram streamlines. Complementary modules support BIDS dataset management, FreeSurfer integration, diffusion MRI processing, morphometric analysis, graph-theoretical network analysis, and GPU-accelerated multi-panel visualization via PyVista. The toolkit comprises 19 modules organised into six layers, exposing 13 object-oriented classes with 234 methods and 207 standalone functions, and a JSON-based configuration system enables workflow customization without code changes. Unlike existing neuroimaging libraries, which typically address these tasks separately, CLABTOOLKIT combines color and lookup-table management, parcellation manipulation, multi-surface visualization, and tractography utilities within a single framework. CLABTOOLKIT is compatible with Python 3.9-3.12 and released under the Apache 2.0 license. Source code, documentation, and example workflows are available at this https URL.

---


### 30. [BiSLW: Bi-Spectral Latent Watermarking for Generative Diffusion Models](https://arxiv.org/abs/2607.02643)

**<font color=#1a73e8>作者：</font>** Aryan Pandit  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based generative models have transformed visual content synthesis, yet they remain vulnerable to unauthorized usage and lack reliable attribution methods. Existing watermarking techniques often treat latent tensors as static spatial feature maps or depend on pixel-domain modification, and most do not explicitly leverage the internal frequency structure of the latent space for dual-band redundant embedding, leaving them susceptible to the stochastic nature of diffusion and regeneration attacks. We introduce BiSLW, a trainable bi-spectral latent watermarking framework that jointly embeds aligned identity signals across complementary spectral bands of the decoded diffusion latent using learned encoders and decoders, going beyond fixed-pattern frequency approaches. We leverage the inherent frequency structure of diffusion latents to design a dual-band watermarking framework. Low-frequency components encode global semantics, while high-frequency components capture fine texture. We exploit this structure to embed watermarks across complementary spectral bands. The watermark is independently injected into both bands via learned encoders and recombined before decoding, ensuring it becomes intrinsic to the generative trajectory. Dual spectral decoders recover the watermark from each band, while a cross-band consistency constraint enforces alignment between semantic and textural embeddings. Experiments show that BiSLW achieves a strong balance between perceptual fidelity and robustness, improving PSNR by over 3 dB compared to prior latent diffusion watermarking methods while preserving near-perfect bit accuracy under aggressive regeneration and common distortions, all with negligible computational overhead.

---


### 31. [A Granularity-Aware EEG Feature Framework for Psychopathology Dimension Prediction](https://arxiv.org/abs/2607.02670)

**<font color=#1a73e8>作者：</font>** Haofan Cheng, Jingjing Hu, Jingrong Pei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) offers a noninvasive approach for examining neurophysiological correlates of dimensional psychopathology, yet systematic evidence across EEG paradigms and feature granularities remains limited. Here, we develop a granularity-aware EEG feature pipeline that organizes multi-scale descriptors into global, regional, and channel levels. Using the Healthy Brain Network (HBN) cohort, we evaluate the prediction of four psychopathology dimensions: p-factor, internalizing, externalizing, and attention problems, across four EEG paradigms. Given the heterogeneity of pediatric psychopathology and the moderate reliability of questionnaire-derived scores, this setting represents a challenging feasibility test rather than a clinical screening scenario. Tree-based models and granularity-balanced feature selection showed promising improvements over conventional approaches in selected conditions, although effect sizes remained modest. Visualization of selected markers revealed dimension-specific spatial and spectral patterns that were broadly aligned with existing neurophysiological knowledge. An exploratory cross-dataset sanity check on the independent PEARL cohort suggested that the proposed selection principle remains technically feasible under protocol shifts, without claiming cross-dataset generalizability. Overall, multi-scale EEG features contain weak but detectable signals related to dimensional psychopathology, and granularity-aware selection may serve as a useful feature-reduction strategy for future EEG-based phenotyping studies.

---


### 32. [Internal Pluralism and the Limits of Pairwise Comparisons](https://arxiv.org/abs/2607.02672)

**<font color=#1a73e8>作者：</font>** Bailey Flanigan, Michelle Si  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Local pairwise comparisons are a standard tool for learning how people want decision rules to work, e.g., in participatory design or alignment. However, their use builds in two strong assumptions: that local comparisons are sufficient evidence about how a person wants an automated decision rule to behave, and that people can always answer those comparisons decisively. We investigate how these assumptions may be compromised under internal pluralism: the idea that an individual evaluates decision rules according to multiple authoritative priorities about how the rule should behave. We provide a formal model of such pluralistic preferences over decision rules, which then lets us identify two distinct failures of forced local pairwise comparison data. First, priorities such as proportionality, egalitarianism, and equal treatment are inherently global: what they imply in one case can depend on what happens elsewhere, so local comparisons may fail to capture them. Second, even when priorities are representable locally, tension between strongly-held priorities can generate internal conflict, producing potentially costly behavioral distortions when comparisons are forced. We then use our model to investigate the alternative -- allowing people to report indecision -- and our findings suggest that doing so can considerably reduce the number of queries needed to learn preferences accurately. We conclude by describing how our model points toward preference-learning methods that elicit these priorities directly, yielding more faithful and interpretable accounts of what people value.

---


### 33. [RES-DARE: Failure-Aware Expert Adaptation and Rollback-Safe Self-Repair for Intrusion Detection](https://arxiv.org/abs/2607.02687)

**<font color=#1a73e8>作者：</font>** Rahil Aftab, Anyash Prasad, Soumya Mazumdar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Intrusion detection systems are often trained under static benchmark conditions, although deployed network environments are affected by traffic drift, sensor noise, changing workloads, and evolving attack behaviour. Under such distribution shifts, static detectors may produce confident but incorrect predictions, leading to silent and unsafe failure modes. In this paper, RES-DARE (Recursive Evolving Specialists-Digital Adaptive Reasoning Engine) is proposed as a failure-aware continual intrusion detection framework with rollback-safe self-repair. Difficult, uncertain, and misclassified samples are treated as failure signals for expert specialisation rather than being discarded as noise. A supervised contrastive encoder, two-pass expert router, failure-buffer mechanism, HDBSCAN-based failure-region discovery, and trust-risk monitor are integrated to support adaptive IDS behaviour. AEHM-v2 is introduced as a rollback-safe repair mechanism, where candidate adaptations are provisionally activated and committed only when macro-F1 is preserved or improved while trust risk remains stable. Otherwise, the system is rolled back to its last validated state. RES-DARE is evaluated on CICIDS2017, UNSW-NB15, and TON\_IoT, achieving macro-F1 scores of 0.9850, 0.9736, and 0.9691, respectively. Under Gaussian feature corruption at strength 0.10, RES-DARE retains an Attack-F1 of 0.7920 on CICIDS2017 and achieves near-zero catastrophic forgetting with F = 0.0015. The results show that RES-DARE improves robustness, warning capability, and deployment safety under degraded conditions.

---


### 34. [S-EMBER: A Large-Scale Benchmark for Streaming Egocentric Memory Retrieval](https://arxiv.org/abs/2607.02689)

**<font color=#1a73e8>作者：</font>** Xiaodong Wang, Xuanyi Zhao, Pedro Rodriguez 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As wearable devices enable continuous first-person recording, AI assistants must reason across long time horizons to recall past experiences-a capability known as episodic memory. Current benchmarks often rely on offline evaluation with access to entire video files, failing to simulate the streaming reality of wearable intelligence. We introduce S-EMBER (Streaming Egocentric Memory Benchmark for Episodic Retrieval), a large-scale benchmark comprising 3,141 videos totaling 388 hours of organic activity captured via Ray-Ban Meta smart glasses. S-EMBER formalizes grounded streaming episodic retrieval, a paradigm shift from global offline search to causal, active recall triggered by visual events in a continuous stream. We provide 9,448 QA pairs requiring manual visual proof through precise temporal localization and supporting flexible response lengths to simulate natural human-AI interaction. Our extensive benchmarking of frontier models uncovers a localization paradox: while semantic reasoning improves with parameter scale, temporal grounding precision remains a stagnant architectural bottleneck that does not benefit from brute-force increases in model size, resolution, or frame density. S-EMBER establishes a hardware-authentic foundation for developing grounded, reliable episodic memory in the next generation of wearable AI agents.

---


### 35. [Property-Constrained 3D Porous Media Reconstruction from 2D Images via Conditional Generative Adversarial Networks](https://arxiv.org/abs/2607.02693)

**<font color=#1a73e8>作者：</font>** Ali Sadeghkhani, Brandon Bennett, Arash Rabbani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study presents a conditional Generative Adversarial Network (cGAN) framework for generating 3D porous media volumes with controlled porosity, trained exclusively on 2D thin section images. The key innovation lies in combining property-conditioned generation with 2D-to-3D reconstruction, eliminating the need for expensive 3D training data while maintaining control over petrophysical properties. The framework employs a hybrid architecture with a 3D generator and 2D discriminator, where multi-axis slice extraction enables learning 3D-consistent structures from 2D training data. Porosity labels are extracted using an Enhanced U-Net segmentation model. The methodology was demonstrated on two carbonate samples with different lithologies: dolomite-anhydrite and pure dolomite. Results show that the framework successfully generates realistic 3D volumes capturing lithological features such as anhydrite inclusions and fine crystalline textures. Porosity control achieved an $R^2$ of 0.93, with mean absolute errors of 0.019 and 0.010 for the heterogeneous and homogeneous samples, respectively.

---


### 36. [Aircraft Detection in Satellite Imagery using Deep Learning Object Detectors](https://arxiv.org/abs/2607.02699)

**<font color=#1a73e8>作者：</font>** Mujahir Hussain Abbasi, S. Beghin, A. T. R. Krishna Priya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The object detection in satellite imagery has garnered considerable attention due to its extensive real-world applications and the inherent challenges it presents, including noise, fluctuating image quality, and intricate backgrounds. This paper proposed a framework for object detection that combines image enhancement and Deep Learning (DL) to make detection more accurate. First, a Gabor filter is used to process the input image to bring out important features and reduce noise. Then, normalization is applied to make sure that the data is evenly distributed so that the model works properly. After that, a model based on YOLOv11 is used to quickly learn and find object features. The proposed method achieves a mAP of 95%, precision of 97%, recall of 85%, and F1-score of 91%, which demonstrates the superior aircraft detection performance. These results show the framework accurately identify aircraft in satellite imagery and is suitable for real-time applications such as surveillance, air traffic monitoring and remote sensing analysis.

---


### 37. [VLRC: Vision-Language Reprojection Consistency as a scalable signal for better feed-forward 3D pretraining](https://arxiv.org/abs/2607.02707)

**<font color=#1a73e8>作者：</font>** Marwane Hariat, David Filliat, Antoine Manzanera  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D models are commonly trained using either expensive geometric supervision or self-supervised photometric objectives, both of which provide incomplete learning signals. We introduce Vision-Language Reprojection Consistency (VLRC), a scalable auxiliary objective that exploits frozen vision-language representations as semantic multi-view supervision. Given a predicted 3D reconstruction, VLRC reprojects dense vision-language features across views and enforces feature consistency between corresponding image locations, requiring no additional 3D annotations. The objective integrates seamlessly with both self-supervised monocular reconstruction and supervised-pretrained feed-forward 3D models during unlabeled adaptation. By aligning geometry with language-grounded features, VLRC not only improves depth and camera estimation but also enables more coherent multi-view semantic fusion for open-vocabulary 3D scene understanding. Experiments on indoor and outdoor benchmarks demonstrate consistent gains in 3D reconstruction accuracy and zero-shot open-vocabulary 3D semantic segmentation.

---


### 38. [When Does Resolution Help a Frozen Backbone? Global Attention at Resolution Predicts Scalable Adaptation for Camouflaged and Marine Animal Segmentation](https://arxiv.org/abs/2607.02708)

**<font color=#1a73e8>作者：</font>** Tyler Rust, Chandra Kambhamettu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting frozen vision foundation models to fine-grained segmentation now largely depends on backbone selection. Whether the backbone applies global attention to a high-resolution token set predicts whether a low-rank adapter turns resolution into accuracy. Isotropic ViTs attend globally over the full grid and keep improving with resolution; hierarchical backbones confine early attention to local windows and pool the grid before their global stages, plateauing at lower resolutions. A controlled six-backbone study establishes the pattern, and editing the backbone points to the cause: pooling keeps the benefit, removing global attention does not. The effect is specific to low-rank adaptation. Under one fixed pipeline, SALT (Side-stem, Attention-gated U-Net, Low-rank Tuning), one RGB-only pass on a strong isotropic backbone wins the best S-measure on the four data-matched camouflaged sets, and leads every marine and salient set. It reaches a new state of the art on both marine-animal benchmarks (MAS3K mIoU 0.878).

---


### 39. [Global Pose Control for Generative View Synthesis in Normalized Object Coordinate Space](https://arxiv.org/abs/2607.02712)

**<font color=#1a73e8>作者：</font>** Zhibing Li, Amogh Gupta, Behnoosh Parsa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel View Synthesis (NVS) enables the generation of unseen views of a scene from a single or multiple images, allowing users to freely explore an object from any viewpoint. Despite the recent impressive qualitative improvements of generative models for this task, existing methods struggle to provide global and intuitive control of target viewpoints because they either use input-relative camera poses or are limited to generating sparse global views. This lack of global pose control severely limits the number of downstream tasks potentially enabled by NVS. To address this limitation, we propose a novel approach for precise camera control in a customizable Normalized Object Coordinate Space (NOCS), requiring single or few unposed images. Our method operates solely on the absolute camera pose of the target view in NOCS, eliminating the need for a relative world frame or camera poses of the input images. Unlike previous methods that treat NVS as a standalone generation task, we formulate it as an image editing problem and build upon state-of-the-art editing models to leverage their superior generalization capability. Camera information is injected as dedicated camera tokens via an in-context multi-modal conditioning strategy. To alleviate the inherent ambiguity of NOCS, we incorporate text descriptions that explicitly define the object's canonical coordinate frame, which also enhances generalization to unseen object categories. Furthermore, we curate a high-quality dataset with consistently aligned orientations and corresponding NOCS text definitions. Extensive experiments demonstrate that our method robustly generates novel views with accurate and consistent orientations from arbitrary unposed images across diverse categories, achieving state-of-the-art image quality and fidelity.

---


### 40. [LiNO: Lifting based multiresolution neural operator](https://arxiv.org/abs/2607.02715)

**<font color=#1a73e8>作者：</font>** Himanshu Pandey, Subham Patel, Ratikanta Behera  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, neural operators have shown promising outcomes for learning solution operators of differential equations directly from data. This framework learns a functional mapping from the parameter field to the solution field, enabling the prediction of an entire class of solutions rather than a specific instance. However, existing operators often struggle to capture both global dynamics and fine-scale structure simultaneously. To design an effective operator capable of representing multiscale features, a hierarchical multiscale decomposition framework is required. In this study, we develop the Lifting Neural Operator (LiNO), a multiresolution operator built on the second-generation wavelet lifting scheme. LiNO learns a multiresolution decomposition directly from data by parameterizing the lifting transform. This lifting transformation is adaptive to the underlying solution function and exactly invertible by construction, enabling information-preserving multiscale operator learning. In the lifted multiresolution space, the operator evolves coarse and directional detail coefficients separately, resulting in scale-aware modeling of the underlying physics. We evaluate LiNO on several benchmarks, including Darcy flow, the Poisson equation, the Allen-Cahn equation, the compressible Navier-Stokes equation, and the Gray-Scott reaction-diffusion system. Together, these benchmarks cover a wide range of physical behaviors, including multiscale phenomena, transport-dominated dynamics, and chaotic systems. LiNO demonstrates strong performance on these challenging benchmarks compared with state-of-the-art neural operators. These results suggest that adaptive multiresolution operators provide a promising direction for scientific machine learning.

---


### 41. [Diagnosing Aerial-View Object Detectors with Foundational Image Generative Models](https://arxiv.org/abs/2607.02718)

**<font color=#1a73e8>作者：</font>** Stanislav Panev, Minhyek Jeon, Vaishnavi Khindkar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in large-scale image generative models enable photorealistic scene synthesis with controllable attributes. Beyond data augmentation, their potential as diagnostic tools for trained vision systems remains unexplored in the aerial and remote sensing domains. We introduce a synthetic diagnostic framework for aerial-view vehicle detection that combines text-guided generation, attribute-controlled editing, and automated attribute verification to construct a controllable synthetic testbed. This enables fine-grained evaluation of pretrained detectors under diverse scene types and environmental conditions that are difficult to isolate in real datasets. Across three detection architectures and three real aerial datasets, synthetic scene-wise performance trends closely match real-world weaknesses. Guided by these diagnostics, targeted supplementation with small real datasets from the identified weak categories yields improvements of up to 13% AP50 while requiring substantially fewer additional samples than non-targeted augmentation. Our results show that controlled synthetic probing can predict real-domain performance gaps and guide efficient data collection. The proposed diagnostic framework is modular and can incorporate alternative generative or vision-language models as capabilities evolve. Our code and datasets are available here: this https URL

---


### 42. [GRCD: Grounded Region Change Detection for Multi-Finding Chest X-Ray Pairs](https://arxiv.org/abs/2607.02719)

**<font color=#1a73e8>作者：</font>** OFM Riaz Rahman Aranya, Peyman Najafirad, Kevin Desai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiologists routinely compare current and prior chest X-rays to track disease progression, producing follow-up reports that describe multiple findings, each localised to an anatomical region and annotated with a temporal change status. Existing automated methods either generate reports from a single image without modelling temporal context, or incorporate temporal information but do not ground their outputs spatially. The few approaches that combine temporal reasoning with spatial grounding are restricted to single-finding descriptions, leaving multi-finding reports with mixed change directions unaddressed. We present GRCD, a framework for grounded report generation from chest X-ray pairs in the multi-finding setting. We first construct a rigorously cleaned dataset of temporal chest X-ray pairs by identifying and correcting two systematic labelling errors in the source annotations. We then introduce a Region-Guided Change Token module that encodes per-region temporal change across anatomical structures and injects this signal into a language model through a dual-pathway strategy combining prepended spatial tokens with gated cross-attention. On a multi-finding test set, GRCD outperforms existing baselines on text generation and clinical accuracy metrics, with gains in change detection. Ablation studies confirm that the dual-pathway design outperforms either integration strategy in isolation on text and clinical metrics, and that region-level change encoding is necessary for multi-finding generation. Code is available at this https URL

---


### 43. [Provable Pruning for Efficient 3D Gaussian Splatting via Coresets](https://arxiv.org/abs/2607.02721)

**<font color=#1a73e8>作者：</font>** Waseem Mousa, Alaa Maalouf  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) enables high-quality real-time novel-view synthesis, but practical scenes often contain millions of Gaussians, making compression essential for deployment on limited hardware. Existing reduction methods are effective but mostly heuristic: they provide no multiplicative approximation guarantee for the rendered objective, and thus rely heavily on costly post-pruning finetuning to recover quality. We ask a basic question: can a 3DGS scene be provably replaced by a much smaller weighted subset (coreset) while preserving the objective of interest? We first show that, in the unrestricted setting, no non-trivial multiplicative 3DGS coreset exists. We then show that multiplicative guarantees are not impossible, but resolution-dependent. For a prescribed rendering resolution, such as representative views or grids of views/rays, we provide the first weighted coreset construction theorem for 3DGS. The construction samples Gaussians by sensitivity: provable importance scores measuring each Gaussian's role in the full-scene objective. Finally, under explicit validity and log-transmittance stability assumptions, we turn this objective guarantee into a rendering guarantee. Empirically, our method is strongest where deployment needs it most: aggressive compression with no or minimal recovery compute. In prune-only and very short finetuning regimes, it achieves state-of-the-art performance, showing that principled importance estimation can be both theoretically meaningful and practically useful. Open-source code is available at this https URL.

---


### 44. [Weighted Conformal Prediction for Lab-to-Track Thermal Transfer in EV Motorsport Powertrains](https://arxiv.org/abs/2607.02722)

**<font color=#1a73e8>作者：</font>** Varshith Roy Kotla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting thermal volatility in high-performance EV powertrains is difficult as internal temperatures are rarely observable outside the lab, and models calibrated on lab drive cycles fail when deployed against real-world loads. We study this lab-to-track transfer problem using conformal prediction, offering distribution-free uncertainty bounds. We implement Ensemble Batch Prediction Intervals (EnbPI; Xu & Xie, 2021), a leave-one-out bootstrap-ensemble conformal method for autocorrelated time series, and calibrate it on real CALCE lithium-ion cycler data (A123 SP20 cells, FUDS profile). We evaluate it under a genuine, measured covariate shift: a second real CALCE test condition (US06 Highway Driving Schedule at 45°C). The unweighted EnbPI bound, achieving its nominal 95% coverage in-distribution (measured: 95.00%), degrades to 70.13% empirical coverage under this real shift. We introduce a weighted EnbPI procedure combining EnbPI's ensemble residuals with density-ratio weighting (Tibshirani et al., 2019), estimating the density ratio via a probabilistic domain classifier. This recovers coverage to 72.42%, a modest, honestly-reported improvement, not a complete fix. We additionally apply the calibrated model to real 2023 Formula 1 telemetry (Monza and Silverstone, driver VER) as an unsupervised out-of-distribution diagnostic. Because no internal thermal channel exists in public trackside telemetry, we report only unsupervised flag rates (65.6% at Monza, 58.0% at Silverstone, well above the 5% in-distribution base rate) and note inconsistent associations between flags and braking/DRS zones. We conclude that conformal domain adaptation is a promising but only partially solved tool for this problem, detailing exactly where it falls short.

---


### 45. [Signal from Space: Detecting Schools and Towers to Bridge the Digital Divide](https://arxiv.org/abs/2607.02724)

**<font color=#1a73e8>作者：</font>** Zakarya Elmimouni, Sandor Farkas, Fares Fourati 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable internet access is essential for modern education, yet millions of school-aged children especially in developing regions remain offline due to unconnected schools. The Giga Initiative aims to connect every school to the internet, but doing so at scale requires efficient methods to map schools and assess surrounding connectivity infrastructure without relying on sparse or noisy third-party datasets. In this work, we propose a scalable, vision-only framework that uses high-resolution satellite imagery and transfer learning to address both tasks simultaneously. By adapting pre-trained object detection models to new geographical regions with minimal labeled data, we detect schools and cell towers directly from space. We then analyze the spatial relationship between detected schools and nearby towers as a proxy for connectivity availability. This purely imagery-driven pipeline enables large-scale infrastructure mapping, reduces dependency on auxiliary data, and supports data-driven prioritization of connectivity investments in underserved areas. Our approach is demonstrated on real satellite imagery from Lesotho, showing strong performance across this region.

---


### 46. [Reinforcement Learning for Data-Efficient Code-Switched ASR](https://arxiv.org/abs/2607.02757)

**<font color=#1a73e8>作者：</font>** Ziwei Ye, Peter Vickers  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio-language models can be prompted for code-switched speech, but their decoding is not optimized for code-switching and often fails at language boundaries. We propose a practical reinforcement learning with verifiable rewards recipe for data-efficient adaptation of audio-language models to code-switched ASR using group relative policy optimization, combining an error rate reward with a script fidelity reward that penalizes wrong writing systems and a two-pass draft-and-refinement procedure. Using Qwen2-Audio as a reproducible testbed across 10 language pairs, training on only TTS code-switched speech, we show that RLVR with 10% of the data matches LoRA supervised fine-tuning trained on the full dataset, with the largest gains on typologically distant pairs. The error rate reward eliminates translation errors while the script fidelity reward separately reduces script contamination without degradation. These gains transfer zero-shot to a human-recorded code-switching corpus.

---


### 47. [LuxSQA: Ask Me in Luxembourgish with TTS-Augmented Spoken Question Answering](https://arxiv.org/abs/2607.02763)

**<font color=#1a73e8>作者：</font>** Nina Hosseini-Kivanani, Marco Matassoni, Alessio Brutti  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spoken Question Answering (SQA) remains largely focused on high-resource languages and carefully recorded speech, limiting the reach of speech-LLM methods in low-resource settings. This paper investigates whether text-to-speech (TTS) can provide task-specific training data for Luxembourgish SQA without requiring a large human-recorded QA corpus. Starting from existing text-based QA resources, we translate questions into Luxembourgish, synthesize spoken questions with multiple TTS systems, and pair them with textual answers. We train a parameter-efficient SLAM-style architecture that connects a frozen Whisper encoder to frozen multilingual LLM backends through a learned projector and LoRA adapters. We compare MMS-TTS, Qwen3-TTS, and OmniVoice variants, including single-source corpora of about 48k questions and a 4TTS multi-source mix of approximately 230k questions. Evaluation on LLAMA-LB-Test with two real Luxembourgish speaker conditions shows that multi-source and voice-design-based synthetic training configurations yield the strongest SQA performance. The results also show that no-reference TTS quality scores do not monotonically predict downstream QA performance, indicating that synthetic speech must be evaluated as task-specific training data rather than only as natural-sounding audio.

---


### 48. [Gemma 4 Technical Report](https://arxiv.org/abs/2607.02770)

**<font color=#1a73e8>作者：</font>** Gemma Team, Sherif El Abd, Vaibhav Aggarwal 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Gemma 4, a new generation of open-weight, natively multimodal language models in the Gemma model family. Designed to advance compute efficiency and reasoning, the Gemma 4 model suite features dense and Mixture-of-Experts architectures, ranging from 2.3B to 31B parameters. Alongside improved vision and audio encoders for all model sizes, we propose a unified, encoder-free architecture for our 12B model, which ingests raw audio and image patches. Furthermore, we integrate a thinking mode, enabling Gemma models to generate reasoning traces prior to responding. We improve inference speed, memory, and compute efficiency, as well as long-context abilities through critical design choices. Gemma 4 establishes a leap in performance across STEM, multimodal, and long-context benchmarks, and rivals larger, frontier open models in human-rated tasks.

---


### 49. [Automated Data Readiness for Scientific AI](https://arxiv.org/abs/2607.02771)

**<font color=#1a73e8>作者：</font>** Sean R. Wilkinson, Valentine G. Anantharaj, Jong Youl Choi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Leadership computing facilities steward large-scale scientific datasets that routinely require substantial transformation before serving as AI training data. However, no existing framework fully unifies automated transformation, readiness assessment, provenance tracking, and agent-native deployment. We present REDI, an open-source framework that addresses this gap through a unified five-stage pipeline (ingest, preprocess, transform, structure, and output) with per-stage instrumentation for reproducibility and deployment as an agent-callable skill; companion tool SetGo automates FAIR compliance and catalog publication. Evaluated across climate, proteomics, materials science, and nuclear fusion, REDI transforms all datasets from raw to AI-ready, with outputs validated against domain-expert references, and preliminary results show near-ideal parallel scaling to 100 nodes on Frontier for the climate case. Provenance-instrumented profiling reveals file I/O as the dominant pipeline cost, with format selection a first-order optimization lever. These results establish REDI as a cross-domain platform providing automated data readiness for scientific AI, transforming data preparation bottlenecks into reproducible, reusable community assets.

---


### 50. [Biomechanics-aware Multi-view Markerless Motion Capture of Dexterous Hand Movements](https://arxiv.org/abs/2607.02796)

**<font color=#1a73e8>作者：</font>** Pouyan Firouzabadi, J.D. Peiffer, Kunal Shah 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Markerless motion capture (MMC) techniques have been widely beneficial in biomechanical analysis of human movement; however, application to complex motions of the hand lags other musculoskeletal systems. The primary goal of this study was to evaluate the performance of a biomechanical reconstruction method that implements a gradient-based optimization approach with a biomechanical model in the loop for tracking dexterous, unconstrained hand movements using MMC. Using a custom, 8-camera setup, we acquired 121 video recordings from 6 participants performing 11 different tasks that spanned 6 hand postures, 5 object manipulation tasks, and involved motion of the proximal upper limb joints. Performance of the proposed MMC pipeline was directly compared to a more commonly adopted two-stage reconstruction method that first triangulates 2D keypoints from computer vision pose estimation algorithms to 3D and then enforces biomechanical constraints by solving a constrained inverse kinematics problem. Relative performance was assessed qualitatively by visual inspection and quantitatively using a computer vision metric. Our method generated solutions for all 121 video recordings; the two-stage method did not converge for 15% of the recordings. Across the remaining videos, our method produced more biomechanically plausible hand kinematics than the two-stage method and was more robust to occlusion effects during tasks that involved objects. The relative robustness of the end-to-end method suggests that it is more effective in utilizing the available 2D digital keypoint information. Automatic and biomechanically meaningful tracking of hand kinematics during dexterous movements has the potential to support clinical evaluation, rehabilitation monitoring, and studies of human motor control.

---


> [!TIP]
> 当前位于：**1-50**（第 1/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
