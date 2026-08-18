# 📦 其他研究 | 2026年08月19日

> 本类共 **435** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-435](./part-09.md)

---

### 301. [Unifying Graph Neural Networks Through a Common Layer Equation](https://arxiv.org/abs/2608.16097)

**<font color=#1a73e8>作者：</font>** Sai Karthik Navuluru, Siddhartha Shankar Das, Bo Ni 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks are commonly described through family-specific equations whose notation obscures shared computations and structural differences. We introduce a common layer equation that represents covered architectures through seven components: an update domain, channel set, propagation bank, per-channel message maps, channel-fusion operator, ego/residual map, and update map. The central factorization separates where information moves, encoded by the propagation bank, from what moves, encoded by the message maps. Function-valued fillings extend the same equation across local message passing, attention, spectral filtering, global communication, relation-specific channels, higher-order domains, and geometric messages.
We make this unification explicit and checkable through worked reductions of canonical layers and component assignments spanning seven nonexclusive architectural families. A fixed slot discipline assigns operations by computational role and defines the framework's coverage boundary. The decomposition also yields component-level theoretical insights: under endpoint-local messages and node-local updates, operator support bounds one-layer dependencies, and one-layer global mixing requires a full effective operator row under the stated hypotheses.
The resulting framework organizes more than 200 architectures in a common design space, enables component-wise comparison and generation of structurally consistent architectures, and connects propagation choices to oversmoothing, oversquashing, heterophily, and expressivity. It further exposes the empirical inverse problem of mapping measurable graph and task properties to validated component choices.

---


### 302. [AsyTO: Asymmetric Temporal Operator for Parameter-Efficient Multivariate Time Series Forecasting](https://arxiv.org/abs/2608.16098)

**<font color=#1a73e8>作者：</font>** Xiachong Lin, Du Yin, Hao Xue 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time-series forecasting faces a structural dilemma: sharing one temporal predictor across variables is parameter-efficient but forces heterogeneous variables through an identical history-to-future map, whereas learning an independent predictor per variable restores flexibility at a cost that grows with the product of variable count, context length, and horizon. We argue that this dilemma dissolves once the object being compressed is the forecasting operator rather than the observed series. Auditing per-variable linear history-to-future maps across standard benchmarks, we find that a phase-locked seasonal component paired with a compact residual operator outperforms a dense phase-blind reference in most audited settings. The residual transport is also directional: lag-invariant alternatives consistently underperform asymmetric history-to-future maps. Guided by this structure, we propose AsyTO, an Asymmetric Temporal Operator that factorizes the tensor of per-variable operators into shared but distinct history-reading and future-writing temporal modes with per-variable mode-wise gains, complemented by a low-rank periodic prototype and a cycle-separable factorization of the temporal modes. Each forecast reads only its own variable's history, so parameters and compute grow linearly in the number of variables. Across eleven benchmarks and multiple forecast horizons, AsyTO attains the best lightweight error in 30 of 44 dataset-horizon settings, locating at the accuracy-compute Pareto frontier.

---


### 303. [TISC: A Text-Driven Image Semantic Communication System for Faithful Reconstruction](https://arxiv.org/abs/2608.16100)

**<font color=#1a73e8>作者：</font>** Feifan Zhang, Yuyang Du, Xiaoyan Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative image semantic communication converts an image into a text description and then performs text-to-image reconstruction at the receiver via diffusion-based generative models. This paradigm has attracted broad attention due to its extremely low bandwidth cost. However, existing methods still face two critical bottlenecks across image-to-text (I2T) semantic extraction at the transmitter and text-to-image (T2I) semantic reconstruction at the receiver: (i) semantic loss and distortion in I2T, where holistic image descriptions may omit fine-grained object attributes and spatial-position information, causing the generated text to deviate from the original image semantics; and (ii) insufficient semantic faithfulness in T2I, where even with the same semantically faithful text description, different initial noise settings may lead diffusion-based reconstruction to produce images with different levels of semantic consistency with the original image. These issues jointly limit the semantic faithfulness of image reconstruction. To address them, we propose TISC, a text-driven image semantic communication framework tailored for faithful reconstruction. TISC incorporates two key designs: (1) Tree-Structured Attribute Semantic Extraction (TSASE), which decomposes semantic extraction into global scene, background, and object-level attribute descriptions, covering spatial position, shape/pose, color, material, and other physical attributes for each detected object; and (2) an Initial Noise Optimization (INO) mechanism, which selects an initial noise seed at the transmitter according to a comprehensive similarity score that jointly considers visual and semantic consistency. Experiments on multiple datasets show that TSASE improves object-position recovery and semantic description faithfulness, while the INO parameter study supports the adopted configuration for noise selection.

---


### 304. [Beyond Similarity Matching: Structured Reasoning for Open-Vocabulary Referring Segmentation in 3DGS](https://arxiv.org/abs/2608.16103)

**<font color=#1a73e8>作者：</font>** Yizhao Wang, Xinfa Wang, Jingbo Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary referring segmentation in 3D Gaussian Splatting (3DGS) requires a neural model to select Gaussian primitives according to free-form language expressions. Existing 3DGS-based methods usually rely on global text-region similarity, which is weak for queries involving attributes, reference objects, spatial relations, and fine-grained parts. This often causes target-reference confusion, granularity mismatch, part-whole leakage, and relation violations. We propose QAGaussian, a query-adaptive neural reasoning framework for language-guided Gaussian primitive selection. QAGaussian first learns query-conditioned multi-scale Gaussian slots as differentiable candidates whose receptive fields are shaped by the input expression. It then builds a relation-aware slot graph with language-conditioned edge weighting to propagate target-reference, attribute, part-whole, and contextual evidence. A granularity-adaptive router softly combines region-level, object-level, part-level, attribute-aware, and relation-aware mask branches, followed by relation-constrained refinement for spatial, part-whole, attribute, and geometric consistency. QAGaussian is pretrained only on Mosaic3D-5.6M for Gaussian-text alignment and evaluated on independent benchmarks without target-dataset fine-tuning. It achieves 47.2 Avg. mIoU and 63.2 Avg. F1, outperforming the strongest 3DGS referring baseline by 2.7 mIoU points and 2.9 F1 points. It also improves Part-mIoU from 38.6 to 43.4, Rel-mIoU from 44.4 to 50.8, and reduces target-reference confusion from 10.8 to 7.4. These results demonstrate that query-conditioned slot learning, relation-aware graph reasoning, and adaptive routing provide an effective neural modeling strategy for open-vocabulary referring segmentation in 3DGS. The code is available at this https URL.

---


### 305. [SUGFW+: An Uncertainty-guided Feature Weighting Framework for Cold Start Active Adaptation of SAM in Medical Image Segmentation](https://arxiv.org/abs/2608.16110)

**<font color=#1a73e8>作者：</font>** Xiaochuan Ma, Ning Zhu, Jia Fu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cold Start Active Learning (CSAL) is important in improving the performance of a medical image segmentation model with low annotation budget by querying a small subset for annotation from an unlabeled training set. Existing CSAL methods typically rely on inefficient dataset-specific Self-Supervised Learning (SSL) to map the unlabeled images into a feature space for sample selection. Recently, the advent of foundation models such as the Segment Anything Model (SAM) offer a promising alternative as the pre-trained model can provide strong generalizable feature embeddings, and allow high performance in downstream tasks after fine-tuning (adaptation). However, how to systematically exploit SAM's inherent embeddings for cold-start sample selection during adaptation with low annotation budget remains underexplored. To address this, we propose an extended SAM-based Uncertainty-guided Feature Weighting (SUGFW+) framework for CSAL and adaptation of SAM. Specifically, it leverages the SAM for Patch-level Feature and Uncertainty Calculation (PFUC), and introduces a Patch-based Global Distinct Representation (PGDR) module that aggregates patch-level embeddings into highly discriminative, uncertainty-aware image-level features. These features are then utilized by a Greedy Selection with Cluster and Uncertainty (GSCU) strategy to combine diversity and uncertainty during sample selection. Unlike prior CSAL methods that decouple sample selection from model training, SUGFW+ tightly integrates these two stages via an Uncertainty-Prompted Fine-Tuning (UPFT) process of SAM in model training. Extensive experiments on four public datasets demonstrate that SUGFW+ achieves state-of-the-art performance against existing CSAL methods. Code is available at this https URL.

---


### 306. [RetroMPA: A Molecular Property-Aware Auxiliary Framework for Enhancing Retrosynthesis Prediction](https://arxiv.org/abs/2608.16111)

