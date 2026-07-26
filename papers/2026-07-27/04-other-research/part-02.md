# 📦 其他研究 | 2026年07月27日

> 本类共 **271** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-271](./part-06.md)

---

### 51. [KeySI: An Interaction Framework for Tuning Text Embeddings Based on Human Feedback](https://arxiv.org/abs/2607.20556)

**<font color=#1a73e8>作者：</font>** Yan Zhu, Y. Chen, Rebecca Faust  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In large-scale text analysis tasks, pre-trained language models are often used to embed text corpora for downstream analysis. However, such models may struggle to capture domain-specific semantics and adapting them typically requires large amounts of labeled data and technical expertise to implement training pipelines. Recent approaches have demonstrated how visual interactions in document projections can capture human feedback as training signals for model tuning. However, these methods operate on document-level feedback, which requires users to open and assess individual documents in order to provide effective feedback. In this paper, we propose KeySI, an interaction framework that enables feature-level feedback through keyword-based concept specification. Users specify feedback by organizing extracted keywords into groups representing concepts, which KeySI translates into document-level supervision for subsequent tuning. By operating on keywords as the primary interaction medium, KeySI reduces the need for manual document inspection and labeling and lowers the barrier to adapting embedding models. We present a prototype implementation that, given a corpus, curates representative keywords, visualizes keywords and document embeddings via dimensionality reduction, allows interactive specification of keyword groups, and supports iterative refinement through system feedback. We evaluate KeySI through a user study, usage scenarios, and quantitative experiments demonstrating its effectiveness in capturing user intent and improving embedding alignment.

---


### 52. [Joint Utilization of Geospatial and census proxies for Autoencoder-Assisted Downscaling (JUGAAD) of socioeconomic indicators in India](https://arxiv.org/abs/2607.20559)

**<font color=#1a73e8>作者：</font>** Aditya Dutt, Paul Gader, Aditya Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Monitoring poverty and food security indicators is imperative for addressing socioeconomic challenges in developing nations. A limitation is mismatches in scale between data sources: census data provide geographic coverage, while socioeconomic indicators are derived from infrequently conducted surveys at coarse resolutions, posing a methodological challenge. This study introduces a deep learning framework, JuGAAD, using Indian census and survey data from 2001 and 2011 as a case study. We employ a three-step process: census and geospatial data are averaged into intermediate village-cluster-scale tessellations to reduce noise and regularize administrative boundary changes; an autoencoder compresses high-dimensional National Sample Survey Office (NSSO) data into a low-dimensional latent representation; and a regression model maps upscaled census and geospatial data to this representation. This function is applied to fine-grained census data to generate high-resolution predictions, validated against ground-truth district-level NSSO indicators. Results confirm the methodology predicts socioeconomic indicators at fine scales with strong accuracy.

---


### 53. [CT-Merging: Consensus Directions and Task-Level Scaling for LoRA Adapter Merging](https://arxiv.org/abs/2607.20561)

**<font color=#1a73e8>作者：</font>** Keumseo Ryum, Joonhyuk Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LoRA adapters provide an efficient way to specialize a pretrained model for many downstream tasks, but deploying one adapter per task requires adapter storage and task selection at inference time. Model merging addresses this issue by combining independently trained adapters into one multi-task adapter. Recent SVD-based LoRA merging methods mainly focus on constructing shared or task specific directions, while the coefficients assigned to the final directions are often directly from the original task SVD. On a fixed merged basis, inherited coefficients preserve component order with high rank correlation, yet their magnitudes differ substantially from the coefficients induced by the task updates. To address this mismatch, we propose CT-Merging, a LoRA-aware merging algorithm that estimates consensus directions from average task subspace projectors and assigns task-level RMS coefficient scales in the final update. CT-Merging uses repeated support across task SVD subspaces to construct the common basis, while reducing reliance on rank wise SVD magnitudes after direction construction. On the DC-Merge CLIP adapter benchmark, CT-Merging achieves superior average normalized accuracy compared to state-of-the-art merging methods and further improves over DC-Merge by 2.56 points on ViT-B/32 and 1.51 points on ViT-L/14 KnoTS-trained checkpoints.

---


### 54. [PhantomSeal: Proactive Deepfakes Defense with Identity/Context Protection and Forensic Tracing](https://arxiv.org/abs/2607.20564)

**<font color=#1a73e8>作者：</font>** Liangqin Ren, Zeyan Liu, Ye Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deepfakes, especially face-swapping attacks, pose significant challenges to authenticity, security, and ethics across science, engineering, and society. While most existing detection/tracing approaches operate post hoc, proactive defenses that aim to intervene before deepfake generation remain limited in terms of real-world effectiveness. In this paper, we present PhantomSeal, the first proactive defense to simultaneously protect both the identity and the context of users' images from being used in face-swapping attacks, while supporting forensic tracing. We present a novel cloaking technique that embeds a selected identity as a stealthy identifier. This mechanism steers the deepfake generation process toward producing content that resembles the chosen cloak identity, thereby preventing successful face-swapping while enabling effective feature-based forensic analysis. The effectiveness and robustness of PhantomSeal is demonstrated in extensive experiments across different face-swapping architectures and models. For example, it reduces the attack success rate of SimSwap, an advanced deepfake model, to 0.30%, and correctly identifies 97.97% of manipulated content. Codes can be found at this https URL

---


### 55. [AuthProbe: Specification-Driven, Multi-Identity Detection of Broken Object-Level Authorization in Recruitment API](https://arxiv.org/abs/2607.20574)

**<font color=#1a73e8>作者：</font>** Jay Barach  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Broken Object-Level Authorization (BOLA), also known as Insecure Direct Object Reference (IDOR), has topped the OWASP API Security ranking since 2019 and is the root cause of some of the largest exposures of applicant data in recruitment technology. The defining feature of this flaw class is that a malicious request is byte-for-byte indistinguishable from a legitimate one, which is precisely why web application firewalls and single identity scanners fail to catch it. We present AuthProbe, an open-source, black-box scanner that detects BOLA and IDOR in HTTP APIs by driving its tests from an OpenAPI specification and by acting under two or more identities that the operator controls. AuthProbe discovers, for each identity, the objects that identity legitimately owns, then attempts to read one identity's objects while authenticated as another and confirms a leak by comparing the response against a ground-truth fetch by the true owner. It also walks predictable identifiers to expose enumeration and reports missing authentication and existence oracles. The tool returns a severity-thresholded exit code and machine-readable reports so that it can gate a continuous integration build. On a synthetic recruitment API in which the McHire failure class is reproduced, AuthProbe detects every planted cross-identity read with no false positives on a hardened counterpart, and its running time grows linearly with the number of objects under test. AuthProbe is released under the Apache 2.0 license with an authorized-use guardrail.

---


### 56. [AI-Driven Surrogate Models for Predicting Electrode-Scale Discharge Behavior in Lithium-Ion Batteries](https://arxiv.org/abs/2607.20577)

**<font color=#1a73e8>作者：</font>** Mengda Xing, Jean-Marie Lagniez, Alejandro Franco  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-based simulations are essential for understanding the electrode-scale discharge behavior of lithium-ion batteries (LIBs) but suffer from prohibitive computational costs. To address this, we introduce a novel deep learning surrogate pipeline based on the Swin3D Transformer to predict spatiotemporal discharge dynamics directly from volumetric data. Our approach integrates two key innovations: Gaussian Positional Encoding (GPE), which enhances spatial feature representation by adapting to the complex geometry of electrode microstructures, and a specialized Temporal Encoding module to capture non-linear timeseries evolution. Experimental validation on an Electrochemical Simulation (ES) dataset demonstrates that our pipeline significantly outperforms state-of-the-art point cloud baselines in prediction accuracy. Furthermore, the proposed method reduces the computational overhead by orders of magnitude, providing a scalable and efficient framework for high-throughput battery design and optimization.

---


### 57. [Fisher Widths: Local Learning Geometry and Anisotropic Recovery](https://arxiv.org/abs/2607.20578)

