# 📦 其他研究 | 2026年10月02日

> 本类共 **382** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-382](./part-08.md)

---

### 151. [Synchronous Multi-view Neural Diffusion](https://arxiv.org/abs/2609.39019)

**<font color=#1a73e8>作者：</font>** Yongquan Shi, Weijun Huang, Yueyang Pi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-view learning seeks to learn more comprehensive representations by exploiting the complementarity and consistency across diverse modalities or views. However, existing multi-view fusion strategies treat intra- and inter-view fusion as independent stages, without simultaneously considering the evolution within views and the dependency across views. Such an asynchronous fusion paradigm inevitably constrains cross-view interactions due to conflicting view-specific structural inductive biases. As a result, information flow is prone to distortion and compression along intermediate pathways, confining the model to learn within a restricted solution space. To address this, we propose Synchronous Multi-view Neural Diffusion (SynMDiff), which conceptualizes the multi-view feature space as a unified dynamical system driven by a diffusion process. By modeling the diffusion flow across arbitrary dyadic feature interactions in a joint space, SynMDiff enables the concurrent and adaptive intra- and inter-view information fusion. While a direct implementation of this synchronized mechanism incurs prohibitive computational costs, we further introduce an energy-based topological sampling strategy and an Ego-Net style centralized training architecture, ensuring both efficiency and scalability during learning and inference. Due to its conceptual elegance and computational efficacy, evaluations on real-world datasets demonstrate that SynMDiff outperforms the baselines by a large margin.

---


### 152. [When Attention Guardrails Become Barriers to Learning: Towards the Tipping Point](https://arxiv.org/abs/2609.39023)

**<font color=#1a73e8>作者：</font>** Meenakshi V., Pavani Ayinampudi, Aditya B. M. V. 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Online learning offers flexibility but lacks the structure of a classroom, where a teacher's presence guides attention. The platform we study restores that structure by monitoring the learner through the webcam during ordinary coursework, interrupting or restarting a video when the learner appears distracted. What such monitoring does to a learner across a whole course, rather than in a single examination, is largely unexamined. We report a convergent mixed-methods study of one monitored course pipeline in a summer internship program. We read two free-text surveys alongside three platform channels. The dropout exit survey yielded 15 analyzable responses; the persisting-learner reflection survey, 36. The channels are camera-verification telemetry (14,529 flags from 448 students), an in-video emotion widget (615 submissions from 273 students), and a mandatory end-of-course survey (up to 634 respondents per item). Neither survey named monitoring, so every mention analyzed here was raised by the respondent. Focus-monitoring was raised by 18 of the 51 free-text respondents: 7 of 15 dropouts and 11 of 36 persisting learners. Among the dropouts who raised it, focus-monitoring was the stated primary cause of departure in 4 of 7 cases. None of the 18 questioned being observed in principle. What learners contest is the misreading of ordinary actions, drinking water or moving the head, and the severity of what follows a flag: a video already watched returns to the start of its segment. These findings identify two targets for redesign: the severity of the response to a flag, and the environment check, which can flag a learner before any content has been seen. We argue that the proportionality of that response marks the point at which an attention guardrail becomes a barrier to learning, the tipping point this study approaches.

---


### 153. [Persistent Watermarking of Text-to-Image Models](https://arxiv.org/abs/2609.39024)

**<font color=#1a73e8>作者：</font>** Dixi Yao, Kaiwen Chen, Tahseen Rabbani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) generation is gaining increasing popularity with the general public, motivating the development of reliable mechanisms for copyrighting such models given their expensive training costs. An adversary may obtain and reuse a pretrained T2I model without authorization, and then serve a modified version through an API service. Such modifications may arise from ordinary downstream adaptation or deliberate attempts to erase ownership, including input-prompt preprocessing, model fine-tuning, and output post-processing. From the model owner's perspective, a key challenge is therefore to embed trigger data that remain persistent under such changes while preserving the model's normal image-generation capabilities. In this work, we propose a contrastive-style watermarking objective with a term that explicitly encourages the watermarked model to behave differently from the original model on trigger inputs. Experiments show substantially stronger trigger-data persistence than prior methods across a wide range of downstream modifications and deliberate attempts to weaken the watermark, resulting in higher detection rates, often approaching 100% TPR@FPR<$10^{-4}$.

---


### 154. [A Rank Graduation metric for Algorithmic fairness](https://arxiv.org/abs/2609.39025)

**<font color=#1a73e8>作者：</font>** Dalia Atif, Paolo Giudici  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fairness assessment in algorithmic decisions that affect individuals, such as credit scoring, often relies on parity measures calculated at the aggregate group level. Such measures may not reveal which individuals experience unfairness or which explanatory factors contribute to it. In this paper, we propose a rank-based framework that evaluates fairness through the distribution of model prediction errors, thereby linking fairness assessment with predictive accuracy and explainability. The framework combines Rank Graduation Fairness (RGF), its integrated measure AURGF, a centered Cramer--von Mises permutation test, and a feature removal procedure for fairness explainability.
We evaluate the methodology using logistic regression, random forest, gradient boosting, and a multilayer perceptron. The simulation study shows that protected-group imbalance can reverse descriptive fairness comparisons, whereas the proposed inferential procedure correctly distinguishes fair from unfair mechanisms. Its application to HMDA mortgage data produces model rankings that differ from those obtained with classical fairness criteria. Tree-based models, rather than logistic regression, provide the strongest combination of predictive accuracy and rank-based fairness, while the fairness null hypothesis is rejected for all four models. The persistence of disparity across statistical, bagging, boosting, and neural network specifications, together with the feature removal results, indicates that the observed unfairness is not specific to a single algorithm or predictor, but is associated with group differences embedded in the characteristics of the lending data. These findings support a broader approach to trustworthy artificial intelligence that combines predictive accuracy, fairness measurement, statistical inference, and explainability.

---


### 155. [Search Shapes Conclusions: Auditing Evidence Selection Bias in Deep Research Agents](https://arxiv.org/abs/2609.39026)

**<font color=#1a73e8>作者：</font>** Shuyao Xiao, Shengling Wang, Xuan Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep Research agents synthesize evidence into cited reports, yet a well-cited report can still reach a misleading conclusion. Citation correctness checks whether cited sources support individual claims. It does not show whether adaptive search exposed a representative view of all documents made available for evaluation, which we call the candidate pool. Early findings redirect later queries, document choices, and stopping, so the documents an agent reads form a selective sample. Existing evaluations rarely account for this selection. We formulate the problem as adaptive evidence sampling and introduce Causal Evidence Selection Correction (CESS). CESS predicts each candidate document's evidence direction and corrects the candidate-pool average using the logged probabilities of selecting each document and reaching each search round. Shrinkage stabilizes short searches, while intervals replace point estimates when some documents cannot be sampled. We also prove that estimating the average evidence direction of a common pool differs from measuring how a change in search policy alters the evidence read. The latter requires intervention. On questions from the MS2 systematic-review benchmark, CESS reduces mean absolute error against the candidate-pool average by $9.2\%$ and reduces the estimate's change under opposing document rankings by $39.4\%$ relative to averaging the evidence scores of documents read. Across trajectories from a public Open Deep Research agent, the corresponding reductions reach $60.1\%$ and $87.2\%$. A further 4,800 trajectories under paired interventions confirm that correcting a pool estimate and measuring a policy effect are different tasks. CESS therefore audits whether the evidence direction underlying a report reflects the documents available for evaluation, while a separate intervention analysis measures the effect of search decisions.

---


### 156. [Switching Linear Attention](https://arxiv.org/abs/2609.39034)

**<font color=#1a73e8>作者：</font>** Hyun Dong Lee, Xavier Gonzalez, Nicolas Zucchet 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing expressive sequence layers with efficient inference remains a central challenge in modern machine learning. Standard softmax attention achieves excellent sequence modeling performance through rich nonlinear token interactions, but it requires a key-value cache that grows linearly with sequence length, limiting its scalability. Linear attention enables efficient recurrent computation with a constant memory footprint, yet its reduced expressivity often yields inferior modeling performance. We introduce Switching Linear Attention (SwiLA), a novel sequence layer that bridges this gap by enhancing representational capacity while retaining the fixed-size recurrent state of linear attention. We derive the SwiLA recurrence from the test-time regression framework, casting the state update rule as online expectation-maximization in a mixture of linear regressions model. At test time, each output dimension dynamically selects among multiple linear attention components based on the input. Across associative recall, in-context language learning, and language modeling benchmarks, SwiLA shows strong performance and narrows the gap to softmax attention, even surpassing it in several settings.

