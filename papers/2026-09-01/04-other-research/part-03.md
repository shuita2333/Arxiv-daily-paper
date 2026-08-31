# 📦 其他研究 | 2026年09月01日

> 本类共 **151** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-151](./part-04.md)

---

### 101. [NumBench: Diagnosing Counting Failures in Text-to-Image Models](https://arxiv.org/abs/2608.28206)

**<font color=#1a73e8>作者：</font>** Sandeep Wadhwa, Mayank Vatsa, Richa Singh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) models often generate the wrong number of objects, yet existing benchmarks are too small or weakly controlled to explain why. We introduce \textbf{NumBench}, a benchmark of 640{,}000 prompts spanning 1{,}600 categories and counts from 1 to 100. Its factorial design varies object composition, spatial guidance, and appearance conditions while balancing counts and category exposure. We also develop a process model in which requested instances compete for a finite set of resolvable image regions. The model predicts a near-quadratic collision deficit at low occupancy and shows how coordinated placement reduces it. For scalable evaluation, we propose the Confidence-Weighted Numeric Precision Score (\cwnps), which aggregates three calibrated detectors and discounts uncertain proposals. Across five commercial systems, two open models, and two specialized counting methods, performance declines sharply with requested count; all evaluated methods are weak above 50 objects. Count range has the largest measured effect, followed by layout and composition. Grid guidance is strongest among guided layouts, consistent with the coordination prediction, although the analysis does not establish collision as the sole cause. A 14{,}400-image human study supports automated evaluation through count 50, while results on 243 natural-language prompts show transfer beyond NumBench templates.

---


### 102. [Generalized Context in Cross Attention for Transfer Learning of Disjoint Tabular Data](https://arxiv.org/abs/2608.28209)

**<font color=#1a73e8>作者：</font>** Kazi F. Akhter, Ibna Kowsar, Manar D. Samad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlike images and text, applying transfer learning to tabular data is challenging due to heterogeneity in feature types, structures, and semantics across disparate domains. Existing methods assume shared features across data tables to enable knowledge transfer between domains, which is unrealistic in practice. \mds{This paper introduces generalized context learning to remove the requirement of shared features across domains. The generalized context captured by transformer projection weights for $key$, $value$, and $query$ provides rule-based generalization rather than the domain-specific context conventionally learned from transformer activations. Projection weights for $key$ from the source domain interact with the weight for $query$ in the target domain to achieve Cross-domain Attention Transfer Learning (CATTLE) in a data-agnostic manner. Our experiments on ten pairs of disjoint source-target data sets show that CATTLE can learn generalized context from a single source data set and is rank-wise and statistically superior to nine state-of-the-art baselines, including machine learning, deep learning, and transfer learning methods using large-scale pre-trained models. CATTLE achieves the best average rank (2.9) and delivers a 3.7% average AUROC gain over the baseline methods.} The CATTLE source code is available at this https URL.

---


### 103. [RASA: Disentangled Spatial-Motional Priors for Cross-Identity Character Animation](https://arxiv.org/abs/2608.28219)

**<font color=#1a73e8>作者：</font>** Zhen Xiao, Zhen Shen, Zhaofan Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-identity character animation aims to drive a target identity from a reference image to follow the motion of a source character from a driving video. The core challenge lies in the inherent entanglement of two capabilities: cross-identity spatial mapping (aligning position, scale, and skeletal proportions) and motion control (refining joint articulation, volumetric consistency, and view coherence). We introduce Reference-Aware Structural Alignment (RASA), a framework that disentangles spatial mapping from motion control by injecting structured priors into a Diffusion Transformer (DiT). Our approach has two stages. First, a Spatial Prior Calibrator (SPC) fuses reference identity with driving pose to generate a spatially grounded initial noise latent, ensuring correct positioning, scaling, and alignment with the driving skeleton. Second, an Inherent Motional Guider (IMG) encodes shape-agnostic SMPL articulation parameters into a semantic motion vector beyond appearance-biased 2D keypoints. Injected into intermediate DiT layers, this vector complements the base pose condition for anatomically consistent articulation and view-aware volumetric refinement. We curate CIM-Bench, a high-quality benchmark with rigorous curation, for evaluation. Extensive experiments show RASA significantly outperforms state-of-the-art methods in motion fidelity and visual quality. Our work establishes a new paradigm showing disentangled spatial and motional priors are key to robust character animation. Project page: this https URL

---


### 104. [WilLaGS: Latent-Conditional 3D Appearance Fields for Robust Gaussian Splatting In-the-Wild](https://arxiv.org/abs/2608.28240)

**<font color=#1a73e8>作者：</font>** Yuhao Bai, Qianqiu Tan, Lilong Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) delivers real-time and high-fidelity rendering but remains challenged by unconstrained in-the-wild scenes, where drastic appearance variations and transient objects violate multi-view consistency. Existing methods are fundamentally limited by independent and discrete embeddings that struggle to capture continuous environmental changes or model spatially-varying local illumination. To address these limitations, we propose \textbf{WilLaGS}, a unified framework for robust 3D scene reconstruction and generative appearance synthesis under unconstrained settings. Specifically, we introduce a generative appearance model where a $\beta$-VAE learns a structured and continuous manifold of global appearance. Conditioned on the latent code, we construct a 3D neural appearance field that generates dynamic Tri-Plane features to encode spatially-varying local illumination effects. Furthermore, to suppress transient artifacts, we present a self-supervised perceptual masking mechanism that leverages a Teacher-Student (EMA) architecture to derive a stable scene consensus, robustly identifying inconsistent regions via perceptual discrepancies. Extensive experiments on multiple datasets demonstrate that \textbf{WilLaGS} achieves state-of-the-art performance in reconstruction quality and novel view appearance synthesis, while maintaining real-time rendering efficiency.

---


### 105. [Spectral Features Dominate BCG Respiratory-Event Detection: A Large-Scale Patient-Independent Comparison of Feature Groups in Sleep Apnea Patients](https://arxiv.org/abs/2608.28242)

**<font color=#1a73e8>作者：</font>** Israel Campero Jurado, Zoe Bousraou, Lara Benning 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unobtrusive ballistocardiographic (BCG) sensing is a promising modality for long-term sleep-apnea monitoring, yet it remains unclear which signal features are most discriminative for respiratory-event detection. We present a literature-guided, patient-independent comparison of ten BCG feature groups using a 512-sensor capacitive pressure mat recorded simultaneously with respiratory polygraphy in 155 patients (52 female, 103 male) undergoing in-hospital evaluation for obstructive sleep apnea. Features were extracted from six spatially distinct signal channels, yielding a 191-dimensional feature vector spanning general statistical, time-domain, frequency-domain, wavelet, frame-energy, and nonlinear complexity descriptors. Under strict leave-one-patient-out cross-validation for binary classification of respiratory-event windows versus event-free reference windows, Random Forest and Histogram Gradient Boosting achieved AUC-ROC of 0.967 and 0.969 and AUC-PR of 0.977 and 0.979, respectively. Feature-importance analysis revealed that frequency-domain features dominate discrimination: breathing-band power in the 0.1-0.4 Hz range accounted for 30.3% of total discriminative information across all spatial channels, and Fast Fourier Transform spectral-shape descriptors of the adaptively preprocessed channel contributed a further 15.1%. AUC and curve-length features provided the main complementary time-domain evidence (21.5%), whereas wavelet-derived and nonlinear features contributed smaller secondary effects (10.4% combined across 59 features). Frequency-domain and time-domain features together accounted for 67% of total discriminative information, demonstrating that a compact, interpretable subset of the full feature library achieves clinically relevant performance under patient-independent validation and providing an empirical basis for feature selection in future BCG systems.

---


### 106. [A comprehensive and trustworthy benchmark of AI methods for change detection in Earth observation](https://arxiv.org/abs/2608.28247)

**<font color=#1a73e8>作者：</font>** Tadej Tomanič, Alice Baudhuin, Jan Sotošek 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Change detection in Earth observation (EO) is critical for monitoring land surface transformations, yet recent research in the field is constrained by inconsistent evaluation protocols and a narrow focus on predictive accuracy without regard for computational efficiency. To address this, we present a standardized, open-source benchmark for evaluating state-of-the-art (SOTA) deep learning methods for Earth observation change detection. We conduct a comprehensive analysis of ten representative model architectures, ranging from convolutional networks (CNNs) to vision transformers (ViTs), across ten heterogeneous change detection datasets. We rigorously evaluate these models with identical experimental protocols, comparing models trained from scratch against those utilizing pre-trained weights. Furthermore, we evaluate predictive performance alongside computational efficiency, including parameter counts and inference latency. Our findings reveal that well-optimized classical architectures, such as Siamese U-Nets, frequently outperform more complex contemporary models when computational efficiency is factored in, and that pre-training consistently provides a significant performance boost with no additional inference cost. To ensure complete transparency and reproducibility, all experimental resources, including standardized data splits, training scripts, training logs, and model checkpoints are publicly available and adhere to FAIR principles (Findable, Accessible, Interoperable, and Reusable).

