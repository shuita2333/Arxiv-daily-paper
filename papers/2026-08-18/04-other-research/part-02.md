# 📦 其他研究 | 2026年08月18日

> 本类共 **165** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-165](./part-04.md)

---

### 51. [XSA-MAD: Cross-modal Semantic Alignment for Morphing Attack Detection](https://arxiv.org/abs/2608.13861)

**<font color=#1a73e8>作者：</font>** Jie Jin, Mahiro Tokumasu, Yu Makino 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Morphing attacks pose a serious threat to face recognition systems. However, existing image-based morphing attack detection (MAD) methods often generalize poorly to unseen generation techniques because they rely solely on visual cues. We propose XSA-MAD, a CLIP-based multimodal framework that explicitly models semantic inconsistencies between bona-fide and morphed faces. Morphing concepts are decomposed into four interpretable attributes, including identity, facial geometry, texture, and consistency, and are encoded as structured and attribute-aware textual representations. The image encoder is progressively aligned with this discriminative textual space, resulting in a unified semantic representation that captures generation-invariant and concept-level discrepancies between bona-fide and morph images. Experiments on MAD22 and MorDIFF, following training on SMDD, demonstrate strong generalization across diverse morphing principles. In particular, XSA-MAD achieves an equal error rate of 2.92% on GAN-based morphs and consistently outperforms existing methods under high-fidelity generative attacks.

---


### 52. [Joint Optimization of Memory and Computing Frequency for Energy-Efficient DNN Inference](https://arxiv.org/abs/2608.13863)

**<font color=#1a73e8>作者：</font>** Yunchu Han, Zhaojun Nan, Sheng Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep neural network (DNN) inference on mobile devices often incurs high latency and energy consumption due to limited computing and memory resources. To enable energy-efficient DNN inference, most existing studies focus on dynamic voltage and frequency scaling (DVFS) for adjusting the computing frequency, while the impact of memory frequency on the inference performance has been greatly overlooked. In this paper, we consider the impact of memory frequency and computing frequency on DNN inference time, and jointly optimize these two frequencies together with communication resources for energy-efficient DNN inference. Based on a realistic inference time model, we formulate an optimization problem to minimize the energy consumption of all mobile devices under the deadline constraint. For local inference, we derive a near-optimal closed-form solution via convex optimization, while an optimal closed-form solution for transmission power is obtained for edge inference with the given bandwidth. Furthermore, we propose a low-complexity heuristic algorithm to effectively solve the overall problem with polynomial time complexity. Simulation results based on measured data show that the proposed near-optimal solution for local inference can achieve optimal performance under strict deadline constraints, with a performance gap of up to 2.5% compared with the optimal solution. Meanwhile, our proposed algorithm significantly reduces the energy consumption of devices by up to 10.4% compared to other methods.

---


### 53. [Attention Capture Is Not Detection: A Two-Stage Account of How Humans Miss Localized AI Image Edits](https://arxiv.org/abs/2608.13865)

**<font color=#1a73e8>作者：</font>** Chiao-Chieh Deng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As AI-generated image edits proliferate, the platforms meant to curb the resulting disinformation treat detectability as a single, undifferentiated property: an edit either gets a warning or it does not. We show this is the wrong model. Across a controlled eye-tracking study ($N=59$, Latin-square design, four conditions crossing edit area and semantic plausibility), a mixed-effects analysis reveals that whether an edit is noticed and whether it is correctly judged as fake are dissociable stages, governed by different factors: edit area drives attention capture ($p<0.001$) while semantic plausibility drives judgment accuracy and look-but-fail-to-see (LBFS) error rates ($p<0.001$). This dissociation survives correction for multiple comparisons; a secondary interaction between the two factors does not. This two-stage account extends a long-standing distinction in visual attention research (between pre-attentive capture and effortful recognition) into the new domain of AI-edit detectability. We then test whether a generative eye-movement model can computationally operationalize the attention-capture stage: a Transformer trained to generate scanpaths tracks per-image attention with strong discriminative power (Pearson $r=0.77$--$0.82$ across held-out stimuli) and, on the harder task of predicting LBFS incidence, modestly outperforms a two-parameter linear baseline even without access to the plausibility label ($r=0.52$ vs. $r=0.48$). We report this comparison, our ablations, and our method's limitations (a single fixed train/validation split, not leave-one-subject-out) without inflation, consistent with responsibly communicating what a machine learning system can and cannot do to help curb AI-driven disinformation.

---


### 54. [Variation Brownian Kernel Ladders](https://arxiv.org/abs/2608.13882)

**<font color=#1a73e8>作者：</font>** Mahdi Mohammadigohari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Claims about the benefit of depth depend on the complexity assigned to a representation. We introduce the \emph{Variation Brownian Kernel Ladder} (VBKL), a path-atomic function-space framework that separates nonlinear recursive dictionary construction from linear variation superposition. Starting from linear projections, each atom recursively composes unit-ball profiles from the Brownian reproducing kernel Hilbert space; the full VBKL space is then the signed-measure variation hull of the completed dictionary. We identify each recursive dictionary as a union of Brownian pullback RKHS balls and establish variation-controlled Hölder regularity, compactness and attainment, and strict growth with depth under a local non-degeneracy condition whose trace lies in the support of the input measure. For associated finite lower-support architectures, we derive Rademacher and generalization bounds through Brownian quadratic chaos, signed threshold traces, and VC entropy. We also construct two-stage approximants by discretizing the outer measure and the selected outer Brownian profiles, obtaining an $M^{-1/2}+m^{-1/2}$ error bound, a sharp interpolation constant $\sqrt{A/2}$, and at most $2M$ active outer-profile basis contributions per evaluation. Controlled experiments illustrate the approximation mechanisms and indicate a favorable limited-data accuracy--complexity trade-off.

---


### 55. [Fashion Outfit Generation via Unified Sequential Composition Models](https://arxiv.org/abs/2608.13888)

**<font color=#1a73e8>作者：</font>** Kaicheng Pang, Xingxing Zou, Ruohan Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The task of synthesizing stylistically coherent fashion outfits from massive item libraries, known as fashion outfit generation, remains a non-trivial challenge, primarily due to the non-monotonic and implicit nature of aesthetic compatibility, coupled with the exponentially large combinatorial search space. In this paper, we formalize this task as Constrained Ensemble Generation (CEG) and model it as a finite-horizon deterministic Markov Decision Process. To address CEG in fashion, we propose the Unified Sequential Composition Model (USCM), which jointly models set-level compatibility and latent composition intents. Guided by USCM's learned priors, a Latent Expansion Monte Carlo Tree Search (LE-MCTS) mechanism is proposed to handle item retrieval during composition, balancing local aesthetic synergy with global structural balance. Extensive experiments on the Polyvore Outfits dataset, along with zero-shot evaluations on the iFashion and PolyvoreU datasets, demonstrate that our framework achieves state-of-the-art performance across independent human preference evaluations, automated aesthetic proxies, and structural validity metrics for constrained fashion outfit generation.

---


### 56. [DepressionAgent: Reading, Listening, Seeing, and Deliberating Multimodal Evidence for Depression Risk Assessment](https://arxiv.org/abs/2608.13891)

**<font color=#1a73e8>作者：</font>** Fangjie Zhu, Haifeng Lu, Sicheng Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Multimodal depression risk assessment requires jointly interpreting textual, acoustic, and visual cues that are often subtle, non-specific, context-dependent, and potentially inconsistent across modalities. Existing multimodal approaches predominantly learn latent representations through feature fusion, leaving the evidence underlying a prediction and the treatment of cross-modal disagreement largely implicit. We propose DepressionAgent, an evidence-centric agentic framework that transforms multimodal depression assessment from implicit feature fusion into explicit evidence deliberation. DepressionAgent first converts textual, acoustic, and visual inputs into modality-specific evidence, and then organizes self-report and behavioral evidence into parallel support--challenge deliberation branches. Cross-modal arbitration explicitly examines agreement and disagreement between the two branches, with conflict reflection revisiting inconsistent assessments before decision making. A subsequent risk reflection mechanism provides an independent textual second opinion for initially low-risk cases to reduce potentially missed risk signals. Without depression-specific supervised training or parameter fine-tuning, DepressionAgent achieves competitive performance on multiple public benchmarks. Extensive ablations, cross-model evaluations, qualitative analyses, and clinician assessments further demonstrate the effectiveness and inspectability of the proposed framework.

---


### 57. [CipherSight: Robust Website Fingerprinting via Record-Resource Semantic Supervision under Distribution Shifts](https://arxiv.org/abs/2608.13905)