---


### 157. [Cycle-Aware Autoencoder with Cross-SignalConsistency for Railway Door Anomaly Detection](https://arxiv.org/abs/2609.39035)

**<font color=#1a73e8>作者：</font>** Ammar Bouketta, Smail Niar, Hamza Ouarnoughi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Passenger access doors are safety-critical subsystems in railway vehicles, yet detecting abnormal door behavior in real operation is challenging because faults are rare, diverse, and often unlabeled. This paper addresses railway door condition monitoring as a cycle-level unsupervised anomaly detection problem, where each complete opening-dwell-closing cycle is treated as a single monitoring unit. We propose the Temporal Cycle-Aware Attention Autoencoder with Cross-Signal Consistency (TCAA-CS), trained exclusively on nominal cycles. It combines a dual-stream encoder that processes continuous physical measurements (position, current, voltage) and binary logical states (door-closed, door-locked) through separate 1D-CNN branches, an LSTM encoder with temporal attention pooling, and a triple hybrid anomaly score fusing reconstruction error, latent-space deviation, and phase-aware cross-signal consistency. The consistency term helps identify cases where individual signals appear plausible but their inter-signal relationships become physically or logically inconsistent. On real industrial data from a passenger train in commercial service, TCAA-CS achieves 93.8% recall, 97.3% precision, and a 0.5% false-alarm rate, outperforming representative unsupervised baselines. System-level evaluation on an NVIDIA Jetson AGX Xavier supports the feasibility of real-time onboard deployment.

---


### 158. [Hard-Gate Candidacy in a Deployed Validator Suite](https://arxiv.org/abs/2609.39037)

**<font color=#1a73e8>作者：</font>** Xin Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Before a validator can be promoted to a hard gate on a deployment pipeline, it has to be shown that its firing separates outputs that reach users in working order from those that do not. We run that screen on 13 validators in a deployed generative agent, against 550 runtime and 350 static builds labelled by downstream outcome, and report each check's marginal separation $J=\mathrm{TPR}-\mathrm{FPR}$ with Newcombe intervals and Fisher exact tests. Two checks survive correction for multiple comparisons, two more are nominal only, and the remaining nine are not distinguishable from zero, three of them because they never fired on any sampled build. Execution itself is not random with respect to the property being gated, and this replicates: across four runs covering 1,867 builds and ten distinct runtime checks, probes were skipped on 144 of 895 broken builds and 1 of 972 acceptable builds (per-run rates 15.6% to 16.6% against at most 0.3%), every skip carrying the same unsafe-to-probe reason. Because a skipped check is recorded as a pass, this imposes a ceiling that no check quality can lift: a check that needs a live artifact cannot operationally detect more than about 84% of broken builds in this harness. For the one check with construct-specific labels, a detector built for blank output fires on 0 of 90 human-labelled blank builds (95% upper bound on sensitivity 3.3%), and the global frame statistic it approximates separates the classes only weakly (AUC 0.59), so the gap is not a threshold that needs tuning. The same gap appears one layer up: on a census of tens of thousands of judge-scored builds, 32.5% of rejections carry no recorded issue at all. We argue that evaluation records must distinguish a check that ran and passed from one that did not run, must carry the evidence for a rejection, and that an inventory of checks is not evidence about a gate.

---


### 159. [BadAction: Backdoor Attacks on Interactive Video Generation via Action-Guided Triggers](https://arxiv.org/abs/2609.39047)

**<font color=#1a73e8>作者：</font>** Zhihang Wu, Zhongqi Wang, Jie Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive video generation (IVG) models have achieved remarkable progress in producing controllable visual content guided by user-defined actions, yet their security vulnerabilities remain largely unexplored. In this paper, we present the first systematic study of backdoor attacks against the interactivity of IVG models. Based on this attack surface, we propose BadAction, which leverages action-guided triggers to achieve the attack. Specifically, BadAction implants predefined motion patterns into the action sequences of backdoor samples and associates them with a static target video. Once triggered, the backdoored model generates frozen future frames that no longer respond to subsequent user actions, while preserving normal behavior on benign action sequences. In addition, we explore a stealthier attack in which multimodal triggers jointly poison action, text, and image inputs. Experiments show that BadAction achieves average attack success rates of 91.0% with action-only triggers and 80.4% with multimodal triggers. Moreover, extensive defense evaluations show that BadAction successfully bypasses existing backdoor detection methods, revealing a critical security gap in the interactive video generation pipeline. Project page: this https URL.

---


### 160. [Structure-aware Reinforcement Learning for Protein Directed Evolution](https://arxiv.org/abs/2609.39048)

**<font color=#1a73e8>作者：</font>** Zikun Nie, Suyuan Zhao, Yizhen Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein optimization remains a longstanding goal in life sciences. Existing machine learning-assisted directed evolution (MLDE) methods primarily rely on sequence-only features, overlooking the critical spatial constraints and co-evolutionary interactions encoded in protein structures. However, directly integrating structural information remains challenging due to the scarcity of reliable mutant structures. To address these issues, we propose StructEvo, a novel structure-aware reinforcement learning framework for protein directed evolution. StructEvo employs a delta-structure fusion encoder to approximate mutant structure features via feature differences, enabling dynamic incorporation of spatial knowledge. The vast mutation space is then decomposed into manageable subspaces through a structure-aligned hierarchical action network, while a geometric constraint further stabilizes delta feature learning. Our approach outperforms prior state-of-the-art methods by 9.2% and 16.3% on two challenging optimization benchmarks, and further identifies an experimentally validated epistasis pattern in GFP, highlighting the importance of structural guidance for effective protein directed evolution.

---


### 161. [TSMD: Temporal-Stream Modality Dropout for Robust Video Highlight Detection](https://arxiv.org/abs/2609.39051)

**<font color=#1a73e8>作者：</font>** Bo-Yuan Cheng, Kuan-Yu Chen, Po-Han Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing multimodal video highlight detectors typically assume that visual, audio, and textual streams are continuously available. In practice, however, inputs may suffer from localized frame missingness or complete-stream outage. We formulate this robustness challenge along two dimensions: temporal missingness, where frames are missing independently in each modality, and stream-level missingness, where one modality is unavailable throughout a video. Moreover, we find that the mean squared error (MSE) loss is misaligned with both the evaluation metrics and the peak-driven nature of highlights. Therefore, we propose Temporal-Stream Modality Dropout (TSMD), which combines structured missingness simulation with a joint objective comprising pointwise MSE, per-video Pearson correlation, and peak-oriented RankNet loss terms. TSMD has three variants: temporal, stream-level, and mixed dropout. On the MoSu and Mr. HiSum datasets, TSMD-Temporal improves mAP@15 by 7.06 and 3.41 points over TripleSumm under 50% independent temporal removal, whereas TSMD-Stream performs the best under complete-stream removal. TSMD-Mix retains most of these complementary benefits and ranks the best or the second-best across the evaluated temporal and stream-level conditions.

---


### 162. [The Missing Coefficients: Bayesian Pairwise Merging for Model Personalization](https://arxiv.org/abs/2609.39055)

**<font color=#1a73e8>作者：</font>** Yaling Shen, Tongtong Wu, Siyuan Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How can we personalize a shared expert library from a user's pairwise choices? Prior work can realize different reward trade-offs by merging reward-specialized experts, given a vector of trade-off weights. In practice, users can more naturally choose between outputs than specify numerical weights. The challenge is therefore to turn these choices into the coefficients required for merging, while accounting for ambiguity when feedback is limited. Our key idea is to treat the unknown reward weights as latent variables: infer a posterior over them from pairwise choices and reward-score differences, and use its mean directly as the merge coefficients. We instantiate this idea as Bayesian Pairwise Merging (BPM), whose posterior also characterizes which reward trade-offs remain plausible given the feedback. We evaluate BPM on radiology summarization, image captioning, and story generation, spanning text-to-text and image-to-text generation. With 100 feedback per simulated persona, BPM achieves macro decided win rates of 91.7%, 77.1%, and 64.3% against uniform merge. For six pairs of simulated personas, each prefers the model fitted to its own feedback, a pattern also observed in a human proof-of-concept. In simulations under BPM's model and prior, its nominal 90% intervals for temperature-scaled reward weights achieve task-averaged marginal coverage of 88.9% and 89.2% with only 10 and 25 comparisons, respectively. BPM thus enables personalization from pairwise feedback without per-user policy training, while characterizing the coefficient ambiguity left by limited feedback.