**<font color=#1a73e8>作者：</font>** Mianzhi Liu, Fan Xiao, Zhiliang Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrosynthesis is a cornerstone of drug discovery and organic synthesis. While data-driven deep learning models have shown remarkable progress, they autonomously learn reaction patterns from extensive datasets with limited integration of established chemical knowledge as priors.
To address this limitation, we introduce RetroMPA, a molecular property-aware, post-hoc enhancement module that injects chemical knowledge into the retrosynthesis pipeline. Rather than functioning as an independent SMILES sequence generator, RetroMPA is a broadly applicable, model-agnostic chemical filter designed to recalibrate and optimize the predictive pathways of existing algorithms.
This plug-and-play framework integrates seamlessly with a range of data-driven retrosynthesis methods, enhancing outputs without modifying model architecture or requiring resource-intensive retraining. By leveraging a property-aware latent embedding space, RetroMPA consistently improves top-1 accuracy across eight representative retrosynthesis models by an average of 5.50% on USPTO-50K.
Furthermore, we validate its scalability on the large-scale USPTO-Full dataset, achieving an average improvement of about 2.03% across both template-based and template-free architectures.
Wet-lab experiments provide preliminary support for the practical utility of the framework. These syntheses confirmed viable, previously unreported substrate combinations for classic reaction paradigms---specifically, Suzuki-Miyaura coupling, Bucherer reaction, and Friedel-Crafts acylation---suggesting that RetroMPA can operate beyond mere data fitting. The code is open-sourced at this https URL.

---


### 307. [TokenSTFormer: A Tokenized Spatial-temporal Attention Model for Holistic Motion Analysis in Adolescent Idiopathic Scoliosis Screening](https://arxiv.org/abs/2608.16122)

**<font color=#1a73e8>作者：</font>** Dong Chen, Kenneth M.C. Cheung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adolescent Idiopathic Scoliosis (AIS) is a prevalent spinal deformity in adolescents that, if left untreated, can result in severe health outcomes. Traditional screening methods are limited by subjective interpretation, reliance on professional expertise and low scalability. To address these challenges, we present ScoliGait dataset, which comprises 1,516 gait video clips paired with corresponding X-ray records. We also introduce TokenSTFormer, a novel model that tokenizes spatial and temporal semantics to enhance feature representation and convergence. Our model achieves state-of-the-art performance, surpassing vanilla Vision Transformer encoder across key metrics, including accuracy of 0.79. This study highlights the potential of leveraging holistic motion features derived from gait video and attention-based models for scalable, cost-effective AIS screening, paving the way for future clinical applications in scoliosis detection.

---


### 308. [Multi-Feature Riemannian Hypergraph for Online Test-Time Adaptation of Motor Imagery Brain-Computer Interface](https://arxiv.org/abs/2608.16134)

**<font color=#1a73e8>作者：</font>** Siqi Li, Zhi Li, Tong Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In clinical motor imagery brain-computer interface (MI-BCI) decoding, cross-day transferability and online operation remain two critical challenges. Hypergraphs can improve transferability by capturing higher-order sample relationships, yet existing hypergraph-based methods for online emotion recognition neglect the cross-day benefits of Riemannian geometry widely adopted in EEG transfer learning. To bridge this gap, we propose the Multi-feature Riemannian Hypergraph (MRieHy), a framework tailored for online test-time adaptation in MI-BCI decoding that leverages Riemannian geometry to strengthen cross-day transferability. MRieHy first computes Riemannian means of covariance matrices from cross-day training data to align multi-day distributions. It then constructs a hypergraph over covariance matrices using Riemannian distance, complemented by a second hypergraph over deep features built with cosine similarity. The two hypergraphs are fused via adaptively learned combination weights, jointly optimized with the label projection matrices. During online testing, MRieHy maintains a first-in-first-out buffer of recent samples, performs Riemannian alignment on the buffered data, and decodes with the learned hypergraph. Extensive experiments on a private four-class ECoG dataset and two public four-class EEG datasets validate that MRieHy achieves notable performance gains over state-of-the-art baselines.

---


### 309. [Graph Neural Assisted Actor-Critic for Latency-Efficient Edge Vision System](https://arxiv.org/abs/2608.16142)

**<font color=#1a73e8>作者：</font>** Alam Noor, Luis Almeida, Kai Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> UAV on-board vision systems are widely used for different activities, including monitoring in no-fly zones. In this case, the vision-equipped UAV streams a video to a ground server where an operator assists its activities. The latency of video transmission has a profound impact on the effectiveness of the operator assistance. However, most techniques available for video transmission still incur significant latency costs. In this paper, we propose a graph convolutional neural network-assisted (GCN-Assisted A2C) deep reinforcement learning (DRL) system model to find the optimal pixel-correlated area of a suspicious object. We combine the Lagrangian dual form with gradient descent to prevent lack of convergence and over- and under-penalization constraint violation during latency optimization. The proposed system model sends a sub-group pixel-correlated area of the frame from the UAV to the server rather than the transmission of the whole video frame. The proposed framework utilizes the GCN model to explore hidden representations of feature-correlated groups of pixels. Moreover, the GCN supervises the A2C model, which selects a subgroup to enhance transmission latency, thus supervising the training of UAV actions in A2C. Experimental results show that GCN-assisted A2C reduces video frame transmission latency together with false detection rate in UAV vision systems over other DRL and state-of-the-art models.

---


### 310. [The Right Prior for the Right Deformation: Rethinking Continuous Deformable Image Registration](https://arxiv.org/abs/2608.16146)

**<font color=#1a73e8>作者：</font>** Hengjie Liu, Chushu Shen, Dan Ruan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deformable image registration models implicitly encode deformation priors through their parametrization and optimization. In this work, we conduct a validation study on continuous registration methods to examine how these implicit priors affect performance across different registration tasks. Classic B-Spline transformations impose locality, smoothness, and scale through their control-point structure, whereas recent INR-based methods impose different priors through neural parameterization and optimization. We compare INR-Dense (IDIR), which directly models a dense displacement field using a SIREN-based INR; INR-BSCP (SINR), which predicts B-Spline control points with an INR; D-BSCP, which directly optimizes single-scale B-Spline control points; and MR-D-BSCP, which adds a multiresolution coarse-to-fine scheme. Experiments on inter-subject brain MR registration (OASIS) and intra-subject exhale-to-inhale lung CT registration (DIR-LAB 4DCT) reveal different behavior across deformation regimes. On OASIS, where deformations are moderate but locally complex, D-BSCP matches or slightly outperforms INR-BSCP, suggesting that the B-Spline parameterization accounts for much of INR-BSCP's effectiveness. On DIR-LAB 4DCT, where respiratory motion is larger and more coherent, single-scale B-Spline methods (D-BSCP and INR-BSCP) are less suitable, while INR-Dense and MR-D-BSCP are more effective. Across both tasks, MR-D-BSCP achieves the best performance among the tested continuous parameterizations. These findings highlight that registration accuracy depends strongly on matching the induced deformation prior to the target motion pattern, and support prior-deformation matching as a practical design principle for medical image registration. Our code will be available at this https URL.

---


### 311. [When Single-Dataset Conclusions Fail: A 45-Task Study of Threshold Tuning and Resampling for Imbalanced Classification](https://arxiv.org/abs/2608.16147)

**<font color=#1a73e8>作者：</font>** Diyorbek Musaev  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Class-imbalance handling is routinely evaluated on a single benchmark dataset, and the resulting conclusions are reported as if they were properties of the method. We show this practice is unsafe. On the public Kaggle credit-card fraud dataset, under a leakage-free nested cross-validation protocol in which the decision threshold is selected on a held-out inner validation fold, a plain Random Forest at the default 0.5 threshold attains F1 = 0.861 +/- 0.021, and threshold tuning yields it no benefit (delta-F1 = -0.002). Read alone, this supports an appealing conclusion: for a well-calibrated ensemble, imbalance handling is unnecessary.
We then apply the identical protocol to 45 binary tasks spanning imbalance ratios from 1:1.5 to 1:178 (2,025 model fits, four model families). The conclusion reverses. Random Forest benefits most from threshold tuning across the suite (delta-F1 = +0.101 +/- 0.134), not least, while three other families replicate their fraud-dataset behaviour almost exactly. SMOTE likewise harms the fraud dataset but helps across the suite (mean delta-F1 = +0.076; 138 wins, 39 losses; Wilcoxon p = 2.7e-17).
Two further results. Threshold-tuning benefit is non-monotonic in the imbalance ratio: near zero below 1:5, peaking at +0.120 in the 1:15-1:40 band, declining to +0.045 beyond 1:100 - explaining why the fraud dataset, at 1:577, is an unrepresentative place to study the question. And we reject an intuitive heuristic: validation-set calibration error does not predict tuning benefit (expected calibration error r = -0.087; Brier r = +0.137), so calibration diagnostics cannot tell a practitioner whether tuning is worthwhile. We release the protocol, the 45-task harness, and all per-run metrics.

---


### 312. [FeatureHospital: A Skill-Driven Multi-Agent Framework for Automated Algorithm Customization in Multi-View Multi-Label Feature Selection](https://arxiv.org/abs/2608.16148)