---


### 107. [Physics-Guided Flow Matching for CT Image Reconstruction](https://arxiv.org/abs/2608.28256)

**<font color=#1a73e8>作者：</font>** Davide Evangelista  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep generative models have recently emerged as powerful priors for solving ill-posed inverse problems in CT, with diffusion-based approaches achieving state-of-the-art reconstruction performance. However, diffusion models typically rely on stochastic sampling procedures, long inference trajectories, and carefully tuned noise schedules, which can limit computational efficiency and numerical stability, especially at high spatial resolutions. In this work, we investigate Flow Matching as an alternative generative prior for CT reconstruction. We train a high-resolution Rectified Flow Matching model on 256x256 chest images from the Mayo Clinic Low-Dose CT dataset. To mitigate overfitting and limited anatomical variability, we employ a two-stage training strategy consisting of an initial phase with strong, anatomically informed data augmentation, followed by a fine-tuning phase with reduced or no augmentation to refine structural fidelity. The resulting model is capable of generating high-quality and anatomically coherent CT-like images, serving as a strong learned prior. We then evaluate multiple reconstruction methods specifically designed for Flow Matching models, including Plug-and-Play Flow, FlowDPS, Flower, and Flow-Priors (ICTM), and compare them against state-of-the-art diffusion-based reconstruction algorithms such as DDRM, DPS, and DiffPIR. Experimental results across several CT inverse problem settings show that Flow Matching-based approaches consistently outperform diffusion-based methods in terms of PSNR, SSIM, and perceptual quality, while requiring fewer sampling steps. Finally, we publicly release the trained Flow Matching model and accompanying code to facilitate reproducibility and future research. Overall, this work demonstrates that Flow Matching provides a stable, efficient, and effective alternative to diffusion models for high-resolution CT image reconstruction.

---


### 108. [SinkSLOT: Sinkhorn via Sparse Lifted Optimal Transport](https://arxiv.org/abs/2608.28262)

**<font color=#1a73e8>作者：</font>** Ian Hsieh, Soumya Snigdha Kundu, Tom Vercauteren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Entropic optimal transport (EOT) has been shown to offer a computationally tractable approximation to exact optimal transport. However, the standard Sinkhorn-Knopp algorithm has two main limitations. First, given discrete measures with $N$ points, each iteration requires $O(N^2)$ operations, which restricts its use on large-scale datasets (e.g. $N\geq10^4$). Second, it uses the independent coupling as a reference measure for regularisation. This assigns mass to high-cost transport edges at moderate regularisation strengths. We propose SinkSLOT, which addresses both limitations by putting forth the expected sliced lifted transport plan as a natural way to sparsify the Gibbs kernel with a non-independent prior coupling. We prove that: 1) SinkSLOT converges; 2) with $L$ slices, each resulting sparse Sinkhorn iteration costs $O(LN)$; and 3) the resulting objective is a divergence requiring no debiasing. Experiments on synthetic benchmarks show that SinkSLOT delivers substantial speedups over state-of-the-art dense and sparse EOT methods. We also demonstrate the applicability of the proposed divergence in a gradient flow experiment. The code is publicly available at this https URL.

---


### 109. [Residual-Guided Randomized Neural Networks](https://arxiv.org/abs/2608.28267)

**<font color=#1a73e8>作者：</font>** Mushir Akhtar, M. Tanveer, Mohd. Arshad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Randomized neural networks enable fast and analytically tractable training by fixing the input to hidden layer parameters at random and learning the output weights in closed form; however, their performance critically depends on a single uninformed draw of hidden units. This one shot and task uninformed feature construction often leads to redundant representations and suboptimal utilization of model capacity. To address this limitation, we propose a simple and broadly applicable residual guided procedure that greedily constructs the hidden layer using a closed form residual decrease criterion. At each stage, we (i) generate a pool of random candidate units, (ii) score each candidate by the exact reduction it induces in the ridge regularized objective, (iii) select the top k units, and (iv) refit the readout in closed form using the standard design with direct input links. This procedure yields a progressive training process with a guaranteed monotonic decrease of the training objective. The method is model agnostic: only the candidate generation is architecture specific, while the scoring selection refitting loop is shared across models. Extensive experiments on 71 benchmark datasets from the UCI repository, covering both binary and multiclass classification tasks, demonstrate that the proposed residual-guided models consistently outperform their baseline counterparts in terms of accuracy, stability, and overall ranking performance.

---


### 110. [RECAST: Recent & Context-Aware Sampling for Test-Time Adaptation in Streaming Biosignals](https://arxiv.org/abs/2608.28271)

**<font color=#1a73e8>作者：</font>** Yong-Yeon Jo, Junho Song, Joon-myoung Kwon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Streaming biosignals vary across subjects and drift over time, so population-trained models lose accuracy during long-term monitoring. Test-time adaptation (TTA) enables online personalization by updating the model on incoming samples. But in a stream, a basic question is left open: \emph{which samples should drive each update?} Using all buffered samples blurs the update with irrelevant segments. Using only the latest segment makes the update noisy and unstable. The most useful samples are recent, aligned with the current physiological state, and reliable enough to learn from. We propose \textbf{RECAST} (REcent \& Context-Aware Sampling for TTA), a lightweight sampling module for buffered TTA frameworks. RECAST builds each adaptation batch from three signals: temporal recency, contextual similarity, and predictive reliability. It changes only which samples are used, leaving the model and the training objective unchanged. On two blood-pressure datasets, RECAST improves estimation accuracy and trend tracking over baselines and ablations. The per-patient gains are statistically significant on both datasets, with broad improvement on the regular benchmark and gains concentrated on the hardest patients in the emergency-department setting. RECAST stays practical, adding only sub-second latency per segment on a single GPU and CPU core.

---


### 111. [Non-Uniform Quantisation for 3DGS Compression](https://arxiv.org/abs/2608.28272)

**<font color=#1a73e8>作者：</font>** Bert Van hauwermeiren, Patrice Rondao Alface, Adrian Munteanu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has emerged as a powerful technique for novel view synthesis, yet its high bitrate requirements pose significant challenges for storage and transmission. To enable practical applications and ensure interoperability within the 3DGS ecosystem, standardised compression formats are essential. In this paper, we propose a novel non-uniform quantisation scheme specifically tailored for 3DGS models. Our approach adapts to the underlying data distribution by applying importance-weighted quantisation and eliminating post-voxelisation redundancy through importance weighted merging. Extensive evaluations on benchmark datasets demonstrate that our method achieves state-of-the-art compression performance. Furthermore, the proposed scheme is compatible with any point-cloud-based representation and is intended as a formal contribution to the upcoming MPEG 3DGS compression standardisation activities.

---


### 112. [Learning to Transfer Across Modes: Towards Unified Urban Mobility Forecasting](https://arxiv.org/abs/2608.28273)

**<font color=#1a73e8>作者：</font>** Yixuan Zhao, Man Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Urban transportation systems consist of multiple mobility modes that coexist within the same city and exhibit complex interdependencies, leading to correlated demand dynamics across modes. However, forecasting demand jointly across different modes remains challenging due to substantial heterogeneity in space and the limited availability of historical data for emerging modes. Existing forecasting methods are largely developed for individual mobility modes and implicitly assume compatible spatial structures between source and target systems, which severely restricts their applicability in multi-modal settings. To address these challenges, we propose \textbf{TransMod}, a unified framework for urban mobility demand forecasting that enables effective knowledge transfer across heterogeneous mobility modes. TransMod constructs a shared zone-level spatial representation that aligns mobility systems with different spatial granularities into a common space, thereby reducing structural mismatch and distributional shift. Built on this unified representation, TransMod further learns transferable spatio-temporal patterns from data-rich source modes and adapts them to data-scarce target modes, alleviating the dependence on extensive target-domain histories. Extensive experiments on real-world datasets demonstrate that TransMod consistently outperforms existing approaches and provides robust forecasting performance under limited target data.

---


### 113. [An algebraic proof of Colombo's difference-power determinant conjecture](https://arxiv.org/abs/2608.28274)

