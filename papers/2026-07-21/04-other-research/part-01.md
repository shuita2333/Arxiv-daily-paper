# 📦 其他研究 | 2026年07月21日

> 本类共 **152** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-152](./part-04.md)

---

### 1. [An Empirical Study of Handcrafted Feature Learning and Convolutional Neural Networks for Facial Expression Recognition](https://arxiv.org/abs/2607.15288)

**<font color=#1a73e8>作者：</font>** Chethiya Galkaduwa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial expression recognition is an important computer vision task with applications in human--computer interaction, mental health monitoring, driver alert systems, and behavioral analysis. While convolutional neural networks (CNNs) dominate modern facial expression recognition, handcrafted feature descriptors such as Histogram of Oriented Gradients (HOG) and Local Binary Patterns (LBP) remain useful classical baselines. This study compares HOG with Support Vector Machine (SVM), LBP with Logistic Regression, and a lightweight CNN across three facial expression datasets: FER-2013, CK+, and KDEF. The results show that CNNs achieve the best overall performance, particularly on more complex data, while HOG performs strongly in controlled environments. LBP performs poorly across all datasets. The study highlights that dataset complexity significantly affects performance and that robust feature learning is essential for real-world facial expression recognition.

---


### 2. [Structure of the Circular-Dyadic Convolution Error](https://arxiv.org/abs/2607.15293)

**<font color=#1a73e8>作者：</font>** Ben Fauber, Alireza Moradzadeh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dyadic and circular convolution can both be computed in $O(N\log N)$ time using the Hadamard transform and the FFT-computed discrete Fourier transform (DFT), respectively. The Hadamard transform is preferable for its real-valued sign flips, yet its substitution for the DFT introduces algebraic error. We present three complementary results that characterize this error. First, we identify exact error cancellation: two input and two output positions are universally error-free, and no reordering of the output can eliminate this error. Second, the error operator is nearly full rank, while its null space has only logarithmic dimension. Third, the expected error is governed by a single alignment scalar, with a closed-form expression obtained by averaging over random filters. In general, the substitution error asymptotically doubles the output energy, except for filters in the universal zero-error subspace, which incur no error. Collectively, these results show that the substitution error is structured, predictable, and governed by alignment.

---


### 3. [Position: Quantum Program Generation Must Prioritize Validity Over Probabilistic Scaling](https://arxiv.org/abs/2607.15313)

**<font color=#1a73e8>作者：</font>** Junhao Song, Yu Zhou, William Knottenbelt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The scaling hypothesis assumes that increasing model parameters yields emergent reasoning capabilities. This position paper argues that applying this probabilistic paradigm to generic quantum circuit synthesis is a directional error. Unlike natural languages, quantum circuits require strict adherence to mathematical constraints that manifest a significant syntax-semantics gap. Training on unverified quantum programs means that models learn syntax but fail to capture the physical semantics of the Hilbert space. Since the valid subset of circuit designs decays exponentially with the number of qubits, post-hoc filtering is mathematically intractable. We propose a pivot from human-centric copilots to verifier-centric agents. We integrate hierarchical constraints, topological masks, and symbolic proxies directly into generation. Our analysis suggests that scale alone cannot bridge the validity gap. Verification-aware architectures offer a viable path for modular quantum program generation. These considerations point toward generation methods that encode task-specific rules of quantum information, rather than relying on imitation alone.

---


### 4. [Rethinking the Readout: Unlocking Video Backbones for AI-Generated Video Detection](https://arxiv.org/abs/2607.15321)

**<font color=#1a73e8>作者：</font>** Manni Cui, Ziheng Qin, ZiAn Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated videos (AIGVs) typically contain subtle temporal artifacts that arise from inter-frame inconsistencies rather than within individual frames. A detector that captures such artifacts should therefore benefit from video pretrained backbones over image only ones. In practice, however, video backbones with standard global readouts often fail to outperform strong image pretrained probes on AIGV benchmarks. We attribute this gap to excessive spatiotemporal aggregation in the readout. Video pretrained backbones tend to compress each frame into a single global descriptor. This compression suppresses local patch level temporal dynamics and discards inter patch relations, which are precisely the cues that AIGV detection most reliably depends on. Based on this, we propose Velocity Gated Patch Velocity Profiling (V-PVP), a lightweight readout that replaces only the aggregation layer with two parallel streams over the patch velocity field, adding only about $0.5$M trainable parameters. V-PVP serves as a general plug-and-play module that consistently improves performance across diverse video backbones under both end-to-end fine-tuning and linear probing settings. Our method reaches \textbf{95.28} AUC on AIGVDBench while keeping the backbone fully frozen. The results show that simply replacing the aggregation layer reactivates the temporal potential of frozen video backbones, restoring their advantage on AIGV detection. Code is available at this https URL.

---


### 5. [Interactive 3D Tangible Display with a High-Speed Stiffness-Variable Jamming Module](https://arxiv.org/abs/2607.15325)

**<font color=#1a73e8>作者：</font>** Chanyoung Ahn, Jaesung Lee, Donhyun Hwang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Multisensory integration, particularly through visual and tactile feedback, plays a crucial role in enhancing audience engagement with artworks. Although recent research has increasingly explored tactile experiences in art, existing systems often lack real-time variable stiffness modulation and depend on bulky mechanical infrastructures. In this work, we propose a novel tangible display based on a magnetic jamming mechanism, enabling real-time, low-noise, and low-voltage stiffness modulation integrated into traditional sculptural artworks. Our system combines visual motion and dynamic tactile feedback within a compact standalone module, allowing audiences to interactively experience variations in the rigidity and form of features such as those found in the traditional Korean mask Hahoetal. This approach offers a new paradigm for interactive art, enabling more immersive, multisensory engagement through the fusion of cultural artifacts and modern technology. Our project page is available at this https URL.

---


### 6. [Lazy Arithmetic using Systolic Arrays for Closing the Verification Gap on Embedded Systems](https://arxiv.org/abs/2607.15328)

**<font color=#1a73e8>作者：</font>** Taisa Kushner, Ryan McCleeary, Martin Brain  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Complex algorithms such as deep neural networks are increasingly being deployed on embedded, resource constrained platforms. However, existing hardware and software schemes for implementing these models on the edge fall short, particularly for safety-critical applications such as medical devices. First, hardware such as GPUs, NPUs and TPUs are designed for throughput rather than correctness of computation of security, and are as such susceptible to fault injection attacks. Second, software schemes designed for porting algorithms onto edge devices -- such as quantization schemes -- are either static and sound (non-optimal power consumption), or dynamic yet unsound (non-optimal for safety-critical applications). To address both these needs we propose a both wholly new approach to real-time, dynamic and sound quantization, as well as the hardware to support it. First we developed a sound, real-time adaptive-precision quantization approach utilizing left-to-right arithmetic to pass the most significant bits (MSB) first, and dynamically adjust precision online while performing sensitivity analysis to quantify and manage the risk of decision-boundary crossings. Next, we propose a novel hardware approach utilizing systolic arrays to perform left-to-right arithmetic to generate the MSB first. Together this provides a wholly novel scheme for enabling not only resource-efficient neural networks and artificial intelligence at the edge, but broadly sound and resource-efficient high-precision mathematics on hardware that ensures resilience to bit flip attacks on the most critical bits. This is presented herein as work-in-progress, with software implementations completed and hardware in-progress.

---


### 7. [Training-Free Open-Vocabulary 3D Point-Cloud Segmentation on the Generalized Few-Shot Benchmark](https://arxiv.org/abs/2607.15331)

**<font color=#1a73e8>作者：</font>** Silas kwabla Gah, Ebenezer Owusu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalized few-shot 3D point-cloud segmentation (GFS-PCS) asks a model to segment a scene into many base classes seen at training time and a set of novel classes. The state of the art reaches novel classes by reconciling a dense but noisy 3D vision-language prior with the few-shot support, but it pays for this with base 3D labels, per-episode training, and the support annotations themselves. We ask how far the same reconciliation can go with none of these: no training, no 3D labels, and not even the few-shot support. We pair a frozen 3D vision-language model (RegionPLC) as a dense prior with a frozen promptable concept segmenter (SAM3), prompted by the bare novel class names and lifted from posed RGB views, and reconcile the two by cross-view consistency: a point becomes novel only when enough of the views that see it agree. On the ScanNet200 GFS-PCS benchmark this fully training-free, open-vocabulary pipeline improves novel mIoU by +2.6 over the training-free dense prior while holding base accuracy within 0.5, and recovers a third (33%) of the novel-class gap to the trained state of the art that uses far more supervision. We further show that injecting the few-shot support into the pipeline, as a fusion gate and as a prototypical dense classifier, adds nothing over consistency alone and in fact degrades it through the classifier, which is why the method needs no support at all. On the harder ScanNet++ benchmark, where the dense prior is far weaker on novel classes, the same pipeline nearly doubles novel mIoU (+15.7, from 16.2 to 31.9) at a 1.7 base cost, lifting the harmonic mean from 21.5 to 31.1