---


### 163. [Argus: A Real-EKS Study of When Predicting Spot Interruptions Beats Simple Checkpointing](https://arxiv.org/abs/2609.39067)

**<font color=#1a73e8>作者：</font>** Angshuman Chakravertty, MD Rayyan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Elastic Compute Cloud (EC2) Spot is 60% to 90% cheaper than On-Demand but can be reclaimed on just a 2-minute notice; for expensive multi-node training this loss can be severe, with one reclaim costing hours of synchronous progress. We build Argus, a Kubernetes operator, and ask empirically, on a CIFAR-10 testbed, when predicting interruptions beats simple checkpointing. Argus on real EKS survives a real Spot drain with a graceful SIGTERM checkpoint, resuming from epoch 8 and losing only the in-progress epoch. Alongside, we further find that in an 80-trial benchmark, the reactive-on-notice degrades toward no protection once interruption outpaces the fixed 2-minute notice, and predictive wasted compute is driven to zero, but with an oversized fixed lead it over-migrates so severely that at the fastest rate only one of five runs completes, while periodic is a strong ML-free baseline. A lead-time sweep turns the lead prediction into a guideline where a small lead suffices for zero waste, but excess lead is wasteful. The predictor built is advisory (a proxy label); real interruption labels and large-model-scale validation are future work.

---


### 164. [HO-FL: Hybrid-Order Federated Learning for Heterogeneous Edge Devices](https://arxiv.org/abs/2609.39074)

**<font color=#1a73e8>作者：</font>** Qiyuan Chen, Xian Wu, Yanan Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) on memory-constrained edge devices faces a dilemma: first-order (FO) optimization (i.e., backpropagation) demands substantial memory, whereas zeroth-order (ZO) optimization suffers from severe convergence slowdown. To resolve this dilemma, we introduce HO-FL, a hybrid-order FL framework that trains a model's bottom segment with ZO optimization and its top segment with FO optimization. Each device can flexibly select its order boundary according to its memory budget while participating in the training of the same global model. Moreover, our convergence analysis reveals a new, fundamental trade-off: clients with larger FO-trained segments can provide more accurate updates, but favoring them can underrepresent other clients' data. We connect this trade-off to the bias and variance of actual multi-step local updates, yielding a sampling optimization problem and a practical dimension-aware approximation with direct model averaging. Experiments on language tasks examine task performance, client memory, and sampling under data heterogeneity. The results show that hybrid-order local training can retain much of the full-FO performance with substantially lower client memory requirements. Our code is available at this https URL.

---


### 165. [Parameter symmetries determine representational geometry in overparameterized nonlinear networks](https://arxiv.org/abs/2609.39078)

**<font color=#1a73e8>作者：</font>** Marvin Theiss, Lukas Braun, Andrew M. Saxe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representations are routinely used across machine learning, psychology, and neuroscience to draw inferences about the computations of biological and artificial systems. Such inferences presume a meaningful link between representational geometry and the computation being performed. For artificial neural networks, however, the extent to which function constrains representation remains unclear. One key obstacle is that these networks admit parameter symmetries: changes in parameterization that preserve function exactly while reshaping representational geometry. Here, we show that a broad class of parameter symmetries acts on representations through just three primitive feature transformations: addition, duplication, and scaling. This feature-level characterization yields a closed-form decomposition of representational geometry into essential and auxiliary components, which makes precise how degeneracy in representational geometry can grow with overparameterization even when function is held fixed. Finally, we show that implementation-level selection rules can resolve this degeneracy, yielding identifiable geometries in which features are weighted according to their contributions to the network's function. Together, our results delineate when representations can support inferences about computation, and when they cannot.

---


### 166. [Shared Phase and Retention Control for Efficient Adaptive Spectral Recurrence](https://arxiv.org/abs/2609.39082)

**<font color=#1a73e8>作者：</font>** Wentao Wang, Hengyu Zhong, Yunhan Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As new evidence arrives, a sequence model must update what it remembers and how memory influences predictions. While Transformers incur computation and cache costs scaling with context length, fixed-state recurrent models offer constant-memory inference. However, linear and spectral recurrences traditionally rely on static transitions, failing to dynamically revise how stored representations decay or rotate. While recent selective architectures introduce input-dependent transitions, they assign independent controls to every memory mode, coupling control cost to state capacity. We show that high-dimensional spectral memory does not require high-dimensional control, and introduce Shared Phase and Retention Control for Efficient Adaptive Spectral Recurrence (SPARC). SPARC employs just two input-dependent scalar signals to coordinate memory retention and phase rotation across heterogeneous complex modes, while preserving mode-specific baseline timescales and frequencies. Its diagonal affine recurrence supports parallel associative scans for sequence-level BPTT as well as exact structured Real-Time Recurrent Learning (RTRL) for online credit assignment. Across partially observable continuous control, POPGym, and sequence classification, SPARC achieves a 9.09% relative return improvement on Walker-P and a 1.36% relative accuracy gain on FordA over second-best methods. On an NVIDIA Blackwell GPU, our implementation reduces recurrent-mixer training latency by 18.2%-34.2% in fixed-token workloads and accelerates scans by 3.1x-4.7x over an optimized RG-LRU baseline. These results show that two shared control signals can efficiently govern adaptive spectral memory across online and full-sequence settings. Code is available at this https URL.

---


### 167. [MRI Super-Resolution with RCDM/WaveMix and Task-Aware Segmentation](https://arxiv.org/abs/2609.39083)

**<font color=#1a73e8>作者：</font>** Kavitha Viswanathan, Harsh Choudhary, Amit Sethi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Super-resolution and quality enhancement of 1.5\,T brain MRI are normally validated with image-fidelity metrics, although their purpose is to improve downstream analysis. We study whether enhancement improves tissue segmentation, and for which segmenters. We propose an unpaired, physics-guided training pipeline for a lightweight ($\le$2.5\,M parameter) recurrent convolutional enhancer: a six-module stochastic 1.5\,T degradation operator, a residual adversarial network that adds scanner-specific texture without moving anatomy, and a cycle-consistent objective with an anti-identity penalty that rules out the copy solution. We then train U-Net, Swin-UNet and wavelet token-mixing segmenters \citep{jeevan2023wavemix} from scratch on either raw or enhanced 1.5\,T images of the same subjects, using identical labels and subject-level splits, for three enhancer variants and two datasets. On ABIDE (41 held-out subjects, FreeSurfer labels) enhancement significantly improves the wavelet segmenter (mean Dice $+0.014$, Wilcoxon $p=3.5\times10^{-5}$; CSF $+0.018$, grey matter $+0.013$), significantly degrades the U-Net ($-0.008$, $p=5.1\times10^{-4}$) and leaves Swin-UNet unchanged. On IXI, whose labels come from FSL-FAST, enhancement lowers Dice for all nine pairings, almost entirely through CSF; we trace this to spatially implausible CSF voxels in the labels that penalise smoother predictions. Enhancement of low-field MRI should therefore be validated per downstream model and against reliable labels.

---


### 168. [UGOD: Uncertainty-Guided Opacity and Dropout for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2609.39089)

**<font color=#1a73e8>作者：</font>** Zhihao Guo, Peng Wang, Zidong Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-view 3D Gaussian Splatting is prone to overfitting because limited observations leave many Gaussian primitives weakly constrained, yet their contributions are still accumulated through alpha blending. Without uncertainty estimation, the renderer cannot distinguish unreliable primitives from well-constrained ones, allowing their erroneous contributions to corrupt novel-view synthesis. We introduce UGOD, an uncertainty-guided framework that estimates a view-dependent uncertainty score for each Gaussian and uses it to regulate its rendering contribution. A lightweight uncertainty head conditioned on Gaussian attributes and viewing direction predicts this score, which then drives a differentiable opacity-modulation mechanism that attenuates high-uncertainty primitives before compositing. During training, a detached soft-dropout branch applies an uncertainty-controlled continuous keep mask to discourage the model from relying on poorly constrained Gaussians and thereby reduce overfitting. Crucially, detaching the uncertainty score prevents gradients from this stochastic regulariser from biasing or collapsing the uncertainty prediction. Experiments on Mip-NeRF~360 and LLFF show that UGOD improves sparse-view novel-view synthesis while producing more compact Gaussian representations than the compared methods. These results demonstrate that Gaussian uncertainty provides an effective rendering-time control for sparse-view reconstruction.