**<font color=#1a73e8>作者：</font>** Kun Li, Li Tie, Peng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Let $n\ge2$ be even, let $\lambda=(\lambda_1,\ldots,\lambda_n)\in\mathbb{R}^n$ have pairwise distinct coordinates, and define the difference-power matrix \[ A_d(\lambda) := \bigl[(\lambda_r-\lambda_s)^d\bigr]_{r,s=1}^n, \qquad d\in\mathbb{N}. \] In 1928, Colombo proved that $\det A_{n-1}(\lambda)\ne0$---and hence $\det A_{n-1}(\lambda)>0$---and that $\operatorname{rank} A_d(\lambda)=d+1$ for $0\le d<n-1$. He conjectured that \[ \det A_d(\lambda)\ne0 \qquad\text{for every } d\ge n-1. \] For even $d$, the conjectured nonsingularity follows from previously published results on distance-power matrices. The remaining open cases were therefore the supercritical odd exponents $d\ge n+1$. We prove nonsingularity for all these odd exponents, thereby completing Colombo's conjecture. Consequently, \[ \operatorname{rank} A_d(\lambda)=\min\{n,d+1\} \qquad(d\in\mathbb{N}). \] Our proof converts a hypothetical kernel vector into a real binary form having more projective real linear factors, counted with multiplicity, than its real Waring length permits.

---


### 114. [GeoFF3D: Coordinate-Anchored Feed-Forward Reconstruction for Large-Scale UAV Mapping](https://arxiv.org/abs/2608.28288)

**<font color=#1a73e8>作者：</font>** Xiang Yang, Yongli Wang, Yunsheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing feed-forward 3D reconstruction methods typically process a bounded number of images and recover cameras and geometry in local or internally normalized frames. Extending them to large-scale UAV mapping requires scalable multi-chunk processing and reliable aggregation, while full Sim(3) alignment can become unstable for near collinear trajectories. We present GeoFF3D, which combines a coordinate-anchored model with a spatial large-scale reconstruction framework (SLRF). The model uses georeferenced camera translations and optional geometric priors to predict camera poses and dense point maps directly in a gravity-aligned Z-up metric frame. SLRF partitions images into spatially overlapping chunks, propagates shared-view priors, and aggregates local reconstructions hierarchically, while remaining applicable to different bounded-view models. Across nine aerial mapping blocks, GeoFF3D achieves the best average reconstruction quality, improving F@5 from 0.829 for Pi3X + SLRF to 0.877. On long UAVScenes sequences, it reaches 0.848, compared with 0.687 for Pi3X + SLRF and 0.451 for the strongest evaluated SLAM/streaming baseline. GeoFF3D reconstructs 2,000 images in approximately five minutes, demonstrating scalable and robust large-scale UAV this http URL code is available at this https URL.

---


### 115. [Memristive-Friendly Hadamard Reservoir Computing: Structured, Multiplier-Free Recurrences at Scale](https://arxiv.org/abs/2608.28295)

**<font color=#1a73e8>作者：</font>** Andrea Ceni, Gianluca Milano, Carlo Ricciardi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reservoir Computing (RC) designs Recurrent Neural Networks around a fixed, i.e., untrained, recurrent layer, and is a natural candidate for neuromorphic hardware. Memristive-friendly reservoirs derive the neuron dynamics from memristive-device kinetics, but still rely on dense recurrent matrices, which are expensive to realize physically. In this paper, we replace the dense matrix with a structured orthogonal operator, built from sign diagonals, a permutation, and a fast Walsh-Hadamard transform. The operator is multiplier-free, requires $O(N)$ parameters and $O(N\log N)$ operations per step, and is never materialized as a matrix. We instantiate it in a standard and in a memristive-friendly Echo State Network, with one binary input connection per unit.
Our mathematical analysis shows that exact orthogonality yields an echo state condition that is tight in the recurrent scaling, and a noise response that is predictable at design time. Moreover, the operator mixes the whole state in a single application. Experiments on twenty classification and seven regression benchmarks, at reservoir sizes up to $N = 8192$, show that the structured models match dense orthogonal reservoirs, and achieve better mean performance than the cycle reservoir by a margin that widens with size. Furthermore, we time the recurrent step on three hardware platforms, where it is up to $50\times$ faster than a dense product and $10^4\times$ smaller in memory. Finally, we ablate the operator and measure the response to noise, quantization, device mismatch and discrete faults.

---


### 116. [Conditional Visual Evidence Utility: State-Dependent Rank Reversals in Frozen Vision-Language Encoders](https://arxiv.org/abs/2608.28316)

**<font color=#1a73e8>作者：</font>** Yunxuan Fang, Xinhe Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Static importance scores compress visual evidence into a single ranking, but the value of remaining evidence can change after one cue has been observed. We study this possibility in controlled compositional visual search, where color, shape, and texture evidence can be independently exposed and their conditional marginal utility measured across acquisition states. In a held-out confirmation on 800 scenes, frozen OpenCLIP and SigLIP exhibit robust state-dependent rank reversals that concentrate in candidate-overlap regimes designed to induce ordering changes. The structure persists across two evidence-accumulation constructions and ten equivalent query wordings, but disappears under query-scene derangement. We also ask whether these reversals matter for decisions. In a post-confirmation exploratory matched-first-action analysis, reranking only after the first acquisition yields positive step-2 utility when decisions are selected under one evidence mode, wording, or backbone and evaluated under another. Together, these results show that evidence importance is state-dependent in this controlled setup and that updating an evidence ordering can retain decision-relevant value across evaluator changes. They motivate evaluating vision-language evidence use conditionally rather than through a single static ranking, while providing a measurable target for future adaptive evidence-selection methods.

---


### 117. [BanglaMed-QA: A Question Answering System for Healthcare Support in Bangla](https://arxiv.org/abs/2608.28329)

**<font color=#1a73e8>作者：</font>** Rowzatul Zannat, Abdullah Al Shafi, K. M. Azharul Hasan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical question answering (QA) systems have become crucial tools for providing reliable health information. But they remain very unexplored for low-resource languages like Bangla due to limited datasets and systems tailored to these languages. To address this, we introduce BanglaMed-QA, a robust QA system specifically designed for the Bangla medical domain. The process begins with building a structured medical knowledge base that includes 4,493 QA pairs in 9 categories under 506 diseases. To improve semantic comprehension, domain-specific root word dictionaries and synonym sets are proposed, in addition to part-of-speech tagging for anaphora resolution. We adopt supervised machine learning models in which SVM is found to be the best model to categorize questions. Multiple similarity metrics, including cosine, Jaccard, BM25, and Levenshtein, are applied with soft and hard voting methods for query matching. The performance of the QA system has been evaluated in two aspects, with a 95% F1 score in an automated evaluation and an average human satisfaction rating of 0.9 out of 1.0. This validates the real-world application of BanglaMed-QA in closing the healthcare information gap for Bangla speakers.

---


### 118. [Real-Valued Hyperdimensional Sequence Representations with Hadamard Product Binding and Shift Equivariance](https://arxiv.org/abs/2608.28334)

**<font color=#1a73e8>作者：</font>** Kenny Schlegel, Dmitri A. Rachkovskij, Denis Kleyko 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Encoding temporal order is a fundamental requirement for sequence representations in Hyperdimensional Computing. Fractional Power Encoding provides similarity-preserving position vectors whose inner products approximate shift-invariant kernels, and it supports shift-equivariant transformations of encoded sequence representations. However, standard formulations of Fractional Power Encoding are primarily designed for binding operations such as circular convolution or complex-valued multiplication, which limits their compatibility with Hadamard product binding of real-valued vectors. This paper develops real-valued position encodings motivated by Random Fourier Features, aiming to retain the desirable properties of Fractional Power Encoding while supporting Hadamard-based operations. We propose three real-valued position-encoding variants: a real-valued baseline based on the inverse Fourier transform, and Sinusoid and Cosine-only representations derived from Random Fourier Features. Among them, the Sinusoid variant provides an explicit algebraic shift operator, allowing temporal shifts to be applied directly to the vector-encoded sequence representation without re-encoding the shifted sequence. Experiments on time-series classification datasets show that the proposed real-valued representations achieve performance comparable to standard Fractional Power Encoding while enabling computationally efficient Hadamard product binding. The Sinusoid variant offers the most favorable trade-off, combining efficient real-valued implementation with exact shift-equivariant transformations.

---


### 119. [Cross-Spectral Dense Correspondence for Multimodal Spectral Medical Imaging](https://arxiv.org/abs/2608.28341)

