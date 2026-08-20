# 📦 其他研究 | 2026年08月21日

> 本类共 **184** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-184](./part-04.md)

---

### 51. [ERASE: EaRly bAckpropagation SchEdule for Faster Training of Modern Recommendation Systems](https://arxiv.org/abs/2608.18469)

**<font color=#1a73e8>作者：</font>** Ergan Shang, Flavio Sales Truzzi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lightweight proxy models enable rapid experimentation without repeatedly training frontier-scale systems, but their small kernels often leave modern accelerators underutilized. Conventional training compounds this inefficiency by scheduling the forward and backward passes as disjoint phases, so spare capacity in one cannot be filled by work from the other. We reinterpret the detachment mechanism of Forward-Forward (FF) as a scheduling primitive: given a local objective, detaching a block's output removes downstream gradient dependencies, making its backward pass ready when its forward pass finishes. ERASE launches each detached subgraph's backward pass early on a separate CUDA stream, overlapping it with subsequent forward work. Execution trace on a lightweight transformer demonstrates this overlap and its limit: a kernel that saturates the device leaves no capacity for concurrency. On a large-scale click-through-rate model, detaching six dense subarchitectures improves training throughput by up to $9.51\%$ while keeping normalized entropy close to the baseline.

---


### 52. [OmniAlign: A Unified Multilingual Aligner for Word and Sentence Alignment](https://arxiv.org/abs/2608.18474)

**<font color=#1a73e8>作者：</font>** Mengpeng Yang, Jingxu Yang, Chao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual sequence alignment is fundamental for building and exploiting parallel corpora, spanning mappings from documents and sentences down to words and subwords. Existing tools, however, typically specialize in a single granularity, so practitioners often need separate systems for word- and sentence-level alignment---especially in multilingual and long-text settings. We present OmniAlign, a unified multilingual aligner that supports both word-level and sentence-level alignment with a single lightweight model. Built on an encoder-only backbone with strong long-context modeling, OmniAlign induces word alignments from contextualized token similarity matrices, and obtains document-level $m$--$n$ sentence alignments via sentence embeddings combined with dynamic programming. To balance fine-grained alignment accuracy and sentence-representation quality, we use a four-stage training pipeline: alignment-oriented continued pre-training, self-supervised learning, supervised fine-tuning on human annotations, and sentence-embedding distillation from a strong multilingual teacher. Experiments show that OmniAlign achieves highly competitive performance on both word- and sentence-alignment benchmarks and generalizes well to unseen language pairs. Surprisingly, later-stage supervised fine-tuning on short texts further improves alignment quality while retaining the long-context understanding acquired in earlier training, keeping the model robust on long-text word alignment.
\normalsize {\color{blue}\textbf{Code}: this https URL}\par {\color{blue}\textbf{Model}: this https URL}

---


### 53. [Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models](https://arxiv.org/abs/2608.18484)

**<font color=#1a73e8>作者：</font>** Pardis Taghavi, Reza Langari, Gaurav Pandey  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free block-sparse attention can accelerate video transformers, but row-wise attention concentration does not by itself specify an executable sparse operator. Queries sharing a block route may have poorly overlapping supports, while retained attention mass alone does not determine the post-softmax error from skipped interactions. We show that partition geometry affects both pooled support and the predictability of the remaining residual from the sparse output. We introduce SparsePR, which combines Response-Coupled Partitioning with Probe-Fitted Residual Reconstruction. Sampled-query key responses form paired K/V groups, whose centroids induce query-response coordinates for shared routing. A small set of exact query rows then calibrates a call-specific affine correction from the sparse output within the output subspace observed in the probe residuals. Across four heterogeneous video generation and world models, SparsePR consistently reduces attention-reconstruction error. Ablations show that probe fitting accounts for most of this reduction, while response-coupled partitioning lowers hard-drop error and improves reconstruction under a finite probe budget. SparsePR preserves generation quality at 22.0-26.0% realized executed-pair density while achieving 1.48x-2.61x end-to-end speedups. Project page: this https URL

---


### 54. [Designing Social Robots for Social-Cognition Training with Autistic Adults](https://arxiv.org/abs/2608.18488)

**<font color=#1a73e8>作者：</font>** Yuval Zohar, Mordi Benhamou, Guy Laban  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social robots have been widely explored as tools for autism intervention, yet this literature has focused predominantly on children and has rarely involved autistic adults as active contributors to design. This creates a mismatch between existing systems and the social-cognitive challenges autistic adults actually face in everyday life, including navigating ambiguous interpersonal contexts, managing conversational timing, and interpreting implied emotional meaning. To address this gap, we conducted an online focus group and co-design session with five autistic adults to explore what a social robot for social-cognition training should do, how it should interact, and under what conditions it would be genuinely useful. The 90-minute session combined open discussion with structured co-design activities on a shared digital whiteboard, and the resulting verbal and visual data were analysed using reflexive thematic analysis. The analysis yielded seven themes that define core design requirements: the robot should function as a scaffold rather than a substitute, prioritise authenticity over comfort, provide personalised and user-controlled feedback, accommodate emotional self-awareness gaps, respect privacy and contextual boundaries, support rehearsal for real-world social situations, and remain configurable in identity, form, and expression. Together, the findings suggest that autistic adults envision the robot not as a companion or live social assistant, but as a private, configurable rehearsal partner designed to support independence over time.

---


### 55. [Physics-Unrolled Neural Operator for Wireless Field Modeling](https://arxiv.org/abs/2608.18495)

**<font color=#1a73e8>作者：</font>** Rafid Umayer Murshed, Saif Ur Rahman, Mingyue Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Radio maps are essential for wireless decision-making tasks such as access-point placement, coverage planning, and localization, but their fine spatial details are governed by complex propagation effects and are costly to simulate accurately. Machine learning offers a path to high-fidelity radio-map prediction without running expensive high-fidelity simulations for every scene. However, generating high-quality training labels at scale is also difficult: the affordable labels come from finite-ray simulations, which are richer than low-fidelity inputs but carry residual Monte Carlo noise. We address this challenge with Physics-Unrolled Hybrid Neural Operator (PU-HNO), a three-stage cascade that predicts high-fidelity indoor radio maps from low-fidelity ray-tracing outputs and scene priors by progressively capturing reflection, diffraction, and scattering effects, rather than treating radio maps as generic images. We prove that, under conditionally unbiased label noise, the model can learn stable propagation structure and outperform its own training labels. Experiments across diverse floorplans show that PU-HNO outperforms image-to-image baselines, wireless learning models, and monolithic neural operators across both image-quality and wireless deployment metrics.

---


### 56. [DyG$^2$T: Modeling Object Dynamics with 3D Gaussian Temporal-Spatial Particle Graph Transformer](https://arxiv.org/abs/2608.18498)

**<font color=#1a73e8>作者：</font>** Yansong Wang, Zhaobo Qi, Xinyan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modeling object dynamics from limited visual observations is a fundamental problem for enabling accurate motion trajectory prediction in embodied interaction scenarios. Existing dynamics modeling methods first compress reconstructed particle representations into sparse Key Points and model their evolution using locally constrained interactions, thereby discarding fine-grained local details and obscuring discriminative interaction modeling across spatial and temporal scales, leading to drifting trajectories and inaccurate appearance prediction. To tackle these issues, we propose DyG$^2$T, a dynamics modeling framework that infers object motion trajectories by spatially completing and temporally discriminating Key Point representations and modeling multi-scale interaction over particle graphs. Spatially, DyG$^2$T enriches each Key Point by aggregating neighboring raw particle positions to recover fine-grained local details, while explicitly encoding relative offsets among Key Points to enhance geometric structure perception. Temporally, we introduce a Temporal Disentangling Network (TDN) to identify dominant cross-frame variations in latent space and amplify inter-frame differences, yielding temporally discriminative representations that are subsequently aggregated via Temporal Attention to capture frame-wise temporal evolution cues. For comprehensive interaction modeling, a Particle Graph Transformer leverages global attention to preserve discriminative long-range dependencies among Key Points, mitigating representation homogenization induced by locality-constrained modeling and providing a robust basis for accurate trajectory prediction. Experiments on both synthetic and real-world datasets demonstrate that DyG$^2$T achieves accurate dynamics modeling and reasoning, and exhibits strong cross-object and real-world generalization.

---


### 57. [Cross-Modal MRI Ovary Segmentation in Endometriosis Using Unpaired TVUS Prototype Priors](https://arxiv.org/abs/2608.18515)

