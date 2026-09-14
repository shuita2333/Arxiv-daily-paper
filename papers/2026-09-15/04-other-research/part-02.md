# 📦 其他研究 | 2026年09月15日

> 本类共 **201** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-201](./part-05.md)

---

### 51. [Robust Prototypical Networks for Few-Shot Sensor Fault Diagnosis](https://arxiv.org/abs/2609.12287)

**<font color=#1a73e8>作者：</font>** Mohammed Ayalew Belay, Amirshayan Haghipour, Pierluigi Salvo Rossi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial fault diagnosis often operates with only a handful of labeled fault examples, making few-shot learning attractive for sensor monitoring. Standard prototypical networks are simple and effective; however, their class prototypes may become unstable in the very-low-shot regime because each decision relies on a small support set. We propose \emph{Multi-Episode Prototypical Networks} (MEPN), which aggregate prototypes from multiple disjoint support episodes and use their mean as the final class representative, reducing prototype variance without changing the encoder architecture. We evaluate MEPN on the DeFACTO sensor dataset using five-way fault classification with synthetic bias, drift, spike, and noise faults injected into real industrial measurements. Over 100 independent runs, MEPN reaches \textbf{\SensorOneShotGcpn\%} in the per-episode one-shot setting ($K\!=\!1$ shot, aggregated over $N_{\text{agg}}\!=\!10$ support episodes), substantially above single-episode baselines. Under an equal 10-sample support budget, MEPN and ProtoNet at $K\!=\!10$ are statistically indistinguishable, confirming prototype accumulation as the mechanism rather than superior fixed-budget learning.

---


### 52. ["People can change, and patterns can be broken": Contextualizing Tradeoffs in Automated Decision-Making Systems](https://arxiv.org/abs/2609.12288)

**<font color=#1a73e8>作者：</font>** Rabeya Bosri, Anna Harbluk Lorimer, Afrida Hossain 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Automated decision-making (ADM) systems are increasingly deployed in domains such as mortgage lending, prison sentencing, health insurance coverage, and hiring. Designing a responsible ADM system in such high-stakes domains requires ensuring privacy protection, fairness across demographic groups, and robustness against adversarial manipulation. However, prioritizing one of these objectives comes at the cost of another, forcing a choice as to which tradeoff to accept in a deployment. These tradeoffs explicitly or implicitly impact the life, safety, and fundamental rights of the people in a society, and thus, the perceptions and priorities of this population are needed before we can produce appropriate solutions. To this end, we conducted a quasi-experimental study (N = 777) in which participants evaluated four decision-making scenarios with controlled tradeoffs. Participants significantly preferred human decision-making (HDM) over ADM in three of four scenarios, emphasizing the value of human judgment, contextual understanding, and the ability to incorporate non-quantifiable factors. Furthermore, in terms of tradeoffs, our findings not only show that participants' preferences are highly context-dependent, but also that their perception of a specific objective, fairness, extends beyond formal definitions. Participants interpret fairness through multiple lenses, including privacy risks and susceptibility to manipulation, and view unfair or manipulated outcomes as failures of accuracy. Overall, our findings highlight the importance of context-aware and human-centered approaches when designing and governing ADM systems in high-stakes situations. Rather than purely technical objectives, it is essential to evaluate ADM systems based on how their tradeoffs align with specific expectations within a given domain, as well as with societal values and perceptions of harm and fairness.

---


### 53. [FRIST: FMRI Representation Informed Shared-space Training Improves EEG-only Individual-Finger BCI Decoding](https://arxiv.org/abs/2609.12298)

**<font color=#1a73e8>作者：</font>** Jintao Zhang, Yidan Ding, Joshua Kosnoff 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finger-level motor decoding is important for naturalistic brain-computer interface (BCI) control, yet individual-finger decoding from scalp electroencephalography (EEG) remains challenging because finger representations are spatially close in the sensorimotor cortex and blurred by volume conduction. Leveraging the high spatial resolution of functional MRI (fMRI), we introduce fMRI Representation-Informed Shared-Space Training (FRIST), a two-stage EEG decoding framework that first learns fMRI-informed spectral projections from simultaneous EEG-fMRI recordings and then uses fMRI-derived class geometry to guide residual refinement of EEG predictions. FRIST transfers information across recordings through shared finger labels without requiring paired trials and uses only EEG at inference. We evaluated 12 able-bodied participants during movement execution (ME) and motor imagery (MI) under two-class and three-class chronological session-held-out decoding simulating the online scenario. Using EEGNet as the EEG feature extractor, FRIST increased group average accuracy from 66.93% to 74.53% for two-class ME, from 44.83% to 56.58% for three-class ME, from 80.78% to 85.63% for two-class MI, and from 60.93% to 69.90% for three-class MI compared with the EEG-only EEGNet baseline. FRIST is also shown to improve EEG-only decoding when the target participant's own fMRI data were unavailable. FRIST also generalized across multiple EEG decoding backbones, reaching 87.40% in two-class MI and 72.54% in three-class MI with EEG Conformer as the EEG feature extractor. These findings indicate that fMRI provide useful spatial constraints for EEG representation learning. FRIST improves noninvasive EEG-based finger-level BCI decoding, offering a multimodal strategy for integrating the spatial specificity of fMRI with real-time applicability of EEG.

---


### 54. [Hybrid Physics-AI Framework of Body Center of Mass Dynamics from Wrist-Worn Sensors](https://arxiv.org/abs/2609.12304)

**<font color=#1a73e8>作者：</font>** Shuhao Que, Valentina Breschi, Ying Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wrist-worn IMU has been widely used for daily-life health monitoring. Yet, it does not fully represent whole-body dynamics, for which the body center of mass (COM) is considered the physiological reference standard. Therefore, this work proposes a simplified kinematic model (KM), which is designed to map the wrist IMU to the COM acceleration. It is built upon several reductive assumptions that enable the solvability of the dynamic equations based on wrist IMU measurements alone. This work further proposes three types of hybrid AI modeling methods, namely human kinematic model-based neural network (HKM-NN) models, to leverage the power of both grey-box and black-box modeling. The HKM-NN methods include serial learning (ser-) and two approaches of simultaneous learning (sim1- and sim2-). The proposed models are trained and tested using our dataset, which includes wrist IMU measurements and ground-truth COM measurements from 10 healthy volunteers during six gait activities and sit-to-stand (SS) transitional movement. The results demonstrate the feasibility of estimating COM acceleration from wrist IMU measurements. Our KM model yields satisfactory results, with an error ranging from 6.7% to 12.5% for gait activities and 5.6% for the SS. In comparison with the KM model, our HKM-NN models significantly enhance the performance, achieving 5.3% to 9.3% errors for gait activities, and the best error of 3.9% for the SS. In addition, the HKM-NN models demonstrate distinct robustness characteristics under noisy test conditions, with sim1-/sim2- generally maintaining greater robustness under Gaussian perturbations, while the KM model exhibits comparatively strong robustness under salt-and-pepper noise. These findings highlight the importance of combining biomechanical structure with data-driven learning for wearable sensing applications operating under imperfect and noisy measurement conditions.

---


### 55. [Self-Verifying Anomaly Detection using Explainable AI for Cybersecurity of DER Networks](https://arxiv.org/abs/2609.12305)

**<font color=#1a73e8>作者：</font>** Damilola Popoola, Souradeep Bhattacharya, Manimaran Govindarasu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid growth of Distributed Energy Resources (DERs) has significantly expanded the cyber attack surface of modern power grids. Furthermore, increasing sophistication in attack techniques demands anomaly detection systems (ADS) that are accurate, interpretable, and reliable to support DER cybersecurity. While ML-based ADS provide strong detection capabilities, their black-box nature reduces operator trust and limits Security Operation Center's (SOC) ability to effectively interpret alerts and respond, highlighting the need for explainable Artificial Intelligence (XAI) to ensure transparency and operational confidence. This paper presents an XAI-based anomaly detection framework tailored for DER networks (ExCYDER). The proposed framework uses a self-verifying mechanism that validates ADS alerts to ensure trustworthy decision-making. ExCYDER combines LightGBM with SHAP to check whether each model decision aligns with its feature-attribution evidence, allowing the system to confirm that its internal reasoning is consistent and reliable. Experiments on a realistic DNP3 dataset achieved over 98% detection accuracy, an average rule--SHAP consistency of 44.6%, a SHAP latency of 14.5 ms per alert, and a confidence deviation within 5%, demonstrating stable verification behavior with minimal computational overhead. The framework distinguished between coherent and inconsistent alerts without compromising detection accuracy, demonstrating that integrated verification within XAI-based ADS enhances interpretability, auditability, and operational robustness for DER-focused SOCs.

