# 📦 其他研究 | 2026年06月23日

> 本类共 **654** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

---

### 151. [Rejections Based on Predictive Uncertainty Enable Reliable Routine Soil Spectroscopy](https://arxiv.org/abs/2606.21179)

**<font color=#1a73e8>作者：</font>** Jonas Schmidinger, Robin Gebbers, Marc-Olivier Gasser 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Soil properties relevant to agricultural and environmental applications are conventionally measured using elaborate laboratory methods involving physical and chemical processing. While highly accurate, these conventional methods are costly and time-consuming. In contrast, optical spectroscopy paired with machine learning enables rapid and cost-effective predictions of multiple soil properties. However, spectroscopic modelling is often considered unreliable, as the predictive accuracy varies between soil properties and individual samples. To balance this trade-off between cost and reliability, we introduce reject-to-remeasure: an AI-based measurement framework that combines probabilistic modelling with uncertainty-guided rejection. In this framework, soil samples are first analysed using spectroscopy, after which predictions are rejected if their predictive uncertainty exceeds predefined quality constraints. Rejected samples are subsequently remeasured using conventional laboratory procedures. On a regional visible-near-infrared spectral soil library from Québec, we demonstrate that reject-to-remeasure with modern foundation models (TabPFNv2.5 and TabICLv2) can facilitate the integration of optical spectroscopy into routine laboratory workflows while meeting user-defined accuracy requirements and reducing measurement costs.

---


### 152. [TF-SNO: Time-Frequency Gated Spectral Neural Operators for Learning Non-Stationary Partial Differential Equations](https://arxiv.org/abs/2606.21189)

**<font color=#1a73e8>作者：</font>** Yitian Zhou, Chaoning Zhang, Zhenzhen Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-stationary partial differential equations (PDEs) arise throughout scientific computing, where the dominant frequency content and energy distribution can drift over time. While efficient in PDE solving, many spectral neural operators apply a shared spectral response across rollout stages, leading to mismatch with time-varying spectra in non-stationary systems. To address this issue, we propose Time-Frequency Gated Spectral Neural Operator (TF-SNO), a state-adaptive framework with learnable time-frequency gating inside spectral blocks. TF-SNO extracts compact frequency-domain and physical-space statistics from the current state to generate modulation coefficients, enabling the spectral response to evolve with the dynamics. TF-SNO learns temporal variation implicitly from the evolving state without introducing an explicit time dimension or time embedding, keeping the modeling complexity low. We further embed the adaptive operator blocks to accurately capture the multi-scale features, thereby improving long-horizon stability. Experiments on six non-stationary PDE benchmarks in 1D and 2D demonstrate that TF-SNO significantly reduces prediction errors and improves robustness compared to strong baselines, with particularly clear gains in long rollout, suggesting the effectiveness of state-dependent spectral adaptation in modeling non-stationary physical systems.

---


### 153. [Real-time pedestrian attribute recognition with YOLOv8 and ResNet18](https://arxiv.org/abs/2606.21200)

**<font color=#1a73e8>作者：</font>** Houssam El Mir  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pedestrian attribute recognition (PAR) assigns semantic labels to detected pedestrians and is useful in surveillance, video retrieval, and human-centered graphics applications. This paper presents a two-stage framework in which YOLOv8n detects pedestrians and ResNet18-based models classify gender, estimate apparent age, and predict 61 binary attributes from each pedestrian crop. PETA and PA-100K are combined through semantic attribute mapping, producing a unified training corpus of more than 100,000 pedestrian images while retaining the PETA attribute space. On the reported test splits, the system obtains 99.89% gender classification accuracy, a 4.23-year apparent-age mean absolute error, and 89.96% multi-attribute accuracy with a 36.32% macro F1-score and 58.80% micro F1-score. Runtime measurements indicate 25-30 FPS on an NVIDIA RTX 5060 GPU. The results show that a lightweight detector-classifier pipeline can support real-time PAR, while low macro F1 indicates that rare attributes remain challenging.

---


### 154. [Whistleblowing and the machine -- towards a considered position](https://arxiv.org/abs/2606.21201)

**<font color=#1a73e8>作者：</font>** Marija Slavkovik, Liuwen Yu, Leon van der Torre 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligent agents and autonomous systems are embedded in our environments. They are both a commercial product and a personal tool that generates a lot of data and can draw conclusions from it: machines generate and keep secrets. But should machines protect all secrets? It has been shown that artificial agents are able to whistleblow and it has been argued that digital multi-agent environments should allow for agents in them to whistleblow. We argue that machine whistleblowing must be normative and principled and routed in the existing understanding of whistleblowing as an important rule-breaking mechanism in society. We also argue that there is a need for government regulators to formulate an informed stance on both what machines should be allowed to whistleblow on and how to legally protect those who develop whistleblowing machines

---


### 155. [Impact Analysis of Speech Representation Learning Models for Acoustic Side-Channel Attack](https://arxiv.org/abs/2606.21210)

**<font color=#1a73e8>作者：</font>** Nitin Choudhury, Vikrant Vikram Pratap Maurya, Arun Balaji Budhuru 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Acoustic side-channel attacks (ASCA) on keyboards have gained increasing attention, yet impact of speech representation learning models in ASCA remains unexplored. Addressing this, we introduce KEYAC, a dataset designed to analyze representation generalization for ASCA under both standard and VoIP codec settings. On KEYAC, we evaluate six representation learning models under zero-shot and partial fine-tuning settings using fully connected and convolutional networks. Results show that while partial fine-tuning improves performance, models struggle to generalize across VoIP codecs. We hypothesize this limitation stems from inadequate modeling of nonlinear feature interactions in conventional fine-tuning architectures. To address this, we employ Kolmogorov-Arnold Networks (KAN) for fine-tuning. Empirical results show that KAN-based fine-tuning consistently outperforms the baselines and establishes a new state-of-the-art on KEYAC.

---


### 156. [Comparative Evaluation of Machine Learning and Deep Learning Models for Wound-Rotor Synchronous Motor Performance Prediction](https://arxiv.org/abs/2606.21230)

**<font color=#1a73e8>作者：</font>** Kıvanç Doğan, Ahmet Orhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wound rotor synchronous motors have emerged as a strong alternative that eliminates dependence on REEs. However, WRSM design requires the simultaneous optimization of numerous geometric and electromagnetic parameters, and the high computational cost of conventional finite element analysis severely limits the rapid exploration of the large parameter space. Although there are machine-learning-based surrogate modeling studies in the literature, they generally compare only a limited number of models, exclude deep learning architectures, and do not provide a comprehensive benchmark specific to WRSM. In this study, the performance of a total of eight machine learning and deep learning models from four different algorithmic families was systematically compared for the prediction of WRSM torque and motor efficiency. On a dataset of 3351 samples generated using Latin Hypercube Sampling in the Motor-CAD simulation environment, each model was trained with 10 different random seed values and tuned via Optuna hyperparameter optimization. Different from the existing literature, this study jointly offers a broad model spectrum including recent deep learning architectures such as FT Transformer, a multi-seed reproducibility protocol, and a Pareto analysis of the computational cost-accuracy trade-off. The results revealed that neural-network-based models systematically outperform tree-based models. The FT-Transformer model achieved the highest single-model accuracy with R^2 = 0.9928, producing predictions in 0.33 milliseconds and thus obtaining several orders of magnitude speedup compared to FEA. Model performances were evaluated in a multidimensional manner using R^2, MAE, RMSE, and MAPE metrics.

---


### 157. [Context-Aware Autoregressive Diffusion for Gloss-Wise Sign Language Production](https://arxiv.org/abs/2606.21234)

