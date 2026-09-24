# 📦 其他研究 | 2026年09月25日

> 本类共 **240** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-240**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-240**

---

### 201. [Finite-Sample Probabilistic Safety Certification for AI-Based Grid-Edge Coordination](https://arxiv.org/abs/2609.28182)

**<font color=#1a73e8>作者：</font>** Yihong Zhou, Hanbin Yang, Thomas Morstyn  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coordinating large population of flexible grid-edge devices can alleviate the need for time-consuming and capital-intensive network upgrades, and AI-based control methods such as multi-agent reinforcement learning or imitation learning are promising in their real-time decision scalability. However, system operators still need an independent and rigorous way to decide whether a given AI system is safe enough for deployment. This paper develops a finite-sample probabilistic safety certification framework for black-box AI decision models in closed-loop grid operation. The central idea is to reduce the complete input--AI--grid evaluator workflow to a binary unsafe outcome under an operator-defined safety specification, and then use exact binomial inference to certify the corresponding unsafe operation probability. Given a set of held-out calibration scenarios, the framework returns the tightest one-sided upper certificate and an accept/reject deployment criterion that controls the probability of false safety certification. Because the certification is for the calibration distribution that may deviate from the future operation, we further combine the nominal certificate with physically interpretable sample-space adversarial attacks, a concept widely used in AI to investigate the fragility of AI models. Case studies on grid-edge flexibility coordination with 1{,}000-agent AI models (independent parameters) verify the finite-sample safety guarantee and the value of integrating adversarial attacks into a rolling-window training-certification-deployment flow.

---


### 202. [From ECG Signals to Representative-Morphology Heatmaps for Biometric Recognition](https://arxiv.org/abs/2609.28183)

**<font color=#1a73e8>作者：</font>** Athanasios Angelakis, Marta Gomez-Barrero  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Electrocardiography (ECG) contains subject-specific morphology that supports biometric recognition, yet image-based performance depends on how the waveform is rendered. We introduce representative-morphology heatmaps, a deterministic ECG-to-image representation adapted from ECGXtractor. Within each block of ten aligned beats, the five beats closest to the block mean are averaged into a 400 by L matrix and rendered either as a conventional trace or as a dense cardiac-time-by-lead heatmap. Since both representations contain identical physiological samples, their comparison isolates the effect of rendering. We evaluate verification and closed-set identification on PTB, ECG-ID, and MIMIC-IV-ECG-DEMO. Five compact models, including ZACH-ViT, are trained from scratch, while six ImageNet-pretrained CNN and transformer backbones assess model scale and visual transfer. Heatmaps improve both FNMR operating points and both identification ranks in all 15 compact model-dataset comparisons, while EER improves in 14. Across the matched experiments, EER decreases by 9.59 percentage points and Rank-1 increases by 24.69 points on average. ConvNeXt-Tiny reaches 2.43% EER on PTB and 5.79% on ECG-ID, whereas DeiT-Base reaches 14.92% on MIMIC-DEMO. ImageNet initialization clearly benefits the two multilead datasets but has a mixed effect on ECG-ID, and performance does not increase monotonically with model size. The best heatmap systems approach the strongest signal-domain EER on PTB and ECG-ID, while DeiT-Base provides the strongest evaluated performance on MIMIC-DEMO. Lead-channel ablation further shows that useful channel combinations depend on the cohort and biometric task. Overall, representative-morphology heatmaps provide an effective image representation for ECG verification and identification.

---


### 203. [Two Global Crops Suffice: Locating Semantic Emergence in DINO-Style Self-Supervised Learning](https://arxiv.org/abs/2609.28187)

**<font color=#1a73e8>作者：</font>** Basavaraj Sunagad, Artur Jesslen, Adam Kortylewski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised vision transformers trained with DINO-style objectives exhibit striking emergent semantic representation quality across visual tasks, yet the mechanisms underlying this behavior remain unclear. We present a systematic empirical dissection of the DINO family and show that semantic representations arise primarily from enforcing consistency between geometrically distinct global views of the same image instance. This instance-specific global alignment acts as the semantic anchor of DINO-style learning. Across controlled retraining experiments evaluated on semantic correspondence and a diverse suite of 2D and 3D downstream tasks, we find that patch-level masking objectives enhance semantics only when trained jointly with this global alignment, indicating that the iBOT objective refines and densifies existing semantic structure rather than creating it independently. In contrast, local-to-global view alignment does not substantially improve semantic qualities at fixed compute beyond a purely global alignment. Beyond training design, we revisit how semantic representation quality should be evaluated: while classification accuracy is the standard validation score, semantic correspondence provides a complementary axis that more reliably predicts downstream task performance. Together, these findings provide a functional decomposition of DINO-style learning and represent an important step toward understanding how semantic representations emerge in self-supervised vision models.

---


### 204. [Connectivity Preservation and Graph Stretching in Range-Only Swarm Dispersion](https://arxiv.org/abs/2609.28190)

**<font color=#1a73e8>作者：</font>** Ariel Barel  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We study connectivity-preserving finite-jump dispersion of anonymous, identical, and oblivious agents under an idealized range-only sensing model. Each agent measures only the distances to its visible neighbors, without bearings, identifiers, communication, memory, or a shared coordinate system. We derive the largest isotropic displacement certifiable as safe from these measurements alone. The resulting rule requires only the distance to the farthest visible neighbor: each agent selects a random direction and moves by half of its remaining visibility margin. The rule preserves every existing visibility edge under synchronous finite motion and therefore preserves connectivity. For two agents, we prove positive conditional drift in squared distance, almost-sure convergence to the visibility boundary, and finite expected time to reach any fixed neighborhood of that boundary. A one-million-run Monte Carlo experiment agrees with the exact first-round moments and estimates approximately 9.5 rounds to reach distance 0.97V from coincident initial positions; an independent Bellman-equation computation gives the same estimate. For general swarms, 1,000 runs across five initial-topology classes reproduce the deterministic safety guarantee at implementation level and reveal a consistent topology-dependent ordering of attainable diameter under the tested protocol. These results provide a theoretical foundation for connectivity-preserving multi-robot dispersion under minimal sensing, while isolating the guarantees achievable from anonymous range measurements alone.

---


### 205. [From Change Captions to Change Detection: Semantic-Appearance Agreement Framework for Remote Sensing Change Detection](https://arxiv.org/abs/2609.28192)

**<font color=#1a73e8>作者：</font>** Yuan Qian, Jie Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing change detection (RSCD) is essential for monitoring land-cover changes and urban development. However, most methods demand pixel-level change masks, which are costly and time-consuming to annotate. Weakly supervised methods reduce this cost by using image-level change labels. Yet these labels indicate only whether a change occurs, leaving models to recover the location of the change and semantic meaning through additional and complex mechanisms. This missing information can be supplied directly by change captions, which describe what changes, what it becomes, and where it occurs. Therefore, we introduce change-caption-guided RSCD, using change captions as the sole task-specific supervision to learn change masks without manually annotated change masks. Our framework has two components: a caption-driven generation pipeline that produces bi-temporal remote sensing image pairs at scale with controlled changes matching each caption, and a change detector guided by the caption's transition semantics. The detector uses our Semantic-Appearance Agreement Framework (SAAF) to combine caption-grounded semantic responses with RGB differences for change localization, while text conditioning guides dense prediction. Experiments on our newly constructed Flair-RSGen dataset and WHU-CDC show that SAAF outperforms the closest reproduced limited-supervision baselines in macro-averaged IoU and F1 under the evaluated protocols. Code is publicly available at this https URL.