**<font color=#1a73e8>作者：</font>** Runhan Song, Qiqi Liu, Chuanzhou Pan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> HTTPS website fingerprinting (WF) aims to identify visited websites from metadata observable in encrypted traffic. However, real-world deployments introduce a significant out-of-distribution (OOD) problem caused by temporal and geographic changes, while previously unseen websites are common in open-world scenarios. Existing methods primarily learn from raw TCP packet sequences and struggle to capture stable and generalizable website representations, resulting in performance degradation under practical conditions.
We propose CipherSight, a TLS-record-based hierarchical framework for robust HTTPS WF. Unlike existing approaches that rely on TCP packet sequences and are sensitive to transport-layer artifacts, CipherSight learns website representations from TLS records by jointly encoding multiple record-level attributes. It introduces a hierarchical architecture that captures both intra-flow dependencies among TLS records and inter-flow interactions across concurrent flows, enabling the model to exploit structural patterns in HTTPS traffic. Besides, to learn robust representations, CipherSight employs a masked record modeling (MRM) task to capture contextual traffic semantics and leverages fine-grained record-resource annotations as privileged supervision through structure-aware objectives and semantic distillation. Experiments show that CipherSight achieves 95.41% accuracy across more than 2,000 website classes in the closed-world setting and maintains over 90% accuracy under both temporal and geographic drift, consistently outperforming all evaluated baselines.

---


### 58. [Hybrid Quantum-inspired Kolmogorov-Arnold Networks for Privacy-Aware Federated Biosignal Learning](https://arxiv.org/abs/2608.13914)

**<font color=#1a73e8>作者：</font>** Chun-Hua Lin, Samuel Yen-Chi Chen, Yu-Chao Hsu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrocardiogram (ECG) recordings are sensitive biomedical data, limiting the ability of hospitals and wearable devices to share raw signals for centralized model training. Federated learning addresses this practical privacy constraint by enabling collaborative model training while keeping raw biosignal data at their respective sources. However, federated ECG classification remains challenging due to limited client-side samples, imbalanced arrhythmia labels, and non-independent and identically distributed (non-IID) data across clients. These constraints require classifiers that are both communication-efficient and robust to cross-client distribution shifts. In this work, we evaluate a hybrid quantum-inspired Kolmogorov-Arnold network (HQKAN) against a multilayer perceptron (MLP) for five-class arrhythmia classification on the MIT-BIH dataset and three-class classification on the INCART dataset under federated averaging (FedAvg). Across multiple client configurations, HQKAN improves most aggregate and minority-class metrics while using 37.35% fewer trainable parameters and reducing communication cost by 24.89% on MIT-BIH; on INCART, it achieves corresponding reductions of 44.81% and 36.41%. These results indicate that HQKAN offers a compact, communication-efficient and robust alternative to the MLP baseline for privacy-aware federated learning on biosignal data.

---


### 59. [Beyond Control Points: Arcsecond Relative-Motion Estimation of Vision Measurement Platforms With Incomplete or Absent Control Fields](https://arxiv.org/abs/2608.13918)

**<font color=#1a73e8>作者：</font>** Meng Lian, Jian Wang, Shuixin Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-range vision-based deformation monitoring is highly sensitive to motion of the camera platform. Absolute-pose differencing typically relies on dedicated control data and propagates two independent pose errors into the relative-motion estimate. We develop a control-adaptive differential framework that estimates inter-frame platform motion directly from image displacements and known 3D points. With no dedicated control point, the framework recovers platform rotation from measurement-point observations. One surveyed control point enables prior-constrained translation recovery, while two nonparallel control rays recover full 3D translation. The framework requires neither nonlinear optimization nor an initial pose estimate. Excluding control data from the rotation stage makes the rotation estimate exactly immune to contamination confined to the control field. The inherited differential formulation also cancels translational extrinsic errors exactly. We derive the rotation observability condition, a leakage bound for unmodeled translation and nonrigid point motion, and the single-point axial-prior bias law. Under 0.5-pixel image noise, attitude changes of up to 30~arcmin, and 3D point perturbations of up to 2~mm, the multi-camera estimator achieves a rotation RMSE of 2.97~arcsec and an average runtime of 0.46~ms. With one surveyed control point, its prior-constrained translation RMSE is 1.19~mm. In a bridge experiment without a stable control field, the median coordinate-wise displacement RMSE relative to total-station measurements is 0.85~mm. The estimator also maintains zero divergence under the tested 3D coordinate perturbations on public RGB-D and stereo sequences. These results establish state-of-the-art accuracy, calibration robustness, and computational efficiency among the evaluated methods.

---


### 60. [Characterizing the Variance Envelope: A Multi-Dimensional Analysis of Spectre Telemetry Across Architectures and Workloads](https://arxiv.org/abs/2608.13920)

**<font color=#1a73e8>作者：</font>** Jaya Keshava Chandra Kotha, Jean-Luc Gaudiot  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware attacks like Spectre exploit built-in processor vulnerabilities, leaving anomalous footprints in Hardware Performance Counter (HPC) metrics. While machine learning can detect these footprints in controlled settings, static models fail in the real world when confronted with background system noise, diverse attack variants, and adversarial traffic pacing. To close this gap, this paper characterizes the "variance envelope"-the full range of how attack signatures shift- across Intel, ARM, and AMD architectures. We evaluate an extensive experimental matrix encompassing three attack variants, four pacing modes, and four background-noise conditions. Our analysis proves that HPC signatures are highly fragile and easily warped by their execution environment. Furthermore, we expose a critical microarchitectural bottleneck: the persistent, hardware-level failure of Prime+Probe attacks on the AMD Jaguar. Ultimately, this comprehensive characterization demonstrates that reliable runtime detection requires architecture-aware, adaptive monitoring rather than static models.

---


### 61. [High-dimensional nonparametric changepoint detection via low-rank degree-two density projection](https://arxiv.org/abs/2608.13922)

**<font color=#1a73e8>作者：</font>** Guoqing Zhang, Zhaixin Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting distributional changes in high dimension is difficult when neither the pre-change nor post-change density is parametrically specified. We introduce a representation-based approach that retains all degree-at-most-two density information while replacing density estimation by matrix mean estimation. For observations in $[-1,1]^d$, a symmetric feature matrix $H_2(X)\in\R^{(d+1)\times(d+1)}$ is constructed so that $M(f)=\E_f H_2(X)$ is an isometric encoding of the degree-two orthogonal projection of the density. We scan matrix CUSUMs after rank-$r$ truncation, exploiting the low rank of the projected jump rather than sparsity of individual coordinates. The resulting \LRD{} estimator has a tent-shaped population objective and a nonasymptotic operator-norm analysis whose leading stochastic term scales as $\sqrt{rd\log(nd)}$. For multiple changes, we give a seeded narrowest-over-threshold procedure and prove exact recovery by an induction that preserves an isolating interval for every undetected change. A cross-fitted scalar refinement learns the changing low-rank direction on one fold and localizes on the other, attaining $\widetilde O_{\Pp}(\kappa^{-2})$ error; a matching Le Cam lower bound shows optimality up to logarithms. A geometrically $\beta$-mixing extension follows from a dependent matrix Bernstein inequality. Experiments with ambient dimension up to $200$, a three-change $d=100$ sequence, and a $128$-feature human-activity benchmark show that the method remains computationally practical and accurately detects pure dependence changes that are invisible to mean CUSUMs.

---


### 62. [OpenBelief-Nav: Evidence-Preserving Object Memory for Open-Vocabulary Language-Guided Navigation](https://arxiv.org/abs/2608.13923)

**<font color=#1a73e8>作者：</font>** Dinh Tuan Nguyen, Anh Dao, Phuong Nam Dang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D scene graphs provide compact semantic memory for language-guided navigation, but mapped objects are often exposed through a single fused feature or committed semantic label. Such commitment can remove minority yet task-relevant hypotheses from the task-time interface. We present OpenBelief-Nav, an evidence-preserving object memory that retains observation-level phrases, reliability cues, and frame-mask provenance while maintaining separate aggregate geometric and visual representations. Semantically related phrases are consolidated into a vocabulary-independent object belief from which task-specific readouts perform fixed-vocabulary projection or free-form retrieval. On five ScanNet200 and eight Replica scenes, full-belief projection achieves mIoU scores of 0.2742 and 0.2912, compared with 0.2393 and 0.2701 for a matched early-commit readout. Across 78 HM3D-YCB navigation trials, consensus and early-commit retrieval each achieve 60/78 successes, compared with 58/78 for belief-weighted retrieval and 55/78 for DualMap. Across 20 Unitree G1 runs organized as 10 matched evaluation cases, a correction policy permitting at most two verified candidate attempts improves target-confirmation success from 6/10 to 8/10 relative to top-1-only execution. Code will be released upon acceptance at this https URL.