**<font color=#1a73e8>作者：</font>** Eric L. Wisotzky, Jost Triller, Simon W. Härtl 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise dense correspondence is a fundamental prerequisite for multimodal spectral imaging systems that fuse disparate wavelength ranges for subsequent analysis in medical and scientific imaging. Corresponding image points are often observed with non-overlapping spectral sensitivities, leading to wavelength-dependent contrast changes, intensity inversions, and appearance shifts for which dense ground truth is difficult to obtain and conventional RGB-based training data provides only limited supervision. We address this data gap by introducing a sensor-agnostic cross-spectral modulation protocol on established correspondence benchmarks with intensity input projection, and by proposing a synthetic cross-spectral correspondence benchmark simulating physically plausible radiometric differences. Evaluation on several modern dense correspondence backbones trained with our unified cross-spectral protocol showed substantial improvements under severe spectral mismatch while maintaining performance on standard RGB benchmarks. Ablation experiments show that view-dependent channel selection and nonlinear radiometric transformations provide complementary robustness, indicating that the primary limitation of existing models is not their structural matching capacity but the mismatch between training distribution and spectral characteristics of the target image pair. Qualitative evaluations on heterogeneous medical spectral acquisition systems demonstrate the practical relevance of the proposed training data augmentation protocol as an enabler for spatially coherent spectral fusion in HSI workflows.

---


### 120. [Denoising-Aware Temporal Point Cloud Completion for 3D Crop Architecture Recovery and Phenotypic Trait Extraction](https://arxiv.org/abs/2608.28343)

**<font color=#1a73e8>作者：</font>** Mrudul Mittal, Soumyashree Kar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-throughput phenotyping depends on accurate 3D reconstruction of plants across growth stages, yet the development and evaluation of temporal completion methods are limited by the lack of datasets with complete geometric ground truth. To address this challenge, we introduce SynthCrop4D, a procedurally generated synthetic dataset of temporally evolving plant point clouds that provides controllable noise, occlusion, and complete plant geometry for benchmarking reconstruction methods. Using this dataset, we evaluate a two-stage pipeline that combines spatial denoising and temporal point cloud completion. First, a denoising module removes structural artifacts from raw laser-scanned point clouds. The resulting data are then processed by an Adaptive Temporal PoinTr model that reconstructs the current growth stage (t) using information from the previous stage (t-1), enabling recovery of regions missing due to self-occlusion. We evaluate the proposed framework on both SynthCrop4D and the real-world Pheno4D dataset (tomato and maize) under settings with and without denoising. Results show that denoising substantially improves reconstruction quality, with the best configuration achieving a Chamfer Distance of 0.0061 on SynthCrop4D (Temporal PoinTr + Mamba-DG) and an F-Score of 0.2080 on Pheno4D (Vanilla PoinTr + Mamba-DG). We further demonstrate the use of completed point clouds for phenotypic trait extraction, including plant height, canopy width, and convex hull volume, obtaining hull-volume MAEs of 0.021 on synthetic data and 0.343 on real data. Together, SynthCrop4D and the proposed pipeline provide a benchmark and methodology for temporal plant reconstruction and high-throughput crop phenotyping.

---


### 121. [AGENT-O: A Semantic Agent Card Framework for Interoperable and Governed Healthcare AI Agents](https://arxiv.org/abs/2608.28345)

**<font color=#1a73e8>作者：</font>** Pengze Li, Cui Tao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AGENT-O is a modular ontology framework that defines a semantic Agent Card for representing health-oriented AI agent systems and supports assessment of reporting completeness in scientific publications. AGENT-O was developed as an OWL 2/RDF ontology covering runtime, models, workflow, tools, clinical use, evaluation, provenance, governance, and reporting assessment. Evaluation included ontology inventory, OWL-RL reasoning, three SHACL suites, 12 SPARQL competency queries, three cases, and model-assisted reporting-completeness assessment of 279 papers across five dimensions. The ontology contained 1,962 RDF triples and 1,922 Protege axioms, with 252 active classes, 198 active object properties, and 51 datatype properties. All SHACL suites conformed on example graphs, all competency queries returned prespecified evidence, and all 279 papers were scored. Incomplete reporting was highest for runtime/architecture (84.6%), governance/safety (82.8%), and provenance/reproducibility (78.1%), compared with evaluation (25.8%) and benchmark-process alignment (29.8%). AGENT-O supported semantic Agent Card representation and reporting assessment while revealing an evaluation-specification gap: evaluation and benchmark procedures were reported more consistently than runtime architecture, governance, and reproducibility. AGENT-O provides a reusable ontology, semantic Agent Card profile, and reporting-completeness workflow for structured reporting and gap identification, but does not assess agent quality or deployment readiness.

---


### 122. [False-CSI Attacks in Power-Domain NOMA for 6G: A Threat Taxonomy and System-Level Impacts](https://arxiv.org/abs/2608.28351)

**<font color=#1a73e8>作者：</font>** Samira Jafarli, Aysha Ebrahim, Suleyman Uludag  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Power-domain non-orthogonal multiple access (NOMA) remains a widely studied technique for improving spectral efficiency and supporting dense connectivity in beyond-5G and 6G networks. Its main operating mechanisms, however, depend on the integrity of channel-state information (CSI). Power allocation, user ordering, pairing, clustering, and beamforming can all be distorted when the CSI consumed by the base station is deliberately biased rather than merely noisy. This article examines false CSI as an attack surface in power-domain NOMA. We organize the threat space using a compact taxonomy with two primary axes: magnitude, which distinguishes underreporting from overreporting, and ordering effect, which distinguishes order-preserving, boundary, and order-reversing attacks. We then show how coordinated false- CSI behavior, group-changing attacks, direction forgery, pilot spoofing, training-phase injection, and RIS-induced channel manipulation extend this basic taxonomy. Finally, we map each attack family to system-level impacts on power allocation, SIC reliability, scheduler behavior, fairness, throughput, and secrecy. The central message is that false CSI should be treated not only as a channel-estimation problem, but also as a control-input integrity problem for 6G NOMA.

---


### 123. [Optimal Adversarial Testing: Extracting Honest Test Results from Dishonest Test Takers](https://arxiv.org/abs/2608.28362)

**<font color=#1a73e8>作者：</font>** Owen Cox, April Xu, Weiyu Xu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In applications, it is often required to test objects or people to determine their qualities in terms of certain metrics. However, besides being naturally noisy, the test results can be corrupted by adversarial behaviors of objects or people being tested (test takers). For example, dishonest test takers can cheat in the exams to distort the test results. With the development of AI technologies, such distortions driven by cheating using AI technologies are becoming more commonplace and severe. In this paper, we propose optimal testing strategies which can still recover needed test results even if there are cheaters polluting the results. The proposed testing strategies will optimally re-test selected group of test takers using different testing security measures. We determine the optimal testing strategies using a dynamic programming method.

---


### 124. [Real-Time Musculoskeletal Surrogates for Pediatric Cerebral Palsy: a Credibility Pilot](https://arxiv.org/abs/2608.28371)

**<font color=#1a73e8>作者：</font>** Mohammad Arif Ul Alam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time musculoskeletal (MSK) surrogates could support personalized rehabilitation for children with cerebral palsy (CP), but their credibility depends on subject-wise evaluation, low inference latency, and calibrated uncertainty. We develop a subject-conditioned causal neural surrogate using OpenSim-derived static parameters, temporal joint kinematics, true muscle capacities, and training-only perturbations. On a real pediatric CP gait dataset comprising nine children, we use leave-one-subject-out validation on six development subjects and evaluate a frozen configuration once on three locked test subjects. The surrogate accurately reproduces musculotendon lengths (R-square = 0.92 in development validation and approximately 0.95 on locked subjects; nRMSE < 8%) while requiring only sub-millisecond to few-millisecond neural inference, well below a 100 ms interactive-rehabilitation target. In contrast, direct muscle-force estimation remains unstable at this small, heterogeneous scale: pooled metrics can overstate within-subject, per-muscle accuracy. A Monte Carlo credibility pilot further shows that propagating only +/-5% anthropometry and muscle-capacity variation produces severely overconfident nominal 90% intervals (approximately 4% force coverage and below 1% MT-length coverage). These results establish a leakage-free evaluation and credibility framework for pediatric MSK surrogates, while identifying force modeling and epistemic uncertainty as the central next challenges for clinically credible digital twins.

---


### 125. [MAP: A Benchmark on Multimodal Accessibility Planning for Real World Places](https://arxiv.org/abs/2608.28384)