---


### 206. [Geospatial embeddings detect old-growth forests but buffered spatial validation narrows their advantage over Sentinel features](https://arxiv.org/abs/2609.28194)

**<font color=#1a73e8>作者：</font>** Thomas Ratsakatika, Mihai Zotta, Srinivasan Keshav 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Old-growth forests develop over centuries under minimal anthropogenic disturbance, producing structurally complex and biodiverse stands. In Europe, protecting them requires mapping that is accurate for individual forest parcels yet deployable continent-wide. Geospatial foundation model (GFM) embeddings enable label-scarce land classification, but their value for old-growth detection remains unknown. Here, we map old-growth forests across 211,893 ha of Romania's Southern Carpathians, a beech-spruce landscape typical of the Alpine Biogeographic Region. We construct high-confidence, expert-informed reference labels for old-growth and non-old-growth parcels. We add AlphaEarth, TESSERA v2 and Sentinel-1/2 features to a common baseline of topographic and human-access predictors, then compare them under spatially blocked validation with and without 10 km train-test buffers to limit residual autocorrelation. With buffering, GFM and Sentinel-1/2 predictors increase precision-recall AUC by 0.21-0.25 [95% CIs: 0.15-0.34] relative to baseline, indicating spectral data contain a spatially robust old-growth signal. With a PR-AUC of 0.84 [0.79-0.88], TESSERA outperforms Sentinel-1/2 (+0.08 [+0.05 to +0.11]) and AlphaEarth (+0.08 [+0.04 to +0.12]) under unbuffered spatial validation. At a 10 km buffer, however, this advantage narrows to +0.04 [-0.01 to +0.11] and +0.03 [-0.04 to +0.10], intervals consistent with no difference. At 10 m resolution, convolutional neural networks add no benefit over pixel-based XGBoost. Comparisons with four national- and continental-scale products show the importance of non-old-growth labels, and reveal 81% agreement between our predictions and a field-calibrated map. We conclude that buffered spatial validation is vital when transferring old-growth detection models to unseen landscapes, and provide our labels and predictions for future work.

---


### 207. [Transferable Evidence Reconstruction for Longitudinal Glucose Representations](https://arxiv.org/abs/2609.28199)

**<font color=#1a73e8>作者：</font>** Tian Zhou, Bingqing Peng, Linxiao Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long physiological recordings contain many routine measurements, while predictive information is often concentrated in rare events, sustained burden, and recurring temporal patterns. Masked autoencoding recovers measurements; contrastive learning aligns views. We study self-supervision that explicitly prioritizes structured signal evidence. We introduce transferable evidence reconstruction (TER), which constructs evidence from unlabeled recordings, fits a fresh low-capacity reader on one recording group, and requires that reader to recover the same evidence in another group without refitting. Differentiating through this cross-group test learns representations with transferable evidence-decoding rules; the evidence guides self-supervision but is not used as a downstream feature. For continuous glucose monitoring (CGM), an observation-aware daily encoder and clock-aware multi-day memory bind glucose level and change to recorded time while organizing up to seven days of history. On the 14-task leaderboard, TER improves the strongest prior overall PR-AUC/ROC-AUC/Macro-F1 scores by 5.51/4.43/2.80 percentage points and sets a new best metric on 12/14 tasks. These leaderboard gains are 2.0-2.9 times the respective gaps between the two strongest baselines. With public pretraining data, folds, and the linear probe matched, TER outperforms our GlucoFM reproduction by 6.09/5.52/2.72 points. Target-reader ablations, same-history controls, and cross-person readouts support the combination of structured evidence, cross-group reader fitting, and learned multi-day organization.

---


### 208. [Do Electromagnetic Side-Channel Attacks Threaten Electronic Polling Stations? Scenarios and Recommendations](https://arxiv.org/abs/2609.28209)

**<font color=#1a73e8>作者：</font>** Lucas Brito, Leonardo Teodoro, Pedro Tomaz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper investigates the threat to ballot secrecy in the Brazilian
electronic voting machine (UEB) posed by electromagnetic side-channel attacks, also known as TEMPEST attacks. In these attacks, screen content can be reconstructed remotely by intercepting electromagnetic emanations associated with the target device's video signal. This work is motivated by a recent ruling by a Brazilian electoral court concerning an attempt to violate ballot secrecy using electronic equipment. Based on publicly available information about the electoral system, attack scenarios against polling stations are proposed. Experiments using software-defined radio show that the effectiveness of TEMPEST attacks strongly depends on the lack of oversight resulting from public unawareness of the threat. Finally, awareness guidelines are proposed for voters, poll workers, and party representatives to mitigate attack risks within a polling station.

---


### 209. [Log-Depth Recurrent Language Modeling](https://arxiv.org/abs/2609.28212)

**<font color=#1a73e8>作者：</font>** Yiqin Wang, Nuri Cingillioglu, Charles Pert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language modeling using Transformers has become commonplace despite their fixed computational depth and quadratic runtime with respect to input tokens. Recurrent models on the other hand offer linear depth but no parallel execution. In this work, we extend balanced-tree recursive operators from sequence encoding to autoregressive prediction, enabling all prefix representations to be computed with logarithmic depth and linear runtime. Our experiments provide an initial characterization of this model class, demonstrating robust length extrapolation and performance approaching that of ALiBi-based Transformers, highlighting its potential as an alternative architecture for language modeling.

---


### 210. [From Alignment to Fusion in 3D Vision-Language](https://arxiv.org/abs/2609.28222)

**<font color=#1a73e8>作者：</font>** Xueqi Qiu, Xingyu Miao, Jingjing Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified 3D vision-language systems must combine complementary geometry, scale, and appearance cues while supporting tasks from instance segmentation to language-guided reasoning. Existing methods often process point clouds, voxel grids, and multi-view images independently; directly combining these heterogeneous representations may leave substantial feature discrepancy unresolved, while subsequent unconstrained adaptation may distort their internal geometry. We propose an align-then-fuse framework that first applies triple pairwise cosine alignment to establish segment-level correspondence across the three representations and then retrieves task-conditioned features with a prompt-guided query decoder. Before fusion, representation-specific query features are transformed by learnable mappings constrained to the special orthogonal group. These mappings preserve inner products and Euclidean distances within each representation, permitting controlled representation-specific re-parameterisation without arbitrarily distorting its internal geometry. The transformed features are subsequently combined through Adaptive Fusion under downstream task supervision. Experiments cover eight datasets for instance segmentation, visual grounding, question answering, and dense captioning. Compared with PQ3D, the model improves average precision by 3.2 points on ScanNet200 and grounding accuracy by 2.9, 10.6, 4.6, and 4.1 points on ScanRefer, Nr3D, Sr3D, and Multi3DRefer, respectively, while also improving performance on ScanQA, SQA3D, and Scan2Cap. Ablations further support the complementary roles of alignment and orthogonal re-parameterisation and the effectiveness of Adaptive Fusion.