---


### 169. [Learning Infinite-Horizon Average-Reward CMDPs via State Augmentation](https://arxiv.org/abs/2609.39093)

**<font color=#1a73e8>作者：</font>** Kihyun Yu, Seoungbin Bae, Dabeen Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study infinite-horizon average-reward constrained Markov decision processes (CMDPs) under the weakly communicating assumption. Existing high-probability guarantees for this setting either require computationally inefficient algorithms or have suboptimal dependence on the number of interactions $T$. We propose, to the best of our knowledge, the first computationally efficient algorithm that achieves $\widetilde{\mathcal{O}}(\sqrt{T})$ regret and cumulative constraint violation with high probability in the tabular setting. The $\sqrt{T}$ dependence is optimal up to logarithmic factors. Our approach incorporates cumulative constraint violation into the state and defines a reshaped reward through differences of a Huber potential. The added state determines the penalty on further violations while the reward function remains fixed on the augmented state space. Since the added state has known deterministic dynamics, only the original transition kernel needs to be estimated. The bounded slope of the Huber potential keeps the per-step reward bounded, and the potential differences telescope to relate the reshaped return to the original cumulative reward and the terminal potential. These properties allow us to apply finite-horizon approximation and optimistic value iteration with clipping, as used in unconstrained average-reward MDPs, without worsening the regret rate in $T$.

---


### 170. [A Generalisation Signal Need Not Be a Model-Selection Signal](https://arxiv.org/abs/2609.39099)

**<font color=#1a73e8>作者：</font>** Aditya Nagarsekar, M P Ashish Bhat, Aadi Nesarkar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model selection in computational biology often relies on validation data drawn from the training regime, even when deployment lies outside it. When validation no longer preserves which model is best, a natural alternative is to rank candidates using properties of the trained network itself. We test this idea using a novel, forward-only proxy motivated by the norm of the Hessian, alongside common Hessian measures, across molecular property, protein fitness, and drug-response tasks. Contrary to our hypothesis, geometry does not become more useful as validation Spearman correlation deteriorates: augmenting validation helps some shifts but significantly harms others. More surprisingly, the proxy still correlates with generalisation gap on most tasks even when Hessian trace and top-eigenvalue relationships are weak or reversed, yet this signal does not reliably identify the deployment-best model. A curvature bound need not preserve cross-model rankings, and low geometric scores can even favour collapsed predictors. Thus, a generalisation signal need not be a model-selection signal.

---


### 171. [Reserve-Aware Contrast Certificates for Conservative Bandits with Uncertain Baselines](https://arxiv.org/abs/2609.39106)

**<font color=#1a73e8>作者：</font>** Qinchuan Cheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conservative bandits must improve an incumbent policy without exhausting a prescribed performance budget. When the incumbent is uncertain, separately bounding candidate and baseline rewards can charge twice for shared estimation error. We develop Reserve-C4B around the baseline-relative contrast itself. A shared confidence set yields an exact expression for this avoidable penalty and a tighter admissibility test at every fixed history. A reserve ledger separates statistical evidence from permitted performance deficit; a prefix-refresh extension recertifies accumulated decisions under the current confidence set without discarding previously certified credit. For linear rewards, self-normalized confidence sets provide simultaneous validity over time and adaptively generated candidates, and the resulting policy satisfies a conditional-mean performance constraint with high probability. Reproducible experiments isolate certificate coupling, prefix refresh, and historical information, showing large reductions in baseline fallback while exposing the limitations of frozen certificates.

---


### 172. [Bongard: Training Machine Intuition](https://arxiv.org/abs/2609.39111)

**<font color=#1a73e8>作者：</font>** Li Ding, Haidi Jin, Chen Ji  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human intelligence relies heavily on learned intuition: recognising patterns and judging situations without explicitly unfolding every intermediate step. We introduce Bongard, an open-weight System One model that treats machine intuition as an independent capability to design and train. A T5Gemma 2 4B-4B encoder-decoder separates reading the evidence from making judgments. The encoder reads the state bidirectionally together with the question instructions, and separate decoder branches share this encoding, so many judgments about the same situation require only one reading of the state. A trained head returns probabilities over the supplied candidates without generating text. Training proceeds in three stages, from supervised judgments to semantic relationships to action outcomes, and each stage updates all 7.09 billion trainable parameters on one Blackwell GPU. Joint-embedding post-training raises accuracy on held-out rephrasings from 75.7% to 85.9%. A sandbox stage then learns outcome distributions from action rollouts and exact oracles, raising accuracy on a frozen sandbox panel from 50.6% to 64.8%. On DecisionBench, the final model reaches 78.05% accuracy over 23,900 decisions and ranks fourth of 61 systems in the public comparison. On one RTX PRO 6000, its median latency is 36 ms for short requests, and 32 questions about one state take 221 ms. Bongard demonstrates that machine intuition can be systematically trained via representation learning and outcome feedback, providing an open, efficient alternative for high-throughput decision workloads.

---


### 173. [Beyond Local Linearity: Scale-Resolved Geometry of Learned Image Encoders](https://arxiv.org/abs/2609.39115)

**<font color=#1a73e8>作者：</font>** Jakub Szymkowiak, Wojtek Pałubicki, Kamil Adamczewski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding how learned representations respond to finite input changes is important for characterizing their sensitivity, invariances, and robustness. Yet existing geometric analyses are predominantly local and describe only infinitesimal perturbations. We introduce a scale-resolved statistic that compares an encoder's measured feature displacement with its local linear prediction as the perturbation magnitude increases. Across diverse image encoders, we discover a characteristic plateau-rise-peak-decay profile, which we call the bump. The bump is absent at initialization, emerges early during standard training, and does not form under randomized labels or random-noise inputs. Its shape also varies with the training distribution and robustness objective. These results establish departures from local geometry as a signature of how encoder representations are shaped by learning.

---


### 174. [GRC-Pose: Generation-Reconstruction Correspondence for Prior-Free 6D Object Pose Tracking](https://arxiv.org/abs/2609.39116)

**<font color=#1a73e8>作者：</font>** Shiyang Liu, Weiquan Lin, Luping Xiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prior-free 6D object pose tracking seeks to recover the trajectory of an unseen object from a single RGB video without object-specific CAD models, posed reference images, or pose annotations. Geometric foundation models provide complementary object-centric and scene-centric cues, yet SAM3D CAD is indexed by an arbitrary object-local surface parameterization, whereas reconstructed evidence is expressed in a sequence-specific world frame with partial surface coverage. To exploit this complementarity, we formulate tracking as generation-reconstruction correspondence and introduce GRC-Pose, a correspondence-based framework that combines learned correspondence prediction with robust pose estimation. Concretely, GeoCorr-Matcher estimates weighted object-scene correspondences and per-match uncertainty for each pose candidate. FGH-Solver integrates these matches through multiple robust geometric estimators and sequence-level posterior inference, while a posterior-gated memory retains only inlier-supported observations through occlusion and viewpoint change. Extensive evaluation shows that with SAM3D CAD, GRC-Pose achieves state-of-the-art Average Recall and motion retention on HOT3D, improving the latter by 58% over prior art. On classical benchmarks including YCBInEOAT and LINEMOD, it remains highly competitive.

---


### 175. [Prequential E-Values for Selected-GP Near-Optimality Certificates](https://arxiv.org/abs/2609.39123)

**<font color=#1a73e8>作者：</font>** Ami Tavory, Noa Cohen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When optimizing an expensive black-box function sequentially, as in hyperparameter optimization, we may want to stop once the best evaluated value is certified within $\varepsilon$ of the global optimum. Such a certificate needs two ingredients: a lower confidence bound for the selected value and an upper confidence envelope over the domain, typically supplied by a Gaussian process (GP). GP-UCB-style stopping rules are valid when the kernel and constants defining this envelope are fixed before the run, but the practical temptation is to tune the envelope from the same adaptive evaluations and then certify as if it had been fixed. We use prequential e-values to make this selection auditable: starting from a predeclared set of fully specified GP/RKHS envelopes, each candidate is tested by its own one-step-ahead e-process, contradicted candidates are deleted, and certification uses the largest upper bound among the survivors. With a valid selected-point lower bound and one declared candidate having valid latent coverage and noise calibration, the rule is anytime-valid. On a 512-seed noisy RBF stress sweep, it roughly halves false-certification risk at comparable power versus fit-then-certify. Relative to random fixed GP precommitment on smooth $d=3,4$ objectives, each additional false certificate is accompanied by 3.0 and 13.5 additional correct certificates, respectively.