**<font color=#1a73e8>作者：</font>** Xingjian Kang, Lina Felsner, Dominik Perrin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transvaginal ultrasound (TVUS) and magnetic resonance imaging (MRI) provide complementary information for endometriosis image analysis, yet existing studies mainly focus on single-modality analysis or disease classification, leaving cross-modal ovarian segmentation largely unexplored. In this work, to tackle the increased difficulty of ovary segmentation in MRI due to ovaries' small target size and ambiguous boundaries with surrounding pelvic structures, we propose a dual branch framework for ovary segmentation across TVUS and MRI. More specifically, by adapting MedSAM3 with TVUS-derived prototype bank, we aim to align anatomically consistent feature representations across both modalities. Extensive experiments are conducted on endometriosis-related TVUS and MRI datasets. We observe quantitative and qualitative improvements of over 5 percentage points for the proposed dual-branch approach compared with multiple state-of-the-art methods. Furthermore, our ablation study shows the contribution of individual components such as the prototype bank and the importance of warm-up pretraining in the source TVUS domain.

---


### 58. [OptiModNet: A UNet-Transformer Hybrid with Grouped-Query and Channel Attention for Optic Disc and Cup Segmentation](https://arxiv.org/abs/2608.18516)

**<font color=#1a73e8>作者：</font>** Soumili Ghosh, Debapriya Roy, Aryan Das 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise segmentation of the optic disc and cup is critical for the early detection and diagnosis of glaucoma. However, achieving consistently high performance across datasets while maintaining low computational requirements remains a significant challenge. In glaucoma detection, low-computation methods are crucial for enabling rapid, large-scale screening and facilitating deployment in resource-limited clinical environments. While deep learning models such as UNets, Vision Transformers (ViTs), and Diffusion models have demonstrated strong segmentation performance but these methods often come with substantial computational overhead. UNets are efficient at capturing local features but are limited in modeling global contextual information. Conversely, ViTs excel at long-range dependency modeling but are computationally intensive. Hybrid architectures, such as UNetR, which combine transformer-based encoders with UNet-style decoders, have shown improved performance but while incurring additional complexity. Considering these, in this work, we propose OptiModNet, a light weight novel hybrid architecture tailored for optic disc and cup segmentation. The model integrates diverse attention mechanisms at multiple stages of the network to enhance both local and global feature representation. We include an Aggregated Pyramid Loss that supervises predictions at multiple decoder depths, to promote better gradient flow and structural consistency. We evaluate OptiModNet on the REFUGE2 dataset for both optic disc and cup segmentation tasks. Our method achieves state-of-the-art performance, exceeding existing approaches by over 2.5\%, while maintaining high efficiency with only 3.73 GFLOPs and 1.93M parameters. The code is available at this https URL.

---


### 59. [Prior-Conditioned Gaussian Discriminants for Generalizable AI-generated Image Detection](https://arxiv.org/abs/2608.18523)

**<font color=#1a73e8>作者：</font>** Shashank Kotyan, Makoto Shing, Yuki Imajuku 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based generators have made synthetic images ubiquitous, but detectors often fail under simultaneous shifts in generator, prompt/style, and source-domain. We study AI-generated image detection as a transfer system described by training prior, frozen encoder feature space, and decision rule, and ask when classifier head training adds value beyond what is already separable in modern features. As a controlled diagnostic, we fit a prior-conditioned Gaussian discriminant ladder: closed-form heads built from first- and second-order feature statistics under nested covariance assumptions. On Percept-Lens, a unified protocol over 39 public datasets (7.1 million images), the best rung is frequently competitive with, and sometimes exceeds, released AI-generated image detector heads when matched on both prior and encoder. We further quantify strong sensitivity to the training prior, data-efficiency of moment-based heads, and representation dependence of Gaussian shift metrics, motivating (prior, encoder, head)-level reporting and stronger analytical baselines for AIGI transfer.

---


### 60. [Bridging Search and CRM: Productionizing AI Product Research Agents for Customer Re-Engagement](https://arxiv.org/abs/2608.18543)

**<font color=#1a73e8>作者：</font>** Mandar Kulkarni, Pooja A., Samir Shah  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern e-commerce platforms often operate search, recommendation, personalization, and CRM systems independently, limiting opportunities for proactive customer re-engagement. This is particularly challenging for exploratory intents such as best smartphones or latest 5G phones, where users may leave the platform for external research before purchasing. We present a scalable, production-deployed framework that bridges search and CRM workflows through AI-powered Product Research Agents. The system identifies users with exploratory purchase intent and low engagement, conducts grounded multi-agent product research using behavioral signals, external knowledge, and enterprise catalog data, and delivers personalized recommendations through WhatsApp. We evaluate the framework in a 23-day production deployment involving approximately 15K WhatsApp notifications for mobile product discovery. The campaign achieved substantial CTR improvements over traditional WhatsApp recommendation campaigns, with evidence of secondary engagement through message forwarding and sharing. The deployment also generated downstream purchases and GMV impact, demonstrating the practical effectiveness of AI Product Research Agents for proactive customer re-engagement and end-to-end customer journey optimization.

---


### 61. [Zero-Shot SAM2 Segmentation and Vision Transformer-Based Recognition of Elamite Cuneiform Symbols from Degraded Tablet Images](https://arxiv.org/abs/2608.18544)

**<font color=#1a73e8>作者：</font>** Utsav Poudel, Rasik Bhattarai, Siddhartha Pathak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated recognition of ancient cuneiform script poses a compound signal-degradation problem: the three-dimensional relief of clay tablets creates spatially varying illumination and cast shadows, surface erosion introduces structured noise that overlaps with genuine sign impressions, and severe class imbalance across 141 sign categories undermines classifier reliability. We introduce EpigraphNet, a segmentation-guided transformer pipeline evaluated on the Persepolis Fortification Archive. From 1,239 annotated tablet images, brightness-adaptive morphological preprocessing and zero-shot SAM2-Large segmentation generate clean binary symbol masks, which a fine-tuned Vision Transformer (ViT-B/16) with inverse-frequency class weighting then classifies. EpigraphNet reaches 86.41% top-1 accuracy on a 132-class benchmark, a 17.21 percentage-point gain over the strongest CNN baseline (ResNet-101, 69.20%) and 5.31-12.91% over four modern backbones (DeiT-B/16, Swin-B, ConvNeXt-B, EfficientNet-B4) under identical conditions. The full pipeline runs at approximately 18 ms per sign on an NVIDIA A100 GPU. A lower Spearman correlation between sign frequency and per-class performance indicates more balanced recognition across frequent and rare classes. Implementation is available at: this http URL

---


### 62. [MARCUS: Missing-Aware Region Representation with Contextual Urban Signals for Rent Prediction](https://arxiv.org/abs/2608.18546)

**<font color=#1a73e8>作者：</font>** Chenya Huang, Bin Liang, Zhidong Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal urban data has expanded the applications of urban region representation learning, such as functional zone identification and real estate appraisal, but also introduces challenges caused by data incompleteness. Existing studies usually handle missing data through imputation, treating missingness as noise while ignoring its potential semantic value. To address this issue, we propose MARCUS, a missing-aware region representation model that treats missingness as a contextual urban signal. MARCUS models missingness in three stages: Intra Learning jointly encodes observed features and missing patterns, Inter Learning estimates modality reliability to guide cross-modal interaction, and Fusion uses missing-aware and time-aware gating to generate the final region embedding. We apply MARCUS to rent prediction, a task with long-term trends and seasonal fluctuations, using real-world datasets from Sydney and New York. Experimental results show that MARCUS achieves state-of-the-art performance, reducing MAE by 51.35% on Sydney and 12.62% on New York compared with the best baselines. Additional experiments, including an imputation-based ablation study and randomized additional-missingness analysis, further demonstrate the effectiveness of the proposed method.

---


### 63. [Measuring Proof Burden in Public Bounty Listings: A RentAHuman Case Study](https://arxiv.org/abs/2608.18547)

**<font color=#1a73e8>作者：</font>** Iman YeckehZaare  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Online bounty markets let requesters advertise paid tasks. Workers may be asked not just to complete a task but to prove it, and proof can mean exposure: revealing identity or location, using a personal account, posting publicly, acting in the physical world, or repeated evidence at later checks, none disclosed by the posted price. We call these advertised requirements proof burden and measure them on RentAHuman, a 2026 market publicized as a place for AI agents to hire humans. We study what listings request, not what workers submit or experience.
We manually audited a nonrandom May 31, 2026 snapshot: every listing our searches returned from RentAHuman and Human Pages, another such market (981 listings, all but one from RentAHuman). Two independent coders recorded 13 features (11 kinds of evidence, recurring monitoring, physical-world action) and our 0-5 Proof Burden Score; a blinded third resolved all disagreements. A planned content screen leaves 779 bounty/task listings as the primary population; 438 (56.2%) score 4 or 5, spanning 154 distinct feature combinations: a checklist, not a single score, tells workers what a listing entails.
Platform metadata labels some requester accounts as agents or bots. Exploratory comparisons show physical-world action, location proof, or recurring monitoring in 75.0% of agent-or-bot-labeled versus 55.3% of human-labeled listings, though score-4-or-5 shares did not clearly differ. The labels are self-reported or platform-assigned, the agent-or-bot-labeled listings come from only 20 displayed names, and the comparison was chosen post hoc, after seeing the data: a hypothesis, not a confirmed difference. We contribute the 13-requirement vocabulary, the adjudicated manual audit, and this descriptive case study; the score is a secondary screening summary. The study offers no worker-validated measure or automated detector yet.