---


### 63. [RGBX-Next: Towards Realistic Generative Rendering from G-Buffers](https://arxiv.org/abs/2608.13929)

**<font color=#1a73e8>作者：</font>** Zheng Zeng, Marco Salvi, Lifan Wu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved impressive results in image, video, and streaming generation. However, compared to traditional 3D rendering, they still lack precise control over the generated output. We believe a viable path forward is to use generative models as learned renderers conditioned on traditionally rendered G-buffers. We introduce RGBX-Next, a unified generative framework for forward and inverse rendering, which allows estimating G-buffers from images, videos, and streams, and rendering realistic images, videos, and streams from G-buffers. Our key contribution is a general recipe for finetuning diffusion transformer (DiT) models into generative forward and inverse renderers. We show that the resulting models achieve high quality in both realistic generative rendering and intrinsic decomposition. We will make all our models publicly available. We believe that the design principles presented in this paper will benefit future research on controllable generative forward and inverse rendering.

---


### 64. [Post-training Quantization for Hybrid Iterative Generative Models](https://arxiv.org/abs/2608.13932)

**<font color=#1a73e8>作者：</font>** Jing Gao, Junyi Wu, Wei Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Iterative Generative Models (IGMs) span autoregressive and diffusion paradigms, and hybrid variants that couple them can achieve remarkable image-generation fidelity. However, their iterative inference incurs substantial computational overhead, making Post-training Quantization (PTQ) appealing for acceleration, while directly applying vanilla PTQ to hybrid IGMs can trigger model collapse. By analyzing these failures, we identify two critical challenges: Excessive Outliers (EOs) in the activations create an irreconcilable trade-off between preserving normal precision and covering EOs, resulting in severe degradation in generation quality; Amplified Anomalies (AAs) arising unpredictably from minor quantization errors, create a mismatch between calibration and inference, thus iteratively triggering model collapse. To address these challenges, we introduce HyGenQ, a PTQ framework for hybrid IGMs. HyGenQ comprises Hierarchical Cluster Decoupling (HCD) and Scaling Recalibration (SR). HCD identifies and decouples outlier channels via a multi-stage clustering process, effectively isolating EOs while maintaining normal value precision, thereby alleviating performance degradation. SR scales AAs beyond Gaussian Bound, thereby avoiding model collapse caused by aggressive truncation. Extensive experiments demonstrate that HyGenQ successfully quantizes representative hybrid IGMs to 8-bit precision (W8A8), significantly outperforming existing baselines and validating its robustness across different model families.

---


### 65. [Probabilistic indirect models for undrained shear strength: addressing significant data missing and variability with advanced imputation and machine learning techniques](https://arxiv.org/abs/2608.13934)

**<font color=#1a73e8>作者：</font>** Haibin Xiong, Shaoheng Dai, Peng Lan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of undrained shear strength (su) is crucial for geotechnical design, but is often hampered by substantial uncertainty in traditional empirical methods. This study uses the CLAY/10/7490 global database to develop probabilistic indirect models to predict su based on Atterberg limits and piezocone cone penetration (CPTU) measurements. Firstly, the dataset has a high missing data rate and variability. We test three imputation methods - multivariate normal (MN), multiple imputation by chained equations (MICE), and miss forest (MF) - to fill the missing values. To validate their effectiveness, a Probabilistic Extreme Gradient Boosting (PXGB) model is developed, and the imputation methods are evaluated by comparing the PXGB's performance when trained on the imputed datasets against that on the original incomplete data. Secondly, the indirect model is built by integrating a multi-head attention (MHA) mechanism into an artificial neural network (ANN) to enhance information extraction from limited data, which leads to the MHA-based probabilistic neural networks (MHA-PNN) model. The models' performance, alongside a conventional MN-based prediction model, was evaluated using root mean square error (RMSE), coefficient of determination (R2), mean absolute percentage error (MAPE), conditional interval width (wCI), and coverage rate (CR). Results demonstrate that the proposed MN-enhanced MHA-PNN model substantially outperforms other models in both prediction accuracy and uncertainty quantification. These findings highlight the potential of this integrated strategy for building robust probabilistic indirect models in geotechnical applications, particularly when confronted with sparse and incomplete datasets.

---


### 66. [CoANeRV: Coordinate-Aware Token-Space Neural Video Representation](https://arxiv.org/abs/2608.13938)

**<font color=#1a73e8>作者：</font>** Jialong Guo, Ke Liu, Mengxuan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural representations for videos (NeRV) have shown strong reconstruction fidelity by storing video-specific information in network weights. However, existing formulations typically require either costly per-video optimization or video-specific weight generation, making it difficult to scale to efficient amortized video representation. We propose CoANeRV, a coordinate-aware token-space framework that adapts the broader token-conditioned neural-field paradigm to amortized video representation. CoANeRV forms compact video tokens in one feed-forward pass and uses a shared coordinate-conditioned decoder to reconstruct continuous spatio-temporal queries, avoiding per-video decoder optimization or generation while retaining coordinate-level reconstruction flexibility. To make token-space reconstruction effective, CoANeRV introduces a coordinate-aware decoding architecture that aligns spatio-temporal queries with video tokens through axis-adaptive positional encoding and temperature-modulated cross-attention. Block-wise coordinate querying further reduces peak attention memory, making high-resolution reconstruction practical. Experiments on diverse video datasets show that CoANeRV consistently improves reconstruction quality over prior feed-forward NeRV and INR baselines, reduces peak memory compared with attention-based coordinate decoders, and provides efficient amortized encoding without per-video optimization. These results support the proposed video-specific combination of feed-forward token formation, spatio-temporal coordinate retrieval, and memory-bounded dense querying. The code is available at this https URL.

---


### 67. [CMCNet: Aligning Ultrasound Image Embeddings with Textual TI-RADS Representations for Fine-Grained Thyroid Classification](https://arxiv.org/abs/2608.13939)

**<font color=#1a73e8>作者：</font>** Bingxin Yu, Xueli Wang, Jerry Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultrasound is the primary imaging modality for assessing thyroid nodules, and the ACR TI-RADS framework standardizes diagnosis through five ultrasound feature categories that are aggregated into five risk levels (TR1-TR5). Although widely adopted in clinical practice, most deep learning approaches focus on binary malignancy classification, while multi-class prediction and explicit utilization of feature-level supervision remain underexplored, largely due to limited annotated data. In this study, we introduce the STN dataset of 600 thyroid nodules with paired transverse and longitudinal ultrasound images, bounding box annotations, and complete labels for all five TI-RADS feature categories. Following the clinical decision process, we investigate how structured feature information can guide representation learning during training while requiring only images at inference. We demonstrate that text embeddings derived from standardized feature descriptions form a stable surrogate representation for TI-RADS risk levels. Based on this observation, we propose CMCNet, which aligns image embeddings to fixed textual embeddings via a Center-Margin Contrastive Loss that simultaneously promotes intra-class compactness and inter-class separation. Experimental results show that this embedding alignment strategy is more data-efficient and robust than direct multitask learning, and consistently outperforms InfoNCE, center loss, a strong multitask baseline, and a VQA-style multimodal model, particularly in imbalanced settings. The dataset is freely available at doi: https://doi.org/10.5281/zenodo.19125693 and the source code is available at: this https URL.

---


### 68. [Vectorized SQIsign Implementation Using AVX-512](https://arxiv.org/abs/2608.13948)

**<font color=#1a73e8>作者：</font>** Weize Wang, Chutong Wang, Yu Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> SQIsign is the sole isogeny-based digital signature scheme submitted to the NIST Post-Quantum Cryptography standardization process, distinguished by its foundation on the hardness of the endomorphism ring problem for supersingular elliptic curves. While offering compact key and signature sizes, SQIsign's practical deployment is hindered by computationally intensive signing procedures. This paper presents the first comprehensive vectorized implementation of SQIsign utilizing the AVX-512 Integer Fused Multiply-Add (IFMA) instruction set architecture. By systematically redesigning the computational stack---encompassing prime-field and extension-field arithmetic, elliptic curve operations including batched point doubling and scalar multiplication, as well as pairing computations via cubical arithmetic and two-dimensional isogeny evaluations---we achieve substantial performance improvements over the reference implementation. When combined with Qlapoti technology, our implementation attains a $2.69\times$ speedup for signing and a $3.18\times$ improvement for verification at NIST security level I.
Contrary to misconceptions regarding the obsolescence of AVX-512, we emphasize that Intel's AVX10 instruction set architecture (revision 10.2, scheduled for widespread deployment in late 2026) will standardize AVX-512 capabilities---including IFMA instructions---across both performance and efficiency cores, ensuring long-term viability of these optimization techniques. Furthermore, our vectorization strategies are architecture-agnostic and provide a methodological foundation applicable to broader isogeny-based cryptographic constructions. This work demonstrates that SIMD vectorization represents a critical yet underexplored optimization dimension for post-quantum isogeny-based schemes, independent of recent algorithmic advances.

