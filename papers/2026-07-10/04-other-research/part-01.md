# 📦 其他研究 | 2026年07月10日

> 本类共 **207** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-207](./part-05.md)

---

### 1. [Pixel-Precise Explainable Stress Indexing: A Semantic Segmentation Framework for Disease Severity Quantification in Field Crops](https://arxiv.org/abs/2607.06585)

**<font color=#1a73e8>作者：</font>** Raunak Kumar, Soumyashree Kar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Plant diseases, resulting from both biotic and abiotic stresses, cause an estimated 20-40% loss in global agricultural yield annually, resulting in economic damages exceeding USD 220 billion. Accurate and scalable stress quantification is essential for precision agriculture, yet traditional manual assessments are labour-intensive and subjective. This paper proposes a unified deep learning pipeline integrating semantic segmentation, regression-based severity estimation, and disease classification. Stress severity is categorised into four levels (Low to Very High) based on the proportion of infected leaf area. Experiments on the Apple Tree Leaf Disease Segmentation dataset (1,641 samples, six classes) evaluate four models: U-Net (MobileNetV2), SegFormer, FCN, and PSPNet. U-Net with MobileNetV2 achieves the best performance with 98.20% pixel accuracy, 0.70 mIoU, and 99.41% detection accuracy at 14.7 ms per image, making it suitable for real-time use. SegFormer performs competitively (mIoU 0.66), while FCN and PSPNet show lower spatial accuracy (approximately 0.49 mIoU). The computed severity index strongly correlates with expert annotations (r = 0.968, R^2 = 0.937), demonstrating the system's reliability for automated crop monitoring and decision support.

---


### 2. [CoFINN: Conservation Flux Informed Neural Networks for Physics Problems Governed by Conservation Laws](https://arxiv.org/abs/2607.06587)

**<font color=#1a73e8>作者：</font>** Adnan Harun Doğan, Mert Deniz, Hande Alemdar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present CoFINN (Conservation Flux Informed Neural Networks), a physics-informed deep learning framework for predicting compressible flow fields governed by conservation laws. Unlike conventional data-driven convolutional neural networks (CNNs), which optimize only pixel-wise similarity metrics, CoFINN embeds finite-volume conservation physics directly into the training process. Unlike classical physics-informed methods which enforce differential-equation residuals at collocation points through automatic differentiation, CoFINN adopts a finite-volume perspective consistent with modern CFD methodology. CoFINN interprets CNN output fields as structured computational grids, where each pixel represents a finite-volume cell, and enforces conservation consistency through sophisticated numerical flux calculations. The framework is evaluated on transonic flow prediction around airfoils at (M=0.7, Re=6 * 10^6), including challenging conditions involving shock waves and high angles of attack. Results show that CoFINN improves aerodynamic force prediction accuracy, reducing drag prediction error by up to 34% at extreme angles of attack and by approximately 15% on average across the test set. Improvements are particularly significant in limited-data regimes, demonstrating that the conservation-based loss acts as an effective physical regularizer. The proposed approach maintains the computational efficiency advantages of CNN surrogates while significantly improving physical consistency and conservation behavior. The framework is architecture-agnostic and extensible to broader classes of conservation-law-governed physical systems.

---


### 3. [AI for Cultural Heritage Textiles: Fine-Tuned Latent Diffusion for Novel Ulos Motif Synthesis](https://arxiv.org/abs/2607.06590)

**<font color=#1a73e8>作者：</font>** Humasak Tommy Argo Simanjuntak, Jesika Purba, Sitogab Girsang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Preserving and revitalising traditional textiles such as Ulos, a cultural heritage of the Batak ethnic group in North Sumatra, Indonesia, requires balancing fidelity to tradition with innovative approaches that meet contemporary design demands. Traditional Ulos weaving faces two key limitations: a narrow range of motifs and a time-intensive design process. This study presents a generative AI framework that fine-tunes two pretrained latent diffusion models: Protogen v3.4 and Stable Diffusion v1.4, on a curated, annotated dataset of high-resolution Ulos motifs to generate culturally consistent yet novel designs. Model performance is evaluated quantitatively using Frechet Inception Distance (FID), Inception Score (IS), and qualitatively through assessments by traditional weavers and members of the public. Protogen v3.4 consistently outperforms Stable Diffusion v1.4, achieving substantially lower FID (~10.5x) and higher IS (2.0x), indicating superior visual fidelity, diversity, and closer alignment with the real Ulos motif distribution. We further examine the effects of strength and guidance scale on generation quality across both models. Lower strength values consistently yield higher fidelity (lower FID), while higher strength values increase generative diversity at the cost of realism, revealing a clear fidelity-diversity tradeoff for both models. Across all tested configurations, a guidance scale of 5-9 provides the most effective balance between fidelity and diversity, stabilising FID, KID, and IS, and is recommended as the operating range for high-quality, diverse Ulos motif generation. These findings demonstrate that carefully fine-tuned generative AI can support the creative renewal of intangible cultural heritage while preserving its stylistic and symbolic integrity.

---


### 4. [LipSSD: Lipschitz-Constrained Single-Shot Detection for Adversarially Robust Object Detection](https://arxiv.org/abs/2607.06592)

**<font color=#1a73e8>作者：</font>** Vincent Lébé, Yannick Prudent, Corentin Friedrich 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detectors have many applications in safety-critical systems, but they are known to be sensitive to worst-case perturbations such as adversarial attacks, which limits their applicability in real-world scenarios. Compared with classification, adversarial robustness for object detection has received less attention, and existing methods are often tied to adversarial training, whose performance may not transfer across attacks, perturbation budgets, or architectures. In this work, we introduce Lipschitz-constrained variants of object detection architectures as robust-by-design alternatives to standard detectors. We validate this approach with LipSSD, a Lipschitz-constrained Single Shot MultiBox Detector (SSD), and provide a comprehensive study of its adversarial robustness using multiple white-box adversarial attacks and datasets. We first analyze the accuracyrobustness trade-off induced by Lipschitz constraints and show that it can be controlled through a single training hyperparameter. We then demonstrate that Lipschitzconstrained detectors are complementary to adversarial training: under the same training setup on the Pascal VOC dataset, adversarially trained LipSSD improves mAP@50 on unseen attacks by up to 15 points over classical adversarially trained SSD. Finally, we use more specific safety-critical datasets such as LARD and KITTI, and show that Lipschitz-constrained detectors can improve robustness while largely preserving clean performance. These results suggest that architectural Lipschitz control is a practical and attack-agnostic direction for improving the robustness of object detectors.

---


### 5. [Blockchain Attacks and Defenses: A Layered and Cross-Domain Survey](https://arxiv.org/abs/2607.06593)

**<font color=#1a73e8>作者：</font>** Junjie Hu, Na Ruan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchains have evolved from simple distributed ledgers into programmable platforms that process complex application logic and carry significant financial value. All modern Web3 systems share a common goal: providing secure, decentralized, and trustworthy execution in an increasingly interconnected environment. However, this evolution has shifted the attack surface from isolated infrastructure disruptions to programmable economic abuse and cross-domain exploits. In this article, we focus on the research of blockchain attacks and defenses. In particular, we categorize the threat landscape and corresponding mitigation strategies according to both a four-tier layered architecture (network, cryptographic, consensus, and application) and cross-domain trust boundaries. We seek to answer these important questions: How has the research in blockchain security evolved over the past decade, especially with the rise of decentralized finance (DeFi) and cross-chain interoperability? How do local security assumptions fail when protocols are composed, and what are the driving needs for Web3 security research in the future?

---


### 6. [Calibration-Family Overfit: Why Trusted Sabotage Monitors Don't Transfer Across Lineages](https://arxiv.org/abs/2607.06596)

**<font color=#1a73e8>作者：</font>** Lucas Pinto  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted monitoring is a central defense in AI control: a cheaper trusted model scores an untrusted model's actions for sabotage, and the most suspicious are audited or deferred. Such monitors are evaluated against one or two untrusted models, and the accuracy is reported as a property of the monitor. We ask whether it is partly a property of the pairing. We make the untrusted policy family the controlled axis: we fit a monitor on family A's transcripts, apply it to family B, and decompose the cross-family AUROC into how obvious each family's sabotage is, how capable each monitor is, and the residual own-family advantage after both are removed: the interaction. On code-backdoor transcripts the interaction is positive and survives the dominant confounds: +0.172 (95% CI [+0.158, +0.185]) on four open-weight families on a strict leak-free basis, holding across an eight-family matrix spanning four frontier vendors, blatancy-matched controls, a trained transcript-reading monitor up to 34B parameters, and a second code benchmark. The gap is geometric: each lineage's sabotage occupies a different scoring direction, and rotating the monitor's scoring direction toward the target lineage recovers most of the lost detection while a matched random rotation recovers nothing. At a 1% audit budget under defer-to-trusted, an off-lineage monitor catches 19% of attack attempts where an in-lineage monitor catches 41% at the same audit cost, a +21.7-point gap. Control evaluations should report cross-family transfer matrices: a single-pairing accuracy overstates the safety a monitor delivers against a lineage it was not calibrated on. We give a four-step protocol that acts on the gap, with each step a measured result.