---


### 176. [CDMD: A Cross-Dataset Mixed-Type Diffusion Model for Tabular Data](https://arxiv.org/abs/2609.39124)

**<font color=#1a73e8>作者：</font>** Mohamed Amine Ketata, Maximilian Schambach, Stephan Günnemann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models for tabular data are typically trained separately for each dataset, limiting knowledge transfer and requiring the storage of many specialized models. In this paper, we introduce CDMD, a tabular diffusion model trained jointly across heterogeneous datasets with different schemas and variable numbers of numerical and categorical features. Unlike existing cross-dataset tabular diffusion models that operate in continuous representation spaces, CDMD defines diffusion directly over the mixed-type feature space and is trained end-to-end. To accommodate heterogeneous categorical domains, we introduce a schema-restricted reverse-process parameterization for masked diffusion models, in which the output space dynamically adapts to each feature's vocabulary. We then compose numerical and categorical feature-level diffusion processes into a schema-dependent row-level process. A shared schema-aware Transformer denoiser captures dependencies between features and parameterizes the reverse process across varying schemas. On seven real-world datasets, a single jointly trained CDMD achieves the highest average generation quality among strong single-dataset and cross-dataset baselines, while using substantially fewer total parameters than the collection of separately trained models. Furthermore, pre-training on a corpus of 337 datasets improves generation on previously unseen datasets under both limited target data and limited adaptation epochs. These results demonstrate the potential of direct mixed-type diffusion for shared and transferable tabular data generation. Our code is available at this https URL.

---


### 177. [How to Reduce Localization Ambiguity? Geometry-Semantic Constrained BEV Representation Learning for Satellite-Ground Localization](https://arxiv.org/abs/2609.39127)

**<font color=#1a73e8>作者：</font>** Junming Feng, Panwang Xia, Qiong Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Satellite-ground localization estimates the planar position and yaw orientation of a ground camera within a geo-referenced satellite image. Most recent methods map ground and satellite features into a shared bird's-eye-view (BEV) space and establish spatial correspondences. However, insufficient depth constraints can assign one ground feature to different distances along a viewing direction, creating geometric ambiguity in BEV feature placement. Similar appearances at different locations can also create descriptor matching ambiguity, while existing descriptor learning lacks explicit semantic supervision to distinguish them. We propose GeoSem-BEV, a geometry-semantic constrained BEV representation learning method. Radial depth supervision constrains distance assignment, and vertical height supervision constrains height aggregation. Shared explicit semantic supervision promotes consistent semantic predictions across views and helps distinguish locations with similar semantics. These constraints improve feature placement and descriptor discriminability, enhancing state-of-the-art BEV localization models. On VIGOR with unknown orientation, GeoSem-BEV reduces mean orientation error by 37.2% and 38.1% in the cross-area and same-area settings, respectively. The corresponding errors are reduced by 10.8% and 15.6% on DReSS-D. On KITTI-CVL, it reduces same-area mean orientation error by 26.8% under 10 degree orientation noise.

---


### 178. [GeoGAT: Bidirectional Temporal Sampling Meets Hierarchical Graph Attention for Global Video Geo-localization](https://arxiv.org/abs/2609.39128)

**<font color=#1a73e8>作者：</font>** Junchao Cui, Xuanzi Ma, Wenqi Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Global video geo-localization aims to infer the geographic location of a video worldwide, evaluating performance across four geographic hierarchies: city, state/province, country, and continent. Existing methods typically employ one-way uniform sampling to process video frames and train independent classifiers for each hierarchy, which leads to the loss of key geographic cues and prediction conflicts between hierarchies, especially for complex multi-shot edited videos. To address these limitations, we propose GeoGAT, which integrates bidirectional temporal sampling with graph attention networks (GATs). Specifically, GeoGAT extracts forward and offset-reversed frame sequences to construct complementary spatiotemporal features. These fused features are then fed into a predefined geographical hierarchy graph, where GATs perform structure-aware message passing, while a dual-constraint mechanism prunes predictions to eliminate cross-hierarchy conflicts. We construct GeoGAT10k, comprising 9,720 multi-shot edited videos from 166 cities worldwide, specifically to benchmark generalization ability on complex video structures. Experimental results on CityGuessr68k and GeoGAT10k demonstrate that GeoGAT eliminates hierarchical conflicts entirely and achieves state-of-the-art performance across all four geographic hierarchies. On CityGuessr68k, GeoGAT outperforms the strongest baseline, evaluated under both classification and retrieval protocols, by 2.6 percentage points at the city level. On the more challenging GeoGAT10k with multi-shot edited videos, the accuracy improvement exceeds 24 percentage points, validating strong generalization to complex real-world scenarios.

---


### 179. [Perceptual Color Difference Modeling Using Machine Learning and Human Similarity Judgments](https://arxiv.org/abs/2609.39130)

**<font color=#1a73e8>作者：</font>** Elnara Kadyrgali, Muragul Muratbekova, Adilet Yerkin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate assessment of color differences is essential for applications ranging from digital design to quality control. While existing color difference metrics, such as CIEDE2000, aim to approximate human perception, they may still exhibit inconsistencies with perceptual judgments. In this study, we investigate a data-driven approach to color-difference estimation based directly on human evaluations. We collect similarity judgments for 2,000 systematically generated color pairs, each rated by seven observers using a four-point ordinal scale. These judgments are then used to train regression models using different color representations, including RGB channel differences, HSI differences, and COLIBRI fuzzy linguistic categories. Experiments with five regression algorithms show that the choice of color model has a greater influence on prediction performance than the choice of regression algorithm. Using COLIBRI features alone, linear regression achieves an R2 of 0.595, outperforming RGB and HSI representations, which achieve R2 values of 0.479 and 0.493, respectively. The best performance is obtained by LightGBM using the combined representation, reaching an R2 of 0.703. The results indicate that human perceptual color differences are better captured when numerical color coordinates are complemented by graded perceptual categories, highlighting the potential of data-driven models for perceptually aligned color-difference estimation.

---


### 180. [Uncertainty-Aware Consistency Distillation for Few-Step Video Generation](https://arxiv.org/abs/2609.39132)

**<font color=#1a73e8>作者：</font>** Lingyu Liu, Yaxiong Wang, Li Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study few-step video generation, i.e., distilling a multi-step video generator, which typically requires tens of sampling steps, incurring substantial latency and compute, into a few-step student. Consistency distillation is a common recipe, in which a multi-step teacher provides the consistency targets for a few-step student. However, these teacher-guided targets are not equally trustworthy, and the content is harder to learn where it varies rapidly over time, e.g., moving foliage shadows or flowing water. We observe that supervision reliability follows the local difficulty of the content rather than semantic complexity: regions that change little yield consistent endpoint predictions, whereas regions with large temporal variation produce larger discrepancies that coincide with the largest perceptual errors. Motivated by this observation, we propose Uncertainty-Aware Consistency Distillation (UACD), which reweights consistency supervision at each spatiotemporal region using a local, parameter-free uncertainty estimate. Specifically, we construct two independently perturbed teacher-guided consistency paths, whose student endpoint predictions provide a consensus target; the discrepancy between the student's direct prediction and this target is the uncertainty proxy. We then relax the consistency penalty on high-uncertainty regions through an exponential weight, while keeping the full penalty elsewhere, since the student cannot be expected to match targets that are hard to learn. To preserve perceptual quality under aggressive step reduction, we integrate feature-space adversarial training with semantic alignment. With parameter-efficient LoRA adaptation of the 50-step Wan model, our method achieves state-of-the-art 4-step generation on VBench 2.0 (0.556 mean score) and is preferred over competing methods in a user study.

---


### 181. [RefCon: Iterative Refinement and Contrastive Memory Extraction for Context-Evolving Agent](https://arxiv.org/abs/2609.39143)