---


### 8. [On the Impact of Entropy-based Features](https://arxiv.org/abs/2607.15379)

**<font color=#1a73e8>作者：</font>** Iuri Mundstock, Abreu Quevedo, Jéferson Campos Nobre 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Network anomaly detection is increasingly challenging due to the growing diversity and variability of traffic patterns, which are not always well captured by traditional statistical features. In this work, we explore the use of entropy as an additional feature to support supervised network traffic classification. The main idea is to use entropy to represent variability in selected traffic attributes, complementing conventional descriptors rather than replacing them. We integrate the entropy-based feature into a standard machine learning pipeline and evaluate its impact through a direct comparison between models trained with and without this feature. Experiments conducted on a public intrusion detection dataset show consistent improvements in classification performance, while the additional computational cost remains low. The analysis of confusion matrices indicates a reduction in misclassifications, especially in traffic scenarios with higher variability. Overall, the results suggest that entropy-based features offer a simple and practical way to enhance existing anomaly detection pipelines. This approach is particularly attractive in settings where lightweight feature engineering and interpretability are important, making entropy a useful complement to commonly used traffic features.

---


### 9. [Precise but Uncoupled: Reviewer Precision Does Not Guarantee Critique Uptake in Multi-Agent Math Reasoning](https://arxiv.org/abs/2607.15388)

**<font color=#1a73e8>作者：</font>** Chih-Hsuan Yang, Jingyan Jiang, Vikram Vasudevan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many math- and science-oriented agent systems use hierarchical designs with specialized reviewer roles, assuming that a dedicated review stage should help turn wrong candidates into correct ones. We test this assumption on 4,181 verifier-grounded Omni-MATH problems using matched gpt-oss-120b actors. Collaboration adds little on the easiest tiers, but from tier 4 onward the gains open sharply; in this harder regime, broadcast-style peer discussion reaches higher final accuracy than a planner-executor-reviewer pipeline (PER). We ask whether this gap is explained by reviewer quality or by whether critique changes the next answer the protocol carries forward. It is not explained by reviewer precision alone: PER's reviewer is more precise than broadcast's (0.861 vs. 0.644), yet evaluator-verified useful critique is much less likely to change the next candidate and produces lower reviewer-guided repair. These results show that reviewer detection quality and critique uptake are empirically separable. Within matched PER interventions, forcing explicit acknowledgment lowers final accuracy, while embedding reviewer guidance directly in the solver's working context partially improves follow-through without closing the gap. Overall, reviewer-centric evaluation can overstate system quality: a protocol may spot errors well yet still fail to solve more problems if it does not act on those critiques.

---


### 10. [Improving Network Anomaly Detection via Choquet-Integral-Based Feature Aggregation](https://arxiv.org/abs/2607.15389)

**<font color=#1a73e8>作者：</font>** Abreu Quevedo, Roger Immich, Giancarlo Lucca 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This work investigates a generalized Choquet-integral-based feature aggregation framework to improve anomaly detection in high-dimensional network traffic data. The approach combines adaptive weighting with incremental feature selection to address feature redundancy. Using Random Forest and XGBoost classifiers, we evaluate models trained with both raw and Choquet-aggregated features under varying feature subset sizes. The proposed aggregation achieves up to $7\%$ higher accuracy while reducing data volume by $77.5\%$ (from $214$~MB to $48$~MB), without degrading precision and recall. Results averaged over multiple stratified repetitions indicate that Choquet-based aggregation yields statistically significant gains ($p < 0.05$) in scenarios with limited feature availability, highlighting its suitability for real-time intrusion detection under bandwidth and feature-availability constraints.

---


### 11. [A Transportable Threshold-Based Framework for Interpretable Classification of Medical Data](https://arxiv.org/abs/2607.15394)

**<font color=#1a73e8>作者：</font>** Antony Garcia, Adrian Noriega, Gabrielle Britton 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Black-box models limit the adoption of artificial intelligence in medicine due to their lack of interpretability and reproducibility. We introduce a statistically grounded framework that provides fully interpretable, rule-based clinical classification using the Bernoulli Naïve Bayes (BNB) model. The method applies supervised $\chi^2$-guided statistical binarization to continuous variables, identifying thresholds that maximize association with clinical outcomes within the training data. This transformation allows BNB to operate effectively on continuous medical data without sacrificing its inherent transparency. The approach was evaluated on three benchmark datasets, Pima Indians Diabetes, Wisconsin Breast Cancer, and Heart Failure Prediction, achieving area-under-the-curve (AUC) scores of 0.800 for the Pima analysis, 0.984 for Wisconsin Breast Cancer, and 0.919 for Heart Failure Prediction. In addition to discrimination, probabilistic reliability was assessed using leakage-safe cross-validated calibration analysis including Brier score, calibration intercept/slope, and post-hoc beta calibration, which improved probability calibration across datasets. These results suggest that a statistically interpretable framework can achieve performance comparable to more complex models while providing explicit, clinically meaningful decision rules and calibrated risk estimates. To illustrate this transparency concretely, a complete worked example demonstrates that model inference can be reproduced using only a reference table and basic arithmetic, without access to software or proprietary tools. This work offers a practical approach to supporting trustworthy and generalizable AI in real-world healthcare settings.

---


### 12. [Partial Information Decomposition as a Multi-Contrast 3D MRI Selection Strategy for Resource-Constrained Deep Neural Network Training in Brain Tumor Segmentation](https://arxiv.org/abs/2607.15396)

**<font color=#1a73e8>作者：</font>** Agamdeep Chopra, Mehmet Kurt  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-contrast 3D MRI segmentation can be computationally demanding when all available sequences are used. We evaluate a pre-training Partial Information Decomposition framework that ranks input pairs according to their redundant, unique, and synergistic information about regional tumor burden and selects the highest-ranked pair for downstream training. Applied to T1n, T1c, T2w, and T2-FLAIR MRI, the framework selected T1c+T2-FLAIR. We then trained eleven architecturally identical lightweight 3D U-Nets using different input configurations. On an independent test cohort, T1c+T2-FLAIR was the strongest two-input configuration and ranked second overall in mean Dice (0.676 versus 0.687 for all four inputs). Independent Shapley analysis on the full-input model also identified T2-FLAIR and T1c as the most influential inputs and their pairwise interaction as the strongest. These findings demonstrate the practical value of PID based pre-training selection for identifying compact, informative MRI input sets before costly 3D model development.

---


### 13. [Unsupervised Keypoints for Real-Time Fall Detection: Comparative Analysis Under Real-world Conditions with Predictive Bandwidth Reduction](https://arxiv.org/abs/2607.15400)

**<font color=#1a73e8>作者：</font>** Tasmiah Haque, Jacob Kosinski, Sumit Mohan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Falls among older adults are a major safety challenge, but continuous monitoring is difficult to sustain. Video captures fall-related posture and motion, yet deployment is limited by privacy, computation, and bandwidth. Supervised pose estimation is anatomically interpretable but vulnerable to occlusion and partial body visibility. We propose a privacy-preserving framework that replaces RGB transmission with compact motion representations based on unsupervised keypoints and predictive temporal modeling. Local processing performs segmentation and keypoint extraction; variational recurrent prediction and sequence classification then detect falls from observed and forecasted motion. We evaluate the framework on the UR Fall Detection and Human Fall datasets using random, subject-disjoint, and occlusion-based splits. Under random splits, neither representation consistently dominates, suggesting that standard protocols may hide meaningful differences. Under subject-disjoint evaluation, supervised keypoints show a statistically significant advantage, but performance varies by subject: they perform better when anatomical landmarks are visible, whereas unsupervised keypoints are more robust to occlusion and partial visibility, though they produce more false positives for complex activities. Under occlusion-based evaluation, supervised keypoints miss nearly half of all falls, while unsupervised keypoints retain strong sensitivity and substantially outperform them. Their anatomical independence allows spatial anchors to adapt to visible body structure rather than fail on absent landmarks. The gap widens under bandwidth constraints, where supervised localization errors compound through the temporal model. These findings show that representation choice should reflect expected visual conditions and that unsupervised keypoints offer an advantage when body visibility is compromised.

---


### 14. [GS-RealBlur: A Flexible Data Acquisition Framework for Real-World Image Deblurring](https://arxiv.org/abs/2607.15401)