**<font color=#1a73e8>作者：</font>** Junxuan Li, Zhiqi Chen, Yuzhou Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-view multi-label feature selection aims to identify a compact and informative feature subset from heterogeneous views while preserving discriminative information for multiple labels. Existing methods are generally developed from specific modeling perspectives and incorporate mechanisms tailored to particular data characteristics. Designing suitable feature selection algorithms across datasets with diverse and heterogeneous characteristics still relies heavily on expert knowledge and substantial manual effort, imposing considerable time and labor costs that severely hinder the practical adoption of feature selection. To address this problem, we propose FeatureHospital, a Skill-driven multi-agent framework for automated multi-view multi-label feature selection algorithm design. FeatureHospital first diagnoses the target dataset to identify its feature selection issues. Based on the diagnosis, specialist agents equipped with domain Skills then prescribe corresponding optimization strategies and Loss terms for different issues. After that, the resulting prescriptions are reconciled to remove overlaps and resolve conflicts before being integrated into a compact dataset-specific objective. Finally, the constructed objective is optimized to select the final feature subset. Experimental results demonstrate that FeatureHospital can construct effective feature selection algorithms for different datasets based on their individual characteristics.

---


### 313. [KeyID: Decoupled Drafting and Keyframe Editing for Identity-Preserving Video Generation](https://arxiv.org/abs/2608.16154)

**<font color=#1a73e8>作者：</font>** Jianjie Luo, Yiming Zhong, Haoming Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identity-preserving video generation (IPVG) requires synthesizing videos that are faithful to both reference subjects and text prompts. Existing methods are often hindered by high tuning costs or limited input-level enhancements, struggling to maintain rigid identity consistency during complex, long-sequence actions. To address these limitations, we propose KeyID, a training-free IPVG framework that decouples the synthesis of video dynamics from the injection of identity. Specifically, KeyID comprises two components: (1) Reference-Aware Video Generation, which produces an identity-agnostic video draft aligned with multiple references, and (2) Identity-Preserved Keyframe Editing, which integrates the target identity via sparse keyframe correction and subsequent motion interpolation. By shifting from dense frame-level supervision to sparse keyframe-level refinement, KeyID effectively resolves the capacity conflict between prompt adherence and identity fidelity. Crucially, our modular design allows seamless extension to multi-subject references and complex sequential action generation without additional training. KeyID outperforms prior works and is validated by automatic and human evaluations on the official challenge benchmark, ultimately securing the runner-up position in the Track 2 (Sequential Action) of the ACM Multimedia 2026 IPVG Grand Challenge. Source code is available at this https URL.

---


### 314. [REFLEX: Reflexive Equilibrium Fixed-point Learning for Endogenous eXchanges](https://arxiv.org/abs/2608.16155)

**<font color=#1a73e8>作者：</font>** Vignesh Nagarajan, Shriraghav Ashok  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In over-the-counter corporate bond markets, dealers compete for client trades by quoting bid and ask prices. Tighter quotes attract more business, but also informed customers more likely to trade ahead of adverse price moves, leaving the dealer holding the risk. As dealers increasingly use machine learning to set quotes, they retrain these models on the trades their own quotes attract, creating a feedback loop in which each model reshapes the market that generates its next training data. The question is therefore not only whether a quoting model performs well, but whether the market it creates stays stable as the model learns from it. Existing performative prediction theory gives a sharp stability condition, yet expresses it through abstract properties of the learning objective a trading desk cannot measure before deployment. We introduce REFLEX, a framework that replaces those unobservable quantities with three measurable features of dealer behavior: how strongly trading volume responds to tighter quotes, how sharply the dealer's objective bends around its optimum, and how quickly informed flow increases as spreads narrow. REFLEX combines these into a single retraining modulus, a pre-deployment stability margin estimated from a desk's own quote and execution history that predicts whether repeated retraining will converge or amplify itself. In simulation, predicted and measured stability agree within 8%, and competing dealers increase instability by 1.74x with two and 3.16x with three, as predicted. Where ordinary retraining becomes unstable at modulus 1.21, a structurally anchored correction converges as blind retraining collapses. Calibrated over 36 years of public market data, stability headroom falls roughly 4.4x for investment grade and 4.3x for high yield from calm to crisis regimes. Ultimately, REFLEX turns an abstract convergence theorem into a market-level safety margin.

---


### 315. [A Tree-Structured Approach for Phishing Template and Attacker Attribution Analysis](https://arxiv.org/abs/2608.16158)

**<font color=#1a73e8>作者：</font>** Unai Agirre, Imanol Jerico, Felipe Castaño 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Phishing remains a persistent and evolving cybersecurity threat, with attack volumes reaching record levels. This growth is driven by the industrialization of phishing through widely available phishing kits and reusable templates, which enable cybercriminals to rapidly generate and deploy large numbers of fraudulent webpages. Although surface-level attributes may differ across these websites, their underlying structures often exhibit significant similarities. However, most existing defenses rely on reactive blocklists or supervised classification models that focus on individual phishing instances, limiting their ability to identify structural reuse and detect coordinated phishing campaigns. To address this limitation, this study investigates whether HTML structure can serve as a robust fingerprint for identifying phishing template reuse. We model webpages as Document Object Model (DOM) trees and extract structural features, optionally enriched with HTML tag-based content information. These representations are then clustered using unsupervised learning methods to group structurally similar webpages. Three clustering algorithms are evaluated and compared, while also analyzing how the depth of the extracted DOM-tree affects cluster formation and overall clustering performance. Finally, cluster quality is also evaluated both quantitatively and qualitatively, including a novel level-wise Jaccard Distance Score and manual inspection supported by visualization tools. Results demonstrate that structural representations of webpages can effectively reveal hidden similarities across phishing sites, enabling the detection of emerging and zero-day templates and supporting the analysis of coordinated phishing threats

---


### 316. [Digital Twin Degradation: Detecting Cyber Physical Attacks via Temporal Inconsistencies](https://arxiv.org/abs/2608.16159)

**<font color=#1a73e8>作者：</font>** Konstantinos E. Kampourakis, Vasileios Gkioulos, Sokratis Katsikas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Digital Twins (DTs) are increasingly used to monitor and analyze Cyber Physical Systems (CPS). However, in adversarial environments, the fidelity of a DT cannot be assumed. Communication delays, data manipulation, sensor degradation, or partial information loss may cause the DT state to diverge from the physical process it represents. Such divergence creates temporal inconsistencies that may reveal cyber physical attacks. This paper proposes a detection framework that monitors temporal consistency between the physical system and a potentially degraded DT view. A DT predictor is trained exclusively on normal system behavior to model short-term system dynamics. During operation, discrepancies between predicted and observed states are transformed into multi-horizon temporal features capturing the magnitude, persistence, and evolution of prediction residuals. An unsupervised density model characterizes normal consistency patterns, while a sequential change detection mechanism identifies sustained deviations indicative of attacks. The approach is evaluated on three widely used Industrial Control System (ICS) datasets, SWaT, HAI, and BATADAL, under multiple DT degradation scenarios, including time desynchronization and partial observability loss. Results show that temporal inconsistency patterns enable reliable event-level attack detection with bounded false alarm rates and low detection latency. The proposed method achieves up to 98% detection reliability on SWaT and false alarm rates below 2%. Unlike conventional anomaly detection methods, the proposed framework does not require attack signatures or labeled attack data and remains effective even when the DT view is degraded. These results suggest that DT degradation, often treated as a limitation, can instead serve as a useful signal for cyber physical security monitoring.

---


### 317. [A Calibrated and Explainable Bimodal Machine Learning Framework for Hybrid Intrusion Detection](https://arxiv.org/abs/2608.16160)

**<font color=#1a73e8>作者：</font>** Hafsa Aslam, Yue Li, Saba Aslam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern communication systems face critical gaps in detecting unknown attacks and rare threat classes due to extreme data imbalance and black-box decision logic. We propose a bimodal framework of calibrated and explainable machine learning (ML) for network security, unifying known-class precision with open-set generalization without the complexity of deep learning. Our framework introduces security-oriented feature extraction to enhance signal-to-noise ratio, hybrid resampling (ADASYN + manual boosting) to reduce class imbalance, isotonic calibration and adaptive thresholding ($\tau=0.30$ for XSS) to recover recall for rare attacks, and SHAP-based explainability to validate domain-aligned decision logic. Evaluated on the CIC-IDS2017 dataset and compared with prior ML models and studies, our framework achieves significant accuracy on known attacks (Macro F1 = 0.8626) and detects unknown classes at 1% FPR with TPR up to 90.17% (DoS slowloris), and 77.04% (Web-XSS). The SHAP analysis confirms decisions are driven by security-relevant features, not model artifacts. Our work bridges the gap between theoretical models and operational IDS by delivering calibrated, explainable, and open-set-capable attack detection and prevention in a single, reproducible framework. Keywords: intrusion detection, cybersecurity and privacy, explainable AI, machine learning

---


### 318. [Trajectory-Level Automatic Curriculum Learning for Legged Locomotion on Unstructured Terrain](https://arxiv.org/abs/2608.16164)