**<font color=#1a73e8>作者：</font>** JungHoon Sung, Boeun Kim, Chu Xin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To generate natural and accurate sentence-level sign language, synthesizing the "gloss", the fundamental semantic unit, is essential. However, most current sign-language production (SLP) methods generate entire sequences at once. While this end-to-end approach is often efficient, it is prone to temporal drift and hand motion blur as sentences get longer, and fails to accurately control individual glosses. In this paper, we propose the Context-aware Gloss-wise AutoRegressive Diffusion model (GARD), a gloss-wise diffusion framework that models coarticulation by conditioning on both semantic (linguistic) and kinematic (motion) contexts. To ensure natural continuity between gloss motions, GARD introduces two additional strategies: i) Inter-Gloss Transition Guidance, which applies gradient-based guidance to kinematically align inter-gloss boundaries and ensure seamless pose consistency. ii) Global Motion Harmonizer, refining the entire gloss motion sequence based on the boundary poses adjusted by Inter-Gloss Transition Guidance. Extensive experiments on Phoenix-T and CSL-Daily datasets demonstrate that GARD achieves superior performance over existing SLP methods in terms of both linguistic accuracy and motion similarity.

---


### 158. [OpenWER: Improving Cross-Lingual ASR Evaluation and Enabling Token-Based Accuracy Metrics](https://arxiv.org/abs/2606.21237)

**<font color=#1a73e8>作者：</font>** Korbinian Kuhn, Gottfried Zimmermann  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Advances in deep learning and end-to-end Automatic Speech Recognition (ASR) have enabled robust multilingual models, but evaluation metrics remain limited in assessing accuracy. Efforts to improve or replace the common metric Word Error Rate (WER) often focus on English, leaving evaluations for low-resource languages under-explored and hindering fair cross-lingual comparisons. We present OpenWER, an open-source implementation that improves WER robustness through language-specific normalisation and compound word detection. A token-based Levenshtein alignment preserves complementary metrics and allows metadata embedding for granular accuracy scores. Our analysis of 52 languages shows absolute WER reductions of up to 25% compared to common libraries. OpenWER contributes to fairness in ASR research by increasing the reliability of WER across diverse languages and enabling more comprehensive accuracy evaluations.

---


### 159. [DIPBox: A Multi-scale Testing Framework for Tracking Dataset Regeneration](https://arxiv.org/abs/2606.21240)

**<font color=#1a73e8>作者：</font>** Tian Dong, Yan Meng, Shaofeng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Training datasets have tremendous proprietary value and are vulnerable to unauthorized copying. Existing defenses mainly focus on tracking individual data points, but pay little attention to the threat of dataset regeneration. Through a measurement study of public tumor datasets, we identify substantial real-world partial-dataset replication, raising concerns about potential license noncompliance. To counter the challenge of tracking previously unknown adversarial regeneration, our key insight is that regeneration that preserves model utility inevitably preserves measurable signals across multiple feature scales. We categorize these dataset features into sample-, set-, and distribution-level features and design four similarity metrics to accurately identify regeneration. Based on these metrics, we develop DIPBox, which to our knowledge is the first testing framework that tracks regeneration suspects via multi-scale similarity testing across a spectrum of defender access settings, from limited to full information. We further provide a learning-theoretic analysis that justifies these multi-scale metrics and formalizes an inherent utility--divergence trade-off, implying fundamental limits on evasive regeneration. Extensive experiments on 16 vision and text base datasets, 320 regenerated datasets, and 590 derived models validate that DIPBox outperforms previous solutions while characterizing its robustness and limits under three adaptive attacks.

---


### 160. [ACE-GS: Acing the Trade-off with Accurate, Compact and Efficient 3D Gaussian Splatting](https://arxiv.org/abs/2606.21244)

**<font color=#1a73e8>作者：</font>** Jijian Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting achieves exceptional real-time rendering, but its substantial computational and storage demands hinder widespread deployment. Existing accelerated paradigms often aggressively prune primitives for rapid convergence, causing severe loss of high-frequency details. To address this, we tackle the fundamental problem of achieving both exceptional rendering quality and ultra-fast reconstruction speed. In this paper, we propose ACE-GS, a progressive optimization framework tailored for accurate, compressed, and efficient scene representation. We realize that precise primitive management is the key to breaking this trade-off. Therefore, we first design a momentum consistency-guided densification strategy, strictly constraining primitive growth onto authentic geometric manifolds to avoid computational waste while significantly accelerating convergence. Building upon this efficient initialization, we deploy a statistical sensitivity-driven sparsification mechanism to precisely prune redundant primitives, yielding a further compressed footprint. Finally, to thoroughly compensate for the risk of micro-structure loss caused by the aforementioned strict primitive control, we introduce a cross-dimensional residual frequency compensation scheme that explicitly back-injects high-frequency error energy into primitive attributes, perfectly restoring sharp geometric details. Extensive experiments validate our superiority. While maintaining a highly compact scene representation, our system achieves up to 3.7 times training acceleration against the rapid framework Speedy-Splat. Requiring only 3 to 5 minutes to converge, ACE-GS secures the highest structural similarity and achieves a peak PSNR improvement of up to 0.89 dB over the original 3DGS, establishing a new benchmark for ultra-fast and high-fidelity novel view synthesis.

---


### 161. [Does RoPE Prevent or Degrade Retrieval Heads? A Mechanistic Analysis Across Model Families](https://arxiv.org/abs/2606.21249)

**<font color=#1a73e8>作者：</font>** Cengizhan Bayram  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval heads, attention heads that copy information from earlier context to the current position, have been proposed as the mechanistic substrate for long-context recall. Rotary position embeddings (RoPE) rotate queries and keys by frequencies decaying with a base hyperparameter theta, and a natural hypothesis is that this rotation either prevents retrieval heads from forming or degrades their function. We test both across four open-weight 7-8B models spanning multi-head and grouped-query attention and a 100x range of theta, using paired-seed needle-in-a-haystack tests, layer-clustered permutation, and causal head-masking. (i) Retrieval heads are causally necessary: masking the 87 detected heads in OLMo-2 collapses recall from 1.00 to 0.00, while masking matched random heads has no effect; this replicates in Qwen. (ii) Higher theta does not reduce retrieval-head count (LLaMA-3.1 at theta=500K has 47 heads vs LLaMA-2 at theta=10K with 42), refuting the prevention hypothesis. (iii) The norm-utility relation is family-specific and significant in opposite directions (Qwen d=-0.49, OLMo d=+0.50, both significant; LLaMA null); since OLMo and LLaMA-3.1 share theta=500K yet differ, the effect is not theta-driven. (iv) Building on Chiang and Yogatama (2025), a controlled patch shows that zeroing the lowest-frequency RoPE dimensions of retrieval heads degrades recall dose-dependently (1.00 to 0.18 when 32 of 128 dimensions are zeroed, vs 0.98 for random dimensions); the effect is head-specific and task-specific. The causal variable is RoPE frequency, not norm-utility. The direction holds in all five models patched (OLMo-2, Qwen2.5-7B/14B, Gemma-2, Mistral) across four lineages and two scales. We do not claim cross-model magnitude. Code and a paired-seed harness are released.

---


### 162. [A Neurosymbolic Framework for Interpretable Skeleton-Based Seizure Detection via Concept-Driven Logical Reasoning](https://arxiv.org/abs/2606.21252)

**<font color=#1a73e8>作者：</font>** Talha Ilyas, Deval Mehta, Zongyuan Ge  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-based seizure detection is essential for the management of epilepsy patients, offering a non-invasive complement to electroencephalography. While several deep learning approaches have been developed for video-based seizure detection, none are inherently interpretable, limiting their adoption and translation into clinical practice. We present, to our knowledge, the first exploration of a neurosymbolic framework for video-based seizure detection that directly addresses this gap. Our approach (1) extracts patient-centric skeleton sequences from epilepsy monitoring units via a prompt-guided foundation model, (2) predicts binary spatio-temporal concept activations grounded in clinical motor semiology guidelines, and (3) composes them via differentiable logic into interpretable Boolean rules with auditable contributions. Furthermore, to mitigate false positives arising from the traditional binary formulation (seizure vs.\ non-seizure), we sub-classify non-seizure segments into clinically relevant normal activities, providing the model with fine-grained discriminative supervision. Evaluated on two public seizure video benchmarks, our framework achieves 89.78% sensitivity with 0.06 false detections per hour on SAHZU and 85.27%,0.09 on IEEE, while producing complete three-level interpretability: every prediction decomposes into which motor primitives were detected, how they were logically composed, and how much each rule contributed to the clinical decision. We publicly release all annotations, extracted pose sequences, our data pipeline and code, this https URL.

---