**<font color=#1a73e8>作者：</font>** Jason Armitage, Ioannis Tsochantaridis, Linda Mazzone 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce MAP, the first benchmark to evaluate multimodal AI systems as assistants for users with accessibility requirements when planning visits to places in the real world. In our evaluation, systems are presented with requests to verify or recommend a point of interest meeting an accessibility requirement. MAP contains two novel assessments: Claim verification for accessibility planning assesses if information on places and stated accessibility features is supported and identifies places that satisfy requested accessibility features. Visual evidence retrieval for accessibility planning checks if a multimodal AI system can select visual evidence for the requested place and accessibility feature. Our methodology supports comparison of AI systems in a setting where place information and accessibility information can change over time by evaluating systems and refreshing ground truth data at scheduled times. The benchmark is based on automatic rating and human rating for a proportion of responses.

---


### 126. [GraspHOI: Full-Body 3D Human-Object Reconstruction with Finger-Level Grasps from a Single In-the-Wild Image](https://arxiv.org/abs/2608.28386)

**<font color=#1a73e8>作者：</font>** Semin Kim, Haechan Shin, Jongyoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing monocular full-body 3D human-object interaction (HOI) methods do not combine explicit finger-level grasp optimization with category-agnostic object reconstruction. Despite plausible body-object configurations, their fingers may float from or penetrate objects instead of forming a grasp. We present GraspHOI, the first framework that reconstructs a full-body 3D HOI from a single image while explicitly optimizing finger articulation against the reconstructed object. GraspHOI recovers object geometry directly, without predefined meshes or a fixed category vocabulary. It reconstructs the body, hands, and object separately, aligning them in metric camera space via depth-based registration and image-space alignment. Occlusion-aware palmar correspondences seat the object against the grasping hand, and contact-aware optimization refines arm and finger articulation to form surface contact without excessive penetration. Across four benchmarks and six baselines, GraspHOI improves relative human-object placement, hand accuracy, and contact plausibility. Full pipeline code will be released.

---


### 127. [Timing-Aware Repurchase Prediction for Web-Scale E-Commerce: Survival Models for Multi-Surface Grocery Recommendation](https://arxiv.org/abs/2608.28393)

**<font color=#1a73e8>作者：</font>** Akshay Kekuda, Shreeranjani Srirangamsridharan, Ishan Bhatt 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Repurchase recommenders in e-commerce are commonly framed as a binary question asking "will this customer buy this item within W days", a formulation that requires a separately trained model for every horizon of interest. We replace this stack with survival models that predict time-to-repurchase directly, and evaluate them on millions of customers from a major grocery e-commerce platform across more than thirty ablation configurations. Our study makes three contributions. First, an empirical hazard analysis reveals a slightly decreasing marginal hazard (k ~ 0.9), differing from the common intuition that grocery items become more likely to be repurchased the longer since the last purchase (increasing hazard, k > 1). Log-Normal achieves the best marginal fit (R^2 = 0.998) and the best ranking, despite Weibull providing the best conditional residual fit, revealing an apparent discrepancy we analyze in detail. Second, a single Accelerated Failure Time (AFT) model replaces three per-horizon binary classifiers, matching or exceeding each at its own horizon while using roughly 3x fewer total trees. Feature importance reshuffles under the survival objective: channel-cadence and recency signals rise while aggregate frequency counts fall. Third, a 4-parameter parametric calibration maps raw survival CDFs to per-horizon probabilities with zero cross-horizon monotonicity violations. Calibration quality varies by an order of magnitude across the AFT family: Exponential AFT (Weibull k=1) achieves expected calibration error (ECE) ~1e-4, roughly 10x lower than Log-Normal, while ranking metrics agree within 0.3% relative. We adopt Exponential AFT for probability-consuming surfaces and Log-Normal for pure ranking, exposing a principled calibration-ranking trade-off within a single AFT family.

---


### 128. [How Far Can 5,500 Hours of Driving Take You? A Scaling Law Analysis of Video Diffusion Models](https://arxiv.org/abs/2608.28404)

**<font color=#1a73e8>作者：</font>** Victor Besnier, Anh-Quan Cao, Elias Ramzi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation for autonomous driving cannot follow the web-scale route: driving data is expensive to collect, bound by privacy requirements, and cannot be scraped at will, so models must make the most of a fixed corpus. We present a systematic scaling-law study of video diffusion models trained from scratch on driving data: a family of models from 1M to 9B parameters, trained at different exposures on up to 5,500 hours of driving. Validation loss follows consistent power laws in both model size and training exposure, answering the questions that shape a training budget: whether compute is better spent on longer training or on a larger model, and whether more data is needed. Loss improves much faster with training exposure than with model size, making longer training the most effective way to improve a fixed model under limited compute. However, larger models continue to achieve lower asymptotic loss, so compute-optimal scaling still favors increasing model size when sufficient compute and data are available. Guided by these laws, we train a 9B-parameter model, to our knowledge the largest video diffusion model trained from scratch on driving data: it sets a new open-source state of the art for driving video generation, as measured on nuScenes. Our code and pretrained models are available at this https URL. NATIX is separately releasing the underlying driving data in stages.

---


### 129. [Exploiting Per-Core Leakage: Electromagnetic Side-Channel Monitoring of Multicore Architectures](https://arxiv.org/abs/2608.28412)

**<font color=#1a73e8>作者：</font>** Daehyeon Bae, Sujin Park, Insup Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multicore processors are increasingly adopted in embedded systems to meet growing performance demands. However, physical side-channel analysis of multicore architectures remains underexplored, as obtaining usable leakage is inherently challenging. Consequently, side-channel security research on such systems has lagged far behind, leaving a critical security gap. To address this gap, we reveal the electromagnetic leakage mechanisms in multicore architectures and, for the first time, demonstrate per-core leakage exploitation, thereby enabling physical side-channel analysis for these systems. As a practical extension, we present a non-intrusive side-channel monitoring method that achieves per-core granularity. To validate its feasibility and practicality, we implement a prototype on a heterogeneous SoC platform with an RF front-end, and evaluate on a commercial off-the-shelf quad-core embedded system, the Raspberry Pi 4B with ARM Cortex-A72 cores.

---


### 130. [Between Algorithm (AI) and Intuition (Human): Preserving Designer Agency in AI-Assisted Sensemaking of Qualitative UX Data](https://arxiv.org/abs/2608.28420)

**<font color=#1a73e8>作者：</font>** Md Haseen Akhtar  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The integration of AI into qualitative design research presents a fundamental tension: how do we leverage AI while preserving the subjective, intuitive judgments that define design expertise? This paper examines this question through a case study of analyzing 20 user responses about video conferencing platforms for educational contexts. We argue that AI sensemaking tools risk flattening the rich data patterns, amplifying contradictory textures of user feedback into sterile categories thereby transforming design research from an interpretive craft into a mechanical sorting exercise (rigid and formal). Through comparative analysis of AI-assisted sensemaking versus human-centered approaches to the same dataset, we identify when algorithmic efficiency enhances understanding and when it diminishes the designer's interpretive agency (uncovering hidden needs, critical enquiry, what if enquiries, making decisions, having trade-offs). We present a framework for augmented sensemaking that positions AI as an instrument for amplifying human judgment rather than replacing it. Our findings suggest that the most valuable role for AI in design research is not to eliminate subjectivity, but to make it more intentional, reflective, and accountable.

---


### 131. [Euclidean Fourier Neural Operators](https://arxiv.org/abs/2608.28425)

**<font color=#1a73e8>作者：</font>** Nathanael Bosch, Niklas Frederik Schmitz, Michael F. Herbst  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fourier neural operators (FNOs) provide an efficient framework for learning mappings between function spaces as they are, by construction, independent of the grid resolution at which they are trained and evaluated. However, FNOs are not independent of the periodic domain they are applied to: their discrete spectral weights are indexed by integer Fourier mode numbers, which correspond to physical wavevectors. When applied to a different domain, the same trained weights act at different wavevectors, and the FNO silently represents a different operator. This makes FNOs unsuitable for tasks where transfer across domains is crucial. We propose Euclidean Fourier neural operators~(EFNOs) as a domain-independent alternative to FNOs. By parameterizing the spectral kernel as a continuous function of the physical wavevector, the EFNO can learn operators that act consistently across periodic domains of varying shape and size. We evaluate the EFNO on a simple heat equation and on a practically relevant materials science task of learning exchange-correlation potentials across different crystal structures, and demonstrate that the EFNO is able to generalize to unseen grid sizes and domains.

---


### 132. [Lossy Event Compression: From Event Stream Distortion to Task Performance](https://arxiv.org/abs/2608.28429)