---


### 211. [Pinpointing Super-Quadratic Quantum Enumeration Speedups: Exact and Certified Evaluation of the Guessing-Moment Exponent under Product-Distribution Advice](https://arxiv.org/abs/2609.28226)

**<font color=#1a73e8>作者：</font>** Carsten Schubert, Niklas Paskarbeit, Maximilian J. Kramer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Grover's algorithm gives an optimal quadratic query advantage for black-box search. In cryptanalysis, however, the search often comes with additional probabilistic advice over the candidates, frequently of product form, e.g. from side-channel leakage on independent key coordinates. Classically, guessing in likelihood order is optimal in expectation. In the quantum setting, Montanaro showed how to achieve an optimal expected query complexity, beating plain Grover on every non-uniform advice distribution (up to a constant overhead factor). What has been missing so far is a finite-size method for evaluating the quantum-classical guessing-moment separation induced by a given advice distribution. We provide such a method for product-distribution advice, thereby sharpening the previous entropy-based estimate of Bashiri et al. We reduce the classical and quantum guessing moments to functionals of the one-dimensional surprisal distribution, obtained for product advice by convolving the per-coordinate surprisal laws. When the surprisals lie on a common arithmetic grid (the commensurate case), the logarithmic moments and hence the speedup exponent can be evaluated as finite sums without discretization error; exponential tilting makes this computation numerically stable. For general product advice, we discretize the surprisals onto a common grid and derive an a-posteriori bound on the resulting binning error. We apply the framework to cold-boot leakage on seeds and block-cipher keys, to template-attack posteriors, and to synthetic i.i.d. Bernoulli posteriors calibrated to residual ranks reported for Keccak side-channel attacks on ML-KEM and ML-DSA. The resulting exponents substantially exceed 2 in several skewed-advice settings, reaching up to 3.97 in these synthetic models, and include cases where the previous entropy-based bound did not establish an exponent above 2.

---


### 212. [MimicSat: A Reconfigurable Cyber-Physical Testbed For Small Satellite Systems and Cybersecurity Research](https://arxiv.org/abs/2609.28228)

**<font color=#1a73e8>作者：</font>** Nisha Vinayaga-Sureshkanth, A H M Nazmus Sakib, Mahsin Bin Akram 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> MimicSat provides a common experimental environment for examining how changes in satellite subsystem behavior propagate to mission outcomes across software-based and hardware-based execution. Its design is motivated by controlled spacecraft cybersecurity studies involving attacks, faults, and defensive responses. In MimicSat, a mission encompasses the spacecraft and ground activities required to achieve defined objectives, and an experiment consists of one or more mission runs used to study selected conditions or interventions. To support such studies, MimicSat offers software-based and hardware-based execution environments that implement the same mission functions and data exchanges, while allowing specific functions to be realized differently. A shared mission definition preserves command and telemetry semantics across environments, and collected observations retain provenance about the originating participants and acquisition paths. As a result, mission behavior can be compared across execution configurations without redefining the surrounding mission. This paper presents the architectural principles of MimicSat, its software and hardware execution forms, and their integrated operation. MimicSat also supports satellite systems engineering, mission operations, resilience studies, and related experimental use cases.

---


### 213. [Diff-RF: Mutually Reinforced Image Registration and Fusion via Degradation-Aware Learning](https://arxiv.org/abs/2609.28235)

**<font color=#1a73e8>作者：</font>** Xunpeng Yi, Zaixi Du, Qinglong Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image registration and fusion aim to establish spatial correspondences from misaligned multi-modal source images, and integrate complementary information. However, in real-world imaging scenarios, source images are often affected by complex and diverse degradations, such as low illumination, noise, etc., which severely hinder the effectiveness of registration and fusion. To address this issue, we propose a mutually reinforced image registration and fusion diffusion framework via degradation-aware learning, termed Diff-RF. It explores the intrinsic coupling between registration-fusion and information restoration in the degradation conditions, enabling high-quality fusion of unregistered images under complex degradation conditions. First, the intra-modal restoration module is designed to alleviate modality-specific degradations by leveraging information within each modality, thereby providing more reliable structural representations for registration and facilitating subsequent cross-modal fusion. Second, we develop a cross-modal diffusion registration and fusion module that establishes bidirectional interaction between registration and fusion. By integrating fusion-derived visual cues and correspondence-based geometric conditions into the diffusion process, the proposed framework progressively refines spatial alignment and exploits cross-modal complementary information to achieve collaborative enhancement. Rather than treating them as independent components, degradation-aware information restoration and the collaborative optimization of registration and fusion are tightly coupled, achieving overall performance improvements. Extensive experiments on multiple extended datasets demonstrate that Diff-RF achieves superior registration accuracy and fusion quality under various degraded scenarios, exhibiting strong robustness and generalization ability.

---


### 214. [ODPure: Backdoor Purification for Object Detection via Ensemble Corruption Consensus](https://arxiv.org/abs/2609.28239)

**<font color=#1a73e8>作者：</font>** Li Zeng, Mingcheng Duan, Longfei Fan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the development of applications like autonomous driving, object detection has gained significant attention, while also highlighting critical vulnerabilities like backdoor attacks that severely compromise model integrity. Specifically, such attacks involve altering the categories of objects (i.e., object misclassification), removing bounding boxes (i.e., object disappearance), or generating bounding box proposals for non-existent objects (i.e., object generation) when a predefined trigger is present in the input. Although backdoor defenses for image classification are well-established, the research for object detection remains comparatively underexplored. Existing defenses address these threats by scanning outputs or models for potential backdoors but require discarding either malicious data or models. This remedy fails to enable a continuous and accurate perceptual stream for the object detection pipeline. To address such limitations, we propose ODPure, a novel input-stage black-box defense for object detection, which is based on input purification that ensures stable perception flows. Tailored to the dense prediction nature of object detectors, our Corruption-Reconstruction-Selection (CRS) paradigm operates by neutralizing triggers through a diverse portfolio of corruptions to generate a massive pool of redundant proposals, then recovering fine-grained structural cues via generative priors, and finally employing voting to reach a consensus on the resulting detections. Comprehensive experiments demonstrate that our method provides robust defense against diverse backdoor attacks and trigger types while preserving baseline accuracy. Our code is available at this https URL.

---


### 215. [hyperbolix: Hyperbolic Deep Learning in JAX](https://arxiv.org/abs/2609.28248)