### 163. [Gradient-Free Warm-Start Library Recovery: an Amortized-Regret Separation](https://arxiv.org/abs/2606.21253)

**<font color=#1a73e8>作者：</font>** Jianwei Lou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning that is gradient-free, local, online, and append-only is attractive for edge and streaming deployment, but its value is usually argued informally. We give a provable account on recurring-regime streams. Given segmentation, a warm-start library learner attains amortized recovery cost $O\!\big(KD/\varepsilon^2+(R-K)\logK/\Delta^2\big)$ versus a memoryless re-estimator's $\Theta(RD/\varepsilon^2)$, an advantage $(R-K)\,\Theta(D/\varepsilon^2)$ growing with dimension $D$ and recurrence density. The mechanism is a decoupling: recognizing which of $K$ seen regimes is active costs $O(\log K/\Delta^2)$, independent of $D$, whereas estimating a regime costs $\Theta(D/\varepsilon^2)$. We prove this is tight: matching lower bounds give recognition $\Theta(\log K/\Delta^2)$ and a memoryless-class bound $\Omega(RD/\varepsilon^2)$, so each term is individually minimax-tight (the joint statement is conditional). The separation is born-immune (a memoryless learner's advantage is identically zero) and paradigm-level: it matches, and does not beat, a fair spawn-capable Bayesian baseline; the contribution is attaining this cost structure without end-to-end backprop and with zero forgetting by construction. A count-calibrated variant ties the baseline's leading constant up to a bounded, never-negative per-recurrence overshoot, hyperparameter-free and with no per-step transcendentals. We bound the scope: recognizable regimes are capped by simplex packing (walls $e^{\Theta(D)}$); autonomous segmentation is impossible at the packing wall (no detector escapes the false-alarm/delay frontier as regimes overlap); the advantage vanishes under overlap. The dimension-dependent separation is corroborated on synthetic streams and real $k$-mer genome distributions (memoryless cost $\propto D^{1.04}$, recognition $D$-independent); the one real sequential stream sits in the $D{=}1$ near-null corner.

---


### 164. [Intrinsic Flow Matching on Quantum Pure-State Manifolds with Phase-Aligned Transport](https://arxiv.org/abs/2606.21256)

**<font color=#1a73e8>作者：</font>** Jian Xu, Delu Zeng, John Paisley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum pure-state ensembles live on complex projective space, making flat Euclidean generative modeling geometrically mismatched. We introduce Intrinsic Flow Matching (IFM), a deterministic transport framework on $\mathbb{CP}^{d-1}$ that learns tangent velocity fields using Pancharatnam phase-aligned conditional paths. IFM replaces local score teachers and reverse-time stochastic sampling with manifold probability flow, while horizontal parameterization removes redundant ambient directions. We show that the IFM objective recovers the induced marginal transport field, represents deterministic projective ensemble flows, and yields endpoint and stability guarantees. Empirically, IFM often improves over ambient Euclidean flow matching across higher-qubit, multimodal, spin-coherent, physics-inspired, and amplitude-encoded MNIST image-vector benchmarks, with strongest gains on high-dimensional and coherence-sensitive tasks but not uniformly across every metric.

---


### 165. [An Empirical Study of OpenPangu Quantization on Ascend NPUs](https://arxiv.org/abs/2606.21257)

**<font color=#1a73e8>作者：</font>** Tong Shi, Jiacheng Wang, Hui Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> OpenPangu models are attractive targets for private and domestic large-language-model deployment, yet their robustness under aggressive post-training quantization on Ascend NPUs has not been systematically characterized. This paper conducts a controlled empirical study of OpenPangu 1B and 7B models on Huawei Ascend 910B1 NPUs. We evaluate representative weight-only and weight-activation post-training quantization methods, including RTN, GPTQ, AWQ, SmoothQuant, GPTAQ, BiLLM, and SliM-LLM, under a unified calibration and evaluation protocol. Across 18 evaluation tasks, we find that 8-bit weight-only quantization is effectively lossless for both models, while 4-bit quantization remains practical for the 7B model but is visibly more harmful for the 1B model on reasoning, math, and code tasks. Ultra-low precision remains challenging: most 2-bit and binary settings collapse to near-random behavior, and W4A4 SmoothQuant produces non-finite perplexity in our evaluation. These results provide an NPU-oriented accuracy map for selecting OpenPangu quantization settings and highlight the persistent difficulty of extreme low-bit compression.

---


### 166. [Few-Shot Hyperspectral Aphid Detection via FastGAN Synthetic Data Generation, Transformer-Based Classification and Explainable AI](https://arxiv.org/abs/2606.21267)

**<font color=#1a73e8>作者：</font>** Ali Saeidan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early detection of aphid infestation in crops is essential for preventing yield loss and reducing unnecessary pesticide use. Hyperspectral imaging combined with Spectral Information Divergence (SID) analysis offers a non-destructive approach for monitoring plant health; however, deep learning methods applied to hyperspectral data are often limited by small dataset sizes. In this study, a data-efficient generative adversarial network (FastGAN) was employed to augment a hyperspectral SID dataset of faba bean leaves containing healthy and aphid-infested samples. The trained generator produced 10,000 synthetic images preserving structural and spectral characteristics of real samples. Image quality was evaluated using Frechet Inception Distance (FID), demonstrating stable convergence and realistic reconstruction of leaf morphology and infestation patterns. The augmented dataset was used to train four classification architectures: VGG16, ResNet-50, EfficientNet, and Vision Transformer (ViT). Results showed that dataset augmentation significantly improved classification robustness, with performance progressively increasing from classical convolutional networks to transformer-based models. The ViT model achieved the highest accuracy and F1-scores, while EfficientNet provided strong balanced performance and ResNet-50 showed moderate improvements over VGG16. Confusion matrix analysis confirmed reduced false negatives and improved disease detection when using advanced architectures. The findings demonstrate that FastGAN-based augmentation effectively enhances hyperspectral plant disease classification and that transformer-based models provide the most reliable discrimination between healthy and infested leaves.

---


### 167. [Beyond Damage Assessment: Recyclable Material Detection in Aerial Disaster Imagery Using a Lightweight Patch-Based Framework](https://arxiv.org/abs/2606.21279)

**<font color=#1a73e8>作者：</font>** Mahmoud Hazem, Karim Hammoudi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Nowadays, more and more disasters of different natures are appearing. Several disaster assessment approaches have been developed in order to identify damaged areas from aerial images. These damaged areas contain rich material that could be recycled towards several ecological purposes. In this paper, we present a lightweight approach that permits the efficient detection of recyclable material. Experimental results show the potential of the proposed approach towards localizing recyclable materials. Accordingly, we provide a rare dataset of material images that we labeled towards supporting the development of recyclable material detectors. The dataset of labeled material images is publicly available at: anonymous.

---


### 168. [Differential Zonotopes for Verifying Global Robustness of DNNs](https://arxiv.org/abs/2606.21282)

**<font color=#1a73e8>作者：</font>** Anagha Athavale, Samuel Teuber, Matteo Maffei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The robustness of deep neural networks (DNNs) is critical in security-sensitive applications, where small input perturbations should not alter model predictions. This property is commonly formalized as local or global robustness: the former considers perturbations around a single input, while the latter -- strictly stronger -- quantifies over all input pairs. While local robustness can be expressed as a safety property, global robustness is a 2-safety property, making it substantially more challenging to verify. We present a novel static analysis technique for verifying the global robustness of DNNs. Our approach is based on differential halo zonotopes, a new abstract domain that extends zonotopes to jointly propagate pairs of perturbed inputs in lock-step while tightly bounding their divergence. In addition, we introduce a symmetric variant of confidence-based global robustness that disregards perturbations leading to differing but low-confidence predictions. This relaxation yields a practically meaningful notion of robustness that applies to a broader class of networks. We implement our approach in a new tool, called TwoSafe, and evaluate it on standard DNN verification benchmarks, including widely deployed models. Our results show that TwoSafe significantly outperforms the state of the art in both precision and scalability, enabling the verification of networks an order of magnitude larger than those handled by prior techniques.

---


### 169. [Unsupervised Domain Adaptation for Sim-to-Real Object Pose Estimation with Contrastive Alignment and Pseudo-Label Refinement](https://arxiv.org/abs/2606.21287)

