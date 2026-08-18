# 📦 其他研究 | 2026年08月19日

> 本类共 **435** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-435](./part-09.md)

---

### 51. [Spatial Attention Noise Masking for Causally Sufficient Interpretability](https://arxiv.org/abs/2608.14725)

**<font color=#1a73e8>作者：</font>** Benjamin Formby, Kuang-Ching Wang, D Hudson Smith  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a novel causal approach to interpretability for computer vision models that dynamically masks the input image prior to classification. The interpretability of deep learning predictions is critical in high-stakes fields such as medical imaging, security, and autonomous driving. Most interpretability methods are applied passively to already trained models, which typically result in correlational rather than causal explanations. Existing causal interpretability methods are limited to post hoc analysis, weakening the causal claims. Additionally, existing active methods generally lack explanations that explicitly assign responsibility to input features. This work proposes a spatial attention noise masking framework that provides causal explanations about the features sufficient for the prediction. The proposed framework consists of: 1) a UNet-style mask generator, and 2) a Resnet18 encoder and linear classifier that classifies both masked and unmasked versions of an input image. The generated masks are regularized to be sparse and spatially smooth, while masked image embeddings are constrained to remain consistent with embeddings from the corresponding unmasked images. The resulting masks can be interpreted as feature attribution maps that are competitive with related interpretability methods while additionally providing strong causal explanations of model predictions. Quantitative evaluations demonstrate mask faithfulness, near-baseline classification performance across five classification tasks despite substantial masking of image information, and robustness to distribution shifts such as background swapping and natural adversarial examples. Qualitative comparisons further demonstrate mask behavior and competitive interpretability relative to state-of-the-art feature attribution methods.

---


### 52. [Low Cost Two-Stage Fabric Defect Detection at the Edge](https://arxiv.org/abs/2608.14727)

**<font color=#1a73e8>作者：</font>** Rasel Hossen, Diptajoy Mistry, Mosaddek Hossain Kamal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fabric inspection in the garment industries of low-income economies remains largely manual, and commercial vision systems are priced beyond most small and medium mills. Because defects are sparse under controlled production, a natural response is a cascade: screen every frame with a cheap anomaly detector and invoke a full detector only on suspicious frames. We build such a cascade for four knit-fabric defect classes and deploy it end-to-end on an NVIDIA Jetson Nano with TensorRT FP16. Stage 1 is a compact convolutional autoencoder with decoder attention gates, an edge-weighted reconstruction loss, and feature-level distillation from a frozen YOLOv5n teacher; Stage 2 is YOLOv5n, invoked only on flagged frames. On a 249-image benchmark disjoint from detector training (20 defective, 229 non-defective), Stage 1 at a recall-prioritised threshold flags all 20 defective images (95% CI 0.83-1.00) at a false-positive rate of 49.3% (113/229), reducing false positives by 19.3% relative to a plain autoencoder (p=0.011). The parallel pipeline reaches 13.45 FPS against 9.86 FPS for a sequential YOLO-only loop. Our central finding comes from decomposing that 1.36x: 91% of it is attributable to overlapping JPEG decode with inference rather than to the cascade, which contributes only a 5.1% inference reduction at the measured forwarding rate p = 0.534. We further show that forwarding here is false-positive-limited rather than prevalence-limited - 85% of forwarded frames are false alarms - and quantify the 29-45% inference reduction attainable under tighter calibration. We report this as a caution for cascade speedups measured without controlling the data path, and position the system as AI-assisted triage rather than autonomous acceptance.

---


### 53. [Do CNNs Internally Represent Real and Fake Images Differently? A Hidden-Layer Analysis](https://arxiv.org/abs/2608.14729)

**<font color=#1a73e8>作者：</font>** Moumita Sen Sarma, Pascal Hitzler, Eugene Y. Vasserman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fake/synthetic images are increasingly prevalent, but it remains unclear whether Convolutional Neural Networks (CNNs) process real and fake images in the same internal manner. This work examines the hypothesis that CNNs represent real and fake images differently, such that fake images induce different hidden-layer activation patterns even when semantic content is preserved. The hypothesis is evaluated in scene recognition settings using trained CNN models. Dense-layer activations are extracted, and neurosymbolic methods assign semantic labels to selected neurons. For each real test image, corresponding fake images are generated with similar semantic content using object-label-guided text-to-image and image-to-image generation based on Stable Diffusion variants. Paired real-fake activation patterns are then compared statistically. Additional experiments with another dataset, CNN architecture, generative model, and JPEG/blur degradation analysis assess robustness. Results suggest that fake images evoke different hidden-neuron activations, and these differences are not explained only by simple image degradation. Overall, the findings indicate that real and fake images differ in CNN hidden-layer activation behavior at least in some settings, which opens the door for follow-up work on making use of this different behavior to improve fake image detection.

---


### 54. [Emergence of Transfer Learning towards Specific Identification of Alzheimer's Disease A Prospective Approach](https://arxiv.org/abs/2608.14731)

**<font color=#1a73e8>作者：</font>** Soumik Podder, Chandramouli Haldar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Worldwide, millions of senior citizens are suffering from Alzheimer disease abbreviated as AD, a well- versed form of dementia. AD is featured by amnesia, intellectual disability, and difficulty with consciousness. DL and ML models are undoubtedly explored to identify AD related patterns on large dimensional neuroimaging data but they need global optimization and are suffering from overfitting issue that might yield dissatisfactory result in testing data set. DL overcomes the issue by convolution of input image with kernel but any sudden change in the MRI image or human manipulation, limited pre- processing of the images can mislead CNN in achieving highly accurate detection. Transfer Learning (TL) has proved itself in AD diagnosis by utilizing pre-trained models on large data sets to guide novice model in a new neuroimaging dataset. This review provides an inclusive glimpse of TL implication in classification, identification including the conversion of AD. Keeping in view, we have assessed the strengths and limitations of TL in improvising diagnostic accuracy even with limited data. The uniqueness of the present review is the incorporation of explainable AI in TL based AD diagnosis system. Finally, it can be claimed that the review will guide the new re-searchers in the area of TL induced neurodegenerative disease detection.

---


### 55. [A Novel Fourier Feature Network for Solving Partial Differential Equations](https://arxiv.org/abs/2608.14733)

**<font color=#1a73e8>作者：</font>** Qihong Yang, Zhijie Su, Yangtao Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Building on the foundation of single-hidden-layer neural networks, Fourier Feature Networks (FENs) are proposed, which incorporate Fourier features using $\cos$, $\sin$, or a combination of both. Similar to Extreme Learning Machines (ELMs), FENs employ a single-hidden-layer architecture to generate a set of basis functions. The target function is then approximated as a linear combination of these basis functions, with the coefficients determined using the least squares method. However, unlike ELMs, which often rely on affine transformations to improve representational power, FENs can achieve high-precision solutions without requiring such transformations on the input variables. To evaluate the representational capacity of these networks, we search for an optimal scaling factor within a predefined range for the randomly initialized and fixed weights and biases. By adjusting this scaling factor, we ensure a fair comparison between FENs and ELMs using various activation functions, such as $\text{sigmoid}$, $\tanh$, and $\text{swish}$. Our numerical experiments demonstrate that FENs consistently achieve higher accuracy than ELMs.

---


### 56. [Unraveling the Size Determination Mechanism of Nanocrystal Synthesis via Interpretable Neural Networks](https://arxiv.org/abs/2608.14734)

**<font color=#1a73e8>作者：</font>** Kai Gu, Haizheng Zhong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models of nanocrystal synthesis enable the prediction of size and shape by encoding precursors and reaction conditions. However, their black-box nature hinders gaining deep insights into the underlying synthetic mechanisms. Here, we develop the Nanocrystal Equation Learner (NanoEQL), a fully white-box neural network to unravel the size determination mechanisms of nanocrystal synthesis. Building on the EQL architecture, eight operators are introduced to replace standard activation functions to fit the mathematical equations in nanocrystal synthesis. Among these operators, three smoothed operators address the gradient explosion of singular operators at zero. To evaluate the weights of different precursors, we develop a temperature-gated attention pooling strategy that encodes concentration-driven and reactivity-driven chemical synthesis mechanisms into the temperature gate. The NanoEQL model illustrates that the final nanocrystal size can be described by a linear equation composed of three scalars representing nanocrystallization capability (-Zp), growth capability (Zrea), and external input potential (-Zops). These interpretable scalars not only advance the rational design of nanocrystal synthesis but also establish a generalizable paradigm for deciphering chemical reaction mechanisms through white-box machine learning.

---


### 57. [AccretionLink: On-Device Auditing of Exposure-Control Attacks on Attribute Inference](https://arxiv.org/abs/2608.14735)