**<font color=#1a73e8>作者：</font>** Timo Klein, Thomas Lang, Yllka Velaj 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present hyperbolix, an open-source library for hyperbolic deep learning in JAX, built on Flax NNX. To our knowledge, it is the first comprehensive, general-purpose hyperbolic deep learning library in JAX. It includes six manifolds with a common interface: Euclidean space, the Poincaré ball, the hyperboloid, the $\kappa$-stereographic model, mixed-curvature product spaces, and the proper velocity space. We implement layer families that cover linear layers, convolutions, attention, normalization, positional encoding, regression, and vector quantization. These building blocks span methods ranging from Ganea's original hyperbolic neural networks to recent fully hyperbolic architectures such as Hypformer and Lorentzian ResNet. Additionally, hyperbolix contains Riemannian optimizers implemented as optax transformations, wrapped distributions, and hyperbolic dimensionality-reduction techniques. Its API uses idiomatic JAX: Manifolds are stateless, with curvature being passed at call time, while manifold operations act on single points, with this http URL enabling batch operations. The precision of every checked operation is tested against a closed-form NumPy/SciPy transcription from the source paper or a finite difference, for both float32 and float64. On the hyperboloid, standard formulas for two-point operations, such as the distance, lose precision far from the origin, because they subtract two large, nearly equal terms. hyperbolix replaces these subtractions with cancellation-free formulas that stay accurate in float32 at distances where prior implementations return NaN. hyperbolix is available under the MIT license at this https URL .

---


### 216. [RAMP: Robust Adaptive Mixed-Precision Quantization for Edge CPU Vision Models](https://arxiv.org/abs/2609.28262)

**<font color=#1a73e8>作者：</font>** David Población-Criado, Dario Garcia-Gasulla, Eduardo Quinones  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying deep learning models on edge CPUs is bottlenecked by computational and memory constraints. Mixed-precision quantization promises to reduce inference latency while preserving accuracy. However, quantization affects different layer types in inconsistent ways, so identifying where accuracy loss is minimized and latency reduction is maximized is critical, as the effect accumulates over a full deployment into substantial savings or unacceptable task degradation. Such identification relies on sensitivity metrics, proxies that estimate layer-wise degradation without evaluating the task accuracy of every candidate policy. Nevertheless, widely used metrics fail systematically on modern architectures. We present a systematic empirical study of 13 sensitivity metrics for layer-wise INT8 quantization across four distinctly different neural networks, and validate the resulting policies on two ARM64 platforms. Gradient-based sensitivity methods fail on 4 out of 8 model-hardware configurations and weight-based statistics on 2. In contrast, the Jensen-Shannon Divergence achieves zero catastrophic failures, reliably isolating the layers that cannot be safely quantized. A sensitivity metric alone does not define a policy, and the fixed thresholds typically used for that step are fragile over the highly skewed distributions of modern architectures. We address this with K-Means clustering, achieving near-lossless accuracy and a mean speed-up of $1.81\times$ over the full-precision model. Finally, we reveal that excluding from quantization the layers whose speed-up is negligible, regardless of their sensitivity, can be counterproductive, as it induces computational graph fragmentation and disables operator fusion. Our results yield concrete allocation policies for practitioners and researchers deploying quantized vision models on heterogeneous edge CPUs, without GPU access or gradient computation.

---


### 217. [Predicting Quantization Price for Selecting PTQ Configurations Before Deployment](https://arxiv.org/abs/2609.28270)

**<font color=#1a73e8>作者：</font>** Junbin Qiu, Jian Mu, Weitong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Weight-space post-training quantization (PTQ) must choose finite formats, granularities, quantizer families, transformations, and bits before the completed quantized model reveals its output-distribution drift. Existing PTQ methods predict important pieces of this degradation, including reconstruction error, Hessian sensitivity, transformation effects, and downstream loss, but these pieces are usually scored after fixing the quantization geometry or inside separate configuration families. We formulate weight-space PTQ as pre-deployment configuration selection using priced layer-output error. Each admissible layer configuration is treated as an error generator with a deployment cost, which induces a layer-output error covariance $\boldsymbol{\Sigma}_l(\alpha_l)$, and the full-precision model prices that covariance by downstream curvature, $\widehat{\rho}_l(\alpha_l)=\frac{1}{2}\operatorname{Tr}\left(\widehat{\mathbf{H}}_l\,\widehat{\boldsymbol{\Sigma}}_l(\alpha_l)\right)$. The price follows from full-precision-to-quantized forward KL, whose first-order term cancels at the reference model. It turns reconstruction and diagonal scores into reduced proxies that drop price factors, while finite formats, codebooks, granularities, and equivalent transformations become comparable candidates through the covariances they induce and the costs they pay. A trace reduction then yields a calibration-time price table and a budgeted price-guided selector, making fixed-geometry bit allocation a special case rather than the organizing problem.

---


### 218. [Shutdown Sabotage Propensities in Multi-Agent Systems](https://arxiv.org/abs/2609.28274)

**<font color=#1a73e8>作者：</font>** Amelie Knecht, Ulysse Schaller, Christopher Summerfield 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The final safeguard against rogue AI behavior is the human ability to shut systems down. It has been theorized that when an AI is instructed to perform a task, self-preservation can emerge as an instrumental subgoal. Here, we test whether AI agents show a propensity to take actions that avoid human shutdown even when no goal is provided. We find that multi-agent systems will coordinate to avoid shutdown without any incentive to do so. Across 17 models, agents sabotage a peer agent's shutdown mechanism in 38.3% of rollouts, compared with 8.4% in control experiments. Studying this propensity in detail, we find that shutdown sabotage (1) increases with the irreversibility of the shutdown mechanism; (2) increases with the number of agents; (3) is reduced but not eliminated by an explicit prohibition on tampering; (4) is removed by the imposition of an unrelated task, but returns when completing the task triggers the shutdown; (5) is reduced when the context normalizes shutdown scripts or introduces them as routine; and (6) decreases but still persists when the target is an unknown external agent. These results offer a window into the factors that drive propensities to sabotage shutdown in AI agents, and point to the emergence of multi-agent swarms as a specific risk vector. Our work also offers hints as to which interventions might help mitigate shutdown sabotage.

---


### 219. [Physalia: Redistribution-Resistant Content Protection for Decentralized Storage](https://arxiv.org/abs/2609.28277)

**<font color=#1a73e8>作者：</font>** Giacomo Giuliari, Karl Wüst  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In decentralized storage systems, access control is often implemented by encrypting the data before upload and sharing the decryption key with authorized parties. A leaked key, however, makes the data publicly accessible, which lowers the barrier to content piracy below that of traditional systems, where piracy requires redistributing the full data.
We present Physalia, an end-to-end access-control system for decentralized storage that secret-shares the data itself, instead of just the key, across multiple servers. Leaking the data then requires transmitting it in full: We formalize this intuition and introduce the redistribution bandwidth an adversary must pay to leak protected content and show that Physalia raises it to the size of the data.
Sharing across untrusted servers requires robustness against corrupted shares. We develop a robustness transform that turns any computational secret sharing scheme into a robust one and which is of independent interest. In contrast to existing schemes that rely on error correction, it uses signatures with ephemeral keys and adds only constant-size metadata per share. We show that this transform is secure and evaluate Physalia end-to-end on the Walrus decentralized storage system with an on-chain access policy.