---


### 56. [Do Influence-Derived Data Perturbations Enable Machine Unlearning? A Controlled Study of Three Plausible Roles](https://arxiv.org/abs/2609.12313)

**<font color=#1a73e8>作者：</font>** Chenkai Wu, Chrispine Kambimbi, Qinyang Zeng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We evaluate Deep Perturbation Learning (DPL), which perturbs training images and labels along influence-derived directions, in three roles in which prior work has positioned it for machine unlearning: a direct deletion signal (the strongest claim), a utility-preserving regularizer, and a warm start for adversarial unlearning. Evidence for the weaker roles has been used to support the stronger one, so we test each role separately under a matched protocol with exact-seed retraining baselines. An audit of the public implementation identifies two correctness issues: image directions are computed on augmented, normalized tensors but applied to raw images, and the label perturbation falls below float32 resolution, leaving labels unchanged. After correcting the image-perturbation pipeline, DPL fails the direct-deletion criterion on CIFAR-10/ResNet-18 in all three paired seeds. Its utility effects are inconsistent in sign across seeds, and once direction-computation time is counted it underperforms simple warm-start baselines. A one-seed Tiny ImageNet check likewise does not favor DPL as a regularizer or warm start; preprocessing inconsistencies in the released code make the direct comparison there inconclusive. These results cover random instance deletion only and do not rule out influence-based methods in other deletion regimes. We release a role-matched evaluation protocol and an audit checklist for perturbation-based deletion claims.

---


### 57. [Function Name Is All You Need to Detect Blockchain Application Attacks](https://arxiv.org/abs/2609.12315)

**<font color=#1a73e8>作者：</font>** Rui Xi, Zehua Wang, Karthik Pattabiraman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchain application attacks, targeting business logic bugs in decentralized applications (dApps), have been an increasing concern to their developers and users, causing significant financial loss. Existing attack detectors either rely on handcrafted rules for detection, or need difficult-to-obtain smart contract source code to analyze attack transactions. This makes them brittle and inapplicable in practice. In this paper, we argue that function name sequences suffice to capture the high-level semantics of a transaction, and hence can be used to detect blockchain application attacks. Our empirical study on transactions from 424 real-world attack incidents shows that 98.46% of call traces can be resolved to function names, whereas only 74.78% invoke contracts with available source code. Based on this observation, we propose TxLucent (pronounced "translucent"), an automated framework to detect blockchain application attacks by extracting application semantics from transaction call traces. TxLucent maps call traces to function name sequences and uses a transformer to learn semantics from such sequences. Consequently, TxLucent can detect attacks without relying on hand-coded patterns or source code. Our results show that TxLucent achieves a 1.56% false negative rate on 424 known incidents with 14,611 attack transactions, and an estimated 0.0017% false positive rate for benign transactions from over 500 million transactions on the Ethereum blockchain. Finally, TxLucent takes an average of 24.90 milliseconds to analyze a transaction, thus supporting real-time attack detection on popular blockchains.

---


### 58. [LoRA-RC: Reservoir Computing with Low-Rank Adaptation](https://arxiv.org/abs/2609.12327)

**<font color=#1a73e8>作者：</font>** Wenbin Wan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reservoir computing (RC) trains only a linear readout over a fixed recurrent layer, making it fast and data-efficient for online prediction. However, a static reservoir degrades under system drift, readout-only adaptation is then insufficient, and unconstrained reservoir adaptation can destroy the echo-state and incremental stability properties that make RC reliable. This paper proposes LoRA-RC, which adapts the recurrent matrix through a low-rank correction driven by streaming prediction errors. The base reservoir and adaptation bases are fixed offline; a small core matrix is adapted online, projected onto a spectral-norm ball, and low-pass filtered at each step. The projection guarantees that every applied recurrent matrix remains within a certified contraction set, and an incremental input-to-state stability bound is established for the reservoir along each online adaptation path, with path-independent rate and gain. On a Lorenz system with an abrupt parameter drift, LoRA-RC cuts post-drift prediction error by 56% versus a fixed RC and 51% versus readout-only adaptation; ablations over 20 seeds show that removing the projection inflates this error by more than a factor of 40.

---


### 59. [Theoretical Guarantees for One-Shot Magnitude Pruning and Compute-Adaptive Early Exit](https://arxiv.org/abs/2609.12337)

**<font color=#1a73e8>作者：</font>** Erdem Koyuncu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study compute reduction in neural networks through a unified partial versus full computation view, captured by one-shot magnitude pruning in the static regime and early exit in the adaptive regime. In an asymptotic single-neuron model, we prove a concentration theorem for one-shot magnitude pruning with explicit rates. We also introduce the conditional perceptron for early exit and show that its excess generalization error decays as a power of the compute gap, with an exponent that grows to infinity as the alignment between partial and full computations tends to one. We then extend the analysis to deep networks, characterizing how pruning-induced distortions accumulate with depth and deriving a corresponding compute-accuracy tradeoff for frozen-backbone early exit under a neural network Gaussian process model. Numerical simulations corroborate the predicted scaling laws.

---


### 60. [UniMo: Unifying Human and Animal Motion Generation](https://arxiv.org/abs/2609.12342)

**<font color=#1a73e8>作者：</font>** Zeyu Zhang, Zhiyuan Zhang, Siheng Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The conditional generation of 3D motion has emerged as a key research topic due to its wide applicability across robotics, AR/VR, gaming, and content creation. However, extending recent advances in text-driven human motion generation to the animal domain remains challenging due to two core limitations. First, animals exhibit highly diverse skeletal topologies, unlike the standard human structure, making unified modeling across species difficult and leading to inefficient per-species models. Second, existing animal motion datasets suffer from limited scale and annotation quality, constraining model performance. To address these challenges, we propose UniMo, a unified point cloud-based motion generation framework that bypasses topological discrepancies by converting parametric skeletons into unparametric representations, further enhanced by dynamic sampling that allocates more points to active joints. Additionally, we present UniML3D, a large-scale motion-language dataset spanning both human and animal categories, containing 145,907 motion sequences and 433,388 captions-over 102x larger than existing animal datasets. Our method achieves state-of-the-art results on UniML3D and three public benchmarks including HumanML3D, KIT-ML, and AnimalML3D, demonstrating the feasibility and effectiveness of unified human-animal motion generation. Website: this https URL.

---


### 61. [VS-Splat: Voxel-Selective feed-forward Gaussian Splatting for end-to-end 3D object reconstruction from sparse-views](https://arxiv.org/abs/2609.12343)

**<font color=#1a73e8>作者：</font>** Yunsu Jeong, Hyuk Heo, Youngsang Kwak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward Gaussian splatting models have demonstrated remarkable effectiveness in reconstructing three-dimensional (3D) objects from a few two-dimensional (2D) images, even if they are unseen. As existing methods typically predict Gaussian primitives uniformly across the 3D space, most primitives are placed in non-object regions. This may hinder the representation of fine object details. This paper proposes a Voxel-Selective Gaussian Splatting model (VS-Splat), a new end-to-endfeed-forward Gaussian splatting framework that predicts many primitives only within selected voxels that are likely to belong to an object, without 3D structural supervision. To achieve this, we propose a new learnable voxel selection approach that identifies object-centric voxels only with 2D rendering supervision. Our sparse-view rendering experiments with three benchmark datasets show that proposed VS-Splat outperforms several state-of-the-art methods. We further demonstrate its effectiveness as a backbone for an existing densification method and show that anoptional extension improves its robustness to inaccurate camera pose estimates.

---


### 62. [EgoMaize: A First-Person Maize Instance Segmentation Benchmark under Severe Field Occlusion](https://arxiv.org/abs/2609.12350)

**<font color=#1a73e8>作者：</font>** Jiayi Li, Zihan Zhang, Erhankang Yan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Close-range first-person field images are important for mobile maize phenotyping because many plant-level traits depend on in-canopy structures that are difficult to ob serve from overhead views. However, post-seedling maize fields create a difficult in stance segmentation setting: stems, leaves, tassels, and neighboring plants are elon gated, repetitive, and strongly occluded. We introduce EgoMaize, a compact benchmark for first-person maize instance segmentation, where the task is to predict ownership consistent plant masks and plant-owned stem/tassel cues from close-range field images with severe same-class overlap. Existing visible-only labels can fragment one physi cal plant into disconnected supervision, while full-amodal labels may require unverifi able completion behind neighboring plants or field objects. EgoMaize therefore uses an evidence-closed annotation workflow for occluded maize regions and assigns unreli able maize regions to ignore rather than background. Baseline results show that pre trained query-based grouping, boundary refinement, and high-resolution crop refine ment help different aspects of the task, but no architecture solves the coupled chal lenges of fine structure recovery, same-class instance ownership, and occlusion reason ing; occlusion-level analysis further shows that performance decreases as plant visi bility becomes more limited. The dataset and code are publicly available at https: //github.com/JaaaaaaaD/EgoMaize.