**<font color=#1a73e8>作者：</font>** Zahra Rezaee, Catarina Brites, João Ascenso  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras generate asynchronous, sparse data streams with microsecond temporal resolution, but in moderate-to-high motion scenes they can produce as many as hundreds of millions of events per second, creating significant bandwidth and storage challenges. Lossy compression is therefore essential for practical deployment, yet existing event stream distortion metrics fail to reliably predict compression-induced degradation at the task level, forcing codec optimization to rely on expensive task-specific evaluations. To address this gap, this paper introduces two fundamentally different event compression pipelines: i) an aggregation-based pipeline that converts the event stream into polarity-based histogram frames for compression with the conventional image codec JPEG 2000, and ii) a frame-free point cloud-based pipeline that codes events natively as 3D points using the octree-based codec G-PCC. Both pipelines are then assessed within a unified task-driven evaluation framework that relates event stream distortion to downstream application performance across four representative tasks: i) video reconstruction, ii) object detection, iii) optical flow estimation, and a delay-sensitive task iv) asynchronous feature tracking under a reference-relative protocol. Building on this framework, five classification-based distortion metrics are applied to event compression for the first time, to the best of the authors' knowledge, and benchmarked against existing event stream metrics. Experimental results demonstrate that the proposed metrics reliably predict compression-induced task degradation across different coding frameworks. This demonstrates that event stream distortion assessment can be an efficient alternative to repeated task-specific evaluation, providing direct guidance for the development and optimization of future event data coding solutions.

---


### 133. [Fidelity Is Not Enough: Dispatch-Level Instrumentation for Agentic Datasheet Extraction](https://arxiv.org/abs/2608.28439)

**<font color=#1a73e8>作者：</font>** Qing Ye, Meng-Hsuan Lin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> One model passed our fidelity check without ever opening the datasheet. We found it while qualifying models for an internal extraction service: a structured-output constraint had silently disabled tool use, and the model answered anyway, with fabricated source text. Only the per-tool trace exposed it. Fidelity -- whether an extracted value matches the source -- is the standard measure for agentic document extraction, and it scores that run a success. We therefore log every tool call in an agentic benchmark of 25 hand-curated claims over three components, with 12 more on a fourth, 37 in all. From that dispatch record we build two instruments: a rule-based failure-attribution classifier, and a silent-failure detector whose two rules check only which tools were called, never the extracted value. The detector raises no flag on 207 clean fidelity-passing extractions across three model families, and recovers all 50 planted faults that withhold exactly the tools its rules check. The two results are not symmetric: the first bounds the false-positive rate, the second is recall by construction, and detection power against runs that call their tools and still answer wrongly is unmeasured. A second, independent oracle, a causal chamber that tests whether the datasheet's claims hold under physical measurement, is intentionally partial: it confirms only what the apparatus can exercise, a verifiable envelope of 2 of those 37 claims, and we give a taxonomy of why the rest are not physically gradable. Under a controlled perturbation, fidelity passes throughout while the chamber verdict flips exactly at the measurement uncertainty. Across three deployed model stacks (one destabilised by its serving stack, not by any capability gap) the tool layer buys portability and observability rather than accuracy, and earns its premium only once a document outgrows the context window.

---


### 134. [Prompt-Guided Interactive Segmentation of Interstitial Lung Disease in Thoracic CT](https://arxiv.org/abs/2608.28453)

**<font color=#1a73e8>作者：</font>** Vasilis Dedousis, Lubnaa Abdur Rahman, Lorenzo Brigatο 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of interstitial lung disease (ILD) patterns is essential for quantitative disease assessment and longitudinal monitoring. However, existing approaches remain limited by relying on dense annotations and producing static predictions that cannot be refined, motivating interactive approaches. While promptable models show promise in interactive segmentation, their adaptation to ILDs remains largely unexplored. To address this gap, we investigate prompt-guided foundation models for ILD refinement and present, to the best of our knowledge, the first adaptation of MedSAM2 for interactive 3D ILD segmentation on thoracic CT. We investigate three fine-tuning strategies and multiple clinically motivated prompts: bounding-boxes (BBox), point, lasso, and scribble. On a dataset spanning seven ILD patterns and healthy lung tissue, full model fine-tuning performed best, improving the average Dice score by 4.7 percentage points over this http URL BBox prompts achieve the strongest performance, non-native MedSAM2 interactions such as lasso and scribble prompts also prove effective. Finally, we present and evaluate a proof-of-concept end-to-end workflow in which MedSAM2 is initialized from an automatic segmentation prior and subsequently refined using radiologist prompts. Model weights and plug-ins made available at: this https URL.

---


### 135. [Acquire, Repair, Preserve: A Diagnosis-Guided Post-Training Recipe for Small-Model Dialogue Game Agents](https://arxiv.org/abs/2608.28458)

**<font color=#1a73e8>作者：</font>** Nan Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interactive dialogue games test a capability that static benchmarks largely leave implicit: a model must carry state across turns, interpret feedback, and choose valid actions under changing constraints. We study this setting in the LM Playschool Challenge with a 2B open-weight model, and find that many failures are not only broad knowledge failures but also local decision failures: repeated guesses, malformed actions, and violations of feedback that the model has just seen. These diagnostics motivate a training recipe organized around three steps: acquire broad game participation through supervised fine-tuning, repair mechanically verifiable failures within one targeted dialogue-game family using turn-local preference pairs, and preserve general capabilities beyond these dialogue games. In the official final evaluation, our submission improves public clemscore from 10.67 to 38.92 and closed in-domain score from 13.41 to 41.17, while approximately preserving aggregate static performance (44.14 vs. 44.24 for the baseline). Out-of-domain clemscore remains low at 7.88, with the largest gains concentrated in unseen variants of the targeted family. Our results suggest that broad SFT brings most of the model's capability improvement; turn-local supervision can be effective when failure detection is precise, with observed transfer concentrated primarily within-family.

---


### 136. [LayerRecall: A State-Conditioned Memory Router for Long-Horizon Consistency in Video Generation](https://arxiv.org/abs/2608.28460)

**<font color=#1a73e8>作者：</font>** Yixuan Ding, Jiahao Kong, Wei Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion enables scalable long-video generation by producing chunks from a bounded recent context. While recency-based caching preserves local continuity, it evicts historical cues needed when subjects, objects, scenes, or attributes reappear. Existing memory mechanisms expose models to nonlocal history, but access alone does not ensure effective use. Our analysis reveals that video DiT layers exhibit distinct preferences for current, recent, and distant context, suggesting that long-range memory requires deciding both what to retrieve and where to use it. We introduce LayerRecall, a current-conditioned, layer-selective memory router that retrieves relevant historical K/V states and injects them only into backbone-specific memory-sensitive layers while preserving local attention elsewhere. To reduce reliance on scarce high-quality long-horizon videos and explicit memory-allocation labels, we further propose Cross-Horizon Prediction Matching (CHPM), which uses a privileged long-context reference to supervise the bounded-memory router in prediction space. Across 100 multi-shot evaluation prompts, LayerRecall achieves the best overall results on MemoBench and MovieBench while matching its backbone on VBench-Long, demonstrating stronger long-range recovery without sacrificing local continuity. Qualitative analyses further reveal memory-guided self-correction, whereby initially mismatched local attributes return to their historical appearance without resetting ongoing motion or scene structure. Additional analyses show cross-backbone portability and negligible inference overhead.

---


### 137. [Anatomy-Aware Promptable Segmentation with Online Interactive Training for AUTOPET V](https://arxiv.org/abs/2608.28461)

**<font color=#1a73e8>作者：</font>** Pablo Lozano-Jimenez, Sergio Romero-Tapiador, Ruben Tolosana  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present an anatomy-aware, promptable model for whole-body lesion segmentation in FDG and PSMA PET/CT, developed for the AUTOPET V challenge. The proposed method is built as family of nnU-Net-based models and trained in two stages: i) a pre-training stage that produces a strong initial segmentation, and ii) an online interactive stage that learns to exploit scribble prompts, refining the prediction over successive interactions. Anatomical context is incorporated through organ supervision using a single shared head that predicts lesions and organs from the same features, which reduces false positives arising from physiological uptake. Also as the tracer (i.e., FDG/PSMA) is not provided at inference, we add a tracer classifier based on image processing and a random forest over coronal MIP features, routing each study to a combined FDG+PSMA model or to a PSMA-specific model. Across four-fold cross-validation the organ-supervised model achieves the best and most stable performance, the interactive stage improves the Dice score monotonically with each prompt, and PSMA-specific training yields the strongest tracer-wise results.

---


### 138. [Quantum-Based Solutions for Security Enhancement in Open Radio Access Networks](https://arxiv.org/abs/2608.28480)