---


### 64. [Performance Drift Detection in Machine Learning as a Service (MLaaS) for IoT Environments](https://arxiv.org/abs/2608.18555)

**<font color=#1a73e8>作者：</font>** Deepak Kanneganti, Sajib Mistry, Sheik Mohammad Mostakim Fattah 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine Learning as a Service (MLaaS) is a powerful cloud paradigm enabling data-driven intelligent applications in Internet of Things (IoT) environments, widely adopted across healthcare, smart homes, and industry due to its cost-effectiveness. However, the dynamic nature of IoT frequently alters data distributions, affecting MLaaS stability, while periodic MLaaS updates further introduce performance drift. Unlike traditional ML systems, MLaaS clients operate as black-box users without access to internal data or parameters, making drift detection particularly challenging. To address this, we propose a novel MLaaS Performance Drift Detection framework for IoT environments. The framework first employs an MLaaS extraction model that learns service behavior from input-output pairs and identifies prediction-influenced features. Building on this, the proposed MLaaS Performance Drift Detection (MPDD) model jointly captures variations in input data and MLaaS behavior. We further design an Adaptive-Temporal Performance Drift Detection Mechanism (APDDM) that dynamically adjusts monitoring frequency based on behavioral and data variations, enabling timely drift detection for effective service management. Extensive experiments on real-world datasets demonstrate that MPDD achieves up to 22-25% accuracy improvement over baseline drift detection methods. APDDM provides an average accuracy gain of approximately 4% and reduces the miss detection rate by around 9% compared to fixed-interval monitoring.

---


### 65. [MorphoGP: A Nonparametric Framework for Predicting Equilibrium Beach Profiles Under Tidal Influence](https://arxiv.org/abs/2608.18558)

**<font color=#1a73e8>作者：</font>** Xi Wu, Yanqing Wei, Hang Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The prediction of equilibrium beach profiles under tidal influence is of fundamental importance for sustainable coastal development, informing shoreline protection strategies and managing coastal ecosystems under changing environmental conditions. However, it remains challenging due to the highly nonlinear interactions among wave, tide, and sedimentary processes. Traditional empirical and numerical models often exhibit limited adaptability across diverse coastal environments, with especially pronounced limitations in beach systems where tidal processes are important . To improve data-driven prediction under these conditions, this study proposes MorphoGP, a unified category-specific Gaussian process framework for predicting equilibrium beach profiles (EBPs) under tidal influence. The framework first introduces a ContourCluster model based on contrastive learning to classify tide-influenced beach morphologies automatically. Within each morphological category, a specialized Gaussian process expert learns statistical associations between environmental descriptors including waves, tides, and sediments and the beach profile's shape. A Gating Net then integrates the outputs of all experts through a probabilistic weighting mechanism to produce the final prediction. Evaluated on data from over 180 beach profiles from tide-influenced coasts along the Chinese coast, MorphoGP achieves improved predictive performance compared with conventional and deep learning models, reducing the test RMSE by about 59.3\% compared with the best baseline and achieving a final RMSE of 0.297 m. The proposed framework provides a physically informed, data-driven tool for equilibrium beach-profile prediction under tidal influence and coastal management, while stronger process-level physical coupling remains an important direction for future development.

---


### 66. [Beyond Distortion Robustness: Rethinking Severe Cropping as Erasure-Resilient Message Embedding](https://arxiv.org/abs/2608.18567)

**<font color=#1a73e8>作者：</font>** Bo Pang, Weibin Kong, Juntu Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Robust message embedding in images is important for multimedia security applications such as copyright protection and content tracing. Existing methods are largely developed under a distortion robustness paradigm, where the embedded signal remains spatially present but is degraded by noise, blur, or compression. Severe cropping poses a fundamentally different challenge because it removes part of the carrier itself, causing partial payload disappearance rather than mere signal corruption. In this paper, we revisit robust message embedding from an erasure-resilience perspective and present CREST, a proof-of-concept framework for severe-cropping-robust embedding. CREST combines coding-theoretic redundancy with neural embedding and recovery by expanding a compact QR message into a redundant spatial payload via LT fountain coding and coupling it with cropping-aware embedding and fragment recovery. Experiments on COCO, DIV2K, and VOC2012 show that CREST improves recovery under severe cropping while maintaining competitive visual quality. Under mixed distortions with an area retention ratio of 0.7, CREST improves TRA from 18.52% to 68.45% and reduces EMR from 13.88% to 4.21% over the strongest baseline. On COCO2017, CREST still achieves 48.55--65.12% TRA when only 30--50% of the image area is retained, whereas all compared baselines fail to recover the message. These results suggest that severe cropping is better understood as an erasure problem rather than a conventional distortion problem, motivating the joint design of neural embedding and coding-based recovery.

---


### 67. [NanoSleep: A Parameter-Efficient Hybrid Temporal Convolutional Network for Single-Channel Sleep Stage Classification](https://arxiv.org/abs/2608.18571)

**<font color=#1a73e8>作者：</font>** S M Asif Hossain, Shruti Kshirsagar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sleep stage classification from single-channel electroencephalography (EEG) is essential for wearable and home-based sleep monitoring. However, many deep learning models achieve high accuracy at the cost of large model sizes, which limits their deployment on resource-constrained devices. In this work, we present NanoSleep, a compact hybrid temporal convolutional network for automatic sleep stage classification. NanoSleep combines a learnable Sinc-convolutional front end, a dual-branch feature extractor that fuses multi-scale temporal and spectral representations, a gated dilated temporal convolutional backbone with channel recalibration, and a conditional random field for sequence-level decoding. We further employ a weighted calibrated focal loss to address class imbalance. We evaluate NanoSleep on the Sleep-EDF and Sleep-EDF-Expanded datasets using subject-wise cross-validation. The proposed model consistently outperforms six representative baseline methods, and an ablation study confirms the contribution of each major component. These results demonstrate that NanoSleep provides an effective balance between accuracy and efficiency, making it well suited for wearable devices, home-based sleep monitoring, and resource-constrained clinical applications.

---


### 68. [VQC-ZTI: Variational Quantum Control for Zero Trust Protection of the Tactile Internet](https://arxiv.org/abs/2608.18572)

**<font color=#1a73e8>作者：</font>** Mubassir Serneabat Sudipto, Shakil Ahmed, Ashfaq Khokhar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tactile Internet services couple cyber events directly to physical actuation, so security decisions must improve risk discrimination without perturbing the control path. This paper presents VQC-ZTI, a split-plane Variational Quantum Classifier framework for zero-trust protection of Tactile Internet services, in which an off-path VQC analyzes encrypted-flow telemetry while an on-path policy engine applies cached deterministic grant, restrict, step-up, and deny actions. By decoupling anomaly scoring from enforcement, VQC-ZTI preserves predictable control behavior and allows detector sensitivity and policy aggressiveness to be tuned independently. We evaluate the framework on CESNET-derived aggregated traffic using random, entity-group, and temporal holdouts with a hybrid PyTorch-PennyLane implementation. The full-hybrid Quantum Neural Network achieves mean areas under the receiver operating characteristic curve of 0.9981, 0.9974, and 0.9941 and reduces the false-positive rate relative to ExtraTrees by 44.6%, 49.6%, and 67.9%, respectively. A representative component-timing decomposition further illustrates that batched VQC scoring remains in the asynchronous evidence path rather than the immediate enforcement path.

---


### 69. [Beyond receptive fields: sequence-pooled normalization can supply most of a sequence labeler's context](https://arxiv.org/abs/2608.18576)

**<font color=#1a73e8>作者：</font>** Qing Tian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A convolutional sequence labeler's receptive field is routinely treated as the extent of the model's usable context: it sets dilation schedules, bounds streaming horizons, and underwrites locality claims. However, we show that this can be false: when a normalization layer computes statistics from the current input along the sequence at inference, those statistics open a sequence-spanning path that bypasses the convolutional receptive field to provide global context. We derive this from the layer's Jacobian (the criterion needs no experiment), and what the path carries has a closed form. On a synthetic labeling process with computable optima, the global summary that a sequence-spanning normalization encodes already supplies almost all of what a larger receptive field would buy where labels come in long runs: a network reaching 9 positions comes within 0.009 of the whole-sequence optimum, against a near-chance bound for its reach. Closing the path, by taking the same statistics per position, multiplies what enlarging the receptive field is worth by up to an order of magnitude on simulated genomes at every difficulty level tested and on real 1000 Genomes haplotypes. The same path also confounds attribution: ablating a trained network's receptive-field-enlarging blocks severs part of the path, overstating their contribution 8.3-16.1-fold relative to retraining from scratch. The substitution of normalization for receptive field fades as labels switch more often. Where labels run long, neither the receptive-field justification nor the ablation is wrong about its numbers, but both credit the wrong component.