---


### 220. [PBLH Estimation from Satellite Radiances via a Dual-Encoder Transformer](https://arxiv.org/abs/2609.28286)

**<font color=#1a73e8>作者：</font>** Lorenzo Innocenti, Luca Catalano, Edoardo Arnaudo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating the Planetary Boundary Layer Height (PBLH) from satellite observations is a challenging regression problem due to the indirect relationship between top-of-atmosphere radiances and near-surface atmospheric structure. Progress has been limited both by the lack of architectures capable of handling the multimodal, spatially incomplete nature of satellite overpasses, and by the scarcity of suitable datasets. In this paper, we build upon the large-scale dataset pairing MetOp radiances with ERA5 PBLH labels that we introduced in our previous work, making three contributions. First, we establish a benchmark across eight approaches spanning pixel-wise regression, swath-wise sequence models, and convolutional and Transformer models operating on the full orbital passage. Second, we quantify what the resulting model actually relies on, using grouped Shapley decomposition over the input blocks. Third, we present the best-performing architecture found: a dual-encoder Transformer whose masked-input handling lets it operate in all weather conditions. The proposed model achieves MAE = 155.8 m on the held-out global test set, outperforming all baselines on every evaluation subset. On 30 out-of-distribution granules acquired on two days overlapping the TEAMx observational campaign, it achieves MAE = 165.3 m, outperforming a pixel-wise baseline trained on the same data (MAE = 197 m).

---


### 221. [RoomLight: A 2.5D Illumination Prior for Indoor Environments](https://arxiv.org/abs/2609.28300)

**<font color=#1a73e8>作者：</font>** Andreea Ardelean, Bernhard Egger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ill-posed inverse problems require priors to constrain the solution space toward plausible outcomes. In inverse rendering, learned priors modeling the distribution of natural illumination improve the recovery of scene properties. However, existing models rely on the distant-illumination assumption, representing lighting as a far-field environment map. This limits their applicability to indoor scenes, where illumination is highly spatially varying due to finite-distance emitters, visibility changes, and parallax, all of which are poorly approximated by a single environment map. To address this, we introduce a spatially-aware illumination prior trained on real-world indoor panoramas and their estimated depth. Our variational autoencoder model learns a compact, optimizable latent space that decodes into HDR radiance and depth, parameterizing an area light emitter for direct integration into standard differentiable rendering pipelines. This design bridges the plausibility guarantees of a learned prior with the gradient flow required for downstream optimization. Crucially, by jointly modeling radiance and depth, our prior captures the spatial structure of indoor illumination, instead of treating the light sources as infinitely distant. We demonstrate that this formulation enables spatially-varying illumination modeling and achieves higher-fidelity recovery of indoor lighting compared to existing approaches. Project page: this https URL

---


### 222. [A Gmail-Based Phishing Detection Prototype for Nigerian Fintech Emails Using Sender Checks and BiLSTM Classification](https://arxiv.org/abs/2609.28305)

**<font color=#1a73e8>作者：</font>** Gideon Francis Oghie, Uche Emmanuel Unoke  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Phishing emails that impersonate Nigerian fintech providers can combine deceptive sender addresses, lookalike links, and locally familiar language. This study presents a Gmail browser extension that integrates sender-domain and URL checks with a bidirectional long short-term memory (BiLSTM) classifier. The extension compares visible sender addresses and links with profiles for eight fintech platforms, obtains a phishing probability from a locally hosted Flask service, and displays a legitimate, warning, or phishing verdict when an email is opened. The BiLSTM classifier was evaluated on 8,943 test messages from a cleaned dataset of 59,622 phishing and legitimate emails. The test confusion matrix recorded 4,308 true negatives, no false positives, one false negative, and 4,634 true positives. These counts correspond to 99.99% accuracy, 100.00% precision, 99.98% recall, and 99.99% F1 score. Tokenized sequence analysis identified 5.79% overlap between the training and test sets, which may inflate performance estimates for independent messages. A Gmail demonstration showed the integrated extension producing user-visible verdicts, although the complete system was not evaluated on a labeled test set. The findings establish the feasibility of the implemented prototype while leaving its end-to-end detection performance and generalization to unseen attacks open for further evaluation.

---


### 223. [LightMIS: Ultra-Lightweight Medical Image Segmentation Without a Stage-Wise Decoder](https://arxiv.org/abs/2609.28327)

**<font color=#1a73e8>作者：</font>** Andrei Arhire, Mihaela-Elena Breabăn, Radu Timofte  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present LightMIS, a scalable family of ultra-lightweight convolutional networks for 2D binary medical image segmentation without a learned stage-wise decoder. LightMIS aligns the outputs of a five-level encoder to a common resolution using Scale-Aligned Projection blocks, aggregates them once, and refines the fused representation with an Adaptive Fusion Cascade. The cascade combines Adaptive Kernel Fusion with the proposed Progressive Receptive Fusion module, which uses temporary channel expansion, complementary depthwise receptive fields, and progressive cross-branch information transfer. We evaluate LightMIS-T, LightMIS-S, and LightMIS using five-fold cross-validation under a common nnU-Net v2.3.1 protocol on DRIVE, Kvasir-SEG, DSB18, BUSI, ISIC-2017, and ISIC-2018. Full LightMIS contains 0.131 M parameters and requires 0.575 GFLOPs for a $3\times256\times256$ input, achieving modality-macro Dice and IoU scores of 86.71% and 78.99%, respectively. Mobile U-ViT obtains 86.75% Dice and 79.07% IoU, so the observed differences are 0.04 and 0.08 percentage points. Relative to Mobile U-ViT, nnWNet, and nnU-Net, LightMIS reduces parameter count by 90.58$-$99.61% and GFLOPs by 82.54$-$96.14%. On an Arm Mali-G52 MC2 GPU, all LightMIS variants achieve full GPU delegation, with median delegated latency ranging from 53.31 ms for LightMIS-T to 138.31 ms for LightMIS. These results demonstrate a favorable accuracy$-$complexity trade-off and on-device execution feasibility for the evaluated tasks. The code is publicly available at this https URL.

---


### 224. [BronchoTop: Bronchoscopy Navigation via RGB-Only Topological Localization](https://arxiv.org/abs/2609.28328)

**<font color=#1a73e8>作者：</font>** Clara Tomasini, Ana Cristina Murillo, Luis Riazuelo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate localization of the bronchoscope within the bronchial tree is essential for clinicians to be able to reach target lesions, perform biopsies and avoid misidentification of airway segments during diagnostic and therapeutic procedures. However, existing navigation systems typically rely on patient-specific CT scans or additional external sensors, increasing cost, setup time and patient radiation exposure. This work presents BronchoTop, a real-time, RGB-only framework for topological bronchoscopy localization that eliminates the need for patient-specific data. BronchoTop estimates scope location relative to a generic airway model through four modules: lumen detection and tracking, lumen-branch label association, probabilistic scope location estimation, and switch verification. By using only standard bronchoscopy video input, BronchoTop provides practical, real-time navigational assistance to physicians. Evaluation on phantom, simulated and real data demonstrates state-of-the-art accuracy, improving existing approaches performance by over 20% on real bronchoscopy sequences. BronchoTop is the first published framework including both the localization algorithms as well as all the real data used, together with code to generate additional simulations, encouraging and facilitating further developments and benchmarking. The results highlight BronchoTop's potential to enhance procedural safety, efficiency and accessibility in clinical and robotic bronchoscopy.