**<font color=#1a73e8>作者：</font>** Vu Khac Ky  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study Gaussian-width complexity on statistical manifolds through a pair of functionals: the primal Fisher width $w_G(T) = w(G^{1/2}T)$, induced by the Fisher metric, and the inverse-Fisher width $w_{G^{-1}}(T) = w(G^{-1/2}T)$, induced by the inverse Fisher metric. The two widths play complementary statistical roles.
On the learning side, the Fisher width measures the size of local parameter fluctuations in the geometry induced by the Fisher information. For Fisher-regular losses, we prove that the scale \(w_G(H_r)/\sqrt n\) is attained on sufficiently small Fisher balls.
On the recovery side, the inverse-Fisher width captures the effect of anisotropic Gaussian measurements whose covariance is determined by the inverse Fisher information. For sparse recovery, the resulting geometry depends not only on sparsity but also on the position of the active coordinates in the Fisher spectrum. We obtain a two-sided estimate for the corresponding statistical dimension, together with support-sensitive recovery estimates and a natural ordering of supports with different curvature profiles.
Finally, we establish a sharp relation between the primal and inverse-Fisher widths. On any common compact coordinate set $T$, they satisfy \[ w_G(T)w_{G^{-1}}(T)\geq w(T)^2. \] Thus, Fisher anisotropy may transfer complexity from one geometry to the other, but cannot reduce both widths relative to the Euclidean scale.

---


### 58. [Geometric Configurations of Perturbed Jailbreak Prompts](https://arxiv.org/abs/2607.20581)

**<font color=#1a73e8>作者：</font>** Lynn Delcon, Andres Algaba, Vincent Ginis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Perturbation techniques that turn unsuccessful jailbreak prompts into successful ones are continuously evolving, constituting a major security threat to LLM safety. In this paper, we investigate the internal representations of such string-level perturbed jailbreak inputs in the small weight models of the Qwen-2.5-1.5B/-3B/-7B-Instruct and Llama-3.2-1B/-3B/-3.1-8B-Instruct families. We select two representation spaces: the last-layer-last-token embedding space and the top-50 next-token probability space. The former space separates prompts based on their spelling and format, while the latter space is effectively one-dimensional but appears more complex to cluster. Within our refusal-dominated answer set we find no behavioral hyperplane in either space. Only the next token "Sure" in the 1.5B Qwen model, and both tokens "," and "ĊĊ" in the 1$ Llama model, display a significant association with a compliant-labeled answer.

---


### 59. [Bayesian uncertainty estimation improves clinical decision making in medical AI agents](https://arxiv.org/abs/2607.20582)

**<font color=#1a73e8>作者：</font>** Frederik Hauke, Patrick Wienholt, Christiane Kuhl 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models for medical image analysis typically lack a reliable measure of confidence, limiting their use in ambiguous or atypical cases. Here we show that Monte Carlo dropout, applied to a multi-task chest-radiograph classifier (eight thoracic findings, 137,593 training images), provides an epistemic uncertainty signal that tracks generalisation across training-set scales and flags confident yet error-prone predictions. Adding this signal to the point prediction raised error-detection AUROC from 0.74 to 0.77 ($\Delta$AUROC +0.023, 95% CI [+0.014, +0.033]). In a controlled 2x2 factorial experiment, a clinical-decision-support agent exploited this uncertainty only when it was delivered as a binary error-risk flag rather than as raw scores, cutting confident misdiagnoses on unreliable findings from 8.5% to 2.7%. Epistemic uncertainty estimation thus carries decision-relevant information beyond point predictions, but its value for downstream agents depends on how it is communicated.

---


### 60. [Exact ReLU realization of affine one-dimensional refinement iterates via residual memory and offset frames](https://arxiv.org/abs/2607.20586)

**<font color=#1a73e8>作者：</font>** Boldsaikhan Bolorkhuu, Tsogtgerel Gantumur  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study vector-valued affine refinement operators of the form [
(W\gamma)(t)=\sum_{j\in\mathbb{Z}} A_j\gamma(Mt-j)+B(t), ]
with finitely supported matrix mask and compactly supported continuous piecewise linear input and forcing data. Building on the homogeneous realization theorem for (B\equiv 0), we prove that, for (M\ge 3), every finite affine iterate (W^n\gamma) admits an exact fixed-width ReLU realization whose depth is (O(n)).
The main new ingredient is a residual memory controller. It replaces the noninvertible residual dynamics by an injective skew-product and permits exact backward replay of the residual states required by a Horner-type evaluation of the affine forcing sum. Offset frames align the forcing atoms away from residual seams, allowing complementary loop readouts to recover their values exactly. The remaining branch-selection ambiguity occurs only where the accumulated affine state has already vanished.
For (M\ge 3), the result applies to arbitrary compactly supported continuous piecewise linear forcing terms. For (M=2), the same construction applies to ordinary-frame seam-separated forcing. We also prove a stage-dependent extension for forcing terms in a fixed finite-dimensional continuous piecewise linear span and record the resulting linear-depth upgrade for open-curve, finite-state, and Hilbert- and Morton-type recursive constructions.

---


### 61. [Detecting Neural Network Failures through Spectral Analysis of Internal Activations](https://arxiv.org/abs/2607.20590)

**<font color=#1a73e8>作者：</font>** Arunan J  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural network misclassifications exhibit characteristic spectral instability in internal activations that is invisible at the output layer. This phenomenon is identified and formalized as Spectral Drift -- the frequency-domain distance between consecutive layer activations -- with empirical validation showing that failures exhibit significantly higher drift than correct predictions (1.9% increase, p<0.001). This spectral signature emerges during internal processing but becomes masked in final outputs, explaining why confidence-based detection methods struggle.
This work introduces Self-Detecting Neural Networks (SDNN), a framework that monitors spectral dynamics across network depth using Short-Time Fourier Transform, wavelet decomposition, and statistical moments to capture multi-scale spectral features. A lightweight detector network (5% parameter overhead) learns to identify failure-indicative patterns via curriculum learning on progressively challenging distributions: natural misclassifications, distribution shifts, and adversarial perturbations.
Experiments on CIFAR-10 demonstrate that SDNN achieves 79.0 +/- 25.3% AUROC across three seeds, substantially outperforming confidence-based baselines including MaxSoftmax (50.5%) and Energy Score (52.9%) by approximately 25-30 percentage points. Ablation studies reveal that wavelet decomposition and statistical features make consistent contributions, while STFT's role remains unclear. This work establishes spectral analysis of internal activations as a promising direction for neural network reliability, revealing diagnostic information inaccessible to output-based approaches.

---


### 62. [STeMP: Spatio-Temporal Modelling Protocol](https://arxiv.org/abs/2607.20592)

**<font color=#1a73e8>作者：</font>** Jan Linnenbrink, Jakub Nowosad, Marvin Ludwig 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal machine-learning modelling is an important tool in environmental research. However, machine-learning models are highly sensitive to both the characteristics of the training data, such as its distribution, and methodological choices, including the cross-validation strategy. Each decision has impact and implications on the model itself as well as the estimation of the model quality and applicability for certain purposes. Taking into account the large role of machine-learning based maps of the environment in science and their transfer into practice, transparent reporting of spatio-temporal models, ideally using standardized model protocols, is essential to enable trust, transparency and comparability. However, such protocols are currently lacking for spatio-temporal modelling.
We propose STeMP (Spatio-Temporal Modelling Protocol) to fill this gap by serving two purposes: standardized reporting to understand the model functioning as well as providing guidance during the modelling process by pointing at critical decisions and parameters. The protocol is structured in three sections: Overview, Model and Prediction. The Overview section contains metadata, while the Model and Prediction sections go into detail, describing predictors, evaluation and software, and further relevant elements of the modelling workflow.
The protocol definition is hosted on GitHub and accompanied by an R-package (this https URL). The R-package contains a web application that can be used to fill the protocol either manually or in a semi-automated way from provided modelling objects. Warnings are returned from the protocol when common pitfalls are encountered, which may help authors as a guide through the modelling process but also support reviewers in the assessment of modelling studies. Via GitHub, incorporation of contributions and feedback from the community is encouraged.

---


### 63. [When Does Recurrence Become an Algorithm? Convergence Selection in Weight-Tied Looped Transformers](https://arxiv.org/abs/2607.20594)

