# 📦 其他研究 | 2026年09月21日

> 本类共 **247** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-247](./part-05.md)

---

### 151. [Scene-Conditioned Relation Routing for urban cellular activity forecasting](https://arxiv.org/abs/2609.20209)

**<font color=#1a73e8>作者：</font>** Qingzhong Li, Jingye Lin, Hui Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Urban cellular activity forecasting requires jointly modeling heterogeneous spatiotemporal signals, including SMS usage, mobile network traffic, and call activity. Existing methods often separate temporal modeling, spatial relation learning, and multi-signal prediction, relying on fixed graph structures or static multi-task learning schemes, which limits their adaptability to changing urban scenes. We propose SCRR-Net, a scene-conditioned spatial relation routing framework in which urban contextual information jointly controls spatial dependency selection and cross-task knowledge transfer. SCRR-Net includes a context encoder, a spatial graph expert routing module, a temporal Transformer encoder, and a task knowledge routing module. Experiments on the Milano and Trento datasets demonstrate that SCRR-Net consistently outperforms competing methods on SMS, network traffic, and call activity forecasting, while providing interpretable routing behaviors.

---


### 152. [Subdomain-aware representation compression for pretrained image embeddings](https://arxiv.org/abs/2609.20213)

**<font color=#1a73e8>作者：</font>** Poowanut Niamluang, Jittat Fakcharoenphol  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dimensionality reduction is a well-known technique for improving space efficiency, typically applied uniformly across an entire dataset. This paper investigates the possibilities of using dimensionality reduction techniques for subdomain representation compression. We explore standard techniques such as Principal Component Analysis (PCA) and Linear discriminant analysis (LDA) in image domains. The results not only demonstrate the expected improvements in space and computation complexity crucial for edge-device ML applications but also show improvements in accuracy over direct full-embedding procedure. One possible explanation is that dimensionality reduction effectively extracts subdomain features. We also performed experiments to demonstrate transfer learning capabilities using the compressed representations.

---


### 153. [Explaining spatial information flow in short-term traffic forecasting models using a gated graph attention network](https://arxiv.org/abs/2609.20217)

**<font color=#1a73e8>作者：</font>** Yue Li, Shujuan Chen, Ying Jin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Short-term traffic forecasting supports real-time monitoring and control of road networks, and graph attention networks (GAT) are the standard means of representing spatial dependence in these models. GAT layers are widely described as capturing the influence of neighbouring locations, but this is seldom verified, because the attention weights offered in support cannot be compared against any measured quantity. That leaves two questions open, how the model should be explained and which of its components are necessary. We address this by adding a gate to the GAT layer which learns, at every sensor and every time step, what share of a sensor's updated state is drawn from its neighbours rather than from itself. Regularising the gate withdraws neighbour information progressively and thereby provides a graded form of ablation. We apply the gated GAT to ST-MetaNet, whose encoder and decoder each place one GAT layer between two recurrent layers, and train it on one calendar year of records from 498 loop detectors on the strategic road network of England. The gate assigns a larger share of neighbour information to sensors carrying heavier traffic and follows the daily and weekly cycle of travel, consistent with adjacent locations being more strongly coupled when busy. Mild regularisation improves accuracy slightly, and accuracy declines at higher strengths as the penalty withdraws information the model needs. The encoder gate closes before the decoder gate, but direct ablation qualifies that ordering. Removing either GAT layer alone leaves accuracy at least as good as keeping both, whereas removing both degrades it substantially, so the two layers are largely redundant rather than either being indispensable. The gated GAT therefore yields a modest accuracy gain, an explanation of where and when spatial information flows, and evidence on which layers the architecture requires.

---


### 154. [A Two-Stage Multi-Scale Attention-Based Network for Weakly Supervised Cataract Fundus Image Enhancement](https://arxiv.org/abs/2609.20222)

**<font color=#1a73e8>作者：</font>** Xiaoyong Fang, Yue Wang, Xiangyu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cataract is a major cause of vision loss and hinders further diagnosis. However, cataract fundus image enhancement often grapples with challenges such as limited paired cataract retinal images and insufficient recovery of fine details in the retinal images. To mitigate these challenges, we in this paper propose a two-stage multi-scale attention-based network (TSMSA-Net) for weakly supervised cataract fundus image enhancement. Our TSMSA-Net leverages the domain transformation to synthesis paired real-like cataract images, solving the problem of difficult acquisition of paired images. To further extract detailed information from fundus images and reduce the generation of artifacts during the enhancement process, we propose a multi-scale attention-based stage to learn more useful features for cataract image enhancement. Experimental results on Kaggle and ODIR-5K demonstrate that our TSMSA-Net outperforms current state-of-the-art cataract fundus images enhancement even without paired images and exhibits certain generalization ability. Experimental results on Kaggle and ODIR-5K datasets indicate that our TSMSA-Net outperforms the current state-of-the-art methods for cataract fundus image enhancement, even in the absence of paired images. Additionally, it demonstrates a certain level of generalization capability. The enhancement also can improve the performance of vessel segmentation and classification in cataract images.

---


### 155. [Before the Warning Comes Too Late: Incremental Phone-Scam Detection from Speech](https://arxiv.org/abs/2609.20223)

**<font color=#1a73e8>作者：</font>** Khang Nhat Hoang Vo, Anh Trac Duc Dinh, Tai Tien Ta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study weakly supervised incremental telecom fraud detection from raw telephone audio, where training provides only conversation-level labels and predictions must be updated before a call ends. We introduce StreamFraudNet, which processes incoming audio through overlapping bounded-context windows using a frozen self-supervised speech encoder, recurrent temporal modeling, and learned aggregation of latent window scores. On a controlled English benchmark, StreamFraudNet achieves a ROC--AUC of \(0.9953\), significantly outperforming acoustic and mean-pooling baselines while remaining competitive with strong global temporal models. The model produces its first prediction after 10 seconds of audio, updates every 2 seconds, and operates faster than real time on the evaluated server hardware. Ablations identify recurrent temporal context as the principal contributor to performance. These results demonstrate that fraud risk can be scored incrementally from raw speech without transcripts or temporal annotations, while highlighting the need for latency-aware training to improve early prediction.

---


### 156. [The Public Discourse Corpus (PDC): A Speaker-Attributed Dataset for Valence and Epistemic Modality with Target Speaker Participation](https://arxiv.org/abs/2609.20232)

**<font color=#1a73e8>作者：</font>** Bo Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce the \textbf{Public Discourse Corpus (PDC)}, the first dataset of public-figure interview speech jointly annotated for affective valence and epistemic modality. The corpus contains 998 videos from 100 speakers across seven professional domains, yielding 186,642 sentences (3.1 million words) after sentence segmentation and filtering. To ensure that all retained videos contain analyzable speech from the intended speaker, we introduce \textbf{Target Speaker Participation (TSP)}---a five-category annotation taxonomy with documented inter-annotator reliability ($\kappa = 0.616$)---as a key methodological contribution that any corpus construction project can adopt. Target-speaker turns are separated from interviewer and third-party speech through an \textbf{audio-first diarization pipeline} combining local Whisper ASR with pyannote speaker separation, released as an open-source implementation. We release the annotated corpus, the annotation tools, the cross-provider validation sample, and the complete processing pipeline. The dataset is available at this https URL.

---


### 157. [SAGE-Yoga: Multi-Cue Learning for Yoga Pose Classification and Joint-Level Correction](https://arxiv.org/abs/2609.20245)

**<font color=#1a73e8>作者：</font>** Hung Le Chi, Khanh Minh Huynh, Long Nghia Tran Pham 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated yoga analysis requires both accurate pose classification and interpretable feedback on pose execution. However, existing methods often rely on a single visual prediction, struggle to distinguish visually similar poses, and treat pose classification and correction as separate tasks. To address these limitations, we propose SAGE-Yoga, a unified coarse-to-fine framework for yoga pose classification and joint-level correction from a single RGB image. Inspired by how yoga instructors assess posture using multiple complementary cues, SAGE-Yoga first employs a bagging-based ensemble of complementary visual backbones to generate a ranked set of candidate pose classes. Additionally, a margin-based gating mechanism preserves confident visual predictions while invoking geometric verification only for ambiguous cases. Moreover, once the final pose class is determined, SAGE-Yoga retrieves a medoid reference pose and compares the observed joint angles with class-specific distributions to identify misaligned joints. Finally, these deviations are translated into actionable corrective feedback. Empirically, experiments on the Yoga-82 dataset show that the visual ensemble achieves 89.0% Top-1 accuracy, while the complete framework improves performance to 90.7% Top-1 accuracy and 90.1% Macro-F1. These results demonstrate that combining complementary visual evidence with selective geometric verification improves fine-grained pose classification while enabling interpretable, joint-level correction.