**<font color=#1a73e8>作者：</font>** Ubaidillah Ariq Prathama, Bo Liu, Yeo Boon Hong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agent interactions generate useful but noisy experience, and retraining models to absorb it is expensive. Context-evolving agents therefore need memory extraction methods that improve with more test-time compute without relying on gold labels. We propose RefCon, which combines sequential self-refinement with parallel self-contrast to extract higher-quality memories without gold labels. Evaluated on AppWorld and BFCL-V3 across multiple context-evolving agent frameworks, RefCon delivers strong and consistent gains, including relative improvements of 21.6% on ACE and 16.6% on ReMe over no-scaling baselines, while a diversity-focused variant (DivCon) achieves a 35.5% gain on ReasoningBank. RefCon consistently outperforms existing baselines without ground-truth labels, and generalizes across model scales and to software engineering tasks, where it surpasses even ground-truth baselines. We further analyze the accuracy-token trade-off and scaling behavior, showing RefCon maintains favorable efficiency and continues to improve as more trajectories are used, unlike diversity-only scaling which saturates earlier.

---


### 182. [Sharp Stationary Gaussian Approximation for Constant-Stepsize SGD](https://arxiv.org/abs/2609.39144)

**<font color=#1a73e8>作者：</font>** Junghoon Seo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove a sharp Gaussian approximation for the invariant law of constant-stepsize SGD with bounded additive noise generated by an exogenous uniformly ergodic Markov chain. For a smooth, strongly convex objective with a Lipschitz Hessian and nondegenerate long-run noise covariance, the centered iterate normalized by the square root of the stepsize is $O(\sqrt{\alpha})$-close in 1-Wasserstein distance to its limiting Gaussian. The proof combines blockwise Gaussian comparison with long-run contraction. A four-state example gives a matching lower bound although the one-time noise marginal is symmetric and every nonzero-lag autocovariance vanishes. In this example, an adjacent third-order mixed moment produces the leading correction.

---


### 183. [MindWorldBench: Evaluating Mental-State-to-Behavior Reasoning in Image-to-Video Generation](https://arxiv.org/abs/2609.39147)

**<font color=#1a73e8>作者：</font>** Ruiqi Li, Xuanyi Liu, Sijia Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current image-to-video models achieve visual realism and physical plausibility, but reasoning about mental states remains unexplored. Actions are driven by belief, desire, and perception, requiring inference beyond explicit instructions. We introduce MindWorldBench to evaluate mental-state-conditioned video generation. We formalize this as mental-state-to-behavior reasoning, where models generate actions from a world state and latent variables without explicit action prompts. MindWorldBench utilizes Zero-Action Prompting and a counterfactual design with 744 prompts to isolate the causal effects of mental states. An automated pipeline evaluates video quality, commonsense plausibility, and mental-state consistency. Evaluations of 11 models show that despite visual fidelity and physical reasoning, models fail to align behaviors with latent mental states. We identify a failure mode, termed Omniscient Bias, where models default to the objective world state rather than human's subjective belief. These results demonstrate a disconnect between visual generation and cognitive reasoning, suggesting a need for explicit mental-state modeling in video generation systems. Project website: this https URL

---


### 184. [TripleFlow: Training-Free Video Object Removal by Bridging Residual Editing and Native Generation](https://arxiv.org/abs/2609.39157)

**<font color=#1a73e8>作者：</font>** Songhe Wang, Lifu Wei, Shuolin Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video object removal presents a uniquely difficult editing challenge. Because a removal prompt specifies only what to erase rather than what to generate, the model must infer and reconstruct a highly specific occluded background entirely from the surrounding context. Existing training-free methods struggle with this because their editing mechanisms act primarily as localized erasers. They fail to actively synthesize the missing background details and often leave behind ghosting artifacts. To solve this, we propose TripleFlow, a training-free framework that tightly couples erasure and generation. It coordinates a source flow, a residual flow, and a synthesis flow throughout the entire process. By reusing a single target prediction, the residual flow isolates and suppresses the object, while the synthesis flow independently reconstructs the occluded background. Crucially, TripleFlow injects this newly synthesized background back into the editing trajectory at every step. This continuous feedback loop ensures that the generated structures actively guide the removal process, achieving seamless completion that is spatiotemporally consistent with the unedited scene. Extensive evaluations across five challenging benchmarks demonstrate that TripleFlow establishes a new state-of-the-art, significantly outperforming existing baselines in both reconstruction fidelity and temporal consistency.

---


### 185. [QuanVI: Score-based Variational Inference via Quantum Maximally Mixed States](https://arxiv.org/abs/2609.39164)

**<font color=#1a73e8>作者：</font>** Yuchen Cong, Zerui Tao, Chao Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Score-based variational inference (VI) provides an alternative to Kullback--Leibler (KL)-based VI by minimizing the Fisher divergence between the variational distribution and the target. A prior score-VI approach formulates this optimization as an eigenvalue problem, with the variational distribution constructed from low-energy eigenstates. However, this eigenvalue-based formulation faces two high-dimensional obstacles: an intractably large parameter count due to exponential scaling and non-uniqueness of individual eigenvectors in degenerate or nearly degenerate low-energy subspaces. We propose QuanVI, a scalable quantum-inspired algorithm that combines a mixed-state density-operator formulation with a quantum tensor network (QTN) parameterization using the matrix product operator (MPO) structure. In degenerate low-energy subspaces, the density-operator formulation represents the subspace by its maximally mixed state rather than relying on a non-unique individual eigenvector, while the QTN parameterization compresses the density operator to avoid exponential parameter growth. Experiments and ablations show that QuanVI agrees with exact solutions in low dimensions and scales to high-dimensional synthetic and Bayesian posterior-approximation benchmarks, including challenging non-Gaussian targets.

---


### 186. [Beyond the Remembered World: Predictive 4D Belief for Persistent Navigation in Evolving Worlds](https://arxiv.org/abs/2609.39166)

**<font color=#1a73e8>作者：</font>** Mingjian Gao, Zhaocheng Li, Haoyang Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent spatial memory enables embodied agents to navigate familiar environments across repeated visits. However, targets may move while unobserved, including during navigation, making remembered locations unreliable by the time an agent arrives. Despite advances in memory retrieval and state prediction, accounting for continued hidden world evolution and revising beliefs under limited visibility remain challenging. We study Evolving-World Navigation, where agents infer target locations from intermittent observations, predict their states at inspection time, and revise beliefs using visual evidence. We propose EvolvingNav, which constructs a time-indexed belief from timestamped 3D object histories through a structured persistence-relocation model. The belief distinguishes persistence at the last observed location from relocation to alternative locations and retains probability mass outside the known candidate set. An event-driven filter propagates the current belief as time elapses, forecasts target occupancy at candidate inspection times, and incorporates new RGB-D evidence. Negative observations downweight location hypotheses according to calibrated, visibility-conditioned detection probabilities, while evidence tracking prevents repeated use of the same observations. A frozen, zero-shot vision-language controller uses the updated belief to choose actions and replan. We further introduce EvoWorld-Bench, a benchmark grounded in human activity traces, comprising 54 scenes and 803,680 tasks with controlled changes before and during navigation. In simulation and real-robot experiments, EvolvingNav improves navigation success and search efficiency over the evaluated baselines. Paired experiments show the clearest gains under learnable temporal patterns, while ablations demonstrate the value of preserving uncertainty and incorporating visibility-aware evidence.

---


### 187. [Whitening Improves Robustness to Spurious Correlations in Linear Probes](https://arxiv.org/abs/2609.39177)

**<font color=#1a73e8>作者：</font>** Floris Holstege, Bram Wouters, Noud van Giersbergen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks tend to rely on simple features that may be spurious and thus fail to generalize. We study this problem in the setting of linear probes, where a (generalized) linear model is fitted on the representations of a (pretrained) model. We use the connection of these models to the max-margin classifier, and show they favor directions associated with large eigenvalues of the covariance matrix. Whitening removes this preference by equalizing the eigenvalues of the covariance matrix. This observation motivates whitening as a preprocessing step that can reduce reliance on spurious correlations without requiring prior knowledge of their presence or labeled data. We examine the effect of whitening on a synthetic data-generating process and standard spurious correlation benchmarks, and find that it improves robustness. We also find that whitening can improve robustness when added to existing approaches.

---


### 188. [MEND: Label-Free Detection, Localisation, and Correction of Latent Hallucination in World Models](https://arxiv.org/abs/2609.39182)