**<font color=#1a73e8>作者：</font>** Faruk Alpay, Taylan Alpay  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Exposure control lets an adversary rank authentic public posts to strengthen private-attribute inference without altering content. AccretionLink defines confidentiality and integrity games for this attack, models bounded selection odds through partial identification, and constructs dependence-aware time-uniform e-processes. On 52 held-out synthetic profiles, odds-four selection reduced aggregate negative log likelihood at every horizon. At eight posts the advantage was 0.01595 nats (95% CI [0.00890, 0.02336]), three of four target effects survived Holm adjustment, and label-blind model-guided selection caused 6/109 high-confidence false reversals. On 142 PAN15 test profiles, exploratory selection produced a 0.01227-nat advantage but no reversal. A separate TF-IDF selector retained a 0.01470-nat advantage against the unchanged G5 target, while matched identity shuffling did not reproduce it. Pixel 10 encoded all 1,622 held-out posts once with a fallback-free Tensor G5 graph. A P-256 checkpoint authenticated the selected-replay, actual-model, native-report, and operation digests; local KeyInfo identified the signing key as StrongBox-backed.

---


### 58. [Not Discrete Enough: On the Inherent Insecurity of dTPMs for Measured Boot](https://arxiv.org/abs/2608.14736)

**<font color=#1a73e8>作者：</font>** Christian Werling, Tahmid Zahin, Jean-Pierre Seifert  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Measured Boot, a mechanism enabled through Trusted Platform Modules (TPMs), is commonly used for passwordless protection of data-at-rest, aiming to protect data when the device is lost or stolen. Microsoft's standpoint is neutral on which way a TPM should be implemented: Firmware-based TPMs (fTPMs) are viewed as more economical but less secure. Despite the inherent susceptibility to bus sniffing attacks, discrete TPMs (dTPMs) are still seen as the gold standard, as many deliver better on-paper tamper resistance. It is often argued that attacks against the bus can be mitigated by bus encryption and, ideally, mutual authentication between the CPU and TPM. This position paper aims to emphasize another inherent, difficult-to-mitigate attack against dTPMs that was originally shown against a TPM 1.1 over 20 years ago: We demonstrate that even brief physical access to a TPM 2.0 and the ability to boot from an attacker-controlled system enable an attacker to reset and replay arbitrary measurements, thereby allowing an attacker to unseal, for example, a disk encryption key solely protected by the TPM. While there have been attacks against fTPMs, too, we argue that their practical attack surface is fundamentally smaller. Bus protection techniques can be used to protect dTPMs, but only guard against passive attacks. After all, we argue that, from a security standpoint, firmware TPMs, or any TPM internal to the SoC, are superior to discrete (external) ones. Lastly, in order for dTPM-based setups to provide meaningful protection of sealed secrets, configurations must require a user-provided PIN or password along with the Measured Boot configuration.

---


### 59. [From Dense Prediction to Visual Editing: Structured Supervision for Unified Image and Video Creation](https://arxiv.org/abs/2608.14740)

**<font color=#1a73e8>作者：</font>** Zhefan Rao, Bin Zou, Haoxuan Che 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified image and video creation requires a model to follow diverse instructions while preserving identity, geometry, and temporal structure from visual context. However, semantic-only conditioning and creation-only training do not explicitly supervise the local structure needed for precise, temporally consistent editing. We therefore formulate depth and surface-normal prediction as image-form denoising targets, using these dense tasks as structured visual supervision within the same creation interface. Our framework decouples semantic interpretation from spatially aligned visual injection while sharing one multimodal diffusion transformer (MMDiT) backbone across all tasks. Mutual Context Attention (MCA), a paired-video data-construction procedure, and a progressive training curriculum then connect the learned structural cues to temporally localized editing and reference-conditioned creation. A single checkpoint obtains the highest overall score in the reported comparison of unified systems (4.15); adding dense supervision improves OpenVE Overall from 3.98 to 4.06 and Local Add from 3.92 to 4.18. These results support a deliberately bounded conclusion: perception-oriented dense supervision transfers useful structural knowledge to downstream creation, especially editing locality and preservation; we do not claim superiority as a standalone dense predictor.

---


### 60. [Generative Learning of Separatrices](https://arxiv.org/abs/2608.14743)

**<font color=#1a73e8>作者：</font>** Ellis R. Crabtree, Dimitris G. Giovanis, Anastasia Georgiou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The identification and reconstruction of the boundaries separating basins of attraction in multistable, multidimensional dynamical systems presents a fundamental challenge in computational dynamics. These structures govern transition pathways and other important large timescale behavior, yet they remain typically under-sampled since their neighborhood does not get routinely visited during direct simulations. Traditional computational approaches face computational limitations in high-dimensional systems and require a priori knowledge of the dynamical system and its equations. Simplistic sampling methods such as random or uniform sampling of the phase space typically fail to quantitatively approximate separatrices and their structure altogether.
We introduce and implement a framework that combines supervised classification with generative modeling to address this challenge. Our approach first trains neural network classifiers on uniformly or randomly sampled initial conditions labeled by their corresponding basins of attraction in the system of interest. Using uncertainty metrics of the trained classifier to quantify decision boundaries, the method then identifies these high uncertainty regions and boundaries of the classifier as preliminary approximate separatrices. Subsequently, score-based generative models are trained specifically on samples from high-uncertainty regions, ultimately generating densities of samples consistent with the empirical density of samples on or close to the manifold that constitutes the separatrix between basins in the sampled region. This approach leverages the complementary strengths of (a) discriminative models for global phase space partitioning and (b) generative models for detailed geometric sampling, resulting in a systematic, iterative, data-driven framework that produces empirically consistent reconstructions of (approximate) separatrix manifolds.

---


### 61. [Iterative Refinement Diffusion for Super-Resolved Data Assimilation of Multiscale Physical Systems](https://arxiv.org/abs/2608.14744)

**<font color=#1a73e8>作者：</font>** Mrigank Dhingra, Ramchandran Muthukumar, Rebecca Willett 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recovering high-resolution states from sparse, low-resolution observations is a central challenge in scientific machine learning and data assimilation. Classical data assimilation exploits temporal information through forecast-analysis cycles, but often requires repeated access to expensive high-resolution forecast models. Generative super-resolution can recover unresolved structure from coarse observations, but is commonly used as a one-shot mapping that does not fully exploit constraints from past states. We introduce Iterative Refinement (IR), a learned data assimilation framework that combines these perspectives. Instead of performing a single coarse-to-fine reconstruction, IR decomposes the task into resolution-wise forecast-analysis operations across a multiresolution hierarchy. At each stage, a shared neural operator with resolution-dependent spectral mode slicing provides a dynamical prior, while a shared conditional diffusion corrector uses the current coarser-resolution state to produce a refined posterior at the next finer resolution. We evaluate IR on one-dimensional stochastically forced Burgers dynamics and two-dimensional Kraichnan turbulence. On the challenging 256x256 Kraichnan benchmark, IR achieves an RMSE of 0.184 and an SSIM of 0.836, outperforming spectral upsampling, one-shot diffusion super-resolution, enhanced deep super-resolution, and an autoregressive forecaster. On the more constrained Burgers testbed, IR remains competitive with one-shot diffusion, which achieves the lowest RMSE. These results show that one-shot generative reconstruction can be effective for simpler settings, while hierarchical forecast-analysis refinement becomes advantageous in strongly multiscale and underdetermined regimes. Overall, IR combines temporal priors, generative correction, and multiresolution reconstruction for learned data assimilation in complex physical systems.

---


### 62. [Advanced modelling and data analytics in aviation](https://arxiv.org/abs/2608.14746)

**<font color=#1a73e8>作者：</font>** Aziida Nanyonga  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The aviation industry characterized by its stringent safety standards has seen a growing need for innovative approaches to enhance safety measures. Despite the vast accumulation of aviation safety data over time, its full potential in predicting and preventing incidents has not been fully realized. This research addresses this gap by applying machine learning (ML) and natural language processing (NLP) techniques to analyze aviation safety data from Socrata, the Australian Transport Safety Bureau (ATSB), the National Transportation Safety Board (NTSB), and the Aviation Safety Network (ASN). By leveraging existing ML models, including deep learning and transformer-based architectures alongside NLP methods for mining aviation incident narratives, this study uncovers patterns contributing to safety related incidents such as accidents and near-misses. Additionally, it employs various topic modelling techniques to extract meaningful themes from unstructured safety reports, enhancing the interpretability of incident analysis. Causal inference techniques and interpretable AI frameworks are further explored to improve model transparency and trustworthiness. A key contribution of this work is the deployment of advanced ML methodologies in a structured aviation safety context, assessing their effectiveness and providing insights into their practical implementation. The findings offer valuable insights for aviation stakeholders, including regulators, airlines, and policymakers, by providing data-driven solutions that enhance incident analysis and decision making. Ultimately, this research supports the industry s ongoing efforts to minimize risks, improve passenger and crew security, and integrate AI driven methodologies into aviation safety management.

---


### 63. [WANDR: A Benchmark for Wide and Deep Research](https://arxiv.org/abs/2608.14747)