---


### 158. [Distance to Class Prototypes: Active Learning for Object Detection](https://arxiv.org/abs/2609.20248)

**<font color=#1a73e8>作者：</font>** Licheng Zhang, Zheng Gong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying a deep object detector in a new setting is limited less by architecture than by the cost of annotating data from that setting. Active learning lowers the cost by choosing which images to label, and the choice is only as good as the signal used to score an unlabeled image. That signal is usually the class posterior, which is cheap but poorly calibrated, or the disagreement across several models or several stochastic passes, which is better but multiplies inference over a pool far larger than the labeled set. We propose a signal richer than the posterior yet still read from one forward pass of one network. A supervised contrastive term added to the training objective shapes a per-object embedding space in which distance encodes class membership, and an unlabeled detection is scored by how far it lies from the region occupied by its predicted category, weighted by its confidence. The criterion needs no ensemble, no auxiliary predictor and no repeated inference, and its entire cost is 2.89M parameters, an increase of 8.3% over a bare detector. On PASCAL VOC and MS-COCO it beats the posterior of the same detector in every round in which a selection is made, by up to 1.08% mAP50 against run to run deviations of 0.02% to 0.18%, and it stays competitive with ensemble and Monte Carlo dropout criteria costing three to fifty forward passes per unlabeled image. Experiments use the single-stage detector under which the compared criteria report their results, so that the selection decision is isolated from the strength of the detector.

---


### 159. [Accuracy Is Not Enough: A Cross-Architecture Audit of Demographic Bias in Deep Knowledge Tracing](https://arxiv.org/abs/2609.20249)

**<font color=#1a73e8>作者：</font>** Dang Quang Minh, Nguyen Dung Son, Nguyen Huu Loi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep knowledge tracing (DKT) models implicitly decide which students an adaptive system believes have mastered a skill, yet almost all evidence on their demographic fairness comes from Bayesian knowledge tracing; the deep models that power modern systems have received no comparable cross-architecture audit. We close this gap: four architectures (DKT, DKVMN, SAKT, AKT) trained under three regimes (standard, reweighting, adversarial) on two public datasets with demographic metadata, Eedi (15.9M interactions) and OULAD (167k after preprocessing), evaluated with ABROCA, student-level bootstrap confidence intervals, and permutation tests addressing recent critiques of fairness-metric instability. Three findings emerge. (i) Bias is real but context-dependent: every architecture shows a significant socioeconomic ABROCA on Eedi (0.018-0.023, $p<0.005$), with per-group AUC lower for economically disadvantaged students, while gender bias is significant on OULAD for three of four architectures after multiplicity correction yet negligible on Eedi. (ii) The most accurate architecture is the most biased: AKT gains about 4 AUC points from item-level Rasch embeddings and shows the largest socioeconomic ABROCA, exceeding every other architecture under a paired bootstrap ($p\leq0.002$); ablating only the Rasch embeddings removes the accuracy gain and the excess bias together. (iii) Standard mitigation is unreliable: reweighting and adversarial debiasing leave ABROCA essentially unchanged in every configuration that preserves accuracy, even though the adversary is pinned at chance at full reversal strength and a weak-strength positive control rules out a dead probe.

---


### 160. [When AI Agents Commit: Cognitive Serializability Across Data, Evidence, Policy, and Authority](https://arxiv.org/abs/2609.20261)

**<font color=#1a73e8>作者：</font>** Jun He, Deying Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents derive concrete mutations from database reads, retrieved evidence, policy, beliefs, and delegated authority. Those inputs may change while reasoning is in progress. Database isolation orders the submitted transaction; agentic transaction processing determines whether a proposal satisfies an executable contract. Neither guarantee establishes a common valid point for the mutation and its derivation inputs unless the contract represents the relevant predicates. Typed dependency tokens distinguish content integrity from applicability, and trusted mediation captures the values exposed to reasoning. Under strict Cognitive Serializability, committed effects admit a serial order and a logical event at which every value exposed to derivation is unchanged. The fences last until the runtime event that realizes the sealed durability domain. The weaker Effect-Compatible Cognitive Admission recertifies an effect against a simultaneously held current dependency vector and current policy without claiming to serialize the original stochastic derivation. TCT combines immutable versioned executable definitions, registry-derived authority plans, sealed envelopes, guard-first commit transactions, post-seal envelope- and witness-bound grants, co-committed receipts, idempotent grant finalization, and receipt-driven epistemic reconciliation. Complete registered footprints and a single growing phase induce an acyclic lock-point order over local guards and incompatible external reservations. The corresponding results give serializability conditions and an observational-equivalence boundary for zero-error soundness and positive progress. A falsification suite tests the implementation obligations: the prototype prevented all injected anomalies and added 3.22 ms mean commit overhead.

---


### 161. [Generative Verification: Rethinking the Uncertainty Signal for Active Learning of Object Detection](https://arxiv.org/abs/2609.20262)

**<font color=#1a73e8>作者：</font>** Licheng Zhang, Zheng Gong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Nearly every acquisition function for active object detection shares one arrangement, in that the model being improved is also the model being interrogated. We depart from it. In generative verification an independent generative model re-derives the label of a detection from the pixels inside its predicted box, and the disagreement between the two becomes the acquisition signal. Two properties follow from the arrangement itself rather than from any tuning. A displaced box, a box on background and a correct box carrying the wrong label all yield a crop that fails verification, so the failure modes arrive already combined in one scalar and the hand-weighted classification and localization terms of existing criteria are no longer needed. And because the verifier never observes the detector confidence, confidently wrong detections score highest, although a self-derived signal reads them as uninteresting and they are the costliest to leave unlabeled. We build the verifier as a conditional diffusion model whose diffusion target is a label representation rather than an image. Its reverse process is stochastic, so repeated generations return a distribution whose concentration reports how firmly the evidence determines the label, where a classifier returns a single point estimate. On PASCAL VOC and MS-COCO the signal outperforms output-uncertainty, feature-geometry, perturbation and ensemble criteria, gaining about one mAP50 point per round on MS-COCO, with its largest margins in the early rounds where confident detector errors are most common.

---


### 162. [AI or Real: Detecting Partially Altered Videos Under Resource-Constrained Environments](https://arxiv.org/abs/2609.20263)

**<font color=#1a73e8>作者：</font>** Tamoghna Chakraborty, Md Nurul Absur, Sourya Saha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The proliferation of generative video models has shifted the practical detection threat from fully fabricated clips to partially manipulated footages. Although modern detectors achieve strong accuracy using foundation backbones of 400M+ parameters, their resource footprint precludes edge deployment. In this paper, we present a lightweight full-frame detector for partially manipulated AI-generated video, designed for deployment on edge hardware without face-detection preprocessing. The system distills a DINOv2-Base teacher into a frozen MobileNetV3-Small student through a pipeline that combines temperature-annealed soft-label transfer, attention-diversity regularization, frame-level supervision, and a residual feature adapter that conditions ImageNet features for artifact detection. We additionally target two failure modes specific to the partial-manipulation regime: false positives on legitimate scene cuts, addressed through within-video temporal hard negatives; and threshold-level miscalibration on the dominant pure-real class, addressed through calibration-aware sampling. Evaluation on a 55,393-sample spliced test set across fake-frame ratios from 6.2% to 31.2% demonstrates the student model closing 58% of the gap to the DINOv2-Base teacher (AUC 0.766) while running at 3.65 ms per 16-frame clip on RTX A4000 with a 150.4 MB checkpoint compatible with edge-device memory and latency budgets.

---


### 163. [CleanVideo: Adaptive Concept Erasure for Text-to-Video Diffusion Models](https://arxiv.org/abs/2609.20267)

**<font color=#1a73e8>作者：</font>** Junchi Liao, Hongji Li, Wenrui Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept erasure aims to selectively eliminate undesired visual semantics from pre-trained generative models without compromising their general utility. Extending concept erasure from images to video is nontrivial. Target concepts emerge gradually and vary across frames and denoising steps. As a result, fixed interventions may miss the target or introduce blurring, jitter, and content distortion. We propose CleanVideo, a selective erasure framework that performs low-dimensional subspace intervention controlled by a tri-modal gating mechanism. By jointly processing spatiotemporal visual features, timestep signals, and textual semantics, CleanVideo determines where, when, and whether to intervene, steering erased content toward natural surrogate concepts when such surrogates can be clearly defined while preserving non-target content. Experiments on three video diffusion models show that CleanVideo effectively erases target concepts while maintaining visual fidelity and temporal coherence, outperforming existing baselines under frame-level and video-level evaluations and under concept-recovery attacks when the protected pipeline remains intact.

---