**<font color=#1a73e8>作者：</font>** Rocky Liu, Tengyu Liu, Baoxiong Jia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training locomotion policies for complex unstructured terrain requires a curriculum to avoid early exploration failures. However, since unstructured terrain lacks explicit difficulty ordering for curriculum design, existing methods resort to heuristic curricula over parameterized terrains. This abstraction limits generalization, as policies can overadapt to near-fixed perceptual patterns. To address this, we propose \textbf{\ourname{}}, an \textbf{T}rajectory-level \textbf{A}utomatic \textbf{C}urriculum \textbf{L}earning framework that generates training tasks directly from unstructured terrain maps. At each curriculum update, the evaluator learns a difficulty function for the current policy that maps a given trajectory task to a difficulty score. The sampler then proposes new trajectories guided by the learned evaluator as the curriculum for the next policy update. This forms a closed loop in which the curriculum is iteratively matched to the evolving policy. Quantitative and qualitative experiments show that \ourname{} continuously provides effective curricula on unstructured terrain, improving trajectory success rate by \(56.3\%\) over direct training without curriculum. Compared with handcrafted curriculum learning, our method improves success rate by \(18.5\%\) on the hardest terrain tasks and by up to \(39.74\%\) when evaluating traversal from diverse approach directions on the same obstacle type.

---


### 319. [Demystifying Oversmoothing in Sheaf Neural Networks: An Index-Theoretic Criterion](https://arxiv.org/abs/2608.16180)

**<font color=#1a73e8>作者：</font>** Junwen Dong, Yuhan Peng, Hao Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To combat oversmoothing in Graph Convolutional Networks, Sheaf Neural Networks (SNNs) were proposed as a generalization by equipping the graph with a sheaf structure and replacing the graph Laplacian with a sheaf Laplacian $\mathcal{L}$. Existing analyses connect sheaf diffusion to oversmoothing via the harmonic space ($\ker\mathcal{L}$), taking its absolute dimension as an indicator of anti-oversmoothing capacity. However, absolute dimension alone is not a reliable measure: certain sheaf configurations inflate $\dim \ker \mathcal{L}$ while their harmonic sections remain entirely constant, without enriching discriminative capacity. We instead introduce the first relative, geometric approach, yielding a precise characterisation of anti-oversmoothing capacity. Under natural conditions on stalk transportation and global sheaf structure, we establish an index-theoretic comparison criterion showing that one sheaf's harmonic space genuinely contains another's beyond trivial inflation. We illustrate this with a concrete instance and further introduce \textit{GyroSheaf}, a sheaf with curved gyrovector-space stalks, extending the criterion to the non-linear setting via local tangent-space linearization. Experiments across ten models confirm the theoretical criterion: sheaf models violating the criterion collapse despite possessing index jumps, while compliant models maintain depth-stable representations.

---


### 320. [Understanding and Stabilizing Deep Q-Learning via Controlled Bootstrapping and Regulated Value Dynamics](https://arxiv.org/abs/2608.16182)

**<font color=#1a73e8>作者：</font>** Bozhou Chen, Yongyi Wang, Hanyu Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Q-learning (DQL) has achieved remarkable empirical success in reinforcement learning, yet its training process remains notoriously unstable. Existing studies often attribute instability to isolated factors such as overestimation bias or representation learning issues, lacking a unified understanding of how different sources of instability interact during recursive value estimation. In this work, we provide a systematic analysis of instability in deep Q-learning from three complementary perspectives: operator-level bias in Bellman bootstrapping, estimator-level sensitivity of greedy action selection to regression noise, and parameter-dynamics imbalance under aggressive data reuse. We identify a reward-triggered self-reinforcing trap and characteristic parameter spike dynamics, then derive stabilization principles for controlled bootstrapping, ensemble quantile estimation, and spike-based parameter regulation. Experiments on Atari-100K and Procgen demonstrate competitive performance and improved training stability.

---


### 321. [Decorrelation Is Not Complementarity: Skill, Not Lineage, Governs Trusted-Monitor Ensembles](https://arxiv.org/abs/2608.16190)

**<font color=#1a73e8>作者：</font>** Anik Jha  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted monitoring has a cheap, trusted model score a stronger untrusted model's actions, and a diverse ensemble of them beats a single stronger monitor at matched cost. They are built by minimising average pairwise correlation, and that paper's twelve monitors shared one base model, leaving open what supplies the diversity. We study 24 open-weight monitors spanning nine pretraining lineages and a 29x range of detection skill (pAUC at 10 percent FPR, 0.028 to 0.803) on backdoored code.
The metric used to build panels does not predict what a panel is for, and we can say why. Agreement on attack items splits into a shared-detectability signal component and an idiosyncratic error component, which predict ensemble gain with opposite sign (Spearman -0.25 and +0.26), so their sum, the metric actually used, predicts it barely at all (+0.05); the cancellation holds in 7 of 8 evaluations. Skill acts on signal (+0.53) while error stays flat (-0.01), which is why a monitor's own skill predicts its agreement with the pool (Spearman 0.84, n = 24, permutation p below 0.0001).
Pretraining lineage is the obvious way to buy decorrelation, and it does not pay. At matched member capability, cross-lineage panels detect no better (permutation p = 0.13), and lineage barely moves the metric either (+0.064, p = 0.18). We report that against ourselves: on our own 22-monitor pool the same test read +0.104 at p = 0.037 until two monitors were added. An earlier pool topping out at pAUC 0.23 had already invalidated another analysis. Such a quantity is a property of the pool assembled.
Panel gain over the best member falls monotonically with panel skill (-0.66 at k = 2, -0.70 at k = 3), and no correlation-weighted selection beats picking the single best monitor out of sample. Across six attacker models the gain result holds in all six, the agreement and cancellation results in five of six.

---


### 322. [Beyond Clear Skies: Synthetic Seasonal and Weather Variations for Real-World Drone Detection](https://arxiv.org/abs/2608.16191)

**<font color=#1a73e8>作者：</font>** Tamara R. Lenhard, Andreas Weinmann, Tobias Koch  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable drone detection under real-world deployment conditions requires training data that spans the full operational design domain, including adverse weather and seasonal appearance variation. However, acquiring and annotating such data at scale remains highly resource-intensive, as adverse-weather conditions are inherently difficult to control, reproduce, and sample systematically. Existing datasets therefore typically provide only limited coverage of such conditions. Conversely, synthetic data offers a scalable alternative: environmental variation becomes controllable, while modern game-engine-based pipelines provide realistic rendering and automatic annotations. Leveraging this potential, we introduce SynDroneVision-Weather (SDV-W), an systematic extension of SynDroneVision (SDV) targeting adverse-weather and seasonal domain shifts in urban drone detection. SDV-W comprises 55,187 annotated high-resolution images from three urban environments, rendered across three seasonal configurations and diverse weather conditions, including rain, snow, and fog at multiple severity levels. By preserving SDV's scene and trajectory configuration, SDV-W enables matched clean-adverse comparisons and quantification of condition-specific detector degradation. Across representative YOLO models and real-world datasets, we show that SDV-W improves detector reliability under adverse appearance shifts, reduces missed detections and false alarms, and is most effective as a complement to general-purpose synthetic drone-detection data. SDV-W will be publicly released upon paper acceptance.

---


### 323. [Baseline-Relative Counterfactual Refinement for Bit-Aware Visual Token Communication](https://arxiv.org/abs/2608.16192)

**<font color=#1a73e8>作者：</font>** Jia Guo, Xiaohan Zhao, Changwang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative visual-token communication reduces transmission load by sending only selected discrete tokens and reconstructing missing content at the receiver. However, existing token-selection criteria based on local uncertainty, importance, or diversity do not directly determine whether changing the current selection improves the final reconstruction under the same packet budget. To address this problem, we propose Gated Counterfactual Refinement for Communication (GCR-C), a rollout-style correction layer over Local-MDL. GCR-C constructs a compact diversified candidate set, evaluates each candidate through matched full-budget Local-MDL continuation, and replaces the baseline action only when a positive baseline-relative reconstruction gain is obtained. Experiments on CIFAR-10, STL-10, a coded 5G-LDPC link, and a limited high-resolution Kodak transfer show that GCR-C consistently improves reconstruction quality at active low- and medium-rate operating points without increasing the realized packet rate, while remaining effective across changes in dataset, channel condition, resolution, token grid, and tokenizer. The results also reveal a clear quality--computation tradeoff due to the additional encoder-side counterfactual evaluation.

---


### 324. [Picking the Right Image to Classify: Reliable-Input Selection in Teledermatology](https://arxiv.org/abs/2608.16198)

**<font color=#1a73e8>作者：</font>** Fabian Gröger, Marco Weishaupt, Philippe Gottfrois 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dermatology models face distribution shifts in teledermatology settings, where submitted images differ from the training data in lighting, angle, distance, focus, and framing. These test-time images are ordinary clinical photographs, but some fall outside the model's training conditions, leading the model to often misclassify them due to shifts in acquisition between training and deployment. When multiple images of the same case exist (several photos of one patient or lesion), a natural way to improve accuracy is therefore to select the image the model is most likely to classify correctly. We call this task reliable-input selection. An oracle that, for each case, selects a correctly classified image when one exists raises weighted F1 by about 20 percentage points on average across six dermatology datasets and nine frozen backbones. This oracle is an upper bound that sees the labels, whereas a selector must choose blindly. Capturing this gain in practice is hard. A selector that needs no pretraining data applies to any frozen model, including those whose data is not public. It must judge reliability from quantities the model exposes at inference: its embeddings, their norms, and its confidence. We benchmark four such training-data-free selectors: the embedding norm, the neighborhood consensus among a case's images, the stability of the prediction under small perturbations, and the model's own confidence. No training-data-free selector substantially narrows this oracle gap. The best of them is the model's own confidence, but it recovers only a small part of the gap on the clinical datasets. A small labeled reference set does not help either: the best selector overall, a fusion of confidence and Mahalanobis distance, still leaves most of the gap. To our knowledge, this is the first study to introduce and benchmark reliable input selection, a clinically important, unsolved task.