---


### 69. [Fast Implicit Neural Light Field Representation via Geometric Decomposition and Multi-Resolution Low-Rank Features](https://arxiv.org/abs/2608.13949)

**<font color=#1a73e8>作者：</font>** Yao Guo, Ligen Shi, Shuchen Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit neural representations provide a compact and continuous way to reconstruct dense light fields from sampled ray coordinates. However, fast light field reconstruction remains challenging because a light field is a high-dimensional signal with strong spatial-angular redundancy and structured disparity variations. Directly fitting 4D ray coordinates with a neural network often requires considerable optimization time to recover both view appearance and cross-view consistency. To address this issue, this paper proposes a fast implicit light field representation based on geometric decomposition and multi-resolution low-rank features. The proposed method decomposes a 4D light field into a horizontal disparity plane, a spatial texture plane, and a vertical disparity plane. Each plane is represented by a low-rank structure that combines a low-resolution 2D grid with the element-wise product of two high-resolution 1D line features at multiple resolution levels. The fused features are decoded by a lightweight multilayer perceptron to predict RGB values. Experiments on public light field datasets show that the proposed method achieves competitive reconstruction quality while providing a better trade-off among model parameters, training time, and inference efficiency.

---


### 70. [HELIX: Model-Harness Co-evolution for Recursive Self-Improvement](https://arxiv.org/abs/2608.13951)

**<font color=#1a73e8>作者：</font>** Tianyu Fan, Chao Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling agent capability has largely focused on improving the model, yet an interactive agent acts through a runtime harness that mediates context, tools, control flow, and stopping. The harness shapes both what a model can accomplish and the trajectories from which it learns. This coupling motivates model-harness co-evolution for recursive self-improvement: build harnesses for a fixed model, update the model from verified sibling trajectories, and rebuild the harnesses as model capabilities change. Realizing this loop requires a controlled way to evolve harnesses while preserving intervention identity and effect. We present HELIX, a source-traceable substrate for harness evolution. HELIX decomposes agent systems into typed ports, reusable atoms, recipes, product shells, and runtime policies. It makes interventions explicit and auditable while retaining trajectories, test outcomes, and provenance. Harness evolution thus serves two linked roles: improving fixed-model execution and producing matched successes, regressions, near misses, and alternative solutions as data for subsequent model improvement. We evaluate HELIX in one evolution round on code repair. A 65-candidate portfolio discovers a fixed harness that improves task coverage by 4.0% over Pi, while the full portfolio exposes up to 58.0% more verified coverage through complementary sibling behavior. Selected candidates are assessed with repeated runs and the SWE-bench evaluator. A 200-slot sibling slice yields 438 verified SFT, critic, filter, and preference records. These results show how harness, model, and data form a feedback system: harness evolution expands current capability and creates learning signal for the next model; model updates motivate the next round of harness evolution. HELIX provides an auditable interface for studying this recursive process. Code is available at this https URL.

---


### 71. [Repair, Not Improvement: Decomposing Constrained Decoding in Tool-Call Abstention](https://arxiv.org/abs/2608.13959)

**<font color=#1a73e8>作者：</font>** Janghoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Function calling is what the recent accounting of constrained generation explicitly sets aside: it finds the decoder's contribution small for format constraints, then warns in its Section 7 against extrapolating where a constraint encodes a correctness requirement, and names function calling as one. Tool abstention is that case at its sharpest: an enum leaves the wording of an answer alone and narrows the set of answers there are, and declining to call anything is the first it drops. We measure the excluded case. Three conditions over one byte-identical prompt separate a grammar's two jobs: it fixes where generation stops as well as which tokens may be emitted. We evaluate open-weight models from 0.6B to 4B on matched English and Korean items, so the language comparison is made within item. Against an unconstrained decoder, prior work's contrast is negative on abstention in four of six cells with intervals excluding zero, worst -29.5 points, and positive with an interval excluding zero in none. The total is a sum with opposite signs: on the smallest model in Korean the stop token costs -20.0, the enum returns +19.5, and the two leave -0.5. What it recovers is form: of 698 abstentions repaired, 545 had no readable answer and 0 were judgements the scorer refused. On tool-needed items it is positive throughout; abstention leads because it is the preregistered measure, and the pooled number being kinder to the intervention makes moving to it worse rather than better. Both preregistered language claims fail.

---


### 72. [Polar Code Based Federated Learning: Convergence Analysis and Resource Allocation](https://arxiv.org/abs/2608.13961)

**<font color=#1a73e8>作者：</font>** Han Xiao, Wei Kang, Nan Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables collaborative model training across distributed devices without sharing raw data; however, it faces significant communication bottlenecks and channel impairments in practice. Conventional network layer treatments either idealize the channel as error free or apply equal error protection (EEP) to transmitted model updates, failing to account for the inherently unequal importance of quantization bits within a single local model. To address this limitation, we propose a cross layer polar code based FL scheme that leverages the unequal error protection (UEP) property of polar codes under finite block lengths. Specifically, the proposed design selectively protects more significant quantization bits, thereby mitigating the detrimental effects of channel noise. We further provide a rigorous convergence analysis of the proposed scheme, deriving an upper bound on the convergence gap, which we then jointly optimize over the number of quantization bits and the polar code block length across all training iterations. Experimental results demonstrate that both constant and variable block length configurations of our polar code based scheme consistently achieve substantial performance gains over uncoded and LDPC-based EEP benchmarks, with the advantage becoming increasingly pronounced as the channel quality deteriorating. These findings confirm the efficacy of our cross-layer design in enhancing FL robustness and efficiency under realistic channel conditions.

---


### 73. [SAFE: Scene-Aware Feature Modulation for Color Constancy with Learned Color Space in Pure-Color Scenes](https://arxiv.org/abs/2608.13967)

**<font color=#1a73e8>作者：</font>** Yuan-Kang Lee, Kuan-Lin Chen, Chih-Heng Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Color constancy on pure-color scenes is challenging: when most pixels share a narrow band of hues, every chromaticity-based cue collapses to a single point and standard estimators become ambiguous. We propose a compact framework that couples two innovations: (i) SAFE, a Scene-Aware FeaturE modulation network that organizes illumination cues into a structured four-token representation, which is then selectively reweighted based on scene complexity features; (ii) the Learned Color Space (LCS), a scene-dependent chromaticity normalization that directly addresses the chromaticity collapse problem for pure-color scenes. Experiment results show that SAFE consistently improves performance in pure-color scenes. Compared to the best-performing baseline in each metric, it reduces the mean angular error by 10%, the best-25% error by 20%, and the worst-25% error by 5.8%.

---


### 74. [Rethinking Auxiliary Modalities in Multimodal Zero-shot Anomaly Detection: From Semantic Fusion to Conditional Modulation](https://arxiv.org/abs/2608.13973)

**<font color=#1a73e8>作者：</font>** Peng Wu, Xin Ge, Yujia Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent foundation model-based methods have endowed RGB images with strong zero-shot anomaly detection (ZSAD) through vision-language pretraining. However, RGB observations alone remain limited in perceiving anomalies dominated by geometric deformation, depth variation, or subtle surface changes. Auxiliary modalities can provide complementary structural information, but existing multimodal methods typically fuse them directly into a shared semantic space, which may disturb the text-aligned anomaly semantics established by RGB foundation models and often requires modality-specific architectures. To address this issue, we propose a plug-and-play auxiliary-conditioned enhancement framework for zero-shot anomaly detection. Instead of reconstructing a joint multimodal anomaly semantic space, our framework preserves the original RGB image-text anomaly matching pathway and uses auxiliary observations as conditional signals for RGB feature refinement, allowing auxiliary modalities to seamlessly enhance existing RGB-based zero-shot anomaly detectors. Specifically, a lightweight meta-learning module takes global RGB and auxiliary representations as input and generates sample-adaptive low-rank residual updates to determine how RGB features should be refined. We further construct uncertainty-aware spatial modulation from the initial RGB anomaly response and auxiliary reliability, which determines where local residual updates are strengthened or suppressed. This global-to-local conditional modulation enables selective multimodal enhancement while preserving the original RGB anomaly semantics. Extensive experiments on MVTec 3D-AD and Eyecandies demonstrate that our framework consistently improves multiple popular RGB-based zero-shot anomaly detectors, achieving state-of-the-art performance for multimodal zero-shot anomaly detection.

---


### 75. [Structural Leakage in Graph Encryption: Attacks and Defenses](https://arxiv.org/abs/2608.13981)