**<font color=#1a73e8>作者：</font>** Mingyang Chen, Zhilu Zhang, Honglei Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality, large-scale paired data is essential for training learning-based image deblurring models. However, synthetic blurry images generally lack realism, while real-world captured images require complex and inflexible camera systems. In this work, we propose GS-RealBlur, a data acquisition framework for real-world image deblurring, achieving both blur realism and acquisition flexibility. Specifically, we use a handheld camera to capture blurry images, and deploy a gimbal to densely capture sharp images of the same scene. We reconstruct the 3D representation of sharp images and calibrate the camera pose of each blurry frame within this 3D. The image rendered from this 3D according to the pose serves as the sharp counterpart. To better align the rendered image with the blurry image, we introduce a Blur-aware Pose Refinement (BPR) module that refines the pose using appearance consistency and centroid alignment constraints. Leveraging GS-RealBlur, we construct a high-quality and diverse dataset. Extensive experiments demonstrate that a deblurring model trained on our dataset achieves superior generalization performance across various real-world deblurring benchmarks, consistently outperforming models trained on existing synthetic and real-world datasets. The code and dataset will be made publicly available.

---


### 15. [Explicit Over Implicit: Enhancing CNNs Via Complex Structure Tensor Representations for Periocular Recognition](https://arxiv.org/abs/2607.15410)

**<font color=#1a73e8>作者：</font>** Kevin Hernandez-Diaz, Josef Bigun, Fernando Alonso-Fernandez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Our study provides evidence that CNNs struggle to extract orientation features effectively. We show that using the Complex Structure Tensor, which contains compact orientation features with certainties, as input to CNNs consistently improves identification accuracy compared to grayscale inputs alone. Experiments also demonstrated that our inputs, provided by mini-complex convnets, combined with reduced CNN sizes, outperformed full-fledged, prevailing CNN architectures. This suggests that the upfront use of orientation features in CNNs, a strategy seen in mammalian vision, not only mitigates their limitations but also enhances their explainability and relevance to thin-clients. Experiments were conducted on publicly available datasets comprising periocular images (Cross-Eyed and PolyU) for biometric identification and verification in both Close-World and Open-World Scenarios using six CNN architectures. Our experiments on the Cross-Eyed and PolyU datasets yield a 5-26% reduction in EER, providing strong empirical evidence that explicit orientation priors mitigate CNN representational limits in Open-World and Close-World scenarios.

---


### 16. [Regularity-Aware Stochastic MGDA with Adaptive Conflict-Avoidant Update Direction Control](https://arxiv.org/abs/2607.15412)

**<font color=#1a73e8>作者：</font>** Chentong Huang, Lisha Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-objective learning (MOL) aims to optimize multiple objectives simultaneously. The multi-gradient descent algorithm (MGDA) is a workhorse that iteratively updates along a common descent or conflict-avoidant (CA) direction across objectives. In stochastic settings, however, the vanilla stochastic MGDA method, SMG, lacks a fast convergence rate because mini-batch sampling introduces noise in the gradients. This causes bias in the update direction, which is controlled by the CA direction continuity. In this paper, we show that the CA direction is $1/2$-Holder continuous with respect to the Jacobian matrix, and the exponent $1/2$ cannot be improved in the worst case. This leads to a suboptimal convergence rate for vanilla stochastic MGDA in prior works. Nevertheless, under additional regularity conditions, we show this can be improved to Lipschitz continuity. Based on this insight, we propose a stochastic multi-objective regularity-aware (MoRe) method that exploits the Lipschitz continuity of the CA direction when the subproblem is regular, and switches to a fixed scalarization weight otherwise. Intuitively, the proposed algorithm employs CA direction update when the gradient conflict is large, and linear scalarization update otherwise. Theoretically, our method improves the convergence rate of SMG in the nonconvex setting from $\widetilde{\mathcal O}(T^{-1/4})$ to $\widetilde{\mathcal O}(T^{-1/2})$, where $\widetilde{\mathcal O}(\cdot)$ hides logarithmic factors. Meanwhile, we also establish the per-iterate conflict-avoidance guarantees. Empirically, experiments demonstrate its effectiveness in multi-task performance and verify convergence behavior consistent with the established theoretical rate.

---


### 17. [Dataset-Origin Signatures and Shortcut Learning in Screening Mammography AI: A Cross-Dataset Case Study](https://arxiv.org/abs/2607.15416)

**<font color=#1a73e8>作者：</font>** Parham Hajishafiezahramini, Matthew Hamilton, Oscar Meruvia-Pastor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable AI for screening mammography requires training data representative of the low cancer prevalence and subtle abnormalities found in screening populations. We examined whether supplementing such data with biopsy-confirmed cases from abnormal-enriched external datasets improves performance. Using the Newfoundland and Labrador Breast Screening Dataset (NLBSD) alongside CBIS-DDSM and CMMD, we evaluated an EfficientNet-B5 encoder initialized with Mammo-CLIP weights as a frozen linear probe under consistent preprocessing and patient-level splits.
The NLBSD-only model achieved an AUC-ROC of 0.737 (95% CI [0.686, 0.785]). Adding external positive cases reduced performance in every configuration (AUC-ROC = 0.620--0.644; DeLong test, Holm-corrected $p < 0.05$), with degradation increasing as additional sources were introduced. Domain-matched evaluation produced modest gains only when the training and test domains coincided, and no configuration surpassed the NLBSD-only model.
As a diagnostic, we reframed the task as predicting each examination's dataset of origin. The datasets were separated almost perfectly despite identical preprocessing, indicating that dataset-specific characteristics strongly influence the learned representation. These findings show that naïvely pooling abnormal-enriched mammography datasets can introduce domain shift that outweighs the benefit of additional positive cases. Differences in acquisition, intensity mapping, and dataset construction persist after normalization, motivating domain-aware strategies for combining heterogeneous mammography datasets.

---


### 18. [qZACH-ViT: Quantization-Aware Intrinsic Explanations with Recursive Attribution-Stabilized Optimization](https://arxiv.org/abs/2607.15421)

**<font color=#1a73e8>作者：</font>** Athanasios Angelakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compact medical-image classifiers need efficiency and interpretable evidence, yet these goals are often addressed separately. We introduce qZACH-ViT, a quantization-aware extension of the zero-token (CLS-token-free), position-free ZACH-ViT backbone with recursive intrinsic patch-level class evidence. We also introduce Recursive Attribution-Stabilized Optimization (RASO), which norm-matches classification and attribution gradients and removes attribution components that conflict with classification. We evaluate four controlled conditions on seven MedMNIST datasets using 50 training images per class and ten fixed seeds, completing 280 runs. All 210 qZACH-ViT checkpoints are converted to executable mixed-precision ONNX INT8 graphs containing 16 signed INT8 MatMulInteger projections with INT32 accumulation. Deployed mixed-precision INT8 qZACH-ViT with Adam improves the FP32 ZACH-ViT baseline mean on all seven datasets, with a mean paired gain of 0.0313 in the dataset-specific primary metric; qZACH-ViT with RASO yields a mean gain of 0.0368. Across 964,920 source-to-INT8 test comparisons, prediction agreement is 99.9751\%, with a mean absolute primary-metric change of 0.000133 and a maximum of 0.004386. Across 3,600 matched intrinsic maps, mean cosine similarity is 0.999955, mean rank correlation is 0.9944, and mean top-10\% overlap is 0.9692. ONNX artifacts are 70.0\% smaller than source checkpoints and provide $1.41\times$ and $2.39\times$ end-to-end CPU speedups with one and four threads. RASO significantly reduces sufficiency error and improves input-noise stability over Adam with the same attribution loss, but does not dominate every predictive or explainable artificial intelligence (XAI) metric. These results establish qZACH-ViT as a deployable compact intrinsically explainable model and RASO as a targeted stability-oriented optimization procedure.

---


### 19. [From hyperplanes to hyperellipsoids: characterizing the inherent interpretability of linear and single-qubit mixed-state binary classification models](https://arxiv.org/abs/2607.15433)

**<font color=#1a73e8>作者：</font>** Kaitlin Gili  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We characterize and compare the inherent interpretability offerings of a standard linear model with a single qubit mixed state model for the task of supervised binary classification. A side by side comparison reveals that a single qubit mixed state model for binary classification is just the ``ellipsoid version" of standard linear model classification. More precisely, rather than learning a hyperplane to classify data, we learn a hyperellipsoid. We discuss the consequences of the geometric inductive biases of both models, as well as how each model contains a different feature importance inductive bias. This short characterization offers an accessible route to quantum machine learning (ML) ideas for readers who have zero background in quantum and are only familiar with linear classification in ML. In support of ML pedagogy, we encourage instructors to utilize this piece to smoothly introduce quantum ML ideas into the undergraduate ML classroom.