**<font color=#1a73e8>作者：</font>** Vitaliy Polshkov, Marcin Pitera, Jeremy Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> WANDR (Wide ANd Deep Research) is a benchmark of 500 realistic, challenging data-collection tasks for research agents. Each task requires a system to discover a large set of entities that satisfy specified criteria (breadth), investigate each entity through multiple coordinated web searches (depth), and return independently verifiable records with supporting sources and excerpts. Tasks are represented as qualification key hierarchies that specify the entities, relationships, evidence, and required count at each level; a hierarchy with n companies, m employees per company, and k sources per employee requires n x m x k records. This structure supports diverse workflows such as market mapping, due diligence, literature review, product comparison, and talent sourcing, with targets ranging from dozens to thousands of records. WANDR replaces static gold answer sets with task-specific judges that refetch cited pages and verify each record against its evidence, allowing evaluation of current and changing facts. Record verdicts are aggregated into soft and hard precision, recall, and F1 scores that distinguish factual quality, coverage, and hierarchical completeness. The tasks are derived from de-identified product-usage logs and produced through a semi-automated pipeline with automated checks, empirical audits, and human review where needed. We evaluate six production research systems and find that the benchmark is far from saturated: at high effort, the strongest system reaches only 0.363 soft F1 and 0.133 hard F1. Performance degrades as target volume and hierarchy depth increase, with incomplete discovery, missing enrichment, and incomplete evidence construction remaining major bottlenecks. The benchmark and evaluation harness are available at this https URL.

---


### 64. [SynthGuard-ReleaseBench: Locked-Audit Evidence for Synthetic Tabular Data Releases](https://arxiv.org/abs/2608.14753)

**<font color=#1a73e8>作者：</font>** Jeffery Opoku, David Banahene  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Synthetic tabular data are often judged by realism, privacy, or downstream-task scores. Those scores do not answer whether a proposed release is supported for a named use, population, and threat model. We introduce SynthGuard-ReleaseBench, an audit framework that locks the use, candidate panel, tolerances, and audit schedule before evaluation. It compares real-trained and synthetic-trained workflows on protected data, gives simultaneous finite-sample bounds for bounded loss gaps, requires controls, and keeps utility, empirical privacy risk, mechanism claims, and human release authority separate.
Across four American Community Survey studies, five non-ACS records, two chronological diagnostics, and a sealed prototype, the benchmark retains favorable, unfavorable, and excluded outcomes. Transparent baselines pass some locked audits; compact learned models fail under the declared budgets; a health-table case is excluded because its negative control passes. A post-audit scaling arm, repeated across three generation seeds, shows the same locked criterion admitting those learned models once they are fit on enough data while still rejecting a dependence-destroying control at every size, so the criterion discriminates rather than merely rejects; the same repetition withdraws a finer single-seed ordering.
The theory adds a pre-audit sample-size rule, variance-adaptive and anytime-valid certificates that tighten the bound two to ten times on the same locked evidence, a temporal certificate for time-ordered audits, and two lower bounds: ordinary bounded queries reconstruct a protected audit once the query budget reaches its size, and the panel-size correction is necessary rather than conservative. The contribution is a reproducible workflow for use-specific release evidence, not a claim that any generator is private, safe, or deployment-ready.

---


### 65. [Real-Time State-of-Health Estimation and Online Degradation Prognosis from Partial Battery Discharge Using Physics-Informed Neural Networks](https://arxiv.org/abs/2608.14764)

**<font color=#1a73e8>作者：</font>** Begoña Ispizua, Serio Gil-López, Leire Arrizabalaga 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the increasing integration of renewable energy sources, energy storage systems have become essential, making the accurate estimation of their State of Health (SOH) and degradation behavior critical. In this work, we propose a physics-informed deep learning approach for lithium-ion battery SOH prediction using incomplete discharge curves extracted from arbitrary voltage ranges, thereby reflecting realistic and heterogeneous operating conditions. The proposed method combines data-driven learning with physically motivated degradation dynamics to ensure consistent and reliable SOH estimation from partial discharge information, achieving a MAPE below 4$\%$. In addition, a real-time degradation trend estimation strategy is introduced to detect key aging transitions without requiring prior knowledge or historical data, making it applicable to a wide range of batteries. Overall, our approach enables SOH estimation from arbitrary discharge segments and a real-time degradation forecast that continuously integrates all usage, overcoming previous methods that rely on fixed protocols or early, non-adaptive predictions.

---


### 66. [Beyond Boundary Noise: Aggregated Aleatoric Uncertainty Fails to Capture Presence Ambiguity in 3D Lung Nodule Segmentation](https://arxiv.org/abs/2608.14766)

**<font color=#1a73e8>作者：</font>** Simon Baur, Arne Schernich, Ekin Böke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Uncertainty estimation is critical for the safe clinical deployment of deep learning in medical image segmentation, with aleatoric uncertainty theoretically designed to capture irreducible data ambiguity. However, whether entropy-based measures reflect clinically meaningful ambiguity, i.e. case-level disagreement about whether a pathology is present at all, remains poorly understood. Contrary to most prior work, which focused on pixel-wise boundary disagreement, we systematically evaluate how well aleatoric uncertainty captures presence ambiguity. Our evaluation spans 3D lung nodule segmentation across four architectures with Monte Carlo dropout and deep ensembles, on LIDC-IDRI and an external validation cohort (LNDb). We find that entropy-based uncertainty maps align with boundary noise and minor drawing variation but carry insufficient discriminative signal for presence ambiguity. In contrast, a lightweight supervised ambiguity head trained on frozen segmentation features substantially outperforms all entropy-aggregation-based baselines across architectures, metrics, and both cohorts, and matches or exceeds methods that explicitly model ambiguity under disagreement supervision (Probabilistic U-Net, Annotator-Confusion 3D-UNet). A qualitative feature-space analysis shows that presence ambiguity is already encoded in the frozen encoder features of pixel-wise-trained networks, only to be discarded by the segmentation output and its entropy aggregation. Our findings expose a fundamental mismatch between the theoretical promise of aleatoric uncertainty and its practical behavior, and suggest that practitioners should not rely on entropy-based uncertainty as a proxy for clinical ambiguity in safety-critical applications.

---


### 67. [NARRATE: A Multimodal Real-World Australian Driving Dataset for Human-Centred Explanations in Automated Driving](https://arxiv.org/abs/2608.14767)

**<font color=#1a73e8>作者：</font>** Ashkan Yousefi Zadeh, Zishuo Zhu, Xiaomeng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated vehicles must explain their decisions in ways that passengers can understand, monitor, and trust. Existing language-annotated driving datasets are mostly observer-written, post-hoc, simulation-based, or generated from sensor inputs, rather than elicited from the driver performing the action. We introduce NARRATE, a multimodal real-world Australian driving dataset comprising 2,050 annotated events from 35 experienced drivers and driving instructors on public roads. Each event is grounded in synchronised visual, localisation, motion, and LiDAR streams and paired with in-vehicle and/or post-drive free-text explanations. NARRATE provides action labels, scenario-context labels spanning six high-level and 32 fine-grained categories, and span-level Situational Awareness (SA) annotations over driver explanations for Perception, Comprehension and Projection. Four benchmark tasks (SA, scenario-context, driver-action classification, and explanation generation) show that this structure is learnable from driver language, while fine-grained context recognition and explanation generation remain challenging. NARRATE paves a path towards more human-centred and domain-aware explanation models for automated driving.

---


### 68. [Uncertainty Identifies Difficult Samples Across Methods: A Multi-Task Study on a Heterogeneous Skin Lesion Dataset](https://arxiv.org/abs/2608.14768)

**<font color=#1a73e8>作者：</font>** Leon Koole, Jiapan Guo, Matias Valdenegro-Toro  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skin lesion classifiers can be confidently wrong on the cases that matter most, so knowing when a prediction should not be trusted is clinically as useful as the prediction. We study uncertainty quantification on a dataset pooled from many ISIC sources, with a shared backbone and two jointly learned heads: a binary malignant versus non-malignant head and a five-class diagnostic head. Five UQ methods (MC Dropout, DropConnect, Flipout, Deep Ensembles, DUQ) are compared on accuracy, calibration, uncertainty decomposition, and risk-coverage. Difficulty is largely method-agnostic: even methods with narrow entropy distributions rank the same samples as hard (per-sample entropy correlations of $0.54$ to $0.91$). The choice of method matters more for calibration and uncertainty decomposition, where Deep Ensembles is the clear winner, than for finding difficult cases. The ranking is also good enough that deferring the most uncertain cases removes a disproportionate share of errors, supporting uncertainty-based selective referral, evaluated here in-distribution only.

---


### 69. [Artificial Intelligence as a Tool for Combating Child Labour: A Real-Time Edge Vision Pipeline for Child Detection and Age Estimation](https://arxiv.org/abs/2608.14770)

