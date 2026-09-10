# 📦 其他研究 | 2026年09月11日

> 本类共 **176** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-176](./part-04.md)

---

### 101. [Interpreting Object-Dependent Concept Brittleness in Text-to-Image Diffusion Models](https://arxiv.org/abs/2609.09909)

**<font color=#1a73e8>作者：</font>** Yifan Yuan, Xiangyu Liu, Hongming Shan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although text-to-image diffusion models generally exhibit strong prompt-following ability, we identify a persistent and previously underexplored failure pattern in which a small subset of prompts differing only in the object consistently fails to realize the same target concept under identical generation settings. We term this phenomenon object-dependent concept brittleness. Such cases suggest systematic internal blind spots rather than random sampling noise. In this paper, we present an interpretability-oriented framework to audit and minimally correct these failures. Our key idea is to analyze denoising trajectories in a step-wise sparse autoencoder (SAE) space, where abstract style and attribute concepts become more separable than in the raw denoising representation. This sparse space enables us to compare successful and failed generations, identify concept dimensions whose evidence is missing, weakened, or temporally delayed, and construct class-level concept prototypes from reliable class-consistent samples. Based on this audit process, we introduce a lightweight inference-time correction strategy that interpolates denoising features toward the corresponding prototype in SAE space. Rather than serving as a task-specific retraining method, this intervention acts as a validation of the diagnosed concept deficiency. We evaluate the proposed framework on style and attribute failure cases across multiple diffusion backbones, with significant improvements in concept consistency, text fidelity, and repair success. Further analyses show that deeper denoising representations provide clearer concept structure, while early-stage intervention offers the strongest correction leverage. Code is available at this https URL.

---


### 102. [A Kernel-Based Modular Discriminant Analysis Framework for Small-Sample Learning](https://arxiv.org/abs/2609.09910)

**<font color=#1a73e8>作者：</font>** Lingxiao Qu, Yan Pei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The small-sample-size (SSS) problem remains a fundamental challenge in machine learning when labeled data are scarce due to cost, accessibility, or ethical constraints. While numerous approaches have been proposed, existing methods often struggle to maintain stable and discriminative representations under high-dimensional and limited-data conditions. Kernelized Linear Principal Component Discriminant Analysis (KLPCDA), a recently proposed modular framework, integrates variance preservation, inter-class separability, and intra-class compactness within a unified kernel space. Although its formulation has shown promising initial results, a systematic understanding of how its components interact across diverse SSS scenarios remains lacking. In this paper, we present a systematic cross-domain study of KLPCDA to characterize the interaction mechanisms among its core objectives. We analyze the behavior of its seven variants across multiple real-world SSS tasks, including hyperspectral image classification, mechanical fault diagnosis, medical diagnosis, and face recognition. Through extensive experiments and ablation studies, we investigate how different objective combinations influence performance under varying conditions such as noise, class imbalance, and high dimensionality. Our analysis reveals consistent patterns in the interaction of the three core objectives variance, between-class, and within-class terms, providing a unified and interpretable understanding of their roles in stabilizing representations and enhancing discrimination in SSS settings. Based on these findings, we further derive practical guidelines for selecting appropriate KLPCDA variants under different data characteristics. Experimental results demonstrate that KLPCDA achieves strong and robust performance across domains, while maintaining low computational complexity suitable for resource-constrained environments.

---


### 103. [Development and Validation of a Physics-Guided Machine Learning Extrapolation Framework Using a Classical Transient Diffusion Benchmark](https://arxiv.org/abs/2609.09912)

**<font color=#1a73e8>作者：</font>** Ashutosh Yadav, Alok Dubey, Prodyut Ranjan Chakraborty 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models used in engineering are typically trained within limited operating ranges, yet reliable predictions are often required beyond these domains. Consequently, the primary challenge is extrapolation rather than interpolation. Rigorous validation is hindered by the scarcity of data outside the training range. To address this limitation, a novel extrapolation framework is integrated with established machine learning architectures to enable accurate and physically consistent predictions beyond the training domain. The framework is established by systematically evaluating two physics-guided architectures: a Bidirectional Long Short-Term Memory (BiLSTM) network and a Physics-Informed Neural Network (PINN). A classical one-dimensional transient diffusion problem is adopted as a benchmark because its exact analytical solution provides unlimited, reliable data across the spatio-temporal domain, enabling rigorous quantitative validation. The problem is particularly challenging because the solution evolves from an initial singularity through a strongly nonlinear transient regime before approaching a steady-state linear profile. When training data are confined to an intermediate portion of this evolution, backward extrapolation toward the singularity becomes especially demanding. To improve reliability, physics-guided coordinate transformations, boundary-aware learning strategies, and stability-enhancing temporal marching are incorporated. Extrapolation is evaluated using a train-predict-validate-extend strategy, in which validated predictions are recursively added to the training set to progressively extend the prediction horizon. The results demonstrate accurate and physically consistent predictions beyond the training domain, highlighting the framework's potential for engineering applications where data availability is limited.

---


### 104. [Multi-Pass, Multi-View Blended Learning for High-Fidelity Volumetric CT Synthesis from Chest X-Rays](https://arxiv.org/abs/2609.09920)

**<font color=#1a73e8>作者：</font>** Ozer Can Devecioglu, Serkan Kiranyaz, Rashid Mazhar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reconstructing volumetric Computed Tomography (CT) from a single 2D chest radiograph (CXR) is an ill-posed inverse problem, further complicated by the scarcity of paired CXR-CT training data. Prior approaches address this by training on Digitally Reconstructed Radiographs (DRRs), which are synthetic projections derived from CT volumes. However, the domain gap between DRRs and real CXRs limits generalization, often resulting in coarse or anatomically inconsistent reconstructions when applied to clinical images. To address this challenging problem, this study introduces a Multi-Pass Multi-View Blended Learning framework for synthesizing high-fidelity volumetric CT directly from real chest X-ray (CXR) images. The proposed approach progressively decomposes the synthesis task into two distinct, complementary learning stages. Stage 1 is an unsupervised CXR-to-DRR Domain Adaptation, while Stage 2 includes three passes, namely, (a) supervised DRR-to-CT Transformation, (b) unsupervised Multi-View Slice Refinement, followed by (c) Progressive Transfer Learning (PTL). With such a blended learning paradigm, the proposed approach mitigates the synthetic-to-real domain gap while enhancing both the structural integrity and anatomical detail of the final output. On the LIDC-IDRI dataset, where paired DRR-CT ground truth is available for quantitative evaluation, the proposed method improves upon prior methods by up to 14% in PSNR and 7.6% in SSIM. The framework successfully generates structurally consistent and anatomically realistic high-fidelity CT volumes from real CXRs, marking a significant advancement toward clinical viability of CT reconstruction from standard radiographic images.

---


### 105. [Multimodal Emotion Recognition in Conversations via Class-Wise Adaptive Modality Fusion and Affective Geometry](https://arxiv.org/abs/2609.09924)

**<font color=#1a73e8>作者：</font>** Oriol Marín, Roger Marí, Gloria Haro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Emotion Recognition in Conversations (ERC) requires integrating heterogeneous textual, audio, and visual cues while accounting for conversational context and emotional dynamics. We extend the Self-Distillation Transformer architecture for ERC with appearance+geometry visual representations, class-wise adaptive modality fusion, and a valence-arousal prior for affective transitions. On the MELD and IEMOCAP datasets, geometry-enhanced visual representations improve weighted F1 by 0.27 and 4.36 points over appearance-only features, respectively, while class-wise adaptive fusion provides further gains of 0.17 and 0.25 points over the original softmax gate. The valence-arousal prior yields targeted improvements of 0.30 and 0.74 accuracy points on emotionally shifted utterances while preserving performance on stable turns. These results indicate that structured facial cues, emotion-dependent modality weighting, and affective geometry provide complementary benefits for multimodal ERC.

---


### 106. [Adversarial Training for Tabular Credit Scoring: A Multi-Attack Robustness Evaluation in P2P Lending](https://arxiv.org/abs/2609.09945)

**<font color=#1a73e8>作者：</font>** Gijs A. F. Niewzwaag, Marijn G. S. Veth, Manuele Massei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning-based credit scoring is increasingly central to Peer-to-Peer (P2P) lending, yet its resilience to adversarial manipulation, where applicants strategically alter self-reported inputs to secure favourable decisions, remains poorly understood. Most adversarial-robustness evidence comes from image and text domains and evaluates a single attack against a matching defence, offering little guidance on how defences generalise across attack types in tabular credit data. We address this with a systematic train-test robustness benchmark on a large Lending Club subset, spanning three model families (logistic regression, a feed-forward neural network, and a transformer for tabular data) and four attacks confined to applicant-mutable features: Fast Gradient Sign Method (FGSM), Projected Gradient Descent (PGD), Salt-and-Pepper (S&P) noise, and DeepFool, plus a mixed-attack regime. Across a full grid evaluated with stratified cross-validation, adversarial training sharply improves robustness against the attack it is trained on and transfers well within the gradient-based family, but transfers weakly to non-gradient corruption, so single-attack defences overstate real-world resilience. Mixed training delivers the most balanced robustness across heterogeneous attacks while preserving clean-test performance, supporting multi-attack stress testing in credit-model governance.