---


### 7. [MiLSD: A Micro Line-Segment Detector for Resource-Constrained Devices](https://arxiv.org/abs/2607.06600)

**<font color=#1a73e8>作者：</font>** Parsa Hassani Shariat Panahi, Amir Hossein Jalilvand, M. Hassan Najafi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Line segment detection is a key building block in visual SLAM, 3D reconstruction, and industrial inspection. Recent deep learning methods have greatly improved accuracy, yet even the smallest models require several megabytes of memory, exceeding low-cost MCU capacity. This work investigates the maximum achievable accuracy under a sub-megabyte budget. We propose MiLSD, a detector tailored for MCU-level constraints, and systematically compare three output representations within a compact fully-convolutional backbone. Our study shows that the proposed F-Clip center-with-length-and-angle formulation learns most effectively at small model sizes. We find that 8-bit quantization preserves full-precision performance, while 4-bit quantization causes significant degradation, particularly in angle regression, with quantization-aware training recovering only part of the loss. With a one-megabyte activation budget and inference enhancements including sub-pixel decoding, test-time augmentation, and a lightweight verifier, MiLSD improves sAP10 on ShanghaiTech Wireframe from 10.6 (25k parameters, 0.25 MB) to 24.1 within 1 MB. Rather than competing with GPU-scale parsers, we map the accuracy memory trade-off across representations, bit-widths, capacities, and post-processing strategies for embedded vision systems.

---


### 8. [TriRoute: Unified Learned Routing for Joint Adaptive Attention, Experts, and KV-Cache Allocation](https://arxiv.org/abs/2607.06601)

**<font color=#1a73e8>作者：</font>** Andrii Balashov, Olena Ponomarova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conditional computation can decouple language model quality from per-token inference cost, yet leading techniques act on a single axis in isolation: Mixture-of-Experts (MoE) sparsifies the FFN, Mixture-of-Depths (MoD) skips whole transformer blocks, and KV-cache quantization compresses attention memory. We argue these three decisions (attention resolution, expert selection, and cache bit-width) are strongly coupled and should be made jointly: a token rare enough to warrant full attention may also need high-precision caching regardless of which expert processes it. We introduce TriRoute, a single lightweight controller shared across all three axes that, for every token at every layer, emits a coordinated policy: (i) an attention mode (skip/local/full), (ii) a sparse set of FFN experts (with a null expert recovering MoD), and (iii) a KV-cache bit-width. The controller trains end-to-end via a heterogeneous relaxation (Gumbel-Softmax with straight-through estimation for categorical decisions and load-balanced top-k gating for experts) under a Lagrangian budget constraint that turns the average compute and memory cost into a controllable knob. We identify a cross-axis routing-collapse cascade in naive joint training, where collapse on one axis propagates to the others, and address it with per-axis normalization and a coupling-aware balancing loss. On decoder-only models from 160M to 1.3B parameters at compute-optimal token counts, TriRoute Pareto-dominates the best independent MoD+MoE+KV-quantization combination at matched inference FLOPs and memory, while better preserving tail-case robustness on rare entities, code, and arithmetic that pure perplexity optimization erodes. Post-hoc analysis reveals interpretable structure: the controller allocates full attention and high-precision cache to sentence-initial positions, rare subwords, and named entities, while cheaply routing function words.

---


### 9. [Do Counterfactually Fair Image Classifiers Satisfy Group Fairness? -- A Theoretical and Empirical Study](https://arxiv.org/abs/2607.06603)

**<font color=#1a73e8>作者：</font>** Sangwon Jung, Sumin Yu, Sanghyuk Chun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The notion of algorithmic fairness has been actively explored from various aspects of fairness, such as counterfactual fairness (CF) and group fairness (GF). However, the exact relationship between CF and GF remains to be unclear, especially in image classification tasks; the reason is because we often cannot collect counterfactual samples regarding a sensitive attribute, essential for evaluating CF, from the existing images (\eg, a photo of the same person but with different secondary sex characteristics). In this paper, we construct new image datasets for evaluating CF by using a high-quality image editing method and carefully labeling with human annotators. Our datasets, \oursceleb and \ourslfw, build upon the popular image GF benchmarks; hence, we can evaluate CF and GF simultaneously. We empirically observe that CF does not imply GF in image classification, whereas previous studies on tabular datasets observed the opposite. We theoretically show that it could be due to the existence of a latent attribute $G$ that is correlated with, but not caused by, the sensitive attribute (\eg, secondary sex characteristics are highly correlated with hair length). From this observation, we propose a simple baseline, Counterfactual Knowledge Distillation (CKD), to mitigate such correlation with the sensitive attributes. Extensive experimental results on \oursceleb and \ourslfw demonstrate that CF-achieving models satisfy GF if we successfully reduce the reliance on $G$ (\eg, using CKD).

---


### 10. [A Quiet Failure in Calibrated Virtual Screening: Marginal Conformal Prediction Under-Covers the Minority Class, and a Class-Conditional Fix Recovers It](https://arxiv.org/abs/2607.06605)

**<font color=#1a73e8>作者：</font>** Muhammadjon Tursunbadalov, Mustafojon Tursunbadalov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction is being adopted in drug discovery to put an honest number on model reliability: pick an error rate alpha, and the method returns prediction sets containing the true label with probability at least 1 - alpha. We show this guarantee can be dangerous on imbalanced datasets. Across four datasets, standard (marginal) conformal prediction hits its global 90% coverage target while leaving the minority class badly exposed: realized minority coverage falls to 64.8% on blood-brain-barrier penetration and to 4.2% on clinical-trial toxicity, where the rare class is nearly abandoned. The failure is not tied to one model: a random forest, a graph network, and a frozen chemical language model all reproduce it (p < 0.001 in every case), with severity tracking baseline calibration on rare labels rather than architecture. A conservation identity explains the effect: the minority's shortfall equals the majority's surplus amplified by the imbalance ratio, predicting the measured gap to within one point and ordering severity across datasets. The failure survives realistic scaffold splits and a second conformal score, while aggregate accuracy and overall coverage stay reassuringly high, which is exactly why it is easy to miss. Class-conditional (Mondrian) conformal prediction closes the gap on every dataset, restoring minority coverage to target for a modest increase in prediction-set size. We localize the failures to generic molecular scaffolds - plain benzene and pyridine cores occurring in both classes - propose a one-number diagnostic, and show with a cost model that abstaining on affected compounds flips a screening campaign from net-negative to net-positive utility. Our contribution is demonstrating on real chemistry how severe and invisible this known conformal-theory gap becomes under imbalance, and laying out a practical protocol restoring per-class reliability.

---


### 11. [NEST: Tackling Dataset-Level Distribution Shifts via Regime-Oriented Mixture-of-Experts](https://arxiv.org/abs/2607.06607)

**<font color=#1a73e8>作者：</font>** Lanhao Li, Bingshu Xie, Lijun Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate long-term forecasting in complex systems is frequently compromised by dataset-level distribution shifts, where diverse underlying behavioral modes and evolving system states drive the dynamic multivariate time-series. While existing methods predominantly focus on local temporal shifts, they fail to explicitly model the global structural challenge where datasets are composites of distinct operational regimes. In this paper, we propose NEST, a specialized framework designed to model and recompose these evolving structures through a two-phase dense MoE architecture. NEST first facilitates structural specialization by partitioning the dataset into distinct operational regimes through unsupervised clustering in a principled moment-entropy space. We introduce a regime-oriented router mechanism that generates initial expert weights based on temporal content, subsequently refined through geometric modulation to regime centroids. Crucially, rather than acting as monolithic predictors, individual experts function as specialized kernels that capture regime-specific dynamics by evolving unique variate-attention patterns. Extensive evaluations on diverse benchmarks, including heterogeneous network traffic and physical phenomena, demonstrate that NEST consistently achieves state-of-the-art performance. Our code and datasets are available at this https URL

---


### 12. [D2PO: Optimizing Diffusion Samplers via Dynamic Preference](https://arxiv.org/abs/2607.06609)