**<font color=#1a73e8>作者：</font>** Dzung Quoc Ngo, Tharmikka Raveendranathan, Tuan Anh Le 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open Radio Access Networks (O-RAN) introduce unprecedented flexibility, interoperability, and intelligence into next-generation wireless systems, but their disaggregated and software-defined architecture also expands the attack surface and creates new security vulnerabilities. Conventional cryptographic mechanisms, while effective against classical threats, may become insufficient in the presence of quantum-enabled adversaries. This article presents a comprehensive perspective on quantum security for O-RAN, examining how quantum-resilient mechanisms can enhance confidentiality, authentication, and trust across the RAN ecosystem. It discusses post-quantum cryptography (PQC), quantum cryptography, quantum authentication, and quantum-enhanced threat detection within a zero-trust architecture based on continuous verification, least privilege, and micro-segmentation. Their integration with the Near-Real-Time (Near-RT) RAN Intelligent Controller, O-Cloud, and open interfaces is analyzed, together with practical deployment considerations, technology maturity, and adoption timelines. Finally, open research directions are outlined toward secure, resilient, and future-proof O-RAN architectures for 6G networks.

---


### 139. [AcrossVAM1.0: Particle World Modeling for Text-Assisted Robot Video Prediction](https://arxiv.org/abs/2608.28491)

**<font color=#1a73e8>作者：</font>** Yafei Zhang, Nan Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting robot videos requires both precise motion reasoning and preservation of high-frequency appearance, yet monolithic pixel models entangle these objectives and often conceal their progress behind a strong last-frame baseline. We present AcrossVAM1.0, a lightweight, text-assisted video action model that factorizes future prediction into object-centric motion and dense appearance. A frozen SAM3-DLP codec decomposes four context frames into semantic particles for the robot, arm, and gripper, together with a background latent. A 0.28M-parameter spatio-temporal Transformer aligns particle identities, rolls their states forward, and is modulated by a frozen OpenCLIP instruction embedding through FiLM. A causal dual-stream decoder combines particle-rendered motion with appearance encoded exclusively from the last observed frame; a residual refiner and learned delivery mask produce five future frames without access to future appearance. On our VRS benchmark constructed from diverse real-robot trajectories, particle dynamics reduce trajectory error by 21.0\% over persistence. Across three delivery-mask seeds, AcrossVAM1.0 improves future-frame PSNR/SSIM from 19.97/0.796 to 20.573/0.8004, while raw particle generation improves motion-region PSNR from 11.89 to 13.23. The delivered model does not yet beat persistence in LPIPS, and correct-versus- shuffled language changes trajectory error by only 2.8--3.1%. We report these limitations alongside oracle, negative-control, multi-seed, and per-robot analyses. The results show that explicit particle dynamics are a promising low-dimensional interface for robot video prediction, while robust language grounding and appearance delivery remain the principal open challenges.

---


### 140. [REPLICANT: Learning Policies for Evading and Hardening Malware Detectors](https://arxiv.org/abs/2608.28499)

**<font color=#1a73e8>作者：</font>** Shae McFadden, Ilias Tsingenopoulos, Mario D'Onghia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To determine the real-world effectiveness of machine learning based malware detection, it is vital to evaluate its robustness against highly capable adversaries. However, state-of-the-art attacks do not effectively model realistic adversaries, as they often assume access to privileged information such as the training data, feature space, or confidence scores of the target. In this work, we present Replicant, a deep reinforcement learning framework that learns the realistic task of evasion under a strict label-only black-box threat model. Replicant learns a reusable policy on how to modify a malware sample and when to query the target, which transfers across samples, detectors, and feature spaces. Across seven Android malware detectors and three feature spaces, Replicant is the strongest and most query-efficient approach achieving a mean attack success rate of 78.8%, a relative improvement of 20.9%-39.2% over the state-of-the-art. Furthermore, when used for adversarial training, Replicant also outperforms the state-of-the art by producing detectors with more generalizable robustness. With Replicant we demonstrate that learning the task of evasion not only results in stronger attack performance but, crucially, provides a better signal for hardening malware detectors.

---


### 141. [Phoneme- and Word-Level Metrics Using Self-Supervised Speech Representations for Forced Alignment Evaluation](https://arxiv.org/abs/2608.28508)

**<font color=#1a73e8>作者：</font>** V.S.D.S.Mahesh Akavarapu, Michael Daniel, Gerhard Jäger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Forced alignment evaluation typically requires manually annotated timestamps, limiting large-scale and multilingual analysis. We introduce two corpus-level metrics based on self-supervised (SSL) speech representations for reference-free forced alignment evaluation: Phoneme-Cluster Mutual Information (PCMI) and Word Acoustic Consistency Score (WACS). PCMI measures agreement between aligned phoneme labels and clusters induced from SSL-speech representations, while WACS measures consistency of repeated word realizations using dynamic time warping similarity between word representation sequences. Using both random and systematic perturbations, we show that PCMI and WACS degrade consistently under alignment perturbations. We further analyze the metrics across multiple alignment systems on 85 languages from FLEURS, validate them against manually annotated alignments from 45 languages in DoReCo, and evaluate them on two phonologically complex low-resource languages. The metrics effectively separate high- and low-quality alignments and correlate strongly with timestamp-based alignment quality measures. Our results demonstrate that SSL-speech representations enable scalable, reference-free forced alignment evaluation. The metrics are available as an open-source Python package at this https URL.

---


### 142. [Learning the Target Priors Before Image Translation: A Decoupled Training Paradigm for Cross-Modal Image Translation in Remote Sensing](https://arxiv.org/abs/2608.28517)

**<font color=#1a73e8>作者：</font>** Keyan Hu, Mingtao Wang, Ziyu Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal image translation in remote sensing must preserve source-observed content while matching the target-domain distribution. Existing methods jointly learn the target prior and cross-modal dependence from scarce paired data, overlooking a key asymmetry: only the latter intrinsically requires cross-modal correspondence. We formalize this distinction through conditional-score and denoising-risk analyses and propose Learning the Target Priors Before Image Translation (LTP-BIT), a prior-first paradigm that decouples the two learning tasks. LTP-BIT first learns a target-domain generative prior from large-scale unpaired imagery, then retains the pretrained backbone weights and learns source-conditioned control through P-DART, a parameter-efficient dual-stream architecture. Controlled experiments show that prior matching and scaling primarily improve target-domain realism, whereas instance fidelity relies more strongly on conditional adaptation. LTP-BIT achieves state-of-the-art performance across SAR-to-RGB and NIR-to-RGB benchmarks using only 9.81% task-specific parameters. On QXS-SAROPT, it retains near-full-data instance fidelity with only 25% of the paired samples.

---


### 143. [When Robots Mishear Us: Mapping the Safety Risks of Voice-Controlled Embodied AI](https://arxiv.org/abs/2608.28518)

**<font color=#1a73e8>作者：</font>** Sihan Jia, Oliver Lemon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate whether automatic speech recognition (ASR) errors in user input can lead to unsafe outputs from Embodied AI (EAI) models. We find that ASR errors can lead to harmful instructions being accepted and executed by EAI models, thereby reducing safety. We simulate ASR errors and combine them with existing safety benchmarks (SafeAgentBench and POEX) to evaluate how different errors affect embodied AI safety. We find that some of them preserve semantic structure but increase harmful ambiguity, while others weaken the model refusal behaviour and allow unsafe plans to be generated and executed. We show that in some cases automatic correction of ASR errors can reduce the risk, but this is not always effective. Overall, we show that ASR errors lead to significant safety risks for embodied AI.

---


### 144. [Texture Image Classification Using DWT AlexNet Feature Fusion and Deep Neural Networks](https://arxiv.org/abs/2608.28524)

**<font color=#1a73e8>作者：</font>** Arun D. Kulkarni  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Texture image classification plays a significant role in computer vision applications, including industrial inspection, medical image analysis, remote sensing, and object recognition. Handcrafted features can capture local texture characteristics but may have limited capability to represent complex visual patterns. In contrast, deep learning models automatically learn discriminative representations but may not fully exploit the multiscale spatial-frequency information inherent in texture images. This paper proposes a hybrid feature fusion framework, termed DWT_AlexNet_DNN, which combines Discrete Wavelet Transform (DWT) features with deep features extracted using AlexNet for texture image classification.

---


### 145. [Relaxed Sender Anonymity for CBDC Interbank Settlement: A Zero-Knowledge Approach on Permissioned EVM](https://arxiv.org/abs/2608.28529)