---


### 107. [Improving Cross-Lingual Token Representations by Adding a Pinch of SALT](https://arxiv.org/abs/2609.09953)

**<font color=#1a73e8>作者：</font>** Guillem Ramírez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual sentence encoders enable scalable transfer across hundreds of languages, powering applications such as translation mining and zero-shot learning in low-resource settings. Although trained for sentence-level alignment, they are increasingly also applied to token-level tasks such as hallucination detection and sequence tagging, exposing a mismatch between training and usage. We propose SALT, a lightweight post-training method that improves token representations by injecting span-level supervision into existing sentence encoders. Across five multilingual token-level benchmarks, SALT achieves the best overall results on four of them, outperforming alternative fine-tuning strategies and competitive encoders. It also improves sentence-level performance on cross-lingual retrieval and classification tasks. These results demonstrate that span-level supervision is an effective signal for improving both token and sentence representations.

---


### 108. [Somatosensory Activation and Attentional States in Creative Making](https://arxiv.org/abs/2609.09960)

**<font color=#1a73e8>作者：</font>** Katherine Rees  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The methods for capturing the creative process come with associated tensions around memory recall, articulation, and communication during the act of making, as well as how to record these considerations. This paper has a twofold purpose: first, to offer an example of a mixed methodology, drawn from dance anthropology, sensory ethnography, and design, that applies embodied methods as an alternative for documenting creative making. Specifically, this incorporates the researcher-as-participant and the collation of fieldnotes, embodied knowledge/movement recall, with notation forms, and participant interviews. These are existing methods in dance anthropology; however, using them alongside exploratory prototyping and workshop approaches broadened this work into transdisciplinary practice. Second, it discusses the activation of somatosensory systems through wearable technology and the facilitation of heightened sensory awareness for the practitioner, leading to a subsequent ability to focus on creative decisions linked to reflection and metacognition.

---


### 109. [Decentralized network congestion control for DAG-based distributed ledger system](https://arxiv.org/abs/2609.09961)

**<font color=#1a73e8>作者：</font>** Mayank Pandey, Rachit Agarwal, Sandeep Kumar Shukla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We propose a variable and behavior-based node-specific proof-of-work (PoW) model for a directed acyclic graph (DAG)-based distributed ledger technology (DLT) network to mitigate decentralized network congestion control. Network congestion control for centralized communication systems is an established field of study, with detailed and continuous research being done on the subject. However, attention to congestion control in decentralized networks is relatively recent and underexplored, especially with DLT, such as blockchain and DAG-based networks. For the DLT networks, the network congestion is caused by factors such as transaction spamming, an increase in the user base, and the launch of new tokens. We focus on the congestion caused by the spamming of transactions within the blockchain and DAG-based DLT network. Based on the network throughput of transactions per second and consensus procedure, the DAG-based DLT needs to control network spamming more than the blockchain network. The PoW model within the DLT consensus framework is a limited deterrent against spamming. Our model provides equal opportunities for all stakeholders regardless of their computational resources. It prevents and penalizes any node that attempts to spam or dominate the network with more than the prescribed number of transactions. Since the system nodes compete to issue transactions with finite network resources, we display the system behavior through a non-cooperative game. Further, we show that our model enforces prescribed behavior amongst the nodes through the proof of the existence of Nash equilibrium in the game.

---


### 110. [CrossLink: Breaking Location Privacy by Linking Device Identifiers Across Protocols](https://arxiv.org/abs/2609.09963)

**<font color=#1a73e8>作者：</font>** Aneet Kumar Dutta, Mihirraj Dixit, Kevin Gni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smartphones simultaneously transmit temporary identifiers over LTE, WiFi, and BLE. Existing privacy defenses analyze identifier randomization per protocol, implicitly assuming that these protections compose across protocols. We show that they do not: Even when each protocol leaks only temporary identifiers and the adversary is fully passive, unsynchronized identifier rotations allow cross-protocol stitching of device traces. We present CrossLink, an uncertainty-aware tracing algorithm that links identifiers across time, space, and protocols under noisy localization and mobility. We evaluate CrossLink using controlled lab experiments with commodity devices and large-scale mobility simulation. Under large-scale mobility simulation, CrossLink reconstructs full traces for 83% of users, versus 22% for the best single-protocol baseline, showing that location privacy must be analyzed jointly across protocols. We further show that CrossLink remains effective under partial coverage: strategically placed sniffers near LTE handover regions, mobile sniffers, and limited high-coverage subregions retain sufficient cross-protocol evidence to bridge observation gaps, achieving substantially higher linkability than random deployments.

---


### 111. [Deep Neural Networks for Learning Intent from sEMG Signals to Support Hardware Devices for Post-Stroke Neurorehabilitation](https://arxiv.org/abs/2609.09971)

**<font color=#1a73e8>作者：</font>** Zakariyya Brewster, Divy Wadhwani, Emily Yan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finger-specific motor intent is a clinically meaningful control signal for post-stroke neurorehabilitation, where residual muscle activity may remain measurable despite weak or incomplete movement. We study five-finger multilabel intent decoding from impaired-arm high-density surface electromyography (sEMG) in PhysioMio, a bilateral longitudinal dataset collected from stroke patients. A common processing protocol aligns movement labels, applies 20--450 Hz Butterworth filtering and Symlet-4 wavelet denoising, segments overlapping 200 ms windows, and extracts twelve time- and frequency-domain descriptors per channel. Direct LSTM, CNN, and GNN baselines reveal complementary behavior: the LSTM attains the highest subset accuracy (0.545), whereas the GNN attains the highest macro F1 (0.706) and macro AUPRC (0.776). Architecture search then identifies CNN-Large as the strongest single-split CNN, with 0.593 subset accuracy and 0.714 macro F1, while CNN-Micro provides a compact architecture for embedded inference. To match a four-sensor hardware design, we retrain CNN-Micro using channels associated with ECRB, ECRL, FDS, and FDP and exclude the ground electrode from model input. Across five seeds, cross-channel knowledge distillation improves the four-channel student over direct training, reaching $0.5219 \pm 0.0114$ subset accuracy, $0.7612 \pm 0.0038$ finger accuracy, and $0.6095 \pm 0.0058$ macro F1. The selected 123K-parameter model accepts nine windows of 48 features and has been exported to ONNX. These results establish a reproducible software path from post-stroke sEMG to compact five-finger intent prediction for subsequent hardware-in-the-loop evaluation.

---


### 112. [Dependency-Aware ROM/CBD Correctness Bounds for ML-KEM-768 at the Heuristic Failure Scale](https://arxiv.org/abs/2609.09983)

**<font color=#1a73e8>作者：</font>** Aurélie Duriez, Christophe Tommasini  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We certify an honest-decapsulation failure upper bound for ML-KEM-768 in an explicit random-function/centered-binomial (ROM/CBD) abstraction. Domain-separated public-matrix streams are modeled as independent uniform ring elements and secret/noise polynomials as independent CBD2 primitives; this is not an information-theoretic statement about the fixed SHAKE instantiation of FIPS 203. Recent formal assessments identify rigorous justification of ML-KEM's heuristic decapsulation-failure scale as an open problem; within the explicit ROM/CBD abstraction studied here, we obtain a dependency-preserving certified upper bound at that scale. The analysis preserves dependencies induced by the public matrix and by both ciphertext-compression terms. Its terminal chain has three components: an exact graph-coupled full-ideal reference for the joint c_u/c_v residual; a proper-ideal bivariate Fourier transport whose rare |T|>=3 branch is closed by an exhaustive three-factor anti-concentration replay; and exact bit-specific FIPS decoding events followed only by a 256-coordinate union bound. A formal partial-Fourier lemma makes the spectral-to-total-variation step explicit. The reduced rational certificate satisfies Pr[K' != K] <= P_* <= 2^-164.81, with -log2(P_*) = 164.810716201343121.... The 164.81 threshold is exact but numerically tight: the certified exponent exceeds it by only about 0.0007162 bit, and 164.82 is not certified. The result is an upper bound for an arbitrary message fixed independently of the public and secret randomness, under honest encryption and decapsulation. It is not an exact DFR, not a fixed-SHAKE equivalence theorem, not a new IND-CCA reduction, and not an adaptive delta-correctness result.

---


### 113. [From Few-Shot Segmentation to Clinician-in-the-Loop Medical Image Analysis](https://arxiv.org/abs/2609.10001)