---


### 63. [When Connected Does Not Mean Similar: Charting the Homophily Boundary of SNAP-KG for Streaming Entity Integration](https://arxiv.org/abs/2609.12356)

**<font color=#1a73e8>作者：</font>** Jui-Chien Lin, Oshani Seneviratne  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> SNAP-KG is a framework for assigning newly arriving entities to semantic communities in a growing knowledge graph (KG) using only their raw features, with no graph access and no retraining at inference time. It was evaluated on five multi-view benchmarks and a 2.4M-node OGB-WikiKG2 KG. In each of these datasets, at least one graph view is homophilous, meaning that connected nodes usually belong to the same class, and SNAP-KG performs well on all of them. This paper asks what happens outside that setting. We extend the evaluation to three heterophilous graphs (Texas, Wisconsin, Chameleon) and measure the edge homophily of every view. When no homophilous view is available, clustering quality drops sharply for both SNAP-KG and the transductive baselines used in its original evaluation. What decides this is the homophily of the relation, not the number of relations. Multi-view fusion still helps, but only when at least one homophilous relation provides a reliable foundation. The homophily assumption is therefore shared by the whole method family, not specific to SNAP-KG. We argue that heterophilous multi-view clustering is a separate research problem, outside the scope of this work. As future work, we outline how a heterophily-aware teacher could be distilled into SNAP-KG's projector to serve both homophilous and heterophilous KGs.

---


### 64. [LatentVerse: A Framework for Understanding Shared and Modality-Specific Information in Multimodal Latent Representations](https://arxiv.org/abs/2609.12364)

**<font color=#1a73e8>作者：</font>** Majd Alafrange, Samuel Friedman, John Kitonyo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent embeddings have become a central data abstraction in modern machine learning, especially in biomedicine, where foundation models are increasingly used to encode multimodal data like clinical text, medical images, omics, and physiological signals. However, the utility and value of these representations depends on understanding their quality, structure, and the information they encode. Existing analysis workflows for evaluating representations remain fragmented across custom scripts, isolated metrics, and most importantly lack multimodal analysis, limiting accessibility and reproducibility. We present LatentVerse, a representation analysis resource that combines a web-based visual analytics platform for accessible, report-driven exploration with a command-line interface for scalable technical workflows. LatentVerse unifies diagnostics for various representation quality metrics and extends to multimodal settings by decomposing embeddings into shared and modality-specific components. We evaluate LatentVerse through controlled unimodal and multimodal simulations, discovery-oriented analyses on real biomedical embeddings, and a user study across diverse use cases. By supporting thorough and interpretable evaluation of latent spaces, LatentVerse makes foundation model representations more understandable in biomedical and data science applications.

---


### 65. [Certified AI Triage of ICU Alarms](https://arxiv.org/abs/2609.12365)

**<font color=#1a73e8>作者：</font>** Mohammed Sameer Syed, Rozhin Yasaei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the VTaC benchmark 71% of ventricular-tachycardia alarms are false, but silencing a real one can delay recognition of a dangerous arrhythmia. We reframe alarm reduction as three-way triage (retain, suppress, or defer) and bound the decision this analysis treats as harmful: among suppressed alarms, the fraction that were genuine stays below a user-set budget with 95% confidence, under i.i.d. event sampling. Alarms sharing a waveform record are dependent, so the clustered analysis is a sensitivity check. On the official split a 5% budget certifies in all three seeds, suppressing 74.8% of false alarms while silencing 1.5% of genuine ones, at AUROC 0.953 and Challenge Score 83.33, numerically comparable to the strongest of the eleven published systems. Our central finding measures what multiplicity costs: the correction charges for every candidate, so a finer grid can certify strictly less. Under held-out calibration the 885-cell grid we declared certifies 1 of 15 fold-runs, while choosing the grid on a separate selection partition certifies 8. We project the calibration volume each budget needs, making an uncertifiable budget a design parameter. Finally, adding a learned reliability dimension to the policy grid did not sharpen the certified frontier.

---


### 66. [Context-Aware Causal Gaze Forecasting for Human-Vehicle Interaction During In-Cabin Tracking Dropouts](https://arxiv.org/abs/2609.12374)

**<font color=#1a73e8>作者：</font>** Shabnam Shabani, Ghazal Farhani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dashboard-mounted gaze trackers often lose sight of the driver's eyes during large head rotations, including shoulder checks, mirror glances, and intersection scanning. These maneuvers occur when information about the driver's visual attention is most useful. Offline gap-filling methods may reconstruct a missing interval using observations from both sides, but an online driver-monitoring system cannot rely on measurements that have not yet occurred. We therefore formulate causal gaze recovery: forecasting unavailable gaze at time t without target-tracker gaze at t or later. We introduce the Causal Context-Gated Forecaster (CCGF), which encodes a 60-frame pre-dropout history of gaze and head pose and combines it with DINOv3 scene features. A learned reliability gate controls the contribution of the history and scene representations as the dropout progresses. We evaluate two scene conditions: Live, in which the scene representation continues to update during tracker loss, and Frozen, in which the final pre-dropout representation is used throughout the missing interval. We evaluate CCGF on 2,047 eligible, naturally occurring GazeSense head\_lost events drawn from 10.5 h of naturalistic driving by ten drivers. Across all recordings, head\_lost accounts for 8.5 percent of GazeSense recording time. Synchronized gaze coordinates from a head-mounted Neon tracker provide supervision and evaluation targets but are never used as model inputs. Under leave-one-driver-out evaluation, CCGF achieves a mean per-driver median error of 175.7 px (10.5 deg) with Live scene updates, a 33 percent reduction relative to history-only causal forecasting. With Frozen scene input, the error increases to 210.8 px (12.9 deg), indicating that scene observations acquired during the dropout provide useful predictive information. We will release the dataset, evaluation protocol, and causal baselines.

---


### 67. [Representation-based Masked Diffusion Model](https://arxiv.org/abs/2609.12382)

**<font color=#1a73e8>作者：</font>** Yangrong Hu, Ding Huang, Xueyu Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked Diffusion Models (MDMs) have emerged as a compelling paradigm for language modeling, offering the capability for efficient parallel text generation. However, existing parallel sampling methods typically update multiple masked tokens independently and ignore the complex mutual dependencies among the masked tokens. This independent updating mechanism lacks global coordination and might lead to incoherent outputs. To address this limitation, we propose Representation-based Masked Diffusion Model (RMDM), a framework that leverages the text representation to explicitly encode global semantics and help to parallel update tokens more precisely. Specifically, we first encode text into a continuous semantic space using a pretrained encoder and learn an invertible transformation that normalizes the representation distribution to a Gaussian prior, facilitating efficient sampling during generation. Conditioned on this latent semantic representation, we train a masked diffusion model to learn the conditional text distribution, where the representation serves as global semantic guidance to coordinate parallel token updates and faithfully approximate the target distribution. Empirical results demonstrate that RMDM significantly improves generation quality, particularly in aggressive few-step sampling regimes.

---


### 68. [Split Conformal Prediction with Label-Shift-Adjusted Bayesian Scores](https://arxiv.org/abs/2609.12386)

**<font color=#1a73e8>作者：</font>** Hyeonsu Lee, Juyeon Kim, Erkhembayar Jadamba 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction provides distribution-free uncertainty quantification under exchangeability. However, this assumption is violated by label shift, where the marginal distribution of labels changes while the conditional distribution of inputs given labels remains stable. Under such shifts, standard conformal procedures no longer maintain their intended coverage behavior. Existing approaches address this via importance weighting. They pair the reweighting with residual-based nonconformity scores that ignore predictive uncertainty. The resulting intervals have uniform width. Bayesian conformal methods produce adaptive intervals by leveraging predictive distributions. They evaluate conformity under the source predictive, which is misaligned with the target domain under label shift. We propose the \emph{Label-Shift-Adjusted Bayesian Score} (LSA score), a nonconformity score derived from a posterior predictive tilting identity. This identity shows that the target predictive is an importance-weighted transformation of the source predictive. We use it to derive a direct correction to the Bayesian score. We evaluate the method on molecular property prediction under controlled label shift. The LSA score consistently yields shorter intervals than residual-based and source-based Bayesian scores. Coverage in the target domain remains comparable. Under stronger shift, all methods incur some coverage loss due to pseudo-label-based density-ratio estimation. The LSA score is defined for any source predictive with a tractable log-density. We instantiate it with Bayesian Ridge Regression, where the correction admits a closed form.