**<font color=#1a73e8>作者：</font>** Tong Zhang, Junhao Hu, Yun Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When does a weight-tied looped transformer -- one block applied T times -- implement an actual algorithm? We answer with four findings from controlled populations on group word problems. (1) The budget law: free training installs a linear computation frontier, a mechanism that solves v positions per loop, whose speed is priced by the training contract: v ~ n_train/T_train (exponent 0.98 +/- 0.04, R^2=0.99), exactly unity under T=n training. SGD selects a frontier matching the minimum the contract demands; granting more test-time loops than ever trained rescues late positions at fixed input length, yielding a principled halting rule T* = ceil(n / v-hat). (2) Architecture prior, not expressivity, picks the algorithm: standard-depth transformers learn parallel scans on this family; weight tying flips the selection to the serial frontier, even when positional addressing for a log-depth scan is supplied. At matched depth and parameters, untied models extrapolate worst and fail to learn A5 at all. (3) The walls are not where circuit complexity says: NC1-completeness costs nothing (A5 generalizes fully), while group order does (S5's 120x120 operator deadlocks joint learning) -- and an operator-first curriculum dissolves the wall in every seed. (4) Mechanisms are portable, not mandatable: warm-starting across budget contracts transfers the algorithm in every seed, re-pricing its speed, while imposing seriality through the input schedule fails where free training succeeds. These results are invisible to standard instruments, which provably saturate at the fixed points trained loops converge to. We introduce a head instrument, the convergence-time scaling tau(n,i), validate it causally via damage cones whose slope reproduces v, and show in-distribution head measurements predict out-of-distribution fate where tail metrics do not. Results replicate on the public easy-to-hard benchmark.

---


### 64. [RealVDeblur: One-Step Diffusion for Generalizable Real-World Video Deblurring](https://arxiv.org/abs/2607.20628)

**<font color=#1a73e8>作者：</font>** Renbiao Jin, Mingxin Yang, Yutian Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world video deblurring remains challenging due to diverse motion patterns, complex degradations, and the scarcity of realistic training data, yet robust restoration is critical for downstream pipelines such as mobile imaging and 3D reconstruction. This work presents \textbf{RealVDeblur}, an efficient generative framework designed to improve in-the-wild robustness under diverse real capture conditions. First, a large-scale, physically grounded blur synthesis pipeline is constructed from scene-level 3D Gaussian Splatting (3DGS) assets and high-frame-rate videos, providing realistic training data covering both camera-induced and object-motion blur. Second, a video diffusion prior is leveraged for restoration; to better accommodate frame-dependent blur variations, temporal compression in the VAE is disabled and a frame-wise encoding scheme is adopted. For practical deployment on long videos, multi-step diffusion sampling is distilled into an efficient one-step generator, and a training-free Temporal Window Mask stabilizes inference beyond the training horizon with constant memory usage. Extensive experiments on diverse real-world benchmarks demonstrate strong perceptual quality, semantic fidelity, and temporal consistency on unseen videos, as well as improved robustness in downstream 3D reconstruction under severe motion blur. Project page: this https URL

---


### 65. [One Round Is All You Need: Analytic Federated Learning for Task-Heterogeneous Multi-Label Medical Image Classification](https://arxiv.org/abs/2607.20641)

**<font color=#1a73e8>作者：</font>** Afsaneh Mahanipour, Hana Khamfroush  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables multiple clinical institutions to collaboratively train a shared disease classifier without centralizing patient data. In practice, however, each institution annotates only the pathologies within its area of expertise, so the federation operates under task heterogeneity: each client holds labels for a strict subset of the target disease categories while the remaining classes are entirely unobserved at that site. Existing gradient-based FL methods fail under this setting because they require hundreds of communication rounds to converge and because missing class labels introduce systematic false-negative bias that the model cannot correct without a principled mechanism. We propose an analytic federated learning framework for multi-label medical image classification under task heterogeneity. The proposed method replaces iterative gradient optimization with three closed-form operations: a balanced label projection that neutralizes class-imbalance bias by normalizing positive and negative contributions to equal total mass; a per-class absolute aggregation law that independently assembles the optimal ridge-regression classifier for each disease category from the sufficient statistics uploaded by its annotating clients; and an optional analytic pseudo-label refinement round that propagates missing-class knowledge from a confidence-filtered teacher classifier to non-annotating clients. The entire procedure requires at most two communication rounds, irrespective of the degree of task heterogeneity or the number of participating clients. Experiments on ChestXray14 under four progressively severe missing-class configurations demonstrate that the proposed method consistently outperforms the state-of-the-art federated multi-label method FedMLP by up to 18.44 BACC points and 13.24 AUC points, while reducing the communication.

---


### 66. [Masked Topology Modeling for Self-Supervised Learning on Parametric CAD](https://arxiv.org/abs/2607.20642)

**<font color=#1a73e8>作者：</font>** Heinrich Jiang, Jennifer Jang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer aided design (CAD) is ubiquitous: virtually any modern object was designed using editable CAD tools. However, with the shortage of available CAD datasets in its native editable and parametric format, boundary representation (B-Rep), it is ever more important to develop data-efficient methods for this domain.
We present a new self-supervised pretraining task, Masked Topology Modeling (MTM), that leverages the face-adjacency graph, an induced structure unique to B-reps that the encoder can be asked to reconstruct. MTM masks a fraction of edges and trains a small head to predict each masked edge's convexity and curve type from the encoder's post-message-passing face features.
We combine MTM with a MoCo-style momentum-queue contrastive learning over B-rep-aware augmentations, a BFS-connected face-region masked-reconstruction objective, and pretraining on the ABC dataset and our new procedurally generated dataset to show strong performance on a number of benchmarks.

---


### 67. [Frontier Financial Judgement: Can agents tell what might move a stock?](https://arxiv.org/abs/2607.20645)

**<font color=#1a73e8>作者：</font>** Joshua Harris  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Frontier Financial Judgement, a challenging new benchmark developed in collaboration with professional equity analysts to assess agents' ability to replicate expert human judgements. Rapidly identifying new information, evaluating its implications and determining its valuation impact is one of the most time-consuming and challenging aspects of real-world equity coverage. This is becoming ever more difficult and important as AI rapidly increases the quantity of new information to process. The strongest agent we evaluate on Frontier Financial Judgement matches all expert labels in only 52.4% of cases. We also find significant divergence in estimated false-positive rates among frontier agents, ranging from ~1% for GPT-5.6 Sol to ~32% for Claude Sonnet 4.6. To construct the benchmark and make it representative of real-world settings, we combine human-designed and labelled synthetic articles with live news articles and historical documents, creating 656 items for assessment. The resulting task requires agents to distinguish genuinely new, valuation-relevant financial information from stale, immaterial or misleading news under realistic conditions. We find substantial trade-offs among agent accuracy, cost, false positives and reliability that continue to hinder the reliable deployment of news-flow filtering in practice.

---


### 68. [Scaling Interpretable Transformers with Parity Bottleneck Layers](https://arxiv.org/abs/2607.20652)

**<font color=#1a73e8>作者：</font>** Andrew Mack, Kraig Yuheng Tou, Mark Henry 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are thought to exhibit the phenomenon of superposition, representing many more features than dimensions in their residual streams. Sparse autoencoders (SAEs) are designed to recover such features post-hoc, but training models that are interpretable by construction has remained impractical, as a per-layer over-complete bottleneck is prohibitively expensive in both memory and compute. To overcome this issue, we introduce the ParityTransformer, a GPT-2-scale architecture whose intermediate representations are efficient and wide / sparse by design. At each layer, a Deep Parity Bottleneck (DPB) replaces a learned over-complete basis with a parameter-free algebraic dictionary, providing a deterministic incoherence guarantee and eliminating the memory requirements that have prevented per-layer interpretable bottlenecks at scale. A DPB is a hierarchically structured sparse bottleneck which efficiently enforces sparsity using a multi-level mixture-of-experts approach: a hardware-aware implementation that closes the cost gap between activation sparse and dense training to a manageable interpretability tax. Empirically, ParityTransformers perform at least as well as post-hoc SAEs on sparse probing tasks, while out-performing on measures of feature absorption, steering effectiveness, and fine-grained causal interventions. Because subsequent computation acts only on features that survive the sparse bottleneck, the ParityTransformer's features are native to the model's forwards pass by construction, addressing the question of whether SAEs probe features the model actually uses during computation. We see this as a step toward training models whose internal representations are interpretable by design rather than recovered post hoc.

---


### 69. [SalesLoop: Reinforcement Learning from Performance Feedback for Sales Lead Ranking](https://arxiv.org/abs/2607.20655)