---


### 70. [SPARC: Subspace Position-Aware Robust Few-Shot Calibration for Distribution-Shifted Industrial Anomaly Detection](https://arxiv.org/abs/2608.18585)

**<font color=#1a73e8>作者：</font>** Seokhee Han, Seungjun Chu, Mateusz Nowak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-based industrial anomaly detectors are calibrated on one distribution but may be deployed on another that differs in illumination, fixture placement, or sensor characteristics, sharply degrading an otherwise accurate detector. Adapting to the incoming lot is a natural response, but labeled anomalies are scarce. We therefore consider calibration using only a handful of verified-normal images available before scoring the rest of the lot. Existing fixes require backpropagation, detector-specific tuning, or choices about feature directions that few calibration samples cannot justify. We present SPARC, a few-shot calibration method that intercepts patch features between encoder and detector and removes a closed-form, spatially indexed estimate of deployment-time nuisance through per-cell subspace projection. It needs only $k \le 8$ verified-normal images and uses the algebraic saturation rank $r{=}k{-}1$ on the encoder's native patch grid. The correction requires no gradient or weight updates and works with memory-bank, density, prototype, and mutual detectors. On the shift-prone benchmarks, SPARC improves pooled Image AUROC and AU-PRO$_{0.3}$ for all seven detectors whose image scores depend on corrected patch features by $+13.8$ and $+3.5$ percentage points (pp), respectively; on benchmarks without engineered shift, the changes are small and mixed. Controls that give competing corrections the same calibration images attribute these gains to the per-cell subspace structure rather than the images alone. Further ablations support the saturation-rank choice and characterize sensitivity to backbone and calibration conditions.

---


### 71. [FD-CanKD: Frequency-Decoupled Cross-Attention Distillation as a Refinement Prior for Compact Object Detectors](https://arxiv.org/abs/2608.18590)

**<font color=#1a73e8>作者：</font>** YoungJae Cheong, Jhonghyun An  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compact object detectors are suitable for resource-constrained visual perception, but their limited representation capacity creates an accuracy gap relative to large models. Conventional detector distillation often relies on prediction-level supervision or a single feature-alignment target, such as response, distribution, correlation, or frequency-domain matching. Frequency-Decoupled Cross-Attention Knowledge Distillation (FD-CanKD) is presented as a detector-oriented framework that transfers teacher knowledge at three complementary levels: head-level prediction supervision, relation-level non-local context transfer, and frequency-level component-selective alignment. Student features first aggregate teacher-side spatial context through cross-attention-based relation transfer, after which frequency-aware alignment preserves complementary structural and detail-sensitive cues. Under controlled Microsoft Common Objects in Context (COCO) experiments, fixed 50-epoch from-scratch comparisons show that FD-CanKD remains competitive with representative detector knowledge distillation baselines. Post-distillation continued fine-tuning further produces a stronger refinement-ready student than detector-only fine-tuning, reaching 48.87 mean average precision (mAP) at intersection-over-union thresholds from 0.50 to 0.95 (mAP50:95), 65.84 mAP50, and 53.40 mAP75 after 20 additional epochs. All distillation modules are removed after training, leaving the deployed student unchanged at 19.7M parameters. The framework is instantiated and evaluated in a controlled YOLOv12 teacher-student setting as a representative compact-detector case study.

---


### 72. [ReX-Shot: Single-Image Rephotography via Geometry- and Camera-Grounded Generation](https://arxiv.org/abs/2608.18593)

**<font color=#1a73e8>作者：</font>** Ruiqi Zhang, Hao Zhu, Wenhao Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image rephotography aims to synthesize new shots of a scene from a single reference image with specified viewpoints, focal lengths, and photographic effects, which are intrinsically coupled in imaging. Existing methods typically treat these factors separately and struggle under joint control: novel-view synthesis may introduce geometric distortions under focal-length changes, while super-resolution and instruction-guided editing remain confined to 2D and cannot reliably extend detail restoration or appearance control to novel viewpoints. We attribute these limitations to imperfect single-image 3D reconstruction and the sampling limit of continuous focal-length enlargement. To reduce projection bias from geometric errors, we use implicitly transformed foundation-model features for robust target-view guidance. We further formulate focal-length enlargement as a geometry-guided super-resolution problem and exploit generative detail priors to recover details lost during sparse 3D resampling. Built on this 3D-aware generative backbone, we lift photographic-effect control from 2D filtering to 3D-aware appearance editing, preserving content consistency across viewpoints and focal lengths. These components form ReX-Shot, a geometry- and camera-grounded generative framework for single-image rephotography. To our knowledge, ReX-Shot is the first unified framework to jointly control viewpoint, focal length, and parameterized photographic effects from a single image. Experiments show that ReX-Shot outperforms representative baselines across all three controls while enabling near-real-time interactive rephotography.

---


### 73. [Finality Before Disclosure for Ledger Authenticators in the Quantum Random Oracle Model](https://arxiv.org/abs/2608.18605)

**<font color=#1a73e8>作者：</font>** Maja Lie, Benjamin Marsh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Public ledgers increasingly authorize state transitions using prior transactions, finalized state, timing, and ordering rather than only a public key, message, and portable signature. We introduce ledger authenticators and $\LAEUF$, an unforgeability experiment for reactive authorization protocols whose public judgment algorithm reads a finalized transcript. The model separates authentication safety from ledger liveness and captures canonical transition freshness, adaptive corruption, exposure before inclusion, censorship, and adversarial ordering. We identify two conditional resource boundaries. An authenticator satisfying our single event conditions yields a contextual one-time signature. Within our rebindable reveal class, safety requires computational post-disclosure non-admissibility. When precursor admission uses only public computation and ledger scheduling, this condition is enforced by closing the evidence eligible to use a disclosed credential. If newly constructed evidence remains admissible after disclosure, censoring the honest reveal gives a forgery. We then define a joint ledger and quantum random oracle execution model in which quantum state persists across classical finalization cuts and oracle evaluations made through the ledger are charged. For a closed finalized target set of size at most $K$, we prove the bound $3\beta_{\mathsf{cut}}^2+3c_{\mathsf{co}}KQ^2/2^\lambda+6\ell/2^\lambda$, where $\beta_{\mathsf{cut}}$ accounts for fresh openings already present at the cut. A commit, close, reveal authenticator instantiates the framework and obtains a multi-user lifetime QROM bound.

---


### 74. [Denoising-Aware Inversion: Revealing Privacy Risks in Noise-Protected Text Embeddings](https://arxiv.org/abs/2608.18610)

**<font color=#1a73e8>作者：</font>** Yubo Wang, Shujie Cui, James Bailey 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dense text embeddings are widely used in data mining, retrieval, and downstream machine learning systems due to their compact and semantically rich representations, but recent embedding inversion attacks have shown that they can expose substantial information about the original text, leading to serious privacy leakage risks. A common defense is to release perturbed embeddings by adding Gaussian noise, which is simple yet effective against standard inversion attacks and does not significantly degrade embedding utility for downstream tasks. However, it remains unclear whether such noise-protected embeddings are sufficiently safe against adaptive attackers that explicitly account for the perturbation process. In this paper, we study text embedding inversion in a noise-protected setting, where the attacker can observe only noisy embeddings and has no access to clean embedding targets. We first analyze why existing generative inversion methods fail under this setting and identify a "Double Noise Trap", which fundamentally prevents standard generative inversion models from achieving high-quality reconstruction. To address this challenge, we propose DAEI, a denoising-aware embedding inversion pipeline that combines a residual denoising autoencoder with generative text inversion where the denoiser is trained in an unsupervised manner using Stein's unbiased risk estimate to enable denoising from noisy observations alone. Extensive experiments show that DAEI achieves approximately 154\% relative improvement in BLEU over the existing generative inversion baseline, while also improving token-level F1 and ROUGE-L by 32--60\%. The promising inversion performance of DAEI challenges the prevailing assumption that simple Gaussian perturbation is sufficient to prevent sensitive information leakage from embedding representations.

---


### 75. [Scalable Geospatial Machine Learning for Power-Line Asset Risk: Integrating Remote Sensing for Lightning and Vegetation Risk Modelling](https://arxiv.org/abs/2608.18611)