---


### 20. [Stochastic Reset Pathfinding: Path-Level Regret for Cascading Bandits over Graph Paths](https://arxiv.org/abs/2607.15440)

**<font color=#1a73e8>作者：</font>** Guni Sharon, Wei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Stochastic Reset Pathfinding (SRP), an episodic learning problem on a known directed graph with unknown stationary edge success probabilities. In each episode, the agent commits to a source-to-goal path, and any edge failure during execution resets it to the source. SRP captures settings such as entanglement distribution in quantum repeater networks, payment routing on the Lightning Network, and delivery in unreliable mesh networks. We show that the global-reset structure makes the optimal policy open-loop, placing SRP within the combinatorial cascading bandit (CCB) framework. We propose a Log-Dijkstra meta-algorithm with UCB (PathUCB) and Thompson Sampling (PathTS) instantiations. Our main technical result is a path-level regret bound for PathUCB that decomposes regret over suboptimal paths via a per-path complexity C(pi) combining each edge's prefix and suffix reliability. The bound is complementary to the edge-level CCB bound and more informative on structured graphs with polynomially many source-to-goal paths. Experiments on quantum-network, layered-DAG, grid-world, and Erdos-Renyi domains support the theory and show that PathTS typically achieves the best empirical performance among the algorithms tested. We then exhibit an adversarial instance on which PathTS fails to converge, consistent with a known exponential obstruction for combinatorial Thompson Sampling on multiplicative-reward problems. We recommend PathTS as the practical default while cautioning that adversarial instances exist.

---


### 21. [Who Became Financially Vulnerable After COVID-19? A Population-Level Machine Learning Analysis Using MEPS Data](https://arxiv.org/abs/2607.15446)

**<font color=#1a73e8>作者：</font>** Alexey Kresin, Zien Cheng, Ammar Ahad 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The cost of healthcare remains a concern in the United States and may have been influenced by disruptions associated with the COVID-19 pandemic. This study examines healthcare financial vulnerability before and after the pandemic using Medical Expenditure Panel Survey (MEPS) data from 2019 and 2021. High financial burden was defined as out-of-pocket healthcare expenditures exceeding 10% of family income. Survey-weighted subgroup analyses were performed to obtain nationally representative estimates across demographic and socioeconomic groups.
Descriptive analyses were complemented by interpretable logistic regression and machine learning models. Logistic regression was used to estimate adjusted odds ratios, while random forest and gradient boosting models were used to evaluate predictive performance. Temporal generalization assessed whether models trained on pre-pandemic data remained predictive when applied to post-pandemic observations.
Financial vulnerability was strongly associated with poverty status, insurance coverage, and prescription drug spending. Subgroup analyses indicated persistent disparities across population groups, with some evidence of increased burden among vulnerable populations in 2021. Despite these differences, models trained on pre-pandemic data exhibited only modest reductions in predictive performance when evaluated on post-pandemic data, suggesting that the principal predictors of healthcare financial vulnerability remained relatively stable over time.
These findings provide a population-level assessment of healthcare financial vulnerability during the COVID-19 period and demonstrate the value of combining interpretable statistical modeling with machine learning for population health research. The results may support future population health surveillance, risk stratification, and healthcare policy research aimed at reducing financial barriers to care.

---


### 22. [Relevant and Irrelevant: A Renormalization Group Analysis of Transformer Attention](https://arxiv.org/abs/2607.15449)

**<font color=#1a73e8>作者：</font>** Parviz Haggi-Mani, Irina Rish  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Using the language of Wilsonian renormalization group theory (RG), we treat the Transformer's attention mechanism as a perturbation of the trained MLP residual-stack fixed point and ask whether it constitutes a relevant, marginal, or irrelevant operator. We derive a fixed-point shift formula and obtain four testable predictions for the fixed-point geometry, effective rank profile, layer specificity, and perturbation decay spectrum. Testing these on synthetic Markov chain sequences with controlled correlation length, we find: (1) For large chains(long correlation), attention is strongly relevant: it closes a residual loss gap the MLP cannot bridge and drives a phase transition in representation space, with effective rank jumping above input dimensionality at layer 1 and stabilizing at a high-dimensional plateau. (2) For short chains(short correlation), attention is irrelevant: the Transformer converges to the same loss and fixed-point geometry as the MLP, though it contracts perturbations faster. (3) The transition is dominated by the first-layer head (L0H0), which accounts for more than 4 times the representational shift of any subsequent head, consistent with the prediction that the relevant operator acts before the MLP begins integrating out positional variation. (4) Perturbation decay experiments reveal a regime reversal: in the long correlation regime the Transformer selectively preserves slow Markov modes (5.4 times the dynamic range in decay length vs. 1.3 times for the MLP); in the short correlation regime it suppresses all modes faster than the MLP, with no spectral selectivity. Together, these results show that the relevance of attention is not a property of the architecture but of the spectral structure of the data-generating process, and that a first-order RG perturbation framework provides a predictive account of that difference.

---


### 23. [Looped Latent Attention: Cross-Loop KV Compression for Looped Transformers](https://arxiv.org/abs/2607.15456)

**<font color=#1a73e8>作者：</font>** James O' Neill, Fergal Reid  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped, weight-tied Transformers reduce parameters by reusing a block, but decoding still stores a separate K/V cache for every recurrence step. We show that this loop-indexed cache is highly structured. For a fixed token, layer and head, K/V vectors trace a short low-rank trajectory across loops, while the head and layer axes remain much flatter. We introduce Looped Latent Attention (LLA), a post-training cache codec that stores compact K and V latents and reconstructs loop-specific K/V vectors only when attention reads them. The default per-head codec compresses recurrence, while LLA-2D also folds heads into one latent for the extreme-compression regime. The codec is initialized from SVD of teacher activations and refined with KL and attention-output distillation. At matched cache budget, per-head LLA outperforms head-axis MLA, cross-layer sharing, KV quantization and final-loop reuse, showing that the recurrent cache is low-rank but not safely collapsible to a single state. The same axis advantage holds on Ouro-2.6B-Thinking and transfers to Huginn-3.5B, where an SVD codec remains near-lossless to 32x in decoder-independent evaluation. The cache reduction is exact. On one H200, the latent-store path increases measured Ouro-1.4B batch capacity at 4k context from 32 to 768 sequences at 21.3x compression. For long math rollouts, on-policy refinement on student-generated prefixes raises MATH-500 at 4x from 0.43 to 0.66 and reduces no-answer generations.

---


### 24. [Robust Peak-cost Constrained Reinforcement Learning](https://arxiv.org/abs/2607.15457)

**<font color=#1a73e8>作者：</font>** Shilpa Mukhopadhyay, Sourav Ganguly, Santosh Mohan Rajkumar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study robust peak-cost constrained reinforcement learning (RP-CRL), where the objective is to maximize expected reward while controlling the maximum cost encountered along a trajectory. This setting is motivated by safety-critical applications in which a single large violation can be catastrophic and therefore cannot be adequately captured by the standard CMDP framework based on expected cumulative cost. Existing reachability-constrained RL methods adopt Lagrangian-based approaches, yet the underlying duality properties of peak-cost constrained MDPs remain unclear. We show that, unlike standard CMDPs, peak-cost constrained MDPs may not admit zero duality gap. We further consider a robust formulation to address simulator-to-real-world mismatch in the transition dynamics. To solve this problem, we develop a surrogate optimization framework and a robust value estimation method based on integral probability metrics. We prove that, with appropriate hyperparameter choices, the surrogate solution attains the same robust reward value as the original problem while violating the constraint by at most epsilon. Experiments show that the proposed method effectively enforces safety under dynamics perturbations while retaining strong reward performance.

---


### 25. [From Black Box to Executable Logic: Explainable Reinforcement Learning through Prolog Expert Systems](https://arxiv.org/abs/2607.15459)