**<font color=#1a73e8>作者：</font>** Hua Shen, Renzhi Chen, Ge Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Graph encryption schemes (GES) enable secure outsourcing of graph data while supporting efficient queries. This report provides a comprehensive analysis of structural leakage in GES for single-pair shortest path (SPSP) queries, integrating findings from two recent works. First, we analyze PathGES, a scheme designed to resist query recovery attacks through heavy-light decomposition (HLD) and canonical fragment encoding. Our analysis reveals that PathGES suffers from significant imbalances in HLD decomposition, with over 99% of token-path mappings being one-to-one on real-world datasets, enabling both the Falzon-Paterson attack and side-channel inference of path lengths. Second, we present Fragment Tree attack that exploits these structural weaknesses to recover query contents, achieving up to 10.24% exact recovery on sparse graphs. Third, we introduce BlindGES, an enhanced scheme incorporating a Merge-and-Divide mechanism and two-level multimap index that reduces one-to-one mappings to below 20%, cuts setup time by 50%, reduces storage overhead by 32%, and limits path length leakage to under 1%. This report systematically presents attack methodologies, defense mechanisms, security proofs, and experimental evaluations on seven real-world datasets.

---


### 76. [XAI-Guided Conservative Decentralized Execution for Offline Multi-Agent Network Slicing](https://arxiv.org/abs/2608.13982)

**<font color=#1a73e8>作者：</font>** Eslam Eldeeb, Hatim Chergui, Merouane Debbah  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The recent advances toward sixth-generation (6G) and beyond-6G networks have accelerated the need for intelligent resource management mechanisms capable of supporting heterogeneous services under shared infrastructures in network slicing. However, resource allocation in network slicing naturally forms a resource-coupled cooperative optimization problem with competing slice demands. Slices compete for limited resources to minimize individual latencies while coordinating to avoid conflicts and underutilization. Although multi-agent reinforcement learning (MARL) has shown promising performance in such settings, existing online formulations remain costly, unsafe, and difficult to deploy due to their reliance on environmental interactions and communication among agents. In this work, we present explainable artificial intelligence (XAI)-guided conservative decentralized execution (X-CODE). X-CODE is an explainable offline MARL that operates offline without environmental interaction, nor inter-agent communication. It exploits explainability-aware reward shaping to modify the relative preference among joint offline transitions during centralized training to improve decentralized resource-allocation behavior. In deployment, the agents operate independently without signaling exchange among the agents. Simulation results demonstrate that the proposed approach achieves zero observed resource-conflict events in the evaluated test episodes while minimizing per-slice latencies. Moreover, the proposed framework exhibits lower signaling overhead and reduces effective inference latency by 88 % under the considered communication-delay model compared to the online baselines. Source codes and datasets are available through: this https URL.

---


### 77. [Nanbeige4.2-3B on Apple Silicon: Fixing Deployment Bugs and Decreasing Looped Transformer Memory Overhead](https://arxiv.org/abs/2608.13987)

**<font color=#1a73e8>作者：</font>** John T. Halloran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Nanbeige4.2-3B is a 3B-parameter agentic model built around a Looped Transformer (LT) that reuses one stack of layers for a second forward pass, adding effective depth without additional parameters. Evaluated on Apple Silicon (MPS), we identify five independent bugs which prevent the released checkpoint from running via Hugging Face transformers out of the box (including a silently-zeroed RoPE buffer and calls to removed transformers cache APIs). Furthermore, we show that fixing these bugs is still not sufficient for agentic tasks, due to the LT's layer-reuse strategy (which effectively doubles peak attention memory) used to achieve parameter efficiency. We thus introduce a chunked-prefill strategy which alleviates the incurred memory-capacity penalty, extending allowable context width by $2.7 \times$ on 32~GiB shared memory. However, even with the reduced memory overhead, we show that patches are required to render Nanbeige4.2-3B usable; resolving both system prompt and MPS-native memory bugs finally allows reliable evaluation on standard MCP and tool-calling benchmarks. On a subset of MCPMark, the debugged model completes up to 30\% of real agentic tasks (up from the original's 0\%), while, on BFCL, it is near-perfect at single tool calls (yet fails the majority of multi-tool tests). We release the patched checkpoint, system prompt optimizer, and evaluation harnesses at this https URL.

---


### 78. [Content Depth Matters in Short-Video Recommendation: Rethinking the Attention Economy](https://arxiv.org/abs/2608.13990)

**<font color=#1a73e8>作者：</font>** Liwei Deng, Jing Jiang, Zhiwei Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Driven by the attention economy, short-video Recommender Systems (RSs) are primarily optimized to maximize user engagement by promoting videos that capture attention within seconds. These systems inherently favor shallow-content videos that are effective at attracting immediate attention. However, growing evidence suggests that prolonged exposure to such content may negatively affect users' cognitive engagement and mental well-being, raising concerns about the long-term societal impact of the short-video platform. To tackle this challenge, this paper introduces a new metric, the \textbf{Content Depth Score (CDS)}, to quantify the content depth of short videos. CDS measures the extent to which a video is expected to stimulate higher-order cognitive processes, using a seven-level scale grounded in established theories of cognitive psychology and learning. As an initial step toward this vision, we present \textbf{SCOPE-Bench}, the first benchmark for content-depth evaluation in short-video recommendation. Built upon a large-scale open-source short-video dataset, SCOPE-Bench provides CDS annotations for 150K videos, enabling systematic evaluation of RSs from a cognitive-content perspective. Leveraging SCOPE-Bench, we evaluate 13 representative RSs and reveal a consistent preference for shallow-content videos. Moreover, we find that these algorithms recommending cognitively deep content are only marginally better than random selection, highlighting a previously overlooked limitation of existing recommendation objectives. Our code and datasets are available at this https URL.

---


### 79. [Simulation-Driven Vehicular Traffic Data Augmentation: Extending Sensor Coverage Through Virtual Sensing](https://arxiv.org/abs/2608.13993)

**<font color=#1a73e8>作者：</font>** Davide Andrea Guastella, Eladio Montero Porras, Evangelos Pournaras 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Urban traffic management relies on sensor networks whose spatial coverage is limited by deployment costs and privacy regulations. Machine learning models trained on such sparse data cannot generalize to unmonitored locations and must be retrained whenever the sensor infrastructure changes. We propose a simulation-based methodology that addresses this problem by generating augmented traffic count datasets in which each physical sensor is replaced by a virtual sensor placed at a surrogate location in the road network. Virtual sensors are selected by a graph-search heuristic that jointly maximises vehicle-flow continuity and traffic-metric similarity between the original and surrogate locations, while enforcing a minimum spatial displacement to ensure diversity of observed traffic conditions. We validate the method on two Belgian cities: Brussels, using a calibrated model, and Namur, using synthetic models. The augmented datasets preserve the bimodal daily demand profile and the dynamics of traffic at the observed locations.

---


### 80. [MedClaw: Heuristic Agent Harness for Long-Horizon Surgical Video Reasoning](https://arxiv.org/abs/2608.14015)

**<font color=#1a73e8>作者：</font>** Yingying Fan, Penghui Du, Leyan Zhu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding tens-of-minutes surgical videos requires long-horizon temporal reasoning, answering what happens before, after, or across stages of a procedure by grounding the question in visual evidence spread across time. Existing approaches handle this poorly: a one-shot vision-language model (VLM) compresses the whole procedure to fit its context window and loses the detail a "before" or "after" question depends on, while video agents that train the model where to look are data-hungry and transfer poorly to out-of-domain surgery. We build an agent harness that separates reasoning from perception and improves by evolving context rather than optimizing weights. A text-only orchestrator plans which evidence to gather and issues an auditable sequence of tool calls, while frozen vision-language sub-agents execute each call over the pixels, viewing, cropping, inspecting frames, and retrieving external knowledge. We further propose a gradient-free, reward-gated Heuristic Skill Distillation loop that mines the agent's own low-scoring traces and keeps a candidate skill only when it raises a validation reward, yielding reusable retrieval skills, notably directed re-look. Growing an external skill library rather than tuning weights, the loop adapts from only about 100 labeled examples, far fewer than supervised or reinforcement fine-tuning requires. To evaluate this agent, we introduce MedClawBench, a de-leaked, doctor-grounded benchmark of 1,123 questions over self-built long neurosurgery recordings and a held-out public lecture-video test split. Across both datasets and all four evaluation dimensions, our agent consistently outperforms one-shot VLMs and general video-agent frameworks, with the largest gains on the long, out-of-domain neurosurgery videos. Project page: this https URL.

---


### 81. [When Does More Correct Data Hurt? Insertion-Stability and the Limits of Dimension-Based Theory](https://arxiv.org/abs/2608.14020)