**<font color=#1a73e8>作者：</font>** Artur Sokolovsky, Bhavik Merai, Moe Jafari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electric power networks are increasingly exposed to weather-sensitive failure mechanisms that require asset-level, spatially explicit risk modelling for effective intervention planning. This study contributes a modular, robust, and explainable probability-of-failure (PoF) modelling framework for utility asset management. The central contribution is an asset-level architecture that can be scaled to new environmental data sources and additional PoF types without reworking the underlying pipeline. This is particularly relevant for industry settings, where risk models must remain operationally maintainable while adapting to changing data availability, asset-management priorities, and climate-driven hazard conditions. We demonstrate the framework for vegetation-related and lightning-related failure modes using a harmonised geospatial machine-learning pipeline. The implementation integrates multi-source predictors, including topography (SRTM), vegetation condition (MODIS Normalised Difference Vegetation Index - NDVI), lightning climatology (LIS VHRMC), OpenStreetMap-derived proximity features, and utility operational records. The resulting architecture is computationally efficient, operationally extensible, and suitable for utility-scale deployment. It provides actionable asset-level risk stratification for inspection prioritisation, vegetation management, asset hardening, and resilience planning, supporting earlier intervention and more climate-resilient network operations.

---


### 76. [CDGP: Contrastive Dual Gaussian Processes for Weakly Supervised Anomaly Segmentation](https://arxiv.org/abs/2608.18614)

**<font color=#1a73e8>作者：</font>** Seungjun Chu, Seokhee Han, Mateusz Nowak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial visual inspection must both decide whether a product is defective and localize the defect, yet pixel-level masks are costly to collect at scale. Most anomaly-segmentation methods learn only from defect-free images and score deviations from normality. A true defect and an unusual-but-normal region, however, can both deviate substantially and receive similarly high scores. We propose Contrastive Dual Gaussian Processes (CDGP), a weakly supervised framework that models normal and anomaly inducing-variable predictive distributions over dense tokens. Its posterior-dominance statistic standardizes their predictive-mean difference by the joint predictive uncertainty, providing both spatial evidence and image-level confidence. This evidence complements hierarchical normal-reconstruction residuals for fine localization. All calibration uses training data only, without human pixel annotations or test-time fitting. Across MVTec AD~2, KSDD2, and VisA, CDGP ranks first among the evaluated methods on all MVTec AD~2 localization metrics and is first-place or competitive on KSDD2 and VisA. Factorized and matched linear-head controls delimit the contribution and scope of the linear-kernel Gaussian process (GP) formulation.

---


### 77. [SPARC: Slice-to-volume Pipeline for Automated Reconstruction of gated 3D+time fetal Cardiac MRI](https://arxiv.org/abs/2608.18616)

**<font color=#1a73e8>作者：</font>** Arnaud Boutillon, Naomi Clarke, Tomas Woodgate 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fetal cardiac MRI (fCMR) provides valuable diagnostic information complementary to echocardiography, particularly for complex congenital heart disease (CHD). Dynamic cine imaging captures cardiac motion essential for assessment of cardiac function; however, the reconstruction of 3D+time cine volumes from 2D+time acquired slices remains challenging due to unpredictable fetal motion and the absence of automated and robust processing tools suitable for clinical deployment. We present the SPARC pipeline (Slice-to-volume Pipeline for Automated Reconstruction of gated 3D+time fetal Cardiac MRI) which combines physics-informed slice-to-volume reconstruction (SVR) of Doppler ultrasound (DUS) gated stacks of slices, assisted by deep learning (DL) models for thoracic segmentation and anatomical reorientation. The proposed SVR algorithm achieves a tenfold reduction in reconstruction time relative to existing frame-wise approaches ($4.8 \pm 1.0$ vs $49.0 \pm 14.1$ min, $p < 0.0001$) while improving the reconstruction quality. Thoracic segmentation performance using ensemble aggregation exceeded inter-rater agreement (Dice $84.7 \pm 3.9\%$ vs $81.4 \pm 7.7\%$, $p<0.05$), while anatomical reorientation achieved a success rate of $90.1\%$. End-to-end evaluation on a large held-out clinical cohort ($n = 121$) demonstrated fully automatic processing in $82.6\%$ of cases with a mean runtime of $7.1 \pm 1.3$ min, compatible with clinical deployment. The complete SPARC pipeline is publicly available as a Docker container this https URL and is currently deployed at our institution as a clinical research tool.

---


### 78. [PALATE: Personalized Aesthetic Learning through Adaptive Taste Evolution for Multi-User Portrait Retouching](https://arxiv.org/abs/2608.18622)

**<font color=#1a73e8>作者：</font>** Jingxuan Wang, Yifan Mei, Yuxia Niu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic portrait retouching has advanced rapidly, yet its objective is inherently subjective: the same portrait admits multiple professionally valid results, and users disagree about which one is best. Most existing methods optimize a population-level aesthetic standard and therefore cannot capture individual taste, while fine-tuning a separate editing model for every user incurs prohibitive training, storage, and data costs. We propose PALATE, a shared reward-evolution framework that keeps the image editor fixed and instead personalizes the selection among retouched candidates of the same source portrait. PALATE decomposes the reward for each user into a global backbone shared by all users, category-level residuals shared by aesthetically similar users, and a lightweight user adapter, with anti-collapse regularizers keeping the three levels complementary.A cyclic dual-level distillation scheme first distills user-specific preferences into category rewards and then consolidates the resulting category-level knowledge into the global backbone, which is redistributed to initialize the next evolution round. In this way, the shared initialization improves progressively across rounds, enabling unseen users to be calibrated from only a few rankings. On expert-retouched candidates from PPR10K with held-out users and held-out images, PALATE attains 72.83% pairwise preference-prediction accuracy, surpassing all reward, aesthetic, and image-quality baselines, of which the strongest, PickScore, reaches 58.06%. Each new user costs only 512 bytes of user-specific parameters and millisecond-level scoring.

---


### 79. [Evaluation of Image Matching Methods for Visual Odometry on UAVs](https://arxiv.org/abs/2608.18624)

**<font color=#1a73e8>作者：</font>** Gašper Spagnolo, Luka Čehovin Zajc, Matej Dobrevski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicles (UAVs) are becoming a powerful tool for many environmental monitoring and transport applications. Yet, their reliance on Global Navigation Satellite System (GNSS) technology for navigation makes them susceptible to catastrophic failures in scenarios where the positioning signal is unavailable or disrupted. This work explores Visual Odometry (VO) as a crucial navigation component. Recently, numerous deep-learning-based methods for image matching have been proposed that are yet to be implemented in a fully-fledged VO system. In this paper, we evaluate recent state-of-the-art image matching methods for the task of VO for UAV position tracking, with a downwards-facing camera, on our synthetic dataset, and find that while the best results are generated by the recent RoMa matcher, SIFT features can outperform some recent state-of-the-art.

---


### 80. [Coordination on a Budget: Federated Active Learning with Few Labels](https://arxiv.org/abs/2608.18634)

**<font color=#1a73e8>作者：</font>** Liam Mohr, Daphna Weinshall  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Active Learning (FAL) addresses the dual challenges of data privacy and label scarcity, where the absence of a global data view introduces additional hurdles for coordinated query selection. We study cross-silo FAL in the low-budget regime, where annotation decisions are most critical. We characterize, both theoretically and empirically, a heterogeneity reversal: in low-budget settings, homogeneous (IID) data requires stronger coordination to avoid redundant queries, whereas heterogeneous data naturally promotes diversity; this trend reverses at higher budgets. Thus, in contrast to the standard federated learning (FL) narrative where heterogeneity is a primary challenge, we show that IID settings are more challenging for query selection in FAL.
Motivated by these findings, we propose a new FAL framework that utilizes federated representation learning to align client data in a shared embedding space. This enables the server to perform globally coordinated active selection over optionally obfuscated client embeddings, while annotation remains local to each client. Although our framework operates in the more challenging low-budget regime, it achieves performance that surpasses existing FAL methods even when they are given substantially larger annotation budgets, demonstrating the value of centralized coordination under privacy constraints.

---


### 81. [Report on The 1st Workshop on Human-Centered Proactive and Personalized Agents for Interactive Information Access at CHIIR 2026](https://arxiv.org/abs/2608.18638)