**<font color=#1a73e8>作者：</font>** Jinkyu Kim, Jinyoung Choi, Bohyung Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose D2PO (Dynamic Direct Preference Optimization), a principled framework for optimizing diffusion sampling policies with respect to timestep schedules and classifier-free guidance (CFG) weights. Our work is motivated by a fundamental limitation of existing student-teacher regression frameworks; low-NFE student samplers are trained to mimic high-NFEteachers, often sacrificing high-frequency texture fidelity while preserving coarse global structures, thereby misaligning the sampler with perceptual quality. D2PO addresses this challenge by reformulating sampler optimization as a preference-based alignment problem, leveraging the Direct Preference Optimization (DPO) framework. To make DPO applicable to diffusion samplers, we model the sampling policy as an energy-based model (EBM), transforming preference comparisons into tractable energy differences. We further introduce a novel energy formulation derived directly from the pretrained score network, enabling preference evaluation in perturbed spaces that jointly capture structural consistency and fine-grained details. Moreover, we introduce dynamic preferences, where the preferred samples used for alignment progressively improve as the sampling policies are learned. This self-improving mechanism replaces rigid static teacher supervision with an iterative, preference-guided refinement process, providing progressively stronger alignment signals. Extensive experiments demonstrate that D2PO aligns diffusion samplers with perceptual quality more faithfully, unlocking the full potential of high-quality teachers and consistently outperforming conventional regression-based schedulers under low-NFE constraints.

---


### 13. [Deep Reinforcement Learning for Reliability Based Bi-Objective Portfolio Optimization](https://arxiv.org/abs/2607.06610)

**<font color=#1a73e8>作者：</font>** Sounaq Das, Tanmay Sen, Raghu Nandan Sengupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Portfolio optimization under uncertainty is inherently a multi-objective decision problem involving complex interactions among return, risk, market dynamics, and practical investment constraints. Existing reliability based portfolio optimization approaches primarily rely on static optimization frameworks and often fail to capture sequential decision making, tail risk, and market frictions such as transaction costs. To address these limitations, we propose a deep reinforcement learning framework for multi-objective reliability based portfolio optimization (MORP-DRL). The proposed framework jointly optimizes expected return and downside risk using three complementary risk measures: variance, Conditional Value-at-Risk (CVaR), and Entropic Value-at-Risk (EVaR). To model uncertainty and heavy-tailed market behavior, asset returns are represented using GARCH(1,1), Extreme Value Theory, and a t-copula dependence structure, while realistic scenarios are generated through quasi-Monte Carlo simulation. A Proximal Policy Optimization (PPO) based strategy is developed under practical constraints including transaction costs and portfolio bounds, and is benchmarked against NSGA-II. Experiments on ten global equity indices across pre-COVID, COVID, and post-COVID market regimes demonstrate that MORP-DRL achieves competitive risk-return performance, reduced downside risk during periods of market stress, and scalability to high-dimensional portfolio settings.

---


### 14. [Audio Sentiment Analysis via Distillation and Cross-Modal Integration of Generated Multilingual Transcripts](https://arxiv.org/abs/2607.06611)

**<font color=#1a73e8>作者：</font>** Andrei-George Durdun, Victor Constantinescu, Radu Tudor Ionescu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatically recognizing the sentiment, positive or negative, from speech is a challenging task, requiring both the analysis of vocal inflections and the interpretation of uttered words. Recent solutions rely on audio foundation models to solve the task, but it remains unclear if such models can take all aspects into account. To this end, we propose a multimodal solution that integrates audio and text information via cross-modal transformers, where text transcripts are automatically generated via an automatic speech recognition (ASR) tool. Moreover, we create multiple text modalities by automatically translating the transcripts into multiple languages via machine translation tools. Audio and multilingual text features are combined via a cascaded architecture comprising cross-modal transformer blocks that integrate modalities one by one. We further distill knowledge from the multimodal model, called teacher, into a unimodal (audio only) model, called student. We conduct experiments on a large-scale dataset, demonstrating that the automatically generated textual information can bring significant performance boosts in multimodal sentiment polarity classification. Our ablation study confirms that both automatic transcripts and automatic translations are helpful. Moreover, we show that the audio-only model can be enhanced via distillation, boosting performance without any computational overhead during inference. To reproduce the reported results, we publicly release our code at this https URL.

---


### 15. [PRoVeFL: Private Robust and Verifiable Aggregation in Federated Learning](https://arxiv.org/abs/2607.06612)

**<font color=#1a73e8>作者：</font>** Harsh Kasyap, Anil Kumar Pradhan, Ugur Ilker Atmaca 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables multiple clients to collaboratively train machine learning models while retaining data locality, thereby enhancing user privacy. However, traditional FL frameworks rely on a centralized aggregation server and assume honest-but-curious clients, making them susceptible to both server-side inference and client-side poisoning attacks. Although recent work has explored secure and Byzantine-resilient FL protocols, they face a fundamental trade-off among privacy, integrity, and verifiability, and incur substantial computational and communication overhead due to the heavy use of cryptographic primitives. In this work, we propose PRoVeFL-a novel, modular FL framework that is Privacy-preserving, Byzantine-Robust, and ensures Verifiable aggregation. PRoVeFL employs multiple servers leveraging multi-key fully homomorphic encryption. Each client encrypts its local model updates and distributes encrypted shares to all servers. This design enables a hybrid computation model in which ciphertext operations are carefully offloaded to the plaintext domain under strict privacy constraints to efficiently evaluate complex statistical aggregation rules. PRoVeFL is compatible with a wide range of state-of-the-art Byzantine-robust aggregation algorithms (e.g., Krum, Trimmed Mean, FLTrust, norm clipping, MESAS, and more) and further enhances them with verifiability mechanisms that require minimal trust in at least one honest server. We evaluate it across different settings and demonstrate its scalability with varying numbers of parameters and participants. PRoVeFL improves runtime over the prior works, Prio and ELSA, based on distributed trust with comparable security guarantees, up to 100x and 10x, respectively.

---


### 16. [STAGformer: A Spatio-temporal Agent Graph Transformer for Micro Mobility Demand Forecasting](https://arxiv.org/abs/2607.06614)

**<font color=#1a73e8>作者：</font>** Ye Zihao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate station-level demand forecasting is essential for the efficient operation of bike-sharing systems, yet it remains challenging due to complex spatio-temporal dependencies and the large scale of urban networks. This paper presents STAGformer, a Spatio-Temporal Agent Graph Transformer that achieves efficient global modeling with linear computational complexity. The model introduces a two-step agent attention mechanism, where a small set of learnable spatial and temporal agent tokens first aggregate global information and then broadcast it back to individual stations and time steps, effectively capturing long-range interactions while reducing the quadratic cost of standard self-attention to O(NT). STAGformer integrates four core modules: a spatio-temporal encoder that fuses dynamic node features with external contextual factors (weather, time, points of interest), a graph propagation module for spatial neighbor aggregation, a temporal convolution module for local pattern extraction, and the agent attention module for global dependency modeling. Extensive experiments on two real-world datasets -- NYC Citi-Bike and Chicago Divvy-Bike -- demonstrate that STAGformer consistently outperforms state-of-the-art baselines across multiple prediction horizons, achieving significant improvements in both RMSE and MAE. Ablation studies validate the contribution of each component, with the agent attention mechanism proving critical for modeling global spatio-temporal dependencies.

---


### 17. [WHERE to Generate Matters: Budget-Aware Synthetic Augmentation for Label Skewed Federated Learning](https://arxiv.org/abs/2607.06616)

**<font color=#1a73e8>作者：</font>** Sangwoo Lee, Sunghwan Park, Jaewoo Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Label skew in federated learning (FL) causes client drift and degrades global accuracy. Synthetic data augmentation can reduce this imbalance; however, full class balancing requires substantial computation cost. We propose FedEAS, a policy that assigns each client an entropy-adaptive per-class generation budget computed from its local label distribution. The budget jointly decides \emph{how much} each client generates and \emph{WHERE} the samples go. Accordingly, the total generation budget follows from the per-client budgets rather than being fixed in advance. FedEAS recovers most of the accuracy gain of full class balancing while reducing the generation budget by 94.1\%. At the same total generation budget, it outperforms Uniform allocation by up to 18.82\% across CIFAR-10 and CIFAR-100.

---


### 18. [Fingerprint, Not Blueprint: How Positional Schemes Set the Default Spectral Algebra of Attention](https://arxiv.org/abs/2607.06621)