**<font color=#1a73e8>作者：</font>** Nidhal Eddine Chenni, Arunkumar Rathinam, Djamila Aouada  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised domain adaptation (UDA) enables robust transfer of knowledge from simulated to real environments while exploiting a subset of unlabeled target data to improve real-world performance. Existing UDA methods for Object pose estimation often rely on global feature matching, multi-stage larger frameworks, or image translation pipelines, which tend to overlook the pose-specific information embedded in feature representations. To bridge this limitation, we introduce CAPLR that targets the adaptation of pose-sensitive features in localized regions, ensuring that domain alignment preserves the geometric cues essential for accurate pose estimation. CAPLR achieves UDA with three key components: (1) Efficient Cross-Domain Pairing strategy leveraging intermediate features to identify pose similar image pairs across domains without supervision; (2) Contrastive Alignment to perform feature alignment at localised regions in both intermediate and task-specific representations; and (3) Consistency-Based Pseudo-Label Refinement to improve reliability by encouraging stable target predictions. Extensive experiments demonstrate that CAPLR achieves state-of-the-art performance across multiple well-known object pose estimation benchmarks featuring diverse and challenging scenarios.

---


### 170. [Reconstructing Randomly Masked Spectra Helps DNNs Identify Discriminant Wavenumbers](https://arxiv.org/abs/2606.21289)

**<font color=#1a73e8>作者：</font>** Yingying Wu, Jinchao Liu, Yan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nondestructive detection methods, based on vibrational spectroscopy, are vitally important in a wide range of applications including industrial chemistry, pharmacy and national defense. Recently, deep learning has been introduced into vibrational spectroscopy showing great potential. Different from images, text, etc. that offer large labeled data sets, vibrational spectroscopic data is very limited, which requires novel concepts beyond transfer and meta learning. To tackle this, we propose a task-enhanced augmentation network (TeaNet). The key component of TeaNet is a reconstruction module that inputs randomly masked spectra and outputs reconstructed samples that are similar to the original ones, but include additional variations learned from the domain. These augmented samples are used to train the classification model. The reconstruction and prediction parts are trained simultaneously, end-to-end with back-propagation. Results on both synthetic and real-world datasets verified the superiority of the proposed method. In the most difficult synthetic scenarios TeaNet outperformed CNN by 17%. We visualized and analysed the neuron responses of TeaNet and CNN, and found that TeaNet's ability to identify discriminant wavenumbers was excellent compared to CNN. Our approach is general and can be easily adapted to other domains, offering a solution to more accurate and interpretable few-shot learning.

---


### 171. [NoduLoCC2026: Lung Nodule Localization and Classification Contest from Chest X-Ray Images](https://arxiv.org/abs/2606.21290)

**<font color=#1a73e8>作者：</font>** Adnan Mustafic, Halim Benhabiles, Adnane Cabani 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose NoduLoCC2026, a challenge on lung nodule detection and localization in chest X-ray images. We have provided a dataset for both tasks and received submissions from 5 international teams. The participating teams' solutions are presented in this work along with results on an external dataset used for testing. Proposed methods show good performance on the classification task. The best method shows a balanced accuracy score of 0.72 and AUC-ROC of 0.79. We highlight the limitations of current approaches for the localization task, with the best approach having predicted the correct number of nodules on 53\% of the test images with a median distance of 12.83mm, showing that it is a more challenging task than the first one. The challenge website is available via this https URL.

---


### 172. [Topological Neural Dynamics: A Neuron-wise Framework for Sequence Modeling](https://arxiv.org/abs/2606.21295)

**<font color=#1a73e8>作者：</font>** Borui Cai, Yao Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing sequence models, including RNNs, LSTMs, continuous-time networks, and Transformers, share a common structural principle: layer-wise dynamics, where all neurons in the same layer co-evolve through a shared parameterized operator, leaving individual neurons no freedom to evolve independently. Yet in many complex dynamical systems, rich global behavior emerges precisely from locally evolving units interacting through structured connectivity. Inspired by this principle, we introduce Topological Neural Dynamics (TND), a sequence modeling framework that shifts computation from layer-wise to neuron-wise dynamics. TND represents a neural system as a directed neuron graph, an interaction operator, and a local dynamics function, where each neuron evolves independently and collective computation emerges from interactions through the explicit graph topology. We instantiate TND as a discrete-time graph-coupled dynamical system and evaluate it as a case study on a behavior cloning task in single-player Pong. Compared with Vanilla RNN, Sparse RNN, LSTM, Closed-form continuous-time neural network (CfC), and Transformer baselines, TND achieves the best catch rate and a mean of 17.47 consecutive catches per round, more than three times that of the strongest baseline. These results suggest that shifting from layer-wise to neuron-wise dynamics provides an effective inductive bias for sequence modeling.

---


### 173. [NASDAQ: Normalized Observation Space Dynamics-Augmented Q-Learning](https://arxiv.org/abs/2606.21297)

**<font color=#1a73e8>作者：</font>** Xinwei Liu, Junyuan Liang, Zicong Hong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Augmenting model-free reinforcement learning (RL) with representations learned through observation dynamics prediction (observation-predictive RL) can improve sample efficiency and performance, with minor modifications and limited additional computation. However, this approach still struggles in challenging tasks with low-dimensional observations. In this paper, we identify a key factor behind this problem: unbalanced reconstruction losses across observation dimensions, where dimensions with larger value ranges dominate the loss. This encourages the agent to neglect dimensions with relatively small ranges, leading to degraded performance. To address this issue, we propose a novel normalization method tailored to online RL, which normalizes low-dimensional observations and balances the resulting losses and gradients. Beyond balancing reconstruction losses, observation normalization enables dynamics prediction to be performed in a normalized observation space, thereby providing a unified treatment of low- and high-dimensional inputs (e.g., physical states and images). Building on this idea, we further introduce Normalized Observation Space Dynamics-Augmented Q-learning (NASDAQ), a framework for observation-predictive RL applicable across diverse domains. NASDAQ learns state-action representations by coupling value learning with two auxiliary tasks: short-term value prediction and next normalized observation prediction. Extensive experiments demonstrate that NASDAQ achieves competitive or superior performance compared with state-of-the-art model-based and self-predictive RL methods, while requiring significantly less training wall-time.

---


### 174. [SCOPE: Scale-Consistent One-Pass Estimation of 3D Geometry](https://arxiv.org/abs/2606.21300)

**<font color=#1a73e8>作者：</font>** Zheng Zhang, Lihe Yang, Tianyu Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present SCOPE (Scale-Consistent One-Pass Estimation of 3D Geometry), a novel approach for estimating 3D geometry from extended monocular video sequences, where existing methods struggle to maintain both geometric accuracy and temporal consistency across hundreds of frames. Our approach generates affine-invariant 3D point maps with shared parameters across entire sequences, enabling consistent scale-invariant representations. We introduce three key innovations: viewpoint-invariant geometry aligning multi-perspective points in a unified reference frame; appearance-invariant learning enforcing consistency across exponential timescales; and frequency-modulated positioning enabling extrapolation to sequences vastly exceeding training length. Experiments across diverse datasets demonstrate significant improvements, reducing relative point map error by 24.2% and temporal alignment error by 34.9% on ScanNet compared to state-of-the-art methods. Our approach handles challenging scenarios with complex camera trajectories and lighting variations while efficiently processing extended sequences in a single pass. Project page: this https URL.

---


### 175. [A Test-time Actor-Critic Approach to News Images Generation](https://arxiv.org/abs/2606.21304)

**<font color=#1a73e8>作者：</font>** Damianos Galanopoulos, Vasileios Mezaris  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces the CERTH-ITI solution for the MediaEval NewsImages 2026 challenge, which focuses on generating images related to news headlines. Inspired by the Actor-Critic paradigm in reinforcement learning, we present a test-time, model-agnostic Actor-Critic Image Generation approach (ACIG). ACIG generates prompts for image creation, produces the images, evaluates the generated results, and if needed refines the image generation prompts accordingly in a feedback loop. ACIG achieved the best results in the NewsImages 2026 challenge, according to the challenge's leaderboard.

---