### 164. [Improving Online Reinforcement Learning via Bidirectional Behavior Prior Distillation](https://arxiv.org/abs/2609.20268)

**<font color=#1a73e8>作者：</font>** Gong Gao, Xiao Lai, Jiaji Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online reinforcement learning (RL) algorithms frequently exhibit poor sample efficiency and unstable learning dynamics, stemming from systematic critic estimation errors that are exacerbated by greedy policy updates. Existing behavior-prior reinforcement learning methods attempt to alleviate this issue by relying on offline pre-training to learn behavior models from fixed datasets and using policy priors to constrain online policy updates. However, the limited quality of offline datasets often hinders the ability to provide high-value policies that can effectively guide policy updates. The absence of expert trajectories significantly impairs online policy learning, leading to low sample efficiency and suboptimal performance. To address these challenges, we depart from conventional behavior prior approaches and propose a Bidirectional Behavior Prior Distillation (B2PD) algorithm. B2PD leverages action-value priors to guide a conditional variational autoencoder (CVAE) in generating a high-value behavior support set. The resulting expert behavior priors are further distilled into the agent, effectively reducing inefficient exploration and enabling stable policy optimization, while establishing a bidirectional knowledge flow mechanism. Empirical evaluations on both state- and pixel-based tasks verify that B2PD substantially improves sample efficiency while maintaining stable policy optimization. More broadly, this work shows that enforcing high-quality behavioral support during online learning effectively mitigates critic-induced error amplification, enabling structured behavior priors to guide policy updates in a principled and sample-efficient manner.

---


### 165. [AI-Driven Real-Time Relay Optimisation in Smart Urban NR-V2X Networks via Learning-to-Optimise Graph Neural Networks](https://arxiv.org/abs/2609.20271)

**<font color=#1a73e8>作者：</font>** Giambattista Amati, Federica Mangiatordi, Emiliano Pallotti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable and low-latency communication is a fundamental requirement for smart city services and Industry 4.0 applications enabled by NR-V2X networks. However, limited Road-Side Unit (RSU) deployment and complex urban propagation conditions often prevent Connected and Automated Vehicles (CAVs) from maintaining stable connectivity. This paper proposes an AI-driven Learning-to-Optimise (L2O) framework based on Graph Neural Networks (GNNs) for real-time multi-hop relay selection in NR-V2X systems. The vehicular network is modelled as a graph, where nodes represent CAVs and RSUs, and edges encode radio-link characteristics. An offline Mixed-Integer Linear Programming (MILP) formulation provides optimal relay decisions used as supervision for training an edge-aware Graph Isomorphism Network with Edge Features (GINE). Extensive experiments on realistic urban datasets demonstrate that the proposed approach achieves near-optimal connectivity performance, recovering up to 11.3% connectivity gain, while reducing execution time by orders of magnitude (up to 100 x speed-up) compared to MILP. The framework enables scalable and real-time network control, making it suitable for smart city and Industry 4.0 deployments.

---


### 166. [A Hybrid Gaze-Motor Imagery BCI Framework for Effective Decision Communication](https://arxiv.org/abs/2609.20273)

**<font color=#1a73e8>作者：</font>** Gowtham Reddy N, KongFatt Wong-Lin, Yogesh Kumar Meena  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Non-invasive brain-computer interfaces (BCIs) and eye-tracking technologies offer promising communication pathways; however, motor imagery (MI)-based BCIs often suffer from low discriminability and high inter-subject variability. To mitigate these issues, this study investigates the impact of visual fixation on neural response stability in both standalone MI and hybrid MI-eye tracking systems. We then propose a novel asynchronous hybrid paradigm that streamlines user intent by utilising eye-tracking for direct selection, followed by MI-based confirmation, significantly reducing the operational steps required by conventional systems. The paradigm was evaluated with 15 healthy participants using a 16-channel EEG system. Results show that MI-related information is predominantly localised within motor cortex regions, with limited-channel configurations (SVM: 0.58) achieving performance comparable to full-montage setups (SVM: 0.54). The hybrid MI paradigm further outperforms conventional MI, achieving up to 100% accuracy with greater robustness across all channel configurations. Our findings indicate that visual fixation enhances neural response stability, while integrating eye-tracking with MI enables the development of reliable, scalable multi-command BCI systems suitable for real-world applications.

---


### 167. [A Multi-Objective Optimisation Framework for Corticomuscular EEG-EMG Pair Selection in Hybrid BCI](https://arxiv.org/abs/2609.20275)

**<font color=#1a73e8>作者：</font>** Dekka Muni Kumar, Yogesh Kumar Meena  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Hybrid brain-computer interface (BCI) systems that integrate electroencephalography (EEG) and electromyography (EMG) signals have shown significant potential in improving the reliability of motor imagery (MI) classification, particularly in neuro-rehabilitation applications. However, identifying informative EEG-EMG channel pairs that effectively capture corticomuscular interactions remains a challenging problem, as existing approaches typically rely on manually predefined channel combinations that may not generalise across subjects. In this work, a data-driven EEG-EMG pair selection framework is proposed, in which channel pair selection is formulated as a constrained bi-objective optimisation problem. The proposed method jointly maximises the spatial relevance of EEG channels with respect to motor cortex regions and the corticomuscular coupling strength between EEG and EMG signals, and is solved using the NSGA-II to automatically identify an optimal subset of pairs. To extract discriminative features, the correlation between band-power time features capturing EEG-EMG interaction is combined with ERD-based EEG features, and a sliding-window-based temporal analysis is employed to account for the dynamic nature of MI signals. The proposed framework is evaluated on MI data from eight stroke patients and achieves an average classification accuracy of 89.6%, demonstrating its effectiveness in capturing physiologically meaningful corticomuscular interactions and improving classification performance.

---


### 168. [JEPA-WAM: Connecting Generated Visual Instructions to World Action Models through JEPA Latent Representations](https://arxiv.org/abs/2609.20277)

**<font color=#1a73e8>作者：</font>** Tianbin Liu, Jian Zhu, Taiyi Su 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) have demonstrated strong robotic manipulation capabilities by augmenting pretrained video generative models with action experts. However, current WAMs still show limited instruction-following ability when conditioned solely on text instructions. We argue that this limitation stems in part from a structural imbalance in robot-learning data: rich visual-action trajectories are often paired with sparse and repetitive language annotations, allowing policies to identify tasks from visual context and motion regularities rather than grounding the instruction itself. To address this limitation, we introduce JEPA-WAM, which augments each text instruction with a bank of stochastically generated visual instructions, providing diverse visual cues for instruction following. Specifically, JEPA-WAM uses an off-the-shelf text-to-image generator to sample multiple task-completion images conditioned on the text instruction, without training the generator. Although these generated images may differ from the current visual scene in appearance and layout, they remain semantically aligned with the instruction and serve as visual goal references. To focus on task-level semantics beyond appearance, we encode these references with a frozen V-JEPA 2.1 encoder. The resulting dense goal representations are compressed into compact goal tokens that condition both the video and action experts through cross-attention. We further construct a real-robot instruction-following benchmark covering in-distribution, out-of-distribution scene, and out-of-distribution instruction settings. On this benchmark, JEPA-WAM achieves success rates of 87.3%, 74.5%, and 80.9% in these three settings, outperforming {\pi}0 and Fast-WAM by at least 10.0, 27.3, and 14.5 percentage points, respectively.

---


### 169. [Labeled Incidence Structures for Native Transformer Modeling of Text, Knowledge Graphs, and Hypergraphs](https://arxiv.org/abs/2609.20278)

**<font color=#1a73e8>作者：</font>** Mahesh Godavarti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text, knowledge graphs, and hypergraphs all have elements that play distinct roles within relation instances, structure that is lost when data is flattened into token sequences. We introduce labeled incidence structures (LIS), a uniform representation that encodes each endpoint as $(x_d, s, e)$: content $x_d$, a role or slot $s$, and the relation instance $e$ in which that role appears. Because every data type maps to the same $(x_d, s, e)$ representation without flattening, a single standard transformer can process them all natively, structural differences are carried entirely by the operators, not the architecture.
LIS assigns a structural address to each endpoint by composing a slot operator and an instance operator, $A(s,e) = R_s R_e$. We characterize when this factorization gives every token a unique, path-independent address. When it does, the natural operator comparing endpoint $j$ to endpoint $i$ is the relative transport $P_{j\to i} = A_i^{-1} A_j$, which gives attention a role- and relation-aware inductive bias without imposing an arbitrary sequence order.
Additive encodings of the form "position term plus relation term" can miss information that depends jointly on $s$ and $e$. We prove this in a controlled example family: when the journey operator is approximated by the sum of a position-only term and a relation-only term, the approximation cannot capture how position and relation combine, only their separate effects.
We also analyze persistent knowledge repositories. Identifiers tied to storage locations make models sensitive to storage order, while freely learned identifiers can become harder to control as the repository size $M$ grows relative to the sample size $n$. Computing relation-instance operators from content avoids this storage-order issue and yields a capacity bound independent of $M$, under fixed architectural and Lipschitz assumptions.