**<font color=#1a73e8>作者：</font>** Li Hengyu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The pre-softmax score of an attention head is a bilinear form $score(i,j) = x_i^T M x_j$ in a learned operator $M = W_q^T W_k$. Because M is generally non-symmetric, hence non-normal, it has a complex eigenspectrum and non-orthogonal eigenvectors, the regime where non-Hermitian and random-matrix tools apply. We ask what this spectrum encodes, at three levels for previous-token and induction circuits. Statically, across seven pretrained models spanning three positional schemes, the strongest previous-token heads are spectrally rotational under RoPE and non-rotational, or content-like, where position enters outside QK (learned-absolute and ALiBi); the model-level separation is perfect at every top-k examined (exact permutation $p=0.029$), and zeroing the per-frequency RoPE phase $Im(M_t)$ eliminates induction on a pre-identified previous-token head in all three RoPE models. Dynamically, over public Pythia checkpoints every head originates at the random-matrix (Ginibre) null; the rotational signature emerges with the behavior, not before it, and the population-median suppression that yields the final profile follows circuit formation, so the profile is a consolidated fingerprint, not a precursor. Causally, and at toy scale, no spectral channel is necessary: constrained two-layer training reroutes around every ban with capability intact, albeit at a significant formation delay (four pre-registered contrasts, $q_BH <= 0.016$). The cost structure exposes each scheme's default: imposing symmetry slows learned-absolute models by a factor of 2.9, whereas a RoPE head with a fully symmetric static M still routes directionally via the phase channel, impossible under absolute positions. Within the settings examined, the positional scheme sets the default spectral algebra of an attention head's solution: a fingerprint sculpted after function, not a hard constraint upon it.

---


### 19. [AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation](https://arxiv.org/abs/2607.06624)

**<font color=#1a73e8>作者：</font>** Andrey Podivilov, Vadim Lomshakov, Sergey Savin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present AgentLens, a production-assessed benchmark for interactive code agents. Most code-agent benchmarks reduce a run to a single bit -- did the task pass? -- but the people who actually use these agents experience the entire trajectory: how the agent follows instructions, uses its tools, verifies its own work, recovers from mistakes, and talks to them along the way. AgentLens evaluates that whole trajectory. It pairs formal verification, where an objective check exists, with LLM-written trajectory reviews and side-by-side comparisons, so that each run yields a readable explanation of why the score is what it is. This makes AgentLens useful for more than ranking models: we use it to diagnose model behavior, compare successive versions of our own agent, and catch product regressions in a nightly evaluation pipeline. We release the benchmark as open source at this https URL.

---


### 20. [Open-Ended Scenario Reasoning for Specialist Model Adaptation](https://arxiv.org/abs/2607.06625)

**<font color=#1a73e8>作者：</font>** Youcheng Zong, Runda Jia, Ranmeng Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Process industries have accumulated validated specialist models, yet sensor drift, feedstock variation, and regime switching cause these models to degrade systematically in new scenarios. Collecting new labeled data and retraining is costly, while continuing with the original model incurs persistent bias. Existing adaptation methods require modifying model parameters with sufficient labeled data, making rapid response on deployed systems difficult. Using LLMs as direct predictors risks hallucinations and uncontrollable outputs. Such predictors also cannot incorporate unstructured scenario knowledge from the field. To address these limitations, this article proposes Reasoning-Driven Open Adaptation for Specialist Models (ROAM), a framework that uses LLM world knowledge and reasoning to adapt frozen specialist models to unseen scenarios without retraining. ROAM confines all corrections to a low-dimensional, semantically interpretable latent space. LLM-generated scenario judgments and online observations are fused under a unified probabilistic framework. A risk-constrained mechanism suppresses corrections under unreliable LLM evidence or abrupt scenario shifts and falls back to the original frozen model when evidence is insufficient. Experiments on a mineral thickening process and the public IndPenSim penicillin fermentation dataset show that ROAM reduces MAE by over 20\% in major shift settings such as hidden shifts with only 839 additional parameters and under 0.02\,ms per-step overhead. These results indicate that LLM reasoning can be turned into a conservative adaptation signal for industrial models already in service.

---


### 21. [Cross-Trajectory Chimera Interventions Reveal Dissociable Roles of Weight Magnitude and Direction in Grokking](https://arxiv.org/abs/2607.06628)

**<font color=#1a73e8>作者：</font>** Truong Xuan Khanh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Which properties of a partially trained network are causally portable to a different, independently trained network? Single-trajectory interventions show necessity within one run, not portability across runs. We introduce cross-trajectory chimera interventions: given two runs from different seeds, we split each weight vector into a norm and a unit direction, recombine one run's norm with the other's direction, and continue training. On two modular-arithmetic tasks that grok, the components dissociate. Direction carries a transferable, donor-specific circuit identity: implanting a donor's direction at the recipient's norm drives the run to the donor's circuit in 40/40 cases, while an angle-matched random control yields no shift. The transfer is threshold-like, and its location is predicted by the recipient's norm, separating perfectly by norm class over all 20 pairs (joint permutation probability 1.9e-4). Norm carries only a modest, distributed delay effect and no identity signal. An adaptive bisection procedure localizes the threshold to +/-1/64. Direction indexes which solution a trajectory approaches; norm governs how susceptible that identity is to being overwritten.

---


### 22. [STST-JEPA: Shallow-Target Spatio-Temporal Joint Embedding Prediction Architecture For EEG Self-Supervised Learning](https://arxiv.org/abs/2607.06629)

**<font color=#1a73e8>作者：</font>** Roy Segal, Yoni Svechinsky, Tomer Fekete  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Brain age -- the age inferred from a physiological recording -- is an emerging biomarker whose deviation from chronological age tracks neurological and psychiatric burden, and EEG is an attractive substrate for it because it is cheap, portable, and temporally rich. Yet EEG brain-age models must contend with cross-site montage heterogeneity, small labelled cohorts, and dominant subject-level non-stationarity, and few EEG foundation models have been shown to deliver competitive age regression across the full pediatric-to-older-adult range in which such a biomarker would actually be deployed. We introduce STST-JEPA, a self-supervised transformer for resting-state and task EEG, pretrained on 47,703 sessions spanning ages 5-81 from the this http URL and Healthy Brain Network (HBN) corpora. The model combines a latent-prediction objective - predicting masked-token representations against an EMA-of-tokenizer target - with an auxiliary signal-reconstruction term, applied to 30-second multi-channel windows under spatiotemporal block masks. A lightweight attentive probe trained on frozen pretrained embeddings achieves a best held-out-validation mean absolute error of 3.06 years (r = 0.924) for age regression on 3,367 sessions, against a predict-the-mean baseline of approximately 10 years MAE. With light task-specific fine-tuning of the model's final layers, the same pretrained encoder achieves rank-1 placements - with the model's native 30-second windows - on the public NeuralBench x this http URL EEG leaderboard for sex classification (balanced accuracy 0.911), age prediction (r = 0.749), and psychopathology composite regression (r = 0.215). We further show that the model's age-prediction residual is negatively correlated with cognitive efficiency over several tasks we examined.

---


### 23. [When Certificates Fail: A Unified Safety Framework for Embedded Neural Interface Models](https://arxiv.org/abs/2607.06630)

**<font color=#1a73e8>作者：</font>** Jasmeet Singh Bindra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Formal robustness certificates for embedded neural-interface models can pass while task accuracy collapses: at perturbation budget e=0.25, EEGNet classification accuracy drops by 25.7% under projected-gradient attack while the Lipschitz-style certificate remains valid for all 9 tested subjects. We argue that this gap between mathematical certification and operational safety is one instance of a broader alignment failure in neural interfaces, where training objectives diverge from user welfare. We propose a unified empirical audit framework organized around three such failures: verification insufficiency, in which certificates pass while task behavior degrades; proxy-fidelity divergence, in which task-optimized representations damage neural signal structure (a time-domain auxiliary objective reduces reconstruction MSE by 0.1132 while worsening spectral log-MSE); and latent information exfiltration, in which public-task embeddings retain private attributes (subject identity recoverable at 48.1% versus 6.7% chance). We instantiate the framework on BCI Competition IV 2a and SEED-IV using multiple deep and classical EEG decoders, official session-level validation, null controls, and paired statistical tests. The verification gap persists across EEGNet, CSP+LDA, and FBCSP+LDA, and is therefore architecture-independent. Our results establish that operational safety auditing, not certificate verification alone, is necessary for responsible neural-interface deployment.

---


### 24. [Dynamic-in-Few-Step: Unifying Dynamic Computation and Few-Step Distillation for Efficient Video Generation](https://arxiv.org/abs/2607.06631)