**<font color=#1a73e8>作者：</font>** Eduardo C. Garrido-Merchán  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A trained deep reinforcement learning policy is a black box, and we ask whether it can be made explainable by rewriting it as an executable logic program that reproduces its behaviour and that a person can read, a logic engine can run, and an optimizer can edit. We present a three-stage post-hoc transformation that extracts a frozen proximal policy optimization teacher, induces an ordered rule list from its decisions in the manner of classical relational learning, and emits the result as a Prolog program whose every decision is executed by an off-the-shelf logic engine; a subsequent expansion stage edits the rule base and accepts an edit only when policy evaluation certifies a return increase. We prove four guarantees. A return-loss bound makes the distilled program a machine-checkable certificate in a finite Markov decision process, and the expansion loop improves monotonically and terminates. For the continuous-observation setting we answer whether the conversion is possible at all: the propositional threshold instantiation converts the network to arbitrary fidelity as the resolution B grows, with disagreement O(1/B) and a return gap that closes at the same rate, and a matching lower bound shows the cost is exponential in the observation dimension for an oblique decision boundary. Empirically, on a two-room key-and-door task with 16,944 reachable states the expanded Prolog program attains exact optimal return in every seed and, in a budget-capped regime, exceeds the stochastic teacher on exact return in ten of ten seeds. On three continuous-control tasks the emitted program substitutes the network, matching the neural teacher within noise on Acrobot with eleven clauses and recovering about 97% of its return on CartPole, while on the finer-control LunarLander it recovers only partially, exactly the ceiling the exponential lower bound predicts.

---


### 26. [ADS-C: Antidistillation Sampling for Classification](https://arxiv.org/abs/2607.15467)

**<font color=#1a73e8>作者：</font>** Khawaja Abaid Ullah, Mohammad Javad Khojasteh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation enables an adversary to replicate a proprietary classifier by querying its prediction interface and training a surrogate on the returned probability vectors. Antidistillation sampling, proposed for large language models, counters this threat with an input-dependent, gradient-directed perturbation of the served distribution; its transfer to classification has not been studied. Adapting the defense to classification, we show its behavior is governed by the distribution of the teacher's per-input confidence margins. Because well-trained classifiers are severely overconfident, the direct transfer exhibits an inert window: below a closed-form-predictable threshold, it affects neither attacker nor defender; beyond it, the defense undergoes a phase transition and degrades the teacher faster than the attacker's student. Temperature softening rescales the transition in closed form, and every temperature configuration lies on the same unfavorable trade-off curve. Our method, ADS-C, composes the perturbation under a closed-form, per-input margin budget that provably preserves every served top-1 prediction, so the defended teacher's accuracy equals the undefended teacher's identically. Under this guarantee the distilled student still loses 17.4 percentage points on CIFAR-100, 29.6 on CIFAR-10, and 13.3 on Tiny-ImageNet; matching this degradation with the unmodified defense costs 27.5, 32.9, and 22.2 points of teacher accuracy. Because served labels are unchanged, a hard-label attacker gains nothing, while the defended soft output trains a student up to 29.7 points below that floor: the incentive to distill served probabilities is not merely removed but reversed. To our knowledge, ADS-C is the first antidistillation defense for classification whose utility cost is exactly zero.

---


### 27. [FLINT: Fingerprinting Federated Learning Architectures from 5G PHY-Layer Side Channels](https://arxiv.org/abs/2607.15469)

**<font color=#1a73e8>作者：</font>** Md Nahid Hasan Shuvo, Mahmudul Hassan Ashik, Moinul Hossain  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) over 5G cellular networks protects raw data but remains vulnerable to side-channel leakage. Prior fingerprinting attacks assume packet-level network visibility, an assumption that does not hold at the 5G Physical (PHY) layer, where user payloads are encrypted and Radio Network Temporary Identifiers (RNTIs) may change over time. However, we demonstrate that PHY-layer scheduling metadata broadcast over the Physical Downlink Control Channel (PDCCH) preserves architecture-associated temporal patterns. We introduce FLINT, a novel black-box fingerprinting framework that infers FL model architecture families, including CNNs, RNNs, and Transformers, using only coarse PHY-layer observations. FLINT overcomes the lack of network-layer visibility by decoding PDCCH scheduling information, mapping changing RNTIs to physical user devices, and applying multi-view temporal modeling to distinguish architecture-specific training behavior. This leakage is security-critical because knowledge of a client's model architecture can transform passive reconnaissance into targeted downstream exploitation. Extensive experiments on an over-the-air srsRAN-based 5G testbed demonstrate that FLINT achieves a macro F1-score of 0.930 for architecture-family classification. To our knowledge, FLINT is the first work to fingerprint AI/ML model architectures using lower-layer 5G side-channel information obtainable by any protocol-aware adversary.

---


### 28. [Deep Learning Approaches for Sleep Apnea Classification from Polysomnographic EEG Signals](https://arxiv.org/abs/2607.15477)

**<font color=#1a73e8>作者：</font>** Shashank Manjunath, Mukesh Cheemakurthi, Aarti Sathyanarayana  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sleep apnea diagnosis via polysomnography remains resource intensive and relies on time consuming manual data analysis and scoring. Recent work has demonstrated that central nervous system effects of sleep apnea events can be detected through electroencephalogram (EEG) signals. However, most work uses a single feature type on various datasets combined with different classification algorithms. In this work, we present a comprehensive comparison of deep learning architectures and feature representations for automated sleep apnea detection from multichannel EEG on a single dataset of pediatric subjects. We evaluate Vision Transformers and Graph Attention Networks across distinct signal representations: raw temporal signals, short-time Fourier transform spectrograms, coherence based graphs, and two topological data analysis (TDA) derived features. Using age and sex matching of our train and test sets, we train on 2410 pediatric subjects and test on 575 pediatric subjects. We achieve a best test AUC of 0.750 using a vision transformer based model trained on TDA features. Stratified analysis across patient demographics (age, sex, AHI severity) and sleep stages (N1, N2, N3, REM) reveals significant performance variation. Our results demonstrate the feasibility of EEG based automated OSA screening while highlighting essential challenges for clinical deployment.

---


### 29. [A Critical Analysis of Trustworthy AI Tools, Mark Frameworks, and the Implementation Chasms](https://arxiv.org/abs/2607.15480)

**<font color=#1a73e8>作者：</font>** Michael Papademas, Xenia Ziouvelou, Kostas Karpouzis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As artificial intelligence (AI) systems increasingly impact society, ensuring their ethical and trustworthy deployment has become a global priority. While a myriad of high-level ethical guidelines have emerged, criticism persists that these frameworks remain abstract and lack concrete mechanisms for implementation. This paper conducts a critical analysis of tools and trust mark frameworks intended to operationalize trustworthy AI (TAI), drawing on a comprehensive dataset from the OECD. Through empirical mapping and descriptive comparative analysis, we identify significant asymmetries in ethical focus, lifecycle coverage, stakeholder targeting, and tool typology. Our findings show a strong emphasis on fairness, transparency, and robustness, with comparatively little attention paid to explainability, digital security, and environmental sustainability. Moreover, most tools and certifications concentrate on post-development stages, with limited guidance for early design or data collection phases. Educational initiatives and policy engagement are notably underdeveloped, suggesting that current TAI efforts are dominated by technical and procedural measures within industry contexts. We argue that bridging the persistent chasm between AI principles and practice requires expanding ethical objectives, embedding ethics across the AI lifecycle, and fostering broader multi-stakeholder participation. This study provides both a diagnosis of existing implementation gaps and actionable recommendations for advancing more holistic, inclusive, and enforceable AI governance

---


### 30. [Inpainting Insights: Elevating Visual XAI with Photorealistic Perturbations](https://arxiv.org/abs/2607.15482)

**<font color=#1a73e8>作者：</font>** Josef Lindl, Mariana Chaves, Damien Garreau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The increasing complexity of state-of-the-art machine learning models has made their behavior progressively harder to interpret, spurring rapid advancements in the field of eXplainable Artificial Intelligence (XAI). Among many methods proposed, perturbation-based approaches play a major role. By systematically altering (perturbing) input features, these approaches measure the impact on the model's predictions. For image data, traditional perturbation techniques, often involve replacing pixel values e.g., with a pre-defined color. However, such approaches, but also more refined deterministic techniques, generate unrealistic out-of-distribution samples and often leave visible artifacts, which can mislead the model and compromise explanation quality. In this work, we adjust LIME, a widely used perturbation-based method, to demonstrate how generative inpainting can improve perturbation-based explanations for images. We achieve photorealistic perturbed samples that align better with the original data distribution and enhance explanation quality.

---


### 31. [Diffusion models recover accurate mixture weights despite score function insensitivity](https://arxiv.org/abs/2607.15485)