---


### 69. [Is Gaussian Splatting Becoming Neural Again? A Taxonomy and Controlled Study of Learned Parameterization](https://arxiv.org/abs/2609.12395)

**<font color=#1a73e8>作者：</font>** YuanHang Wang, Xin Cao, Yi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Three-dimensional Gaussian Splatting (3DGS) combines explicit primitives with efficient rasterization, yet recent systems increasingly use neural networks to generate or share Gaussian parameters. We characterize this trend along five axes: attribute decoding, spatial sharing, view-conditioned decoding, topology generation, and amortized inference. An analysis of 19 representative methods shows that these choices address different limitations and cannot be reduced to a binary neural label. We also isolate three forms of neural parameterization in a controlled mip-NeRF 360 study. Sharing appearance and opacity improves reconstruction quality, while decoding geometric structure offers no further gain. The evidence favors selective neuralization: shared functions help when they capture reusable correlations without sacrificing the local geometric freedom of explicit splats.

---


### 70. [Niching Agents in The Core](https://arxiv.org/abs/2609.12398)

**<font color=#1a73e8>作者：</font>** Gary B. Parker, Jim O'Connor, John Asaro  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Core is a unique competitive co-evolution algorithm that allows agents to evolve autonomous control without utilizing a traditional fitness function. The agents evolve via local interactions through tournament selection, crossover, and mutation, producing offspring by evolving better controllers. Previous works have shown The Core's ability to evolve agents capable of combat and navigation in the Xpilot video game. This research expands upon that premise by niching agents to specific subsets of the original environment The Core was tested in. Our results demonstrate the niched agents capacity for success over agents niched to the entire system and agents niched to different sub-environments.

---


### 71. [OneLA: Scaling Linear-Attention Decoding to Large Beams in Generative Recommendation](https://arxiv.org/abs/2609.12399)

**<font color=#1a73e8>作者：</font>** Xiangrui Yang, Cheng Peng, Yunfeng Zhao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative recommendation (GR) relies on large-beam decoding to generate hundreds of candidate items, creating a new scaling challenge for recurrent linear attention. Existing linear attention serving systems either materialize a full recurrent state for every beam or repeatedly replay shared history, incurring substantial memory and traffic overhead. To address this, we present OneLA, a linear-attention decoding framework that exploits the shared prompt and short divergent suffixes of GR workloads. Specifically, OneLA represents all beam states using a single shared prompt-derived state and compact, append-only records of their divergent transitions. Using this representation, OneLA computes only the state information required at each decoding step, without reconstructing a full recurrent state for every beam. Furthermore, OneLA uses a lightweight ancestry index to track the transition records that make up each beam's history, allowing beams to be updated without moving or copying existing records. A fused GPU kernel further reuses the shared state across beams. Our analysis shows that OneLA achieves 1.54-2.46x end-to-end decode speedups while substantially reducing recurrent-state memory use and data movement.

---


### 72. [Decentralized Evolution of Hexapod Gaits with Independent Leg Controllers](https://arxiv.org/abs/2609.12400)

**<font color=#1a73e8>作者：</font>** Gary B. Parker, John Asaro, Jim O'Connor  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents a novel approach to hexapod locomotion by evolving each leg's gait independently through a decentralized evolutionary algorithm. Using the Webots simulator and the Mantis hexapod robot, we optimize individual leg controllers without centralized coordination, allowing emergent behaviors to drive the development of efficient, coordinated locomotion. Our decentralized method is benchmarked against cooperative coevolution, demonstrating improved efficacy in generating stable and adaptive gaits while showing interesting emergent coordination. By enabling independent evolution of leg controllers, this method reduces the complexity of gait optimization and highlights the potential of decentralized strategies for scalable and adaptive robotic systems.

---


### 73. [GSO-Net: Visual State Machines for Hazardous Freight Transfer Compliance at Petrochemical Logistics Nodes](https://arxiv.org/abs/2609.12408)

**<font color=#1a73e8>作者：</font>** Yu Xie, Bangshu Xiong, Zhibo Rao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hazardous-freight operations at petrochemical logistics nodes are safety-critical for intelligent transportation systems, yet existing vision benchmarks rarely address procedural compliance under realistic deployment constraints. In large infrastructure networks, cameras often operate under sparse round-robin polling, so transfer status must be inferred from incomplete observations and localized evidence. We present GSO-Net, a large-scale benchmark for visual understanding of standard operating procedures (SOPs) in petrochemical unloading scenarios. To our knowledge, GSO-Net is the first public benchmark dataset dedicated to visual SOP understanding in petrochemical hazardous-freight transfer scenarios. It contains over 50,000 independently sampled frames from 64 real expressway petrochemical logistics nodes and adopts an SOP-derived hierarchy linking 9 macroscopic procedural steps with 15 microscopic operational states. Two tasks are defined: joint detection of microscopic states and macroscopic steps as the core benchmark, and frame-level step classification as a diagnostic reference. Experiments with lightweight, transformer-based, open-vocabulary, and holistic models reveal a clear gap between object perception and transfer-stage understanding. Current models remain weak on contact-level state grounding, transient step recognition, and stage consistency, especially under sparse polling, tiny critical targets, and long-tailed operational evidence. GSO-Net provides a practical benchmark for fine-grained state perception and vision-based safety monitoring in hazardous freight transportation. The dataset is publicly available at this https URL

---


### 74. [OphBiWSSD: Scaling Temporal Action Localization in Ophthalmic Surgeries with Bidirectional Weight-tied State Space Duality](https://arxiv.org/abs/2609.12409)

**<font color=#1a73e8>作者：</font>** Yang Liu, Qionghong Ma, Joongwon Chae 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-frequency surgical maneuvers in ophthalmology necessitate high-fidelity temporal modeling, yet characterizing long-range procedural dependencies remains computationally prohibitive for attention-based architectures. Existing models often require aggressive temporal downsampling, which compromises the detection of fine-grained action boundaries and instrument-tissue interactions. To address these scalability constraints, we present OphBiWSSD, a framework that reformulates surgical temporal action localization leveraging Bidirectional State Space Duality. By employing a weight-tied selective scan mechanism that incorporates both preceding and succeeding surgical contexts, our approach facilitates the global synthesis of non-causal temporal cues with linear complexity. This streamlined architecture is well-suited to capture the bidirectional dependencies present in ophthalmic workflows, effectively bridging the gap between local boundary precision and long-range procedural context without incurring the quadratic memory overhead of traditional Transformers. Extensive experiments on the OphNet benchmark demonstrate that OphBiWSSD achieves state-of-the-art temporal localization performance, with mean Average Precisions of 44.42% on phases and 43.08% on operations, surpassing the baselines by 6.80% and 6.66%, respectively. Empirical validation indicates that our approach ensures precise temporal localization and offers a computationally viable pathway for deploying surgical intelligence systems in clinical environments. The code is publicly available at this https URL.

---


### 75. [A Multimodal Explainable Deep Learning Framework for Alzheimer's Disease Diagnosis using 3D Magnetic Resonance Imaging and Clinical Data](https://arxiv.org/abs/2609.12410)

**<font color=#1a73e8>作者：</font>** Yusuf Brima, Marcellin Atemkeng, Lakshmana Rao Namamula 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dementia is a major and growing global health burden, with Alzheimer's disease (AD) accounting for most cases. Timely and accurate diagnosis is central to managing this burden and increasingly depends on integrating complementary clinical and imaging information. Multimodal deep learning can combine these modalities for AD diagnosis, but how its explanations behave across modalities, fusion strategies, and cohorts remains unclear. We developed an explainable multimodal framework pairing a 3D CNN encoder for T1-weighted MRI with a feedforward network for harmonized clinical and demographic data, comparing varied model setups on three-way and pairwise diagnostic tasks using 6,479 internal records from the ADNI and 1,703 independent records from the OASIS-3. On ADNI, the tabular-only model achieved the highest three-class AUC-ROC of 0.879 and best discriminated cognitively normal (CN) versus mild cognitive impairment (MCI; 0.903), while cross-attention performed best for MCI versus AD (0.861); CN versus AD was highly discriminative overall. On OASIS-3, the vision-only model performed best (three-class AUC-ROC 0.910); CN versus MCI remained difficult, and no fusion strategy consistently outperformed single modalities across tasks and cohorts. SHAP and Integrated Gradients identified the MMSE as the dominant tabular feature in both cohorts, with global feature rankings agreeing strongly in ADNI ($\rho=0.94$) and OASIS-3 ($\rho=0.96$); CAM-based explanations, however, changed with model configuration and cohort. These findings show that multimodal performance and explanations are task, modality, fusion, and cohort-dependent: a dominant cognitive signal persisted across cohorts, but feature contributions and CAM explanations did not, underscoring the need to evaluate explainability under cohort shift rather than as a stable, intrinsic property.