---


### 325. [Quantifying the Gap Between Laboratory Battery Test Patterns and Field Duty Profiles](https://arxiv.org/abs/2608.16212)

**<font color=#1a73e8>作者：</font>** Chunyang Zhao, Chresten Træholt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Laboratory battery tests provide the main empirical basis for battery performance and degradation studies, but their operating patterns do not directly represent field duty profiles. This paper quantifies the gap by comparing six accessible evidence sources covering controlled cycling, drive-cycle testing, dynamic cycling, NMC811 laboratory ageing, a real electric-vehicle charging trace, and fleet-scale electric-vehicle state-of-health (SOH) data. The analysis combines usage frequency, usage intensity, usage C-rate, and a duty-structure index (DSI) based on normalized current dispersion and ramping. The representative single-segment DSI ranges from 0.630 for the field source trace and 0.699 for NASA to 2.936 for Oxford and 2.855 for Imperial, while usage C-rate ranges from 0.14-0.40 for Imperial, NASA, Stanford, and Hyundai to 2.00 for Oxford. Long-term ageing also differs: the 80 percent retention region occurs near 351 NASA cycles, 6292 Oxford checkpoints, and 1019 Stanford cycles. In chemistry-aligned NMC/NCM evidence, Imperial retains 0.813 under standard cycling and 0.865 under drive-cycle ageing, while the field source has median SOH 0.889 with visible dispersion. Field operation further shows a median use intensity of 137.2 km/day and 56.9 percent of charges ending at or above 95 percent SOC. These results show that battery performance metrics are conditional on the duty pattern that generated them; application-oriented studies should report explicit duty-profile descriptors together with chemistry, capacity, and ageing metrics.

---


### 326. [Beyond Peak Backlog: Conditional Energy and Temporal Geometry in Capacity-Constrained Delayed Bandit Optimization](https://arxiv.org/abs/2608.16216)

**<font color=#1a73e8>作者：</font>** Anling Xiang, Yuwen Yang, Yang Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What is the right delay complexity when a learner can track only $C$ pending feedback items and discarded feedback is permanently lost? Existing one-point bandit convex optimization guarantees in this model pay $\sqrt{T\sigma_{\max}}$, where $\sigma_{\max}$ is the peak backlog, although unlimited tracking admits the sharper $\sqrt{d_{\mathrm{tot}}}$ dependence on total delay. We introduce a scheduler-side conditional-energy interface that separates rate adaptation from the one-point perturbation filtration and handles the dependent importance weights created by randomized admission. Under the same semi-clairvoyant oracle and pathwise hard-capacity contract, this yields an untuned learner whose delay term scales as $O(\sqrt{E_C d_{\mathrm{tot}}})$, with only an explicit restart factor $E_C$; a public constant-factor peak bound removes this factor while $d_{\mathrm{tot}}$ remains unknown. Under strong convexity, the same interface yields the temporal cost $H_A(d)=\sum_t \sigma_t/(A+t)$. Two delay vectors with identical delay multisets, $d_{\mathrm{tot}}$, $\sigma_{\max}$, and capacity can nevertheless have polynomially different minimax regret, showing that timing matters under curvature even when aggregate delay summaries agree. Finally, a continuous hard family converts tracking capacity into a zeroth-order query budget and gives a complementary capacity-starvation lower endpoint. The upper bounds require $C\ge \ln T+1$ and do not constitute a complete capacity minimax characterization.

---


### 327. [Trusted Hardware Acceleration for Function Secret Sharing](https://arxiv.org/abs/2608.16223)

**<font color=#1a73e8>作者：</font>** Pengzhi Huang, Kiwan Maeng, G. Edward Suh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Function secret sharing (FSS) is a core building block for privacy-preserving systems such as secure inference and private information retrieval (PIR), but incurs significant overhead in key generation, communication, and data this http URL present the distributed function accelerator (DFA), a hardware accelerator that targets the dominant primitive in FSS: distributed point function (DPF) generation and evaluation. DFA combines a high-throughput fixed-function engine for AES-based pseudorandom number generation with a lightweight programmable unit for protocol-specific logic. In untrusted mode, DFA serves as a pure accelerator for DPF evaluation, improving throughput and energy efficiency without changing the protocol. In trusted mode, it further enables local, on-the-fly key generation, eliminating key distribution, and reducing storage and data movement overheads.
Across representative workloads, DFA achieves a reduction of 10X end-to-end latency, a reduction of up to 20X communication and more than 5X energy savings for secure inference; and an improvement of 5X throughput and 10X energy reduction for PIR, with modest hardware cost.

---


### 328. [PCT-Prompt: A Prompt-Guided Transformer Framework for Dense Prediction Tasks in Point Clouds](https://arxiv.org/abs/2608.16225)

**<font color=#1a73e8>作者：</font>** Dejun Zhang, Yanzi Bai, Yiqi Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard Transformers have proven effective in point cloud object classification, but their performance in dense prediction tasks within complex scenes is often hindered by weak prior assumptions. To address this challenge, we propose PCT-Prompt, a novel framework that enhances standard Transformers by introducing a prompt-guided feature branch to improve performance in dense prediction tasks. The standard Transformer branch leverages pre-trained models for global feature extraction from point cloud data, serving as the backbone for processing high-level features. Meanwhile, the prompt-guided feature branch consists of two key components: a fine-grained feature extraction block that captures multi-scale geometric features using geometry-sensitive abstraction layer, along with the PnP-3D layer to integrate local context with global regularization. The second component, the prompt-refined feature learning block generates prompt tokens, which are subsequently refined through cross-attention mechanisms. Additionally, we introduce a prompt drop mechanism that progressively removes prompt information across Transformer layers, balancing local details and global consistency. Experimental results on the ShapeNetPart, S3DIS, and DALES datasets demonstrate that PCT-Prompt significantly improves the adaptability of standard Transformers to dense prediction tasks, achieving strong performance in real-world scenarios.

---


### 329. [A Privacy Study of Sparse Collaborative Inference](https://arxiv.org/abs/2608.16236)

**<font color=#1a73e8>作者：</font>** Maximilian Andreas Hoefler, Karsten Mueller, Wojciech Samek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collaborative inference (CI) splits a model between an edge device and a server, whereby the client computes an intermediate activation, transmits it, and the server completes the computation. This raises two concerns, the communication cost of the transmission and the risk that it reveals private information about the input. Recent work reduces this cost by sparsifying activations and entropy-coding the result. Sparsity has also been argued to improve privacy, on the intuition that transmitting fewer values reveals less about the input. We test this claim by decomposing the sparse activation into the retained values and the set of positions they occupy, and by reconstructing inputs from each component in isolation. We find that sparsification reduces the leakage far less than it reduces the transmission cost, and that the remaining risk shifts to the positions, which prior analyses treat as side information for decoding. Across natural-image and face datasets, the positions alone constitute a serious privacy risk, enabling high-fidelity reconstructions and re-identification of individuals. The leakage from the positions persists even when both the transmission cost and the task utility are low. We conclude that the positions of sparse activations should be treated as sensitive transmitted data and audited carefully in the context of collaborative inference. Code is available at this https URL.

---


### 330. [Optimizing Multi-Market Participation of Battery and Electrolyser Systems Based on Field Performance](https://arxiv.org/abs/2608.16238)

**<font color=#1a73e8>作者：</font>** Chunyang Zhao, Stoyan Trenchev, Shi You 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The increasing share of renewable energy in power systems creates a need for fast-response and flexible resources to maintain system stability. With the expansion of electricity markets and ancillary service products, opportunities arise to stack revenues across multiple services. Long-term Power-to-X (PTX) electrolysers and short-term battery energy storage systems (BESS) are prevalent flexible resources, yet most studies neglect real hardware behavior, such as ramp limits, efficiency, and setpoint-tracking accuracy. This work presents experimental and modeling results for a 55 kW/79 kWh BESS and an electrolyser comprising three 2.4 kW units. Key characteristics are identified through measurements and embedded into a price-driven optimization framework for participation in the Danish electricity and ancillary service markets, utilizing real market data from 2022 to 2025. The optimized daily profits for multi-market participation are 1,749.27 DKK and 289.46 DKK for the BESS and electrolyser, respectively. With the demonstrated business cases for BESS and PTX systems, this work highlights the importance of incorporating experimental performance when evaluating participation across multiple markets and years.

---


### 331. [Convolution-Free Holistic Multivariance Decomposition Layer for Efficient Hyperspectral Image Classification Tensor Networks](https://arxiv.org/abs/2608.16241)