**<font color=#1a73e8>作者：</font>** Yazhou Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot medical image segmentation (FSMIS) seeks to delineate unseen structures from a small support set, but its standard formulation fixes task-defining evidence before inference. This assumption is fragile when query cases exhibit acquisition shift, atypical pathology, ambiguous boundaries, or poor image quality. Prototype learning, cross-domain matching, interactive segmentation, uncertainty estimation, test-time adaptation, and promptable foundation models address parts of this problem, yet have not been jointly evaluated under a common model of expert attention and clinical risk. This Perspective reframes FSMIS as a sequential clinician-model decision problem with a static support budget $K$ and a distinct interaction budget $B$. At each step, a system accepts the current segmentation, requests feedback, or defers to full expert review. Queries vary in location and modality and are selected by response-conditioned net expected value of information; clinician-provided feedback informs bounded adaptation only after prespecified provenance, consistency, and safety gates. The framework separates distributional atypicality from predicted clinical failure and treats clinician responses as informative but fallible observations. We synthesize the transition from few-shot and cross-domain segmentation to interactive and selective adaptation, delineate the integration gap, and define four research directions with falsifiable hypotheses. Evaluation spans external-domain calibration, quality-effort trade-offs, reader studies, and prospective workflow assessment. The central claim is not that interaction alone resolves domain shift, but that scarce expert attention should be allocated only when it is expected to reduce clinically relevant risk.

---


### 114. [What Makes Adversarial Examples Transfer Across Deepfake Detectors?](https://arxiv.org/abs/2609.10002)

**<font color=#1a73e8>作者：</font>** Rafael M. Mamede, Pedro C. Neto, Ana F. Sequeira  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake detectors remain vulnerable to transfer-based black-box attacks, in which adversarial examples are generated on a source surrogate model and transferred to a target model, unknown to the attacker. Yet how source--target compatibility shapes attack success remains poorly understood. Prior studies evaluate limited detector pools and rarely disentangle architectural from training factors. We conduct a controlled evaluation of adversarial transferability across 60 detectors spanning six backbones, two pretraining regimes, and five training-data configurations, using two attack procedures: AutoAttack (AA) and the Carlini--Wagner attack with Expectation over Transformation (CW--EOT). Matched comparisons reveal significantly higher transfer when source and target share an exact backbone, architecture family, pretraining regime, or training data. This compatibility structure is attack-dependent: exact backbone compatibility has the largest effect under AA, whereas shared pretraining and training data have the largest effects under CW--EOT. When transfer is averaged across non-target sources, mean attack success rate (ASR) is $7.21\%$ under AA and $19.52\%$ under CW--EOT. By contrast, a multi-source oracle combining both attacks attains a \(64.48\%\) mean ASR after excluding exact backbone and training-data matches, showing that source averaging can substantially understate target vulnerability. We release 240,000 adversarially perturbed images, complete pairwise transfer results, detector configurations, and evaluation code. These findings establish source--target compatibility and source-model selection as central dimensions of credible transfer-based black-box robustness evaluation.

---


### 115. [An Explainable Machine Learning Framework for Predicting Blood-Brain Barrier Permeability Using Molecular Descriptors](https://arxiv.org/abs/2609.10012)

**<font color=#1a73e8>作者：</font>** Fatemeh Mahmoudi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Blood-brain barrier (BBB) permeability is a critical determinant in the development of central nervous system therapeutics because it directly influences the ability of drug candidates to reach their target sites within the brain. In this study, an explainable machine learning framework was developed to predict BBB permeability using molecular descriptors generated from the MoleculeNet BBBP dataset with the RDKit cheminformatics toolkit. Fifteen physicochemical descriptors extracted from 2,039 compounds were used to train four supervised machine learning algorithms, including Logistic Regression, Support Vector Machine (SVM), Random Forest, and Extreme Gradient Boosting (XGBoost). Hyperparameter optimization was performed using GridSearchCV, while model interpretability was investigated using SHapley Additive exPlanations (SHAP). Among the evaluated models, the optimized XGBoost classifier achieved the best predictive performance, with an accuracy of 88.97%, a precision of 88.92%, a recall of 97.76%, an F1-score of 93.13%, and a ROC-AUC of 0.9282. Stratified five-fold cross-validation further demonstrated the robustness of the proposed model, yielding a mean ROC-AUC of 0.8982 +/- 0.0130. Feature importance and SHAP analyses consistently identified TPSA, HBD, and LogP as the most influential molecular descriptors governing BBB permeability prediction. Overall, the proposed framework provides an accurate, interpretable, and computationally efficient approach for BBB permeability prediction and may serve as a valuable tool for the early-stage screening of CNS drug candidates.

---


### 116. [Structure-Aware Unsupervised Anomaly Detection for Spacecraft Telemetry with Adaptive EVT Thresholding](https://arxiv.org/abs/2609.10017)

**<font color=#1a73e8>作者：</font>** Óscar Alcarria, Rafael Sánchez, Javier Sempere 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Operational anomaly detection in spacecraft telemetry typically requires labeled historical anomalies or extended warm-up periods. These requirements are rarely met in practice. We propose an unsupervised, deployment-ready framework that produces predictions from the second month of operation without any labels, prior fault knowledge, or mission-specific tuning. The approach combines incremental monthly retraining, statistical model selection, and adaptive Extreme Value Theory (EVT) thresholding for false alarm control. On the ESA Anomalies Dataset (ESA-AD), it achieves $F_{0.5}=0.700$ on Mission~1 and $F_{0.5}=0.698$ on Mission~2 under strict chronological evaluation.

---


### 117. [Elastoformer: Enabling Dynamic Adaptivity via Elastic Model Transformation](https://arxiv.org/abs/2609.10018)

**<font color=#1a73e8>作者：</font>** Sudaksh Kalra, Dolly Sapra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> EdgeAI systems are increasingly employing computer vision applications to enable intelligent, on-device decision-making in real-time. However, these deployments face highly dynamic operational conditions, with fluctuating constraints on latency, power availability, and memory resources. Deep Neural Networks (DNN), which follow fixed computational execution flows, lack the flexibility to adapt to such variability, resulting in inefficient and suboptimal performance in edge scenarios. This underscores the need for architectures that are not only efficient but also dynamically scalable at runtime. In this paper, we propose Elastoformer: A framework that transforms conventional neural networks (NN) into Elastic NN capable of real-time elastic inference. Unlike the conventional bag-of-models approach, which requires maintaining multiple independent models for different operating conditions, Elastoformer offers a single, modular solution that dynamically switches between multiple modes of operation at runtime, adapting efficiently to the changing computational budgets of edge devices without the overhead of managing separate models. Experiments reveal that our framework achieves up to 85% reduction in computation FLOPs, 50% reduction in latency and 76% reduction in memory overhead, while showcasing the architecture agnostic nature of the framework across both Vision Transformers and CNNs. Our code is available at this https URL.

---


### 118. [Beyond Contact Sensors: Deep learning with Pseudo-Labeling for remote Photoplethysmography](https://arxiv.org/abs/2609.10026)

**<font color=#1a73e8>作者：</font>** Bhargav Acharya, Barbara Hammer, Hanna Drimalla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heart rate is a critical biomarker of health, and remote photoplethysmography (rPPG) enables its contactless estimation from video data for telemedicine applications. Recent advancements in deep learning based rPPG methods achieve state-of-the-art results, outperforming classical signal-processing methods in complex scenarios. However, deep learning methods depend on datasets with precise synchronization between videos and ground truth signals collected via contact sensors, whereas signal-processing-based methods do not. To address this dependence on labeled datasets, which are labor-intensive to collect, we investigate under which circumstances pseudo-labels extracted using unsupervised signal-processing methods can replace contact sensors labels for training deep learning methods. Our systematic evaluations found that for datasets with imperfect synchronization, the pseudo-label approach outperforms supervised training on contact sensors. For datasets with good synchronization, results are mixed: within-dataset evaluation shows no significant difference between training methods, while cross-dataset evaluation favors supervised training. However, removing a single outlier participant significantly improves the pseudo-label approach's cross-dataset performance, highlighting the importance of label quality. These results demonstrate that signal-processing methods can generate valid training signals for deep learning models, reducing dependency on labor-intensive dataset collection while maintaining competitive performance.

---


### 119. [Field-level prediction of mid-plane stress tensor fields in concrete target penetration: a cross-velocity graph neural operator surrogate](https://arxiv.org/abs/2609.10032)