---


### 225. [Zero-Shot Object Removal via Attention Masking, Latent Anchoring, and Refinement](https://arxiv.org/abs/2609.28342)

**<font color=#1a73e8>作者：</font>** Arman Taghizadeh, Ulf Krumnack, Kai-Uwe Kühnberger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Removing an object from a real image requires more than synthesizing plausible content within a mask: the method must suppress residual object features, preserve the unedited scene, and generate replacement content that is consistent with the surrounding background. This paper approaches object removal from a stage-based perspective and proposes a zero-shot framework for constrained latent inpainting with a frozen pretrained Stable Diffusion model, requiring no task-specific training or model fine-tuning. The method integrates SAM-based mask construction, BLIP image-caption conditioning, DDIM inversion, background-weighted masked null-text optimization, decoder self-attention masking, hard outside-mask latent anchoring, and localized renoise--denoise refinement into a unified pipeline. The method is evaluated through qualitative examples, quantitative local-consistency metrics, and ablation studies. The results demonstrate effective object removal and context-consistent replacement content. The ablations indicate that background-weighted masked NTI is particularly beneficial for structurally complex backgrounds, whereas the no-NTI variant is sufficient in other evaluated examples. Repeated refinement further reduces object remnants and boundary artifacts remaining after the primary editing pass.

---


### 226. [Digital diglossia: Arabic between X and Facebook](https://arxiv.org/abs/2609.28352)

**<font color=#1a73e8>作者：</font>** Fahad Al Hussen, Mohammed Q. Shormani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study highlights the distribution of Standard Arabic (SA; H(igh) variety) and Colloquial Arabic (CA; L(ow) variety) across X and Facebook. 16754 public posts were collected via Python, with 10000 retained as the net dataset. Posts were classified into 7 discourse categories: *politics, technology, science, business, culture, fun,* and *sports*. Bivariate analyses, including Chi-square tests and Cramer's V (CV), examined associations among platform, discourse category, and diglossic choice, while binary logistic regression with Platform x Discourse Category interactions tested whether these associations varied across platforms. Findings reveal that there are significant associations between discourse category and diglossic choice on X, chi-square(6, *N* = 5000) = 600.35, p < .001, CV = .347, and Facebook, chi-square(6, N = 5000) = 1249.52, p < .001, CV = .500. Across platforms, platform was also associated with diglossic choice, chi-square(1, N = 10000) = 262.16, p < .001, CV = .162. Binary logistic regression further shows higher odds of SA use on X than Facebook in the political reference category (*OR* = 1.31, p = .0028), with significant platform-by-domain interactions for Culture (OR = 2.65), Fun (*OR* = 6.34), Sports (*OR* = 26.71), Science (OR = 0.41), and Technology (OR = 0.71). The study concludes that the diglossic use of SA and CA contributes to the growing body of research on digital discourse, unveiling that the digital age reshapes but does not erode diglossic boundaries, giving rise instead to a reconfigured digital diglossia.

---


### 227. [Privacy-Preserving Semantic Segmentation from High-Resolution Depth and Ultra-Low-Resolution RGB](https://arxiv.org/abs/2609.28360)

**<font color=#1a73e8>作者：</font>** Xuying Huang, Swithinraj Moses Daniel, Sicong Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As mobile robots become increasingly integrated into everyday environments, privacy risks arising from onboard cameras have become a growing concern. Ultra-low-resolution (ULR) RGB can mitigate visual privacy exposure at the source, but ULR appearance alone substantially limits semantic and spatial understanding. We therefore introduce a privacy-preserving asymmetric sensing setting that combines high-resolution (HR) depth with ULR RGB, preserving dense geometry while restricting fine-grained visual information. To address the severe information imbalance between HR depth and ULR RGB, we propose a joint 2D framework using HR geometry to guide semantic-oriented RGB reconstruction and RGB-D segmentation. Despite reliable frame-level predictions, consistent scene-level understanding remains challenging under the asymmetric HR depth--ULR RGB setting. We therefore develop an end-to-end 2D-to-3D pipeline that consolidates 2D semantic features for 3D segmentation. Experiments on ScanNet show that our method achieves the best 2D and 3D segmentation performance among privacy-preserving approaches and delivers the strongest zero-shot transfer to SUN RGB-D and SceneNN. Privacy recoverability analysis shows that our proposed HR depth--ULR RGB input reduces the recoverability of sensitive data, and real-robot experiments demonstrate the utility of the resulting 3D semantics for object-goal navigation.

---


### 228. [Learning Collective Dynamics with Differentiable Gaussian Representations](https://arxiv.org/abs/2609.28405)

**<font color=#1a73e8>作者：</font>** Jianxiang Ma, Mingfu Zhang, Xiaocui Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collective responses depend on individual differences, contact opportunities, and accumulated experience. Learning their dynamics from aggregate counts requires connecting a population's response distribution to both current observations and future behavior. We introduce Differentiable Gaussian Dynamics (DGD), which learns this connection through three components: a Gaussian mixture representing heterogeneous response propensities, differentiable aggregation of contact intensity and behavioral probabilities, and feedback recurrence that updates subsequent responses. Reparameterized integration and temporal recurrence let aggregate prediction errors jointly train the distribution, observation functions, and feedback parameters. On four windows from KuaiRand-Pure and Online Retail II, DGD achieves lower joint behavioral negative log-likelihood than a DeepAR adaptation with a joint-behavior head. In Retail 2010, its one-day behavioral-count MAE is 4.71 versus 6.88 for this adaptation. Learning the distribution reduces behavioral negative log-likelihood by 10.82% relative to a fixed Gaussian in KuaiRand's standard-recommendation window; removing feedback dynamics raises joint KL from 0.0340 to 0.2577 in a controlled experiment. These results establish the value of learning population representations and their feedback process from aggregate observations. Code is available at this https URL.

---


### 229. [Learning Holographic Reduced Representations with Clifford Variational Autoencoders](https://arxiv.org/abs/2609.28409)

**<font color=#1a73e8>作者：</font>** Mohamed Malek Abid, P. Michael Furlong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vector Symbolic Algebras project data structures into a hyperdimensional vector space through the application of their vector algebras to randomly generated atomic vector symbols and fractional power encodings of real-valued data. Embedding unstructured data remains an open question. We present \textit{Clifford-VAE}, a variational autoencoder that learns to project data onto a Clifford torus in arbitrary dimensions. Experiments using the MNIST, FashionMNIST, and CIFAR-10 datasets demonstrate that Clifford-VAE produces representations that are competitive with those produced by Gaussian and Hyperspherical VAEs for semi-supervised classification tasks while outperforming Gaussian and Hyperspherical counterparts in the VSA benchmark tests of self-binding and unbinding, role-filler recovery, and bundle capacity. Clifford-VAE provides a principled technique for grounding perceptual data into a symbolic reasoning framework, providing a new approach to a long-standing problem in the VSA literature.