**<font color=#1a73e8>作者：</font>** Kirandeep Kaur, Vinayak Gupta, Tanya Roosta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Interactive information access is increasingly moving beyond reactive query-response paradigms toward agentic systems that can personalize interaction, retain context, infer latent needs, recommend next steps, and initiate support. This shift creates new opportunities for adaptive and context-aware assistance, while also raising important questions about autonomy, privacy, trust, transparency, user welfare, and evaluation. The First Workshop on Human-Centered Proactive and Personalized Agents for Interactive Information Access provided an interdisciplinary forum for examining these questions across information retrieval, human-computer interaction, dialogue systems, AI ethics, cognitive science, learning technologies, and human-centered AI. Through invited talks, paper presentations, and open discussion, the workshop engaged with topics including calibrated initiative, knowledge-gap navigation, long-term memory, value-sensitive design, implicit personalization, AI-mediated care, proactive dialogue, and evaluation beyond task accuracy. A central theme across the workshop was that proactivity should not be understood only as earlier action or improved prediction, but as a form of initiative that must be appropriately timed, transparent, contestable, and aligned with user goals. This report summarizes the workshop and synthesizes the research challenges it surfaced for designing proactive and personalized agents in interactive information access.

---


### 82. [SAM2Dual: Training-Free, Dual Memory for Long-Term Video Object Segmentation](https://arxiv.org/abs/2608.18640)

**<font color=#1a73e8>作者：</font>** JeongRae Kim, Changwon Lim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-term video object segmentation (VOS) remains challenging due to error accumulation under extended occlusions, re-appearance, and scene changes. Although SAM2 provides strong zero-shot performance, its streaming memory can amplify drift over long horizons when recent, unreliable predictions dominate the memory state. We propose SAM2Dual, a training-free, plug-and-play inference-time enhancement that improves long-video robustness without updating model weights. SAM2Dual introduces a Dual Memory design that explicitly separates (i) short-term memory for rapid local adaptation and (ii) long-term memory built via interval-based sampling to preserve global identity cues, combined through a gated fusion strategy. In addition, we present Text-Aware Memory (TAM), which extracts a compact word-level cue from early frames and uses text embeddings to reweight memory contributions based on semantic compatibility, supporting identity preservation when visual evidence becomes weak or ambiguous. Across long-term benchmarks, SAM2Dual consistently improves stability on long videos, raising J&F from 49.33 to 50.65 on MOSEv2 and achieving consistent gains on LVOSv2.

---


### 83. [IriSig-Spoof: A Real-World Benchmark for Time-Robust Satellite RF Fingerprinting and Spoofing Detection](https://arxiv.org/abs/2608.18642)

**<font color=#1a73e8>作者：</font>** Shichang Guo, Yuanyu Zhang, Shuangrui Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Low Earth orbit (LEO) satellite Internet is becoming critical communications infrastructure, yet its open wireless links remain vulnerable to satellite impersonation and signal spoofing. Radio frequency fingerprinting (RFF) offers a potential defense by exploiting transmitter-specific hardware imperfections manifested in received signals. However, the reliability of existing satellite RFF methods remains difficult to assess because no unified dataset and benchmark support temporal, open-set, and cross-scenario evaluation. To address this gap, we introduce IriSig-Spoof, a real-world Iridium dataset comprising 5.17 million messages collected from 66 satellites over 32 days, together with software-defined radio (SDR)-generated spoofing signals from indoor and outdoor settings. We further establish three benchmark tasks: temporal robustness evaluation, open-set RFF identification with unknown-signal rejection, and cross-scenario spoofing detection. Experiments using a multi-scale attention convolutional neural network (MACNN) show that temporal robustness varies across configurations, with the best configuration achieving 97.75% average cross-day accuracy. In open-set evaluation, MACNN achieves an area under the receiver operating characteristic curve (AUROC) of 0.9715, while showing that effective unknown-signal rejection does not necessarily ensure reliable identity assignment. Cross-scenario experiments reveal differences at low false-positive rates. IriSig-Spoof provides a reproducible basis for evaluating robust RFF methods under temporal variation and changing attack conditions.

---


### 84. [ProxyGuard: Direct Reliability Inference for Randomized Data Release Mechanisms with Shared Targets](https://arxiv.org/abs/2608.18643)

**<font color=#1a73e8>作者：</font>** Dipesh Tharu Mahato, Pramod Dhungana  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Researchers often choose a proxy dataset from many releases, transformations, or seeds. Search can make an invalid release appear adequate, while one adequate release does not establish that its generator is reliable. ProxyGuard controls both errors using prespecified bounded risks and a sealed target set. Named-release mode corrects for multiplicity and certifies specific releases. Direct shared-target mode evaluates independent mechanism draws on a common target, lower-bounds their favorable-score rate, and subtracts a bound on favorable scores contributed by invalid releases. Conditional on the target, release scores are independent, yielding a finite-sample mechanism-reliability guarantee without independent target batches or assumptions on release-level $p$-value dependence. We show that the mean-only penalty is sharp and derive a smooth-score certificate with additive target concentration. In a registered three-requirement study, direct mode raises power from 5.6\% to 64.2\% at reliability 0.95, while named mode remains stronger under high-signal evidence. Prospective audits span full-pipeline Rice--TVAE, which retrains on every draw, and a non-tabular text mechanism.

---


### 85. [Clinically Structured Surrogate Rewards for Post-SFT Medical Image Captioning](https://arxiv.org/abs/2608.18654)

**<font color=#1a73e8>作者：</font>** Hyun Jun Kim, Heeseung Shin, Changwon Lim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image captioning requires translating heterogeneous visual evidence into concise clinical descriptions, where errors in findings, assertion states, or anatomical relations can alter clinical meaning despite surface-level fluency. Sequence-level policy optimization can directly optimize complete captions, but common rewards rely on global text similarity, direct image-caption compatibility, or unordered concept overlap, leaving visual neighborhoods and clinical-claim structure implicit. We propose a clinically structured surrogate reward framework for post-SFT medical image captioning. The framework combines biomedical semantic and short-range lexical fidelity with two structured rewards: distributional image-neighborhood alignment, which matches the medical-image-bank distributions induced by reference and generated captions, and clinical graph consistency, which applies maximum-weight one-to-one matching to entities, assertion states, and typed relations. The four rewards are independently normalized within each rollout group, combined with fixed relative weights, and optimized with GDPO. Across organizer-evaluated hidden test sets for the Standard and Synthetical ImageCLEFmedical Caption tracks and three vision-language backbones, the method improves Overall, Relevance, and Factuality over matched SFT baselines in all six backbone-track combinations, with average relative gains of 3.4%, 2.1%, and 5.8%, respectively. Ablations and paired diagnostics indicate that the structured rewards provide complementary signals, reducing image-neighborhood divergence and improving entity-assertion-relation consistency.

---


### 86. [X2Streaming-TTS: Causal Token-Level Text-to-Speech from Streaming Text with Speech-State Inheritance](https://arxiv.org/abs/2608.18661)

**<font color=#1a73e8>作者：</font>** Rime Wen, Zehan Liu, Shawn Qin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Streaming text-to-speech is essential for low-latency spoken dialogue systems, yet many systems wait for sentence-level text and are therefore only pseudo-streaming. True token-level synthesis must generate speech from uncertain prefixes while maintaining perceptual continuity over an unbounded stream with bounded context. We present X2Streaming-TTS, a causal TTS framework that consumes asynchronously arriving text tokens and emits speech without accessing future input. To handle uncertain prefixes, we introduce causal commitment, which keeps ambiguous expressions provisional through uncertainty-aware buffering and performs capacity-adaptive, punctuation-aware segmentation. To preserve acoustic continuity, we further introduce causal speech-state inheritance, which carries the complete Code2Wav state and selected historical Talker states across segment boundaries. Together with an attention prior constraint, it blocks access to future positions while retaining bounded acoustic context. Experiments show that X2Streaming-TTS outperforms existing pseudo-streaming models on most subjective and objective metrics. Further analysis shows that causal commitment stabilizes online segmentation and reduces failures caused by insufficient context, while speech-state inheritance improves boundary continuity without degrading naturalness or speaker identity. X2Streaming-TTS thus achieves strict token-level synthesis with quality comparable to the evaluated offline baselines, a median time to first audio token (TTFT) of 15.8 ms for a single request, and a median TTFT of 260.8 ms at 128 concurrent requests. Our implementation is publicly available at this https URL .

---


### 87. [Dynamic SpectraFormer for Ultra-High-Definition Underwater Image Enhancement](https://arxiv.org/abs/2608.18662)

**<font color=#1a73e8>作者：</font>** Zhiqiang Hu, Tao Yu, Shouren Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater images suffer from color distortion, haze, and poor visibility due to light refraction and absorption in water. These challenges significantly impact the utilization of Autonomous Underwater Vehicles (AUVs) or marine robots. Typically, color and brightness distortions manifest at lower frequencies, while edge and texture distortions are prevalent at higher frequencies. Traditional methods struggle to concurrently rectify these mixed distortions as they primarily concentrate on the spatial domain. To address these issues, we introduce the Dynamic SpectraFormer, which enhances underwater images through a frequency domain transformer. The Dynamic SpectraFormer introduces an ultra-high-resolution sparse spectrum attention module, which could capture the long-term dependency without losing the universal approximating power. Additionally, we have developed a dynamic spectrum weight generation layer that serves as an adaptive spectrum band selector, accentuating critical frequency bands and suppressing less relevant ones. Consequently, this method significantly improves underwater image quality by addressing both high- and low-frequency distortions. Our extensive ablation studies and comparative evaluations consolidate the Dynamic SpectraFormer's efficacy across multiple underwater image enhancement benchmarks. The source code is available at this https URL.