**<font color=#1a73e8>作者：</font>** Chenyu Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lead ranking in Customer Relationship Management (CRM) systems faces a persistent challenge: models achieving high offline accuracy often underperform in production. We identify three fundamental gaps responsible for this disconnect: offline-online metric mismatch, pointwise-listwise objective misalignment, and temporal distribution drift. To address these gaps, we propose SalesLoop, a reinforcement learning framework that establishes a closed feedback loop between model predictions and real-world business outcomes. Our approach introduces (1) a performance-aware reward that encodes conversion outcomes weighted by ranking position and conversion velocity, and (2) Discriminative GRPO, a listwise optimization objective that adapts Group Relative Policy Optimization to discriminative ranking models.
SalesLoop improves NDCG@K by +7.9\% and P@K by +15.8\% over the strongest static baseline. A 160-day production A/B test at a New Energy Vehicle manufacturer, spanning 16.5M leads and 280 sales specialists across two provincial markets, validates statistically significant cumulative lift of +4.7\% ($p=0.047$) and +8.7\% ($p=0.002$). In production, the ranking backbone achieves Top-10\% recall of 44.1\% and surfaces high-intent leads at $2.3\times$ the conversion rate of specialist baselines.

---


### 70. [Adaptive Multi-Horizon Reinforcement Learning](https://arxiv.org/abs/2607.20656)

**<font color=#1a73e8>作者：</font>** Manoosh Samiei, Doina Precup, Paul Masset  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective decision-making in complex and changing environments requires balancing short-term and long-term consequences. In reinforcement learning (RL), this trade-off is typically controlled through a fixed discount factor, which imposes a single exponentially discounted temporal horizon. However, biological agents exhibit flexible and adaptive temporal discounting, suggesting that effective planning requires multiple timescales. Here, we propose a multi-horizon approach that adaptively selects and combines temporal horizons, enabling robust adaptation to changes in reward structure without manual discount-factor tuning. This flexibility makes the method particularly suitable for continual learning scenarios involving task switches and varying environmental configurations. Empirically, we demonstrate that our approach identifies effective discount factors across a range of MiniGrid environments, including continual settings composed of three sequentially changing tasks. These results suggest that adaptive temporal discounting can improve parameter efficiency and enhance adaptability in both artificial and biologically inspired learning systems.

---


### 71. [Axolotl3D: a Unified Framework for Faithful 3D Shape Completion](https://arxiv.org/abs/2607.20660)

**<font color=#1a73e8>作者：</font>** Anita Hu, Maria Shugrina  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent 3D generative models produce high-quality geometry from a single image using large-scale priors and diffusion architectures. However, they assume complete visibility and single-view inputs, limiting applicability in multi-view, occluded, or editing scenarios. Although prior works address these challenges individually, they lack a unified framework for controllable 3D completion under diverse conditioning signals. We present Axolotl3D, a multi-modal and occlusion-aware 3D generation model that jointly conditions on images, visibility masks, camera parameters, and a partial point cloud. The point cloud serves as a geometric anchor promoting faithful shape completion, while camera parameters ensure consistent multi-view alignment in a shared 3D coordinate system. A unified training strategy synthesizes diverse conditioning regimes from large-scale 3D data, enabling robust cross-modal reasoning. Experiments on Toys4K and OmniObject3D demonstrate state-of-the-art performance under both clean and occluded settings, as well as strong results in real-world reconstruction and geometry-consistent editing.

---


### 72. [From Agent Failures to Text Policies: What Works and What Breaks](https://arxiv.org/abs/2607.20668)

**<font color=#1a73e8>作者：</font>** Jaideep Ray, Ankit Goyal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> TextGrad improves language-model systems by revising text from feedback. Its core thesis is that natural-language feedback can act as a gradient for optimizing text components without changing model weights. Applying it to agents is harder because feedback arrives only after a sequence of actions, making it difficult to identify which decision caused failure. We study this problem by separating the ability to follow a useful policy from the ability to learn that policy from experience. Our main finding is a clear gap between these two abilities. Human-written policies improve two frozen 7B agents on TextWorldExpress by 5.0 success points, showing that useful policy text exists. However, policies generated from agent trajectories do not reliably outperform fixed prompting, even with richer traces, counterfactual evidence, or iterative GEPA search. The main challenge for agent-level TextGrad is therefore not executing textual policy updates, but reliably generating and selecting them from experience.

---


### 73. [ODeform: Learning Continuous 4D Motion for Shape Deformation with Neural ODEs](https://arxiv.org/abs/2607.20670)

**<font color=#1a73e8>作者：</font>** Yordanka Velikova, Mahdi Saleh, Liming Kuang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modeling continuous object deformation is important for many computer vision and robotics tasks, such as manipulation and simulation. Existing approaches rely on learning-based methods or physics simulators to model shape deformations. However, these approaches either use discrete time steps or are too computationally intensive for real-time applications. We present ODeform, a novel extension of Neural Ordinary Differential Equations to continuous 4D dynamics of deformable objects in 3D space. Our method transforms 3D point clouds and physical conditions (like material properties) into a unified latent space. By solving the resulting ordinary differential equations over time, we model deformations as continuous flows within this learned embedding, eliminating the need for discrete time steps while maintaining computational efficiency. We evaluate our approach on unseen physical parameter configurations, showing improved motion prediction accuracy over baseline methods. Our experiments further demonstrate a successful transfer to real 3D captured objects with novel shapes, along with effective interpolation and extrapolation of the learned dynamics. Our code and data will be made publicly available.

---


### 74. [End-to-End Learning of Safe Optimal Feedback Control in High Dimensions with Control Barrier Function Layers](https://arxiv.org/abs/2607.20674)

**<font color=#1a73e8>作者：</font>** Xingjian Li, Kelvin Kan, Deepanshu Verma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problem of learning high-dimensional semi-global feedback controllers under hard safety constraints enforced by control barrier functions (CBFs). Incorporating CBFs into end-to-end policy training requires embedding a quadratic-program-based safety filter as an optimization layer, but computational and differentiation bottlenecks have largely restricted prior approaches to low-dimensional systems, typically with at most 16 state dimensions. We address this limitation by combining operator splitting with the recently developed Jacobian-Free Backpropagation (JFB) method to enable scalable end-to-end training while preserving hard safety guarantees through the CBF safety filter. We justify this training methodology theoretically using nonsmooth analysis techniques and demonstrate its effectiveness on high-dimensional multi-agent nonlinear control problems with state and control dimensions up to 1200 and 400, respectively.

---


### 75. [Explanation-Based Runtime Verification for Trustworthy ML-driven Optical Networks](https://arxiv.org/abs/2607.20675)

**<font color=#1a73e8>作者：</font>** Omran Ayoub, Carlos Natalino, Ali Al Housseini 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) models are increasingly integrated into optical network automation frameworks to support tasks such as failure management, performance monitoring and resource allocation. In these environments, ML-driven predictions may be directly coupled with control-plane actions where incorrect decisions can immediately impact service quality, resource efficiency, and network stability. As automation levels increase, ensuring the reliability of individual decisions at deployment time becomes a critical requirement. Explainable artificial intelligence (XAI) techniques have emerged to improve transparency by highlighting the factors influencing ML predictions. In addition to identifying influential features, they provide insights into the underlying reasoning process of the model, revealing how different input variables contribute to the final outcome and how feature interactions shape the decision boundary. In this work, we introduce explanation-based runtime verification, an approach that exploits model explanations to assess the soundness of individual ML decisions before they are executed in the network control loop. The proposed approach evaluates explanation coherence and physics grounding consistency at runtime, enabling the system to defer or reject decisions flagged as uncertain. We demonstrate the effectiveness of our approach on a representative use case of lightpath quality of transmission classification. Experimental results show that explanation-based verification can intercept a significant fraction of erroneous decisions while preserving high automation rate.

---


### 76. [Enhancing Attack Detection Capabilities in BACnet/IP Networks Using Machine-Learning Models](https://arxiv.org/abs/2607.20686)

**<font color=#1a73e8>作者：</font>** Derek Manzella, John D. Hastings  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Building Automation Systems (BAS) manage critical building functions using protocols such as BACnet/IP, yet defenders have limited tooling and few labeled datasets for detecting BACnet-specific attacks. This work addresses these gaps through three contributions. First, CISA's Zeek BACnet parser is modified to produce a unified per-packet log, simplifying feature engineering for machine-learning (ML) pipelines. Second, a simulated BACnet/IP testbed is developed using bacpypes3 to model a small commercial HVAC system with physics-based device behavior, schedule-aware controller logic, and per-packet attack labeling. Third, five unsupervised anomaly detection models are evaluated using baseline traffic and six BACnet attack types, including denial of service, reconnaissance, property tampering, and false data injection. Results show that One-Class SVM achieved the strongest overall performance, with an average F1 score of 0.864 across all attacks and F1 scores above 0.99 for high-volume denial-of-service and reconnaissance attacks. Detection is much stronger for high-volume attacks, such as DoS attacks and reconnaissance, than stealthier techniques such as tampering and false data injection, which scored around 77%.