---


### 76. [DERA: Detached Edge-Residual Adaptation for Prohibited item Detection](https://arxiv.org/abs/2609.12411)

**<font color=#1a73e8>作者：</font>** Yonathan Michael, Mohamad Alansari, Mohammed Bennamoun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prohibited-item detection in X-ray imagery remains challenging due to object superposition, weak texture, and material clutter which obscure both semantic appearance and object boundaries. We propose \textbf{DERA}, a \textbf{D}etached \textbf{E}dge-\textbf{R}esidual \textbf{A}daptation framework for prohibited item detection under X-ray imagery. DERA combines hierarchical visual features with a parallel pixel-difference edge pyramid and learns an object-specific boundary prior from training-time contours of the instance masks. The detached prior gates edge-sensitive features, which are injected into the early visual stages through residual heads. This staged design preserves the foundation detector at the start of adaptation, isolates boundary supervision from semantic feature learning, and restricts the final adaptation stage to only \(14.7\)K trainable parameters. Evaluated on PIDray, CLCXray, and STCray, DERA improves the baseline by \textbf{3.1}, \textbf{1.6}, and \textbf{2.4} AP points, respectively.

---


### 77. [Why User Studies and Participant Experience Reporting Matter for VR Motion Privacy?](https://arxiv.org/abs/2609.12415)

**<font color=#1a73e8>作者：</font>** Azim Ibragimov, Eric D. Ragan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Public VR game leaderboards contain tracked motion recordings uploaded by hundreds of thousands of users. Once uploaded, these recordings are accessible to anyone and create privacy risks (i.e., identification and profiling). Prior work has proposed mechanisms that modify tracked movement to reduce these risks. Their utility is commonly evaluated through physical deviation, where smaller deviations indicate better utility, while user studies are less common. However, it remains unclear how well physical deviation explains users' acceptance of a mechanism compared to user studies. We examine this through a user study of three VR motion privacy mechanisms at five physical deviation levels. We find that user studies explain substantially more variation in mechanism acceptance than physical deviation, although physical deviation remains significant. We also find that prior VR experience and exposure to VR privacy mechanisms significantly affect acceptance. We recommend combining physical deviation with user studies and reporting participants' prior experience.

---


### 78. [Spectral Consistency-Guided Multiview Point Cloud Registration for Low-Overlap Scenes](https://arxiv.org/abs/2609.12417)

**<font color=#1a73e8>作者：</font>** Tianyu Li, Yanghong Lin, Shudong Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multiview point cloud registration is particularly challenging in low-overlap scenes, where reliable correspondences are limited and incorrect pairwise transformations can affect global pose estimation. In addition, registering all scan pairs is computationally expensive because many pairs provide weak geometric information. To address these problems, we propose GMPCR, a non-learning-based spectral consistency-guided framework for efficient and robust multiview point cloud registration. GMPCR builds a refined second-order compatibility structure from initial correspondences and uses its dominant spectral response to evaluate both correspondence reliability and scan-pair confidence. This allows unreliable correspondences to be filtered and informative scan pairs to be selected before relative transformation estimation, leading to a sparse pose graph and reduced pairwise registration cost. For each retained scan pair, maximal-clique-based hypothesis generation is used to estimate reliable relative transformations. The resulting pose graph is further refined by an adaptive history-aware synchronization scheme, in which the effect of residual history is adjusted according to changes in the global rotation residual. A recovery mechanism also allows down-weighted edges to regain confidence when their global consistency improves. Experiments on 3DMatch, 3DLoMatch, ScanNet, and ETH demonstrate the effectiveness of GMPCR. It achieves registration recalls of 97.2% and 89.6% on 3DMatch and 3DLoMatch, respectively, while maintaining competitive performance on ScanNet and ETH. The results show that GMPCR provides a favorable balance among registration accuracy, robustness to low overlap, and computational efficiency. The code is publicly available at this https URL.

---


### 79. [RiPPLE: Cross-Space Performance Prediction from Early Training for Neural Architecture Search](https://arxiv.org/abs/2609.12418)

**<font color=#1a73e8>作者：</font>** Yifan Yang, Zhaoyan Wang, Zheng Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural architecture search (NAS) evaluates candidate networks, but fully training enough architectures to rank an entire space is expensive. Zero-cost proxies score architectures at initialization, yet their ranking quality varies across search spaces. Learned predictors reduce evaluation cost but typically require fully trained labels or partial-training features for individual candidates. We introduce $\textbf{RiPPLE}$, $\underline{\textbf{R}}$anking v$\underline{\textbf{i}}$a $\underline{\textbf{P}}$refix-$\underline{\textbf{P}}$ropagated $\underline{\textbf{L}}$abel $\underline{\textbf{E}}$xtrapolation, which treats partial training as a source of labels for a small coverage set of anchors. RiPPLE trains these anchors to an early prefix, extrapolates their learning curves to surrogate labels, and propagates the labels over label-free architecture features. The early-training signal remains a label on the anchors rather than a per-candidate feature. Feature, readout, and encoding rules are selected without held-out accuracy and reused across search spaces. We evaluate the method on twelve benchmark cells from four search-space families and on the larger DARTS space. The results examine ranking quality, label efficiency, architecture selection, and the roles of readout, coverage, and propagation. RiPPLE provides a whole-space ranking from a fractional anchor-training budget, with comparisons interpreted under their respective evaluation and cost protocols.

---


### 80. [MInTRL: Off-policy Intervention can boost On-policy RL](https://arxiv.org/abs/2609.12419)

**<font color=#1a73e8>作者：</font>** Mingyu Chen, Yefan Tao, Gerald Friedland 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards is typically performed on-policy, keeping training data close to the current policy but limiting learning to trajectories that the policy can discover itself. Off-policy methods such as supervised fine-tuning, on the other hand, can leverage external knowledge beyond the base model's capabilities, but may suffer from large distribution shift. The key challenge is thus to expand exploration without sacrificing learnability. In this work, we introduce Minimal Intervention Reinforcement Learning (MInTRL), which expands the exploration frontier through sparse, local interventions in otherwise on-policy rollouts. During generation, a judge-intervention policy periodically reviews the current policy's output, replaces erroneous suffixes with short corrections, and immediately returns control to the policy. During training, MInTRL adopts a sequence-level advantage-regression objective that eliminates the need for importance sampling. We show that sparse, local interventions can substantially improve coverage beyond finite-budget on-policy sampling while preserving the overall on-policy nature of the resulting trajectories. Across math and code benchmarks, MInTRL consistently outperforms standard on-policy and off-policy baselines. Ablations show that MInTRL remains effective with self-intervention and across different judge policies, while performance peaks at moderate intervention intensity, highlighting the importance of intervening minimally. These results establish minimal intervention as an effective paradigm for enhancing on-policy RL.

---


### 81. [Hierarchical Belief Modeling for Zero-Shot Opponent Adaptation in Partially Observable Multi-Agent Navigation](https://arxiv.org/abs/2609.12422)

**<font color=#1a73e8>作者：</font>** Kowei Shih, Lu Cheng, Zeyu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Lux AI Season 3 requires agents to act under partial observability, randomized episode level dynamics, and a best of five match structure that rewards both tactical execution and fast adaptation. We present HORIZON, a hierarchical agent that combines symmetry aware spatial perception, dual memory belief tracking, relic centric graph attention, information gain driven exploration, and an opponent conditioned policy mixture. HORIZON separates short horizon control from cross match meta reasoning, while auxiliary belief and world model objectives stabilize learning. Trained with PPO in a large scale JAX simulator, the resulting agent explicitly infers hidden game parameters and opponent style. Experiments show consistent gains in match win rate, episode win rate, adaptation gain, and league rating over strong recurrent and feed forward baselines.

---


### 82. [IDORacle: Template-Guided SQL-Sink Mediation for Object-Level Authorization in Java Applications](https://arxiv.org/abs/2609.12426)