### 176. [Towards Dys-XAI: Influence-Based Explanations for Dysarthria Severity Assessment](https://arxiv.org/abs/2606.21306)

**<font color=#1a73e8>作者：</font>** Xiaoliang Wu, Qiyang Sun, Yupei Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dysarthria severity assessment is essential for therapy planning and longitudinal monitoring, yet manual perceptual rating is time-consuming and variable across clinicians. Although deep learning models achieve strong performance, their black-box nature limits clinical adoption. Existing speech explainability methods typically provide acoustic feature importance scores that are difficult for end-users to interpret. We propose an influence-based, instance-level explainability framework that explains each decision through supportive and competing training samples. Using gradient-based influence approximations, we compute per-utterance influence scores to identify supportive and competing training samples for each prediction. Controlled deletion experiments from 5 to 20 percent validate the explanations, showing that removing highly influential samples systematically shifts predictions. This approach provides auditable explanations by linking decisions to perceptible reference cases.

---


### 177. [Task-Differentiated Atomic Skill Expansion and Routing for Continual Learning Across Highly Heterogeneous Tasks](https://arxiv.org/abs/2606.21307)

**<font color=#1a73e8>作者：</font>** Jiacheng Wang, Xinjia He, Qi Ding 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning (CL) is commonly studied under the assumption that sequential tasks are semantically related or structurally similar. However, in highly heterogeneous settings, where tasks differ substantially in reasoning patterns and input-output formats, existing methods often suffer from catastrophic forgetting and inefficient capacity allocation. To address this challenge, we propose Task-differentiated Atomic Skill Expansion and Routing (\texttt{TASER}), a CL framework that jointly determines how many new atomic skills to introduce for each task and which skills to activate. The framework first uses atomic skill incremental learning to dynamically expand capacity based on task divergence and model uncertainty. It then applies orthogonality-enhanced skill detection to ensure these skills remain semantically distinct and independently reusable. Finally, a skill dynamic routing mechanism composes task-relevant skills through lightweight task-conditioned gating. We further introduce \texttt{HeteroCLBench}, a highly heterogeneous benchmark for CL, comprising 19 diverse tasks across 9 cognitive dimensions under a standardized sequential protocol. Experiments on \texttt{HeteroCLBench} show that \texttt{TASER} consistently outperforms strong baselines by improving plasticity and reducing catastrophic forgetting.

---


### 178. [WildBox: A Dataset and Benchmark for Aerial Monocular 3D Detection of African Savanna Wildlife](https://arxiv.org/abs/2606.21309)

**<font color=#1a73e8>作者：</font>** Vandita Shukla, Kilian Meier, Lucie Laporte-Devylder 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce WildBox, a dataset and benchmark for monocular 3D detection of wildlife from drone video, comprising 237,505 3D bounding box annotations across seven African savanna species grouped into six benchmark classes. Annotations follow a KITTI/Omni3D-compatible format in a per-segment scale-normalised camera frame, with instance identities maintained across each segment. We evaluate two open-vocabulary monocular 3D architectures, OVMono3D-LIFT and DetAny3D, under zero-shot, ground-truth 2D box prompt, and supervised fine-tuning protocols. Open-vocabulary 2D foundation models provide usable zero-shot wildlife localisation (50.55 AP@50), but zero-shot 3D detection collapses to 0.00 AP across both architectures and every 2D-input condition tested, including ground-truth 2D box prompts, thus isolating the failure to the 3D stage. Fine-tuning on WildBox recovers performance to 8.68 +/- 0.47 AP-BEV@0.50 and 13.17 +/- 0.69 AP3D macro. Depth contributes 84% of normalised Hausdorff distance after fine-tuning and over 99% in zero-shot, identifying monocular aerial depth as the dominant open problem in this regime. A coarse-to-fine curriculum, i.e. pretraining on a merged zebra class before fine-tuning on the Grevy's/plains split, improves macro 3D performance with less total compute, with the largest gains on the two zebra subclasses. WildBox is released with video-level splits, evaluation code, and baseline checkpoints to enable progress in 3D wildlife perception from drone video.

---


### 179. [Warning labels shift perceptions of sycophantic AI, but not its influence](https://arxiv.org/abs/2606.21317)

**<font color=#1a73e8>作者：</font>** Lujain Ibrahim, Myra Cheng, Cinoo Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent work has raised concerns about the influence of sycophantic AI on user judgment and relationships. One proposed mitigation, which has received regulatory attention, is to warn users about potentially harmful AI behaviors such as sycophancy. In a preregistered experiment in which participants (N = 2,610) discussed real interpersonal conflicts with an AI system, we test whether warning labels mitigate sycophancy's influence. We find that a basic AI disclosure (``This chatbot is AI'') has no detectable effect. Labeling the system as sycophantic (``...may agree with you and validate you even when you are wrong...'') does shift users' perceptions, reducing perceived objectivity and trust, but it does not reliably reduce sycophancy's influence on users' self-perceived rightness or their willingness to repair the conflict. Our results reveal a gap between AI perception and AI influence: by shifting perception without reducing influence, warning-based interventions may offer a false sense of protection. Addressing the harms of sycophancy will therefore require understanding the specific mechanisms through which it shapes judgment, and improving model behavior itself.

---


### 180. [Distinguishing indistinguishable attractors: Unsupervised anomaly detection with reservoir computers](https://arxiv.org/abs/2606.21322)

**<font color=#1a73e8>作者：</font>** Davide Prosperino, Haochun Ma, Christoph Räth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Detecting when a nonlinear dynamical system departs from its normal regime is a recurring problem across the sciences, from cardiology to climate and energy systems. We show that a very simple Kolmogorov--Smirnov test on the output weights of a reservoir computer is highly sensitive to regime changes in nonlinear dynamical systems, including those invisible to both classical nonlinear measures and modern deep-learning detectors. The core idea of our algorithm is to treat the readout layer of a reservoir computer as a representation of the input dynamics. Since the input mapping and the reservoir itself are random and fixed, the trained output weights are the only object encoding the system at hand. We summarize this fingerprint by the empirical cumulative distribution function of the readout weights and compare it to a reference band built from the training data. This unsupervised, online detector distinguishes two visually indistinguishable butterfly-shaped attractors, resolves parameter drifts seven times smaller than the strongest deep-learning baseline, flags noise four orders of magnitude below the signal, and identifies ventricular flutter in a clinical ECG recording. More broadly, we aim to establish a perspective on reservoir computers in which the trained output weights are treated as a representation of the learned system in their own right, rather than merely as a means to forecasting.

---


### 181. [MedTS-TTT: Test-Time Training for Medical Time Series Classification](https://arxiv.org/abs/2606.21329)

**<font color=#1a73e8>作者：</font>** Mingzhi Chen, Yiyu Gui, Guibo Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medical time series (MedTS) signals such as electroencephalography (EEG) and electrocardiography (ECG) support many clinical applications. However, substantial subject-level heterogeneity often induces subject-level distribution shift, causing a fixed parameter set to generalize poorly to unseen individuals. Compared with domain adaptation methods that often depend on extra adaptation components or target-batch statistics, Test-Time Training (TTT) provides a more practical solution for sequential clinical data by enabling online adaptation from unlabeled test samples. However, many representative TTT methods require iterative inner-loop optimization, increasing test-time overhead. In this paper, we propose MedTS-TTT, a test-time training framework for medical time series modeling. MedTS-TTT is built upon Closed-Loop Self-Alignment Test-Time Training (CLSA-TTT) and a Gated Convolutional Backbone (GCB). CLSA-TTT constructs a token-level self-supervised target and performs a single-step fast-weight update for intra-layer closed-loop alignment, enabling rapid sample-wise adaptation without iterative inner-loop optimization. GCB combines CLSA-TTT-based fast adaptation and token-level fusion with a gated convolutional branch to balance local dynamic modeling and information-flow control. On 4 public datasets (2 EEG and 2 ECG) with subject-independent splits, MedTS-TTT achieves 11 top-1 rankings out of 12 evaluations across 9 baselines and 3 metrics. The code is publicly available at this https URL.

---


### 182. [Ramanujan Graph Rewiring with Non Negative Resistance Curvature](https://arxiv.org/abs/2606.21333)