**<font color=#1a73e8>作者：</font>** Wenpu Du, Peng Zhou, Yunlong Xia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Although the impact resistance of concrete has been studied extensively, a framework linking mesoscale heterogeneity to full-field stress-tensor prediction has been lacking. Data were generated with a full-scale aggregate-resolved LS-DYNA model (projectile diameter 45 mm, mass 2.13 kg, target diameter 500 mm x thickness 200 mm, mesh 10 mm), verified against published penetration experiments (Frew 2006, Hanchak 1992, Forrestal 1996) by configuration similarity. The dataset contains six-component stress-tensor fields on the X-Z mid-plane for 400 cases (4 impact velocities x 100 aggregate seeds). Three contributions are reported. First, case-by-case verification of the terminal penetration state delimited the rest-state validity of penetration depth and anchored reliable observables to rigid-body motion and field-level stress evolution. Second, a field-level graph neural operator surrogate learned the time-varying stress-field evolution and evaluated cross-velocity leave-one-out extrapolation. Third, the full-scale, aggregate-resolved, cross-velocity, per-seed database was established as a reproducible resource. Cases at 100, 135 and 200 m/s still moved at window end (negative velocity, i.e. rebound), and only one 165 m/s case arrested. Penetration depth is therefore not reported as a rest-state scalar except for the single arrested case (69.33 mm); nose-node depth differences were confirmed as numerical artifacts of displacement integration after erosion. The single-step relative L2 error was 0.6977, reported honestly; autoregressive rollout from frame 11 to 39 took about 144 ms, a speedup of about 3.6x10^3 to 4.3x10^3 relative to single-core LS-DYNA, reported as application value. Validation is bounded by configuration similarity and field-level self-consistency; the framework is a simulation-trained decision-support method within the studied parameter space.

---


### 120. [MedDeID enables locally governed clinical-text de-identification from real or synthetic training data](https://arxiv.org/abs/2609.10049)

**<font color=#1a73e8>作者：</font>** Stig Hellemans, Tom Stroobants, Elyne Scheurwegs 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical notes contain personally identifiable information (PII), restricting reuse for research and medical AI, especially when data cannot leave an institution. We developed MedDeID, an on-premises framework combining in-house annotation and synthetic-note generation with model training, inference, pseudonymisation and evaluation. On an independently annotated, adjudicated 300-note Dutch hospital benchmark, a hospital-trained compact transformer detected 98.9% of identifying text while redacting 0.24% of text outside annotated identifiers; a synthetic-only counterpart detected 96.1%. On 100 primary-care notes, the synthetic-trained model achieved higher recall than the hospital-trained model (90.3% versus 87.0%) and greater robustness to identifier-format perturbations. An English instantiation trained without real text detected 99.7% and 98.9% of annotated identifier characters on two external synthetic benchmarks. These results demonstrate transfer of the workflow to another language, but not clinical English performance. MedDeID provides a route to locally governed de-identification using real or synthetic training data.

---


### 121. [Hybrid Quantum-Classical NLP Classification with Compact Semantic Representations: An Experimental Analysis of Representation Compression](https://arxiv.org/abs/2609.10089)

**<font color=#1a73e8>作者：</font>** Ali Hassan, Zijia Zhao, Maha A. Metawei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language and sentence-embedding models provide rich semantic representations, but their high dimensionality poses a challenge for near-term quantum machine learning (QML), where quantum circuits can process only a limited number of input features. We investigate a hybrid quantum-classical pipeline that transforms high-dimensional sentence embeddings into compact representations for variational quantum classification. The workflow combines a pretrained sentence-embedding model, dimensionality reduction, angle encoding, a variational quantum circuit (VQC), and a classical decision layer. We systematically compare principal component analysis (PCA), neighborhood components analysis (NCA), and linear discriminant analysis (LDA), covering both unsupervised and supervised dimensionality reduction. Using the TREC question-classification dataset, we study the relationship between representation dimensionality, information retention, qubit count, and classification performance. Preliminary PCA experiments reveal a strong information bottleneck: reducing 768-dimensional embeddings to 3, 4, 5, and 8 dimensions retains about 8.2%, 10.2%, 11.9%, and 16.4% of the variance, with corresponding classification accuracies of 50.3%, 51.2%, 57.9%, and 63.4%. In contrast, supervised reduction is substantially more efficient. LDA reaches 85.3% accuracy and NCA reaches 83.1% using only 5 dimensions, under a leakage-free cross-validation protocol, compared with 85.1% for a full 384-dimensional classical baseline. These results indicate that supervised dimensionality reduction can preserve task-relevant information far more effectively than variance-based compression, making compact representations a promising route toward practical hybrid quantum-classical NLP models.

---


### 122. [LinearMask-GS: Stable-Mask Importance Pruning for Compact 3D Gaussian Splatting](https://arxiv.org/abs/2609.10095)

**<font color=#1a73e8>作者：</font>** Donghun Ryu, Minhyeok Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) enables real-time novel view synthesis but produces millions of primitives through adaptive densification, leading to significant storage overhead. Learned-mask pruning methods such as LP-3DGS address this by assigning each Gaussian a learnable mask to identify and prune redundant primitives. However, we identify a limitation of this paradigm: the steep slope of the Gumbel-Sigmoid activation drives mask values to the extremes within the short mask-training window, before the importance ranking has stabilized, producing a sharply bimodal distribution from which that ranking can no longer be reliably recovered. We propose LinearMask-GS, which replaces Gumbel-Sigmoid with a linear increment activation that keeps mask values in a mid-confidence regime throughout mask training, producing a stable, unimodal mask distribution whose ranking tracks importance. On Mip-NeRF 360, our method achieves 3.6x and 1.6x Gaussian reductions over 3DGS and LP-3DGS, respectively, while maintaining or improving rendering quality. For outdoor scenes, it yields a 1.6x reduction (from 2.18M to 1.36M) with notable gains in PSNR (+0.38 dB), SSIM (+0.025), and LPIPS (-0.029).

---


### 123. [A Systematic Evaluation of Molecule Generation Models for De Novo Drug Design: From Benchmarks to Practical Insights](https://arxiv.org/abs/2609.10099)

**<font color=#1a73e8>作者：</font>** Xinrui Xu, Xueer Wang, Dan Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecule generation has emerged as a powerful computational tool for de novo drug design, enabling the exploration of chemical space beyond the limits of conventional virtual screening. The field has progressed rapidly, driven by advances in molecular representations, generative architectures, and target-aware modeling strategies. However, existing reviews typically address specific model families or application scenarios in isolation, rather than offering an integrated perspective on how these components collectively form a coherent generation workflow. In this review, we present a comprehensive evaluation of molecule generation models for de novo drug design, covering 82 methods across five deep generative frameworks, including recurrent neural network (RNN)- and Transformer-based models, variational autoencoders (VAEs), generative adversarial networks (GANs), flow-based models, and diffusion models. We first summarize widely used benchmarks and molecular representations, and then examine the methodological principles underlying both general and pocket-conditioned generation. A central contribution of this work is a systematic synthesis and comparative analysis of reported performance across commonly used benchmarks and evaluation metrics. We also summarize representative experimentally validated case studies. Looking ahead, we discuss future directions in standardized 3D data, interaction-aware generation, receptor flexibility, and multi-objective molecular design, with the aim of improving the reliability and experimental relevance of molecule generation. All collected benchmark resources, evaluation metrics, and model references are provided in a publicly accessible repository at this https URL.

---


### 124. [Distributed and Private Textual Data Synthesis from Embeddings](https://arxiv.org/abs/2609.10104)

**<font color=#1a73e8>作者：</font>** Ergute Bao, Hongyan Chang, Ali Shahin Shamsabadi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We revisit differentially private (DP) text synthesis in the realistic setting of distributed users, where privacy concerns preclude a trusted curator with access to raw user texts. Existing DP text synthesis pipelines are designed for a trusted, centralized curator and often cannot be deployed in distributed settings due to unrealistic trust and access assumptions; when adapted naively, they require repeated, tightly synchronized user participation and incur significant overhead. To address this gap, we propose a DP--cryptography co-design for textual data synthesis that requires no trusted curator and requires only lightweight user participation. Our approach has two optimized components. First, we design a distributed-friendly DP synthesis algorithm that releases a one-time DP summary in an embedding space: it identifies frequent semantic regions and releases their DP centroids, enabling training-free, non-iterative offline text synthesis. We further introduce semantic support protection, which ensures the released summary avoids semantic neighborhoods of infrequent texts, reducing the risk of exposing rare user data. Second, we develop a custom secure protocol that implements this algorithm over distributed user data, enforcing end-to-end DP guarantees without requiring a trusted curator. On four benchmarks, we achieve utility comparable to the state-of-the-art centralized DP synthesis method.

---


### 125. [Storage-Scalable Progressive Semantic Communication via Knowledge-Base Reuse](https://arxiv.org/abs/2609.10112)

**<font color=#1a73e8>作者：</font>** Heng Zhu, Ye Liu, Kun Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing knowledge-base-assisted semantic communication schemes commonly adopt either single knowledge-base quantization (SKBQ) or multi-knowledge-base residual quantization (MKBQ). SKBQ incurs limited storage overhead but has restricted quantization capacity, whereas MKBQ supports progressive refinement by assigning an independent knowledge base (KB) to each stage, causing the KB storage to grow linearly with the transmission depth. To address this problem, we propose storage-scalable knowledge-base reuse quantization (SSKBQ), which reuses a compact set of KBs across multiple residual refinement stages and thereby decouples the number of transmission stages from the number of maintained KBs. A stage-aware residual supervision mechanism is further introduced to regularize intermediate quantized representations and encourage progressive refinement. Experimental results demonstrate that KB reuse provides an effective solution to the storage scalability problem while maintaining competitive progressive reconstruction performance.