**<font color=#1a73e8>作者：</font>** Andrew Dennehy, Ramchandran Muthukumar, Rebecca Willett 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Score-based generative models exhibit a puzzling behavior: they often appear to cover all modes of a target multimodal distribution and yet may fail to learn the correct relative mode amplitudes, which can be interpreted as mixture weights. We resolve this apparent paradox by relating the diffusion score matching (DSM) loss to the error in estimating mixture weights from generated samples. We show that, even when the target score is insensitive to mixture weights, generated samples can recover the weights accurately if the scores at intermediate noise levels are informative about the weights. Accordingly, we define the diffusion score sensitivity index (DSSI) as the variation in the DSM loss relative to changes in a parameter. We then show that the DSSI governs the accuracy with which the parameter of the target distribution can be estimated from generated samples. For Gaussian mixtures in arbitrary dimensions, we prove that the mixture weight estimation errors are on the same order as the DSM loss under mild conditions. Empirically, we show the emergence of sensitivity during the noising process of benchmark data distributions under typical noise schedules, and that these sensitivity values predict how well a well-trained model recovers mixture weights. Furthermore, we show that the choice of noise schedule can reduce diffusion sensitivity, leading to mode amplification. Although we focus on mixture weights, the proposed sensitivity framework governs the recovery of any qualitative parameter of the target distribution.

---


### 32. [Trajectory-aware Cross-view Geo-localization with Sequential Observations](https://arxiv.org/abs/2607.15491)

**<font color=#1a73e8>作者：</font>** Tianyi Gao, Jiayu Lin, Danielle Beaulieu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view geo-localization matches ground-level observations against geo-tagged satellite imagery. Recent methods show that sequential queries such as video clips yield richer spatiotemporal cues than single images, yet they overlook a complementary sequential modality: route descriptions -- which capture the same trajectory at a higher level of abstraction and are often the only input available (e.g., a user directing an autonomous vehicle to a pickup point). To bridge this gap, we introduce SeqGeo-VL, a dataset of $\sim$39K video-text-satellite triplets, and TrajLoc, a unified framework capable of processing both video clips and route descriptions. By leveraging both dense visual and abstract linguistic semantics, TrajLoc enables these modalities to mutually reinforce cross-view matching. We further propose TrajMod, a lightweight module that conditions query embeddings on trajectory geometry, yielding spatially-aware representations. Experiments show that TrajLoc achieves substantial gains over state-of-the-art methods on both video and text geo-localization. The project page is available at this https URL.

---


### 33. [An Auto-Scaling Approach for Serverless Environments Based on a Multi-Expert Consensus Mechanism](https://arxiv.org/abs/2607.15511)

**<font color=#1a73e8>作者：</font>** Mobina Kashaniyan, Mehrdad Ashtiani, Amirhossein Ghassemi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Serverless computing provides automatic resource management and pay-per-use execution, but effective autoscaling remains challenging because of dynamic workloads, cold-start latency, and dependencies among functions. We present a dependency-aware autoscaling framework that integrates graph-based bottleneck identification, short-term workload forecasting, multi-model consensus, and cost-aware scaling control. Serverless applications are represented as directed dependency graphs, and structurally important functions are identified using weighted degree centrality. Resource demand is predicted using lightweight MLP, LSTM, and CNN models. Their outputs are combined through a performance-weighted probabilistic ensemble inspired by Bayesian model averaging. The controller further incorporates cold-start awareness and cost comparison to select among scale-up, scale-down, and hold actions. Experiments using real workload traces show that supervised forecasting substantially outperforms unsupervised clustering for autoscaling decision generation. The proposed ensemble achieves 99.88 percent prediction accuracy and reduces prediction error compared with representative hybrid forecasting methods. Evaluations across multiple cloud pricing models also demonstrate consistent infrastructure cost reductions while maintaining performance targets. The results show that combining dependency analysis, multi-expert forecasting, and cost-aware control provides a robust and practical solution for serverless autoscaling.

---


### 34. [Intentional Electromagnetic Interference Attacks on Facial Recognition](https://arxiv.org/abs/2607.15512)

**<font color=#1a73e8>作者：</font>** Tyler Fitzsimmons, Adam Czajka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Attacks on general computer vision algorithms are often relegated to the digital domain, with the optimization performed purely in the digital world and then translated to physical mediums for implementation. In the field of biometrics, including facial recognition, physical presentation attacks targeting biometric sensors are dominant and present significant opportunity and risk. This paper highlights a critical vulnerability in the physical-to-digital pipeline of biometric sensors and provides a standardized approach for testing facial recognition system robustness against hardware attacks, going beyond and potentially complementing presentation attacks (as defined in ISO/IEC 30107 standard series). Specifically, in this work we (a) demonstrate that intentional electromagnetic interference is possible to be conducted with commonly accessible radio frequency (RF) equipment, (b) assess the robustness of state-of-the-art face recognition methods against RF-based attacks, and (c) provide a dataset composed of face images captured with and without electromagnetic interference to serve as a new benchmark for testing modern face matchers against RF-sourced interference.

---


### 35. [Interactive Mascot: A Scene-Centric Interaction Grammar for Data Visualizations](https://arxiv.org/abs/2607.15523)

**<font color=#1a73e8>作者：</font>** Zhicheng Liu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Scene-centric visualization systems expose semantic components, such as marks, encodings, layouts, and axes, as first-class objects that can be directly manipulated. Existing interaction abstractions, however, are largely based on event streams, signals, and data selections rather than semantic scene components. This mismatch makes interactions involving scene components less natural to specify and limits the expressive power of scene-centric visualization systems. We present Interactive Mascot, a scene-centric interaction grammar for data visualizations. Interactive Mascot extends scene-centric representations for static visualizations by modeling interactive behavior as information flow among four interaction components (trigger, responder, evaluator, and updater) and two forms of context (event context and state context). To realize these semantics, we introduce a dependency-graph execution model that systematically transforms interaction specifications into executable dependency graphs using reusable graph patterns associated with semantic visualization components. We implement Interactive Mascot in the JavaScript library this http URL and evaluate its expressiveness, performance, and usability. Interactive Mascot naturally covers Vega-Lite's interaction design space while additionally supporting stateful interactions, direct manipulation of scene components, and freeform selection. It achieves runtime performance comparable to Vega-Lite, and a qualitative user study shows that the grammar is learnable and usable for interaction authoring.

---


### 36. [Recursive Harness Self-Improvement](https://arxiv.org/abs/2607.15524)

**<font color=#1a73e8>作者：</font>** Hyunin Lee, Jinglue Xu, Jeffrey Seely 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Under model--harness co-evolution, harnesses are not merely inference-time scaffolds but data-generating components whose execution traces can shape future foundation models. This motivates harness-in-the-loop learning: optimizing harnesses for both immediate agent performance and the quality of traces used for future model training. However, continually updating provider-built scaffolds is costly and labor-intensive. We therefore investigate whether optimizing user-constructed harnesses in a task-specific manner can improve execution-trace quality while remaining computationally lightweight and requiring only a few update iterations. To this end, we introduce Recursive Harness Self-Improvement (RHI), which represents the harness as a prompt-level specification of the agent loop and iteratively refines it using pairwise feedback over its own revision history. Across 30 synthetic machine-learning research tasks spanning quantitative finance, robotics, and pharmacy, a few RHI iterations suffice to substantially raise the performance ceiling of low-reasoning-effort agents, exceeding the corresponding maximum-reasoning-effort setting while reducing inference cost by up to 60%. We show that these gains arise primarily from improved task-specific context management through more effective inter-agent information flow rather than longer reasoning traces. Finally, we formalize this behavior as an information-theoretic hypothesis for RHI's implicit optimization objective, suggesting RHI as a practical algorithm for continual learning within the paradigm of model--harness co-evolution.

---


### 37. [Physics-aware Masked Diffusion-based Flood Simulation for Urban Fisheye Disaster Detection](https://arxiv.org/abs/2607.15527)

**<font color=#1a73e8>作者：</font>** Sodtavilan Odonchimed, Tsogt Enkhbayar, Oyunzul Munkhtamga 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical simulations that predict the behavior of urban disasters, such as climate-related flooding, play a crucial role in disaster prevention and the development of anomaly detection models. However, the severe shortage of flood data in real-world environments, combined with the inherent distortions of fisheye lens images, which are used for urban surveillance, has made high-precision simulations challenging. To address this, we propose a new physical simulation system PhysFlood that leverages Diffusion Models to synthesize realistic floods from just a single image captured by a fisheye lens. Our system not only enables simulation from a single image, but also features the ability to freely control and generate diverse flood scenarios by manipulating physically meaningful variables, such as water levels. In our evaluation experiments, we conducted a qualitative human study and demonstrated that the simulation images generated by PhysFlood exhibit both acceptable realism and robustness.

---


### 38. [Publicly-Verifiable Certificates for Statistical Algorithms](https://arxiv.org/abs/2607.15528)