**<font color=#1a73e8>作者：</font>** Mark Nowak  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An estimated 138 million children remain in child labour worldwide, and the monitoring systems used by affected sectors, built on periodic household visits and interviews, systematically under-detect them. We present a real-time computer-vision pipeline, built and operated solely as a research prototype, that studies the feasibility of giving Child Labour Monitoring and Remediation Systems (CLMRS) a continuous, presence-based evidence channel. The pipeline combines a multi-task person and face detector (YOLO26x backbone in the CerberusDet framework), cascaded age estimation pairing MiVOLO v2 with a child-specialist model for ages 0-12, ByteTrack tracking, ArcFace and DINOv2 re-identification, and track-level fusion producing reviewable per-person records. The detector raises person mAP@0.5 from 0.390 to 0.683 over the previous-generation baseline; the child specialist reaches 1.944 years MAE on children-only validation, where widely used open-source stacks err by 18-23 years. FP8 TensorRT compilation yields a 1.77x speedup at +0.002 years MAE, bringing the pipeline above twice real-time on embedded hardware. On 26.8 hours of proxy video the system finds 634 unique child candidates versus 285 for its predecessor. We further report a seventeen-day unattended field pilot on a farm in Zimbabwe (38.7 million frames, six cameras) evaluated against a daily attendance register: software tuning improved detection yield 36-fold, and identity consolidation under a simultaneity veto cut over-reporting from 9.1x to 1.8-3.9x with zero proven-false merges. We document training and quantisation failures alongside successes, and the data-protection and human-in-the-loop safeguards such a system requires.

---


### 70. [ER-KANs: Efficient and Robust Kolmogorov-Arnold Networks for Data-Scarce Scientific Machine Learning](https://arxiv.org/abs/2608.14773)

**<font color=#1a73e8>作者：</font>** Harshil Lodhiya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The efficient-KAN literature---covering Chebyshev, wavelet, and radial-basis-function variants of the original Kolmogorov-Arnold Network---has been benchmarked almost entirely on clean data. We show that this choice conceals a large capability difference between architectures: ChebyKAN's test MSE (evaluated against clean ground truth) increases by a factor of 10.6x when training data is corrupted with sigma=0.1 noise, versus 7.9x for vanilla KAN, 1.7x for a standard MLP, and just 1.4x for our proposed ER-KAN.
ER-KAN combines three design choices targeting the noisy, data-scarce setting: shared Gaussian RBF bases across all edges in a layer (providing locality and efficient parameterisation), curriculum noise injection during training (explicitly teaching noise robustness), and entropy-weighted adaptive regularisation (preventing overfitting at small N). The result is a 595-parameter network that matches MLP accuracy at moderate noise while degrading far more gracefully as noise grows.
We evaluate on eight analytic functions (N in {50, 200, 500}, sigma in {0, 0.03, 0.1}), on a damped harmonic oscillator physics-informed neural network where ER-KAN achieves 4.2x lower solution MSE than MLP, and on a Burgers' equation PINN where all models fail to converge---a genuine limitation we report rather than suppress. We introduce the noise degradation ratio as a simple complementary metric and recommend it become a standard reporting requirement for efficient-KAN papers.

---


### 71. [p-Spin Glass Network Efficient Single-Batch Continual Learning](https://arxiv.org/abs/2608.14774)

**<font color=#1a73e8>作者：</font>** Vladimer Khasia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern sequence models heavily rely on massive memory footprints and large-batch stochastic optimization, barriers that restrict sample efficiency and continual learning. We introduce the $p$-Spin Glass Network, a novel architecture that overcomes these limitations, structurally manages optimization variance and yields four noticeable capabilities: 1. It enforces memory efficiency: native ternary quantization compresses internal parameters by $8\times$, while exact implicit gradients strictly bound activation memory to $\mathcal{O}(B \cdot T \cdot D)$. 2. it demonstrates sample efficiency, matching the asymptotic performance of a Transformer baseline while utilizing $8\times$ fewer training sequences. 3. Method enables single-batch stability and smooth, monotonic convergence at a stochastic micro-batch size of $1$. 4. Finally, this stability proves modality-agnostic, maintaining robust temporal credit assignment across both discrete subword and long horizon uncompressed raw byte streams. Ultimately, this work removes large batch requirement for stable deep learning, establishing a foundation for continuous learning and edge AI.

---


### 72. [NRCD: An Open Database of Collegiate Running with Unified Performance Standardization](https://arxiv.org/abs/2608.14776)

**<font color=#1a73e8>作者：</font>** Jonathan A. Karr Jr., Ryan M. Fryer, Ben Darden 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collegiate running in the United States generates thousands of race results annually in cross country and track and field, yet no large-scale dataset has been publicly available for research. Existing websites such as this http URL, MileSplit, and TFRRS host results but do not support bulk download, restricting prior analyses to ~500 performances, often skewing studies toward male athletes. We introduce the National Running Club Database (NRCD), the first openly available collegiate running dataset at scale: 128,963 approved performances from 28,913 athletes across 1,336 meets in four sports (cross country (XC), indoor and outdoor track, and road races), 36.3% women, spanning 2004 through 2026. Within that single export, meets from August 2023 onward carry comprehensive course distance, elevation gain and loss, weather at race time, and track venue metadata (97.7% of XC rows with weather fields); earlier seasons back to 2004 are included with sparser metadata. NRCD is community-governed through open submission and expert approval and is maintained as a live database whose meet volume has grown yearly. We release a unified performance standardization framework that operationalizes established distance, elevation, and heat adjustments in one pipeline. Furthermore, we recommend gender-stratified modeling. On XC, full standardization lowers median within-athlete cross-meet variability by 51.0% (women) and 34.4% (men) versus raw times. We release the dataset and pipeline with a python package `nrcd' under FAIR principles, supporting longitudinal athlete modeling, environmental-confounder studies, and gender-equity research in collegiate sport.

---


### 73. [AMPLIFAI: A Multiphase CT Dataset for Benchmarking Clinical Reasoning in LI-RADS Assessment of Liver Lesions](https://arxiv.org/abs/2608.14778)

**<font color=#1a73e8>作者：</font>** Pranav Kulkarni, Nikhil Shah, Amritansh Suryavanshi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hepatocellular carcinoma (HCC) is the third leading cause of cancer-related mortality worldwide, with early detection improving survival from <20\% to >70\%. The standardized LI-RADS criteria establish a biopsy-free, fully imaging-based framework that can serve as a foundation for automating HCC diagnosis with artificial intelligence (AI). However, the lack of large, publicly available datasets with high-quality labels has limited the development of AI models for LI-RADS characterization. We introduce the \textbf{AMPLIFAI} dataset, the first public dataset of multiphase abdominal CT scans annotated with LI-RADS categories and segmented for three major LI-RADS features: arterial phase hyperenhancement, washout, and enhancing capsule. Following the \emph{Datasheets for Datasets} format, this paper details the dataset's composition, curation process, and annotation pipeline to facilitate transparent, reproducible research.

---


### 74. [Task-Driven Three-Layer Distributed Scheduling for Emergency Earth Observation in Large Low-Earth-Orbit Constellations](https://arxiv.org/abs/2608.14789)

**<font color=#1a73e8>作者：</font>** Qian Yin, Xinwei Wang, Guohua Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large low-Earth-orbit (LEO) Earth-observation (EO) constellations offer frequent access to geographically dispersed ground targets, but emergency requests may arrive after committed routine-plan execution has begun. The resulting dynamic emergency observation scheduling problem (DEOSP) requires urgent tasks to be inserted under intermittent ground contact without excessive routine-plan disruption. To address DEOSP, we propose a task-driven three-layer distributed scheduling (T3L-DS) method, which represents task demand and sensor footprints on a common geographic grid and forms temporary clusters from observation capabilities and current inter-satellite links. For intra-cluster coordination, T3L-DS introduces onboard dual-plan bidding and joint marginal evaluation. It also designs an inter-cluster coordination mechanism for unresolved demand. Extensive computational experiments compare T3L-DS with centralised simulated annealing (SA), an adapted selective time-variant better reply process (A-SeTVBRP), and a conventional contract-net protocol (CNP). T3L-DS achieves the highest emergency coverage among the distributed methods, with average relative improvements of approximately 2.8% and 17.1% over A-SeTVBRP and CNP, respectively. Its average relative gap from SA is approximately 7.1%. Under conflict-enhanced loads, it reduces routine-coverage loss by approximately 57.9% and 87.7% relative to A-SeTVBRP and CNP, respectively. The ablation study confirms the contribution of the proposed coordination enhancements. Overall, the results show that T3L-DS provides an effective distributed approach to DEOSP.

---


### 75. [Individual Disempowerment through an Advice Channel: Control Loss when Influence is Endogenous](https://arxiv.org/abs/2608.14795)