---


### 77. [Spatially Grounded Concept Bottleneck Models for Trustworthy Breast Ultrasound Diagnosis](https://arxiv.org/abs/2607.20691)

**<font color=#1a73e8>作者：</font>** Moshiur Rahman Tonmoy, Dunren Che, Haitham Y. Adarbah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept Bottleneck Models provide interpretable-by-design predictions by mediating diagnosis through human-understandable concepts, but in medical imaging, their trustworthiness is often limited by the quality and granularity of available supervision. In particular, predicted concept activations can be driven by irrelevant regions, leading to spatially unfaithful explanations. We study a data-centric spatially grounded Concept Bottleneck Model (SG-CBM) that leverages coarse lesion delineations as weak supervision to encourage anatomically plausible concept evidence. For breast ultrasound, we derive two clinically motivated zones from each lesion mask: (i) an in-lesion region of interest for morphology-related concepts and (ii) a posterior acoustic band for posterior phenomena. We train concept maps using a grouped spatial grounding objective and preserve semantic faithfulness with a linear bottleneck classifier. Across five-fold stratified group cross-validation, the proposed SG-CBM improves diagnostic AUROC and concept macro-AUROC while markedly increasing spatial alignment of concept evidence. We also perform a Train-corrupt/Test-clean annotation-quality stress test to quantify the impact of supervision quality on diagnosis and spatial faithfulness. Overall, the results underscore the need for data-quality-aware supervision design and systematic trustworthiness validation for deployable healthcare AI systems.

---


### 78. [DS@GT ARC at ImageCLEFmed GANs 2026: Geometric Filtering for Privacy-Preserving CT Slice Generation](https://arxiv.org/abs/2607.20692)

**<font color=#1a73e8>作者：</font>** Eric Regina, Richard Arnaud, Samir Hadi Cisneros  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a privacy-preserving framework for synthetic lung CT slice generation developed for the Image-CLEFmed GANs 2026 challenge. The approach combines Optimal Transport Conditional Flow Matching with privacy-oriented training and a post-generation "Supervisor" pipeline that filters generated candidates in learned geometric latent spaces using autoencoder embeddings, Determinantal Point Processes, and Stein Kernel Thinning. Official results show a strong realism-privacy trade-off, with the best-performing model achieving a Privacy Preservation Score of 0.549 and competitive visual fidelity with an FID of 0.3290. While the proposed geometric filtering substantially reduces nearest-neighbor memorization and membership-inference leakage, persistent patient re-identification scores indicate that preventing direct image copying is not sufficient to remove deeper patient-specific anatomical identity, highlighting an important frontier for future privacy-preserving medical image generation.

---


### 79. [Attribution Markets: A Fisher-Market Formulation for Fractional Credit Assignment Between Planned Tasks and Performed Actions](https://arxiv.org/abs/2607.20694)

**<font color=#1a73e8>作者：</font>** Salavat Ishbulatov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personal and organizational planning systems maintain two records that drift apart: what was planned (a task's effort budget) and what was done (a logged action's duration and description). Existing systems bridge them with an exclusive, all-or-nothing link that strands genuinely related but unlinked effort and reports false stalls on active goals. We formulate the bridge as a quasi-linear Fisher market: planned tasks are budget-constrained buyers, performed actions are divisible goods, and a fused text/structural/temporal signal sets each buyer's valuation. Two market instruments - a seller reserve price and a buyer cash option - yield conservation, a hard budget cap, and a provable junk filter as theorems. We extend the market with a concave completion utility discounting progress as a task nears its plan; standard convergence theory for the market's algorithm does not transfer here, resolved by a satiation-threshold fixed point with existence (Brouwer) and local uniqueness under an explicit diagonal-dominance condition, validated empirically on random and adversarial instances. A de-circularized, multi-seed benchmark - observed affinity corrupted independently of the scored ground truth - surfaces a genuine weak spot: the market's sharp, zero-entropy equilibrium is more sensitive to affinity noise than entropy-regularized optimal transport's permanently smoothed one. We resolve this with a one-parameter entropy-regularized generalization unifying the two, plus a noise-adaptive rule for its regularization strength. We report full reproducibility parameters, discuss limitations candidly, and relate the result to multi-touch attribution, optimal transport, and online Fisher-market algorithms.

---


### 80. [CEDAR: Causal Edge Discovery for Autoregressive Processes](https://arxiv.org/abs/2607.20696)

**<font color=#1a73e8>作者：</font>** Mohammad Fesanghary  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose CEDAR (Causal Edge Discovery for Autoregressive Processes), a constraint-based method for lagged causal edge discovery in sparse autoregressive time series. CEDAR screens candidate cross-variable lags using AR(1)-residualized, U-centered distance correlation, then applies two targeted conditional-independence tests per significant cross-variable lag candidate and accepts at most one lag per ordered pair. A stable MCI pruning step removes indirect edges, and optional deterministic C-nodes adjust for specified trend-like nonstationarity. In sparse regimes where few lags survive screening, CEDAR requires $O(d^2)$ CI tests after screening while retaining edge-level interpretability. CEDAR is most effective when data are scarce and variables exhibit lag-1 self-dynamics; methods with richer conditioning sets become preferable as $T$ grows or when higher-order autoregressive or simultaneous multi-lag effects are common.

---


### 81. [Buzz to Boom: Detecting Message Progression Vulnerabilities in Electron Applications via Segmented Directed Fuzzing](https://arxiv.org/abs/2607.20698)

**<font color=#1a73e8>作者：</font>** Jianjia Yu, Zhengyu Liu, Ziyang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Electron is a popular framework for building cross-platform desktop applications using web technologies. Such applications consist of multiple processes with different privilege levels that communicate via message passing. When inter-process messages carry attacker-controlled inputs, they can propagate across processes and reach privileged APIs, e.g., command execution. Such a message propagation behavior is characterized as Message Progression Vulnerabilities (MPVs). The exploitation of MPVs is challenging because it often requires multiple steps, e.g., first arbitrary code execution in one process via message passing, and then command injection in another process using another message crafted in the first process. To our knowledge, existing works on Electron security only study unsafe configurations and malicious Document Object Model (DOM) content, i.e., they cannot detect or exploit these vulnerabilities that need to be triggered by complex cross-process exploits via message passing. We present Proton, a segmented directed fuzzing framework for detecting MPVs. Our key insight is to decompose end-to-end fuzzing into per-process segments along message-passing boundaries, where the goals of fuzzing each segment are either: (i) reaching a sink in the current process or (ii) propagating the payload to the next process, to enable the exploration of another process. In the second case, the messages seed the corpus of the next segment. Finally, Proton synthesizes crash inputs from each process to validate end-to-end exploits. We evaluate Proton against 589 real-world Electron applications, resulting in 23 zero-day MPVs. Among them, 22 lead to OS command execution, including projects with over 50k GitHub stars. We responsibly disclosed all findings. To date, we have received 13 acknowledgments, 11 fixes, and 11 CVEs, including a bug bounty from Vercel.

---


### 82. [U-CFR: Uncertainty-Guided Cascade Forward Refinement for Interactive Segmentation](https://arxiv.org/abs/2607.20705)

**<font color=#1a73e8>作者：</font>** Elijah Danquah Darko, Min Xian, Terence Soule 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive image segmentation is critical for efficient image annotation; however, existing methods often require many corrective clicks or rely on passive refinement schemes that converge slowly. We propose Uncertainty-Guided Cascade Forward Refinement (U-CFR), a novel inference-time framework that enables models to autonomously self-correct after each user interaction. U-CFR introduces a boundary-aware uncertainty score that fuses segmentation uncertainty, contour gradients, and explicit edge predictions to guide the placement of internal pseudo-clicks. These self-generated clicks target the most ambiguous boundary regions, providing strong corrective signals without additional manual input. To support this process, we design a dual-head network with a shared encoder-decoder backbone: a segmentation head ensures region consistency, while an edge head sharpens boundary alignment. In inference, U-CFR launches a cascade of refinement steps, where each stage leverages the uncertainty-driven pseudo-clicks to refine the mask progressively. Experiments on standard benchmark datasets demonstrate that the proposed U-CFR improves click efficiency, initial mask quality, and boundary accuracy. It reduces the required clicks by over 10% on challenging datasets like Berkeley and offers a more intelligent and efficient interactive annotation.