**<font color=#1a73e8>作者：</font>** Michael Ngo, Michael P. Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Following Goldwasser, Rothblum, Shafer, and Yehudayoff, who defined a framework for interactive proofs of learning [ITCS'21], we initiate the study of non-interactive proofs of learning. We define and study a new notion: Publicly-Verifiable Certificates of Statistical Validity (pvCSVs), which allow for public, distributionally-robust certification that the result of a learning algorithm is valid. In a pvCSV, a learner publishes a hypothesis $h$ and corresponding certificate $\pi$; then, any user, who holds a user-specific distribution, can read the pair $(h,\pi)$ and determine efficiently whether the hypothesis is valid according to the user-specific distribution.
We construct pvCSVs in the context of Adaptive Statistical Query (SQ) Algorithms. To certify SQ algorithms that makes $k$ adaptive queries, we construct pvCSVs where the sample complexity scales with $O(\log k)$, whereas the sample complexity of the best learning algorithms scale with $\tilde{O}(\sqrt{k})$. More generally, we study proof systems for learning in the SQ model, demonstrating the model's strengths as well as its limitations.

---


### 39. [Logic, Optimization, and Artificial Intelligence](https://arxiv.org/abs/2607.15532)

**<font color=#1a73e8>作者：</font>** J. N. Hooker  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Logic and optimization can, in combination, make valuable contributions to rule-based AI. Logic is the obvious medium for encoding a rule base and drawing inferences from it, while optimization provides a powerful technology for computing inferences. Their combination has taken on new relevance amid a growing concern for transparency in AI. which is important for reproducibility, explainability, trustworthiness, and fairness. Rule-based AI provides a natural solution to transparency that is becoming increasingly practical due to today's highly advanced optimization methods. This article surveys several areas of logic-optimization partnership, including probabilistic logic, Bayesian logic, belief logics and Dempster-Shafer theory, nonmonotonic (default) logic, many-valued logics, and inference of logical formulas from noisy data based on Boolean regression. It shows how to compute projections, the fundamental problem of both logic and optimization, using decision diagrams and logic-based Benders decomposition. It describes the use of postoptimality analysis to explain how conclusions are reached, further enhancing transparency, as well as the role of optimization in answer set programming modulo theories. The paper concludes by suggesting possible future research directions.

---


### 40. [CASAband: Easy-to-Wear Textile Wristband using Shape Memory Alloy Actuators for Spatial and Temporal Haptic Feedback](https://arxiv.org/abs/2607.15533)

**<font color=#1a73e8>作者：</font>** Baekgyeom Kim, Anoush Sepehri, Jessica Healey 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Haptic interfaces for the wrist and forearm offer an attractive alternative to hand-worn devices as they are simple to wear, leave the hands free for interaction with the real world, and interfere minimally with natural arm motions. To be useful in real-world settings, however, such devices must balance functionality, wearability and comfort, all while being fully untethered with minimal mass and volume. In this work, we present CASAband, a haptic wristband that integrates compliant amplified shape memory alloy actuators (CASA) into a multi-layered textile wristband to deliver spatial and temporal haptic feedback. CASAband operates completely untethered, generates no noise, and has a total mass of 63 g. The device incorporates four actuators that can generate up to 1.7 N of blocked force and 3.2 mm of free displacement with an operating bandwidth ranging from 1.34-6.59 Hz depending on the applied voltage. We conducted a perceptual study and determined that users could identify the location of a single haptic cue around their wrist and discriminate among several patterned cues with over 90% accuracy on average, highlighting that CASAband can be a suitable wearable interface to deliver information for real-world guidance and navigation tasks. To highlight the potential use cases for CASAband, we conducted two demonstrations: a pick and place task where the user relied only on haptic communication from a moderator, and an outdoor pedestrian navigation task where the user relied only on directional cues on the wrist. CASAband is one of the first haptic interfaces that balances the tradeoff between form and function and presents new opportunities for haptic feedback in the real world

---


### 41. [E3DGS: Unified Geometric-Photometric Equivariance for 3D Gaussian Splatting via Color-as-Geometry Embedding](https://arxiv.org/abs/2607.15536)

**<font color=#1a73e8>作者：</font>** Chankyo Kim, Maani Ghaffari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) captures scenes by coupling explicit geometry (position, covariance) with view-dependent photometry (Spherical Harmonics). However, building $\mathrm{SE}(3)$-equivariant architectures on these primitives presents a fundamental representation bottleneck. Color has been treated as a signal rather than a geometric entity, making it nontrivial to unify symmetry across geometry and appearance as the camera frame changes. While translations are handled by relative coordinates, rotations act heterogeneously across attributes: $\mu\mapsto R\mu$, $\Sigma\mapsto R\Sigma R^\top$, and $f_\ell\mapsto D^\ell(R)f_\ell$. This mismatch complicates strict equivariance, leading existing methods to either discard or flatten SH coefficients, thereby breaking symmetry. We propose a unified solution rooted in representation theory: for SH degrees $\ell\le2$, photometry is algebraically isomorphic to a rank-2 geometric tensor. We prove that the Wigner-$D$ action on these SH coefficients can be exactly reformulated as the conjugation action on $3\times3$ matrices. Leveraging this, we introduce the Unified Matrix Embedding, a lifting that maps all Gaussian attributes into a unified carrier space, $\mathfrak{gl}(3)$. Building on the "Color-as-Geometry" formulation, we present E3DGS, a rigid-body ($\mathrm{SE}(3)$) equivariant architecture that processes 3D Gaussians without Clebsch-Gordan tensor products. Evaluations on object vision and action-conditioned Gaussian world modeling demonstrate that our unified approach yields strong robustness under camera-frame changes and improved data efficiency.

---


### 42. [ImprovedVBGS: Real-time Continual Variational Bayes Gaussian Splatting](https://arxiv.org/abs/2607.15542)

**<font color=#1a73e8>作者：</font>** Damani Mguni-Coker  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> On-the-fly reconstruction is a key requirement for many applications in robotics and autonomous navigation. Variational Bayes Gaussian Splatting (VBGS) enables continual learning without replay buffers using Coordinate Ascent Variational Inference (CAVI), but its per-frame iterations over all observed points make it too slow for real-time use with strict memory and latency requirements. We present ImprovedVBGS, an accelerated framework for on-the-fly continual reconstruction. This is achieved primarily through (i) spatially truncated variational inference, and (ii) improved reassignment that uses forwarding, truncation and eliminates wasteful dynamic recompilation. On the NeRF synthetic dataset, we reduce mean per-frame latency from ~84.0 s to ~0.050 s on an RTX 3070 Ti, a 1680x speed-up while maintaining reconstruction quality.

---


### 43. [CoWeaver: A Bi-directional, Learnable and Explainable Matching Engine for Mixed Human-Agent Science Collaboration](https://arxiv.org/abs/2607.15545)

**<font color=#1a73e8>作者：</font>** Jiayao Gu, Kexin Chu, Peidong Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> LLM-based agents excel at writing articles, coding and information retrieval. However, they fail to form strong collaborations within the scientific community due to the bidirectional, dynamic nature of the problem and a high demand of decision interpretability. We proposed COWEAVER, a bidirectional, learnable and explainable algorithm to match scientists and form strong collaborations within a human-agent network. COWEAVER matches candidates and requesters through filling capability gaps and filters candidates through a two-stage ranking step. Finally, the model explores newcomers by maintaining uncertainty-aware capability estimates and updating them through requester's feedback. We show that the selection mechanism of combining both exploration (UCB) and greedy of COWEAVER exceeds the greedy-only mechanism - the analytical best solution - on 6 out of the 20 tasks and performed on par with the greedy-only mechanism in terms of selecting the best candidate. We compared COWEAVER baselines in terms of matching quality and efficiency. COWEAVER outperforms baselines on all metrics.

---


### 44. [Hard Rules, Soft Preferences: Bridging Reasoning, Learning, and Optimization for Personalized Packing Checklist Generation](https://arxiv.org/abs/2607.15562)

**<font color=#1a73e8>作者：</font>** Himel Dev, Madhusudan Basak, Tanmoy Sen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Packing for air travel is recurring and error-prone: the checklist must be personal and context-aware, yet feasible under safety rules, item dependencies, and luggage limits. Existing packing assistants are template-driven and generic, or recommendation-driven but unconstrained, leaving users to manually patch regulatory and capacity violations. We propose a reasoning-guided learning framework with three stages: (1) a symbolic engine that generates a regulation-aware seed checklist with explicit dependency structure, (2) a two-stage preference learner that estimates inclusion and priority utilities from user add and remove actions while mitigating survivorship bias, and (3) a CP-SAT optimizer that selects a compact, compliant subset. The architecture instantiates a general pattern for constrained personalization, applicable wherever hard feasibility coexists with sparse preference signals. On 604 labeled trip scenarios, comprising 29K inclusion labels and 343K pairwise comparisons, the symbolic engine attains 99.7% recall and 0.96 rubric validity, compared with 0.78 to 0.81 for frontier LLMs. Gradient-boosted trees and LambdaMART reach an AUC-ROC of 0.943 and an NDCG@5 of 0.923. CP-SAT attains 100% constraint satisfaction, compared with 28% for greedy selection and 10% for random selection. Deployment in FlyEnJoy, a production iOS travel app, doubled checklist completions and reduced editing and completion time.