**<font color=#1a73e8>作者：</font>** Yu Cheng, Siyue Yao, Zhongang Qi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Diffusion Models (VDMs) have demonstrated superior generation quality but suffer from prohibitive computational costs. While recent few-step distillation techniques significantly accelerate inference, they typically enforce a static model architecture across all denoising stages, ignoring the varying computational demands inherent to different noise levels. In this work, we propose a novel post-training acceleration framework that exploits this redundancy by integrating dynamic structural sparsification directly into the distillation process. Unlike conventional post-hoc compression applied to a fixed diffusion pipeline, our approach jointly optimizes the denoising steps and structured model sparsity, transforming a pre-trained VDM into a compact, step-specific Mixture-of-Models (MoM). To address the training instability arising from this joint optimization, we introduce a Progressive Training Strategy coupled with an Output Rollout Mechanism, which ensures the coherent learning of structural decisions across timesteps. Furthermore, we develop a specialized inference engine to deploy the resulting MoM efficiently. Our method is orthogonal to existing acceleration techniques and highly effective: On Wan-14B, it removes 24% of the per-step FLOPs on top of 4-step distillation, adding a 1.2x wall-clock gain and reaching a 30x speedup over the 50-step teacher while preserving competitive generation quality.

---


### 25. [Does Demand Response Increase Vulnerability to Cyber Attacks by Adversarial Data Modifications?](https://arxiv.org/abs/2607.06632)

**<font color=#1a73e8>作者：</font>** Clemens Kortmann, Eike Cramer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks are crafted data manipulations that aim to deteriorate the outcomes of prediction or decision-making algorithms. In the energy systems literature, adversarial attacks have been studied with a focus on problems regarding the electricity grid. Such problems include forecasting and grid state estimation, where adversarial attacks are also known as false data injection attacks. Only few studies have analyzed the potential impact that adversarial attacks have on the demand side. We analyze how manipulated price forecasts impact the decision-making in industrial demand response. To this end, we design adversarial attacks that aim to deteriorate the output of electricity price forecasting models and solve scheduling optimization problems of energy-intensive production processes using the distorted price forecasts. We make use of a generalized process model to investigate the vulnerability to adversarial attacks for a range of production scheduling problems with different levels of process flexibility. We find that adversarial attacks can erode the profits gained from demand response. However, when perturbations are limited in extent (so that they are hard to detect by the human user), demand response preserves about 90\% of its financial advantage compared to steady-state process operation. Further, we find that the impact of adversarial attacks on demand response does not only depend on the magnitude of the perturbations but rather on the orientation of the adversarial perturbations. Therefore, we argue that attack analyses should explicitly incorporate the sensitivities of scheduling optimization models into the attack design to enable more rigorous assessments of decision-making under adversarial attacks.

---


### 26. [When Do Geometric Algebra Layers Beat Scalarization? A Controlled Study on SO(3)-Equivariant Vector Laws](https://arxiv.org/abs/2607.06634)

**<font color=#1a73e8>作者：</font>** Fabien Polly  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compact networks built from Clifford algebra Cl(3,0) primitives are exactly SO(3)-equivariant and learn synthetic 3D vector laws from few samples. We ask whether the geometric algebra structure itself contributes anything beyond exact equivariance. We compare against a minimal scalarization baseline: invariant dot products fed to a small MLP that outputs coefficients on the equivariant basis {v_i, v_i x v_j}, which is also exactly equivariant. On single-stage laws (rotation by axis-angle, cross product, central force), scalarization matches or beats the Cl(3,0) network at a fraction of the training cost, so the geometric algebra adds nothing there. On compositional targets whose computation graph nests group operations (apply R2 R1 to a point; map a local force through an orientation, then take a torque), the Cl(3,0) network beats scalarization by an order of magnitude in the low-data regime, reaching with 100 samples what the baseline needs 3000 for, and the gap survives strengthening the baseline with the triple-product invariant and 17x more parameters, external Vector Neurons and e3nn baselines, and a multiplicative coefficient network. Ablations show the required network depth tracks the rotation chain length, and scalarization falls below the constant predictor on chains of four rotations. The advantage is not composition per se: on a rotation-free nested cross product, which flattens into polynomial invariant coefficients, scalarization wins by 24x. No tested model, equivariant or not, extrapolates invariant magnitudes: on radius and separation shifts every model is worse than a constant predictor once errors are normalized. We conclude that geometric algebra layers are not a general shortcut for low-data 3D learning, but become useful precisely when the target composes group elements in depth.

---


### 27. [Optimized Instance Alteration for Explaining and Assessing Robustness of Classifiers](https://arxiv.org/abs/2607.06637)

**<font color=#1a73e8>作者：</font>** Evgenii Kuriabov, David Miller, Jia Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we propose a unified approach for diagnosing misclassification and assessing the robustness of black-box classifiers. Central to our method is an optimization framework that modifies an instance so that the classifier predicts a specified target label, while ensuring that the modification remains easily explainable. The objective function contains two components: an explainability-aware $L_0$ (XA-$L_0$) penalty that promotes sparse and interpretable modifications, and a classifier loss objective that steers the perturbed instance toward the desired output. This integrated optimization formulation is used both to identify the underlying causes of misclassification and to evaluate robustness by determining how an instance can change within a tolerance region before being reassigned to another class. To quantify robustness, we introduce the Tolerance Region Confusion Matrix (TOR-Confusion Matrix), which measures a classifier's susceptibility by modeling the class-to-class transition probabilities induced by tolerance-bounded perturbations. We validate the proposed method on both image and tabular datasets, demonstrating its ability to jointly deliver interpretability and robustness assessment.

---


### 28. [UASPL: Uncertainty-Aware Self-Paced Learning with Evidential Neural Networks](https://arxiv.org/abs/2607.06638)

**<font color=#1a73e8>作者：</font>** Yifan Zhang, Yuxin Hu, Zhuobin Hao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-paced learning (SPL) is an effective learning paradigm that simulates the human learning process by progressing from easy to difficult samples based on the value of the loss function during the learning process. It has shown great potential in improving model performance and training efficiency. However, the prediction results of samples with smaller loss values are not necessarily reliable, indicating that such samples are not always simple samples for the model. Hence, this article proposes an uncertainty-aware self-paced learning based on evidential neural networks, termed UASPL, which integrates predictive reliability into sample selection through a general loss function within the Subjective Logic framework. This loss function incorporates uncertainty estimation and can be extended to different variants of SPL. Moreover, this loss function couples a sample selection preference, thereby ensuring the interpretability of the sample selection process. Finally, the experimental results on multiple datasets show that UASPL outperforms other SPL methods in terms of classification performance, interpretability, and generality. The source code is available at: this https URL.

---


### 29. [At-Grok Is Not Converged:A Measurement-Validity Audit for Grokking Representation Metrics](https://arxiv.org/abs/2607.06639)

**<font color=#1a73e8>作者：</font>** Truong Xuan Khanh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On modular arithmetic, a network's embedding keeps compressing for tens of thousands of steps after it has already generalized. Reading effective rank at the grokking transition overstates the converged value by 3-5x on an MLP, and by 1.3-1.5x on a transformer trained to convergence; on the MLP it also erases which cells compress at all. Compression lags the accuracy transition by an amount on the order of the time-to-grok, at least 10,000 steps, rather than coinciding with it. A one-variable ablation shows what sets the lag size: adding LayerNorm to an otherwise identical transformer moves the fraction of compression done by the grok step from 0.87 to 0.25, and a pre-registered control rules out scale invariance as the mechanism. We package this as an audit that separates onset from compression, flags censoring, excludes boundary cells that never fully generalize, and checks that the reference floor has plateaued, with an adversarial suite that caught a false-confidence bug in our own branch. A secondary, MLP-specific depth law linking norm budget to converged floor fails a generality test on a transformer and flips sign under free weight decay. Code and the toolkit are released.

---


### 30. [The Approximation Ratio for the Risk of Myopic Bayesian Active Learning for Linear Regression](https://arxiv.org/abs/2607.06642)

**<font color=#1a73e8>作者：</font>** Stephen Mussmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active learning studies the fundamental question: what data should we choose to observe? The greedy algorithm in optimal experiment design is a common heuristic and also equivalent to myopic Bayesian active learning for linear regression, the common framework where long-term planning is replaced with the one-step optimal choice. In this work, we prove a first-of-its-kind approximation ratio for the greedy algorithm's risk that is tight up to an absolute constant. The approximation ratio is linear in the maximum initial leverage score (MILS), a newly identified quantity fundamental to the greedy algorithm's performance. Finally, we illustrate the results with simple numerical simulations.

---


### 31. [The Power of Backdoor Absorption in Community Training](https://arxiv.org/abs/2607.06643)