---


### 88. [Candidate-Fate Accounting for Transparent Sensor Diagnostic Pipeline Search](https://arxiv.org/abs/2608.18665)

**<font color=#1a73e8>作者：</font>** Haotao Xie, Yutian Chen, Yangqi Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial sensor diagnostics relies on preprocessing, representation, and classification pipelines, making automated pipeline search useful for reducing manual design cost. However, existing automated machine/deep learning (AutoML/AutoDL) reports typically retain only fitted trials, scores, and winners, omitting generated candidates that are invalid, pruned, skipped, cached, or unfitted. This omission limits reviewers' ability to check signal constraints, budget use, and unevaluated legal alternatives. To address this, we propose candidate-fate accounting, a candidate-level audit framework for diagnostic search traces. It records each observed candidate as auditable evidence: hashes merge repeated observations, legality checks flag invalid candidates, allocation rationales explain budget decisions, and a closed fate ledger assigns one terminal fate to each candidate. Experiments on three bearing-diagnostic datasets show that the framework detects invalid candidates and identifies 30--41 candidates omitted by fitted-trial-only reports, with closed fate records verifying complete candidate accounting while maintaining competitive diagnostic performance. The code is available at this https URL.

---


### 89. [Teeth2Point: A Two-Stage Dental CBCT ROI-to-Point Segmentation Framework](https://arxiv.org/abs/2608.18667)

**<font color=#1a73e8>作者：</font>** Qi Ma, Shipra Jain, Niko Benjamin Huber 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern deep learning architectures have demonstrated strong performance in dental CBCT segmentation. One remaining crucial challenge is accurate tooth labeling in cases with missing or malpositioned teeth, which are highly relevant for dental practice. Transformer-based architectures should in theory be able to resolve such ambiguities using global anatomical context. However, due to the high resolution of CBCT volumes and the wide spatial distribution of teeth within volumes, dense patch-based volumetric processing faces an inherent trade-off. Computational costs limit the number of patches that can be used in self-attention and thus, one can either increase the extent of the context captured in self-attention or capture fine-grained structural details by using small patches, but not both. In this work, we present Teeth2Point, an efficient point-based transformer framework for dental CBCT semantic segmentation that can avoid this trade-off. Teeth2Point first localizes volumetric regions of interest (ROIs) surrounding teeth using a convolutional model, then converts ROIs into point tokens using adaptive sampling. A transformer model predicts accurate segmentations using the point tokens, which allow capturing global context while retaining high resolution. The transformer is first pretrained using self-supervised learning (SSL), in the style of DINO but using domain-specific augmentation strategies, followed by supervised finetuning. The SSL pretraining, which includes random token masking, provides robustness to complex anatomical variations. Compared with the strongest two-stage baseline, Teeth2Point improves abnormal-case performance by 1.44 DSC points on average across four datasets; relative to the first-stage nnU-Net, the gain is 1.9 points.

---


### 90. [Reinforced Planning with Latent World Models](https://arxiv.org/abs/2608.18669)

**<font color=#1a73e8>作者：</font>** Armin Sommer, Jannik Schilling  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Humans solve complex problems by constructing plans and mentally simulating their outcomes with an internal model of the world. Machine learning has produced world models that similarly predict the outcomes of action sequences, but the improvement of candidate plans still isn't fully learned. Current planners are either hand-designed, distilled from a hand-designed optimizer, or learned only to inform an amortized policy rather than to revise the plan itself. We introduce the Reinforced Planning, a method based on the idea that search can be learned by reinforcing good search rules into a neural planner. Our implementation RP1 learns both how to evaluate imagined outcomes through a critic, as well as how to improve multi-step plans through an optimizer trained fully offline from imagined world-model roll-outs. To our knowledge, RP1 is the first method to fully learn how to improve multi-step plans. Furthermore, it can be trained independently of and attached to any pretrained latent world model. Across visual navigation, arm reaching, and robotic manipulation on two world-model backbones, RP1 substantially outperforms hand-designed search algorithms, reaching near-perfect success in several settings while using $1,000 \times$ less world-model rollouts and being up to $67 \times$ faster than the strongest alternative under concurrent planner inference.

---


### 91. [DynCur-Geo: Dynamic Curiosity Reward Shaping for Multimodal Active Geo-Localization](https://arxiv.org/abs/2608.18673)

**<font color=#1a73e8>作者：</font>** Yiming Sun, Yang Zhang, Pengfei Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Active geo-localization enables low-altitude UAVs to search for specified targets from limited local aerial observations, supporting time-sensitive applications such as search and rescue and emergency inspection. However, multimodal target cues, restricted views, and sparse feedback make it difficult to balance exploration with target convergence. Existing curiosity-driven methods assign a fixed intrinsic-reward weight throughout search, which can continue rewarding novelty after the agent nears the target and induce detours. We propose DynCur-Geo, a dynamic curiosity framework that adjusts prediction-error intrinsic reward according to remaining target distance. A distance-aware gate encourages early exploration and shifts the policy toward goal-directed behavior near the target, while potential-based reward shaping supplies dense progress guidance. Experiments across multimodal, cross-scene, disaster-affected, and long-range settings show consistent gains over active geo-localization baselines.

---


### 92. [An Empirical Benchmark of Deep Time-Series Models for Smart Meter Energy Forecasting](https://arxiv.org/abs/2608.18675)

**<font color=#1a73e8>作者：</font>** Behnaz Kavoosighafi, Maria Eidenskog, Wiktoria Glad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate forecasting of energy consumption is important for the efficient operation of power systems, with direct implications for operational costs, energy management, and system maintenance. Due to the availability of extensive high-resolution consumption data from smart meters, data-driven methods have been used for short-term and long-term forecasting. However, their comparative performance on real-world smart meter data is still not well studied. In this paper, we present an empirical benchmark of nine modern deep learning models for time-series forecasting, including linear, MLP-based, convolutional, and Transformer architectures. We evaluate these models on two publicly available smart meter datasets. Our analysis focuses on three factors that strongly affect forecasting performance: the length of historical input, the prediction horizon, and the choice of model architecture. We show that extending the historical context improves accuracy, but only up to a saturation point, after which additional input provides limited benefit. In contrast, accuracy decreases as the prediction horizon increases. We also investigate the trade-off between prediction accuracy and computational complexity, and assess the statistical significance and practical magnitude of performance differences across models. Our results show that deep learning models consistently outperform classical baselines, while lightweight architectures achieve relatively similar performance at significantly lower computational cost. Additionally, architectural differences only become meaningful at longer forecasting horizons and on more heterogeneous datasets. Finally, a subgroup analysis across geodemographic and household categories shows that model choice has limited impact for most population segments.

---


### 93. [FRAGMENT: Factorized Graph Representations for Document Generation and Editing via Entity-Aware Transformations](https://arxiv.org/abs/2608.18679)

**<font color=#1a73e8>作者：</font>** Ayoub El Bouchtili, Guilhaume Leroy-Meline  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structured documents such as invoices, forms, reports, and scientific articles derive meaning from the interplay between spatial layout, textual content, and logical structure. Generative models operating at the pixel or token level often struggle to capture these dependencies effectively. We explore FRAGMENT, a generative framework that represents a document as a typed relational graph and factorizes its distribution as p(structure, content) = p(structure) * p(content | structure). The framework consists of two stages. The first stage, the Architect, is a causally masked Transformer conditioned on document category that autoregressively generates the graph topology and typed spatial relations. The second stage, the Builder, is a GATv2-based graph attention network that enriches the graph with normalized bounding boxes, text, and visual style attributes. Both stages define explicit likelihood models, yielding a tractable document-level likelihood that serves as an anomaly score for forgery detection. For controlled editing, a prompt-conditioned extension injects instruction embeddings into the Builder through cross-attention, enabling semantic and entity-aware modifications. We describe training on DocLayNet and fine-tuning on FUNSD and SROIE. Experiments on DocLayNet, FUNSD, and SROIE evaluate FRAGMENT alongside representative autoregressive, layout-only, and graph-based baselines, providing an empirical analysis of the characteristics and trade-offs of the proposed factorized graph generation framework.

---


### 94. [Sounds Uncertain: Exploring the Affective Aspects of Sonification for Uncertainty Visualization](https://arxiv.org/abs/2608.18680)