**<font color=#1a73e8>作者：</font>** Ali J Alrasheed, Aryan Yazdan Parast, Basim Azam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Models are appearing as the next major frontier in computer vision. However, their robustness is currently largely unexplored. We identify the phenomenon of hallucination in latent World Models: given a state and an action, the predicted next latent can decode to a scene that never occurs. Because the prediction is statistically ordinary and is fed back autoregressively by the model, the error is both silent and compounding. We study whether such latent hallucination can be detected, localised, and corrected at inference time, on a frozen self-supervised world model in the absence of ground-truth error labels. We introduce Masked Empirical-Bayes Neural Denoising (MEND), a single conditional score network trained by denoising score matching on real transitions, whose score field serves three roles: its magnitude detects hallucination, its per-token field localises it to specific image patches, and it defines an inference-time correction direction. On two navigation environments MEND detects hallucination with an AUROC of up to 0.80 without using actions, exceeding a single-Gaussian density baseline while also localising the error (per-token AUPRC up to 0.87) and correcting it, all from one score field. Our correction reliably reduces single-step latent error and improves predictions. We identify that a part of the error is tangent to the data manifold, hence, we focus on detection and localisation while highlighting promises of the correction.

---


### 189. [Fiber-Resolved Microstructure Quantification from Multi-Shell Diffusion MRI using Detection Transformers](https://arxiv.org/abs/2609.39184)

**<font color=#1a73e8>作者：</font>** Sebastian Endt, Marcus Wirth, Johannes Reinhold Schlund 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fiber orientation and compartmental microstructure are central to the characterization of white matter tissue in diffusion MRI, yet existing methods either resolve fiber orientations without quantifying microstructure, or quantify microstructure while assuming a fixed number of compartments and a single fiber direction. Nonparametric approaches that recover both require tensor-valued diffusion encoding and computationally expensive Monte-Carlo inversion of an ill-posed inverse Laplace transform. We propose to reframe this problem as an object detection-like task, adopting the Detection Transformer (DETR) architecture to jointly predict mean diffusivity (MD), fractional anisotropy (FA), main fiber direction, and signal fraction for a variable number of compartments per voxel from standard multi-shell diffusion MRI with linear encoding. Hungarian matching during training resolves permutation invariance across compartments. We introduce mean Average Precision as a reproducible benchmark metric. Evaluated on synthetic test data with up to five compartments per voxel, our model achieves $R^2=0.95$ for MD, $R^2=0.88$ for FA, and a median angular error of 4.2°, with performance scaling naturally with compartmental signal fraction.

---


### 190. [Dynamics to decision: A mathematical theory of Lyapunov spectra and decision boundaries in deep classifiers](https://arxiv.org/abs/2609.39190)

**<font color=#1a73e8>作者：</font>** Shirin Panahi, Amirhossein Nazerian, Ali Pezeshki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A deep classifier is defined not only by the decision it produces, but also by the sequence of transformations through which that decision is formed. Treating this evolution as a dynamical system across layers provides a natural framework for asking how decision geometry emerges through depth and how far back we can trace a boundary's dynamical signature. We model a feed-forward classifier as a finite, nonautonomous discrete dynamical system, with layers playing the role of discrete time steps. We study the Finite-Time Maximum Lyapunov Exponent (FTMLE) of the data samples' dynamical trajectory through depths of the classifier. The FTMLE measures the rate of convergence/divergence of nearby trajectories. We move the observation endpoint backward from probabilities to logits and then to hidden representations. For Gaussian classes, we prove that probability-level FTMLE carries a clear geometric signature of the decision boundary, with its dominant direction aligned with the boundary normal. Moving one step backward to the logits, we prove this relationship is no longer universal but depends critically on how the classifier is trained, particularly on the choice of loss function. Moving further backward to the hidden representation, the connection becomes more conditional: boundary-related FTMLE can persist, but only under identifiable structural conditions. We propose geometry-aware fine-tuning for restructuring the classifier's hidden FTMLE, and propose conditions for guaranteed concentration of high hidden FTMLE near the decision boundary. Through our numerical results, we show the generality and validity of our theoretical results. Understanding the evolution of data samples as traveling through the layers of classifier provides a principled foundation for identifying where boundary-relevant sensitivity emerges and for developing layer-aware regularization strategies.

---


### 191. [Importance-Aware Feature Sparsification for Wireless Split Learning](https://arxiv.org/abs/2609.39194)

**<font color=#1a73e8>作者：</font>** Bumjun Kim, Yoon Huh, Wan Choi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wireless split learning (SL) reduces on-device computation by offloading upper layers to a server, yet transmitting high-dimensional intermediate features at each iteration remains a major communication bottleneck. Existing methods select features at the client side using task-agnostic criteria such as magnitude, statistics, or clustering, which increases client-side processing and often degrades accuracy under non-independent and identically distributed (non-i.i.d.) client data. We propose importance-aware class-balanced sparsification (ICS), a lightweight approach in which the server ranks feature channels using Grad-CAM-based scores obtained from the true-class logit during backpropagation. The per-class scores are aggregated into a class-balanced, label-agnostic importance vector that mitigates head-class bias under label skew, and each client reuses this vector in the next round to retain the top-$N$ feature channels, incurring no additional client-side forward or backward passes. We further derive a non-asymptotic convergence bound that isolates the sparsification-induced error and characterizes how the sparsification ratio and mini-batch size jointly affect convergence under a fixed communication budget, and we analyze the communication and computational overhead of ICS against representative baselines. Beyond sequential CNN-based SL, we extend ICS to parallel split learning and to transformer-based models. Experiments show that ICS consistently outperforms the baselines, with larger gains under severe non-i.i.d. partitions.

---


### 192. [In a Streaming World, Should You Stand Still? A Comprehensive Benchmark of Anomaly Detection in Streams](https://arxiv.org/abs/2609.39215)

**<font color=#1a73e8>作者：</font>** Magali Parrino, Antoine Ajenjo, Emmanuel Remy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series anomaly detection (TSAD) is increasingly deployed in streaming settings, where data arrive sequentially and may exhibit non-stationarity. As a result, several works from the recent literature propose streaming anomaly detection methods that rely on incremental updates to adapt over time. However, most of these approaches originate from the streaming outlier detection literature and largely ignore core characteristics of time series anomalies. Moreover, their empirical evaluation is typically conducted on synthetic or small-scale benchmarks with limited diversity, making it unclear whether streaming methods are truly advantageous in realistic TSAD scenarios. In this work, we carry out the first large-scale experimental study comparing streaming and static TSAD methods under a unified streaming evaluation benchmark. We consider a realistic setting in which an initial batch of data is available for model training, followed by online evaluation of both detection accuracy and computational efficiency. In addition, we propose a distribution-drift dataset of real time series, called TSB- drift, to isolate scenarios where streaming updates are theoretically justified. Our results show that, contrary to common assumptions, static TSAD methods significantly outperform streaming approaches in most streaming settings. Such finding highlights a critical gap between the design of existing streaming methods and the requirements of modern TSAD, and calls for a rethinking of how streaming capabilities should be integrated into TSAD.

---


### 193. [DC-SAE: Deep Compression Semantic Autoencoder for Faster Diffusion Convergence](https://arxiv.org/abs/2609.39222)

**<font color=#1a73e8>作者：</font>** Xu Huang, Ye Huang, Zijun Liao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-compression tokenizers are essential for scaling latent image generative models. However, aggressive compression creates a fundamental tradeoff between reconstruction fidelity and generation efficiency: high compression image encoder always increases the learning difficulty of diffusion training, resulting in slow model convergence. Recent representation autoencoders speed up the diffusion training by improving the latent feature's expressive capability by replacing VAE encoders with pretrained semantic encoders, yet they are typically limited to moderate compression and lose pixel-level details necessary for faithful reconstruction. To achieve both high compression and fast diffusion training, we propose DC-SAE, a Decoupled Compact Semantic Autoencoder designed for high-compression image generation with accelerated diffusion model convergence. DC-SAE consists of two key components: (1) a macro-level architecture design that leverages semantic encoders to enable higher compression ratios, and (2) a pixel-level encoder that preserves low-level details, ensuring high-fidelity image reconstruction. We empirically demonstrate that DC-SAE performs strongly on image generation tasks, achieving both compact latent representations and efficient training dynamics. Specifically, on the ImageNet dataset with $512 \times 512$ resolution, DC-SAE achieves $32\times$ spatial compression, with 29.79 PSNR and 3.37 gFID, substantially outperforming the previous state-of-the-art high-compression tokenizer baselines DC-AE by 13.5% and 54.9% on PSNR and gFID, respectively, maintaining comparable throughput and faster diffusion model training convergence. Beyond class-conditional generation, a $1.6$B-parameter DiT using DC-SAE achieves 0.84 on GenEval and 86.007 on DPG-Bench for text-to-image generation at $1024\times1024$ resolution.