**<font color=#1a73e8>作者：</font>** Issam Seddik, Sami Souihi, Mohamed Tamaazousti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Backdoor attacks severely threaten large-scale AI models. When model owners delegate training to external compute providers within a decentralized training paradigm, adversaries can craft stealthy, low-frequency triggers to inject malicious behavior while evading standard audits. Traditionally, detecting these attacks requires a full re-computation of the training steps--a prohibitive overhead that directly contradicts the owner's resource constraints. To address this, we investigate the resilience of continuous optimization dynamics under Byzantine perturbations, where adversaries are forced to compete against a continuous influx of honest updates. Under a threat model where an adversary compromises f out of n total trainers, we quantify the minimum auditing overhead required by the model owner to probabilistically bound the attack success rate. We formalize this injection-absorption dynamic as a Discrete-Time Markov Chain (DTMC). Using this framework, we prove that the success probability of any bounded adversary asymptotically collapses to zero under a defense strategy combining natural absorption, a randomized scheduler, and lazy verification oracle. Empirical results demonstrate significant backdoor suppression with zero utility degradation even when invoking the verification oracle on merely 10% of the total training steps. This approach yields a provably sound and computationally efficient defense for safety-critical AI.

---


### 32. [Diffusion enabled Optimal Transport distances for graph matching](https://arxiv.org/abs/2607.06646)

**<font color=#1a73e8>作者：</font>** Iman Seyedi, Francesco Archetti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces Diffusion Semi-Relaxed Fused Gromov-Wasserstein (DsrFGW), a novel method for graph comparison that unifies node features and structural connectivity through optimal transport. While traditional Gromov-Wasserstein and semi-relaxed variants (srGW, srFGW) capture graph structure, they often struggle with sparse, noisy, or partially observed graphs. Inspired by Graph Diffusion Distance, which posits graphs are similar if they enable similar information transmission patterns, DsrFGW incorporates diffusion processes allowing information propagation across nodes, capturing local and global structural patterns while reducing sensitivity to noise or missing edges. An extensive evaluation on 36 synthetic pairwise graph matching tasks (easy, medium, hard) demonstrates consistent superiority over srFGW, achieving accuracy improvements of 0-20 percentage points and dramatic Adjusted Rand Index (ARI) gains: in medium-difficulty scenarios, srFGW often achieves negative ARI (worse than random) while DsrFGW offers better performance in terms of both internal and external clustering quality measures (i.e., Adjusted Rank Index and Accuracy with respect to the true underlying clusters, respectively). Even under severe noise, DsrFGW improves clustering quality in 92% of the synthetic tasks with optimal diffusion scales adapting to problem difficulty, establishing DsrFGW as a robust framework for graph comparison under structural uncertainty.

---


### 33. [ORAN-DEFEND: Subspace Detection and Sanitization of Backdoor DRL xApps in Open RAN](https://arxiv.org/abs/2607.06647)

**<font color=#1a73e8>作者：</font>** Md Raihan Uddin, Fatemeh Lotfi, Tolunay Seyfi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open Radio Access Networks (O-RAN) increasingly delegate near-real-time control to deep reinforcement learning (DRL) xApps obtained from third-party vendors, creating a new supply-chain attack surface. A backdoor policy behaves optimally until an adversary injects a covert trigger into the observed key performance indicator (KPI) telemetry, at which point it issues harmful control actions that degrade quality of service (QoS). We present ORAN-DEFEND, a retraining-free wrapper that sanitizes a frozen, potentially compromised xApp by projecting each KPI window onto a safe subspace estimated from a small number of trusted clean rollouts via singular value decomposition (SVD). We establish, both analytically and empirically, a precise recovery condition: the defense succeeds if the trigger energy concentrates in the orthogonal complement of the safe subspace, and we quantify this boundary through the trigger's $\Eperp$ energy fraction. On the Colosseum COLORAN dataset, we evaluate four structurally distinct DRL backdoor attacks, like TrojDRL, SleeperNets, BadRL, and Q-Incept, spanning inner-loop and outer-loop poisoning regimes and demonstrate $100\%$ return recovery and $\geq99.5\%$ defense success rate across all four when the subspace assumption holds. A geometry ablation reveals an intrinsic and previously uncharacterized limit of any linear projection defense: when the trigger collocates with the legitimate signal, the $\Eperp$ energy fraction governs recovery monotonically, and the linear residual detector collapses to chance even while a nonlinear classifier retains perfect separability.

---


### 34. [Final Checkpoints Are Not Enough: Analyzing Latent Reasoning Faithfulness Along Training Trajectories](https://arxiv.org/abs/2607.06648)

**<font color=#1a73e8>作者：</font>** Hengyu Jin, Shu Yang, Di Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent reasoning methods perform multi-step inference entirely in the model's continuous hidden states, promising more compact and efficient reasoning. However, these opaque hidden states raise a question of faithfulness: whether these latent reasoning steps causally drive the final answer. Prior work investigates this question at converged checkpoints and reports several unfaithful behaviors, such as latent reasoning steps that can be replaced without changing the answer, but leaves how these behaviors form during training unexamined. We instead track how faithfulness evolves across saved checkpoints for different latent reasoning paradigms, applying a verifiable counterfactual edit on the input and a noise-ablation activation patch on the latent reasoning steps. We find that (i) at the output level, latent reasoning methods can look similarly unfaithful at convergence under counterfactual edits while following qualitatively divergent trajectories; (ii) at the activation level, the causal contribution of latent reasoning steps to the final answer decays across training for both paradigms, with the examples that flip on the output side in (i) also being the examples on which this contribution decays; and (iii) the activation-level trajectory diverges by answer format, decaying on binary choice and rising on open-ended decoding. These findings highlight that latent reasoning faithfulness depends on training stage and answer format.

---


### 35. [From Jumps to Signatures: a Generative Method for Temporal Point Processes](https://arxiv.org/abs/2607.06652)

**<font color=#1a73e8>作者：</font>** Niels Cariou-Kotlarek, Vasileios Lampos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rough path signatures are a universal feature map for continuous paths and, via the expected signature, characterise path distributions. These guarantees do not directly extend to cadlag paths of Temporal Point Processes (TPPs), limiting the use of signature methods for event sequences. Furthermore, neural TPP models, including recent generative approaches, optimise per-event objectives with no global sequence-level loss, while evaluation of variable-length event sequences lacks distributional discrepancy measures. This paper proposes a common pathwise framework for addressing these limitations. We introduce the interarrival embedding, a stable, injective lift from jump paths to continuous paths of bounded variation, extending signature methods to discrete event sequences. Our theoretical contributions give rise to sigTPP, the first signature-based generative model for TPPs, trained using a path-level loss on complete trajectories. We further analyse the space of counting paths and derive three distributional discrepancies, providing mathematically justified tools for evaluating generative TPP models. Across synthetic and real-world datasets, sigTPP achieves the best average rank based on eight complementary metrics, outperforms or is within a standard error of the strongest baseline in 64% of the dataset-metric pairs, and according to a relative score, improves against every baseline by at least 19% on average.

---


### 36. [Dual Attention Heads for Personalized Federated Learning in ECG Classification](https://arxiv.org/abs/2607.06653)

**<font color=#1a73e8>作者：</font>** Kien Le, Joseph Lindley, Quoc Bao Phan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables collaborative model training across institutions without sharing sensitive patient data. However, the inherent heterogeneity of electrocardiogram (ECG) data across healthcare providers presents significant technical challenges for robust classification. We propose FedDualAtt, a personalized federated learning approach that splits transformer attention heads into global and local branches. Global heads are aggregated via FedAvg to capture shared cross-site patterns, while local heads remain client-specific to adapt to institution-level recording characteristics. Experiments on FedCVD, an FL benchmark for cardiovascular disease detection, demonstrate that FedDualAtt outperforms existing FL and personalized FL methods in ECG classification tasks. Analysis of global-local head ratios reveals that different clients benefit from varying levels of architectural personalization.

---


### 37. [Robust Human-AI Complementarity under Uncertainty](https://arxiv.org/abs/2607.06656)

**<font color=#1a73e8>作者：</font>** Yewon Byun, Bryan Wilder  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models are often intended to augment rather than replace human decision makers, by providing information that is complementary to human judgement.
Yet, in practice, human decision makers routinely fail to realize such complementary gains, even when models provide useful signal.
In this work, we study how asymmetric information about the quality of information available to a human decision maker vs. an AI impacts the ability of a decision maker to extract complementary value from AI predictions.
We show that a key factor is the error correlation structure between human and AI predictions. In particular, when the AI's prediction errors are \textit{negatively correlated} with those of the human, the decision maker can construct robust strategies which guarantee improvements in expected utility. We empirically investigate whether these conditions for complementarity arise in practice, using real-world forecasting benchmarks.

---


### 38. [Exploring the Interaction of Explanation Styles, Context, and Trust of AI Privacy Redaction in AI-mediated Interactions](https://arxiv.org/abs/2607.06687)