---


### 126. [SA-Profile: Automated Sulcus Angle Profiling from Super-Resolution MRI](https://arxiv.org/abs/2609.10125)

**<font color=#1a73e8>作者：</font>** Michael Wehrli, Leo Widmer, Edwin Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Trochlear dysplasia (TD) is an abnormality of the femoral trochlea associated with anterior knee pain and patellar instability. The sulcus angle (SA) is used to assess trochlear morphology, but it is typically measured on a single axial MR slice with no clear guidance on which to select, making it sensitive to slice selection and landmark placement. We propose an automatic framework for continuous SA profiling from super-resolved MR volumes. Clinically acquired axial, coronal, and sagittal MR scans are combined using implicit neural representations to reconstruct a high-resolution volume. SA measurements are computed across the trochlear region using two landmark detection U-Net models. The approach was evaluated on the public fastMRI dataset and a small in-house cohort of patients with TD. Compared with conventional manual single-slice SA measurements, the proposed automated method yielded a mean absolute error of 11.6$^\circ$ while providing continuous characterization of trochlear morphology. Population-level analysis demonstrated distinct mean SA profiles between the public cohort and the in-house TD cohort, highlighting the potential of profile-based assessment to characterize TD. By reducing reliance on a single manually selected axial slice, the proposed framework extends conventional SA assessment to a continuous profile-based description of trochlear morphology without additional imaging, while remaining conceptually linked to current clinical assessment. Further validation is required. The code is available: this https URL.

---


### 127. [TransGaze-Object: Transformer Based Driver Gaze Object Prediction Framework in Real Driving](https://arxiv.org/abs/2609.10139)

**<font color=#1a73e8>作者：</font>** Pavan Kumar Sharma, Ayush Pande, Pranamesh Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driver gaze provides information regarding driver visual attention and situational awareness to the surrounding traffic. Existing driver gaze estimation studies represent gaze in terms of gaze zone or gaze vector/point-of-gaze (PoG). However, object-level gaze information provides a more semantically meaningful representation of visual attention by identifying attended objects, such as vehicles, pedestrians, or traffic signals. In this study, we propose an end-to-end driver gaze object prediction framework, TransGaze-Object, Transformer-based Gaze Object prediction model. The proposed framework first extracts facial features, including face and iris-weighted eye features, along with trafficobject spatial features. A transformer based cross-attention mechanism is then used to compute similarity scores and attention weights for predicting the drivers gaze object. To train this model, we propose a benchmark driver gaze dataset, Urban Driving-Face Scene Gaze (UD-FSG), comprising synchronized driver-face and traffic-scene images, scene objects bounding boxes, and gaze labels in terms of 2D gaze coordinate and gaze object. The TransGaze-Object model achieves an overall accuracy of 60% for gaze-object prediction, compared to 51% accuracy obtained from associating the estimated Point-of-Gaze to traffic objects. The error analysis reveals that TransGaze-Object reduces confusion between traffic objects (predicted) and the background (ground-truth), achieving an error rate of 11.68%, a 49.7% relative reduction compared with 23.21% error obtained from PoG-based gaze-object association. Overall, the results demonstrate the effectiveness of directly predicting gaze objects from driver-face and traffic-scene information, rather than estimating an intermediate Point-of-Gaze and subsequently associating it with traffic objects.

---


### 128. [Sound Debloating of Redundant Checks in Zero-Knowledge Machine-Learning Circuits](https://arxiv.org/abs/2609.10149)

**<font color=#1a73e8>作者：</font>** Zhantong Xue, Pingchuan Ma, Zhaoyu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Zero-knowledge (ZK) proof systems for neural-network inference compile the model into a system of arithmetic constraints. Many of these constraints are redundant checks: range proofs, sign lookups, and bit decompositions who are globally entailed by the rest of the circuit through chains of reasoning that span distant gadgets. Removing them shrinks the circuit and accelerates proving, but the removal must be carefully justified: an unsoundly debloated circuit becomes forgeable, accepting witnesses the original would have rejected and so allowing a prover to claim, for example, that a neural network produced an output it never actually computed. Such soundness vulnerabilities are not hypothetical: under-constrained circuits in deployed ZK systems have enabled attackers to forge transactions and bypass verification entirely.
We present an automated framework that removes redundant checks while provably preserving soundness. For each candidate removal, our tool first checks whether the rest of the circuit, on its own, can still rule out every value the removed check was excluding. Using whole-circuit abstract interpretation, the analysis searches for such alternative justifications and records them in a provenance graph; a check is then removed only when an alternative path through the graph still derives the facts that it is checking. This ensures that the debloated circuit opens no new forging strategy to an adversary. We evaluate circuits spanning MLP, CNN, RNN, and transformer architectures generated by two production frameworks (ezkl and zkml), with up to 25.3 million constraints. Our tool removes up to 48.7\% of constraints and reduces prover time by up to 72.8\%, without weakening security.

---


### 129. [ScopeMamba-YOLO: Widening the Perceptual Scope Inward and Outward for Small Object Detection in Remote Sensing Imagery](https://arxiv.org/abs/2609.10156)

**<font color=#1a73e8>作者：</font>** Junjie Fan, Yijun Mai, Linduo Wei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small object detection in unmanned aerial vehicle (UAV) and remote sensing imagery requires preserving high-resolution detail while modeling long-range context. Adding a stride-4 detection level and removing the stride-32 stage benefits tiny targets but weakens peripheral spatial support, whereas directly inserting selective scanning into the main feature path can interfere with weak local cues. We propose ScopeMamba-YOLO, built around an off-path, zero-gated selective-scanning principle that decouples contextual modeling from the convolutional stream. The principle is instantiated by a Cascaded Global-Context Module (CGCM) in the backbone and a Selective-Scan PAN (SS-PAN) in the neck. An Adaptive Multi-scale Strip (AMS) Block reduces the cost of high-resolution feature extraction, while a Scale-Adaptive DFL (SA-DFL) head reallocates distributional support and regression capacity across scales with only 0.008M additional parameters. Controlled experiments show that matched main-path selective scanning reduces mAP50 by 0.98 pp, whereas off-path CGCM improves the final configuration by 0.67 pp over the three-seed no-CGCM mean; operator controls indicate that this gain is not explained by auxiliary branch capacity alone. ERF analysis further shows that the complete context pathway increases the peripheral energy ratio from 0.008 to 0.090 at stride 8. On VisDrone-2019, ScopeMamba-S achieves 50.8% mAP50 with 3.57M parameters, exceeding YOLOv8s by 10.8 pp while using 32% of its parameters; ScopeMamba-M reaches 52.6% mAP50 with 6.48M parameters. Consistent improvements are also observed on AI-TOD, especially for very-tiny and tiny objects.

---


### 130. [CoGe-GCD: Reframing Generalized Category Discovery with Compositional Generalization](https://arxiv.org/abs/2609.10158)

**<font color=#1a73e8>作者：</font>** Luyao Tang, Jiewei Zheng, Kunze Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generalized Category Discovery (GCD) assigns unlabeled instances, mixed with labeled data, to known or novel categories, requiring human-like compositional reasoning: reusing primitives learned from known classes and deciding when new combinations imply new categories. Existing GCD methods operate on unstructured token features and struggle to extrapolate to novel compositions. We propose CoGe-GCD, which rethinks GCD through compositional generalization with two coupled stages. (i) Compositional Perception structures patch tokens by mapping them to a small vocabulary of primitives and refining token embeddings via competitive token-primitive assignment and information passing, yielding coherent groups for discovery. (ii) Generalizing Induction exploits the induced geometric structure and applies a structure-preserving calibration over spatial relations, maintaining probabilistic semantics while improving extrapolation to unseen primitive combinations. CoGe-GCD is implemented as an inductive-bias module between backbone and projection head, without modifying heads or losses, and can be plugged into diverse GCD frameworks. On standard benchmarks, it consistently improves all-class accuracy, unknown-class number estimation, and geometric quality, with marginal computational overhead. Code is available at this https URL.

---


### 131. [An Exponential Deterministic--Randomized Gap in ERM-Oracle Complexity for Thresholds on an Unknown Order](https://arxiv.org/abs/2609.10196)