---


### 170. [Queries Knew More Than We Thought: Uncovering Latent Knowledge in Segmentation Models](https://arxiv.org/abs/2609.20283)

**<font color=#1a73e8>作者：</font>** Ignacio M. De la Jara, Cristian Rodriguez-Opazo, Damith Ranasinghe  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern segmenters often fail after the expensive computation has already been done: a useful mask is present among the model's query-conditioned candidates, but the deployed selection rule does not expose it. We study this output-selection bottleneck in frozen DETR-family models. A ground-truth-only oracle first shows substantial hidden headroom in already-computed mask proposals. This raises a simple question: How can we better use the masks a segmenter has already computed but does not expose? We then ask whether that headroom can be recovered without adding queries, generating new masks, rerunning the backbone, or updating weights. HYDRA is a small selector trained only on cached frozen outputs. At inference time, it scores the cached candidates against an explicit keep-baseline option and acts only when a held-out calibrated margin indicates the selected candidate is sufficiently better. Trained on training-split caches and calibrated on held-out data, HYDRA improves Mask2Former, MaskDINO, and OneFormer by up to +7.41 dataset mIoU points on ADE20k and COCO, and improves SAM 3 by +9.4 class-macro prompt-IoU points on average across eight domains while preserving useful predictions through calibration. Paired LoRA controls show that lightweight weight adaptation does not remove the bottleneck: exposed predictions are often flat or worse, while routing over the adapted candidates still recovers accuracy. Finally, we connect the effect to query specialization under bipartite matching and verify it in a controlled TinyDETR study. These results show that frozen segmenters should be evaluated not only by the masks they expose, but also by the useful candidates they suppress.

---


### 171. [TinyCNN: A 193K-Parameter Network for On-Device Plant Disease Detection, with a Cross-Dataset Robustness Diagnosis](https://arxiv.org/abs/2609.20290)

**<font color=#1a73e8>作者：</font>** Ngoc-Bao Ho-Lam, Thai-Anh Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting crop disease early is central to sustainable agriculture and food security under United Nations Sustainable Development Goal 2 (Zero Hunger), and is especially urgent in resource-constrained regions where expert diagnosis is scarce but low-cost mobile devices are widespread. This paper presents TinyCNN, a lightweight convolutional neural network for on-device plant disease classification. TinyCNN uses depthwise separable convolution blocks and contains only 193,190 trainable parameters with 110.05M MACs for a 224x224 input image. On the 38-class PlantVillage benchmark, TinyCNN achieves 98.88% test accuracy and 98.03% macro-F1 while being approximately 58x smaller than ResNet18 and 11.8x smaller than a MobileNetV2 teacher, directly reducing the energy, memory, and cost footprint of inference in line with Green AI principles. The paper further analyzes vanilla knowledge distillation as a sustainable model-compression strategy; an ablation over alpha in {0.3, 0.5, 0.7} and T in {2, 4} selects alpha=0.3, T=4, producing a distilled TinyCNN with 98.81% test accuracy. Finally, cross-dataset evaluation from PlantVillage to PlantDoc reveals a substantial robustness gap under real-world conditions, which a Grad-CAM analysis attributes to off-leaf, background-driven attention consistent with shortcut learning. TinyCNN is thus an energy-efficient, deployable building block for sustainable agricultural intelligence, while field robustness remains the key barrier to durable real-world impact.

---


### 172. [Personalising a Cross-User Surface Electromyography Encoder Under a Small Calibration Budget](https://arxiv.org/abs/2609.20296)

**<font color=#1a73e8>作者：</font>** Jethro Odeyemi, W. J. Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A myoelectric interface needs calibration from the user before it will function. Earlier work has treated calibration as a quantity, but has not asked the question of what a device should do with the calibration repetitions once they have been collected. This paper views personalizing the cross-user encoder as a design decision with a cost. Four alternative approaches to using exactly the same labeled repetitions were tested from a single cross-user encoder per held-out subject. Prototypical adaptation, linear probes, scaled fine-tuning and full fine-tuning were tested at every budget up to the maximum each database allows, five repetitions on DB1 and four on DB2 and DB5. Comparing four ways to spend a small calibration budget across 77 subjects, full fine-tuning is the most accurate at every budget, consistently enough that there is no exception among subsets of subjects. The result which impacts how one might make an engineering decision however is that a gradient free prototypical rule recovers 52 to 78 per cent of its benefit with no optimiser and no per-user copy of the weights, which makes personalisation something a worn device can do at donning time. The widespread intuition that a good representation only needs a fresh classifier is incorrect here. How well each method may perform relative to a per-user classifier that would be fitted by a clinic will depend on the specific database.

---


### 173. [Intact-to-Amputee Transfer in Surface-EMG Gesture Decoding: Training Source and Calibration Budget](https://arxiv.org/abs/2609.20297)

**<font color=#1a73e8>作者：</font>** Jethro Odeyemi, W. J. Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A recogniser trained on one person rarely transfers to the next, and useful performance usually demands a fresh round of labelled calibration from the end user. A systematic review of 1077 studies quantifies where the evidence is thin: amputees appear in about one in six. Here a montage-agnostic cross-user encoder is carried to eleven transradial amputees on a protocol matched to its intact-limb training data. Zero-shot cross-population transfer fails outright: the encoder requires labeled data from the new user before it begins decoding, and it then exceeds the per-user classifier a clinic would fit by 0.190 macro F1 at three repetitions and for every subject in the cohort. Given three labelled repetitions it reaches 0.779 macro-F1 against 0.589 for the per-user pipeline. Training on forty intact subjects produces better transfers to a new amputee than training on ten other amputees, and combining the two produces better transfers than either individually. The prediction pre-registered for this study, which extends the encoder's baseline-strength account with the premise that amputee EMG is less separable, holds true only after a few repetitions become available and after enriching the source pool with additional amputees. At a single repetition, and at every budget under a source matched to the intact-limb comparison, it fails. Thus, it locates the boundary of the proposed account.

---


### 174. [A Learning Algorithm for Threshold Boolean Networks with Prescribed Fixed Points](https://arxiv.org/abs/2609.20298)

**<font color=#1a73e8>作者：</font>** Gonzalo A. Ruz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a learning algorithm for inferring threshold Boolean networks (TBNs) with a prescribed set of fixed points. The proposed method employs a custom differentiable loss function that jointly enforces fixed point preservation, penalizes spurious attractors, encourages binary outputs, and promotes sparsity through L1 regularization. Applied to the FOS-GRN model of Arabidopsis thaliana, the approach achieved perfect reconstruction (i.e., all 10 desired fixed points and no spurious ones) in 5 out of 30 independent runs, recovering on average 8.53 $\pm$ 0.90 correct fixed points with no spurious attractors. In contrast, standard methods such as the Perceptron and Logistic Regression recovered up to 10 fixed points but introduced between 8 and 31 spurious ones. An additional analysis varying the sparsity coefficient ($\lambda$) confirmed that the method's performance and the structural properties of the inferred networks remain robust within a practical range (up to 0.01) of regularization strengths. Overall, the results demonstrate the effectiveness and stability of the proposed algorithm in capturing meaningful network dynamics under prescribed dynamical constraints.

---


### 175. [Not All Layers Are Equal: Dynamic Layer Routing for Reliable CLIP OOD Detection](https://arxiv.org/abs/2609.20299)

**<font color=#1a73e8>作者：</font>** Ignacio M. De la Jara, Cristian Rodriguez-Opazo, Damith Ranasinghe  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Information aggregation across model layers are revealed to improve OOD detection. In contrast to crafting a method for layer-wise information aggregation in recent work, we investigate if layer selection is a learnable problem. In other words, we transpose the question from how to fuse layers to one asking which layers to trust for an input. Using a generalizable, weak, out of distribution context crafting approach for supervision, shown to be more effective than state of the art methods' mechanisms, we formulate learning a lightweight router to select a sparse, final-layer-anchored expert over CLIP's layer depth for OOD detection.
Across three diverse benchmarks we demonstrate our learnable routing method dubbed Voyager improves OOD detection. On ImageNet-1K, Voyager achieves an average FPR@95 of 18.86, outperforming the strongest, comparable, prompt-learning method by 8.8 points. These gains persist across multiple supervision sources, including those used by existing state-of-the-art prompt-learning methods, demonstrating that, whilst our weak OOD supervision context is highly effective, the key advantage is realized from the learnable router component rather than the supervision source. Significantly, Voyager is highly practical; router learning takes approximately two minutes using less than 1 GB of memory, making it approximately 20x more efficient than current prompt-learning approaches.
Anonymized Code: this https URL