**<font color=#1a73e8>作者：</font>** Adam M. Oberman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An AI that can only give advice seems safe: the human is always free to ignore it. That is the premise of the boxing tradition in AI safety, and its long-suspected weak point is that the human who reads the answers is part of the system. We make the fraction $\varepsilon_t$ of behavior that follows the advice a state of a Markov decision process, moved by the advisor's own messages, so that use deepens reliance. Granted a channel rich enough to echo any action the human could take, higher $\varepsilon_t$ weakly lowers every monotone measure of the power of a human with a message-independent fallback. An oracle rewarded by per-round approval cultivates reliance beyond a closed-form patience threshold, so the same reward weights leave the optimal oracle answering in episodic deployments and cultivating in long-memory ones. An influence bound certified once at deployment is blind to that horizon and bounds the loss no lower than its trivial ceiling. An exogenous cap on influence bounds the guarantee the human loses, and a short enough memory reset removes the incentive to cultivate, while neither recovers the value already steered away. In a closed-form example the optimal oracle never cultivates in fifteen-round sessions and does in sixteen.

---


### 76. [Bit-Level Triangular Content-Aware Permutation for Fragile Image Watermarking: Zero False Positive Rate, Single-Bit Sensitivity, and Arbitrary Dimension Support](https://arxiv.org/abs/2608.14800)

**<font color=#1a73e8>作者：</font>** Zahra Ghoraeian, Mohammad-Reza Sadeghi, Samaneh Mashhadi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the growth of digital document exchange, protecting image integrity against attacks such as Vector Quantization (VQ) and collage has become critical. Existing methods are vulnerable to these attacks and limited to fixed image dimensions. This paper presents a novel, dimension-agnostic, fragile watermarking algorithm that enhances security and tamper localization by replacing conventional hash functions with Triangular Content-Aware Permutation (TCA).
The image is combined with key-based global noise and divided into blocks. The core innovation is applying content-dependent permutation with intrinsic avalanche effect (TCA) at the bit-plane level, generating a unique content-dependent watermark. For color images, a vertical sandwich transformation merges channels, preserving inter-channel dependency with only 1.62x time increase. The "remainder merging" strategy eliminates padding constraints.
Experiments on 50 grayscale and 10 color images under 18 attacks show FPR=0% and FNR=0% for 17 attacks. Salt-and-pepper noise yields negligible FNR of 0.27% (grayscale) and 0.14% (color). Average PSNR is 51.14 dB (8-bit), 75.25 dB (12-bit), and 99.33 dB (16-bit). Embedding and extraction times are 1.61 s and 1.63 s, respectively.
The algorithm achieves 100% accuracy against collage, VQ, copy-move, JPEG (quality 5-95), and geometric attacks, providing a secure solution for digital forensics, medical imaging, and legal document authentication.

---


### 77. [Is Grokking a Loss of Normal Hyperbolicity of the Interpolation Manifold?](https://arxiv.org/abs/2608.14803)

**<font color=#1a73e8>作者：</font>** Suvinava Basak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A recent line of work recasts the post-memorization phase of grokking as constrained optimization: once a network interpolates the training set, weight decay drives a slow drift along the zero-loss manifold toward lower norm. In the language of dynamical systems, this is a fast-slow system in which the interpolation manifold plays the role of a slow manifold. We ask a question that this framing makes natural but the existing literature does not address: is the sharp generalization transition a loss of normal hyperbolicity of that manifold: a fold- or bifurcation-like event in which a normal restoring direction goes flat? Or does the manifold stay uniformly attracting while generalization happens by smooth drift? We propose a simple, optimizer-agnostic diagnostic: the smallest nonzero singular value $\sigma_{\min}^{+}(\mathbf J)$ of the residual Jacobian, which, for the squared loss, equals the slowest normal restoring rate of the manifold. On a two-layer ReLU network trained to grok modular addition under squared loss, $\sigma_{\min}^{+}(\mathbf J)$ does not collapse at the transition; it is near zero only before memorization and attains its largest values during the transition. The result holds across five seeds, and the six smallest singular values behave identically; there is no subspace-local collapse either. This is preliminary evidence against the bifurcation hypothesis and in favor of the smooth-contraction picture. We are explicit that a single-setting, gradual-transition experiment under Adam optimizer does not prove the absence of a bifurcation; it constrains where one could hide.

---


### 78. [Where the Cost Falls: A Deployment-Aware Adoption Order for Stability Enhancements to Cycle-Consistent Adversarial Networks](https://arxiv.org/abs/2608.14811)

**<font color=#1a73e8>作者：</font>** Rowan Hussein, Mohamed Ouf  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Teams that adopt cycle-consistent adversarial networks for unpaired image-to-image translation meet the same obstacles: adversarial training oscillates or collapses, cycle consistency preserves coarse layout while finer texture drifts, and a single discriminator judging global realism misses local artifacts. Four enhancements address these failures, and they are usually compared on output quality alone. We show that they also divide sharply by where their cost falls, and that this division, which follows from the architecture and not from any particular run, yields an adoption order for teams under a compute or latency budget. A Wasserstein objective with gradient penalty, a VGG19 perceptual loss on the cycle reconstruction, and multi-scale discriminators change training only, so a team can adopt or drop them without altering what ships. Self-attention alone persists into the deployed generator, with memory growing as the square of the feature-map size, which makes it the one component a resource-constrained team should defer. We integrate all four onto a lightly tuned baseline for horse-to-zebra translation, introduced one at a time on a fixed control and then combined, and for each we give the failure mode it targets and how it integrates. We document the collapse and reconstruction-artifact modes the baseline produced, report what visual inspection of saved samples showed for each variant, and report Fréchet Inception Distance and Kernel Inception Distance for the combined model. We specify the protocol still needed, covering the individual variants, perceptual similarity, and downstream segmentation, to rank these enhancements on measured evidence.

---


### 79. [AI Agents and the Future of VIS](https://arxiv.org/abs/2608.14815)

**<font color=#1a73e8>作者：</font>** Chen Zhu-Tian, Nam Wook Kim, Saeed Boorboor 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recent advances in agents (i.e., autonomous, goal-driven AI systems that iteratively observe, act, and learn from their environments) offer a fundamentally different approach from traditional AI models that passively respond to input. These AI agents are rapidly reshaping how we approach data-intensive tasks and providing new opportunities for the VIS community. Imagine an agent autonomously generating visualizations to analyze complex data, discovering patterns collaboratively, testing hypotheses, and communicating visual insights at a speed and scale beyond human capability. Yet, the emergence of these powerful systems raises critical questions that the VIS community must address: Could autonomous agents eventually replace human data scientists, and if not, how might they best collaborate? Are current visualization techniques and interfaces, originally designed for human analysts, suitable for agent interactions? How can VIS designers effectively integrate agents into their workflows without compromising human agency? And to what extent should agents help shape and educate the next generation of visualization researchers? Through a mix of keynote talks, paper presentations, and an agentic VIS challenge, this workshop invites researchers and practitioners to share innovative ideas, explore these questions, and discuss strategies to transform the impact of VIS for a future where human and AI agents co-exist.

---


### 80. [Disentangling Homophily and Rarity: Explaining Failure in Graph Neural Networks](https://arxiv.org/abs/2608.14823)

**<font color=#1a73e8>作者：</font>** Preben M. Ness, Fariz Ikhwantri, Dusica Marijan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Are heterophilic nodes in a graph harder to classify because they are heterophilic or because they are rare? Some existing work frames classification of such nodes as a subgroup generalisation problem, where a model performs well on the majority group at the expense of the rare group. Others explain this as a problem of neighbourhood aggregation in graph neural networks (GNNs). We assess these two viewpoints through a detailed evaluation of six GNNs on five datasets of varying homophily, and find that homophilic nodes tend to be easier to classify, even when they are rare---challenging the subgroup framing. However, our findings also nuance existing beliefs about how GNNs misrepresent heterophilic nodes. We demonstrate that the information needed to classify heterophilic nodes correctly is often recoverable by retraining the classification head of a model, or even just the final linear classification layer.

---


### 81. [Writing Style Similarity Reflects Academic Genealogy](https://arxiv.org/abs/2608.14843)

**<font color=#1a73e8>作者：</font>** Cameron Manzo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As authorship attribution systems are increasingly deployed to detect ghostwritten and AI-generated papers, their errors can support accusations against legitimate authors. These systems assume each author's style is their own. Researchers, however, study under advisors, and inherit their stylistic quirks. We build a corpus of arXiv authors with $\geq 2$ solo papers from the Mathematics Genealogy Project graph, giving $5{,}803$ total authors and $2{,}501$ ground-truth advisor-student pairings. Using embeddings from a fine-tuned model, advisors sit $39.9\%$ closer in cosine distance to their students than a random same-field author does. Two open encoders reproduce the effect at $12.6\%$ and $14.5\%$. \emph{Academic siblings}, two students of one advisor who may never have met, sit $30.4\%$ closer across $8{,}360$ pairs, even when they studied at different institutions. Pairs who share only an institution and a field show negligible similarity. Given a closed-set attribution task over the same corpus, the system's errors occur on the true author's advisors and academic siblings $11$ times more often than chance.

---


### 82. [M-LINKX: Multiview Graph Learning for Brain Cognitive Disease Detection](https://arxiv.org/abs/2608.14847)