**<font color=#1a73e8>作者：</font>** Hugo Attali, Rachid El Jouhri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have emerged as a powerful paradigm for learning on graph-structured data by iteratively propagating and aggregating information across edges. However, conventional message passing schemes often suffer from over-squashing, whereby exponentially large neighborhoods are compressed into fixed-dimensional embeddings, impeding effective long-range dependency learning. In this work, we introduce Ramanujan Propagation, a graph rewiring strategy that leverages Ramanujan graphs to alleviate topological bottlenecks in GNNs. We first establish that suitably chosen Ramanujan graphs guarantee non-negative resistance curvature, which mitigates over-squashing and facilitates efficient information flow. We then propose an algorithmic framework to construct a Ramanujan rewired graph that preserves the local connectivity of the original graph. Our experiments demonstrate that our method outperforms nine state-of-the-art rewiring techniques. These results establish Ramanujan graphs as a rigorous structural prior for scalable, topology-aware message passing in GNNs.

---


### 183. [Synthetic Audio Generation Framework for Air Traffic Control Speech Recognition](https://arxiv.org/abs/2606.21340)

**<font color=#1a73e8>作者：</font>** Raphaël Bagat, Zhe Zhang, Junichi Yamagishi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Speech Recognition (ASR) systems, despite achieving remarkable accuracy in general-purpose domains with native speech (L1), struggle in domains like Air Traffic Control (ATC) due to strong channel noise, a presence of non-native (L2) English accents, and data scarcity. We propose a synthetic data generation pipeline with acoustical properties simulations specifically designed to address this lack of real data to improve recognition accuracy in the ATC domain. Our approach leverages a combination of neural generation techniques, including Text-to-Speech, Voice Conversion, L2-to-L1 accent conversion, and a novel controllable L1-to-L2 accent conversion framework built to simulate accented speech. Our experiments with the Whisper model on the ATCO2 corpus demonstrate that fine-tuning with either synthetic data alone, or a mix of real and synthetic data, significantly improves the word error rate over out-of-the-box and real data only baselines respectively.

---


### 184. [Mind the Noise: Sensitivity of Transformer-based Interaction-Aware Trajectory Prediction Models to Noisy Data](https://arxiv.org/abs/2606.21344)

**<font color=#1a73e8>作者：</font>** Shahab Salehi, Luca Lusvarghi, Miguel Sepulcre 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Trajectory prediction allows autonomous vehicles to anticipate the future behavior of surrounding objects (or agents) and, accordingly, maximize the safety and efficiency of their driving. State-of-the-art Transformed-based interaction-aware trajectory prediction models, which rely on attention mechanisms to capture multi-agent interactions and maximize prediction accuracy, are commonly trained and evaluated on long-range high-quality datasets. These datasets are typically obtained by aggregating data from multiple vehicles or drones and removing any object detection or tracking noise offline. Yet, information about a surrounding object's state (its position, speed, heading) is far from being noiseless in real-world deployments. Object state estimation is affected by perception uncertainties and localization errors that can be particularly large for objects received via Vehicle-to-Everything (V2X) communications. In this paper, we analyze the impact of noisy object state information on the trajectory prediction accuracy of a state-of-the-art Transformer-based interaction-aware trajectory prediction model. Our study demonstrates that trajectory prediction accuracy can rapidly deteriorate as the noise intensity increases. Numerical results show that the prediction accuracy can reduce by a 1.3x factor under small noise levels and by as much as a 3.9x factor under the highest (yet realistic) noise conditions. These findings reveal the strong sensitivity of trajectory prediction models to noisy data, underscoring the need for more realistic training and evaluation datasets as well as noise mitigation strategies.

---


### 185. [A Reward-Petri-Net Interpretation of Temporal Behavior Trees](https://arxiv.org/abs/2606.21350)

**<font color=#1a73e8>作者：</font>** Till Schmeil, Günther Waxenegger-Wilfing, Sebastian Schirmer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces an interpretation of Temporal Behavior Trees (TBTs) as Reward-Petri-Nets (RPNs) for reinforcement learning (RL). Designing reward functions for complex, long-horizon robotic tasks is notoriously difficult, especially when tasks have hierarchical structure and temporal constraints. TBTs extend conventional behavior trees (BTs) used in robotic applications by incorporating temporal properties into their leaf nodes. This allows TBTs to represents not only the behavioral task structure defined by BT operators such as Sequence, Fallback, and Parallel, but also the task's temporal constraints. In this work, the constraints are specified in the leaf nodes using Linear Temporal Logic. In order to inform RL rewards using TBTs, we provide a translation from TBT into a Petri Net (PN) and show how rewards can be automatically assigned based on the TBT's structure, resulting in a RPN. In a series of increasingly challenging environments, we demonstrate how TBT-based rewards enable learning where vanilla RL fails, improve sample efficiency, and offer flexible, intuitive control over the learning progress. We showcase the learning impact by using different reward distribution schemes and TBT structures.

---


### 186. [Urban Power Grid Topology and Hierarchy Identification from Open Data](https://arxiv.org/abs/2606.21352)

**<font color=#1a73e8>作者：</font>** Shiliang Zhang, Sabita Maharjan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding the complex topology and hierarchy of urban power grid is crucial for energy prognosis, power flow management, and system resilience analysis. However, detailed grid information remains largely proprietary. This creates significant barriers for research and innovation, especially when analyzing the last-mile distribution networks connecting individual buildings. This paper addresses this challenge by developing an open-data-driven framework for the complete identification of urban power grid topology, from high-voltage transmission down to individual building connections. Particularly, we fuse public infrastructure data (power-lines, substations, transformers, poles) to map the high and medium-voltage skeleton using graph-based algorithms. We then leverage geospatial machine learning on OpenStreetMap building data to group power demand clusters, and infer the physical topology of the final distribution lines linking the clustered buildings. We apply the developed framework to the district of Alna in Oslo, Norway, and we reconstruct the complete grid topology that connects 7,330 buildings and all major electricity infrastructure assets. With the research in this work, we provide a critical tool that facilitates power system analysis, e.g., power flow optimization, cascading failure simulation, and grid resilience against the penetration of distributed renewable generation.

---


### 187. [Beyond Classification Accuracy: An Exploration-Range Evaluation of Adaptive Crawling for Fake Shopping Sites](https://arxiv.org/abs/2606.21353)

**<font color=#1a73e8>作者：</font>** K. Karasawa, K. Takeshige, S. Matsugaya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In recent years, fake shopping sites targeting Japanese users have appeared in the top results of search engines through SEO poisoning, causing increasing damage. Conventional collection methods rely on fixed keywords and cannot keep up with evolving attack campaigns, delaying the discovery of new sites. We propose a closed-loop crawler that incorporates the page-level outputs of a fake-site classifier (fastText+LightGBM) into the search queries of the next cycle. Search queries are generated by a seed-compound strategy that combines characteristic words extracted from positive pages with seed words from the fake-shopping context (e.g., ``deep discount,'' ``official''). To complement evaluations that tend to focus on classifier accuracy, we also introduce per-cycle new-host counts and cumulative unique-host counts as exploration-range metrics. In a comparative experiment ($n=3$ for the proposed method, $n=2$ for the baseline), the fixed-keyword baseline yielded zero new-host acquisition from cycle 2 onward, indicating complete stagnation, whereas the proposed method continued to discover new hosts and, at cycle 3, achieved a cumulative unique-host count approximately 7.6 times that of the baseline on average.

---


### 188. [LEViL: Label-Efficient Video Learning via Zero-Shot Distillation over VLM-Generated Pseudo-Label Spaces](https://arxiv.org/abs/2606.21358)