---


### 176. [Improving Generalization and Robustness in Offline Reinforcement Learning via Boundary-Aware Data Augmentation](https://arxiv.org/abs/2609.20300)

**<font color=#1a73e8>作者：</font>** Gong Gao, Weidong Zhao, Xianhui Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current offline reinforcement learning (ORL) algorithms tend to overfit the training dataset and exhibit poor in-distribution generalization and robustness performance when deployed to real environments, thus compromising their effectiveness. Existing methods typically enhance in-distribution generalization and robustness by leveraging regularization techniques widely used in computer vision. However, due to the high sensitivity of low-level physical signals to distributional shifts, these methods still suffer from notable limitations in in-distribution generalization and robustness, making it difficult to achieve stable performance in complex environments. To address this issue, we theoretically analyze the error bounds of the behavior policy and action-value function trained with random episode interpolation, revealing that the error scales positively correlated with the distance between states. Based on this insight, we propose a method called $\bf{B}$oundary-$\bf{A}$ware $\bf{D}$ata $\bf{A}$ugmentation (BADA), which leverages neighboring states to construct interpolation boundaries, enabling the generation of synthetic data that more faithfully preserves the original data distribution. We first conduct qualitative studies in a toy environment, showing that BADA generates mixed samples that preserve desirable policy smoothness while accurately reconstructing multimodal value distributions. Extensive experiments on limited offline datasets further demonstrate that BADA attains state-of-the-art performance across diverse benchmarks.

---


### 177. [AgentPProf: Semantic Profiler for Long Horizon AI Agents](https://arxiv.org/abs/2609.20301)

**<font color=#1a73e8>作者：</font>** Yusheng Zheng, Chaokun Chang, Yu Mao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly orchestrate long-running activities with users, tools, and system resources for days and weeks. To improve agent quality, safety, and cost efficiency, developers need to determine where failures happen, what triggers unsafe effects, and which tasks consume the most budget, then optimize those tasks. In systems software, profiling answers similar questions by aggregating resource consumption and attributing it to responsible code paths to identify hotspots. Yet existing agent observability tools focus on per-execution debugging and tracing rather than cross-run, long term profiling, making these questions difficult to answer at scale. Agent observability needs profiling, not only debugging, but profiling agents is challenging: the responsible entities are task intent like diagnose authentication, compare branches rather than code paths, and lack stable identifiers for aggregation. We propose a semantic operation stack model that adapts profiling to agent trajectories. Uniform operations represent all activities, and operation stacks replace the runtime call stack, enabling hierarchical attribution at different granularities. We observe that an agent's task occupies a contiguous span and decomposes into subtasks, so we introduce recursive operation segmentation, which recursively splits trajectories at task boundaries. AgentPProf is a profiler that aggregates agent trajectories into pprof-compatible profiles, enabling flame graph visualization and analysis. AgentPProf reaches 0.764 $B^3$ F1 against human annotations on CodeTraceBench. On three problem-localization benchmarks, the profile raises MAP by up to 56%, demonstrating that it effectively attributes resources, locates problems, and helps optimize token cost at practical profiling cost. AgentPProf is available at this https URL.

---


### 178. [SAGG: Sample-Adaptive Gradient Gating for Robust Multimodal Learning under Heterogeneous Corruption](https://arxiv.org/abs/2609.20302)

**<font color=#1a73e8>作者：</font>** Wentao Zhang, Yifan Zhu, Yutong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal gradient balancing methods modulate encoder gradients with a shared scalar per modality, implicitly assuming that corruption is uniform across the training batch. In practice, corruption is sample-heterogeneous: within a single mini-batch, different samples may have different modalities corrupted. We prove that under this heterogeneous corruption model, any batch-level sample-agnostic linear estimator with a shared modulation parameter incurs an irreducible bias with respect to the clean-data gradient, and that sample-level all-or-nothing gating is the unique unbiased strategy within a natural distribution-free estimator class. Motivated by this result, we propose Sample-Adaptive Gradient Gating (SAGG), which makes a binary retain-or-discard decision per sample via an online feature-norm quality test and incorporates a truncation mechanism for variance control. We prove that SAGG-based SGD converges at the standard O(1/sqrt(T)) rate to stationary points of the clean loss without a corruption-dependent error floor, and derive a certified robustness radius for the independent-encoder architecture that connects per-modality Lipschitz constants to the classification margin. Experiments on Kinetics-Sounds and UCF-101 under Gaussian noise injection, partial modality missing, and natural contribution imbalance show that SAGG consistently outperforms ten existing methods, with the largest gains in high-corruption regimes where batch-level bias is most severe.

---


### 179. [Viveka-Insight: a cross-lingual concept graph and citation-grounded retrieval resource over the complete works of Swami Vivekananda in English and Bengali](https://arxiv.org/abs/2609.20303)

**<font color=#1a73e8>作者：</font>** Tamal Maharaj  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Classical philosophical corpora pose three compounding challenges for language resources: they exist in several languages without parallel alignment, their vocabulary is remote from that of contemporary readers, and generated text over culturally sensitive material must be verifiably grounded. We present Viveka-Insight, a bilingual resource and open-source pipeline for the works of Swami Vivekananda (1863-1902): the nine-volume English Complete Works and the ten-volume Bengali Vani o Rachana, two related but non-parallel corpora of about 15 million characters. Four layers are released: (i) a structure-preserving parse (32,694 paragraphs, 168,842 sentences) with per-paragraph anchors deep-linking into the published editions; (ii) a cross-lingual concept graph of 8,362 language-agnostic concepts with 87,518 relation-typed paragraph-concept and 55,872 concept-concept edges, in which canonical English labels act as a string-equality key linking Bengali and English passages with no parallel data; (iii) a bilingual alias inventory of 60,850 surface forms (30,053 English, 30,797 Bengali); and (iv) a human-annotated set of 200 paragraph-concept edges judged by three annotators, released with all per-annotator judgments. We report known-item cross-lingual retrieval over 194 verified rendered lecture pairs (Recall@10 0.86 in both directions), a 30-question audit of citation integrity and modern-question bridging, and a human study placing concept-extraction precision at 0.60 under strict two-annotator consensus (Cohen's kappa = 0.61). The extractor's confidence weight is calibrated: restricting to weight >= 0.8 raises precision to 0.71 while retaining 98% of concept-bearing paragraphs. Precision is markedly lower in Bengali than English (0.54 vs 0.68), locating the weakness in exactly the half that cross-lingual access depends on. The design transfers to other multilingual classical corpora.

---


### 180. [Diagnose, Recover, Certify: Task Readiness under Hidden Dynamics Changes](https://arxiv.org/abs/2609.20304)

**<font color=#1a73e8>作者：</font>** Nguyen Viet Tuan Kiet, Huynh Thi Thanh Binh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A deployed control policy can conceal consequential dynamics changes: an actuator may lose effectiveness without affecting the current task when the policy rarely excites it, despite being critical for a future task that has not yet been specified. We introduce task readiness under dormant dynamics drift, a decision problem that unifies active change diagnosis and post-change control recovery under a limited, task-agnostic interaction budget. An agent must identify whether and where local dynamics have changed, use a small number of informative interactions to characterize the change before downstream task identity is revealed, and subsequently provide each candidate task with either a recovered policy and a calibrated lower bound on its achievable return or an abstention decision to a safe fallback. We propose Evidence-Gated Matched-Pulse Transport, an intervention-based Bayesian procedure that couples fault localization with estimation of actuator effectiveness through a shared matched-response representation, thereby preserving diagnostic reliability while converting localized evidence into recovery-relevant uncertainty. This uncertainty is propagated to task-conditioned policy selection and readiness certification, enabling deployment decisions that explicitly trade off expected performance, confidence, and fallback use. We evaluate the resulting framework on a diverse suite of dormant-actuator benchmarks spanning multiple simulators, under a protocol that separates diagnosis from capability recovery, scores deployment by readiness coverage, selective risk, and interaction cost as well as return, and identifies the fault regimes in which transported evidence is decisive.

---


### 181. [Hypernetwork-Parameterized Spatially Adaptive Neural Operators for PDE Learning](https://arxiv.org/abs/2609.20309)