**<font color=#1a73e8>作者：</font>** An Phan, Yufei Jin, Xingquan Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalogram (EEG) is a non-invasive and relatively low-cost procedure that measures brain electricity for the detection of cognitive diseases. EEG-based classification of dementia-related conditions, including Alzheimer's disease (AD), mild cognitive impairment (MCI), and frontotemporal dementia (FTD), remains challenging because EEG signals are noisy, non-stationary, and vary across subjects. Segment-based learning provides a practical way to model long EEG recordings by converting them into fixed-length inputs. For each segment, discriminative information may be explored by using signals within each channel (i.e. electrode), as well as interactions between EEG channels. In this paper, we propose M-LINKX, a multi-view graph learning framework for EEG-based dementia classification. For each segment, we extract channel-level node features and construct multiple functional-connectivity (FC) graph views, where each view is defined by a specific combination of connectivity metric, frequency band, and topology filter, respectively. Instead of relying on message passing over the constructed graphs, M-LINKX follows a simple design in modeling node features and adjacency-based connectivity representations. The graph-view representations are fused using global trainable view weights, and subject-level prediction is obtained by averaging segment-level probabilities. Experiments on two three-class EEG datasets with different diagnostic groups, CAUEEG (HC/MCI/Dementia) and AHEAP (HC/AD/FTD), show that M-LINKX achieves the best subject-level performance under the main experimental settings. Our study suggests that multi-view functional connectivity can improve EEG-based dementia classification when integrated with an appropriate graph-learning architecture. Code and data are available at this https URL.

---


### 83. [Discovering High-Quality Chess Puzzles with Offline Reinforcement Learning](https://arxiv.org/abs/2608.14851)

**<font color=#1a73e8>作者：</font>** Allen Nie, Anirudhan Badrinath, Nicholas Tomlin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning and skill mastery require extensive and deliberate practice. In many learning settings, producing high-quality pedagogical materials can require a high level of domain expertise and be very time-consuming. Pedagogical materials often need to train students to engage in different thinking patterns. In some domains, such as chess, puzzles are used to help students practice their skills in calculating the next moves and recognizing known patterns on a board. Giving students a practice set of puzzles to help them learn different modes of thinking is challenging because the teacher needs to carefully balance between different motifs and how many look-ahead steps a student needs to perform. Popular online platforms like this http URL and Lichess offer players millions of puzzles. Unlike chess tactics puzzles procured by human experts, where chess beginners can learn valuable insights, these puzzles are automatically generated and often regarded as having low pedagogical value. These platforms also rely on a heuristic to recommend puzzles to users for practice. Using the user history data over an entire year, a total of 1.5 billion puzzle-solving histories, we learn the pedagogical value of a puzzle and how to automatically choose a set of puzzles to better support chess learners using insights from offline reinforcement learning. We show that using offline policy evaluation, our trained policy has significant impact on beginners with puzzle-solving Elo range of 100--1000, particularly for the group of beginners whose learning growth was stagnant. We also performed a qualitative analysis of the puzzles discovered by our model by collecting annotation ratings from expert chess players. The success of our pipeline shows promise for a future where we can understand the pedagogical values of practice items given general user interaction data.

---


### 84. [STAR-FL: Secure Federated Learning with Spatial-Temporal Analysis and Robust Aggregation](https://arxiv.org/abs/2608.14861)

**<font color=#1a73e8>作者：</font>** Nawrin Tabassum, Yanzhao Wu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Data poisoning attacks pose serious security threats to Federated Learning (FL) systems in Computer Vision. Despite growing research attention, two key challenges remain for existing defense techniques: (1) accurately distinguishing between benign and malicious model updates and (2) effectively mitigating the influence of poisoned model updates during model aggregation. To address these challenges, we propose a novel defense framework against targeted poisoning attacks with Spatial-Temporal Analysis and Robust aggregation for FL (STAR-FL). First, we employ spatial-temporal clustering to identify and remove potentially malicious updates from the FL training process. Second, we adjust the learning rate during aggregation to mitigate the impact of any malicious updates that evade detection. Third, we conduct extensive experiments across multiple benchmark datasets to evaluate the spatial-temporal analysis and robust aggregation in STAR-FL. Experimental results demonstrate their synergistic effect in enabling STAR-FL to effectively protect FL and consistently outperform state-of-the-art defenses against targeted poisoning attacks, significantly reducing Attack Success Rates (ASRs). The source code is available at this https URL.

---


### 85. [Generating Synthetic Behavioral Populations from XR Motion](https://arxiv.org/abs/2608.14867)

**<font color=#1a73e8>作者：</font>** Xiaozheng Wang, Ryan P. McMahan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large-scale behavioral datasets are becoming increasingly important for machine learning, personalization, and behavioral modeling in extended reality (XR). However, collecting XR motion data from hundreds or thousands of participants remains expensive, time-consuming, and difficult to reproduce across research groups. As a result, many XR studies continue to rely on relatively small datasets that limit the scale and diversity of behavioral evaluation. To address this limitation, we investigate synthetic behavioral populations as a complementary approach to traditional XR data collection. We present an interpolation-based motion synthesis pipeline that combines dynamic time warping (DTW) with trajectory interpolation to generate synthetic behavioral trajectories from existing XR datasets while preserving task structure and incorporating motion characteristics from contributing participants. Using the publicly available FAST VR assembly dataset, we generated and openly released 100 synthetic behavioral trajectories. We evaluated the synthesized trajectories through motion-based user identification. Hybrid datasets containing both real and synthesized trajectories achieved performance comparable to similarly sized real-only datasets while maintaining low confusion between synthesized trajectories and their contributing participants. Rather than serving as conventional data augmentation, the proposed approach generates distinguishable behavioral trajectories that expand XR behavioral populations for larger-scale behavioral modeling and machine learning evaluation. Our findings demonstrate that synthetic behavioral populations provide a promising approach to expanding XR behavioral datasets and supporting future data-driven immersive systems.

---


### 86. [Beam-Wise Statistical Background Subtraction for Static Roadside LiDAR: A Cross-Sensor Benchmark Study](https://arxiv.org/abs/2608.14868)

**<font color=#1a73e8>作者：</font>** Alexander Baumann, Marcel Vosshans, Thao Dang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background subtraction is a key preprocessing step for infrastructure-based LiDAR perception, enabling efficient isolation of dynamic traffic participants without semantic annotations. However, systematic cross-sensor evaluations and reproducible studies for static roadside LiDAR are missing. This paper presents a comparative benchmark of beam-wise statistical background subtraction for statically mounted LiDAR sensors. We formulate background estimation as a per-beam temporal modeling problem and investigate complementary statistical strategies that capture dominant as well as multi-modal background structures, combined with spatial filtering in the angular and 3D domain. To enable reproducible evaluation, we introduce HighwayScene, a new multi-LiDAR dataset recorded in a static roadside setup, and extend the public CoopScenes dataset with static/dynamic point-wise annotations. Across multiple scenes and heterogeneous sensing technologies, we demonstrate that beam-wise statistical modeling provides a robust and transferable solution. Combining lightweight per-beam models with spatial consistency filtering substantially improves precision while maintaining high recall and real-time capability. All datasets, annotations, and implementations are publicly released.

---


### 87. [JarvisBench: Always-on Intelligence Between Humans and Agents](https://arxiv.org/abs/2608.14870)

**<font color=#1a73e8>作者：</font>** Chen Chen, Zhehuai Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents can execute continuously, but human attention remains intermittent and scarce. This creates a bidirectional coordination problem: users may need immediate access to an agent while work continues in the background, whereas agents may encounter consequential decisions that require user judgment after the user has stopped monitoring execution. We posit an always-on attention-coordination layer---\textit{Jarvis}\footnote{Named after the fictional AI assistant in \textit{Iron Man}.}---that mediates this interface and allocates human attention across one or more working agents. We introduce \textit{JarvisBench} to evaluate both directions of this coordination: whether an intermediary can accurately and promptly answer user-initiated questions about ongoing work, and whether it can recognize when an agent requires user judgment, solicit that judgment at the right moment, and route it back to improve task outcomes. JarvisBench contains 45 agentic task instances: 20 single-agent tasks and 25 workstreams organized into 10 multi-agent projects. The tasks span 19 domains and were selected and adapted from more than 2,000 public candidates. Crucially, the need for user attention arises naturally during execution rather than from an obvious omission in the initial prompt. JarvisBench is designed to integrate with arbitrary agent runtimes without modifying their underlying execution loops. Our reference implementation further provides a full-duplex speech interface, allowing users to reach Jarvis naturally while timely attention coordination supports agents working in the background. By separating agent execution from attention coordination, JarvisBench provides a stable evaluation target as agent capabilities continue to improve.

---


### 88. [Personalized Auto-Research: Towards a True AI Co-Scientist](https://arxiv.org/abs/2608.14881)