---


### 83. [Perspective Latents as an Architectural Condition for Causal Emergence in Active Inference Agents](https://arxiv.org/abs/2607.20708)

**<font color=#1a73e8>作者：</font>** Hongju Pae  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A recent line of work measures causal emergence in reinforcement learning agents through Integrated Information Decomposition, reporting that $\Phi_r$ grows with training and tracks reward improvement. For active inference, this raises the question of how reward-free predictive organization relates to such information-theoretic signatures. I test this within an active inference agent whose architecture separates a fast perception latent $z$ from a slow global latent $g$, where $g$ is driven by prediction error and structurally decoupled from policy gradients. In a reward-free environmental regime-switching protocol, $\Phi_r$ concentrates in $g$; its aggregate magnitude is largely architectural and decreases with training. The substantive effect of learning becomes legible only at the atom-compositional level: decoupling flips sign from negative to positive and becomes regime-invariant under environmental change, while downward causation carries the regime-dependent adjustment. These results identify $g$ as the architectural locus of $\Phi_r$-relevant temporal organization in an active inference agent, and argue against reading scalar $\Phi_r$ as a direct index of learned integration.

---


### 84. [NVIDIA-labs OO Agents: Native Python Object-Oriented Agents](https://arxiv.org/abs/2607.20709)

**<font color=#1a73e8>作者：</font>** Paul Furgale, Severin Klingler, James Nolan 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional agent development is split across prompt templates, tool schemas, callback code, and workflow graphs. We present NVIDIA Object-Oriented Agents (NOOA), a model-agnostic Python framework for building reliable AI agents. NOOA takes a simpler approach: an agent is a Python object. Its methods are the actions the model can take, fields are its state, docstrings are its prompts, and its type annotations are contracts. A method whose code body consists of "..." is completed at runtime by an LLM-driven agent loop, while methods with normal bodies remain standard deterministic Python. This gives developers and agents the same interface, so agent behavior can be tested, traced, refactored, and improved just like other software.
This paper makes three contributions. (1) We present the agent-as-a-Python-object programming model and the design principles behind it. Where Python has existing abstractions, we adopt them directly. Agent-specific capabilities--context, events, state rendering, long-term memory, and validated LLM loops--are exposed through simple Pythonic APIs, so both developers and agents share one familiar programming model. (2) We identify six model-facing ideas that NOOA is, to our knowledge, the first to combine on a single surface: typed input/output, pass-by-reference over live objects, code as action, programmable loop engineering, explicit object state, and model-callable harness APIs for context and events. We find the community already converging on several of these ideas--often as experimental or partial features--and present the comparison to encourage further adoption. (3) We demonstrate that current models use this interface effectively, both in targeted capability tests and on agentic and reasoning benchmarks such as SWE-bench Verified and Terminal-Bench 2.0 and ARC-AGI-3.

---


### 85. [GPE: Evaluating Robust Evidence Aggregation for Fact Verification under Controllable GEO-Style Poisoning](https://arxiv.org/abs/2607.20730)

**<font color=#1a73e8>作者：</font>** Zhaoqi Wang, Zijian Zhang, Xiaomei Yuan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly use search tools to retrieve up-to-date information, introducing a new attack surface in which retrieved documents can be manipulated. This risk is amplified by the development of generative engine optimization, which can make selected content more likely to be retrieved, cited, and adopted by models. Existing fact-verification benchmarks and evaluation frameworks do not provide the controlled evidence environments needed to assess robustness against GEO poisoning. We therefore propose GPE, which consists of a multi-domain fact-verification benchmark and an evaluation framework for controlling evidence sources and poisoning ratios. Experiments across multiple verification methods and poisoning attacks demonstrate that GPE exposes robustness degradation and efficiency trade-offs that cannot be observed through clean evaluation alone, confirming the need to evaluate fact verification under adversarial evidence environments.

---


### 86. [Cardinality-Decomposed Loss: Matching Training Objectives to Relation Structure in Heterogeneous Recommendation Graphs](https://arxiv.org/abs/2607.20737)

**<font color=#1a73e8>作者：</font>** Parul Maheshwari, Amulya Paruchuri, Yiqing Zou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks trained on heterogenous bipartite graphs form a common basis in recommendation systems. These graphs often express relations that vary in cardinality, for example, user-item preferences are one-to-many and user-attribute features are one-to-one. Traditionally, a unique loss function is applied for all of the network components which is often Bayesian Personalized Ranking (BPR). While BPR works well for the recommendation task, we find that it causes attribute embeddings to collapse to near-random geometry -- a silent failure that leaves standard ranking metrics largely unaffected and therefore invisible to conventional evaluation. This in turn pollutes user node embeddings, which are shaped by both edge types simultaneously, hurting downstream tasks like personalization, segmentation, etc. Here we propose a Cardinality-Decomposed Loss (CDL) that combines both Cross Entropy (CE) and BPR to enable the model to collectively optimize for relations across cardinalities. We confirm this CE-BPR conflict by showing the two losses compete in the shared encoder's parameter space. We evaluate CDL on five datasets spanning two structural configurations -- one-to-one attributes on user nodes (MovieLens-1M, this http URL-360K, PayPal Audience Factory, BookCrossing) and on item nodes (Yelp) -- and find that CDL consistently improves discriminability in attribute embeddings. We also show that ranking (NDCG) improves when attributes carry meaningful preference signal, but conflicts with it when the correlation is weak. We use a lambda parameter to navigate this trade-off, and a lambda-sweep reveals that dataset behavior is governed by two graph properties -- semantic alignment and topology leakage. Semantic alignment measures whether the attribute predicts preferences, while topology leakage measures whether the graph's connectivity already encodes it.

---


### 87. [ArbiGraph: Arbitrarily Scalable Verifiable Task Graphs for Evaluating Context Management](https://arxiv.org/abs/2607.20764)

**<font color=#1a73e8>作者：</font>** Pavel Golikov, Evgenii Opryshko, Gennady Pekhimenko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce ARBIGRAPH, a benchmark generator for evaluating whether tool-assisted language agents can retain, update, compose, and discard task-relevant context across extended reasoning workflows. ARBIGRAPH represents each task as a natural-language problem with an executable Python solver, and composes tasks through typed intermediate states, instantiated here as scalar and list values. This design enables controllable task graphs whose length, dependency structure, distractor count, and value type can be varied while preserving exact automatic verification. We instantiate ARBIGRAPH with math, GSM-style word-problems, and Python-tracing task categories, and evaluate a Qwen3.5-27B tool-assisted agent across four topologies. The results show high accuracy on isolated tasks but substantial degradation on more complex dependent tasks: accuracy drops by up to 33.3% on branching chains of dependent math tasks. This shows that ARBIGRAPH exposes failures that are not visible from single-task evaluation alone. Our code, generated datasets, and evaluation results are available at this https URL

---


### 88. [Memory-Computation Tradeoffs in Semi Amortized Parametric Optimization](https://arxiv.org/abs/2607.20769)

**<font color=#1a73e8>作者：</font>** Shijie Pan, Agustin Castellano, Zeyu Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning-enabled decision systems often use offline data or computation to reduce online compute cost. Despite the empirical success of such approaches, there is limited general understanding of how much offline information is needed to achieve a desired accuracy under a fixed online computation budget. We study this question through the lens of amortized parametric optimization: an offline phase stores a finite memory of solved problem instances, and an online phase produces a solution to a new instance by retrieving a warm start and applying $K$ steps of projected gradient descent. We analyze this setup for smooth convex parametric optimization over a compact domain, using a nonparametric predictor built from the stored offline solutions. For $\mu$-strongly convex objectives, we establish matching upper and lower bounds on the memory required to guarantee $\varepsilon$-accuracy under a fixed online iteration budget $K$. For convex objectives satisfying a $\beta$-growth condition ($\beta>2$), we obtain near-matching bounds and identify a phase transition in $K$ beyond which additional memory provides no benefit. We further provide a general proof framework that (i) explicitly quantifies the memory cost of acceleration---how much offline memory is required to achieve a prescribed speedup over the unaided online optimizer---and (ii) identifies two key quantities driving this cost: the convergence rate of the online optimizer and the Lipschitz sensitivity of the solution map to the problem parameter. Experiments on parameterized ridge regression confirm the predicted memory--computation--accuracy tradeoffs.