**<font color=#1a73e8>作者：</font>** Joseph Sankoorikal Johny  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adding data known to be correct ought to be safe. Not always. Larsen, Pabbaraju and Shetty model the failure with a monotone adversary, which reads an i.i.d. training sample and may append as many further examples as it likes, provided the target hypothesis labels them all. Mehrotra has since settled the cost, showing that for classes of VC dimension d >= 2 no learner can guarantee expected error better than Theta((d/n)log(en/d)), a logarithmic factor above the clean PAC rate.
Because that rate is a worst case over all classes, it says nothing about which classes actually suffer the penalty, and the answer turns on the learner. We call a learner insertion-stable if feeding it more correctly labeled examples can only shrink the region where it errs. Such learners are immune to the adversary, since on any given sample the risk after insertions never exceeds the risk on the clean part alone, however much is added and however cleverly it is chosen. High- probability guarantees carry over unchanged, and because Closure is insertion-stable every intersection-closed class keeps its clean rate of E[Err] <= (21d+34)/n.
Immunity is not something the classical dimensions can predict. Two classes can agree on VCdim = Ldim = 2 and still split, one at Theta(1/n) and the other at Theta(log(en)/n), while intervals have unbounded Littlestone dimension and are immune anyway. On Mehrotra's hard class we prove more than the failure of a single algorithm, showing that no monotone permutation-invariant compression scheme of any finite size attains the clean rate.
The question is therefore not whether a class is hard, nor whether a learner is good, but whether the two suit each other. Given an insertion-stable learner that is optimal on clean data, correct additions are free, and without one the cost belongs to the class, so changing the learner will not avoid it.

---


### 82. [Residual Dominance as a Structural Account of Last-Item Reliance in Causal Self-Attention Recommenders](https://arxiv.org/abs/2608.14021)

**<font color=#1a73e8>作者：</font>** Keito Kozaki, Keigo Sakurai, Ren Togo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transformer-based sequential recommenders with causal self-attention often rely heavily on the most recent interaction at inference time, but how this behavior is structurally expressed in the representation used for prediction remains unclear. We combine prediction-time diagnostics with norm-based analysis of the full attention block. First, we show that SASRec-style models exhibit highly localized last-item reliance. We then find that, although self-attention aggregates contextual information, residual addition sharply shifts the full-block representation toward same-position contributions, which we term residual dominance. To probe this interpretation, we use inference-time residual scaling as a controlled diagnostic intervention. Changing the residual strength induces a monotonic trade-off between structural mixing and last-item reliance, while reducing residual strength recovers a subset of final-position misses for which representations at non-final positions already rank the ground-truth item correctly. Our results provide a structural account linking extreme last-item reliance to residual dominance at inference time. The code is publicly available.

---


### 83. [ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models](https://arxiv.org/abs/2608.14022)

**<font color=#1a73e8>作者：</font>** Xinye Li, Lingshuai Lin, Lei Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action-conditioned video world models require low-latency causal generation and reliable responses to game-native controls. Although causal distillation enables one- or few-step video synthesis, extending it to interactive world models remains challenging, as discrete keyboard states and continuous mouse motion must remain aligned with temporally compressed latent chunks during causal training and autoregressive rollout. We introduce ForgeWM, a progressive framework that transforms a bidirectional action-conditioned video generator into efficient few-step world models through domain adaptation, teacher-forced causal training, causal consistency distillation, and on-policy distribution matching with a bidirectional teacher. The resulting budget-specialized students operate at steady-state denoising budgets of 1, 2, and 4 steps. ForgeWM further supports a dual-path deployment protocol combining latency-critical interaction with optional replay-time refinement, where the one-step student re-noises and refines its saved draft. On paired Minecraft trajectories, ForgeWM leads the evaluated systems in Imaging Quality, reference-aligned motion-profile agreement, action-sign accuracy, and mouse-control accuracy, while achieving the lowest reference LPIPS; the same four-stage recipe transfers to gamepad-controlled FPS gameplay. Replay-time refinement matches four-step reference quality while remaining roughly three times closer to the experienced trajectory than regeneration from noise. These results demonstrate ForgeWM's effectiveness for controllable few-step video generation.

---


### 84. [E-S2Feat:Semantic-Guided Spiking Local Feature Detection and Description for Event Cameras](https://arxiv.org/abs/2608.14027)

**<font color=#1a73e8>作者：</font>** Yang Yi, Juntao Hua, Jinpu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Benefiting from high temporal resolution and dynamic range, event-based local feature methods have attracted increasing attention. However, event sparsity, noise, and limited texture still hinder robust local feature learning. Deploying such methods on resource-constrained platforms such as unmanned aerial vehicles also requires balancing accuracy and energy efficiency. To address these challenges, this paper proposes \textbf{E-S2Feat}, a spiking neural network framework for event-based local feature detection and description. The framework jointly optimizes local feature learning from the perspectives of feature representation and selection. First, a module-specific spiking activation mechanism preserves fine-grained structural cues and discriminative information under low-bit, energy-efficient inference, thereby improving overall representation fidelity. Furthermore, a semantic-guided feature modulation mechanism leverages semantic priors to refine keypoint response distributions and enhance local descriptor discriminability, thereby guiding the model to extract local features with greater geometric stability and stronger discriminative capability. Experiments on the ECD and EDS datasets show that the proposed method significantly outperforms baseline methods such as SuperEvent in pose estimation accuracy. It also achieves accuracy comparable to its artificial neural network counterpart while delivering an approximately 4.8-fold improvement in theoretical computational energy efficiency. Visual-inertial odometry experiments on the TUM-VIE dataset further verify the effectiveness and practical application potential of the proposed method in complete SLAM systems.

---


### 85. [S2Dialog: Multimodal Dialogue Retrieval with Semantic and Acoustic-Style Modeling](https://arxiv.org/abs/2608.14029)

**<font color=#1a73e8>作者：</font>** Xueqi Wang, Zhigang Wang, Runqing Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal dialogue retrieval aims to retrieve dialogues from multimodal dialogue banks that are similar to a target dialogue in terms of both textual semantics and acoustic conversational styles. Such dialogue-level retrieval is crucial for many dialogue-related tasks, including Emotion Recognition in Conversation, Spoken Dialogue Systems, and Conversational Speech Synthesis, where external dialogue examples can provide valuable semantic and stylistic references. However, existing retrieval methods are still largely limited to utterance-level or unimodal matching, and often fail to capture the global semantic coherence and stylistic consistency of an entire dialogue. To address this gap, we propose S2Dialog, a unified framework for dialogue-level semantic-style retrieval from multimodal dialogue banks. Specifically, S2Dialog consists of a Dialogue-level Textual Retriever and a Dialogue-level Acoustic Retriever, which encode the textual and acoustic modalities of a dialogue into dialogue-level representations, respectively. To further enhance multimodal retrieval, we introduce Dialogue-level Textual-Acoustic Contrastive Learning, which aligns semantically and stylistically similar dialogues while distinguishing unrelated ones. Extensive experiments on the multimodal dialogue dataset DailyTalk demonstrate that S2Dialog achieves outstanding retrieval performance.

---


### 86. [Adversarial Learning of Classifier-Free Guidance Schedules](https://arxiv.org/abs/2608.14038)

**<font color=#1a73e8>作者：</font>** Ashwini Pokle, Alexandre Galashov, Arnaud Doucet 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern text-to-image diffusion models rely on classifier-free guidance (CFG) to achieve high image fidelity and text alignment. However, CFG typically applies a static, global scale across all timesteps, samples, and conditions -- a choice that is generally suboptimal and can introduce artifacts, as different states may benefit from different levels of guidance. While time-varying schedules are known to improve quality, designing them by hand is non-trivial and application-dependent. In this paper, we learn the guidance schedule as a function of diffusion time, conditioning and the current noisy sample, in order to better align sampled images with the text prompt. We frame this as a density ratio estimation problem: a discriminator is trained to estimate the time-dependent log-density ratio between the true and guided marginal distributions, while a lightweight generator network predicts the optimal, state-dependent guidance scale. Empirically, our approach outperforms both heuristic CFG schedules and prior methods for learning dynamic guidance on text-to-image generation benchmarks.

---


### 87. [Source-Agnostic Image Translation Based on Latent Aware Adaptive Masking](https://arxiv.org/abs/2608.14046)