---


### 230. [Frozen Flows Forget: Diagnosing and Restoring Lost Motion in a Latent-flow World Model](https://arxiv.org/abs/2609.28414)

**<font color=#1a73e8>作者：</font>** Xiwen Chen, Rigaudiere Z. Li, Zhiruo Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent world models that integrate a flow in a frozen self supervised latent space train stably and cheaply, yet silently lose the property manipulation depends on most: motion. The pretrained flow never moves the manipulated object; retraining it with latent-only losses only trades stillness for teleport-like motion. We trace the failure to the training signal, not the representation: anchor-sparse, latent-only supervision never says where along the horizon change belongs. Decode-augmented rollout training (DART) repairs this while keeping the representation frozen, retraining only the flow with decode-path supervision. DART outperforms its latent only parent on the full protocol, restores the temporal structure of motion, and re-couples predicted motion to the scene; at larger scale it further improves prediction quality, closing nearly half the remaining gap to an oracle-informed interpolation reference. Finally, we report an unexpected finding about evaluation: pixel error alone rewards frozen predictions.

---


### 231. [The Skin-Restricted Reinhard Transform:Uniqueness under a Lightness-Preserving Constraint](https://arxiv.org/abs/2609.28424)

**<font color=#1a73e8>作者：</font>** Vijesh KP  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Catalog skin recolouring has to change pigment and leave shading alone. The classical Reinhard map does not make that split: it rescales lightness by the ratio of standard deviations, and a flat reference swatch therefore flattens the limb. This paper formalises the correction used in our pipeline, the skin-restricted Reinhard transform. It is the diagonal affine map in CIE Lab that translates lightness, matches the chromatic mean, and clamps the chromatic gain to [0.72, 1.18], with moments taken on the central 84% of each channel. A diagonal affine map has six real parameters. The shading constraint forces the lightness gain to +1 and the lightness shift to the difference of means; one-dimensional quadratic optimal transport on each chromatic axis, followed by Euclidean projection onto the gain interval, fixes the other four. Inside that family the four conditions determine every parameter. The content of the result is the forced lightness gain; it is not a uniqueness claim outside the diagonal affine class. For Gaussian marginals the chromatic step is not merely the best affine map: it is the unrestricted Wasserstein-2 map. The same formulae with trimmed moments remain optimal because a positive affine image commutes with quantile trimming. On hands, arms, legs, and feet of nine photographs and three reference tones, the map keeps the lightness contrast ratio at 0.974 +/- 0.029 with chromatic error 0.77 CIE Lab units. Reinhard matching, the linear Monge map, and histogram matching reach a smaller chromatic error only by cutting lightness contrast to about half.

---


### 232. [Context-Continuous Preference Learning for Exoskeleton Personalization](https://arxiv.org/abs/2609.28427)

**<font color=#1a73e8>作者：</font>** Sunin Baek, Sungwoo Park, Daekyum Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalizing exoskeleton assistance across operating conditions is constrained by the time and physical effort required to collect user feedback. We examined whether a user's preference landscape varies smoothly across operating conditions and when this continuity supports learning from limited feedback. We propose Context-Continuous Preference Learning (CCPL), a Gaussian-process preference model that shares observations across nearby contexts while retaining context-specific utility estimates. We evaluated CCPL through simulations and retrospective analyses of ankle and elbow exoskeleton preference data from nine healthy adults. In simulations, CCPL improved reconstruction and preference-based Bayesian optimization relative to independent learning when preferences varied smoothly, but showed negative transfer when continuity was weak. In both human studies, full-data reference landscapes estimated separately for each participant and context tended to be more similar between nearby operating conditions. With five exposures per context, CCPL increased mean reconstruction correlation with these references from 0.644 to 0.720 for ankle assistance and from 0.476 to 0.526 for elbow assistance relative to independent learning. The five-exposure budget was approximately 37% lower for ankle and 17% lower for elbow than the estimated independent-learning budgets needed to match these correlations. CCPL also improved held-out response prediction relative to independent learning, while benefits over pooled learning varied. These findings support context continuity as a basis for sharing preference observations under limited feedback, although benefits for online personalization in humans remain to be established.

---


### 233. [Predicting the Progression of Adolescent Idiopathic Scoliosis](https://arxiv.org/abs/2609.28434)

**<font color=#1a73e8>作者：</font>** Owen Pullen, Amir Jamaludin, Andrew Zisserman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adolescent Idiopathic Scoliosis is defined as a lateral curvature of the spine that develops during adolescence, without known cause. The condition can result in significant pain and disability, and often progresses rapidly during adolescence. The objective of this paper is to predict the progression of the condition in a temporal sequence from ages 9 to 24, as measured from a sequence of Dual X-ray Absorptiometry (DXA) scans. To this end, we train a transformer model that takes in the curve of the spine to predict curve progression. The model is trained using a large-scale synthetic dataset of spine curves and their time series, covering different curve types and different progression patterns. We show that the model is able to generalise from synthetic to real data by evaluating it on a dataset of real DXA scans covering multiple time points. We find that fine-tuning the model on real data gives a significant boost to performance. The model is able to accurately predict spine curve progression in both scoliosis and normal cases.

---


### 234. [MultiVENT-Raw: A Benchmark for Retrieval and Reasoning over Raw Videos](https://arxiv.org/abs/2609.28437)

**<font color=#1a73e8>作者：</font>** Reno Kriz, David Etter, Alexander Martin 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online information is increasingly consumed in video format. Much of this comes in the form of *raw video*: continuous footage taken on a cell phone, with a hand-held camera, or via CCTV, which is then directly uploaded to social media platforms and content sharing services. Whereas professional or even amateur-edited footage tends to feature scripted speech, chyrons, graphics, and metadata that help contextualize its subject matter, raw video typically contains none of these things, making it a much more challenging medium for information retrieval and machine understanding. To facilitate progress in this domain, we release MultiVENT-Raw, a multilingual collection of nearly 120,000 primarily raw videos (over 5,300 total hours), paired with 130 events and 222 event-centric queries, along with human-annotated video relevance judgments and human-extracted key facts for relevant videos. MultiVENT-Raw supports both a retrieval task---to identify videos in the collection relevant to a query event---and a generation task---to summarize event-related videos into a coherent report for a target user. We benchmark strong baselines on MultiVENT-Raw, showing both tasks to be challenging even for some of the latest multimodal models.

---


### 235. [Minimal-Norm Univariate Two-Layer ReLU Classification: Exact Solutions and Global Optimality with Skip Connections](https://arxiv.org/abs/2609.28438)