**<font color=#1a73e8>作者：</font>** Süha Tuna, Ülker Başar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feature extraction for hyperspectral image classification is conventionally addressed using rigid tensor decompositions that fail to capture complex spatio-spectral interdependencies, or heavily parameterized convolutional neural networks that are computationally expensive. To overcome these limitations, this work introduces the Holistic Multivariance Decomposition (HMD) framework as a novel, end-to-end differentiable neural network layer. By explicitly separating independent single mode variations from cooperative higher dimensional interactions via learnable, matrix valued supports, the proposed HMD-0, HMD-1 and HMD-2 approximants are optimized jointly with a downstream classifier via backpropagation. Comprehensive evaluations across three benchmark HS datasets demonstrate that the higher level HMD layers achieve superior classification accuracy compared to classical learnable tensor baselines, including Tucker, Canonical Polyadic, and Tensor Train decompositions. Furthermore, HMD-1 and HMD-2 achieve a generalization capacity and training stability comparable to standard 2D and 3D-CNNs while requiring significantly fewer feature extractor parameters. These results demonstrate that the HMD framework provides a structurally robust substitute for traditional convolution in multidimensional HS image classification, offering high parameter efficiency and stability throughout the optimization process.

---


### 332. [The Trade-off Between Covariate Dependence and Latent Structure in Representation Learning](https://arxiv.org/abs/2608.16245)

**<font color=#1a73e8>作者：</font>** Małgorzata Łazęcka, Ewa Szczurek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Disentangled representation learning seeks latent representations whose indicidual dimensions each align with a distinct covariate. Unsupervised approaches typically target latent dimension independence, yet this gives no guarantee that the resulting dimensions align with semantically meaningful covariates. Supervised approaches structure the latent space using observed covariates, but under correlated covariates they cannot simultaneously control one-to-one latent-covariate alignment and latent independence. We introduce a unified, supervised framework that couples latent dimension-covariate dependence with constraints on the latent structure. Within this framework, we show an inherent trade-off, where enforcing latent independence or exclusive one-to-one latent-covariate dependence comes at a provable cost in latent-covariate alignment. We prove that the resulting disentanglement regimes are ordered by the strength of that alignment. Each regime admits a closed-form transformation of the latent space. We apply these transformations post-hoc to realign the representations of pretrained models such as CLIP, DINOv2, and ViT, and we fold them into the inference of informed factor analysis (iFA), a probabilistic model with covariate-informed factors. On simulated and real multi-omics data, we show that both post-hoc alignment and iFA enable controllability of structured latent representations.

---


### 333. [SCOUT: Semantic Concept Discovery for Open-Vocabulary Editing of face Recognition Templates](https://arxiv.org/abs/2608.16251)

**<font color=#1a73e8>作者：</font>** Leon Todorov, Peter Rot, Peter Peer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face recognition templates are compact identity representations, yet they also encode rich semantic information about facial appearance. Prior work has shown that templates can be inverted to images or indirectly manipulated through image-editing pipelines, but direct semantic editing in template space remains largely unexplored. Existing interpretability methods for face recognition often rely on manual neuron inspection or predefined attribute labels, limiting scalability and semantic flexibility. To address this gap, we propose SCOUT (Semantic Concept Discovery for Open-VocabUlary Editing of Face Recognition Templates), an end-to-end framework for discovering and directly manipulating semantic concepts in face recognition templates using mechanistic interpretability. SCOUT learns sparse template representations, generates semantic hypotheses for latent features from natural-language descriptions, and validates their stability. The resulting features act as controllable semantic directions for direct editing, avoiding costly edit--re-encode pipelines. Experiments with face recognition models using CNN, ViT, and Swin backbones show that SCOUT discovers interpretable concepts beyond standard attribute labels and enables controllable, identity-aware template manipulation with negligible impact on identity matching. We further show that edited templates can subsequently be decoded with independent inversion models for visualization and evaluation.

---


### 334. [Efficient Coreset Selection via K-Nearest Neighbor Graphs](https://arxiv.org/abs/2608.16270)

**<font color=#1a73e8>作者：</font>** Yingfan Liu, Leiyu Zhang, Jiadong Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coreset selection reduces the cost of model training by replacing a large training set with a small representative subset. Existing gradient-approximation coreset methods such as CRAIG and cluster-based variants can preserve model accuracy. Still, their selection stages often rely on dense pairwise distances or large item-cluster bound matrices, leading to high time and memory costs on large datasets. This paper proposes KNNG-CS, a lightweight coreset selection method based on a $K$-nearest neighbor graph. KNNG-CS exploits local neighborhood structures to estimate the importance of each data item and greedily selects representative nodes without maintaining a quadratic distance matrix. The method requires only linear storage in the number of edges. Experiments on four real-world datasets show that KNNG-CS achieves accuracy comparable to representative gradient-approximation coreset methods, while reducing selection time by $2.3\times$-$41.2\times$ and peak memory to $0.3\%$-$7.5\%$ of the baselines.

---


### 335. [Disentangling Innovation Practices in Automation-Adopting Organizations: a Co-Performance Perspective](https://arxiv.org/abs/2608.16279)

**<font color=#1a73e8>作者：</font>** Garoa Gomez-Beldarrain, Kars Alfrink, Euiyoung Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As organizations increasingly adopt automation, innovation practitioners are responsible for selecting, adapting, testing, and implementing externally sourced innovations. However, little is known about how these upstream practices shape worker-automation arrangements, limiting our ability to intervene in innovation practice to address automation adoption challenges. To disentangle this relationship, we interviewed nine innovation practitioners at a major European airport pursuing long-term autonomous operations and analyzed their practices through a co-performance lens. We synthesize five co-performance design principles and examine where current practices align or conflict. Our findings reveal tensions: innovation practitioners prioritize full-automation arrangements while postponing human considerations; contextual constraints shape solutions, but openness to reconfiguration remains limited; and co-learning rarely extends beyond pilot phases. These insights provide HCI research and practice with guidance for reframing the conceptualization of automation, particularly by encouraging earlier consideration of human roles, promoting iterative visions, and recognizing workers as co-designers throughout innovation pipelines.

---


### 336. [Audio-Visual Segmentation via Depth-Guided Collaborative Modeling](https://arxiv.org/abs/2608.16285)

**<font color=#1a73e8>作者：</font>** Zhaojin Fu, Yuyang Hong, Qi Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-Visual Segmentation (AVS) is a fundamental task in multimodal perception that performs pixel-level segmentation of sounding objects in videos by leveraging both visual and audio cues. It has broad applications in video understanding, human-computer interaction, and autonomous driving. However, most existing AVS methods do not explicitly model geometric cues such as relative distance and occlusion, thereby limiting the robustness of cross-modal alignment. In human perception, spatial structure is naturally integrated with audio-visual evidence to accurately localize sounding objects. Motivated by this, we incorporate estimated depth as a spatial structural cue for AVS and propose DGCM-AVS, a tri-modal framework that jointly models audio, visual, and depth information. Specifically, we design a Depth-Aware Dynamic Modulator to improve the separation of adjacent objects while preserving intra-object feature consistency. Furthermore, we propose Depth-Guided Progressive Fusion, which uses depth as an intermediate bridge to progressively align audio cues with visual features. Compared to state-of-the-art methods, DGCM-AVS achieves relative improvements of 10.2 percent in M_J and 8.7 percent in M_F on the AVSS dataset. We believe our study highlights depth as a promising yet underexplored modality for AVS and may encourage further research in this direction.

---


### 337. [SCALE: State-Calibrated Latent Embeddings for JEPA Planning in the Right Geometry](https://arxiv.org/abs/2608.16287)

**<font color=#1a73e8>作者：</font>** Jiaming Hu, Yan Zheng, Tian Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-embedding predictive world models plan by scoring predicted terminal embeddings against a goal embedding using a cost defined on the representation itself. Two prominent strategies for obtaining non-collapsed representations are to inherit a pretrained feature space, as in DINO-WM, and to learn an embedding end to end with anti-collapse regularization, as in LeWorldModel (LeWM) with SIGReg. These strategies show complementary strengths across tasks. Although task-relevant state is decodable from the full embeddings of both models, DINO-WM's leading principal components usually retain substantially more state information than LeWM's. Because Euclidean planning costs are dominated by high-variance directions, this difference affects how strongly state can influence candidate selection. We propose SCALE (State-CAlibrated Latent Embeddings) to give the end-to-end LeWM representation the favorable geometric property observed in DINO-WM. SCALE induces this property by correlating sampled pairwise latent distances with distances in a standardized task-relevant state space, without replacing LeWM's learned encoder. Across five tasks, three planning solvers, and five compute budgets, SCALE improves every task--solver average over LeWM. A latent-to-state regression control matches or exceeds SCALE's full-embedding decodability yet leaves latent--state distance alignment essentially unchanged and yields less consistent planning gains. SCALE adds a single lightweight training-time regularizer and no planning-time overhead. These results show that planning depends not only on whether task-relevant information is present, but also on whether it shapes the geometry consumed by the planner.

---


### 338. [PosterText: Towards Unified Visual Text Generation and Editing for E-commerce Poster](https://arxiv.org/abs/2608.16289)