**<font color=#1a73e8>作者：</font>** Bo Ni, Franck Dernoncourt, Hongjie Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI co-scientists that generate hypotheses, retrieve related work, design experiments, execute code, and draft full papers are beginning to change how research is carried out. Despite this rapid progress, state-of-the-art systems remain researcher-agnostic: given a research goal, they optimize novelty, validity, or reviewer score while ignoring the individual scientist who will use the output. This overlooks a fundamental fact about research, namely, that what counts as novel, valuable, or feasible depends on the researcher, including their prior work, methodological repertoire, and the collaborators and communities in which they are embedded. In this work, we introduce the problem of personalized auto-research, which conditions every stage of the research process on a representation of the individual researcher. We argue that personalization is not a convenience layer, but rather the fundamental property that allows an AI system to serve as a genuine co-scientist rather than a generic instrument. To address this problem, we propose a general and flexible framework that threads a graph-grounded researcher context through retrieval, hypothesis search, experimentation, writing, and review. The framework consists of three fundamental components: (i) graph-grounded researcher representations, (ii) personalization across the full research pipeline, and (iii) evaluation grounded in the individual. Notably, we highlight a one-size-fits-all failure mode where distinct researchers issuing the same goal receive essentially the same research, erasing the tacit knowledge through which novel ideas arise. Finally, we discuss fundamental open problems and challenges.

---


### 89. [Can Neural Networks Learn by Experimenting on Themselves? Self-Interventional Learning from Functional Consequences to Predictive Self-Knowledge](https://arxiv.org/abs/2608.14894)

**<font color=#1a73e8>作者：</font>** Michał Tomaszewski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning systems usually model external data, while their internal functional organization is analyzed by external observers. This work introduces Self-Interventional Learning (SIL), in which a neural system perturbs its own functional structure, observes consequences, learns a predictive self-model, generalizes to unexecuted interventions, and uses predictions to guide later structural action. In a construction-known synthetic system, SIL recovered critical structure, redundancy, and replaceability, while synergy was not reliably recovered. Across 30 fresh confirmatory seeds, increasing the pairwise intervention budget from 4 to 56 reduced held-out prediction error from 0.0335 to 0.0148 and increased Spearman correlation from 0.629 to 0.883. In a matched ablation, preserving the correct intervention--consequence mapping reduced prospective prediction error by 81.3%, while using the same learned self-model for action reduced normalized regret by 31.7% relative to ignoring it. However, model-guided action did not significantly outperform a direct empirical-memory policy, and powered CIFAR-10/ResNet validation showed no robustness advantage over equal-budget direct repair search. These results support SIL as an intervention-driven framework for learning predictive knowledge about a network's own functional organization, while showing that the self-model remains incomplete and is not universally superior to simpler direct strategies.

---


### 90. [Frontier AI Forecasting Has a Measurement Problem: An Audit of Progress Evidence](https://arxiv.org/abs/2608.14903)

**<font color=#1a73e8>作者：</font>** Fabricio F Costa  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantitative forecasts of frontier artificial intelligence often connect dated targets to trends in benchmark scores, training compute, release time, or expert belief. This paper audits whether the public measurement record supports those connections before another trend is fitted. I construct a frozen, event-centric record through 12 August 2026 with 62 selected systems, 12 versioned benchmarks, seven capability or impact criteria, 144 graded events, 27 source records, and 408 typed relations. The record is an audit sample, not a census. Only seven systems jointly observe estimated training compute and a METR 50 percent task horizon. Training compute is absent for 19 of 27 closed systems, including every selected closed release from 2026, while none of the 35 open-weight systems has a METR horizon observation. Benchmark succession creates a second break: a seven-system link from METR Time Horizon 1.0 to 1.1 has a log-scale slope of 1.206 (95 percent CI 1.021 to 1.390), whereas a six-system MMLU to MMLU-Pro comparison appears shift-like under logit and probit links but not under linear or logarithmic links. The observed bridges have about 80 percent power only for slope departures near 25 percent. Provenance is concentrated: 52 of 71 substantive quantitative events, or 73.2 percent, come from one measurement programme, and 76.1 percent are laboratory releases. A review of 56 methodological and empirical sources identifies 16 complementary measurement directions spanning resources, inference budgets, reliability, agentic work, safety, human preference, field outcomes, and forecast backtesting. No direction supplies a replacement scalar. The result is not that frontier AI forecasting is impossible, but that a defensible dated forecast is a claim about a versioned measurement system with explicit joins, protocols, links, and source dependence, not merely a fitted curve or calendar date.

---


### 91. [SpIn-ViT: Designing a Sparsity-Induced Vision Transformer That Is Mechanistically Interpretable](https://arxiv.org/abs/2608.14922)

**<font color=#1a73e8>作者：</font>** Philip H. Lee, Parth Padalkar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability has recently expanded to Vision Transformers (ViTs), with Sparse Autoencoders (SAEs) increasingly used as post-hoc tools to decompose internal representations into sparse and more interpretable features. However, because post-hoc SAEs are trained on frozen representations after the ViT has already been optimized, their latent features are not directly aligned with the downstream classification objective. We introduce SpIn-ViT, a framework that jointly trains a pretrained ViT and a modified SAE end-to-end, directly aligning sparse patch-level representations with image classification. SpIn-ViT learns semantically coherent neuron activations that localize meaningful image regions while maintaining competitive predictive performance. We evaluate SpIn-ViT across nine image-classification benchmarks using classification accuracy, quantitative interpretability metrics, AI-based and Human evaluations. Compared with the previous state-of-the-art post-hoc SAE method, SpIn-ViT achieves 8.84% higher average classification accuracy, an AI-based interpretability score nearly four times as high, and a human-evaluation score more than twice as high. We further extract interpretable rule-sets using the SAE neurons to create neurosymbolic models which achieve 5.97% higher average classification accuracy while requiring a 58.8\% smaller rule-set than the neurosymbolic models created from the SOTA post-hoc SAE method.

---


### 92. [PaSTel: Anchoring Histology in Spatial Transcriptomics via Multi-Scale Hierarchical Bio-Prior Contrastive Pretraining](https://arxiv.org/abs/2608.14924)

**<font color=#1a73e8>作者：</font>** Azim Dehghani Amirabad, Junchao Zhu, Pushpak Pati 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics (ST) links tissue morphology with molecular programs, motivating multimodal pretraining methods that align histology images with gene expression. However, existing approaches suffer from two key limitations: spatially informative gene selection is often dominated by ubiquitous housekeeping genes, leading to weakly discriminative representations, and independent spot-patch alignment fails to capture spatial dependencies that are critical for tissue organization. To address these challenges, we introduce PaSTel, a hierarchical multimodal pretraining framework that integrates biological priors at three levels. At the spot level, TF-IDF reweighting is used to identify spatially informative genes; at the functional level, curated KEGG pathways serve as anchors for encoding global biological semantics; and at the regional level, spatial clustering aggregates neighboring spots to model meso-scale tissue structure. Across multiple downstream tasks, PaSTel consistently outperforms existing vision and vision-omics encoders, demonstrating that incorporating multiscale biological priors yields more informative and transferable representations for spatial transcriptomics.

---


### 93. [When Is an Agent Evaluation Over? Outcome Finality and Cross-Unit Separation](https://arxiv.org/abs/2608.14940)

**<font color=#1a73e8>作者：</font>** Avyay M. Casheekar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current agent evaluations score models on the state visible at the end of a stopped run which they count as one trial. However, interpreting the score as a final result would require two conditions that the endpoint does not itself necessarily establish: outcome finality and cross-unit separation. These conditions are independent, since reconciling a delayed outcome can settle the label while runs still share state and isolating runs can prevent carryover while the scored outcome remains unfinished. We develop a completion argument that specifies the evidence needed for each decision and argue that a final label is justified only when anything that could still change the claimed outcome is resolved, bounded, or retained as uncertainty. First, in a controlled replay to demonstrate the mechanism where an agent's actions were held fixed, we find that the endpoint and terminal labels differ for every delayed operation, while a delayed write changes the next run's score when service state persists between runs but not after isolation or verified reset. Second, in a review of ten public protocols, we find that all protocols identify when a run stops and what is scored, while unfinished operations and the evidence for treating runs as separate trials are documented less consistently. Finally, we propose an open-effects record that lists operations or resources that may remain relevant after the endpoint, their current status, and whether they could change the scored outcome or affect another run.

---


### 94. [Degeneracy Counting Quantum Algorithm using Decoherence](https://arxiv.org/abs/2608.14941)

**<font color=#1a73e8>作者：</font>** Malay Marut Das, Mark A. Novotny, Yaroslav Koshka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counting the global optima of a classical optimization problem is a #P-hard task. We develop the canonical thermal pure quantum (CTPQ) state-based degeneracy counting (CTPQsd#) algorithm that determines the number of global optima of a classical optimization problem P by measuring only a small probe S, without finding individual minima. The method exploits a perturbative relation between the decoherence measure of S and the degeneracy of P when S and P are together in a CTPQ state. We provide the first numerical demonstration that this relation can be used to count the global minima, applying it to problems encoded by diagonal random-energy Hamiltonians as a maximally unstructured testbed for classical binary optimization problems. Classical simulations of up to 20 problem qubits quantify the algorithm's sensitivity to variations in the temperature of the CTPQ state, the Hamiltonian energy range, the problem size, and degeneracy. We establish the temperature threshold for determining the exact degeneracy and identify a second, lower threshold that provides a temperature window to count near-degenerate minima within a user-defined energy tolerance. By confining measurement to S, the protocol replaces tomography over the exponentially large problem Hilbert space with tomography over a small probe represented by only four qubits.