**<font color=#1a73e8>作者：</font>** Roshni Kaushik, Maarten Sap, Koichi Onoue  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-mediated communication is increasingly being utilized to help facilitate interactions; however, in privacy sensitive domains, an AI mediator has the additional challenge of considering how to preserve privacy. In these contexts, a mediator may redact or withhold information, raising questions about how users perceive these interventions and whether explanations of system behavior can improve trust. In this work, we investigate how explanations of redaction operations can affect user trust in AI-mediated communication. We devise a scenario where a validated system removes sensitive content from messages and generates explanations of varying detail to communicate its decisions to recipients. We then conduct a user study with 180 participants that studies how user trust and preferences vary for cases with different amounts of redacted content and different levels of explanation detail. Our results show that participants believed our system was more effective at preserving privacy when explanations were provided (p<0.05, Cohen's d ~ 0.3). We also found that contextual factors had an impact; participants relied more on explanations and found them more helpful when the system performed extensive redactions (p<0.05, Cohen's f ~ 0.2). We also found that explanation preferences depended on individual differences as well, and factors such as age and baseline familiarity with AI affected user trust in our system. These findings highlight the importance and challenge of balancing transparency and privacy in AI-mediated communications and suggest that adaptive, context-aware explanations are essential for designing privacy-aware, trustworthy AI systems.

---


### 39. [CoMind: Understanding Collaborative Human Activity from Multiple Minds and Views](https://arxiv.org/abs/2607.06691)

**<font color=#1a73e8>作者：</font>** Alexey Gavryushin, Dingxi Zhang, Zhao Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-human collaboration is a fundamental aspect of everyday life, essential to success in a wide range of goal-directed activities from household tasks to professional teamwork. While much research has focused on modeling coordination and task execution, the cognitive processes that support such collaboration, particularly Theory of Mind (the ability to infer the mental states of others), remain difficult to study in natural settings. To address this gap, we introduce a novel egocentric and exocentric video dataset capturing real-world collaboration in cooking scenarios. The dataset integrates multi-perspective video, high-quality audio, gaze tracking, and 3D scene and object scans, with annotations for shared attention to objects, social cues and interactions between agents, as well as agent-object interactions. We establish benchmarks for Joint Attention Estimation, Socially Conditioned Object Interaction Anticipation, and Collaborative Handover Prediction, enabling research on multimodal perception, proactive assistance, and collaborative planning. By providing temporally aligned, richly annotated multimodal data, CoMind facilitates the development and evaluation of AI systems capable of modeling complex social interactions and reasoning about human behaviors in collaborative environments. Our dataset and benchmarks are made available at this https URL.

---


### 40. [SPEAR: A Simulator for Photorealistic Embodied AI Research](https://arxiv.org/abs/2607.06701)

**<font color=#1a73e8>作者：</font>** Mike Roberts, Renhan Wang, Rushikesh Zawar 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive simulators have become powerful tools for training embodied agents and generating synthetic visual data, but existing photorealistic simulators suffer from limited generality, programmability, and rendering speed. We address these limitations by introducing SPEAR: A Simulator for Photorealistic Embodied AI Research. At its core, SPEAR is a Python library that can connect to, and programmatically control, any Unreal Engine (UE) application via a modular plugin architecture. SPEAR exposes over 14K unique UE functions to Python, representing an order-of-magnitude increase in programmable functionality over existing UE-based simulators. Additionally, a single SPEAR instance can render 1920x1080 photorealistic beauty images directly into a user's NumPy array at 73 frames per second - an order of magnitude faster than existing UE plugins - while also providing ground truth image modalities that are not available in any existing UE-based simulator (e.g., a non-diffuse intrinsic image decomposition, material IDs, and physically based shading parameters). Finally, SPEAR introduces an expressive high-level programming model that enables users to specify complex graphs of UE work with arbitrary data dependencies among work items, and to execute these graphs deterministically within a single UE frame. We demonstrate the utility of SPEAR through a diverse collection of example applications: controlling multiple embodied agents with distinct action spaces (e.g., humans, cars, and robots) across several in-the-wild UE projects; rendering photorealistic city-scale environments; manipulating UE's procedural content generation systems; rendering synchronized multi-view images of detailed human faces; coordinating an interactive co-simulation with the MuJoCo physics simulator; and editing scenes with natural language via an AI coding assistant.

---


### 41. [Flowcode: An AI-Powered Programming Environment for Scaffolding Iteration in Creative Computing Education](https://arxiv.org/abs/2607.06721)

**<font color=#1a73e8>作者：</font>** Tiffany Tseng, Liliana Hanem Seoror, Jeevika Adda 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Building upon found examples is a popular way people learn to code, especially in creative coding communities where sharing projects and remixing are common practices. But effectively doing so requires being able to 1) understand how existing code works, and 2) extend it by writing code that implements your own ideas, practices that can be challenging for new creative coders. We explored how to support these two processes through the design of Flowcode, a creative coding programming environment that integrates a flowchart for visualizing code structure and a chat interface tailored to support learning to code over vibe coding. We share how we iterated on the design of Flowcode over two studies with new creative coders, reflecting on the roles visualization and friction may play in enabling productive AI-use in computing education.

---


### 42. [A Good Initialization is All You Need for Faithful Visual Attribution](https://arxiv.org/abs/2607.06726)

**<font color=#1a73e8>作者：</font>** Zihan Gu, Jiayu Wang, Hua Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Faithful visual attribution identifies which image regions support a model prediction. Search-based perturbation methods lead the insertion--deletion faithfulness frontier by masking regions and measuring score changes, but they usually output a complete ordering of all regions. Many applications, especially MLLM attribution and repair, only need a compact top-\(k\) evidence mask. We study this mask-first attribution problem. An exactly \(k\)-region mask is combinatorial: useful evidence can depend on interactions among fine regions. Coarse grouping can stabilize early search but aggregates redundant content, whereas one-step scoring can miss high-value combinations. We introduce two forward-only methods. \textsc{CoPAIR} uses a PhaseWin--Greedy gap diagnosis to construct coarse singleton/pair candidates that warm-start full-ordering search. \textsc{TRACE} directly searches fixed-cardinality fine-region masks with cross-entropy sampling, elite retention, and distribution updates, with a finite-budget recovery analysis. The resulting evidence set can be returned as a compact attribution mask or used to initialize Greedy or PhaseWin when a complete ranking is required. Across ImageNet classification with CLIP ViT-L/14, CLIP RN101, and ResNet-101, our initialized search methods establish a new state-of-the-art frontier for faithful full-ordering attribution under inclusive forward-call accounting. On POPE and RePOPE with Qwen2.5-VL-3B-Instruct and LLaVA-v1.5-7B, \textsc{TRACE}+Greedy gives the strongest search-based MLLM attribution results. Direct \textsc{TRACE} masks further achieve single-point RePOPE repair rates of \(94.44\%\) and \(96.00\%\), showing that compact evidence masks can be actionable attribution outputs, not merely prefixes of full rankings.

---


### 43. [Hardware-aware Graph Neural Networks prunning for embedded event-based vision](https://arxiv.org/abs/2607.06739)

**<font color=#1a73e8>作者：</font>** Piotr Wzorek, Kamil Jeziorek, Tomasz Kryjak  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event-based cameras are gaining popularity as the sensor of choice for mobile robotics, due to their high performance in dynamic environments. However, these applications require efficient real-time data processing with low latency and power consumption. One strategy to meet these stringent requirements is hardware acceleration of efficient algorithms that preserve the temporal sparsity of event data. In this work, we propose an optimization strategy for Graph Convolutional Neural Networks models aimed at adapting their architecture to the limited resources of embedded heterogeneous FPGA platforms. Our method incorporates hardware-aware pruning and quantization, taking into account the trade-off between on-chip memory savings and inference accuracy. Strategic exploration of the design space with Fine Grid Search and Greedy layer-wise Iterative Deepening Search methods enables flexible adaptation of the model architecture to the target platform. Our approach was evaluated across various network configurations and multiple datasets, resulting in BRAM memory reductions of 28.8% for CIFAR-10 (with a 1.65% decrease in accuracy), 31.4% for MNIST-DVS (accuracy drop of 3.55%), and 26.5% for N-Caltech101 (with a 5.18% accuracy reduction).

---


### 44. [Creating a Mixed-Reality Installation with Families through Theatrical Co-Design](https://arxiv.org/abs/2607.06754)