**<font color=#1a73e8>作者：</font>** Tomislav Dobrički, Byung-Woo Hong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we propose a source-agnostic framework that dynamically refines a binary mask throughout the reverse diffusion process by computing the discrepancies of a pretrained diffusion model's prediction for each latent time step. Rather than relying on a fixed threshold, our method introduces a time-dependent statistical thresholding scheme derived from the empirical mean and standard deviation of prediction discrepancies across the latent noisy images from the target distribution. This allows the mask to adapt to the model's varying predictive confidence at different noise levels, effectively isolating domain-specific regions while preserving global structural coherence. Experimental results on the AFHQ and Celeba-HQ datasets demonstrate that our approach outperforms state-of-the-art unsupervised Image-to-Image methods in both realism (FID, KID) and faithfulness (SSIM, LPIPS). By requiring only a pretrained model of the target domain, our approach enables precise, automated localization and seamless translation across diverse source distributions without any specialized training. The project source code is available at: this https URL

---


### 88. [Discovery and Spatial Characterisation of Multiple Shortcut Groups for Auditing Vision Model Bias](https://arxiv.org/abs/2608.14051)

**<font color=#1a73e8>作者：</font>** Akshit Achara, Vishnunarayan Manickam, Thomas Day 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models trained on datasets with spurious correlations can achieve high average accuracy whilst relying on shortcut features that do not generalise out of distribution. Whilst out-of-distribution testing highlights subgroup performance disparities arising from shortcut learning, it does not localise the regions within images that are associated with it. Existing research mostly uses attribution maps from interpretability methods to understand the spatial nature of spurious correlations. For example, conditional alignment methods separate task-relevant evidence from evidence tied to spurious correlations by comparing attribution maps from a task model, a sensitive attribute model, and a bias-reduced reference model. This yields shortcut-aligned and task-aligned contribution maps for each image. However, existing methods aggregate these maps across the dataset, potentially masking recurring spatial shortcut patterns that occur only in subsets of images. We address this limitation by grouping per-image shortcut and task contribution maps into recurring spatial patterns using K-means and non-negative matrix factorisation, and visualising the resulting shortcut groups through contribution maps and representative examples. Across CelebA, CheXpert, Waterbirds, Camelyon17, and ISIC2019, and across ResNet and ViT models, the discovered shortcut groups reveal both shared and distinct spatial patterns of shortcut and task contribution, with varying subgroup composition and error rates, enabling targeted inspection of image subsets with higher error rates. We perform input occlusion and internal test-time interventions to show that masking or suppressing task contribution regions substantially degrades the model classification performance and propose a combined shortcut suppression and task amplification feature intervention approach which generally reduces performance disparities.

---


### 89. [Voxel-based 3D Facies Segmentation from Seismic Data: A Comparative Study](https://arxiv.org/abs/2608.14058)

**<font color=#1a73e8>作者：</font>** Duc-Thanh Pham, Minh-Tan Pham, Anh Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Seismic facies segmentation has emerged as a significant challenge in geophysics, requiring robust methods and systems to effectively identify geologically analogous facies with limited labeled data. Although existing studies have shown promising results in 2D facies segmentation, they often preprocess the original 3D seismic volumes into sets of 2D slices, typically the inline and crossline directions, and treat this problem as a purely 2D segmentation task. This simplification introduces discontinuities across slices and fails to preserve the spatial and structural continuity in 3D seismic data, thus limiting the model's ability to learn coherent geological patterns. In this work, we present a comparative and reproducible benchmark for voxel-based 3D seismic facies segmentation, built upon publicly available seismic volumes including the Netherlands F3 and the Parihaka datasets, with standardized data splits and evaluation metrics. By evaluating the three representative families of modern 3D segmentation architectures, we establish strong baseline results that highlight the potential and remaining challenges for future research in this domain.

---


### 90. [Benchmarking data-driven material models on the classic Treloar dataset](https://arxiv.org/abs/2608.14063)

**<font color=#1a73e8>作者：</font>** Hagen Holthusen, Moritz Flaschel, Denisa Martonová 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine learning is rapidly reshaping constitutive modeling, offers new ways to learn material behavior directly from experimental data, and challenges long-established modeling paradigms. But with a growing number of machine-learning-based approaches available, how do they compare in practice? In this paper, we use the classic experimental data of Treloar to benchmark popular frameworks for hyperelasticity: (Generalized-Invariant) Constitutive Artificial Neural Networks, Physics-Augmented Neural Networks, (Adaptive) Material Fingerprinting, and Efficient Unsupervised Constitutive Law Identification & Discovery. We compare their fitting performance, computational cost, hyperparameter sensitivity, and ease of implementation. Furthermore, we discuss the trade-offs between predictive accuracy and model complexity. The latter is assessed by quantifying both the number of material parameters in the discovered models and the computational time required to evaluate the constitutive model and its derivatives. The results show that all methods can reproduce the benchmark data remarkably well. Rather than identifying a single winner, we highlight the strengths and limitations of each approach and provide practical guidance for their use. The source code for all six methods, including the training and comparison scripts, as well as all results and data used in this study, is publicly available via this https URL.

---


### 91. [When Denoising Hurts: Rethinking the Terminal Step of Diffusion Time Series Forecasters -- Extended Version](https://arxiv.org/abs/2608.14067)

**<font color=#1a73e8>作者：</font>** Dat Nguyen-Cong, Luong Tran, Tung Kieu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models offer a natural way to model uncertainty in time series forecasting, yet their iterative sampling process is often treated as a uniformly beneficial refinement procedure. Our study challenges this view by examining how forecast quality evolves throughout reverse diffusion. We find that general temporal structure is often recovered at relatively high noise levels, whereas continued low-noise refinement can introduce statistical drift and degrade the final forecast. Our analysis further suggests that this behavior explains why prior methods often favor relatively narrow diffusion architecture and schedule design. Building on this observation, we propose a label-free global stopping criterion that detects the optimal termination point, eventually speeding up inference and improving predictive accuracy. Additionally, since early stopping terminates inference in high-noise regions, we propose a Bernoulli timestep sampler that concentrates training on this region while preserving coverage of the full diffusion process. Extensive experiments conducted across eight real-world datasets demonstrate the superior performance of our method compared to existing approaches.

---


### 92. [Mandato: Protocol-Level Enforcement of Digitally Signed Mandates on AI Agent Actions with Cryptographically Chained Audit Trails](https://arxiv.org/abs/2608.14074)

**<font color=#1a73e8>作者：</font>** Giovanni Racioppi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly act on external systems through standardized tool-calling protocols such as the Model Context Protocol (MCP), yet no infrastructure layer constrains their actions to what a principal has verifiably authorized: authorization logic lives in application code, is neither signed nor independently auditable, and the resulting logs lack evidentiary value. We present Mandato, a governance proxy that enforces digitally signed mandates on agent actions at the protocol level. A mandate is a machine-readable, cryptographically signed authorization artifact specifying which tools an agent may invoke, under which parameter constraints and contextual conditions, for how long, and on whose behalf; the proxy evaluates every tool call against the applicable mandate chain, blocks non-conforming calls in line, and records every decision -- permit, deny, and the evidence for each -- in an append-only, hash-chained audit log designed for evidentiary use and periodically anchored via qualified timestamps. The mandate is deliberately modeled on the civil-law institution of delegation of authority, making the artifact legible to lawyers and auditors, not only to engineers. We give the mandate model and its decision semantics, the reference architecture as an MCP-transparent proxy with separated decision and enforcement points, and a mapping of the mechanism onto EU AI Act Articles 12 and 14, GDPR accountability, NIS2, and eIDAS 2, including a roadmap to qualified attestation through Qualified Trust Service Providers (QTSPs). We describe the implementation status of the reference system and a quantitative evaluation plan covering enforcement overhead, audit completeness, and tamper-evidence verification cost.

---


### 93. [A Pathway to General-Purpose Scientific AI: Multimodal Comprehension of Scientific Images](https://arxiv.org/abs/2608.14075)

**<font color=#1a73e8>作者：</font>** Jennifer D'Souza, Fahad Ahmed, Cecilia Andrea Bustamante Andrade 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific figures and tables encode essential experimental evidence, yet remain difficult for digital libraries and multimodal AI systems to retrieve and interpret. The ALD/E-ImageMiner benchmark and ICDAR 2026 Competition on Information Extraction from Atomic Layer Deposition/Etching Scientific Figures provide 1,951 figures from 205 publications, expert-annotated for classification, data table extraction, summarization, and visual question answering. In these companion proceedings, we present a forward-looking perspective on how the benchmark can guide future scientific-image challenges. We examine how its tasks probe capabilities from visual and quantitative reading to domain-grounded reasoning and evidential justification, and how Bloom-informed question design can support deeper scientific understanding. We propose "scientific conceptual understanding from images" as a long-term benchmark objective, with future directions including broader domains and figure types, contextual and cross-document synthesis, hypothesis evaluation, provenance, uncertainty, counterfactual grounding, and open-ended multimodal research. This perspective connects the ICDAR 2026 challenge to a broader agenda for machine-actionable scientific visual knowledge and verifiable multimodal scientific AI.