**<font color=#1a73e8>作者：</font>** Jiaquan Zhang, Chaoning Zhang, Shuxu Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatially heterogeneous partial differential equations (PDEs) exhibit location-dependent dynamics arising from variations in geometry and physical coefficients. Existing neural operators improve localized modeling through multiscale features, attention mechanisms, or domain decomposition, yet their update rules often remain spatially shared. Hypernetwork-based methods adapt parameters across PDE instances but typically generate only one global parameterization per instance. Consequently, shared operators may underfit boundaries and high-gradient regions, with these localized errors accumulating during autoregressive rollout. We propose a spatially adaptive neural operator (SANO), which replaces this spatially shared parameterization with a spatially continuous field of location-dependent operator parameters. SANO uses Fourier-encoded coordinates and a coordinate-conditioned hypernetwork to generate spatial operator-conditioning codes at sampling points. A Hyper-Neural Element (HNE) mechanism interpolates these codes within local subregions, coupling neighboring operators while allowing their update rules to vary across space, and partition-of-unity weights assemble the overlapping local predictions. Experiments on one-, two-, and three-dimensional PDEs and two perforated-domain elliptic benchmarks show that SANO consistently outperforms competitive neural-operator, hypernetwork-based, and physics-informed baselines.

---


### 182. [ZeroHAT: Behavior-Conditioned Zero-Shot Human Activity Trace Generation](https://arxiv.org/abs/2609.20310)

**<font color=#1a73e8>作者：</font>** Rongchao Xu, Dahai Yu, Lin Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human activity traces record individuals' timestamped visits to points of interest and are essential for applications such as mobility prediction and urban simulation. However, accessing large-scale HATs is challenging due to high collection costs and privacy concerns. Synthetic HAT generation offers a promising way to make such data available and has attracted growing interest from both industry and academia. Although many efforts have been devoted to this topic, most of them rely on real data from a region to generate synthetic data for the same region, which is infeasible for the many regions where real HATs are unavailable. To fill this gap, we propose ZeroHAT, a behavior-conditioned framework that generates synthetic HATs for a target region in a zero-shot manner by transferring behavioral patterns learned from real HATs in source regions and adapting them with publicly available contextual information about the target region. ZeroHAT has three key novel components: (i) a multidimensional consistency-aware intent extractor; (ii) a cross-region behavioral cloning module; and (iii) a behavior-conditioned activity realization module. We evaluate ZeroHAT on a ten-city benchmark, where extensive experiments show that ZeroHAT achieves 4.5-6.4x the normalized downstream utility of the strongest baseline and improves average fidelity by 15.6%-40.8% across target regions.

---


### 183. [EviRec: Continual Evidence Learning for Dual Cold-Start POI Recommendation](https://arxiv.org/abs/2609.20313)

**<font color=#1a73e8>作者：</font>** Rongchao Xu, Lin Jiang, Guang Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Point-of-Interest (POI) recommendation is a core task in location-based services, yet most existing methods assume a fixed user population and POI catalog. Through a large-scale data-driven analysis of 10 U.S. cities, we identify substantial POI churn, user turnover, category drift, and decay in static POI memory, motivating the study of continual dual cold-start POI recommendation. To address this setting, we propose EviRec, a continual evidence-learning framework that estimates how much historical evidence should be trusted separately for each candidate POI. EviRec scores each visible candidate from three complementary views: a matching view based on the user's recent mobility profile, a transition-memory view that captures repeated mobility routines, and a lifecycle view that reflects candidate maturity. Because a near-zero transition score may indicate either irrelevance or insufficient observation, EviRec qualifies the evidence using each candidate's observation state and applies a reliability gate to adaptively route between transition-memory and lifecycle evidence. We evaluate EviRec on a full-year, five-city POI check-in dataset containing more than 30,000 users and 684,200 trajectories. Experimental results show that EviRec consistently outperforms state-of-the-art baselines, with the largest gains concentrated on cold-start queries. In particular, EviRec improves NDCG@10 by 20.4\% on Dual-New cases over the strongest baseline. In-depth analyses further confirm that these gains arise primarily from candidate-specific reliability gating while largely preserving previously learned mobility routines.

---


### 184. [DDQN-MLP: An Explainable and Adversarially Robust DRL-Guided Adaptive Learning Framework for Ransomware Detection](https://arxiv.org/abs/2609.20314)

**<font color=#1a73e8>作者：</font>** Jannatul Ferdous, Rafiqul Islam, Arash Mahboubi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ransomware detection remains challenging because modern variants exhibit diverse, evasive, and partly benign-like behaviors that undermine fixed supervised learning objectives. This study proposes DDQN-MLP, a training-time deep reinforcement learning framework for behavioral ransomware detection using Windows 11 sandbox telemetry. A Double Deep Q-Network (DDQN) acts as a discrete adaptive sample-weighting controller by observing batch-level loss and prediction-confidence dynamics and assigning sample-importance weights to guide a lightweight Multilayer Perceptron (MLP). After training, the DDQN is discarded, leaving only the efficient MLP for deployment. The framework was evaluated using 5-fold stratified cross-validation on a balanced dataset of 2,000 executable profiles comprising 1,000 ransomware samples from 30 families and 1,000 benign samples. DDQN-MLP achieved 99.30% accuracy, an F1-score of 0.9930, and an ROC-AUC of 0.9991, outperforming conventional static weighting, focal-loss, and alternative DRL variants. Explainability was assessed using SHAP and LIME, together with a SHAP-gradient alignment diagnostic for evaluating consistency between feature attribution and model sensitivity. White-box adversarial testing across multiple perturbation levels further showed that adversarial training improved feature-space robustness without reducing clean-data accuracy. The results demonstrate that DDQN-MLP provides an accurate, explainable, robust, and computationally efficient framework for high-throughput ransomware detection.

---


### 185. [NeuSOGA3D: A Neuro-Symbolic Framework for Explainable 3D Geometric Reconstruction](https://arxiv.org/abs/2609.20323)

**<font color=#1a73e8>作者：</font>** Qingde Li, Qingqi Hong, Zihan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Three-dimensional reconstruction from unorganized point clouds remains a challenging problem in computer vision, geometric modeling, and computer-aided design. While neural implicit methods achieve impressive reconstruction accuracy, geometry is typically encoded in latent representations that limit interpretability and reuse within engineering workflows.
We present NeuSOGA3D (Neuro-Symbolic Geometric Abstraction in 3D), a hybrid framework that combines learned perceptual priors inherited from NeuSOGA with explicit symbolic geometric reasoning. The method projects point clouds onto principal orthographic planes, constructs symbolic implicit spline representations from the resulting observations, and fuses them through shape-preserving constructive solid geometry operations to generate a coarse visual hull. Additional geometric detail is recovered through cross-sectional decomposition and volumetric reconstruction using Partial Shape-Preserving Splines.
Unlike conventional neural implicit approaches, NeuSOGA3D progressively transforms observations into explicit symbolic entities, including control polygons, implicit spline fields, cross-sections, and volumetric lofts. Experiments on all forty categories of the ModelNet40 benchmark demonstrate the ability of the framework to recover structurally meaningful and CAD-compatible geometric representations from diverse point-cloud observations. The results highlight the potential of combining learned perception with symbolic geometric reasoning for explainable geometric intelligence.

---


### 186. [How Do We Visualize Space in Molecular Biology? A Study of Spatial Transcriptomics Visualization Practices](https://arxiv.org/abs/2609.20324)

**<font color=#1a73e8>作者：</font>** Denisse Chacón-Ramírez, Mark S. Keller, Eric Mörth 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A cell's identity depends on where it sits in tissue: for example, a macrophage behaves differently in a tumor core than at its edge. Spatial transcriptomics has transformed how we study this by recovering that lost coordinate, but it does so by producing data that is simultaneously high-dimensional, multimodal, and uncertain. Visualizing this combination is a hard problem in its own right, and one that warrants an assessment of how the field currently represents it, what has worked, and what is still missing. We surveyed 148 papers and 1,824 figure panels using a What-Why-How coding framework grounded in Munzner's nested model, connecting the data represented, the biological tasks motivating each visualization, and the design choices through which they are expressed; a subset of the surveyed work also contributed dedicated interactive visualization software that was not necessarily reflected in the static figures, and we looked at what interaction capabilities those tools supported as well. We close by outlining where the field stands and the challenges ahead for bioinformatics and visualization researchers to tackle together.

---


### 187. [Sharp Reconstruction Bounds for Autoencoders Using the Same Forward Map](https://arxiv.org/abs/2609.20333)

**<font color=#1a73e8>作者：</font>** Patricia Medina, Hy P. G. Lam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study reconstruction in autoencoders that apply the same forward map before and after setting the observed coordinates to zero. For equal odd input and hidden dimensions $d\geq 3$, among orientation-preserving diffeomorphisms whose Jacobian singular values lie in $[m,M]$, we show that the least uniform reconstruction-derivative error is $\max\{1-M(M-m)/2,0\}$, with affine maps attaining this sharp bound at every prescribed depth. A translated radial rotation can nevertheless reconstruct any prescribed ball exactly with singular values arbitrarily close to one, motivating additional conditions for a finite-data bound. We test this prediction on a 798,452-point terrestrial LiDAR forest scan. At input scale $0.05$, the mean theoretical bound is $0.155$, about $84\%$ of the mean normalized training error $0.185$ across four spatial regions, two depths, and three seeds. At this scale, adding one hidden coordinate reduces the mean reconstruction error below $6\times10^{-6}$.