**<font color=#1a73e8>作者：</font>** Xuan Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attias, Hanneke and Ramaswami (NeurIPS 2025) asked whether randomization provably reduces the oracle calls needed for online learning when the class is accessible only through an oracle. We study the instance they singled out: transductive online learning of thresholds on an unknown total order of T instances, with a consistency-type ERM oracle that returns a full concept consistent with a queried labeled set (or reports non-realizability). Our main result is a separation for a fixed natural oracle. When the oracle is the minimal-prefix rule (or the maximal-prefix rule), every deterministic learner makes M mistakes and Q calls with $M+Q\ge T-\varepsilon$ on some instance ($\varepsilon\in\{0,1\}$, according to whether the empty prefix is a concept), and the constant is exact; hence $O(\log T)$ mistakes cost $T-\varepsilon-O(\log T)$ calls, whereas that paper's randomized learner achieves $O(\log T)$ expected calls and mistakes under the same rule. The randomized order is optimal: on an explicit hard distribution under the minimal-prefix rule, every learner has expected mistakes at least $((T+1-\varepsilon)\,128^{-\mathbb{E}[Q]}-1)/2$, so $\Omega(\log T)$ expected calls are necessary for polylogarithmic mistakes. The separation is governed by the oracle's selection rule, not by the class alone: for a legal feasible-median ERM rule a deterministic learner achieves $O(\log T)$ calls and mistakes, while a global-median rule again forces linear total cost. The same linear bound holds when the oracle's answers are chosen adversarially and then frozen into a memoryless oracle. We add partial tradeoff results for fixed query budgets (the middle regime is open) and an interface contrast: with only a weak consistency oracle, returning a realizability bit, both deterministic and randomized learners need $\Theta(T)$ calls.

---


### 132. [Politics of Feelings: Emotional Expression and Legislative Effectiveness in the U.S. Congress](https://arxiv.org/abs/2609.10198)

**<font color=#1a73e8>作者：</font>** Segun Aroyehun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotions are a pervasive feature of political communication, yet existing research has focused primarily on describing patterns of emotional expression rather than examining whether they are associated with consequential legislative outcomes. We address this gap by investigating the expression and correlates of discrete emotions in more than 1.7 million speeches delivered in the U.S. Congress between 1973 and 2024. Using a transformer-based emotion classifier, we measure eight discrete emotions: anger, fear, disgust, sadness, joy, enthusiasm, pride, and hope. We examine how these emotions vary over time, across policy topics, legislator characteristics, and their relationship with legislative effectiveness. We find that congressional speeches are becoming emotionally expressive over time. Emotional expression also varies systematically across policy domains and ideological positioning of legislators. Notably, the relationship between emotional expression and legislative effectiveness depends on the specific emotions expressed: enthusiasm and pride are positively associated with effectiveness, whereas anger exhibits a negative association. Emotional valence and emotional diversity are positively associated with legislative effectiveness, while emotional intensity is negatively associated with legislative effectiveness. These findings demonstrate that computationally derived measures of discrete emotions can provide insight into affective dimensions of legislative speeches and facilitate our understanding of how legislators communicate, interact, and perform within democratic institutions.

---


### 133. [Seeing the Voice, Preserving the Self: A Participatory Design Approach to Deaf-Centric Text-to-Speech](https://arxiv.org/abs/2609.10199)

**<font color=#1a73e8>作者：</font>** Shela Atemnkeng, Patrick Boudreault, Paige DeVries 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We describe a participatory design approach toward developing Deaf-centric text-to-speech (TTS) technologies. While TTS is growing rapidly in the mainstream, it has received little attention to date in the deaf and hard of hearing (DHH) technology space. Critical problems have remained unaddressed for DHH users, including the ability to manipulate tone, emotions and delivery via non-auditory means. Verifying that the generated speech matches intent and is appropriate for a given situation without having to listen to it is another challenge. Respecting cultural and identity factors in the generated speech is also important. This work explores the design space with DHH participants through two focus groups, three co-design sessions, and four one-on-one early-stage design evaluation sessions. Participants included people both familiar and unfamiliar with TTS, as well as DHH content creators. We describe key findings, design ideas, results, and implications for future Deaf-centric TTS development. We also identify unmet technology requirements that pose barriers to adoption of Deaf-centric TTS technology.

---


### 134. [Robust Beam Prediction for V2X Networks with Multi-Modal Sensing](https://arxiv.org/abs/2609.10200)

**<font color=#1a73e8>作者：</font>** Chen Shang, Dinh Thai Hoang, Diep N. Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Integrated sensing and communication (ISAC) provides a promising foundation for beam prediction in future vehicle-to-everything (V2X) networks. However, existing sensing-assisted beamforming methods still rely heavily on radio-frequency sensing, which may become unreliable in complex vehicular environments. Meanwhile, the growing availability of heterogeneous sensors, such as cameras and LiDAR, offers new opportunities to improve beam prediction through richer environmental perception. Motivated by this, this paper proposes a multi-modal beam prediction framework for V2X networks. Specifically, we develop BeamTransFuser, a hierarchical Transformer-based architecture that progressively fuses camera, LiDAR, radar, and GPS observations for robust beam prediction. In addition, to handle possible missing modalities in practical deployment, we introduce a generative module that reconstructs missing modality features from the available observations. Experimental results on a real-world multi-modal V2X dataset show that the proposed framework consistently outperforms representative baselines, while the generative module further improves robustness under incomplete sensing conditions.

---


### 135. [Through the Looking Glass: Directly Reading and Writing Transformers](https://arxiv.org/abs/2609.10210)

**<font color=#1a73e8>作者：</font>** Mark Oskin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How many of a transformer's components decide a token? Counted by the absolute value of each unit's and channel's contribution to the logit, one prediction rests on thousands to hundreds of thousands of them. But contributions are signed, and across eighteen models the mass pushing away from the predicted token is a median of seven times the mass carrying it. Divide by the net and the count is dozens: on the baseline, 53 components carry ninety percent of a prediction, 13 it cannot survive losing, and 8 suffice to produce it alone. Across twelve models trained elsewhere, 124M to 7B parameters, the sufficient set runs from two components to sixteen, and what a prediction draws on, followed all the way back, is one to three percent of the model, a share that does not grow with size. Three quarters of a layer's update is a fixed linear map of the state it received.
Everything is read from the model's own parameters and activations, with nothing trained or fitted, and it names a component on both sides: what it writes, from the predictions it drives, reaching close to half of every model; what it reads, from its weights in the frame of its own layer, at 58.9 percent above chance over its eight strongest inputs. Sorting the remainder by upstream source yields grammatical categories the embedding cannot see.
A name can be acted on. An association the model does not hold installs into one spare unit, key and value read from the weights, for a quarter of a percent of held-out loss, a fortieth of what a rank-one update costs. An installed attention head and a unit two layers above it make an edit fire only where a token occurred earlier in the context, and a unit the model trained for itself is driven from two layers upstream, 86 percent of the effect passing through it. An order-preserving activation puts a unit's inputs at the instrument's ceiling, at the price of a two-part install.

---


### 136. [Hierarchical and Permutation-Invariant Feature Transformation Learning via Policy-Guided Embedding Search](https://arxiv.org/abs/2609.10225)

**<font color=#1a73e8>作者：</font>** Rui Liu, Tao Zhe, Yanyong Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feature transformation improves predictive performance on tabular data by constructing informative abstractions from raw features. Recent generative approaches encode transformation knowledge into continuous embedding spaces for efficient exploration of candidate strategies, but face three key limitations: (1) overlooking hierarchical relationships between low-level features, operations, and high-level abstractions; (2) enforcing order-sensitive embeddings on inherently permutation-invariant transformation sequences, thereby introducing systematic bias; and (3) relying on gradient-based search, which is ill-suited to non-convex transformation spaces. We propose a framework with two complementary components. First, a permutation-invariant hierarchical module captures interactions across features, operations, and abstraction levels, with a self-attention pooling mechanism that maps semantically equivalent structures to consistent embeddings aligned with downstream performance. Second, a policy-guided multi-objective reinforcement learning strategy initializes the search from empirically strong seeds and jointly optimizes predictive accuracy and transformation efficiency. Extensive experiments on diverse tabular benchmarks demonstrate the effectiveness and robustness of our framework against strong baselines. Our code and data are publicly available at: this https URL.

---


### 137. [Meme Coin Factories: Uncovering Large-Scale Manipulations on pump.fun](https://arxiv.org/abs/2609.10246)

**<font color=#1a73e8>作者：</font>** Nicolas Szwajcok, Taro Tsuchiya, Enze Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Once complex, creating and deploying a new cryptocurrency has become trivial. Coin launchpads now allow users to generate a new coin with merely a few clicks, at a minimal cost. Launchpad popularity has grown in tandem with the rise of "meme coins," which usually do not offer any novel technological properties and are purely created for fun. The most prominent coin launchpad, this http URL, has gained significant traction, grossing over 100 million USD in daily trading volume. The mass adoption of coin launchpads, however, also enables strategic actors to easily manipulate trading signals, unbeknownst to inexperienced traders who then buy certain coins, and enable these strategic actors to profit from rapid and unsustainable price increases ("pumps"). To identify such manipulations at scale, we conduct a large-scale study of this http URL, collecting information on all 15 million coins launched in the last two years, and performing analysis on large, random samples of transaction data. We identify five classes of manipulation strategies: 1) wash trading, 2) creator address obfuscation, 3) coordinated sell, 4) copycat coins, and 5) social media manipulation. We find that strategic actors often bypass the platform interface and implement these strategies in a highly automated and low-latency fashion, by interacting directly with the blockchain. We further uncover the existence of "Market-Manipulation-as-a-service (MMaaS)," third-party tools that enable users to perform these manipulations without any technical expertise. We conclude by devising mitigations and proposing recommendations for traders, this http URL, wallets or chain scanners, software development platforms, and regulators.