**<font color=#1a73e8>作者：</font>** Yuewantong Song, Guanhang Shi, Yin Cai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Insecure Direct Object Reference (IDOR), often modeled as Broken Object-Level Authorization (BOLA), remains prevalent in Java database applications because identity and authorization checks at the controller or service layer are disconnected from SQL execution based on resource identifiers. Existing work largely detects these vulnerabilities but offers limited low-intrusion runtime protection for legacy Java-SQL applications. We present IDORacle, a template-guided SQL-sink interception and rewriting framework for preventing horizontal privilege escalation at runtime. IDORacle propagates authenticated identity context across HTTP requests, asynchronous tasks, and data-access boundaries through a server-side trace identifier. At the MyBatis/JDBC boundary, it extracts SQL templates, computes dual fingerprints, and performs one-time template analysis to generate reusable mediation plans. During execution, it combines subject context, SQL ASTs, table metadata, and cached authorization proofs to permit, rewrite, or block operations. Its guard model supports direct ownership predicates, join-derived ownership, probes for group-owned resources, role-sensitive state transitions, and sensitive-column mediation. A Java-SQL benchmark grounded in real-world CVE reports shows that IDORacle prevents the tested horizontal authorization violations with a worst-case guard latency of 0.17 ms. Redundancy-aware optimization reduces average per-instance overhead by more than 90%, to 0.017 ms for hot SQL templates.

---


### 83. [An End-to-End Automated Pipeline for Controllable Crack Data Synthesis](https://arxiv.org/abs/2609.12431)

**<font color=#1a73e8>作者：</font>** Conghui Li, Muxin Pu, Chern Hong Lim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated crack inspection increasingly relies on deep learning, yet its reliability is limited by scarce and weakly controllable defect data. Existing generative augmentation methods often treat crack synthesis as a generic image-generation task, offering insufficient control over morphology, boundary fidelity, and scene context. This paper proposes an end-to-end automated pipeline for controllable crack data synthesis that formalizes crack geometry and inspection context into reusable computational constraints. First, procedurally sampled Bézier-curve skeletons are translated into realistic crack masks using a GAN, enabling scalable generation of diverse crack morphologies without manual mask design. Second, a dual-ControlNet diffusion framework disentangles appearance guidance from geometric guidance, with an edge-based branch enforcing strict boundary consistency. The framework supports both background-free synthesis and context-aware inpainting. Experiments on CRACK500 and CrackTree200 show consistent gains over existing augmentation baselines, demonstrating a scalable engineering informatics workflow for automated crack-inspection data generation.

---


### 84. [Observation-Anchored Selective Assimilation for Longitudinal Tumor-State Proxy Forecasting in Post-Treatment Glioma](https://arxiv.org/abs/2609.12435)

**<font color=#1a73e8>作者：</font>** Yeonjae Jung, Minwoo Shin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-treatment MRI in patients with glioma provides serial observations for updating patient-specific tumor-state proxy estimates, but variable appearances and trajectories complicate forecasting. We formulate forecasting as an observation-aware digital-twin update in which an intermediate observation anchors the patient-specific state. Among 203 patients and 594 follow-up time points, a predefined no-new-treatment criterion retained 120 of 236 candidate triplets, split into 81/24/15 training/validation/test triplets at the patient level. Each time point was represented by a continuous voxel-wise tumor-state proxy map in [0,1] derived from MRI lesion labels. A SegMamba-based single-step forecaster predicted update proposals from multimodal source-state tensors. Observation-Anchored Selective Assimilation (OASA) retained the observed intermediate proxy as the state anchor and selectively applied updates through a validation-selected tiered case-level rule and voxel-wise soft gate. We compared initial-scan forecasting, rollout without assimilation, latest-observation persistence, direct prediction, OASA, OASA + calibration, and morphological dilation. Checkpoints, OASA rules, and calibration thresholds were selected using validation data only. Across three seeds on 15 held-out test triplets, OASA maintained Dice at $\tau$ = 0.2 comparable to persistence (0.6071 $\pm$ 0.0025 vs. 0.6070) while yielding numerically higher Dice at $\tau$ = 0.5 (0.4269 $\pm$ 0.0079 vs. 0.3981), with a small RMSE increase. Calibration increased Dice at $\tau$ = 0.2 to 0.6178 $\pm$ 0.0025, increased false-positive (FP) support (11,836$\rightarrow$18,663), and reduced false-negative (FN) support (22,107$\rightarrow$17,536). This reflects near-threshold support calibration rather than improved biological predictive capability. Code is publicly available at this https URL.

---


### 85. [ForkSCOPE: Charting the Agentic Garden of Forking Paths](https://arxiv.org/abs/2609.12438)

**<font color=#1a73e8>作者：</font>** Arjun Balaji, Batuhan Duru Yeltekin, Tian Zheng  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Even with a fixed dataset and research question, data analysis involves many defensible decisions. Understanding how these choices influence the results is scientifically important but remains challenging. Crowdsourcing and agentic AI can generate hundreds of end-to-end analyses, but scaling generation alone can create a processing bottleneck and an analytic ``black hole.'' A common workaround is to impose a shared fixed decision taxonomy, which can limit insight and understate uncertainty. We present ForkSCOPE, a human-AI collaboration framework that induces structure bottom-up from the code corpus of end-to-end analyses, without a taxonomy fixed before or after generation, so the organization and evaluation of the garden can scale with the corpus. ForkSCOPE surfaces the charted garden of forking paths through a human-AI collaboration pipeline and an evidence-linked interactive viewer for steering and verification: it spotlights organically identified forks and structures and produces a derived taxonomy and decision map compatible with existing multiverse tools.

---


### 86. [3D Digital Twin Visualization of Multiclass GRF-Based Gait Disorder Classification](https://arxiv.org/abs/2609.12442)

**<font color=#1a73e8>作者：</font>** Nayoung Son, Minwoo Shin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated gait analysis requires accurate classification and interpretable outputs. We propose an integrated framework for classifying healthy gait and multiple musculoskeletal impairment groups using bilateral ground reaction force (GRF) and center-of-pressure (COP) signals. The signals were normalized over the stance phase and standardized using training-set statistics. The model achieved a validation accuracy of 99.00\% and a test accuracy of 90.07\% under a session-level split. Class-specific $\epsilon$-LRP identified positive and negative contributions across both sides, multiple signal components, and different stance phases. Separately, the processed GRF signals and model predictions were synchronized within a Blender-based 3D visualization, enabling sample-level inspection of gait trials and classification results. The proposed framework integrates classification, explainability, and 3D visualization to improve model transparency. The source code is available in the following repository: this https URL

---


### 87. [PDoS: A Profitable Denial-of-Service Attack against Proof-of-Work Blockchain Liveness](https://arxiv.org/abs/2609.12450)

**<font color=#1a73e8>作者：</font>** Junjie Hu, Tianzhu Han, Na Ruan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The security and liveness of Proof-of-Work (PoW) blockchains fundamentally depend on the economic rationality of miners. Existing incentive-driven denial-of-service attacks, such as BDoS, can deter rational miners from participating, but require the attacker to continuously absorb substantial economic losses and are therefore difficult to sustain in high-value networks. Meanwhile, prior infiltration-based withholding attacks are designed to extract revenue rather than to directly disrupt chain liveness.
We present PDoS, a hybrid attack that combines block header signal deterrence with parasitic revenue extraction. PDoS disrupts blockchain liveness while exploiting the victim pool's share-reward mechanism to subsidize the attack cost, thereby lowering the adversarial hash-power threshold required to induce rational miners to shut down. We further show a counterintuitive result: in high-fee or high-MEV environments, higher block value can make PoW systems less secure by increasing the attacker's parasitic revenue and pushing the attack across the break-even point into a self-sustaining, or even profitable, regime. To the best of our knowledge, PDoS is the first attack to demonstrate that disrupting PoW blockchain liveness can be economically self-sustaining and even profitable.

---


### 88. [From the Task Boundaries of Narrative Text to Structural Anchoring, Uncertainty Triggers, and Cross-Calibration](https://arxiv.org/abs/2609.12453)

**<font color=#1a73e8>作者：</font>** Bowen Deng, Jiaqi Zou, Kexin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Causal graphs represent structural relationships among variables, yet users must still interpret direction, mechanism, and adjustment conditions in relation to the task at hand. Prior work often compares explanation formats as fixed conditions and pays less attention to how users distribute reasoning across graphs, direct explanations, and stories. We developed CoNS-Explorer, which uses reviewed instructional DAGs/SCMs to maintain a shared causal-fact ledger and generate fact-matched direct explanations and contextualized stories. A controlled survey experiment ($N=240$) compared the two texts as complete presentation packages. In the primary GLMM, the Story condition had a positive but uncertain overall association with accuracy (OR $=1.55$, 95\% CI $[0.34,7.10]$, $p=.572$); a population-averaged GEE showed a significant positive effect (OR $=1.89$, 95\% CI $[1.02,3.48]$, $p=.042$). Task-type interactions localized the clearest advantage to total-effect adjustment. Story also significantly increased situational presence. In a separate system-task and interview study ($N=24$), participants freely used graphs, direct explanations, and stories across three causal models. They established structural anchors with graphs and numerical results, consulted text when direction was unclear, mechanisms were unfamiliar, or multiple paths competed, and checked their judgments against other representations or external evidence. Integrating the two studies, we develop a process framework of structural anchoring, uncertainty triggering, explanation routing, and cross-calibration, together with four testable design propositions for adaptive causal explanation.