**<font color=#1a73e8>作者：</font>** Xiaoan Liu, Lichen Ma, Zipeng Guo 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated e-commerce poster design requires both high-quality poster generation and flexible editing of existing designs. However, most existing methods either target end-to-end poster generation or follow multi-stage design pipelines, with limited capability for flexible and precise editing of existing posters. To enable unified generation and editing of e-commerce posters, we introduce Text Patch Generation and Editing, a unified task formulation that treats text patches as atomic units and covers four operations: poster generation, patch addition, patch deletion, and patch modification, with optional reference-guided style control. Based on this, we propose PosterText, a unified model trained with a four-stage curriculum, including text rendering pretraining, instruction-following training, reinforcement learning for preference alignment, and spatial guidance self-distillation for execution refinement. We further construct a large-scale dataset with patch-level annotations and a comprehensive benchmark for evaluation. Extensive experiments demonstrate that PosterText achieves competitive performance against existing generation and editing approaches, validating the effectiveness of the proposed framework.

---


### 339. [Principled Authority Switching for Shared Autonomy in Human-Robot Teams](https://arxiv.org/abs/2608.16293)

**<font color=#1a73e8>作者：</font>** Sandeep Banik, Naira Hovakimyan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Shared autonomy requires principled mechanisms for allocating and transferring control between a human and an autonomous agent. Existing approaches often rely on blending control inputs or heuristic switching rules, which lack theoretical guarantees and fail to account for the dynamics of authority transfer. This paper develops a cooperative game-theoretic framework for authority switching in shared autonomy. We formulate the control switching problem as an identical-interest dynamic game in which authority transitions are embedded into the system dynamics, yielding optimal switching policies rather than ad hoc rules. We establish the existence and characterization of team-optimal policies in pure strategies under stochastic human override, accounting for asymmetric authority where humans retain override capability. For linear-quadratic systems, we derive closed-form recursions for the optimal switching policies and value functions, enabling efficient computation independent of the continuous state. We validate the framework on scalar and multi-dimensional linear systems, demonstrating how optimal switching adapts to varying system dynamics, cost structures, and override probabilities. The results reveal fundamental trade-offs between human adaptability and autonomous efficiency, illustrating the practical benefits of grounding shared autonomy in cooperative game theory.

---


### 340. [FTA-Mem: Fact-Time-Affect Anchored Memory for Low-Density Long-Term Dialogue](https://arxiv.org/abs/2608.16303)

**<font color=#1a73e8>作者：</font>** Chang Liu, Shuyi Zhang, Changsheng Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term emotional-support agents require memory mechanisms for personalized understanding across sessions. However, emotional-support dialogue is often low-density: turns are incomplete, evidence is scattered, and user states evolve over time. Existing memory methods usually rely on fixed units, such as turn-level notes or session summaries, which may lose details or introduce redundant noise. We propose FTA-Mem, a structured memory framework for low-density long-term dialogue. FTA-Mem uses Boundary-preserving Window Segmentation (BWS) to form coherent situation fragments, and constructs Fact-Time-Affect Memory Units (FTA Units) that jointly encode factual content, temporal grounding, and affective context. Retrieved units are then synthesized into structured context for answer generation. Experiments on ES-MemEval and LoCoMo show that FTA-Mem improves overall long-term memory question answering across benchmarks with different information-density characteristics. On ES-MemEval, FTA-Mem achieves 0.3871 F1 and 0.6668 BERTScore. Further analysis shows that situation-level FTA construction better balances evidence preservation and construction cost than coarse session-level or overly fine-grained turn-pair construction, providing an effective granularity trade-off for long-term dialogue memory.

---


### 341. [Cross-View Urban Sensing: Mapping Subjective Streetscape Perception via AlphaEarth Embeddings and Urban Context](https://arxiv.org/abs/2608.16310)

**<font color=#1a73e8>作者：</font>** Peilin Li, Pengfei Chen, Jingyu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Residents' perception of the urban streetscape is an important factor in public health, active mobility, and social wellbeing. Street view imagery (SVI) has emerged as a widely used data source for assessing these perceptual qualities, yet its uneven coverage and irregular updating limit large-scale measurement. Here, we present CVLNet, a Cross-View Learning Network that predicts street-level perception from AlphaEarth embeddings and multi-source urban contextual data without requiring SVI at inference. CVLNet applies per-task adaptive gating to jointly model five perceptual dimensions, using labels from the pretrained SVI-Percept model as ground truth. The proposed method is evaluated across four Southeast Asian cities: Singapore, Kuala Lumpur, Jakarta, and Manila. CVLNet achieves a median road-segment-level Adjusted $R^{2}$ of 0.76 and consistently outperforms the baseline models, with gains ranging from 5.9--11.3% across the five perceptual dimensions. Ablation experiments show that AlphaEarth features and urban contextual features contribute complementary information. We further produce citywide road-level streetscape perception maps for five subjective perceptual dimensions across all four cities, extending perception estimation from the 13--31% of the road network directly covered by available SVI to the complete road network of each city. Integrating these maps with WorldPop gridded population data, we quantify exposure inequality across population-density, demographic, and land-use groups using the Deficit Palma Ratio. These results demonstrate that remote sensing can serve as a scalable alternative to SVI for citywide streetscape perception mapping, enabling a more comprehensive assessment of urban environmental inequality.

---


### 342. [$\texttt{Flip-Team}$: Cooperative Takeover Games with Stochastic Human Override](https://arxiv.org/abs/2608.16311)

**<font color=#1a73e8>作者：</font>** Sandeep Banik, Naira Hovakimyan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Shared autonomy requires principled mechanisms for allocating and transferring control between a human and an autonomous agent. Existing approaches often rely on blending control inputs or heuristic switching rules, which lack theoretical guarantees and fail to account for the dynamics of authority transfer. This paper develops a cooperative game-theoretic framework for authority switching in shared autonomy. We formulate the control switching problem as an identical-interest dynamic game in which authority transitions are embedded into the system dynamics, yielding optimal switching policies rather than ad hoc rules. We establish the existence and characterization of team-optimal policies in pure strategies under stochastic human override, accounting for asymmetric authority where humans retain override capability. For linear-quadratic systems, we derive closed-form recursions for the optimal switching policies and value functions, enabling efficient computation independent of the continuous state. We validate the framework on scalar and multi-dimensional linear systems, demonstrating how optimal switching adapts to varying system dynamics, cost structures, and override probabilities. The results reveal fundamental trade-offs between human adaptability and autonomous efficiency, illustrating the practical benefits of grounding shared autonomy in cooperative game theory.

---


### 343. [Advancing Open and Reproducible Relational Learning: RelArena-$α$, TabPFN-Rel and RPI](https://arxiv.org/abs/2608.16319)

**<font color=#1a73e8>作者：</font>** Adrian Hayler, Klemens Flöge, Alan Arazi 等 47 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This first release of Prior Labs in relational learning shows our continued commitment to open science. We open-source three pieces of software that we expect to accelerate research in the field towards meaningful real-world impact. We aim to steer further development based on feedback from, and in collaboration with, the community. Given the early stage of development, our $\alpha$-release targets researchers and early-adopting practitioners. Over the past years, a variety of datasets and tasks for relational learning have emerged, but the community has not converged on a reliable, reproducible way to compare different methods on these tasks. Our $\alpha$-release, RelArena-$\alpha$, provides a unified framework for running and comparing baselines on RelBench v1 by standardizing data loading, evaluation protocols, tuning regimes, and support for systems with custom tuning, inspired by established tabular benchmarks such as TabArena. We plan to work with the research community to further develop RelArena-$\alpha$ into a catalyst for progress in the relational learning community. We release the initial version of TabPFN-Rel, a purpose-built relational harness for TabPFN-3. Currently ranked first among models on RelArena-$\alpha$, TabPFN-Rel makes key improvements upon RDBLearn. Beyond its ranking, TabPFN-Rel serves as a strong baseline, adding to the growing evidence that flattening a relational database into a single table remains competitive with specialized relational architectures on real-world tasks.
To facilitate adoption of relational learning methods in research and industry, we release an initial $\alpha$-version of our Relational Predictive Interface, RPI, an open-source, model-agnostic interface that enables early adopters to easily define problems on new databases and apply any model implemented in RelArena-$\alpha$, including TabPFN-Rel, to these problems.

---


### 344. [LaGSplat: Inferring Physics-Governed Interactive Simulation from Monocular Video Using Latent Lagrangian Gaussian Splatting](https://arxiv.org/abs/2608.16324)