**<font color=#1a73e8>作者：</font>** Pavlos Panagiotidis, Roma Patel, Boriana Koleva 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Co-designing with families for environmental sustainability relies on participatory imagination, yet habitual family roles and uneven participation, especially between adults and young children, often constrain it. A second challenge is continuity: workshop relationships and embodied ways of working do not easily survive into the final design, where artefacts travel more readily than roles or interactional dynamics. We report on a nationally toured mixed-reality installation developed through applied-theatre-led co-design with families. Across three workshops and user testing, applied theatre methods supported families to co-create narratives, artefacts, and interactional roles that shaped the public event. We show how theatrical co-design can rebalance child-adult participation through playful status shifts, and how selected workshop dynamics can be re-staged within a public mixed-reality installation. We contribute a theatrical account of participatory design in which designers work not only with artefacts and ideas, but with roles, rhythms, authority, and the social conditions that support collective imagination.

---


### 45. [QANTIS: Hardware-Calibrated Sequential POMDP Belief Updates on IBM Heron](https://arxiv.org/abs/2607.06760)

**<font color=#1a73e8>作者：</font>** Bayram Yuksel Eker, Suayb S. Arslan, Ozgur Nazli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous systems under partial observability act on beliefs, not raw sensor events. QANTIS treats the quantum processor as a calibrated belief-update service in that loop: it receives a prior and an observation model, estimates the rare-event evidence term, and returns an ordinary posterior to a classical planner. This paper asks whether that service can be reused across a sequential Tiger POMDP horizon on present IBM Heron hardware without corrupting the planner-facing posterior. We answer with a controlled hardware case study rather than an end-to-end autonomy or wall-clock speedup claim. The study compares no amplification, guarded Grover amplification, and all-step fixed-point amplification on the same trajectory, then checks whether the returned posterior would change the downstream action. All-step FPAA preserves the Tiger posterior across the reported 8-step and 12-step primary runs, and the 20-step and 32-step controls remain inside the same operating band. In every reported decision check, the hardware posterior and the exact Bayes posterior select the same immediate action. Boundary-aware BIQAE stabilizes amplitude estimation near zero and near one, while a rare-event sweep maps the logical sample-complexity envelope for one-in-a-million evidence. The result is an operating envelope for a hardware-calibrated belief-update primitive, not a standalone hardware-advantage claim.

---


### 46. [Devising Interactive Spaces: A Rehearsal-Oriented Tool for Creating Responsive Environments for Immersive Theatre](https://arxiv.org/abs/2607.06761)

**<font color=#1a73e8>作者：</font>** Pavlos Panagiotidis, Paul Tennent, Jocelyn Spence 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present a rehearsal-oriented system for creating responsive built environments during theatre devising workshops. The system connects bespoke sensing modules for gesture, position, and speech recognition to light and sound outputs through a visual no-code programming layer. It was developed, used, and refined across six workshops with eight professional performance-makers, where participants created light-and-sound scores, gesture- and position-triggered scenes, responsive architectures, participatory prototypes, and a multi-room scratch performance. Rather than presenting a production-ready show-control platform, this demo focuses on how sensing and actuation can be made available as compositional materials during early-stage creative experimentation for immersive theatrical compositions. The system is designed to support quick configuration, visible mappings, and in-room testing, allowing performers to experiment with responsive spaces with minimal technical support. We describe the system architecture, its workshop use, and the practical conditions that helped integrate interactive sensing into embodied performance-making.

---


### 47. [Trees from Marginals: Autoregressive drafting with factorized priors](https://arxiv.org/abs/2607.06763)

**<font color=#1a73e8>作者：</font>** Yuma Oda, Ryan Mathieu, Roman Knyazhitskiy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding greatly increases the interactivity of autoregressive language models by trading off computation for extra tokens generated in a single forward pass. Factorized draft models are especially efficient because they predict future-token marginals in parallel, but their independence assumption causes acceptance rates to degrade sharply as the speculative budget grows. We analyze this limitation and introduce Weaver, a lightweight autoregressive adapter that constructs proposal trees from the top-K marginals of a factorized drafter. Weaver restores conditional dependencies between proposed tokens while avoiding a full-vocabulary projection. To support fast verification for models with Gated Delta Net layers, we derive a rollback-free tree-verification algorithm and implement optimized CUDA kernels in SGLang. By combining these model and systems contributions we achieve a 4.37-fold speedup over autoregressive decoding, and outperform a highly optimized DFlash baseline by 24.7%.

---


### 48. [Cost-Effective Agent Harnesses for Abstract Reasoning and Generalization on ARC-AGI-1](https://arxiv.org/abs/2607.06764)

**<font color=#1a73e8>作者：</font>** Kabir Moghe, Peter Chin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent progress on ARC-AGI-1 from disclosed architectures has come broadly from two regimes: heavy test-time compute over frontier models (evolutionary search, exhaustive sampling, extended chain-of-thought), or benchmark-specific training in which small models are fine-tuned on ARC data, often with task-specialized architectures. We study a third regime: an open-weight model in non-thinking mode (DeepSeek V3.2) under a strict budget, with no ARC-specific fine-tuning. We study what is recoverable through architecture alone, building agentic harnesses that decompose pattern-discovery and program-synthesis stages explicitly. First, we introduce an Explorer-Definer Pipeline that separates pattern discovery from executable transformation synthesis, implemented as a two-stage agent pipeline. Next, we present the Reflective Orchestrator, which augments the pipeline with autonomous exploration of new transformations when previous hypotheses fail on training pairs. On the ARC-AGI-1 public 400-task evaluation set, the pipeline reaches 57.50% pass@2 at \$0.25 per task, and the orchestrator reaches 67.25% pass@2 at \$0.62 per task. Together these architectures lift a 15.50% one-shot baseline by ~52 points without benchmark-specific training or heavy test-time compute. Furthermore, the orchestrator-driven lift tests a falsifiable diagnostic the pipeline produces; unbiased pass@k analysis suggests the pipeline is generation-bound, not selection-bound (selection via training-pair accuracy captures ~95% of the candidate ceiling) and predicts that significant improvement requires broader generation, not better ranking. The orchestrator implements this prediction via adaptive re-exploration and confirms it (unbiased pass@1 lift +9.81 pp, matching selection-mediated pass@2 lift). An additional pipeline ablation identifies its think tool as a significant component, with removal reducing pass@2 by 5.75 pp.

---


### 49. [Efficient Long-Horizon Learning for Learned Optimization](https://arxiv.org/abs/2607.06772)

**<font color=#1a73e8>作者：</font>** Xiaolong Huang, Benjamin Thérien, James Harrison 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned optimization aims to improve upon hand-designed optimizers (e.g., Adam and Muon) by meta-learning small neural network optimizers over a distribution of tasks. While recent work has greatly advanced the architectural design and inductive biases of learned optimizers (LOs), current meta-training approaches still suffer from two main difficulties: (1) they cannot efficiently scale meta-training to long-horizon inner problems and (2) they often fail to surpass comparable hand-designed optimizers. To address these limitations, we propose Efficient Long-hOrizon (ELO) learning, an efficient meta-training algorithm that (1) reallocates redundant meta-training compute to longer failure regimes, achieving efficient long-horizon learning, and (2) enforces decoupled progressive expert supervision, providing stable meta-learning signals that additionally improve the generalization of LOs. Our empirical study evaluates ELO for meta-training both element-wise and matrix-based LOs. Across downstream language modeling (GPT-2-124M/350M on FineWeb) and image classification (ViT-B/16, ResNet-50 on ImageNet-1K) tasks, ELO substantially improves the long-unroll performance and out-of-distribution generalization of the base LOs. In particular, ELO-Celo2 consistently outperforms well-tuned AdamW across all evaluated tasks, while remaining competitive with Muon on language modeling. \textit{Notably, all ELO baselines require less than 7 H100 GPU-hours for meta-training.}

---


### 50. [Efficient Bayesian Deep Ensembles via Analytic Predictive Inference](https://arxiv.org/abs/2607.06776)

**<font color=#1a73e8>作者：</font>** Sina Aghaee Dabaghan Fard, Marie Maros, Jaesung Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce an efficient Bayesian deep ensemble method for predictive regression designed to enhance interpretability while maintaining competitive predictive performance and computational efficiency. Our method combines the statistical rigor of Bayesian inference with the scalability of deep ensembles, providing calibrated uncertainty estimates that enable its use not only for standalone prediction but also as a component within broader learning systems. To achieve these goals, our work relies on three key design components: (i) low-dimensional ensemble representation: predictions are expressed as a combination of a small number of trained neural predictors, enabling scalable inference whose cost depends on ensemble size rather than dataset size; (ii) closed-form Bayesian aggregation: ensemble predictions are combined using Bayesian linear regression, yielding interpretable posterior weights and calibrated uncertainty without approximate inference; and (iii) Independent ensemble training: multiple neural networks are trained separately, producing diverse predictive representations that improve robustness and uncertainty calibration. Empirical results on standard regression benchmarks demonstrate that the proposed approach achieves competitive predictive performance while maintaining reliable uncertainty estimates across settings.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-207](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