---


### 89. [HARP: The Human--AI Research Platform](https://arxiv.org/abs/2607.20773)

**<font color=#1a73e8>作者：</font>** Zeshu Zhu, Natalie Friedman, Kevin Weatherwax 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shifted human--computer interaction from `traditional'' interface journeys toward more conversational exchanges. Researchers studying HCI and UI use moderated usability sessions, interviews, surveys, transcript analysis, and static prototypes. However, static prototypes provide limited opportunities to study interaction with live AI systems or systematically control how an LLM behaves across participants and scenarios. Conversation transcripts reveal little about how users formulate, revise, and hesitate over prompts before submission. We designed the Human--AI Research Platform (HARP) for researchers, designers, and anyone who has ever wondered, `What if AI did this?' HARP places participants in controlled mock scenarios with live, configurable AI agents. Researchers can control agent prompts, model parameters, response characteristics, and experimental conditions; trigger surveys at predefined moments; and record prompt composition time, response latency, deletions, and keystroke pauses. Planned capabilities include voice, facial expression, gesture, and, where legally and ethically appropriate, emotion analysis. We illustrate HARP through a study examining how technical specificity and response length affect retention of LLM output. By pairing controllable live agents with behavioral and self-report measures, HARP enables systematic testing of how AI design choices affect users.

---


### 90. [Flint: A Semantics-Driven Data Visualization Intermediate Language](https://arxiv.org/abs/2607.20775)

**<font color=#1a73e8>作者：</font>** Yunhai Wang, Kecheng Lu, Junhao Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present Flint, an intermediate language that enables authors to create high-quality visualizations from concise, semantics-driven specifications without explicitly configuring low-level parameters such as scales, axes, and formatting. Unlike prior systems that infer default configurations from surface-level data representations, often producing brittle choices, Flint introduces a hierarchical data semantic model that allows users to specify the meanings of data fields structurally and helps the compiler derive appropriate visualization configurations. From a concise specification, the system generates and optimizes library-agnostic visualization configurations and translates them into complete, executable specifications for multiple target grammars, including Vega-Lite, Apache ECharts, and this http URL. We demonstrate that Flint simplifies the authoring process without compromising on visual quality, and it is an effective intermediate language for both humans and AI agents to create visualizations.

---


### 91. [Rethinking Open-World Video Anomaly Detection: Diagnosing Definition Blindness](https://arxiv.org/abs/2607.20780)

**<font color=#1a73e8>作者：</font>** Inpyo Song, Jangwon Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-world video anomaly detection (OWVAD) is expected to detect events that match a user-specified definition of abnormality. This requirement is stronger than generic anomaly localization: in the same video, changing the definition should change which temporal regions are scored as anomalous. We show that current OWVAD evaluation largely fails to isolate this conditional behavior. Standard VAD metrics and the dynamic-definition protocol can be dominated by target-versus-normal separation, allowing models to obtain strong scores while remaining nearly insensitive to the queried definition. We call this failure mode definition blindness. To explain why it is missed, we decompose dynamic-definition evaluation into target-versus-normal detection and target-versus-other-anomaly discrimination, and find that the former receives 7.2-26.8$\times$ more weight across common VAD benchmarks. Motivated by this diagnosis, we introduce three definition-conditioned evaluation metrics, DC-Disc, DC-Det$\Delta$, and DC-Sel$\Delta$, which progressively remove normal-frame, generic-anomaly, and multi-event selection shortcuts. Experiments on UCF-Crime, XD-Violence, and MSAD reveal that several strong VAD, OWVAD, and general vision language model baselines localize anomalous moments but exhibit weak definition following, often with near-zero definition-response margins. To validate that the failure is actionable, we further introduce DeCoS, a definition-contrastive scoring rule that subtracts anomaly evidence shared across definitions. DeCoS improves the strongest baseline by 7.3-16.0 AUROC points on DC-Disc and 15.5-28.3 points on DC-Det$\Delta$. Overall, our results argue that OWVAD should be evaluated as definition-conditioned anomaly scoring, not as anomaly detection under different prompt labels.

---


### 92. [The Human-AI Substitution Principle: When will you be replaced by AI in your organization?](https://arxiv.org/abs/2607.20781)

**<font color=#1a73e8>作者：</font>** Bonny Banerjee, Shreya Singh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) is rapidly transforming organizations, raising a fundamental organizational and economic question: when will a human employee be replaced by AI? We present an analytical model for studying Human--AI Task Allocation (HAT) in hierarchical organizations. A central feature of the HAT model is that it formally encodes the economic asymmetry between human skill acquisition and AI capability scaling. The HAT model allows us to derive how risk-adjusted costs, skills, organizational depth, deployment scale, strategic adaptation, and risk jointly determine when, where, why, and under what structural conditions human--AI replacement occurs. A key result is the Human--AI Substitution Principle, which provides a precise condition --- grounded in the formal asymmetry assumption --- under which AI replaces human labor. Building on this result, we show that AI adoption can produce abrupt workforce transitions, hybrid human--AI organizations, including cases where risk heterogeneity sustains human and AI roles without requiring a minimum-human-fraction constraint, and flatter managerial hierarchies with wider spans of control. The HAT model identifies structural conditions under which middle-management roles exhibit elevated vulnerability to automation, and shows that the vulnerability of highly skilled workers depends on a skill threshold shaped by organizational depth, baseline costs, and risk differentials. More broadly, the paper connects automation economics, organizational design, AI governance, and workforce planning into a unified theory of AI-driven organizational transformation.

---


### 93. [Synthetic minority data is redundant or invalid: a data-dependent validity theory and a de-biased test](https://arxiv.org/abs/2607.20787)

**<font color=#1a73e8>作者：</font>** Ahmad B. Hassanat, Ahmad S. Tarawneh, Ghada A. Altarawneh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For two decades, the standard remedy for class-imbalanced learning has been to fabricate synthetic minority examples, and the standard evidence of their validity has been a check that cannot fail: synthetic points are scored against the very data that generated them. We de-bias the check. Validity becomes a population quantity -- the probability that a synthetic point truly belongs to the minority class -- with a consistent estimator that scores synthetic points against withheld real data. Where held-out ground truth is available, the classical test underestimates true invalidity in 96-99% of method-by-imbalance-ratio cells, while the de-biased estimator tracks it closely. We prove validity is a property of the data, not the method: class overlap sets an invalidity floor no faithful generator escapes, making oversampling redundant where classes separate and invalid where they overlap. Across 91 methods, three classifiers, and datasets spanning medicine and finance -- including a generator engineered to pass the classical check -- none clears both bars: gains over the best trivial baseline are noise-thin (median below 0.01 F1, a decision threshold's reach), and most damage calibration. We release the audit as a pip-installable test and flip the burden of proof: synthetic minority data must now demonstrate, on the data at hand, both validity and information gain.

---


### 94. [3D-GIMP: When 3D Gaussian Inpainting Meets PatchMatch](https://arxiv.org/abs/2607.20789)

**<font color=#1a73e8>作者：</font>** Xuening Tian, Dieter Schmalstieg, Shohei Mori  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D scene editing have leveraged iterative diffusion models to update input views. However, this process is computationally expensive and struggles to produce sharp details. Meanwhile, ``hallucination drift'' frequently introduces multi-view inconsistencies, leading to structural artifacts when rendering novel viewpoints. To address this problem, we present 3D-GIMP (3D Gaussian Inpainting Meets Patch Matching), a novel hybrid paradigm designed for high-fidelity object removal in 3D Gaussian Splatting. Instead of diffusing every view, 3D-GIMP performs a single generative inpainting on a key reference view, which serves as an appearance prior. We then introduce a 3D-aware PatchMatch algorithm to propagate these reference textures across all remaining views via correspondence matching, effectively bypassing the stochastic nature of frame-by-frame diffusion. By prioritizing reconstructive consistency over iterative generation, 3D-GIMP maintains high-frequency details across arbitrary resolutions while ensuring a mathematically consistent 3D reconstruction. Our experiments demonstrate that 3D-GIMP not only achieves competitive inpainting quality as previous methods using diffusion in multiple views, but also outperforms these methods in rendering speed and view consistency.