---


### 89. [EvoRS: On-Policy Self-Evolution of Reward Systems for Open-Ended Reinforcement Learning](https://arxiv.org/abs/2609.12459)

**<font color=#1a73e8>作者：</font>** Weiyuan Li, Aili Chen, Xintao Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-ended reinforcement learning often relies on rubric-based rewards for tasks without directly verifiable answers. Yet the policy and reward system form a dynamic feedback loop: as the policy optimizes the current reward, an initially useful reward system may become unreliable due to reward hacking or reduced response discriminability. The reward system should therefore evolve rather than remain fixed during training. Existing dynamic-rubric methods adapt evaluation criteria, but reward failures can also arise from scoring mechanisms or signal composition. We introduce EvoRS, a self-evolving RL framework that evolves the reward system from on-policy experience, representing it as an executable Reward-DAG. Specifically, an agentic designer updates this system from on-policy rollouts and reward traces to maintain train-time reliability. Across writing and roleplay, EvoRS achieves the best quality under all three judges, outperforming the policy by \(2.107\) and \(4.767\) points, respectively, while reducing reward hacking and coverage failures and preserving reward informativeness. Ablations confirm that a comprehensive fixed reward system cannot remain reliable in open-ended tasks and must evolve throughout training.

---


### 90. [Not All Speech Is Intent: Adaptive Self-Correcting Inference Layer for Post-ASR False Wake-Up](https://arxiv.org/abs/2609.12469)

**<font color=#1a73e8>作者：</font>** Preeti Saraswat, Divya Neelagiri, Anil Yadav  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> False wake-up activations remain a persistent challenge in conversational AI. Speech phonetically similar to a device's wake word can produce a syntactically valid and semantically coherent ASR transcript that the assistant incorrectly executes. Most existing systems make a single intent decision in isolation, without a mechanism to learn from recurring errors over time or adapt to individual users through personalized learning. We introduce the Feedback-Driven Adaptive Self-Correcting Inference Layer (ASCIL), a complementary post-ASR correction framework that re-evaluates wake-up intent before response generation by fusing acoustic embeddings, linguistic cues, device context, and patterns from past misclassifications. ASCIL interprets implicit signals, including hesitation, disengagement, and silence, and explicit signals, including cancellation and repetition, as automatically inferred, noisy behavioral indicators of potential misclassification. These signals drive online pattern updates without manual annotation, whereas the intentional/unintentional reference labels used for offline evaluation are human-annotated. It generalizes from prior errors, applies corrective adjustments at inference time, and continuously updates in parallel with natural-language execution. Evaluated on a proprietary dataset of 3,667 interactions with human-annotated intentional/unintentional reference labels spanning 14 acoustic and contextual conditions, ASCIL achieves 54.27% relative error reduction on a session-disjoint subset constructed from baseline failures, and up to 24.39% relative error reduction at threshold 0.90 on the issue-tagged evaluation slice. These gains are achieved while improving intentional acceptance rates, with a median added latency below 60 ms in the reported benchmark.

---


### 91. [A Differentially Private Federated Proximal Optimization Framework for Customer Churn Prediction in Heterogeneous Federated Telecom Networks](https://arxiv.org/abs/2609.12470)

**<font color=#1a73e8>作者：</font>** Joydeb Kumar Sana, Subrata Chakraborty, M M Manjurul Islam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Customer churn is one of the major issues in the telecommunication industry. To predict customer churn, conventional centralized machine learning approaches have been widely used. This centralized approach requires customer data to be stored in a central repository, which raises privacy concerns and may violate data protection regulations. Federated learning addresses this problem by allowing multiple telecom operators to collaboratively train a global model without transferring their raw customer data. However, real-world customer data are often heterogeneous (non-IID), which may negatively affect the performance of standard federated learning. Trained models can also suffer from privacy attacks. To address those issues, we propose a Differentially Private (DP) based Federated Proximal optimization (FedProx) framework. All experiments were performed on two publicly available telecom churn datasets. We trained Federated Averaging (FedAvg), DP-FedAvg, FedProx, and the proposed DP-FedProx framework. For baseline comparison, we also used several centralized and local models. To evaluate the models, we employed seven widely used evaluation metrics. The experimental results show that the FedProx based models consistently outperform the FedAvg based models. Compared with the best centralized model, the proposed DP-FedProx framework achieves competitive prediction performance with only a small reduction in accuracy while providing privacy guarantees. To explain our model, we conducted SHAP analysis which shows that DP-FedProx method priorities revenue group features. These results indicate that the proposed DP-FedProx framework provides a practical balance between prediction performance and data privacy protection.

---


### 92. [Partition-Invariant Tuning for 3D Scene Understanding](https://arxiv.org/abs/2609.12473)

**<font color=#1a73e8>作者：</font>** Hongqiang Lin, Tianle Wang, Shuiwang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene-level point cloud understanding remains challenging due to diverse geometries and spatial layouts. While pre-trained 3D point cloud foundation models (PFMs) offer strong transferability, full fine-tuning (FFT) incurs substantial computational and storage costs. Parameter-efficient fine-tuning (PEFT) provides a promising alternative, but existing PEFT methods largely focus on object-level point clouds and overlook serialization-induced partition variations in large-scale scenes. To address this issue, we propose PointPiT, a partition-invariant tuning framework for scene-level point clouds. Specifically, a Scene-aware Structural Adapter (SSA) integrates local geometric patterns with global scene context to mitigate partition-induced representation shifts. Moreover, Gradient Subspace Optimization (GSO) selects informative and partition-stable update directions, suppressing partition-dependent variations during optimization. Extensive experiments across multiple scene-level benchmarks demonstrate that PointPiT achieves competitive or even superior performance to full fine-tuning with less than 1% of backbone's parameters, while achieving consistent state-of-the-art performance among representative PEFT methods.

---


### 93. [When Does AI Augment Work? A Workflow-Level Framework for Human-Agent Collaboration](https://arxiv.org/abs/2609.12482)

**<font color=#1a73e8>作者：</font>** CIVIC-AI Collaboration, Jiaying Wu, Caleb Ziems 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We aim to characterise the value of artificial intelligence in the workplace. Current studies largely measure this value in terms of the current automation capabilities and public adoption of AI. However, such metrics ignore the greater impacts of human--agent collaboration in transforming the nature of work. To account for this, we must expand the scope of our analysis beyond atomised tasks of today, and instead focus on how AI can augment entire workflows of the future. To ground this analysis, we establish a precise definition of AI augmentation comprising six conditions, spanning durable net value, meaningful human control, accountability and recovery, and long-term human development through learning, career pathways, and job purpose. We elaborate on these conditions and apply the framework in a case study of AI-mediated social surveys. We conclude by outlining how organisations, researchers, and government leaders can use this framework to make sense of the future of work.

---


### 94. [Access Control as Verified Parse Constraints](https://arxiv.org/abs/2609.12488)

**<font color=#1a73e8>作者：</font>** Saranachon Iammongkol, Zhiyi Huang, David Eyers  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Commercial security gateways repeatedly ship implementation bugs in the code path between the network and the policy decision: hand-written enforcement logic that diverges from the policy author's intent, and ad-hoc request parsers at the network boundary that introduce memory-safety flaws of their own. In both cases the bug is in the deployed enforcement code, not in the policy. Existing approaches either leave the enforcement runtime unverified or connect a formal model to a hand-written engine only by differential testing.
Our contribution is a class result: a forward-only, backtrack-free EverParse validator is a verified recognizer for a bounded, finite-state class, and access-control decision functions with fixed-offset fields and bounded disjunction belong to it, so one machine-checked proof transfers to every policy in the class rather than being re-established per policy. Concretely, we encode a bounded policy language's decision function into a fixed-size byte buffer and verify the enforcement code once---covering all byte values---with an SMT solver, proving the validator accepts if and only if the decision function accepts, for every policy, request, and session. Editing rule content over a fixed endpoint set then needs no new proof; adding endpoints reruns the toolchain; extending the language needs new proofs. We establish faithful enforcement of a policy, not that a policy is itself secure.
The verified gate is platform-independent, requiring only EverParse/Z3 and a C compiler, whose correctness we assume. We demonstrate a deployment on the seL4 microkernel, which ensures every request passes through the gate and that unverified components cannot corrupt the verified enforcement chain.