**<font color=#1a73e8>作者：</font>** Pietro Tiberi, Gabriele Marcelli, Vitangelo Lasorella  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Central Bank Digital Currency (CBDC) interbank settlement systems operating on Distributed Ledger Technology (DLT) face a fundamental trade-off: blockchain transparency enables trustless verification but exposes commercially sensitive bilateral transaction flows to all network participants. We propose a confidential interbank settlement protocol for permissioned Ethereum-compatible networks that resolves this tension through a relaxed sender anonymity model tailored to regulatory AML/CFT requirements. In this model, the initiating institution remains publicly identifiable on-chain for accountability and compliance, while the receiving institution, transfer amount, and business payload are cryptographically obfuscated. We realize the protocol on Hyperledger Besu using QBFT consensus, combining Groth16 zero-knowledge proofs over BN254, Poseidon hash commitments in an incremental Merkle tree, multi-recipient ECIES payload encryption, and an on-chain NoteRegistry contract that stores encrypted notes as an append-only ledger log, eliminating trusted off-chain custody servers. The protocol supports shield, confidential transfer, and unshield state transitions. Experimental evaluation across a five-node network (three commercial banks, a central bank operator, and a securities depository) demonstrates end-to-end settlement in 8-16 s, proof verification overhead of about 1 ms (around 220k gas) via EVM precompiles, and client proof generation in 4-12 s on commodity ARM hardware. While receiver confidentiality is established at the protocol level, the current proof-of-concept NoteRegistry uses owner-indexed events, a trade-off addressable in production via uniform event broadcasting.

---


### 146. [Offline-Verifiable Accountability for Cross-Organization Agent Messaging: A Preserved Evidence-Bundle Approach](https://arxiv.org/abs/2608.28542)

**<font color=#1a73e8>作者：</font>** Adil Alshammari, Hayretdin Bahsi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cross-organization agent workflows require preserved evidence that remains independently verifiable during later audit or dispute review. They may involve multiple organizations, delegated actions, policy-relevant events, and disputed accountability claims. This is difficult when live systems are unavailable, controlled by one party, or not trusted by all participants. Existing mechanisms provide useful pieces, including authenticated logging, delegation semantics, signed checkpoints, and consistency checks. What remains missing is a verifier-centered event-level bundle for checking evidence sufficiency offline under an explicit policy. We propose a preserved evidence-bundle model and a policy-controlled offline verifier for agent-to-agent workflow events. Each bundle preserves policy-required evidence, including sender authentication, authenticated log commitment, witness-backed checkpoint evidence, append-only continuity, delegation-aware authorization evidence, and explicit receiver-signed receipt evidence when required. The verifier accepts only claims supported by the selected policy-required evidence, giving a later reviewer an offline basis for assessing evidence sufficiency. It does not infer delivery or receipt from transport behavior or log inclusion alone. In a prototype evaluation over 300 complete workflows and 1200 valid preserved bundles, we measure offline verifier-side latency across policy profiles and workflow-event evidence requirements. Checkpoint-context anchoring has the highest latency in the current prototype, while delegation and workflow-prerequisite evidence require additional verification steps. In targeted negative-evidence tests, all corrupted or policy-insufficient bundles were rejected, with no false acceptance observed. These results support evidence-based audit and dispute review without relying on live services or platform-specific logs.

---


### 147. [Video Generative Models as Geometry Learner](https://arxiv.org/abs/2608.28549)

**<font color=#1a73e8>作者：</font>** Haosen Yang, Jifei Song, Zhensong Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent generative approaches to geometry estimation adapt pretrained image diffusion models and treat the task as image-conditioned generation. Leveraging off-the-shelf image diffusion models, they either (i) train task-specific geometry models (for depth and surface normal estimation) independently, losing the opportunity of exploring the intrinsic correlation of these geometric targets, or (ii) jointly fine-tune modified image diffusion backbones (e.g., altered self-attention), which typically demands substantial labeled data. To overcome these limitations in a principled fashion, we repurpose pretrained video generative models as a unified and data-efficient framework for geometry estimation, formulated innovatively as a next-frames prediction task. Our method, GeoNeXt, inherits naturally structured knowledge and richer priors from the video model, while further adapting them for joint modeling of images and geometry targets (image <-> geometry), enabling more data efficient and effective learning of geometry. Extensive experiments validate our method for zero-shot monocular depth and surface normal estimation across diverse datasets, outperforming both previous task-specific and unified generative competitors while using substantially less training data. Notably, our method rivals discriminative state-of-the-art approaches trained on over 100x more data and even standouts on several benchmarks.

---


### 148. [Advancing Interaction-Sensitive Feature Selection: Novel Relief-Based Algorithms, Expanded Comparisons, and Recommendations for Biomedical Data Mining](https://arxiv.org/abs/2608.28552)

**<font color=#1a73e8>作者：</font>** Kia Kazemi-Nia, Harsh Bandhey, Philip J. Freda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As a precursor to high-dimensional biomedical data modeling, reliable feature selection can reduce computational expense, improve modeling performance, and yield simpler, more interpretable models. However, most filter-based feature selection methods struggle to detect feature interactions, while wrapper or embedded feature selection methods are computationally expensive. Relief-based algorithms (RBAs) are filter methods that are sensitive to feature interactions while mitigating these other limitations. This study (1) refactors, optimizes, and expands the scikit-rebate Python package with existing and newly proposed RBA variants and (2) conducts rigorous RBA benchmark comparisons across diverse genomic simulations. We expand scikit-rebate to include SWRF*, mu-Relief, and 5 novel RBA variants implementing alternative strategies for neighbor selection and feature scoring. All RBAs were evaluated to compare predictive feature ranking and runtime across simulated genomic datasets varying in sample size, number of features, heritability, and underlying association type (e.g. main effects and interactions). All RBAs, except mu-Relief, were proficient in detecting 2-way interactions in noisy data. RBAs utilizing 'far' scoring were best at detecting 2-way interactions - with MultiSWRFDB* top-performing - but were far less sensitive to main effects. SWRF, MultiSWRF, MultiSURF, and MultiSWRFDB yielded top performance across main effect and 2-way interaction datasets with MultiSWRFDB performing best when also considering 3-way interactions. Refactoring of scikit-rebate resulted in 10 to 35-fold reductions in RBA runtimes. The newly introduced RBAs were among the strongest performing, and by robustly retaining both main effects and 2-way epistatic interactions, these algorithms preserve predictive signals for downstream modeling.

---


### 149. [Blog: Survey of Optimizers](https://arxiv.org/abs/2608.28557)

**<font color=#1a73e8>作者：</font>** Ruoran Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural-network optimization in 2025-2026 is no longer well described as a succession of new Adam variants. The design space has expanded from coordinates to matrices and layers, from fixed training horizons to policies over time, and from mathematical update rules to state representations that must survive sharding and low-precision computation. This survey organizes recent optimizers and training optimization methods along four largely independent axes: temporal estimation, update geometry, horizon management, and representation and systems. It connects the spectral normalization of Muon, the historical matrix statistics of Shampoo and SOAP, adaptive and hybrid matrix methods, memory-efficient optimizers, schedule-free training, small-batch corrections, and quantized optimizer states. The central empirical conclusion is deliberately non-triumphal: matrix-aware methods represent a genuine advance, but there is no context-independent replacement for AdamW. Rankings change with model scale, data-to-parameter ratio, batch size, schedule, parameter partition, tuning budget, and whether the target metric is tokens, FLOPs, wall-clock time, or memory. The practical consequence is a compositional view of optimizer design and a stricter protocol for evaluating optimizer claims.

---


### 150. [SignRR: Retrieve and Refine Real Motion for Sign Language Production](https://arxiv.org/abs/2608.28568)

**<font color=#1a73e8>作者：</font>** Fidel Omar Tito Cruz, Angie Sanchez Marquina, Summy Farfan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign language production (SLP) aims to generate continuous signing motion from spoken language, often through gloss-to-pose generation. Prior work mainly follows two paradigms. Generative models synthesize motion from a learned prior or from noise, without reference to an observed signing instance, making rare hand configurations and signer-specific articulation difficult to preserve. Retrieval-based methods reuse real, well-articulated motion segments, but concatenating segments from different signers and co-articulation contexts can introduce rhythm and style inconsistencies across the full sequence, not only at segment boundaries. These limitations suggest a complementary solution: use retrieval to provide realistic articulation, and use learned refinement to impose the global coherence that retrieval alone lacks. We therefore propose retrieve-and-refine, a paradigm that starts from real retrieved motion and refines it into a globally coherent signing sequence rather than generating motion from scratch. Our framework, SignRR, initializes motion from a dictionary of real sign segments and refines the full sequence with a part-aware Residual VQ-VAE, where residual quantization preserves fine hand articulation and temporal length differences are handled in the latent space. Experiments on PHOENIX14T and CSL-Daily show that SignRR achieves state-of-the-art back-translation performance while maintaining competitive pose quality.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-151](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