**<font color=#1a73e8>作者：</font>** Louen Pottier  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present LaGSplat (Latent Lagrangian Gaussian Splatting), a framework that infers interactive, physics-governed dynamics from one or a few monocular videos. At inference it lets a user push on the filmed object, rigid or deformable, with an external force that was never measured, annotated, or seen during training. This is possible because a low-dimensional latent state $\mathbf{q} \in \mathbb{R}^d$ plays two roles at once: it is the generalised coordinate of a learned dissipative Lagrangian and the conditioning variable of a Gaussian Splatting decoder. The inductive bias of this decoder, whose primitives are explicit points $\mu_i(\mathbf{q})$ that move with the object, is what lets a force $f$ applied in the image pull back into a latent generalised force $J(\mathbf{q})^\top f$ and enter the equations of motion, which pixel-space (CNN) or neural-field (NeRF) decoders cannot do. We validate LaGSplat on test cases of increasing difficulty, from rigid to deformable and from autonomous to forced real systems, combining monocular video and sensor measurements. We further demonstrate interactive use: forces of arbitrary magnitude and direction can be applied to the reconstructed object at any time, its response rendered in real time, in 2D or 3D. Assuming a dissipative Euler-Lagrange equation over a few generalised coordinates trades generality for a bounded, plausible response to unseen forces, where an unconstrained predictor diverges.

---


### 345. [KC-BFPRL: Knowledge-Guided Multi-UAV Collaboration for Grassland Restoration via Bilevel Formerpointer-Based Reinforcement Learning](https://arxiv.org/abs/2608.16326)

**<font color=#1a73e8>作者：</font>** Dongbin Jiao, Xianyi Wang, Yuchen Yuan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-unmanned aerial vehicle (UAV) systems provide scalable service platforms for large-scale environmental tasks, such as grassland ecosystem restoration. However, coordinating fleet operations requires solving the restoration area maximization problem (RAMP). This non-linear combinatorial optimization challenge is complicated by payload-dependent energy dynamics and heterogeneous ecological degradation. We propose a novel knowledge-guided collaborative bilevel formerpointer reinforcement learning framework (KC-BFPRL) to address this complexity. Using a hierarchical paradigm, KC-BFPRL decomposes RAMP into global task allocation and local restoration planning, with the latter further divided into upper-level trajectory planning and lower-level restoration area allocation. Our specialized architecture pairs featuring a Transformer-based encoder that fuses static environmental features with dynamic UAV states, and a Pointer Network decoder trained via a robust actor-critic framework. By embedding ecological priority rules and heuristic logic, KC-BFPRL achieves a structured warm-start, solving the RL cold-start problem while ensuring strict constraint satisfaction. Extensive experiments demonstrate that KC-BFPRL consistently outperforms state-of-the-art baselines, achieving superior objective values and efficiency. It maintains a $0.00\%$ optimality gap in the most complex scenarios U8-R160 and operates nearly three times faster than MAPDP, validating its robustness, scalability, and real-time applicability for large-scale automated ecological restoration.

---


### 346. [GRNEdit: Efficient General Video Editing from a New Binary-Evidence Perspective in Generative Refinement Networks](https://arxiv.org/abs/2608.16328)

**<font color=#1a73e8>作者：</font>** Feng Xie, Jiagao Hu, Fuhao Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-based general video editing seeks to unify diverse editing operations within a single, intuitive interface. Existing approaches often rely on resource-intensive conditioning, using either heavyweight branches or costly source concatenation. Is there any efficient way to model editing intent? Thus, we introduce GRNEdit, a lightweight two-stage framework. GRN inspires our approach by encoding visual semantics through combinations of bits. Through task-specific fine-tuning, we take this representation further and recast editing semantics as local retain-or-flip decisions over individual bits. Source information is consequently modeled as coordinate-wise evidence supporting the observed binary states, while the GRN backbone remains responsible for resolving their global composition into coherent generative semantics. In Stage I, a compact encoder translates discrete source codes into continuous evidence signals, which GRN assimilates throughout binary refinement. Inspired by null-prompt training for classifier-free guidance, we further assign the null condition an editing-specific meaning: an empty instruction denotes no edit and is supervised through source reconstruction. This identity pathway not only implicitly strengthens evidence utilization and content preservation in Stage I, but also produces a source-preserving state in the same representation space as the edited state. Stage II can therefore directly compare each edited state with its source-preserving counterpart and use their discrepancy to revise unresolved target-bit decisions. Trained on only 0.6M pairs with less than 3\% conditioning parameters, GRNEdit-2B and GRNEdit-8B achieve scores of 4.03 and 4.18 on OpenVE-Bench. The 2B model outperforms multiple 14B open-source editors, while the 8B model performs on par with leading open-source editors.

---


### 347. [Unlocking Motion in Expressions: Temporal Calibration for Referring Video Object Segmentation](https://arxiv.org/abs/2608.16332)

**<font color=#1a73e8>作者：</font>** Yiwen Jiang, Zhengtong Zhu, Ruixin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring Video Object Segmentation (RVOS) aims to segment referred objects at the pixel level in video sequences based on natural language descriptions. Existing methods typically introduce motion information within a unified cross-modal temporal modeling framework, where language cues are used for target localization and segmentation. However, the dependency of expressions on motion semantics is not explicitly modeled, making it difficult to adaptively adjust the use of motion information according to different semantic requirements. To address these issues, we propose an Expression-driven Motion Calibration (EMC) framework for RVOS that explicitly unlocks and leverages the motion semantics within expressions. The proposed method extracts interpretable motion control signals from expressions via a Motion Signal Processing (MSP) module, and employs a Motion Influence Calibration (MIC) module to adjust the contribution of motion cues during temporal decision making. In addition, a Semantic Temporal Stage Construction (STSC) module is introduced to build expression-relevant temporal stages, providing a compact temporal candidate space for motion calibration. Through extensive evaluation on six standard benchmarks, including Ref-YouTubeVOS, Ref-DAVIS17, MeViS (valid/valid$^u$), A2D-Sentences, and JHMDB-Sentences, the superiority of our method is validated. We will release the code on this https URL.

---


### 348. [Transfer Learning of Keystroke Dynamics for Cross-Device User Authentication](https://arxiv.org/abs/2608.16334)

**<font color=#1a73e8>作者：</font>** Nuwan Kaluarachchi, Sevvandi Kandanaarachchi, Kristen Moore 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Keystroke dynamics (typing patterns) can be used as a behavioural biometric modality for user authentication, with applications such as fraud prevention. While the modality has been shown to work well for single device authentication, its application to cross-device scenarios is more challenging. Dynamics learned on one device (eg., phone) may not be directly applicable to authentication on a secondary device with a different form factor (eg., tablet) due to changes in typing patterns that can lead to distribution drifts. To address this, we propose a cross-device user authentication system based on inductive transfer learning, where keystroke dynamics learned on one device are adapted to a secondary device. The adapted data is then combined with necessarily limited training data for the secondary device, which is used to robustly train a binary classifier. Furthermore, an extended set of keystroke features is used to better capture discriminative dynamics. Experiments on the BBMAS dataset show that proposed system achieves an equal error rate of 14.2% for the cross-device scenario, surpassing state-of-the-art methods.

---


### 349. [SIGMA-Lane: Scale-pyramId Gated MAmba for Temporally Consistent Video Lane Detection](https://arxiv.org/abs/2608.16338)

**<font color=#1a73e8>作者：</font>** Tiancheng Zhang, Mengmeng Wang, Yan Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video lane detection requires predictions that remain stable across frames, yet severe vehicle occlusions can break temporal cues. In streaming recurrent models, corrupted observations may enter the hidden state and produce errors that persist into later frames. Existing occlusion-aware refinements usually provide obstacle masks as auxiliary inputs, so the state-update path is only indirectly protected. We propose SIGMA-Lane, which treats this failure mode as state contamination in State Space Model (SSM)-based temporal modeling. SIGMA-Lane places occlusion-aware gates on the SSM write and residual-fusion paths, controlling how current observations enter temporal memory and are fused back after temporal propagation. After coordinate-consistent affine alignment, the model combines two complementary paths: SSM-consistent dual-gating for temporal filtering and Structural Spatial Retrieval (SSR) for recovering missing lane structure from aligned historical priors. Experiments on VIL-100 and OpenLane-V show improved temporal stability under heavy occlusion, with competitive F1 and mIoU scores.

---


### 350. [Task-Anchored Representation Shaping for Pre-Trained Model-Based Continual Learning](https://arxiv.org/abs/2608.16345)

**<font color=#1a73e8>作者：</font>** Zhiming Xu, Huiyu Yi, Zhen-Hao Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-trained models (PTMs) provide a strong foundation for continual learning by offering stable representations that facilitate lightweight adaptation to new tasks. However, adapting well to each task does not ensure reliable inference over all learned tasks. Since task boundaries are often artificial and semantically entangled, an input from an unknown task can remain ambiguous even with strong PTM features, making cross-task prediction a key bottleneck. We propose Task-Anchored Inference Latent Shaping (TAILS), a lightweight post-PTM module that can be integrated into diverse continual learners and optimized through a decoupled step. TAILS uses fixed task anchors as persistent references to accumulated knowledge. It interprets each sample's feature representation relative to these references, then composes relevant evidence across tasks into latent recall. Rather than selecting a task-specific path or adjusting classifier outputs, TAILS uses latent recall to directly correct the feature representation before prediction. It therefore resolves cross-task ambiguity at the representation level, while leaving the original PTM, method-specific modules, and classifier unchanged. Extensive experiments across multiple PTM-based continual learning paradigms show that TAILS can improve classification and task-inference performance with modest parameter overhead and negligible inference cost.

---


> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-435](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