---


### 95. [PhysioAI: Clinical Knowledge-Guided Semantic Supervision for Skeleton-Based Physiotherapy Action Recognition](https://arxiv.org/abs/2609.12491)

**<font color=#1a73e8>作者：</font>** Jie Cao, Euijoon Ahn, Anwar Hassan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skeleton-based action recognition can support automated tracking of physiotherapy exercises, particularly in remote rehabilitation settings where continuous in-person supervision is impractical. However, most existing methods are developed for large-scale daily-action benchmarks rather than rehabilitation scenarios. Public rehabilitation exercise datasets are typically small, with only subtle kinematic differences between exercise classes. For participants with motor impairments, exercise execution may also deviate from standard movement patterns in amplitude, speed, and coordination, increasing intra-class variability and making reliable recognition more difficult for skeleton-based models. We propose PhysioAI, a clinical knowledge-guided semantic supervision framework that injects structured physiotherapy knowledge into skeleton representation learning. PhysioAI combines graph-based spatiotemporal modelling of human movement with training-time semantic anchors derived from a structured Clinical Knowledge Dictionary (CKD). The CKD descriptions are encoded using a frozen Contrastive Language-Image Pre-training (CLIP) model and projected into an anchor space, where they provide class-specific semantic targets for skeleton representation learning. The resulting CKD-derived anchors are used only during skeleton-model training; inference requires only skeleton inputs. Under subject-disjoint evaluation, PhysioAI achieves $99.03\pm1.34\%$ on KiMoRe Overall, $94.64\pm7.36\%$ on the Hard-67 stress test, and $87.44\pm7.69\%$ on UI-PRMD Overall. These results exceed the strongest comparator for each endpoint by $0.27$, $2.87$, and $1.33$ percentage points (pp), respectively. These findings demonstrate that structured clinical knowledge can serve as an effective source of training-time supervision for physiotherapy action recognition.

---


### 96. [RoES: Rotational Equivariant Selective-frequency Fusion for Multimodal Images](https://arxiv.org/abs/2609.12497)

**<font color=#1a73e8>作者：</font>** Jiabao Wang, Wenjian Liu, Yaoming Cai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared-visible image fusion facilitates robust multimodal perception by integrating complementary textural nuances from visible sensors with thermal signatures from infrared systems. Due to the task's inherently ill-posed nature, existing methods heavily rely on structural priors but typically enforce rotation equivariance uniformly across all features. Such a holistic approach overlooks a critical distinction where low-frequency shared structures strictly adhere to equivariant constraints while high-frequency modality-specific details require greater flexibility to preserve unique information. To bridge this gap, we propose RoES, a Rotational Equivariant Selective-frequency fusion network. Instead of employing static decomposition, we introduce a trainable rotation-enhanced updater/predictor module to dynamically decouple low- and high-frequency components. The resulting representations are then processed through a dual-branch fusion module tailored for spectral consistency. Specifically, a rotation-equivariant Mamba is employed to capture long-range structural dependencies in the low-frequency domain, while a polar spectral attention-based Dual-Fourier block refines high-frequency details under explicit low-frequency guidance. Extensive experiments demonstrate that RoES consistently achieves state-of-the-art performance in both fusion quality and downstream object detection, establishing a robust solution for multimodal fusion by reconciling frequency-selective features with equivariant constraints. The source code is available at this https URL.

---


### 97. [When2Talk: When Should a Proactive In-Car Agent Talk?](https://arxiv.org/abs/2609.12503)

**<font color=#1a73e8>作者：</font>** Kaiser Hamid, Peihang Li, Nade Liang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Proactive in-cabin agents can help passengers understand automated-vehicle (AV) behavior, but communicating every ride event may introduce unnecessary interruptions. We investigated how communication should adapt to event priority and passenger activity. In a mixed-methods within-subject study, 41 participants rode as passenger in a VR simulated fully-automated vehicle. We compared an event-triggered (ET) policy that communicated immediately at every event with a context-sensitive (CS) policy that selected \textit{Immediate}, \textit{Delayed}, or \textit{Silent} communications. CS increased communication appropriateness and substantially reduced perceived interruption. Perceived trust did not differ between policies, although baselines dispositional trust differentiated communication preferences. Findings highlight event consequence, passenger activity, continuing information value, and confirmation need as key considerations for selective in-cabin communication.

---


### 98. [LettuceVisSim: A Simulator That Generates Lettuce Image Time-series for Vision-Based Reinforcement Learning](https://arxiv.org/abs/2609.12505)

**<font color=#1a73e8>作者：</font>** Ziye Zhu, Bert van 't Ooster, Congcong Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-based reinforcement learning holds strong potential for decision-making in controlled environment agriculture (CEA). However, its development is hindered by the scarcity of labelled crop images. To address this gap, LettuceVisSim, a lettuce growth simulator that generates labelled time series of crop images, was developed and validated. The simulator contains a process-based model (PBM) for shoot dry weight dynamics, a canopy layout algorithm for deriving canopy layout representations from shoot dry weight, and a Unity rendering engine for image generation. Five findings support the simulator. First, the PBM reproduced shoot dry weight under dynamic plant-density management with $\mathrm{R}^{2}=0.84$. Second, a piecewise cubic regression mapped shoot dry weight to potential projected area with $\mathrm{R}^{2}=0.94$. Third, the canopy layout representation was validated using 12 experimental datasets each having different dynamic environmental and spacing conditions. It reproduced the ground coverage ratio dynamics observed in measured images, achieving $\mathrm{R}^{2}=0.84$ when driven by measured shoot dry weight and $\mathrm{R}^{2}=0.40$ (0.76 excluding one outlier) when driven by PBM-simulated values. Fourth, the Unity rendering engine converted canopy layout representations into RGB and segmentation images at less than 10~ms. Fifth, a demonstration showed that a lighting-control policy can be learned and applied by observing only crop images that were generated with LettuceVisSim, providing a proof of concept of vision-based reinforcement learning in CEA using LettuceVisSim.

---


### 99. [Aligned Radiometric RGB-Thermal Fusion for UAV Facade Anomaly Screening](https://arxiv.org/abs/2609.12521)

**<font color=#1a73e8>作者：</font>** Yuan Yang, Shulei Li, Haobo Liang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle facade inspection can combine red, green, and blue (RGB) imagery with thermal measurements to screen surface and subsurface anomalies. However, geometric discrepancies between the sensors and thermal image rendering can obscure spatial correspondence and weak temperature contrasts. This article presents a sensor-level pipeline comprising per-sensor correction, RGB-to-thermal registration, common-support cropping, and signed local contrast encoding of 16-bit radiometric measurements. The encoding preserves the distinction between locally hotter and colder regions and supplies the fourth input channel of a compact single-stream detector. We introduce M3T, a dataset of 674 paired RGB and radiometric thermal samples from five facade-inspection projects covering eight component and anomaly categories. The median residual registration error is 3.384 pixels, and a controlled-displacement analysis characterizes how the local contrast response changes under controlled displacement. Project-grouped four-fold evaluation yields mean average precision of 0.168 over intersection-over-union thresholds from 0.5 to 0.95, using 28.50 billion floating-point operations per image. A separate single-split ablation shows improved delamination detection over RGB-only and alternative thermal inputs, although aggregate accuracy does not improve over RGB alone. Evaluation on RGBT-Tiny shows mixed performance with rendered thermal imagery. These results characterize the category-specific benefits and limitations of aligned radiometric contrast for compact facade screening.

---


### 100. [Temporal Recurrence Favors Fewer Layers](https://arxiv.org/abs/2609.12531)

**<font color=#1a73e8>作者：</font>** Ivan Anokhin, Johan Obando-Ceron, Irina Rish 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In streaming tasks, recurrent models can carry latent computation across time, allowing each update to build on representations produced earlier. This raises a basic question: once temporal recurrence provides sequential computation across steps, how much depth is still needed within each step? Prior work has shown that recurrence can make shallow models competitive. We instead study this question as a compute-allocation problem, varying within-step depth, expert width, and the number of parallel experts per layer across several compute budgets. For each budget, we compare the best observed recurrent and non-recurrent allocations and the performance they achieve under approximately matched per-step computation. Across Sokoban and autoregressive FineWeb language modeling, we find that temporal recurrence shifts the best observed compute allocation toward substantially fewer layers, with comparable or better performance.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-201](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