---


### 45. [Are All Tokens Necessary for Visual Place Recognition? An Empirical Study of Token Reduction for Efficient Inference](https://arxiv.org/abs/2607.15563)

**<font color=#1a73e8>作者：</font>** Tong Jin, Yunpeng Liu, Shuyu Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent visual place recognition (VPR) methods based on vision transformers, particularly foundation models, have achieved remarkable recognition performance. However, these models process all visual tokens throughout the entire network, resulting in substantial computational overhead, which hinders their deployment in real-time and resource-constrained scenarios. A natural question thus arises: are all visual tokens necessary for VPR? To answer this question, we present the first systematic benchmark of token reduction for efficient visual place recognition. Our benchmark comprehensively evaluates representative token pruning, token merging, and hybrid pruning-merging methods across multiple state-of-the-art VPR models and diverse benchmark datasets covering urban, suburban, and natural environments. We further investigate token reduction from multiple perspectives, including recognition performance under different reduction configurations, computational complexity, inference speed, qualitative visualization, and deployment efficiency on edge devices. Through extensive experiments and in-depth analysis, our benchmark reveals multiple important characteristics of token reduction in VPR and provides several practical insights into the trade-offs between accuracy and inference efficiency. For example, token reduction can reduce computational cost by up to 29\% and improve throughput by up to 44\%, while incurring less than 1\% degradation in recognition accuracy. Overall, this work establishes a comprehensive foundation for future research on token-efficient VPR and efficient visual retrieval systems. Our codes and models will be available at this https URL

---


### 46. [Physiological Prior-Driven Label Enhancement for Cross-Subject EEG Emotion Recognition](https://arxiv.org/abs/2607.15566)

**<font color=#1a73e8>作者：</font>** Hongyu Zhu, Lin Chen, Yuming Fu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG)-based emotion recognition captures affective neural signals with high temporal precision, but cross-subject variability and label noise remain critical challenges to its practical healthcare deployment. Existing label-denoising methods lack physiological grounding, while physiology-informed approaches rely on hand-crafted hyperparameters. To bridge these two paradigms, we propose PhyDA, a plug-and-play, tuning-free framework that unifies neurophysiological priors with data-driven label refinement. PhyDA comprises two modules. Since cross-subject variability renders global thresholds suboptimal, the Physiological Noise Quantifier (PhyNQ) exploits a spectral slope} to produce a subject-specific noise score, providing a neurophysiologically interpretable quality assessment {that naturally adapts to each individual. The Data-Adaptive Label Refiner (DALR) directly adopts this noise score as the contamination ratio to drive a label refinement pipeline that requires no additional neural network training, thereby directly mitigating the impact of inter-subject label noise. Extensive experiments on three public datasets (DEAP, SEED, SEED-IV) across seven backbone architectures under strict leave-one-subject-out cross-validation demonstrate that PhyDA consistently and significantly outperforms both general and EEG-tailored label-denoising baselines, achieving average accuracy gains of 2.76%, 2.66%, and 3.32%, respectively. Visualization further confirms its neurophysiological interpretability and practical robustness. The source code is available at: this https URL.

---


### 47. [Information-Directed Sampling for Causal Bandits](https://arxiv.org/abs/2607.15577)

**<font color=#1a73e8>作者：</font>** Muhammad Qasim Elahi, Murat Kocaoglu, Mahsa Ghasemi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal bandits exploit structural relationships among variables to share information across interventions and accelerate the identification of high-reward decisions. In many applications, however, some variables cannot be directly manipulated, even though they influence the reward and provide useful information about the underlying causal system. We study contextual causal bandits with non-manipulable variables, where context variables are observed before action selection and additional variables are observed after each intervention. Assuming a known causal graph without latent confounding, we adopt a Bayesian formulation in which the conditional probability tables of the observational distribution constitute the unknown parameter. This representation allows observations collected under one intervention to update reward estimates for other interventions through their shared causal mechanisms. We develop causal variants of Thompson Sampling and Information-Directed Sampling (IDS) for this setting. For Thompson Sampling, we establish an entropy-dependent sublinear Bayesian regret bound. For IDS, we derive an entropy-dependent regret bound that explicitly quantifies the additional error introduced by Monte Carlo approximation of the expected regret and information gain; when these quantities are available exactly, the bound recovers the standard sublinear IDS rate. We further provide high-probability confidence bounds for the Monte Carlo estimates used by the algorithm. Experiments on several synthetic causal bandit tasks show that the proposed methods outperform causal and non-causal baselines by more effectively exploiting information shared across interventions.

---


### 48. [Rethinking Transfer in Continual Learning: A Replay-Based Realisation](https://arxiv.org/abs/2607.15587)

**<font color=#1a73e8>作者：</font>** Yang Meng, Zhenya Liu, Zhuokai Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning studies how deployed language models can continually acquire new tasks without expensive retraining from scratch. Existing methods, whether rehearsal-based (replaying stored past data) or rehearsal-free (regularising or isolating parameters), overwhelmingly target one objective: preventing catastrophic forgetting. Forward transfer, the past helping the future, has meanwhile been pursued almost exclusively through parameter reuse, with no explicit account of when transfer should be expected at all. We begin one step earlier: before designing a transfer mechanism, we ask when transfer should exist at all. We answer with a framework of three measurable conditions: the target task must leave room for improvement beyond its own limited supervision, transferable information must survive continued optimisation, and replay must come from compatible previous tasks. We instantiate this view as Transfer-Selective Replay (TSR), which selects replay data predicted to benefit the incoming task rather than replaying past examples indiscriminately. Selection is guided by a zero-training task signature, while distillation preserves stability on previous tasks. Under the standard continual learning protocol in the low-budget regime, TSR consistently improves forward transfer while maintaining stability, outperforming existing replay baselines across heterogeneous and homogeneous task streams. More broadly, the results argue for treating transfer as a first-class objective of continual learning, to be understood before it is engineered.

---


### 49. [Field-Aware RankMixer with Dual-Stream Bilinear Fusion for the Tencent UNI-REC Challenge](https://arxiv.org/abs/2607.15590)

**<font color=#1a73e8>作者：</font>** Yufeng Zhang, Zhengqi Xu, Jiajun Cui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents our solution to the KDD Cup 2026 Tencent UNIREC Challenge. The task requires joint modeling of multi-domain user behavior sequences and non-sequential multi-field features for target-ad pCVR prediction. We develop a Field-Aware RankMixer (FA-RankMixer) with dual-stream bilinear fusion. The model first applies target-aware DIN modules to extract user interests from multiple behavior domains. It also models recent and earlier interests separately for the longest behavior sequence. The model then forms semantic tokens based on feature fields and behavior domains and uses RankMixer blocks for cross-token interaction. A shallow MLP stream complements the deep RankMixer stream, and a group-wise bilinear module fuses their representations. Our final solution ranks ninth on the official leaderboard. Our code is available at this https URL.

---


### 50. [WREN: Low Light Image Enhancement Using Retinex theory-based Double U-Net-like Structures](https://arxiv.org/abs/2607.15604)

**<font color=#1a73e8>作者：</font>** Reina Kaneko, Junya Hara, Hiroshi Higashi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes a neural network for low light image enhancement (LLIE) based on retinex theory to make LLIE robust for various dynamic range scenes. The retinex theory is an image formulation model inspired by a human color perception hypothesis, where a low light image is decomposed into intrinsic color context (i.e., reflectance map) and scene-dependent illumination (i.e., illumination map). Due to non-uniqueness of its decomposition, existing retinex-based LLIE methods often fail to achieve stable decomposition, which lead to over-enhancement. Typically, they are sensitive to the dynamic ranges that vary in different lighting conditions. To tackle this issue, we propose WREN: An LLIE neural network with double U-Net-like structures. WREN consists of two U-Net-like sub-networks. The first network has one encoder and two decoders that decompose an input image into the reflectance and illumination maps. The second network with a customized Transformer block between an encoder and a decoder only enhances the illumination map obtained from the first network: This completely follows the assumption of the retinex theory. Finally, the enhanced illumination map is recombined with the reflectance map. The network is trained end-to-end with a scale-invariant loss function, which gives robustness against the illumination scaling. Numerical results show that our method achieves the state-of-the-art performance across multiple datasets. Our code is available online.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-152](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