---


### 188. [Structured Four-Stage Legal Translation: From Natural-Language Traffic Rules to PROLOG](https://arxiv.org/abs/2609.20334)

**<font color=#1a73e8>作者：</font>** May Myo Zin, Wachara Fungwacharakorn, Ken Satoh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traffic regulations are written for human interpretation and therefore rely on shared background knowledge and flexible phrasing, which inherently introduce ambiguity, context dependence, and semantic underspecification. These linguistic characteristics conflict with the precision required by computational reasoning engines such as Prolog, which demand explicit logical structure. This study evaluates two baseline translation approaches, Natural Language to Prolog ($NL\rightarrow Prolog$) and Logical English to Prolog ($LE\rightarrow Prolog$), and introduces a new reasoning-guided translation framework called Structured Four-Stage Legal Translation ($S4L\rightarrow Prolog$). The proposed S4L framework performs semantic role extraction, scene completion, logical mapping, and Prolog rule generation within a single guided prompt, enabling direct translation of raw traffic rules into executable logic without human intervention. A benchmark consisting of twenty real-world traffic rules was used to evaluate each approach in terms of syntactic validity, semantic correctness, and logical completeness. $S4L\rightarrow Prolog$ achieves the highest accuracy, correctly formalizing 75 percent of the rules, while $NL\rightarrow Prolog$ reaches 60 percent and $LE\rightarrow Prolog$ reaches 55 percent. Qualitative analysis further shows that S4L captures implicit causal relations, deontic modality, and exception structure more reliably than the baselines. These results demonstrate that structured reasoning prompts can substantially improve the reliability of natural-language-to-logic translation for legal and safety-critical applications.

---


### 189. [Fast Cross-Strength Multi-Contrast Brain MRI Translation using Latent Bridge Matching](https://arxiv.org/abs/2609.20341)

**<font color=#1a73e8>作者：</font>** Siddharth Srivastava, Till Bretschneider  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Magnetic Resonance Imaging (MRI) acquired at different field strengths exhibits pronounced variation in noise, resolution, homogeneity, and contrast, which limits comparability across acquisition settings and complicates downstream analysis. We address this with a unified conditional model for controllable field-to-field synthesis, built on the framework of conditional latent bridge matching. Our single model achieves highly competitive results across the validation phase for all three tasks of the MRIxFields2026 challenge without task-specific architectures or training. We achieve fast generation with only a single inference step, producing all modality and field-strength combinations for $30$ axial slices in under $90$ seconds, as well as cross-modality-strength translation for a full volume in under $70$ seconds, on a single NVIDIA A5000 GPU. We further provide extensive ablations regarding different components of our solution. Code: this https URL

---


### 190. [EliGSiR: Continual RGB-D Mapping with Gaussian Splatting under Bounded Compute](https://arxiv.org/abs/2609.20348)

**<font color=#1a73e8>作者：</font>** Björn Ellensohn, Elmar Rueckert, Christian Rauch  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional 3D Gaussian Splatting assumes a closed set of observations and long optimization schedules. Continual RGB-D mapping in contrast poses the problem that new observations arrive online, while previously reconstructed regions must be preserved. We present EliGSiR (Evidence-guided Load-adaptive Incremental Gaussian Splatting with Image Replay), a continual Gaussian mapper that controls how the available optimization budget is used as the reconstruction evolves. Map-Guided View Scheduling filters redundant incoming views and reconsiders retained views according to the current state of the map. Load-Adaptive Fidelity adjusts supervision resolution to the current mapping load instead of following a fixed resolution schedule. Targeted Geometry Growth separates depth supervision from Gaussian creation and adds geometric capacity only where repeated RGB-D observations indicate missing or misplaced structure. Together, these mechanisms adapt which views are optimized, how much image detail is used, and where the representation grows while mapping remains active. We evaluate EliGSiR on Replica, TUM RGB-D, ScanNet++, and real RGB-D sensor sequences, considering both the final reconstruction and the map available throughout acquisition. On TUM RGB-D fr3/long_office_household, EliGSiR reaches 21.52 dB with the same ground-truth mapping poses used by the controlled baselines, compared with 19.42 dB for SplaTAM. In the tracked-pose comparison, EliGSiR with live ORB-SLAM3 poses reaches 23.02 dB in 155.5 s, compared with 20.10 dB in 230.9 s for CaRtGS using its native tracker. We further evaluate reconstruction throughout acquisition and show how EliGSiR adaptive view scheduling, supervision fidelity, and geometry growth improve the use of the available mapping budget.

---


### 191. [A Qualitative Model for Reasoning about Path and Support](https://arxiv.org/abs/2609.20349)

**<font color=#1a73e8>作者：</font>** Abhishek Jaiswal, Zoe Falomir  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning abilities correlate strongly with performance in STEM fields. Games offer a compelling medium for training these critical skills in developing children who have a natural proclivity for play. However, to facilitate human-like tutoring and player guidance, these games require an AI agent capable of making commonsense inferences from spatial events. Qualitative reasoning (QR) models appear to be a suitable framework for these application domains. As these models reason in symbolic representations, they can seamlessly translate game states into interpretable feedback for human-like player guidance. This paper introduces a hybrid qualitative model designed for Camelot Jr., a block-puzzle game that requires constructing multi-level bridges to connect two avatars stationed on separate towers. The game poses a challenge for the player, who must make platforms stable, plan their path, and ensure they use all the provided blocks. To handle the precise physics required by the domain, we integrate a mathematical center-of-mass stability logic to guide our qualitative solver. Our work facilitates spatial skill training in Camelot Jr. and contributes to the development of human-centric, explainable game-playing agents.

---


### 192. [COMPASS: Ordered Clustered Routing at 100K Scale](https://arxiv.org/abs/2609.20352)

**<font color=#1a73e8>作者：</font>** Ido Greenberg, Hugo Linsenmaier, Piotr Sielski 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale routing often requires visiting clusters of nodes in a prescribed order, giving rise to the Ordered Clustered Traveling Salesman Problem (OCTSP). Optimizing each cluster independently seems natural, but misses non-local dependencies. We introduce the COMPASS algorithm for OCTSP, which combines search with learning-accelerated routing by orchestrating parallel sub-solvers. COMPASS has no quality ceiling and its solutions keep improving with compute. It exploits the clustered structure, and can reach exact solutions in time exponential in cluster size rather than instance size. Empirically, COMPASS consistently outperforms alternative methods. Unlike common large-scale routing solvers, COMPASS consumes general distance matrices and is not limited to coordinate inputs. We demonstrate scaling to 100K synthetic nodes and to 28.5K real e-commerce nodes. To our knowledge, the latter is the largest reported routing solution over asymmetric distances, 9x beyond established ATSP benchmarks.

---


### 193. [Minimax-Optimal Online Contract Design with Unrestricted Bounded Contracts](https://arxiv.org/abs/2609.20353)

**<font color=#1a73e8>作者：</font>** Rui Ai, David Simchi-Levi, Han Zhong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study repeated contract design when a principal observes outcomes but not the actions that generate them. The principal may use any bounded outcome-contingent payment vector, and the agent's best response can make expected profit discontinuous in those payments. For every fixed number $m\ge2$ of outcomes, the minimax regret over $T$ rounds is of order $T^{m/(m+1)}$, up to logarithmic factors. The upper bound allows arbitrary action spaces and agent heterogeneity, without smoothness or monotone-surplus assumptions. Its key is an effective-dimension reduction that the benchmark can be normalized even when fixed tie-breaking is not shift invariant, after which revealed preference yields a monotone response map in payment-difference coordinates. A learning policy built on a Lipschitz parametrization of this map attains the rate using only observed outcome categories. The lower-bound construction accounts for how incentive losses accumulate across outcome dimensions. It shows that each additional contractible outcome creates a precise and unavoidable increase in the worst-case cost of learning.

---


### 194. [Generating Heterogeneous 3D Geological Microstructures from 2D Images via a Stable Diffusion-Adversarial Model](https://arxiv.org/abs/2609.20358)