---


### 194. [Emergent Multi-View Geometry Through Self-Distillation](https://arxiv.org/abs/2609.39227)

**<font color=#1a73e8>作者：</font>** David Nordström, Thibaut Loiseau, Vincent Lepetit 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Over a century ago, Henri Poincaré argued that a motionless observer cannot acquire the notion of space. Yet, most visual representation learning methods operate on individual images, while those that leverage multiple views rely on RGB reconstruction, entangling geometry with appearance. We propose Poincar3, a self-supervised method that learns representations from multiple views through self-distillation instead of RGB reconstruction. We combine masked patch and image-level distillation with a teacher that observes additional views, enabling training from scratch without explicit 3D supervision. Poincar3 outperforms both previous single and multi-view self-supervised approaches such as DINOv3, MuM, and Muskie on correspondence estimation, camera pose estimation, and 3D reconstruction. Using a lightweight Poincaré adapter, we also find that our learned features encode camera motion more accurately than existing self-supervised representations.

---


### 195. [What Streaming Anomaly Detection Finds (and Misses) in Industrial Time Series](https://arxiv.org/abs/2609.39232)

**<font color=#1a73e8>作者：</font>** Magali Parrino, Antoine Ajenjo, Emmanuel Remy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EDF relies on continuous monitoring of its power plants to detect anomalies as soon as they occur. Given the absence of a universally optimal streaming method in unsupervised settings, we compare streaming methods with state-of-the-art TSAD models deployed online on a real nuclear power plant dataset. This work also evaluates Automated Anomaly Detection in a streaming context. Results show higher consistency for online TSAD and strong robustness from ensembling strategies.

---


### 196. [MultiTable: A Faster Hash Table at any Physical Load Factor up to and Including One](https://arxiv.org/abs/2609.39233)

**<font color=#1a73e8>作者：</font>** Maksym Petkus  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present \emph{multitable} and its Rust reference implementation: a stable hash table both materially faster at equal physical memory and more flexible than the SwissTable in its Rust's hashbrown implementation. As an arithmetic mean over 84 configurations it delivers $\mathbf{2.1\times}$ hashbrown's throughput when both hash the same raw bytes and $\mathbf{1.9\times}$ when hashbrown is keyed on native integers, its best case; on negative lookups alone, $3.2\times$ and $2.9\times$.
Multitable reaches \textbf{any physical load factor} up to and \textbf{including one} ($0.9999$ demonstrated), exactly for the requested capacity, compared to hashbrown which doubles at $0.777$ for 4-byte keys and values. At $75\%$ saturation of hashbrown (assumed average case of its rigid ladder) and multitable sized to $0.97$ physical load factor, hashbrown takes $66\%$ more space. The lookup probe count has no cliff as the load factor approaches one. Bucket size, physical load factor, and failure budget are parameters, and the multitable can be grown without rehashing.
We implement two variants of multitable: plain and filtered. At equal physical memory on an Apple M2 Pro the filtered multitable leads hashbrown in all $84$ insert, hit, and miss configurations. Multitable is more \textbf{memory-efficient}, at equal mixed-lookup throughput on the map of $4$-byte keys and values the filtered multitable needs up to $12\%$ fewer bytes than hashbrown, and the plain multitable is $18\%$ smaller, holding $\mathbf{22\%}$ more keys in the same memory.

---


### 197. [A differentiability framework for zigzag persistent homology via linear interpolation](https://arxiv.org/abs/2609.39242)

**<font color=#1a73e8>作者：</font>** Enrico Maria Ferrari, Clemens Bannwart, Matteo Biagetti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Persistent homology can be differentiated and incorporated into learning pipelines, but no analogous framework exists for zigzag persistence, which is needed when the underlying topological structure evolves non-monotonically over time. We develop such a framework for sequences of simplicial complexes obtained by thresholding time-dependent filtering values on a fixed complex. By assigning persistence diagram endpoints the real-valued times at which linearly interpolated filtering values cross the threshold, we transfer the continuity of the filtering values to the diagram points. This yields smooth local lifts of the resulting persistence-diagram-valued map, from which we derive differentials almost everywhere under mild regularity conditions on the parametrization of the filtering values. We prove local Lipschitz continuity outside an explicit measure-zero exclusion set; standard stochastic subgradient convergence guarantees therefore do not apply directly. We argue that, even without such guarantees, this exclusion set is small enough in practice to allow effective optimization. We test this empirically in two experiments: sensor network coverage optimization and dynamic graph classification.

---


### 198. [Client and Training Data Selection for Computationally Efficient Synchronized Federated Learning](https://arxiv.org/abs/2609.39250)

**<font color=#1a73e8>作者：</font>** Muzaffer Citir, Hiroki Nishikawa, Sangyoung Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is a promising paradigm of machine learning, which preserves user privacy by enabling learning without sharing raw data with a cloud server. Straggling clients have been a problem for FL as they introduce delays in aggregating the local models and hence, the convergence of the global model. Therefore, it is important to have a mechanism that ensures fast convergence of the global model as well as good FL participation rate. Another issue for the convergence of a model in FL is the non-independent and identically distributed (non-iid) data across the clients. Prior approaches based on probabilistic client selection do not work well under non-iid data especially when the number of clients is small. We show scenarios where such approaches fail and propose a joint client-training data selection algorithm for fast convergence of FL models. Our experiments on CIFAR-100 dataset show that convergence of the FL model can be significantly improved over prior works that can consider non-iid data and heterogeneous computation and higher model accuracy.

---


### 199. [From Benchmarks to Production: Transferring Time Series Anomaly Detection Methods for Electricity Production Monitoring](https://arxiv.org/abs/2609.39257)

**<font color=#1a73e8>作者：</font>** Nicolas Vautier, Paul Caron, Nardi Xhepi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate forecasting of electricity production is essential for maintaining the operational efficiency and strategic planning of energy utilities. In industrial settings, such forecasts are generated daily to ensure supply-demand balance and optimal management of production assets. However, the increasing complexity of modern power systems and data flows poses significant challenges for ensuring the reliability and consistency of these forecasts. This paper addresses the problem of anomaly detection in short-term production forecasts at EDF, formulated as identifying atypical intra-day patterns that may signal data quality issues or operational irregularities. We introduce TAMIS, a scalable and interpretable system that analyzes daily production time series to automatically detect anomalous days based on deviations from historical patterns learned from past data. Designed for human-in-the-loop workflows, TAMIS surfaces top-ranked anomalies through an automated daily newsletter, enabling efficient expert review and continuous monitoring. An extensive experimental evaluation on real-world industrial data demonstrates that TAMIS achieves the best accuracy-efficiency trade-off compared to baseline methods. To foster further research and reproducibility, we publicly release the anonymized application datasets used in our study.

---


### 200. [Effective Does Not Mean Useful: Conditional Functional Substitutability for Redundancy and Scaling in Transformers](https://arxiv.org/abs/2609.39259)

**<font color=#1a73e8>作者：</font>** Jiaheng Chen, Jiaxing Li, Yucheng Xiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern neural networks scale predictably, yet the mechanisms behind these regularities remain unclear. Neural redundancy is typically characterized by component importance or representational similarity, both indirect proxies. We view redundancy as an input-conditioned, dynamic relation: intermediate computational states are functionally redundant when they induce similar downstream responses. We introduce Conditional Functional Substitutability (CFS) to directly characterize such functional substitution. CFS exposes functional relations and reduction potential missed by conventional importance- and similarity-based measures. Across modalities and Transformer families, CFS reveals systematic functional reorganization with scale. Controlled scaling further shows that performance gains need not track growth in substitutability, while fixed-capacity models with more independent functional structure perform better, providing a functional account of diminishing returns. Predicted CFS further enables dynamic computation with a better performance--computation trade-off than importance-based component selection, suggesting new directions for redundancy-aware computation and more efficient model scaling.

---


> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-382](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