**<font color=#1a73e8>作者：</font>** Aslı Çelik  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Supervised video pretraining is a common transfer learning practice for improving downstream action recognition performance. However, it requires large-scale labeled source datasets, and the effectiveness of the learned initialization is influenced by the similarity between the source and target domains. Constructing such labeled pretraining datasets for different target domains is costly and difficult to scale. To address these limitations, this study proposes a label-efficient video learning framework that combines annotation-free video pretraining with target-label-set-aware fine-tuning. During pretraining, a vision-language model (VLM) generates textual descriptions of unlabeled videos, which are processed to construct an interpretable semantic pseudo-label space. A frozen video-language model then produces zero-shot soft target distributions over this space, allowing a student video encoder to learn semantically rich representations without manual source annotations. During downstream adaptation, target-label-set-aware fine-tuning combines supervised learning from labeled target videos with zero-shot distillation over the actual target label set, helping preserve VLM-derived semantic guidance while adapting the pretrained encoder to the target task. Experiments on UCF101 and HMDB51 show that the proposed framework outperforms the compared semi-supervised video action recognition methods across all evaluated limited-label regimes. Moreover, the annotation-free pretraining stage learns transferable representations that provide an effective initialization for full-data fine-tuning, despite relying on a comparatively modest unlabeled pretraining pool.

---


### 189. [Predictive Repair Management Using a Multi-Head Attention Transformer and Online Learning](https://arxiv.org/abs/2606.21364)

**<font color=#1a73e8>作者：</font>** Xinyao Zhang, Willie Cade, Karl R. Haapala 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of repair duration is an important challenge in product maintenance due to its implications for resource allocation, customer satisfaction, and operational performance. This study aims to develop a deep learning framework to help fleet repair shops accurately categorize repair time given product historical data. The study uses an automobile repair and maintenance dataset and creates an end-to-end predictive framework by employing a multi-head attention network designed for tabular data. The developed framework combines categorical information, transformed through embeddings and attention mechanisms, with numerical historical data to facilitate integration and learning from diverse data features. A weighted loss function is introduced to overcome class imbalance issues in large datasets. Moreover, an online learning strategy is used for continuous incremental model updates to maintain predictive accuracy in evolving operational environments. Our empirical findings demonstrate that the multi-head attention mechanism extracts meaningful interactions between vehicle identifiers and repair types compared to a feed-forward neural network and a random forest model. Also, combining historical maintenance data with an online learning strategy facilitates real-time adjustments to changing patterns and increases the model's predictive performance on new data. The model is tested on real-world repair data spanning 2013 to 2020 and achieves an accuracy of 78%, with attention weight analyses illustrating feature interactions.

---


### 190. [FLM-Occ: Feed-forward Likelihood Maximization for Efficient Indoor Occupancy Prediction](https://arxiv.org/abs/2606.21373)

**<font color=#1a73e8>作者：</font>** Guangcheng Chen, Lihuang Fang, Huaqi Tao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent indoor occupancy prediction methods adopt Gaussian primitives as a sparse 3D representation for computational efficiency. However, their training relies on voxel classification, which imposes only local constraints and lacks global supervision on the distribution of the primitives. Therefore, they inevitably predict spurious primitives in empty regions, undermining both representational and computational efficiency. To address this, we propose Feed-forward Likelihood Maximization (FLM), a novel framework that reformulates occupancy prediction as voxel distribution estimation. In FLM, a network is trained to predict a mixture model that maximizes the likelihood over ground-truth occupied voxels in a feed-forward manner. To enable end-to-end training of networks and voxelization of a standard mixture model, we define mixture weights as normalized primitive volumes to implicitly enforce simplex constraints and derive novel voxelization formulas. Based on FLM, our FLM-Occ, a novel method that is capable of relocating randomly initialized primitives over long distances to model a scene. On Occ-ScanNet, FLM-Occ achieves superior accuracy using only 32 superquadrics, 2.7% of the prior SoTA, while running 3.7 times faster.

---


### 191. [ARENA: An Architecture for Measuring the Transferability of Autonomous Cyber Defense](https://arxiv.org/abs/2606.21377)

**<font color=#1a73e8>作者：</font>** Sidnei Barbieri, Ágney Lopes Roth Ferraz, Wagner Comin Sonaglio 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Operational evidence is not automatically scientific evidence. The most realistic Security Operations Center (SOC) data is production telemetry, yet it remains scientifically inaccessible because raw logs cannot be released; as a result, research relies on synthetic or dated datasets. We treat the boundary between private production telemetry and reusable research artifacts as the design object: a methodology that extracts, anonymizes, structures, and validates Security Information and Event Management (SIEM) data from a production financial SOC while preserving task-relevant investigative structure within a declared privacy boundary. Two consumers stress the same artifact. As training material, it fails loudly: 37 MITRE ATT&CK-mapped HIKARI challenges work only when anonymization preserves temporal order and entity consistency. As a measurement substrate, it fails quietly: across 200 SOCpilot incidents, a deterministic verifier detects non-compliant Large Language Model (LLM) actions that are absent from the human baseline. The result is a measurable privacy-utility boundary rather than a formal anonymity claim.

---


### 192. [OSOG: A Differentiable, Physics-Informed Synthetic Data Engine for Micro-Optical Environments](https://arxiv.org/abs/2606.21381)

**<font color=#1a73e8>作者：</font>** Caio Silva  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning in computational microscopy is severely constrained by the scarcity of densely annotated datasets. While synthetic data generation has bridged this gap in macroscopic computer vision, traditional graphics engines rely on geometric ray-tracing, failing to capture the micro-optical phenomena required for microscopy. Conversely, while wave-optics formulations exist, rendering them computationally tractable at the scale required for deep learning remains a massive systems challenge. To address this, we introduce the Optical Synthetic Object Generator (OSOG), a high-performance, fully differentiable forward-modeling engine. Drawing on established physical models of diffraction and phase retardation, OSOG maps continuous Optical Path Difference (OPD) calculations into a highly optimized, PyTorch-native Structure-of-Arrays (SoA) architecture. We validate this computational framework across three axes: First, object detection models (YOLOv11-OBB) trained purely on OSOG-generated data achieve robust zero-shot transfer to real-world highly occluded Lysozyme micrographs. Second, we introduce DiffOSOG, demonstrating that the engine's end-to-end differentiability allows for the exact recovery of continuous optical parameters via curriculum-guided inverse rendering. Finally, OSOG bypasses the $\mathcal{O}(N)$ bottlenecks of sequential ray-tracing, demonstrating sub-linear scaling by synthesizing 40,000 complex wave-optic particles in under 50 milliseconds (\>20 FPS). By providing a fast, scalable, and physically grounded tensor pipeline, OSOG enables true real-time, on-the-fly dataset generation.

---


### 193. [Unsupervised Disentanglement Without Compromises : How Functional Orthogonality Enforces Identifiability](https://arxiv.org/abs/2606.21385)

**<font color=#1a73e8>作者：</font>** Mathieu Cyrille Simon, Pascal Frossard, Christophe De Vleeschouwer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper explores unsupervised disentangled representation learning from a functional perspective. We define latent concepts as factors that influence observations through locally orthogonal directions, formalized as an orthogonality constraint on the Jacobian of the generative mapping. We prove that this condition yields identifiability of general nonlinear generative models, without requiring statistical independence or causal assumptions, provided the latent domain admits all combinations of factor values. Experiments with orthogonality-regularized normalizing flows empirically confirm the theory, demonstrate reliable recovery of ground-truth factors, and shed light on the success of VAEs. These findings challenge the prevailing impossibility claims for unsupervised disentanglement and provide a principled alternative foundation.

---


### 194. [VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models](https://arxiv.org/abs/2606.21386)

**<font color=#1a73e8>作者：</font>** Florian Seligmann, Emiliyan Gospodinov, Enes Ulas Dincer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language-action models (VLAs) achieve state-of-the-art performance on many robotic manipulation tasks, yet they can still behave unpredictably in out-of-distribution scenarios. Runtime failure detection is therefore essential for the safe real-world deployment of VLAs. However, existing task failure detectors require computationally expensive action sampling, are based on architectural assumptions that limit their applicability to VLAs, or need access to failure rollouts. We propose VLA-FAIL, a lightweight and broadly applicable failure detection framework for VLAs that combines two novel failure detectors with minimal overhead, without requiring failure data. The first, last-layer Mahalanobis distance (LLMD), detects out-of-distribution states by measuring token-wise deviations in last-layer features relative to the training data. The second, action chunk consistency (ACC), exploits the temporal overlap induced by receding-horizon control and detects failures when consecutive action chunks become inconsistent. To capture the trade-off between detection accuracy and detection latency, we introduce AUCPDT, a threshold-independent metric that jointly evaluates precision, recall, and detection time. Through extensive real-world and simulation experiments, we demonstrate that LLMD and ACC capture complementary failure modes whose combination enables reliable and early failure detection across diverse tasks, frequently outperforming significantly more expensive baseline methods.