**<font color=#1a73e8>作者：</font>** Ali Aouf, Eric Laloy, Bart Rogiers 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Characterizing the physical properties of clay and cementitious materials matters across many fields, from materials science to geological waste disposal. Property simulation typically calls for 3D imaging, which is expensive, not always accessible, and technically limited for certain materials. Recent progress in deep generative models offers a way around this, reconstructing 3D volumes from the more easily acquired 2D images.
Among GAN-based methods for 3D microstructure generation, SliceGAN has shown strong results for homogeneous isotropic and anisotropic systems. It struggles, however, to capture the finer detail of more complex heterogeneous microstructures, which motivates alternative generative frameworks.
We introduce a hybrid approach that draws on the stability and generation quality of denoising diffusion models. Since no 3D ground truth is available, we replace the standard denoising loss with an adversarial loss, which yields a stable training process in our experiments. We show that the resulting model generates microstructures of varying complexity with minimal slice artefacts and close agreement with ground-truth phase fractions and structural descriptors.

---


### 195. [MM-Future: Multi-Mode Joint World-Action Modeling for Autonomous Driving](https://arxiv.org/abs/2609.20377)

**<font color=#1a73e8>作者：</font>** Shuai Liu, Hechangle Gong, Hao Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving involves coupled decision-making and scene evolution under multi-mode uncertainty. To capture this coupling and uncertainty, we introduce MM-Future, a world-action model that generates multiple paired scene-action hypotheses and models bidirectional interaction within each pair. Each hypothesis is initialized from a structured action prior and an independent future scene source, which are then co-evolved through a modality-aware diffusion Transformer. To support efficient multi-mode rollout, MM-Future compresses multi-view video into planning-oriented representations, dubbed MM-Tokens. Finally, a future-conditioned proposal scorer ranks trajectory candidates by shared history context and their paired predicted future. On NAVSIM navtest, MM-Future achieves 94.0 PDMS and 91.5 EPDMS, while attaining a 32.3 HD-Score in zero-shot closed-loop evaluation on HUGSIM. Ablations show consistent improvements over both single-mode and action-only variants, validating the benefit of multi-mode joint world-action modeling.

---


### 196. [Compact Vision Models for Iris Presentation Attack Detection under Presentation Attack Instrument Shift and Environmental Degradation](https://arxiv.org/abs/2609.20386)

**<font color=#1a73e8>作者：</font>** Athanasios Angelakis, Marta Gomez-Barrero  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Iris presentation attack detection (PAD) is security-critical when a subsystem that appears reliable during development encounters presentation attack instruments (PAIs) or acquisition conditions absent from validation data. We benchmark three compact scratch-trained computer-vision models, each with at most approximately 0.26 million trainable parameters, on the Notre Dame subset of LivDet-Iris 2017 under PAI-driven domain shift and environmental degradation. All models are trained without external pretraining or data augmentation and evaluated over five seeds. A validation-selected threshold is transferred unchanged to the known-attack, unknown-attack, corrupted, and pooled test partitions. From known to unknown attack presentations, Attack Presentation Classification Error Rate (APCER) increases by 17.11-30.47 percentage points and Detection Equal Error Rate (D-EER) increases by 7.38-12.73 percentage points. At the validation-selected threshold, ZACH-ViT obtains the lowest unknown-attack APCER (47.69 +/- 4.84%) and D-EER (38.87 +/- 0.93%), while Compact-TransMIL obtains the lowest Bona Fide Presentation Classification Error Rate (BPCER). ZACH-ViT also gives the lowest unknown-attack BPCER at an APCER limit of 10% (81.29 +/- 1.95%). The high absolute errors show that the comparative advantage of the best compact model does not constitute deployment readiness under unknown PAIs.

---


### 197. [Learning Principal-Agent Contracts for Equitable Smallholder Carbon Farming under Moral Hazard and Adverse Selection](https://arxiv.org/abs/2609.20404)

**<font color=#1a73e8>作者：</font>** Rishi Bharadwaj, Yadati Narahari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agricultural soils are a major untapped carbon sink. Carbon farming is emerging as a promising practice for tapping this potential. Smallholder farmers, who dominate agriculture across South Asia and sub-Saharan Africa, are key to scaling climate mitigation via carbon farming. It is ironic that real-world carbon programs largely fail to reach them. We study this important gap through the lens of contract design. An aggregator offers a single pooled contract to a heterogeneous population of smallholder farmers who have private adoption costs (adverse selection) and exert unobserved effort (moral hazard), with agronomic outcomes evolving over multiple seasons. We formulate this evolving contracting problem as a POMDP and use reinforcement learning to learn a dynamic profit-maximising contract. We analyse the performance of the aggregator under various conditions. We find that a profit-maximising aggregator does not merely inherit the exclusion of smallholders, it amplifies it. On large farms the aggregator realises 87.7% of achievable adoption, against only 8.2% on smallholdings. Per-hectare Measurement, Reporting and Verification (MRV) costs fall as farm size rises, and the aggregator's pooling contract compounds this gradient rather than offsetting it. A counterfactual that makes MRV costs purely area-proportional eliminates this disparity. Our results and simulation can guide contract and policy design that opens carbon income to smallholders while enabling agricultural soils to contribute to climate mitigation at scale.

---


### 198. [The Bias of Nonlinear Two-Time-scale Stochastic Approximation under Constant Step-Sizes](https://arxiv.org/abs/2609.20409)

**<font color=#1a73e8>作者：</font>** Djamel Rassem Lamouri, Dorian Baudry, Nicolas Gast  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two-timescale stochastic approximation (TTSA) is a fundamental tool for analyzing coupled iterative algorithms in reinforcement learning, optimization, and stochastic control. However, finite-time guarantees for nonlinear two-timescale schemes remain difficult to obtain, especially under constant step-sizes. In this paper, we study nonlinear TTSA with step-sizes $\alpha\gg\beta$. Under standard stability, regularity, and Markovian noise assumptions, we upper bound the mean-squared error and the bias of both iterates around their limiting equilibria. Our bounds scale as $O(\alpha+\beta^2/\alpha^2)$, which we prove to be tight when $\beta\le\alpha^{3/2}$. The analysis separates the contributions of initial conditions, fast-timescale tracking error, Markovian dependence, and timescale coupling, thereby clarifying the origin of the $\beta^2/\alpha^2$ term. Our results reveal qualitative differences from the linear TTSA setting previously studied, showing that nonlinear dynamics introduce additional finite-time effects that are absent in the linear case.

---


### 199. [Stress-testing Alignment Midtraining](https://arxiv.org/abs/2609.20412)

**<font color=#1a73e8>作者：</font>** Sid Baines, Jonathan Bostock, Maria Angelica Martinez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When aligning frontier models through post-training techniques, it is not possible to directly demonstrate all of the behaviours we want a model to exhibit in all possible deployment environments; our model must generalise outside of the post-training distribution. One proposed solution is alignment midtraining (AMT), which continues pretraining on large volumes of alignment-relevant documents to encourage generalisation in later stages of training.
Despite the prominence of AMT as an alignment approach, there is limited public evidence for its effectiveness. To resolve this, we identify several assumptions around midtraining and evaluate them across scale: up to 110 billion-parameter models and 1 billion midtraining tokens. For instance, we study a scenario where post-training data is ambiguous between two possible motivations. We find that midtraining can steer the model's motivation in simple versions of this setting. However, the presence of a tiny fraction of finetuning data which suggests a competing motivation erases the effects of AMT. We also study scenarios in which we want an AI to follow a number of rules, but only demonstrate a subset of them. We find that demonstrations must be present either in midtraining or post-training datasets for these rules to be robustly learned.
Based on these and other findings, we do not believe that there is sufficient public evidence for us to confidently state that midtraining can address the core difficulties inherent in aligning powerful AI systems.

---


### 200. [TouchSight: Bare-Handed Tactile Prediction from Egocentric Video via Generative Visual Augmentation](https://arxiv.org/abs/2609.20414)

**<font color=#1a73e8>作者：</font>** Danyan Zhou, Jinxuan Lu, Jiawei Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tactile signals provide direct contact and force measurements that are essential for understanding physical interactions and enabling dexterous robotic manipulation. However, tactile sensing requires direct measurement at contact interfaces, making large-scale data collection reliant on intrusive, costly, and restrictive instrumentation. We present TouchSight, a monocular egocentric vision framework for dense full-hand contact force prediction that leverages 500 hours of pressure-glove recordings and extensive hand-object interaction (HOI) data. To address the appearance gap between gloved training data and bare-hand real-world scenarios, we construct TwinTouch-20H: 20 hours of paired visual data in which generative video models re-render gloved recordings as bare-hand observations against new backgrounds while preserving the original measured tactile labels. TouchSight predicts dense force from both gloved and generated bare-hand videos, outperforms prior contact prediction methods on OakInk2, qualitatively generalizes to natural bare-hand egocentric videos from unseen datasets, and improves consistently as glove supervision scales. These results demonstrate that dense tactile signals can be recovered from egocentric vision alone, without tactile instrumentation at capture time.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-247](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