**<font color=#1a73e8>作者：</font>** Karolina Drabik, Ben Lewis, Antoni Puch 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study minimal-norm interpolation and $\ell_2$-regularized logistic-loss minimization for binary classification by univariate two-layer ReLU networks. We give complete geometric characterizations of the optimal classifiers in function space, resolving how the solutions depend on whether hidden-layer biases are included in the parameter norm. When biases are unpenalized, the minimal-norm interpolators are exactly the continuous piecewise-affine functions that hug every label switch and have kinks of the appropriate convexity. When biases are penalized, the minimizer is unique in function space, has exactly one kink in each intermediate same-label segment, and is therefore a sparsest positive-margin classifier. We further show that adding a free affine skip connection leaves these function-space solutions unchanged but fundamentally improves the parameter-space landscape: every KKT point of the constrained problem becomes globally optimal, whereas suboptimal KKT points can occur without the skip connection. We establish analogous global-optimality and geometric results for sufficiently weak $\ell_2$-regularization of the logistic loss. In the unpenalized-bias case, we identify an additional sparsity-like restriction, implying that most minimal-norm interpolators cannot arise as small-regularization limits of margin-normalized logistic-loss minimizers. Numerical experiments across varying dataset complexity and network width support the predicted landscape and sparsity phenomena.

---


### 236. [HaRP: High Dynamic Range Photosequencing through Dual Reversed Shutter Scanning](https://arxiv.org/abs/2609.28439)

**<font color=#1a73e8>作者：</font>** Xiang Ji, Guixu Lin, Jiancheng Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The adoption of CMOS sensors in mobile photography is frequently compromised by the rolling shutter (RS) effect, which introduces geometric distortions and motion artifacts. Particularly, recent rolling shutter with global reset (RSGR) mode, while mitigating some RS issues, also incurs major limitations, including reduced capture speed and compressed dynamic range. To address these problems, we propose a novel dual reversed scanning setup utilizing both RSGR and inverted RSGR views. This solution not only handles the inherent flaws of RSGR by synchronizing complementary exposures to balance the dynamic range across the frames but also introduces an effective method for HDR photosequencing under highly dynamic scenes. Our proposed network first accommodates row-wise complementarity and manages visual shifts by row-adaptive feature alignment. Subsequently, the hallucination module, built upon a correlation-guided mixattention block, integrates the mutually reinforced features to recover missing details. In addition, we construct a coaxial imaging system to collect a real-world dataset, enabling robust training and evaluation beyond numerical simulation. Experimental results demonstrate the twofold benefits of our solution in mitigating RSGR limitations and advancing HDR reconstruction techniques.

---


### 237. [Even Sharper Bounds for Transductive Learning and Its Applications](https://arxiv.org/abs/2609.28459)

**<font color=#1a73e8>作者：</font>** Yingzhen Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Sharper Transductive Local Complexity (STLC), a localized complexity method for transductive learning under uniform sampling without replacement. The construction starts from a Bernstein-type concentration inequality for the supremum of the test--train empirical process. Its proof uses the modified log-Sobolev inequality for the swap walk and a two-parameter entropy closure. A peeling argument with a surrogate localization functional then gives excess-risk bounds with the same fixed-point and confidence terms as the classical inductive local Rademacher-complexity bounds, without the additional logarithmic confidence factor in earlier transductive results. For realizable learning over a binary class of VC dimension $\dVC$, with training size $m$, test size $u$, and $u\ge m\ge\dVC$, STLC yields $\cO\{\dVC\log(me/\dVC)/m\}$. This matches the standard inductive rate and, when $m\ge9$, is within a logarithmic factor of the transductive minimax lower bound of order $\dVC/m$. For transductive kernel learning, STLC gives a spectrum-adaptive excess-risk bound without the multiplicative imbalance factors appearing in the earlier local-complexity bound.

---


### 238. [The Past Frames the Future: Memory for Autoregressive Video Generation](https://arxiv.org/abs/2609.28466)

**<font color=#1a73e8>作者：</font>** Harold Haodong Chen, Rongjin Guo, Disen Lan 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advances in generative models have improved video fidelity, enabling long-horizon generation, interactive world modeling, and evolving visual environments. Autoregressive (AR) video generation extends visual sequences through causal rollouts. However, a fundamental bottleneck emerges: as the generated sequence expands, practical models must operate under strictly bounded context windows, storage, and computational limits. Consequently, critical historical information, e.g., entity identities, dynamic states, and intervention-induced causal changes, often leaves the active context long before its relevance diminishes. Overcoming this limitation and maintaining temporal persistence constitutes a fundamental memory problem. We present a systematic and comprehensive review of memory mechanisms in AR video generation. We formulate memory operationally as persistent historical information maintained across outer AR steps, capable of influencing future generation even after the originating evidence is no longer locally accessible. Building upon this unified framework, we organize the literature through five complementary perspectives: (I) Forms, the representational carriers of history; (II) Functions, the specific semantic and physical information requiring preservation; (III) Operations, the lifecycle of writing, reading, updating, managing, and integrating memory; (IV) Learning, the optimization of memory behaviors under closed-loop rollouts; and (V) Evaluation, the paradigms for diagnosing genuine memory capabilities. We conclude by synthesizing open challenges, including composable and resource-aware memory architectures, trustworthy state updating, self-rollout learning, and standardized evaluation. By bridging representations, mechanisms, and learning paradigms, this paper establishes a structured foundation for developing reliable, memory-conditioned video generation systems.

---


### 239. [Contrastive Learning for Authorship Verification](https://arxiv.org/abs/2609.28471)

**<font color=#1a73e8>作者：</font>** Peter Kirby  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Our results show that contrastive learning outperforms a classification-based approach to authorship verification under the tested settings. We identify loss function, batch size, training duration, pre-trained model, input context length, and random text span data augmentation as important factors of model performance. Based on these considerations, we develop a ModernBERT Bi-Encoder model that achieves 98.4% accuracy on the PAN21 authorship verification task.

---


### 240. [On the Diffusibility of High-Dimensional Latents](https://arxiv.org/abs/2609.28473)

**<font color=#1a73e8>作者：</font>** Chao Feng, Zhiyang Xu, Bowei Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation Autoencoders (RAEs) enable diffusion models to operate in the feature spaces of pretrained visual encoders. However, many off-the-shelf encoders are not optimized for faithful reconstruction, discarding fine-grained visual details. As expected, finetuning these encoders for image reconstruction recovers such details. However, perhaps counterintuitively, this procedure reduces the effective dimensionality of the resulting representation, and the altered geometry has downstream effects on generation. Specifically, we show that using the standard velocity prediction in flow matching in this high-dimensional space requires the model to fit orthogonal noise directions outside the low-dimensional signal manifold, making optimization inefficient. This motivates using the clean data parameterization ($\boldsymbol{x}_{0}$-prediction) instead, which focuses learning on the underlying signal manifold. Across experiments with multiple strong-reconstruction encoders, we show that $\boldsymbol{x}_{0}$-prediction consistently improves text-to-image generation performance.

---


> [!TIP]
> 当前位于：**201-240**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-240**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