---


### 138. [Are Unreachable Nodes Truly Safe? Fully Eclipsing Monero's P2P Network!](https://arxiv.org/abs/2609.10260)

**<font color=#1a73e8>作者：</font>** Ruisheng Shi, Jiaqi Zeng, Lina Lan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Eclipse attacks isolate a blockchain node by monopolizing its network connections. Existing attacks on Monero (NDSS'25), Bitcoin (USENIX'15/21, S&P'20) and Ethereum (WWW'26) implicitly assume that the adversary can establish inbound connections, thereby excluding a large and practically dominant class of nodes: \textit{unreachable nodes} operating behind NATs. Such nodes are widely believed to enjoy stronger networks. We challenge this assumption and show that unreachability does NOT imply the expected resilience!
We present the first eclipse attacks tailored to unreachable nodes in Monero's P2P network. Our attacks require no inbound access to the victim. Instead, they first poison the peerlist of reachable nodes, which subsequently act as propagation relays to contaminate unreachable nodes' whitelists. The adversary then exploits Monero's built-in outbound connection refresh logic to evict benign neighbors and eventually monopolize all outbound connections. We instantiate this strategy in two attacks: Nyx, which targets long-running unreachable nodes and achieves a complete and persistent eclipse through network-wide poisoning; and Moros, a stealthier attack that exploits the bootstrapping phase to rapidly eclipse newly joined unreachable nodes.
We ethically evaluate both attacks. Nyx is validated via large-scale simulations on a Monero network constructed using the SEED Emulator, while Moros is demonstrated on the Monero mainnet against controlled targets. Our results show that unreachable nodes can be reliably driven into stable, long-lived eclipse states. We also propose countermeasures.

---


### 139. [When Fusion Fails: Corruption-Aware Rebalanced Fusion for Multi-Modal Medical Image Segmentation](https://arxiv.org/abs/2609.10261)

**<font color=#1a73e8>作者：</font>** Yuchen Pei, Xiaoyu Hu, Yixiong Zou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal medical image segmentation leverages complementary diagnostic information, yet fusion can underperform single-modality baselines when spatially aligned inputs differ in quality. Here, "corruption" primarily denotes resolution-induced degradation rather than misalignment or complete modality absence, while synthetic noise is evaluated only as an auxiliary setting. We identify a critical optimization-inference inconsistency: degraded modalities can receive weak training updates yet substantially affect predictions, indicating active interference with fusion. We attribute this failure to resampling-induced feature corruption and optimization bias, where noisy features propagate through skip connections and encourage unreliable modality selection. We therefore propose CoReFuse-Med, a Corruption-aware Rebalanced Fusion framework that suppresses corruption during feature transmission and rebalances modality contributions during high-level fusion. Experiments on EPVS, BraTS, and WMH, including multiple Z-axis slice-retention ratios and an auxiliary noise test, demonstrate improved accuracy and robustness under modality-quality discrepancies. Our code is available at this https URL.

---


### 140. [Training Trajectories Determine Circuit Removability in Annealable Soft-Prior Transformers](https://arxiv.org/abs/2609.10287)

**<font color=#1a73e8>作者：</font>** Zonglin Yang, Ziming Zhao, Wei Tang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Soft positional priors can help small Transformers learn retrieval circuits, but it is unclear whether the resulting circuits remain functional once the prior is removed. We test this with an annealable soft-prior Transformer whose attention biases can be learned, faded, or zeroed during training and evaluation. On associative recall, unforced models perform well with the prior active ($0.772 \pm 0.020$) but collapse at zero gate ($0.095 \pm 0.009$). Smooth fade-to-zero training preserves high zero-gate accuracy ($0.734 \pm 0.028$), whereas forced-zero training, hard switching, and post hoc continuation fail to recover the same effect. The pattern also appears on Markov induction. Linear regression ICL provides a boundary case because zero-gate training can learn that task directly. Mechanistic traces show that circuit consolidation occurs after the gate reaches zero, even though the responsible heads vary across seeds. These results suggest that circuit removability in small discrete retrieval tasks depends on the training trajectory, not just the final architecture.

---


### 141. [An Empirical Analysis of ReDoS Vulnerabilities and ReDoS Detection Tools](https://arxiv.org/abs/2609.10294)

**<font color=#1a73e8>作者：</font>** N'Zolieh Ismaël Mahassadi, Raphaël Khoury, Justin Vallé 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> ReDoS vulnerabilities are a type of denial of service software weakness that occurs when a regex is used to validate user-supplied input. In some cases, the regex matching process can take exponential time, leading to a denial of service. In this study, we examine and compare the effectiveness of five publicly-available regex detection tools, and one regex correction tool, using three datasets. We further perform an empirical analysis of all ReDoS vulnerabilities reported to the NVD database in order to understand how they differ from non-ReDoS vulnerabilities and glean insights about this type of weakness. We find that ReDoS vulnerabilities are becoming more prevalent and are much more likely to be exploited than non-ReDoS vulnerabilities. We further find that detection tools exhibit substantial disagreement on whether or not a given regex is vulnerable.

---


### 142. [The Semantic Bottleneck: Leveraging Semantic Representations for Non-Invasive Speech Decoding](https://arxiv.org/abs/2609.10296)

**<font color=#1a73e8>作者：</font>** Gilad D. Landau, Dulhan Jayalath, Oiwi Parker Jones  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Non-invasive speech decoding remains constrained by the low signal-to-noise ratio of neural recordings, which makes fine-grained reconstruction of phonemes or individual words difficult. Motivated by neuroscientific evidence that high-level semantic representations are distributed across cortical regions and evolve over slower temporal scales, we hypothesize that semantic content may provide a more suitable target for non-invasive decoding than low-level acoustic or lexical features. We introduce Brain2Semantics2Text, a method that reconstructs text through an intermediate semantic embedding space. Our model maps sentence-level MEG responses into a semantic manifold and then inverts the predicted embeddings into natural language. This semantic bottleneck enables recovery of high-level meaning without word-level alignment. We describe the core principles of the approach, its implementation, and the strategies used to mitigate the challenges of learning a reliable neural-to-semantic mapping. Finally, we compare against prior non-invasive Brain2Text methods and show improved sentence-level results.

---


### 143. [TRACE: Trajectory-robust Admission with Evidence Ordering for Efficient GUI Agents](https://arxiv.org/abs/2609.10297)

**<font color=#1a73e8>作者：</font>** Yuhao Wang, Mu Qiao, Xindong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GUI agents accumulate high-resolution screenshots as the trajectory unfolds, increasing inference latency and memory usage. Training-free visual token pruning can reduce this cost, but cache reuse introduces a fundamental constraint. Once tokens are discarded, the corresponding visual evidence cannot be recovered without re-encoding. Pruning therefore becomes an \textit{irreversible admission decision} that must remain useful for unknown future targets while preserving coverage of operable regions under tight budgets. To address these challenges, we propose \textbf{\method{}}, a training-free framework for \emph{\textbf{T}rajectory-\textbf{r}obust \textbf{A}dmission and \textbf{C}overage-aware \textbf{E}vidence ordering}. Specifically, we combine a query-independent layout-derived interaction prior with instruction relevance and feature novelty to rank visual evidence according to both potential future utility and diversity. Then, we reserve part of the budget for native visual tokens distributed across the screen, repairing missing spatial coverage without breaking the ordering. Together, these mechanisms produce a nested token order, allowing retained visual evidence to shrink monotonically across budgets while remaining reusable throughout the trajectory. Finally, our monotone KV contraction incrementally contracts retired frames into compact session state, avoiding repeated visual encoding or pruning. Extensive experiments across six GUI benchmarks and diverse models verify the effectiveness of our proposed \method{} under tight budgets. The source code will be released.

---


### 144. [Learning Intrusion Response Strategies for OT Systems](https://arxiv.org/abs/2609.10298)

**<font color=#1a73e8>作者：</font>** Duc Huy Le, Rolf Stadler  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyberattacks against Operational Technology (OT) systems, which monitor and control industrial processes, pose an increasing threat to essential societal services. For this reason, developing automated intrusion response strategies is highly important. In this paper, we present a formal model of an OT intrusion response use case using the POMDP framework. It includes a realistic model of partial observability that is based on traffic measurements. This approach allows us to develop tractable, learning-based solution methods for automated intrusion response, which are based on PPO. We evaluate the obtained response strategies on an emulated OT system and find that they are effective against several types of MITRE attacks for the studied use case.

---


### 145. [A Dominant Diffuse Phase in the Sparse Autoencoder Phase Diagram](https://arxiv.org/abs/2609.10299)