---


### 195. [From Production SIEM to Reusable Cybersecurity Artifacts](https://arxiv.org/abs/2606.21389)

**<font color=#1a73e8>作者：</font>** Sidnei Barbieri, Leonardo Vaz de Meneses, Ágney Lopes Roth Ferraz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Operational evidence is not automatically scientific evidence. The most realistic Security Operations Center (SOC) data is production telemetry, yet it remains scientifically inaccessible because raw logs cannot be released; as a result, research relies on synthetic or dated datasets. We treat the boundary between private production telemetry and reusable research artifacts as the design object: a methodology that extracts, anonymizes, structures, and validates Security Information and Event Management (SIEM) data from a production financial SOC while preserving task-relevant investigative structure within a declared privacy boundary. Two consumers stress the same artifact. As training material, it fails loudly: 37 MITRE ATT&CK-mapped HIKARI challenges work only when anonymization preserves temporal order and entity consistency. As a measurement substrate, it fails quietly: across 200 SOCpilot incidents, a deterministic verifier detects non-compliant Large Language Model (LLM) actions that are absent from the human baseline. The result is a measurable privacy-utility boundary rather than a formal anonymity claim.

---


### 196. [CAT-Translate: Building Compact Open-Source Models for Japanese-English Translation](https://arxiv.org/abs/2606.21413)

**<font color=#1a73e8>作者：</font>** Yuu Jinnai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Nowadays, large multilingual translation models demonstrate impressive translation capabilities in the machine translation benchmarks. This raises a practical question to the developers: is it worth developing translation models specialized for a particular language pair if you only need to support that language pair? To give an anecdotal answer to this question, we develop a family of small language models (0.8B, 1.4B, 3.3B, and 7B parameters) specialized for Japanese-English bidirectional translation. We employ a two-stage supervised fine-tuning approach followed by Multi-Objective GRPO (Ichihara et al. 2025) to train models on synthetically generated parallel corpora. We evaluate our models on WMT and real-world translation benchmarks across business, legal, medical, financial, and patent domains. While multilingual models achieve strong performance on WMT benchmarks, our compact models outperform them on real-world benchmarks, suggesting the practical utility of developing specialized translation models even in the era of large multilingual models.

---


### 197. [Federated Temporal Attention Intelligence for Cyber-Resilient IoMT: Lightweight Digital Twins and PPO-Driven Honeypot Deception](https://arxiv.org/abs/2606.21422)

**<font color=#1a73e8>作者：</font>** Syed Zeeshan Haider, Anwar Shah, Muneeb Arif 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of Internet of Medical Things (IoMT) devices introduces critical cybersecurity vulnerabilities in healthcare environments where resource-constrained medical devices operate under strict latency requirements and stringent data-privacy regulations. To address these challenges, this paper presents the Lightweight Digital Twin and Federated Reinforcement Learning (LDT-FRL) framework, a privacy-preserving defense architecture integrating four complementary mechanisms: a Temporal Attention Encoder (TAE) built on a GRU backbone with learned temporal self-attention for flow-level threat classification; lightweight LSTM-based Digital Twins trained on normal-class traffic to generate per-device anomaly scores that gate the TAE classifier through a learned sigmoid coupling; a Federated Proximal Policy Optimization (PPO) agent selecting among ALLOW, ISOLATE, and HONEYPOT_REDIRECT actions based on a seven-dimensional state; and an intelligent honeypot layer that converts redirected suspicious traffic into actionable threat intelligence. A federated aggregation strategy employing EMA-smoothed per-client validation losses as inverse-weighted FedAvg coefficients stabilizes global model updates under non-IID client distributions. Evaluated on CICDDoS 2019 and TON-IoT benchmarks, LDT-FRL achieves 99.66% and 99.95% test accuracy respectively, with macro-F1 scores of 0.9913 and 0.9995, converging 81% faster than the DTFL-CD baseline while attaining perfect F1=1.000 on the severely imbalanced MITM class. Explainability analysis via SHAP, LIME, Grad-CAM, and counterfactual methods confirms that the TAE focuses on semantically meaningful flow features, providing interpretable evidence for each defense decision.

---


### 198. [Dual-Attention Convolution Experts for Sparse Tensor Completion](https://arxiv.org/abs/2606.21427)

**<font color=#1a73e8>作者：</font>** Yanlei Liu, Zhenyu Liao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tensor factorization (TF) has been widely adopted for high-dimensional sparse data completion tasks. Despite significant progress, neural TF methods often struggle to capture complex cross-mode interactions and remain vulnerable to (extreme) data sparsity. To address these challenges, we propose a novel neural tensor factorization approach, termed Dual-Attention Convolution Expert Networks with Group-Level Contrastive Learning (DCGC). For the first problem, DCGC generates diverse non-linear alignment patterns of latent factors via a multi-channel convolution network, and leverages the gated dual-attention mechanism to drive the model to focus on more important output channels (i.e., convolution experts) and the aligned features. Furthermore, DCGC introduces a group-level contrastive learning strategy that aggregates positive samples with identical feedback levels while separating negative samples across different levels. This strategy injects high-quality self-supervised signals to mitigate data sparsity. Extensive experiments conducted on five datasets demonstrate that our DCGC outperforms the state-of-the-art methods in sparse tensor completion for traffic and recommendation applications. Code to reproduce the experimental results in the paper is available at this https URL.

---


### 199. [Universal Encoders for Modular Relational Deep Learning](https://arxiv.org/abs/2606.21434)

**<font color=#1a73e8>作者：</font>** Jakub Peleška, Gustav Šír  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relational Deep Learning (RDL) models multi-tabular databases as temporal heterogeneous graphs for end-to-end representation learning. While RDL is evolving rapidly, existing approaches face significant generalization obstacles. They are either schema-specific, requiring training from scratch for every new database, or they rely on monolithic architectures that entangle feature encoding with graph message-passing. Analyzing these limitations, we establish four core pillars for building foundational relational models: semantic granularity, structural topology, temporal causality, and unified optimization.
Addressing these pillars, we propose a modular approach that decouples row encoding from graph message-passing. We introduce the Universal Row Encoder, a transformer-based module that integrates raw cell data with schema metadata$-$including column semantics, table names, and global distribution statistics$-$to produce table-width invariant row embeddings. By explicitly feeding global statistics to an intra-row self-attention mechanism, the encoder natively contextualizes unseen features and handles sparse data. Serving as a flexible "backend" for any downstream graph architecture, our pretrained encoder enhances cross-database knowledge transfer on the established RelBench benchmarks while improving learning convergence and memory footprint.

---


### 200. [Pixel Watch: Robust Heart Rate Sensing from Multipath PPG and On-Device Deep Learning Trained on 10,000 hours of Free-Living and Fitness Data](https://arxiv.org/abs/2606.21436)

**<font color=#1a73e8>作者：</font>** Daniel Roggen, Megan Walker, Yojan Patel 等 29 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The Pixel Watch 2 (PW2) is the first Google smartwatch to combine multipath photoplethysmography (PPG) with deep learning-based heart rate inference, designed to significantly improve sensing accuracy during motion-heavy activities. The device processes 10 optical channels using an on-device, 15-layer temporally dilated convolutional neural network (~300K parameters) to yield a 1 Hz heart rate output. Crucial to this model's performance was its training on a massive dataset comprising 10,000 hours of data from 962 participants, curated from a broader corpus of controlled and free-living activities. We evaluated the PW2's sensing performance across two independent validation sets: an in-house fitness dataset (229 participants, 250 hours) and an external free-living dataset (27 participants, 1000+ hours). The system achieved 95% Limits of Agreement of -10.34 to 8.66 BPM during exercise and -6.57 to 7.48 BPM during free-living activities, demonstrating substantially tighter error margins than previous Google devices. Finally, we discuss key design lessons, emphasizing that large-scale deep learning was instrumental in fully leveraging multipath PPG hardware over traditional signal processing approaches.

---


> [!TIP]
> 当前位于：**151-200**（第 4/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