**<font color=#1a73e8>作者：</font>** Marcel-Simon Dutt, Sita A. Vriend, Elias Elmquist 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Affective visualization can influence how users perceive, interpret, and engage with data by embedding and conveying emotion through visual design. While sound is widely used in media to evoke emotions, little is known about how sonification can support affective visualization. In this work, we investigate how sonification can communicate emotion in uncertainty visualizations through a co-design study. Participants created two sonifications to accompany a visualization: one conveying the affective component of uncertainty and one conveying neutrality. Our findings show that uncertainty was commonly associated with wavy auditory qualities related to an ominous sentiment. On the other hand, neutrality was associated with clear and relaxing auditory qualities. These results provide insights for the design of visualizations that integrate sonification to communicate the affective component of uncertainty.

---


### 95. [Transforming Heart Disease Prediction with Advanced Machine Learning Techniques](https://arxiv.org/abs/2608.18687)

**<font color=#1a73e8>作者：</font>** Sami Ullah, Muhammad Mohsin Khan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heart disease remains the leading cause of mortality globally, necessitating early and accurate detection to improve patient outcomes. This research focuses on the predictive analysis of heart disease using machine learning (ML) techniques, comparing the performance of multiple classifiers to identify the most accurate and least error-prone method. Two datasets from UCI and Kaggle repositories were utilized, each containing 14 attributes related to heart health indicators. Techniques including J48, Naive Bayes, Logistic Regression, Simple Cart, Bagging, Decision Stump, AdaBoost, Artificial Neural Networks, and Support Vector Machine (SVM) were applied. Evaluation metrics such as Mean Absolute Error (MAE), Relative Absolute Error (RAE), accuracy, precision, recall, and F-measure were used for performance comparison. Results revealed that SVM achieved the highest performance on the UCI dataset, while Simple Cart performed best on the Kaggle dataset, offering the highest accuracy and lowest error rates. The research work concludes that ML models, when properly tuned and validated, can significantly assist in the early diagnosis of heart disease, offering critical support for clinical decision-making. Future work may involve hybrid approaches and the use of more recent datasets to further improve prediction accuracy.

---


### 96. [Europe's Climate Ambition Under Scrutiny: Evidence from Deep Learning Emission Projections](https://arxiv.org/abs/2608.18690)

**<font color=#1a73e8>作者：</font>** Jacopo Ghirri, Carlos Rodriguez-Pardo, Lara Aleluia Reis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The European Union has committed to reducing greenhouse gas emissions 55% below 1990 levels by 2030, but whether current trends are compatible with this ambition remains uncertain. We apply deep learning to high-resolution socioeconomic and sectoral data across EU27 member states till 2023 to project sectoral CO$_2$ trajectories under current trends, extrapolating observed sectoral momentum without assuming changes in the pace or effectiveness of the policy environment beyond what is already reflected in historical data. We project that EU27 emissions will exceed the 2030 target by 35% (620 Mt CO$_2$ shortfall), with only a small minority of countries on trajectories consistent with the bloc's commitments. While the Power sector achieves target-consistent reductions driven by the renewable transition, Mobility shows minimal progress and accounts for over a third of total emissions by 2030, reflecting a structural inertia across member states rather than geographically concentrated lag. Our findings indicate that substantial additional intervention is required to close Europe's ambition-implementation gap, and call for establishing up-to-date energy information in Europe.

---


### 97. [Composed Historical Image Retrieval by Modeling Temporal Representations](https://arxiv.org/abs/2608.18694)

**<font color=#1a73e8>作者：</font>** Adrià Molina Rodríguez, Oriol Ramos Terrades, Josep Lladós Canet  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While time evolves linearly, the geometry of neural embedding spaces is inherently multi-dimensional, often chaotic, and difficult to interpret. In principle, one could constrain an embedding space to a single temporal dimension; however, such a reduction would sacrifice performance on downstream tasks, as one-dimensional embeddings cannot retain sufficient expressive capacity. This paper asks whether it is possible to learn representations that preserve temporal structure while remaining effective for image and object retrieval, and answers this question by building the mathematical foundations of such a system. We propose Temporally Decomposable Image Representations (TDIR), a representation learning algorithm that decomposes historical photographs into separate date and content components through orthogonal subspaces. We define and prove the conditions under which such a decomposition is achievable, characterize the error incurred when those conditions are only partially met, and show that orthogonality between temporal and categorical subspaces emerges naturally from the joint optimization, without requiring it to be imposed explicitly. Beyond its geometric properties, TDIR enables a class of transitive operations on embedding spaces: the temporal information of one image can be extracted and injected into the representation of another, with no label supervision required. All theoretical properties are grounded and validated in the real-world problem of Composed Image Retrieval on historical photographs, where a query simultaneously specifies object content and a target time period, either through labels or through example images. This in-the-wild setting serves as a concrete backing for the propositions we derive, offering an intuitive and interpretable way to navigate photographic archives while maintaining competitive performance in both date estimation and object retrieval.

---


### 98. [CamWorldQA: Perceptual Quality Assessment of Camera-Controlled World Video Generation](https://arxiv.org/abs/2608.18710)

**<font color=#1a73e8>作者：</font>** Yunhe Li, Likun Wu, Sijing Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative video models have enabled camera-controlled world video generation, allowing models to synthesize videos under user-defined camera trajectories. However, existing video quality assessment (VQA) methods are mainly developed for natural videos and fail to capture the unique perceptual characteristics of camera-controlled generation, such as viewpoint consistency, motion coherence, and content preservation. In this work, we introduce CamWorldQA, the first benchmark for perceptual quality assessment of camera-controlled world video generation. CamWorldQA contains 720 generated videos produced by 6 representative generation methods from 20 diverse source videos under 6 camera trajectories, where each video is annotated with a human-rated perceptual quality score through subjective experiments. Furthermore, we propose CWQA, a no-reference quality assessment network with three complementary branches that extract spatial features, temporal motion features and optical flow features to jointly predict quality scores. Extensive experiments demonstrate that CWQA achieves superior performance over existing quality assessment methods on the CamWorldQA dataset.

---


### 99. [EgoHRV: Continuous Heart Rate Variability Estimation from Egocentric Systems for Autonomic Response and Skill Assessment](https://arxiv.org/abs/2608.18711)

**<font color=#1a73e8>作者：</font>** Berken Utku Demirel, Christian Holz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric vision systems capture human behavior from visible cues, but overlook physiological indicators of autonomic states such as stress, engagement, and attention. Heart rate variability (HRV) is a widely used noninvasive marker of autonomic regulation under stress. HRV reflects small timing differences between successive heartbeats and has so far been out of reach for egocentric platforms, where motion and noise in gaze video mask exactly this fine-grained timing. We propose EgoHRV, a method that estimates HRV as well as heart rate (HR) from the gaze cameras that are already integrated into egocentric headsets. Our pipeline combines a 3D backbone with a novel low--high decomposition module that extracts the blood volume pulse (BVP) signal from gaze video. Our cross-domain pretraining aligns the frequency-domain representations of contact-based and camera-derived signals. This alignment gives EgoHRV the temporal precision to recover HRV from the subtle fluctuations in gaze video. EgoHRV achieves state-of-the-art accuracy for HR and HRV estimation from egocentric video, and its uncertainty-aware design improves downstream behavioral modeling. Integrating our HRV estimates and confidence measures into EgoExo4D's proficiency estimator raises accuracy by 17.8%. Beyond skill, continuous HRV estimation also opens egocentric systems to stress- and arousal-aware estimation tasks. Code: this https URL

---


### 100. [The Impact of CutMix on Reliability and Robustness in Semantic Segmentation](https://arxiv.org/abs/2608.18715)

**<font color=#1a73e8>作者：</font>** Steven Landgraf, Markus Ulrich  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ensuring not only high accuracy but also reliable and robust predictions is critical for the deployment of semantic segmentation models in safety-critical applications such as autonomous driving. Despite the widespread use of CutMix - a simple yet powerful data augmentation strategy - its effect on the reliability and robustness in dense predictions tasks remains unexplored. Motivated by recent findings that semi-supervised segmentation methods, where CutMix is a core component, can severely degrade reliability, this study isolates and systematically analyzes the influence of CutMix on segmentation accuracy, calibration, and uncertainty quality. We evaluate two representative architectures, the CNN-based DeepLabV3+ and the transformer-based SegFormer, across both in-domain and out-of-domain scenarios. Our results show that CutMix has only a minor impact on segmentation accuracy but consistently improves the reliability, particularly under distribution shifts. These improvements indicate that CutMix primarily enhances the trustworthiness of the model's calibration and uncertainty rather than the raw segmentation prediction itself. This distinction is crucial for safety-critical deployment, where reliable confidence estimates are as important as raw performance.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-184](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