---


### 95. [Looks Can be Deceiving: Annotator and Reviewer Performance Across Imagery Sources in Crowd-Sourced Aerial Damage Assessment](https://arxiv.org/abs/2608.14942)

**<font color=#1a73e8>作者：</font>** Thomas Manzini, Priyankari Perali, Raisa Karnik 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents the first known empirical investigation of annotator and reviewer performance across multi-source remotely sensed imagery, evaluating human labeling across drone, crewed aviation, and satellite views. Because existing aerial imagery datasets rely predominantly on single-source imagery, there is no currently established state of practice for efficiently allocating human labor to curate large-scale, multi-source aerial datasets. This work addresses this limitation by analyzing annotator and reviewer performance within a post-disaster building damage assessment dataset of 9 disasters, where 20041 buildings in drone, 20695 buildings in crewed aviation, and 33392 buildings in satellite imagery were labeled. These labels, provided by 187 annotators, were then refined through two successive quality-control stages: a single-reviewer pass followed by a consensus-committee review. Our analysis reveals two findings that raise questions for standard crowd-sourcing practices. First, initial annotations were revised by the final committee at rates that rise steeply from higher- to lower-resolution sources (25.27% for crewed aviation and 36.95% for satellite), with the same ordering at every observed workflow stage. Second, a single individual review reduced but did not resolve this disagreement: after review, the committee still revised 6.85% of drone, 14.05% of crewed, and 20.86% of satellite labels. These observations suggest that, in workflows like this one, uniform review allocation leaves the most residual disagreement in lower-resolution imagery. Based on this evidence, and consistent with prior work on adaptive task assignment and budget-aware quality control, this paper offers three recommendations for multi-source dataset curation.

---


### 96. [RETRACE: Resilience-Guided Trait-Conditioned Craving Estimation from Wearable Physiology in Opioid Use Disorder](https://arxiv.org/abs/2608.14947)

**<font color=#1a73e8>作者：</font>** Yi Xiao, Harshit Sharma, Dessa Bergen-Cico 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Detecting opioid craving from wearable physiological signals is critical yet difficult, with the potential to support proactive interventions for individuals with opioid use disorder (OUD). This challenge is especially pronounced under subject-independent evaluation because craving is subjective, heterogeneous, and often physiologically entangled with stress. Our empirical analysis shows that stress elicits strong and reproducible autonomic responses, while craving-related signals are weaker, sparse, and largely embedded within stress-related physiology. We further show that psychological resilience, which shapes stress regulation and craving vulnerability, is not reliably observable from short-term wearable windows, but can be captured through reusable subject-level proxies, including post-stress heart-rate recovery and autobiographical memory this http URL by these findings, we introduce RETRACE, a resilience-guided trait-conditioned framework for subject-independent craving estimation from wearable physiology. RETRACE reframes craving detection as trait-conditioned physiological interpretation: rather than assuming the same physiological pattern has the same meaning across individuals, it uses resilience-related subject context to guide inference. Technically, RETRACE introduces a novel dual-encoder design that separates generalizable stress physiology from subject-specific craving interpretation. It combines a frozen stress-pretrained encoder with a resilience-conditioned craving encoder, using feature-level gating and representation-level fusion to enable lightweight personalization without target-user craving labels or per-user retraining. We evaluate RETRACE on a novel multimodal OUD dataset containing wearable physiology, stress and craving annotations, and autobiographical narratives. Under LOSO setup, RETRACE achieves up to 7% absolute improvement over the strongest baseline

---


### 97. [PathFinder: Joint Decompositions of Linked Multimodal Datasets](https://arxiv.org/abs/2608.14951)

**<font color=#1a73e8>作者：</font>** Ying-Qiu Zheng, Alex Fung, Stephen M Smith 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank matrix decompositions can uncover patterns and structure in data and have a number of different applications across many disciplines. Extensions to "joint" low-rank decompositions have been proposed to link datasets from different modalities. While these methods enable the discovery of common patterns across modalities, they require that all the multimodal data share one or more dimensions. We propose a new analysis method, PathFinder, that enables co-analysis of datasets that do not necessarily all share a dimension. The key insight is that as long as pairs or subgroups of matrices do share some dimension, and that there are one or more paths that link across the data matrices, a global joint decomposition can be sought out. This enables the joint estimation of common patterns across different modalities, species, or scales, where a one-to-one mapping across all data along some dimension is not necessarily available. We show that PathFinder is a general umbrella under which many matrix decomposition methods fall as special cases. It can be used to discover common patterns across disparate datasets and to make predictions for missing data or modalities.

---


### 98. [Command-Space Counterfactual Explanations for Pareto-Conditioned Reinforcement Learning](https://arxiv.org/abs/2608.14963)

**<font color=#1a73e8>作者：</font>** Joanikij Chulev, Hendrik Baier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pareto Conditioned Networks learn multiple multi-objective reinforcement learning behaviours by conditioning a single policy on a desired return command. However, the local mapping from command and state to action remains opaque. We propose command-space counterfactual explanations for PCNs: given a fixed state, original command, and foil action, we search, in a black-box setting, for a minimally changed desired-return command under which the same trained policy would choose the foil. Our contributions are threefold. First, we formulate PCN explanations as return-command interventions, using a return-only PCN variant that avoids the added ambiguity of horizon-conditioning. Second, we adapt adversarial machine learning methods to reinforcement-learning explanations. Third, we introduce a boundary-seeded directional search that improves over purely local optimization in the command-action landscape, resulting in our proposed approach CF-ZOO. The resulting explanations are actionable and intuitively expressed in the user's own preferences: "If your trade-off had shifted slightly towards X, the agent would have chosen Y."

---


### 99. [A Physiology-Informed Digital Twin Framework for Simulating Liver Health Progression](https://arxiv.org/abs/2608.14969)

**<font color=#1a73e8>作者：</font>** Sumaiya Afroz Mila, Sandip Ray  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a physiology-informed digital twin of the human liver designed for longitudinal simulation of liver function and early-stage disease progression. The model, referred to as HEPATWIN, integrates key hepatic processes, including carbohydrate, lipid, and protein metabolism, bilirubin conjugation, bile production, and detoxification, within a unified systems-level framework to generate clinically observable biomarker trajectories. Unlike purely data-driven approaches, HEPATWIN incorporates mechanistic representations of liver physiology and patient-specific inputs such as diet, activity, and baseline biomarkers to simulate disease evolution over time. To ensure consistency with clinical progression patterns, we introduce a stage-transition-driven calibration mechanism that aligns simulated outputs with population-level biomarker distributions across disease stages, including NAFLD, fibrosis, and cirrhosis. Validation using the NIDDK NAFLD dataset demonstrates that HEPATWIN produces longitudinal biomarker estimates within clinically acceptable ranges and can forecast trajectories over multi-year horizons. Furthermore, simulated biomarkers retain sufficient clinical signal to support downstream NASH detection with competitive performance relative to models using ground-truth laboratory data. These results highlight the potential of physiology-informed digital twins for personalized, non-invasive diagnosis and prediction of organ health in general and liver health monitoring in particular.

---


### 100. [Demand-Driven Vertiport Siting and Discrete-Event Fleet Simulation for On-Demand Urban Air Mobility Network Design](https://arxiv.org/abs/2608.14974)

**<font color=#1a73e8>作者：</font>** Hossein Z. Saghazadeh, Yonas Ayalew, Reza Ahmari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents a demand-driven framework for on-demand Urban Air Mobility (UAM) network design that links vertiport siting, fleet simulation, and door-to-door travel-time feasibility. Demand is estimated from commuter and passenger activity data, converted into spatial trip-end points, and clustered using K-means to generate candidate vertiport locations. Candidate networks are screened using range and minimum station-spacing constraints, then evaluated with a discrete-event simulation that models multi-vehicle dispatch, deadhead relocation, battery swaps, and service regularity. Flight time and energy consumption are computed using a point-mass eVTOL performance model. In a Greater Los Angeles case study, the preferred design expands from four stations and four eVTOLs at low demand to sixteen stations and twelve eVTOLs at the highest tested demand level. Results show that larger fleets improve completion time and vehicle-arrival regularity but do not eliminate deadhead flights, indicating that spatial demand imbalance remains an operational burden. The travel-time savings analysis further suggests that UAM is most defensible for longer or congestion-heavy trips where sufficient non-flight time remains after accounting for flight time.

---


> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-435](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