---


### 95. [Ocular Verification for Virtual Reality](https://arxiv.org/abs/2607.20790)

**<font color=#1a73e8>作者：</font>** Husanpreet Singh, Robert Tran, Ayushree Kharel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Virtual reality (VR) headsets (e.g., Meta Quest, Apple Vision Pro) provide a seamless user experience due to their fast, frictionless interaction with the physical world in a simulated environment. User authentication relies on biometric cues such as iris in such headsets. However, traditional iris recognition protocols may not be adequate in cases of unconstrained acquisition, which is typical of VR-based data. In this work, we examine three crucial aspects: (1) evaluating ISO/IEC 29794-6 iris quality metrics on VRBiom dataset and analyzing their limitations, (2) addressing data-specific challenges such as off-axis gaze, non-uniform illumination, and specular reflection using generative models, and (3) performing unimodal (iris, periocular) recognition and multimodal score-level fusion (iris + periocular). We observe that some metrics (e.g., margin adequacy) fail on VR-acquired data; whereas, image adjustments primarily benefit periocular recognition, and multimodal fusion lowers EER by ~11% over unimodal iris recognition performance. We will release the evaluation scripts upon acceptance for reproducibility.

---


### 96. [Refusal-Gated Decoding: Preserving Refusal Behavior Under High-Temperature Sampling](https://arxiv.org/abs/2607.20791)

**<font color=#1a73e8>作者：</font>** Phillip Howard, Xin Su, Allen Roush 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-temperature sampling is one of the primary mechanisms for increasing diversity in LLMs. Recent advances in truncation-based sampling techniques have helped mitigate drawbacks of high-temperature sampling such as neural text degeneration, thereby enabling greater diversity in LLM outputs without sacrificing coherence. However, increasing the entropy of the token probability distribution via high temperatures has also been shown to weaken model guardrails by reducing the model's refusal response in the presence of harmful prompts. Despite the potential benefits of high-temperature sampling and the importance of maintaining model safety, there is a lack of existing solutions for maintaining the refusal behavior of LLMs under a higher entropy regime. To address this gap, we systematically study how temperature influences refusal behavior in LLMs and propose an efficient sequential decoding approach which preserves a model's greedy decoding refusal response at high temperatures while incurring minimal additional latency. Through extensive experiments, we show that our approach preserves 91-99% of the greedy decoding refusal behavior across three benchmark datasets without compromising the model's high-temperature response for safe prompts. Our work demonstrates how refusal behavior can be maintained in an efficient manner for applications which require high-temperature sampling.

---


### 97. [Memoir: Should a Model Write to Its Memory While It Thinks?](https://arxiv.org/abs/2607.20792)

**<font color=#1a73e8>作者：</font>** Jaber Jaber, Osama Jaber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Memoir combines per-sample fast memory, shared slow parameters, variable-depth latent recurrence, and a future-latent energy objective. We test its riskiest coupling: each pondering iteration may rewrite the fast tier that the same iteration reads. On procedural associative recall with key interference, we compare a coupled arm against an otherwise identical read-only pondering arm. Both arms contain 81,738 parameters, including 76,362 trainable parameters, and use matched declared forward multiply-accumulate counts, data, optimizer, schedule, and seeds. After 240 training steps across 12 seeds, coupled recall is 0.5203 with a 95 percent interval of [0.4522, 0.5883], while read-only recall is 0.6557 with [0.5953, 0.7160]. The arms are paired per seed, and the read-only lead of 0.1354 gives a paired t of 3.23 on 11 degrees of freedom with a 95 percent interval of [0.0431, 0.2277] on the difference, winning on 10 of 12 seeds. After 960 steps across 8 seeds, both arms reach 1.0000, so the measured effect is a learning-speed penalty at a fixed budget, not a demonstrated capability penalty. That longer control is ceiling limited, leaving convergence on a non-saturating task unmeasured. A predicted failure in which memory rewriting corrupts the energy signal did not occur: the energy margin grew and held. Kernel restructuring also reduced delta-rule forward time from 0.907 ms to 0.351 ms on the stated device. Code and evidence are available at this https URL

---


### 98. [Can an AI System Be Creative? A Critical Perspective from Art and Engineering](https://arxiv.org/abs/2607.20796)

**<font color=#1a73e8>作者：</font>** Ivan Magrin-Chagnolleau  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper examines the question of whether artificial intelligence (AI) systems can be creative, approached from the dual perspective of a researcher trained in electrical engineering, pattern recognition, machine learning, and neural networks, who has also spent most of his life engaged in the arts as actor, stage and film director, writer, composer, and visual artist, and in philosophy. Drawing on Margaret Boden's foundational framework, both her three properties of creativity (novelty, surprise, and value) and her three types of creative processes (combinatorial, exploratory, and transformational), the paper argues that AI systems are structurally incapable of creativity in its strongest sense. While they exhibit genuine capability in the domain of combinatorial creativity, they are significantly bounded in exploratory creativity, and fundamentally incapable of transformational creativity. The paper further argues that the most important limitation of current AI systems is not the absence of novelty per se, but the absence of any mechanism for serendipity, accident, or the unexpected, all of which play a central role in the phenomenology of creativity, and the absence of any subject position from which to recognize and welcome such chance events. The paper concludes by proposing a model of human, AI creative collaboration that is both realistic and generative, illustrated by several concrete experiments. The paper is itself a demonstration of the thesis it advances: it was composed through a deliberate human AI collaborative process, which is described in the methodological note that opens it.

---


### 99. [External Clustering Validation by the Homogeneity-Parsimony Trade-off](https://arxiv.org/abs/2607.20799)

**<font color=#1a73e8>作者：</font>** Andreas Tiffeau-Mayer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scalar metrics are often used to evaluate clusterings against known classes, but they can obscure a fundamental trade-off: clusterings should be informative about class labels while avoiding unnecessary fragmentation. Here we describe normalized scores of cluster homogeneity and parsimony that quantify this trade-off. These scores build on the information bottleneck principle, modified to not reward lossy compression. We show by example and mathematical proof that our definitions of these scores have the intuitive property of varying monotonically under cluster refinement in contrast to related proposals. Extending the information-theoretic framework beyond Shannon entropies, we furthermore derive set-matching and pair-based counterparts of the homogeneity and parsimony scores. These unify commonly used evaluation criteria and show that, in the pair-based setting, the homogeneity-parsimony trade-off recovers the receiver operating characteristic of binary classifiers. We demonstrate the framework's utility for feature selection and algorithm comparison, illustrating how considering scores jointly can clarify clustering operating points and identify Pareto-optimal solutions.

---


### 100. [Classical Acceptance Is Not Hybrid Authentication: Measuring X.509 Verifier Semantics in Post-Quantum Migration](https://arxiv.org/abs/2607.20800)

**<font color=#1a73e8>作者：</font>** Taesung Kim, Boheung Chung, Keonwoo Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A relying party validating a hybrid X.509 certificate --- carrying both a classical and a post-quantum credential --- must distinguish whether its accepting judgment rests on the post-quantum evidence or only on the classical path. To preserve compatibility, the separable designs place that evidence where classical path validation may ignore it. A verifier can then validate the classical path and accept while the post-quantum evidence never bears on the decision --- a valid classical result silently promoted to a hybrid conclusion it did not establish. We measure this across eight path-validation stacks (seven independent codebases), in nine validation modes, over six certificate schemes. Under a hybrid-required policy, nearly every stack parsing a separable hybrid certificate accepts on the classical path without making the post-quantum evidence outcome-bearing; one enforcing mode instead fractures interoperability over a signature-input encoding not yet interoperably profiled; and stacks that verify post-quantum signatures still do not enforce the binding by default: the gap is structural, not explained by missing primitive capability alone. Under lifecycle desynchronization the downgrade is realized: when a bound post-quantum credential is revoked while the classical certificate stays valid, the default path still accepts, because the bound credential lies outside the decision's scope. Binding success is not authentication success. We contribute a specification-derived verifier model and an executable, policy-parametric reference contract --- what a verifier must recognize, verify, make outcome-bearing, and check before reporting a validation as hybrid --- with a diagnosis of why standards do not require it.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-271](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