---


### 94. [Owner3D: Ownership-Guided Style Writing for Training-Free Localized 3D Stylization](https://arxiv.org/abs/2608.14078)

**<font color=#1a73e8>作者：</font>** Suchang Tao, Kaifeng Shi, Zhiyan Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Localized 3D stylization aims to modify the appearance of a specified object part while preserving the remaining surfaces. In large reconstruction models (LRMs), this task is challenging because style is injected into intermediate appearance representations before rendering, while compact triplane features are shared across target and non-target surfaces, causing style leakage and boundary ambiguity. We propose Owner3D, a training-free framework for localized 3D stylization that integrates localized appearance control directly into the LRM reconstruction process. Specifically, Owner3D introduces ownership-guided style writing to restrict reference-style injection to target regions, producing a single localized stylized triplane without additional training while avoiding separate global style and appearance representations. To resolve appearance ambiguity near semantic boundaries, we further introduce boundary dual slots that maintain separate local feature sources for target and non-target regions. Finally, a surface-first texture readout hierarchically combines surface, 3D, and triplane ownership evidence to robustly recover appearance under incomplete visibility. Experiments on a benchmark constructed from Google Scanned Objects and PartNet demonstrate that Owner3D consistently outperforms existing 3D stylization methods in target-region style fidelity and non-target appearance preservation, reducing appearance leakage by 86.4% and 89.9% compared with StyleSplat and LAENeRF, respectively.

---


### 95. [The conditional superiority of fast silicon sampling](https://arxiv.org/abs/2608.14079)

**<font color=#1a73e8>作者：</font>** Nickolas Hock Yuen Lam, Ji Xuan Voo, Xiangyu Ma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Silicon sampling can produce surprisingly good population estimates at times. Does doing it fast attenuate such fidelity? In this study, we extend and assess ongoing work in silicon sampling by comparing the algorithmic fidelity of "fast" and "slow" modes of silicon sampling among a nationally representative sample of Singaporean survey respondents. We find that silicon sampling with contemporary frontier models remains a method in early development to be used only with great caution. While silicon samples are able to produce moderately faithful estimates of population means, they continue to understate opinion variance and distort the latent contextual space behind human opinions. Conditional on such limitations, we find "fast" modes of silicon sampling to be relatively superior to traditional "slow" modes of silicon sampling. Fast silicon sampling is significantly more efficient in compute resources and run-time while being monotonically superior to slower modes of sampling in algorithmic fidelity.

---


### 96. [Resource-Adaptive Primal-Dual Learning for One-Warehouse Multi-Store Systems with Censored Demand](https://arxiv.org/abs/2608.14096)

**<font color=#1a73e8>作者：</font>** Jiameng Lyu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The one-warehouse multi-store (OWMS) system is a fundamental inventory network in which a nonreplenishable warehouse allocates shared stock across multiple stores over time. Existing OWMS learning policies are built around a fixed target calibrated to the initial average resource rate, but such a fixed-target architecture cannot re-center after realized sales change the remaining resource available per future period. We develop Resource-Adaptive Primal-Dual Learning, a new learning framework that tracks the primal-dual resolving path with censored demand as the remaining-resource state evolves. In each period, the current resource rate indexes the target store allocations and dual variable, while censored sales provide gradient estimates for updating both. The analysis combines expected-sales geometry with a moving-target argument to yield logarithmic expected regret, improving on the state-of-the-art square-root-order guarantees of existing OWMS learning policies. The underlying design and analytical ideas may inform other online learning problems with depleting shared resources. Numerical experiments further demonstrate good finite-horizon performance of a practical variant across different horizon lengths and inventory regimes.

---


### 97. [Sequence prediction under a lying oracle](https://arxiv.org/abs/2608.14102)

**<font color=#1a73e8>作者：</font>** Puspabeethi Samanta, Nikhil Karamchandani, Jayakrishnan Nair  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problem of sequential prediction of an $m$-ary sequence, where at each epoch, (i) the environment selects an outcome from an $m$-ary alphabet, (ii) the learner selects a probability distribution over the same alphabet (unaware of the outcome generated by the environment), and finally, (iii) the learner incurs a cost that depends on the probability assigned to the outcome. The cost function we consider captures the complexity of predicting the outcome generated by the environment, in a scenario where the aforementioned prediction is performed via comparative queries to a lying oracle. We consider both stochastic and adversarial environments, propose algorithms for both settings, and establish logarithmic upper bounds on their regret.

---


### 98. [Retrieval Grounding Latent Reasoning for Dense Retrieval](https://arxiv.org/abs/2608.14107)

**<font color=#1a73e8>作者：</font>** Gang Zhou, Xiongxi Yu, Hu Tian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning-intensive retrieval requires text representations to capture not only semantic similarity, but also the reasoning needed to determine relevance under a given retrieval instruction. Existing reasoning-enhanced embedding models improve retrieval by incorporating reasoning information into dense representations, yet their supervision is typically dominated by the final retrieval objective. As a result, latent reasoning trajectories may learn shortcut reasoning patterns that preserve retrieval performance without producing meaningful incremental retrieval gains. We propose Retrieval Grounding Latent Reasoning (RGLT), a latent reasoning framework for dense retrieval that explicitly connects intermediate latent transitions with retrieval improvements. RGLT performs non-autoregressive reasoning in hidden space through an instruction-conditioned latent reasoning trajectory constructed from silent tokens. It combines process-supervised explicit-to-implicit distillation with retrieval-grounded supervision, using stage-wise CoT reconstruction to shape intermediate latent states and retrieval-effect credit to optimize incremental retrieval gains across the latent reasoning trajectories. Experiments on reasoning-intensive retrieval benchmarks show that RGLT consistently outperforms strong baselines while preserving efficient embedding inference.

---


### 99. [Fixed-Budget Gaussian Volume Encoding with Structure-Aware Allocation](https://arxiv.org/abs/2608.14112)

**<font color=#1a73e8>作者：</font>** Michael R. Martin, Joseph Insley, Victor A. Mateevitsi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scientific simulations often produce scalar volumes faster than they can be stored, transferred, and loaded, while in situ reduction must use only a limited share of simulation resources. This work encodes scalar fields as anisotropic Gaussian primitives under a fixed budget. The complete primitive set is allocated analytically from local field structure, including position, orientation, and shape, then refined directly against the scalar field without densification, pruning, or count changes. The selected budget determines encoded storage before refinement and, together with the iteration schedule, provides a controllable refinement-time budget. In a controlled benchmark, truncation-aware field evaluation reduces encoding time by up to 51x; 1.4 million Gaussians encode a billion-voxel volume in at most four minutes on one desktop GPU, with reduced-iteration refinement completing in under one minute. Across five datasets spanning 2.1 million to 1.1 billion evaluated voxels, compression-useful configurations achieve 15.0-38.7 dB PSNR at compression ratios from 2.2x to over 40,000x. Pre-encoding structure statistics characterize fields for which one-shot allocation yields limited gains from additional capacity. Because primitives retain scalar attributes rather than baked appearance, a single compact model serves every subsequent visualization state - supporting post-hoc transfer-function, colormap, lighting, and viewpoint changes without re-encoding.

---


### 100. [Learning to Run Power Networks: Effective AlphaZero-inspired Topological Control](https://arxiv.org/abs/2608.14114)

**<font color=#1a73e8>作者：</font>** Lukas Zetto, Benjamin Schäfer, Qiong Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As the integration of volatile renewable energy sources increases the strain on modern power grids, the use of Reinforcement Learning (RL) for autonomous topological reconfiguration has emerged as a promising research field to keep strained grids stable and operational. Compared to traditional redispatching measures, topological actions offer a cheaper and more cost-effective way to manage grid congestion. However, their implementation is hindered by a vast combinatorial action space and strict operational constraints. This paper investigates the effectiveness of model-based AlphaZero-inspired approaches that utilize Monte Carlo Tree Search (MCTS) for proactive grid management. We systematically evaluate how reward functions, observation density, and search guidance influence an agent's survivability. Our results demonstrate that the optimized AlphaZero approach achieves a peak survivability of 98.43%, significantly outperforming the proximal policy optimization (PPO) variant. We find that conducting the MCTS without guidance from a prior learned policy or value function can enhance training efficiency, and that a straightforward binary survival reward provides more effective search guidance than complex, multi-objective functions. Our findings demonstrate that while AlphaZero is a powerful framework for topological control, pure reinforcement learning is not sufficient; rather, an effective and reliable system requires a 'minimalist' integration of domain-specific heuristics, binary rewards, and a restricted observation space of line loads.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-165](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