**<font color=#1a73e8>作者：</font>** Alexis D. Plascencia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) are increasingly used to recover interpretable features from neural-network activations, yet systematic feature co-occurrence can cause distinct features to be absorbed or merged. The MAIS-O43 open problem proposes a controlled experiment to characterize when recovery of a true synthetic dictionary gives way to feature merging as the nesting fraction $\gamma$, sparsity penalty $\lambda$, and dictionary size $M$ vary. We implement the specified protocol and evaluate 200 independently initialized fits across ten of the 165 grid cells. We observe zero full-dictionary recoveries and zero merges. Instead, every run converges to a reproducible diffuse phase: reconstruction is nearly perfect, but learned atoms typically remain far from the true features (median best cosine 0.5-0.7 against a 0.95 recovery criterion) and learned codes are an order of magnitude denser than the ground truth. This behavior persists under robustness checks and across the full 165-cell grid using standard minibatch Adam (3,300 additional fits). Since the global optimum of the exact sparse-coding objective is known to merge nested features in the two-feature case, these results suggest that trained SAEs need not reach the corresponding minima, and that the phase diagram of trained models may differ fundamentally from that of objective minimizers.

---


### 146. [SynThermFace: Amplifying Limited Paired Data for Visible-Thermal Face Recognition via Synthetic Data Generation](https://arxiv.org/abs/2609.10303)

**<font color=#1a73e8>作者：</font>** Anjith George, Adam Unal, Sebastien Marcel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face recognition (FR) is a widely used modality for biometric authentication, but conventional models rely on visible-spectrum imagery and degrade when high-quality RGB images cannot be captured. Cross-spectral face recognition addresses this limitation by matching visible images with other modalities such as thermal imagery, enabling more reliable performance in low-light, nighttime, and unconstrained conditions. However, progress is limited by the scarcity of paired visible-thermal data, which is difficult and costly to collect at scale. We propose SynThermFace, a framework that amplifies limited real visible-thermal supervision into larger paired adaptation datasets for cross-spectral face recognition. A diffusion model is first adapted using a limited set of paired visible--thermal images and then used to generate large-scale paired visible--synthetic thermal data from existing real or synthetic visible face datasets. The generated pairs are used to adapt a pretrained visible-spectrum face recognition model into a CFR model. Unlike synthesis-based approaches that require image translation at test time, the proposed method shifts generation to the training stage and performs inference with a single forward pass through the adapted recognition model. Under the same MCXFace real-pair protocol, PACT improves over the evaluated CFR adaptation baselines, isolating the effect of the proposed adaptation objective. Training PACT on larger generated paired datasets provides additional improvements over both the unadapted model and the real-pair PACT configuration. Cross-database evaluation on the Tufts dataset provides evidence that the learned representation transfers to an unseen database. The source code and trained models will be made publicly available.

---


### 147. [View-Structured Conformal Prediction for 3D Gaussian Splatting](https://arxiv.org/abs/2609.10307)

**<font color=#1a73e8>作者：</font>** Junzheng Chu, Bin Pan, Zhenwei Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) renders novel views in real time, but an uncertainty heatmap does not certify that a rendered view meets a certain prediction coverage. We treat novel-view synthesis as structured regression and ask that, with probability at least $1-\alpha$, RGB prediction boxes cover at least a $1-\beta$ fraction of pixels in a new view. We propose View-Structured Conformal Prediction (VSCP). It splits the pre-calibration scale into a spatial shape from the renderer and a transferable view-difficulty factor, which predicts the smallest view-wise multiplier that shape needs. A held-out quantile over views (View-CP) then gives finite-sample validity even when transferring to new scenes. The same factorization makes the analysis exact: a conformity score is the ratio of oracle to predicted view difficulty, and excess width separates into a test-side and a calibration-side term. Across 13 real scenes, pixel-pooled calibration reaches 89.9\% marginal pixel coverage but only 61.4\% view-event coverage at a 90\% target, while View-CP reaches 91.7--92.0\%. At matched coverage VSCP cuts width by 22.1\% against a constant scale, and matches a ten-model ensemble's 21.0\% reduction using only one model per scene and four rather than ten rasterization passes per query. VSCP also improves on the closest single-model baseline, the 3DGS-U field, by 4.7 points ($p=0.0225$). The view predictor transfers from bounded source families to all nine unbounded Mip-NeRF~360 scenes. There the full scale beats the constant scale with 20.7\% width saving on all nine scenes. It also keeps an 18.3\% saving under a different densification backbone and runs at 216--280 FPS on an RTX~4090.

---


### 148. [One Loop, Two Gains: Can Active Learning win the Lottery for Free?](https://arxiv.org/abs/2609.10311)

**<font color=#1a73e8>作者：</font>** Benedikt Tscheschner, Eduardo Veas, Marc Masana  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The lottery ticket hypothesis posits the existence of winning tickets: sparse subnetworks that, when trained in isolation from their original initialization, match the accuracy of the full dense network. The predominant method for discovering such tickets, iterative magnitude pruning, alternates pruning with full retraining from scratch until convergence over many cycles. Similarly, deep active learning also retrains a model from scratch after each acquisition round as new labels become available. Despite this shared reliance on iterative retraining with a substantial computational overhead, the two paradigms have been studied separately. We observe that the iterative training loop inherent to pool-based active learning already provides the exact computational structure that iterative magnitude pruning exploits, and propose Improve & Prune (I&P), a method that integrates magnitude pruning into each active learning retraining cycle at practically no additional cost. This raises a key empirical question: can iterative magnitude pruning produce winning tickets under the non-stationary data regime of active learning? We investigate this question across multiple acquisition functions, architecture families, and image classification datasets, including an active fine-tuning scenario. Our results demonstrate that I&P yields sparse, deployable models at each active learning iteration. Those match the accuracy of their dense counterparts at sparsities up to 95%, effectively obtaining winning tickets as a byproduct of the active learning pipeline. These per-iteration sparse models can address two computational bottlenecks - per-round model retraining and acquisition scoring over the unlabeled pool - that currently prevent the practical adoption of DAL on large architectures and large unlabeled pools.

---


### 149. [Decoupled Self-Forcing Distillation for Streaming Talking Head Generation](https://arxiv.org/abs/2609.10317)

**<font color=#1a73e8>作者：</font>** Yanru An, Ruiyan Wang, Wenwu Wei 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming talking-head generation produces each frame as its driving audio arrives, yet fidelity and efficiency have so far pulled in opposite directions: end-to-end methods condition a video diffusion model on audio directly and achieve high quality but only at large scale, while cheaper two-stage methods generate an intermediate motion representation and trail in fidelity. We argue the cost of the former lies in the target of fusion: the video latent is dominated by identity, appearance and background, none of which audio bears on, so coupling audio to every pixel blurs detail and wastes capacity. We instead fuse conditions in a low-dimensional identity-disentangled motion space, routing audio and motion captions by their temporal granularity, and generate motion latents with a small causal autoregressive transformer that a pretrained diffusion renderer turns into video. Conditions thus control video transitively, and high fidelity no longer requires a large backbone. Streaming this decomposition needs both models to be causal, and the exposure-bias problem could be solved by self-forcing given a bidirectional teacher. But there is no such teacher in motion space. Our decoupled self-forcing distillation resolves both models under one frozen teacher: conditioned on motion, it distills the renderer into a block-causal student; unconditionally, it scores rendered rollouts against real videos, supervising motion by the video it produces. This lifts the fidelity ceiling from the motion generator onto the stronger renderer. The two models run as parallel causal streams, reaching 15.4 FPS at 1.3 s latency with no quality degradation.

---


### 150. [Geometry Without Coordinates: LiDAR Diffusion as a 3D Feature Bridge](https://arxiv.org/abs/2609.10322)

**<font color=#1a73e8>作者：</font>** Samed Doğan, Nico Leuze, Alfred Schöttl  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transferring the rich priors of large 2D foundation models to sparse 3D LiDAR remains challenging, as training native 3D foundation models at comparable scale is limited by data and annotation scarcity. We introduce a LiDAR-conditioned diffusion model trained on pseudo-labels from off-the-shelf 2D foundation models. The model supports multiple output modalities, including depth, semantic segmentation and instance prediction, selectable via a textual task prompt. Because the model is conditioned on LiDAR, both its outputs and its intermediate UNet features can be projected back onto the input point cloud, enabling analysis of a 3D representation learned entirely under 2D supervision. We study this representation directly in point-cloud space, explicitly excluding raw spatial coordinates to isolate feature content from projection geometry. Linear probes recover up to ~23% Mean Intersection over Union (MIoU) on 3D semantic classes, compared to ~3.5% for a matched Gaussian-noise control, indicating substantial non-trivial structure. Pairwise cosine similarity across modality-specific feature streams reveals a layered organization. Early encoder layers remain weakly aligned across modalities while individually decodable, intermediate layers converge toward a shared representation, and decoder layers re-specialize toward task-specific outputs. These findings indicate that LiDAR-conditioned diffusion models can induce structured 3D representations from 2D supervision alone, with a modality-dependent manifold that locally unifies near a shared bottleneck. This positions diffusion as a viable mechanism for transferring large-scale 2D priors into sparse 3D domains.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-176](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
