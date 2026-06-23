# 📦 其他研究 | 2026年06月23日

> 本类共 **654** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

---

### 201. [Fusing Backdoors, Machine Learning, and Optimization for Large-Scale Parametric Mixed-Integer Programs](https://arxiv.org/abs/2606.21440)

**<font color=#1a73e8>作者：</font>** El Mehdi Er Raqabi, Pascal Van Hentenryck  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale optimization problems are often solved repeatedly under similar structural conditions, leading to substantial computational overhead. This occurs in applications such as power systems, transportation, and supply chain networks, where the underlying structure is fixed while parameters frequently vary under perturbations.
This paper proposes a Learning to Optimize (LTO) framework that accelerates the solution of large-scale general mixed-integer problems by leveraging the concept of a backdoor, i.e., a subset of variables that drive most of the computational complexity. The proposed BIPC framework consists of three phases. Phase I is an identification procedure that discovers a backdoor for a set of instances in the distribution. Phase II uses supervised learning to develop machine learning models that, given an instance, predict values for bounded-domain backdoor variables and intervals for wide-domain backdoor variables. These predictions define a reduced optimization problem where the predictions constrain the backdoor variables, while the other variables remain free. Phase III optimizes this reduced problem and, if necessary, applies a correction step to restore feasibility or the optimality guarantees.
Experiments on real-world, large-scale problems show substantial reductions in solution time with only a limited loss in solution quality. The framework enables organizations to solve large-scale optimization problems efficiently in the presence of frequent perturbations, such as unexpected events, demand fluctuations, or operational changes. Because these changes affect parameters rather than the problem structure, BIPC can quickly provide high-quality, feasible solutions, offering a practical approach to integrating machine learning into existing optimization pipelines.

---


### 202. [Synergistic Dual-Branch Adaptation for Multi-modal Generalized Category Discovery](https://arxiv.org/abs/2606.21446)

**<font color=#1a73e8>作者：</font>** Yuxun Qu, Minyu Zhou, Yongqiang Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalized Category Discovery (GCD) aims to classify old categories and discover new ones from unlabeled data. Recent multi-modal approaches introduce retrieved or synthesized texts into a dual-branch architecture to provide semantic cues complementary to visual features. However, the cross-modal synergy in existing dual-branch methods remains coarse and incomplete: the two modalities are encoded independently with the bias and noise in the derived text left unaddressed during encoding, and existing mutual learning strategies operate only on global class-level anchors, lacking fine-grained relational supervision. To address these limitations, we propose the Synergistic Dual-Branch Adaptation (SDBA) framework, which serves as a plug-and-play enhancement compatible with existing dual-branch methods such as GET and TextGCD. SDBA comprises two components: the cross-modal synergistic adapter inserts lightweight adapters into both branches and further injects visual information into the text adapter at each encoder layer to enhance text feature learning during encoding; the neighborhood mutual learning module enforces consistent local neighborhood distributions between the two branches via bidirectional KL divergence, providing fine-grained relational supervision for both old and new classes. Extensive experiments on six benchmarks demonstrate state-of-the-art performance, and consistent improvements on different baselines validate the broad scalability of the proposed framework.

---


### 203. [Precision Recall Controllable Radiology Report Generation via Hybrid Natural Language and Clinical Reward Learning](https://arxiv.org/abs/2606.21447)

**<font color=#1a73e8>作者：</font>** Ling Chen, Ruinan Jin, Jun Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated radiology report generation (RRG) has gained increasing attention because it can reduce the heavy workload of clinical report writing. However, most existing methods mainly optimize for natural language generation (NLG) metrics that focus on language fluency, while providing little control over clinically important factors such as precision and recall. As consequence, generated reports may be fluent but not well aligned with different clinical needs. To address this challenge, we propose a reinforcement learning framework for precision recall controllable RRG, where a control parameter explicitly adjusts the trade-off between clinical precision and recall during inference. This design allows the model to flexibly generate reports according to different clinical requirements. To ensure clinical correctness, we introduce a \blue{clinical reward} into the training objective, which helps improve clinical efficacy (CE) beyond standard language-based optimization. In addition, we apply a group-relative training strategy that normalizes rewards within each training group, reducing reward variance and improving training stability. Extensive experiments on the MIMIC-CXR dataset show that our method consistently outperforms state-of-the-art approaches in both NLG{ and CE} evaluation metrics, while providing reliable control over the CE precision recall trade-off.

---


### 204. [Technical Report for ICRA 2026 GOOSE 2D Fine-Grained Semantic Segmentation Challenge: Exploring Query-Based Segmentation and Increased Spatial Context for Outdoor Scene Understanding](https://arxiv.org/abs/2606.21456)

**<font color=#1a73e8>作者：</font>** David Pascual-Hernández, Roberto Calvo-Palomino, Inmaculada Mora-Jiménez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this report, we present our submission to the GOOSE 2D Fine-Grained Semantic Segmentation Challenge, organized as part of the Workshop on Field Robotics at ICRA 2026. The challenge combines data from the GOOSE and GOOSE-Ex datasets, which comprise more than 13k images captured from 4 distinct camera setups, annotated using a hierarchical taxonomy of 56 fine-grained classes and 11 broader categories. Starting from SegFormer as a baseline, we progressively improve segmentation performance through increased training crop sizes, a transition to the query-based Mask2Former architecture, and test-time augmentation. Our experiments show that query-based segmentation significantly outperforms the baseline model. Furthermore, increasing the crop size used during training yields substantial gains, highlighting the relevance of preserving scene context for fine-grained semantic disambiguation. Our final submission, using test-time augmentation, achieves an mIoU of 69.6% on the challenge test set, providing a strong baseline for fine-grained semantic segmentation in outdoor environments. To facilitate reproducibility and future research, code and weights will be made publicly available at this https URL .

---


### 205. [Native space based pipelines outperform template space based pipeline in subcortical segmentation](https://arxiv.org/abs/2606.21463)

**<font color=#1a73e8>作者：</font>** Tomás Lima, Daniel Novák, Eduard Bakštein  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of subcortical regions is critical for neurosurgical planning and functional research. Most automated methods rely on template space coregistration, which may compromise patient-specific accuracy, particularly in small structures. We identify a need to evaluate whether native space approaches offer a measurable advantage, which we evaluate in the context of movement disorders. We developed two UNet-based segmentation pipelines of the Subthalamic Nucleus (STN) - a common surgical target in Parkinson's Disease - and the neighbouring Red Nucleus (RN) and Substantia Nigra (SN). We collected 7T and 3T MRI data from five public datasets. The pipelines were evaluated in the native-space against manual labels. We further investigated the effect of the template resolution. Motivated by the hypothesis that models may better learn target boundaries in higher field, we tested the transferability of 7T-trained models to 3T clinical images, and whether synthetic 3T training data - generated via a disentangled representation learning method - could help bridging this domain gap. On held-out 7T data, the native pipeline consistently outperformed the template one. For the STN, native-space Dice reached 0.775 +- 0.055 versus 0.713 +- 0.051 (1 mm template), with HD95 of 0.79 +- 0.24 mm versus 1.17 +- 1.10 mm, respectively. Similar advantages were observed for the RN and SN. Increasing template resolution did not improve accuracy. When applied to 3T images, all models showed a considerable performance drop. Adding synthetic 3T data yielded only modest improvements, though without degrading 7T performance. Native-space segmentation is preferable for applications requiring patient specific anatomical fidelity, such as the surgical planning in PD. Bridging the 7T-to-3T domain gap remains an open challenge, motivating future work on domain adaptation tailored to subcortical structures.

---


### 206. [Towards Transparent Mental Health Insights: An Explainable AI Model for Career-Related Depression and Anxiety Among University Students Using Structured Data](https://arxiv.org/abs/2606.21474)

**<font color=#1a73e8>作者：</font>** Arsham Azam, Rasikh Ali, Tayyaba Farhat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Career anxiety and depression among university students present a growing challenge to mental health and academic achievement. This study proposes an Explainable AI (XAI) framework using multimodal data and Federated Learning (FL) to identify early indicators of career-related mental health problems in a privacy-preserving and culturally responsive manner. The framework combines structured behavioral data and facial emotion features from interview videos via an intermediate fusion neural network with attention mechanisms. Label smoothing was applied to improve model generalizability. FL was used across institutions to enable collaborative training without raw data sharing. Evaluation was conducted using the Student Mental Health Survey dataset from university students across Pakistan. Our model attained an F1-score of 89.12%, recall of 86.54%, accuracy of 92.08%, and precision of 91.88%. Using Integrated Gradients and SHAP, the model identified key behavioral markers of depression including avoidance of direct gaze, lower facial expressiveness, and social withdrawal, consistent with psychological theory. This research presents an interpretable, scalable, and context-sensitive AI system for mental health pre-diagnosis with potential integration into student support services globally.

---


### 207. [Deep Learning for Soil Moisture Estimation: Fusing Satellite Data with Optimally-Lagged Meteorological Features](https://arxiv.org/abs/2606.21475)

**<font color=#1a73e8>作者：</font>** Adrian Canovas-Rodriguez, Aurora González Vidal, Antonio F. Skarmeta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate soil moisture estimation in semi-arid agricultural regions requires integrating remote sensing and meteorological information while accounting for the delayed response of soil moisture to atmospheric forcing. This study introduces a Cross-Correlation Function (CCF) methodology to determine optimal temporal lags (0-30 days) between meteorological variables and soil moisture, as well as inter-depth lags (0-15 days) describing vertical moisture propagation from the surface (10 cm) to deeper layers (20-50 cm). The approach was validated across seven agricultural plots in southeastern Spain. Three deep learning architectures, each targeting a distinct prediction granularity, were evaluated under five feature configurations ranging from satellite-only to full satellite-meteorology-depth fusion: a CNN for per-pixel estimation within each plot, an LSTM for frame-level (daily plot-mean) prediction, and a CNN-LSTM hybrid operating on sliding windows with pooled multi-patch training. Models were assessed on held-out data to measure genuine generalisation. Meteorological variables improved performance over the satellite-only baseline, while subsurface depth information proved decisive across all architectures. The per-pixel CNN achieved the strongest single-patch result (R^2 = 0.877, RMSE = 2.28), with a seven-patch average R^2 of 0.535, representing an improvement of +1.00 over the satellite-only baseline. The pooled CNN-LSTM hybrid obtained the highest overall performance (R^2 = 0.930, CVRMSE = 8.0%). These results demonstrate that explicitly modelling atmospheric and vertical subsurface delays substantially improves soil moisture estimation for precision agriculture.

---


### 208. [Economic Transformation and Cultural Change: Evidence from Two Centuries of French Drama](https://arxiv.org/abs/2606.21485)

**<font color=#1a73e8>作者：</font>** T. D. Oliveira, L. A. Attilio, M. J. Davila-Fernandez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How do large-scale economic transformations shape cultural production? We address this question by combining computational linguistics, econometrics, and formal modelling, using French drama as a well-documented empirical laboratory. Applying latent Dirichlet allocation to a corpus of 1,215 theatrical texts published between 1700 and 1900, we show that aristocratic discourse centred on sovereignty and political authority was gradually displaced by bourgeois and household economic themes as French capitalism developed. Bayesian vector autoregressive models with max-share shock identification suggest a temporal shift in the literary response to economic shocks: bourgeois everyday-life themes reacted to GDP shocks in the eighteenth century, whereas household-economic concerns became responsive only after 1820, amid accelerating industrialisation. A discrete-choice model shows that peer effects among authors and sensitivity to prevailing economic conditions can jointly account for these dynamics. Monte Carlo simulations reproduce the observed historical trajectory with reasonable fidelity. These findings offer a quantitative framework for understanding how economic transformations propagate into cultural production through identifiable social mechanisms, contributing to the study of cultural evolution and the long-run relationship between institutions and literary discourse.

---


### 209. [A Longitudinal Study of Android Apps Signing Key Protection](https://arxiv.org/abs/2606.21487)

**<font color=#1a73e8>作者：</font>** Mark Huasong Meng, Qing Zhang, Weirao Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Android app signing relies on developer-managed credentials, making secure key protection essential for the integrity of the software supply chain. A recent platform key leakage incident involving two major OEM manufacturers demonstrates that even robustly designed signing mechanisms can be compromised due to developers' oversight. In this work, we conduct a longitudinal ecosystem study to characterize this threat by mining public repositories for Android signing credentials, recovering compromised keys via exposed passwords, and matching them against signatures from over 4,000 apps collected from major stores and OEM system images. Our analysis identifies 5,673 compromised keystores on GitHub and 26 unique certificates linked to 278 real-world apps. These include 26 third-party apps in public app stores and 252 preinstalled apps from seven manufacturers, collectively affecting over 10 billion users. We demonstrate the practical exploitability of these leaks through a proof-of-concept app replacement attack and identify spillover risks in non-smartphone platforms, including a popular automotive head-unit platform installed in over 1,100 vehicle models. Our results reveal that signing-key mismanagement is a systemic risk, underscoring the need for a more rigorous key-management support in Android release engineering and distribution infrastructures.

---


### 210. [Robustness Cannot be Reduced to Regularization: Studying Adversarial Training Beyond the Linear Case](https://arxiv.org/abs/2606.21488)

**<font color=#1a73e8>作者：</font>** David A. R. Robin, Rafael Pinot, Yann Chevaleyre  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The vulnerability of ML models to adversarial examples has recently emerged as a major concern. While adversarial training is one of the most effective countermeasures to this issue, its high computational cost remains an obstacle to practical deployment. Recent progress in reducing this cost has relied, in the case of linear models, on a formal equivalence between the adversarial risk and a simpler form of regularized risk. This enabled significantly more efficient training procedures, which naturally raises the question of whether such an equivalence can be extended beyond linear models. In this work, we formally show that no such equivalence is possible for two-layer networks. Our proofs proceed via a reduction to key properties that fundamentally separate the adversarial risk from any simple regularized risk which would only exhibit a weak form of data dependence. Beyond this setting, we provide empirical evidence on Wide-ResNets indicating that the same type of impossibility persists in deeper and more expressive architectures.

---


### 211. [Predicting High-Risk Colorectal Polyps in African Americans Using Pre-Colonoscopy Clinical Features: Machine Learning Model Development and Temporal Validation](https://arxiv.org/abs/2606.21492)

**<font color=#1a73e8>作者：</font>** Basheer Qolomany, Mrinalini Deverapall, Adeyinka Laiyemo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Risk stratification for advanced colorectal polyps typically relies on colonoscopy and/or pathology findings. However, there is growing interest in whether non-invasive features available prior to colonoscopy can help identify patients at higher risk. Such approaches may enhance clinical decision-making by prioritizing surveillance for individuals most likely to harbor high-risk polyps, when colonoscopy resources are limited while potentially reducing unnecessary procedures in lower-risk patients. Importantly, the use of non-invasive, pre-procedural information may also help promote more equitable access to risk stratification, particularly in settings where colonoscopy resources are limited or unevenly distributed. We aimed to develop and externally validate machine learning models to predict high-risk colorectal polyps using only non-invasive, pre-colonoscopy demographic, clinical, and behavioral features in a diverse, predominantly African American, urban cohort.
We conducted a retrospective cohort study using demographic, lifestyle, and comorbidity data from patients who underwent colonoscopy at Howard University Hospital to develop and validate several machine learning models, including neural networks, random forest, support vector machines (SVM), Naive Bayes, logistic regression, decision trees, k-nearest neighbors (KNN), and XGBoost, for predicting high-risk colorectal polyps. High-risk polyps (HRP) were defined as villous or tubullovillous adenomas, high-grade dysplasia, polyps >= 10 mm in size, and/or the presence of >= 3 polyps per procedure; all other cases were classified as low-risk polyps (LRP). The dataset included 4,681 patients from 2015-2022 used for internal validation and 1,562 patients from 2023-2024 used for external validation.

---


### 212. [Semi-Supervised Vision-Language-Action Model](https://arxiv.org/abs/2606.21493)

**<font color=#1a73e8>作者：</font>** Hongyang He, Jiuming Liu, Victor Sanchez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models enable robots to predict actions directly from visual observations and language instructions, but adapting them to new environments still depends on costly action-labeled demonstrations. To reduce this dependence, we study semi-supervised VLA adaptation under limited supervision signals, where only a small portion of trajectories contain robot actions and the remaining trajectories provide action-unlabeled vision-language observations. Unlike standard semi-supervised learning, the missing supervision is an embodied action signal that must be visually grounded, language-consistent, physically feasible, and temporally stable. To address this problem, we propose SemiVLA, a self-distilled teacher-student framework that learns from reliable pseudo-actions on unlabeled trajectories. SemiVLA introduces a VLA-specific reliability controller to assess vision-language alignment, action feasibility, and temporal transition consistency, and further updates the teacher through a Bottleneck-Projected Alignment Update to avoid noisy feedback contamination. With OpenVLA as the backbone, SemiVLA consistently improves multiple PEFT strategies across LIBERO and CALVIN. Under 10\% labeled trajectories, SemiVLA with Selective LoRA achieves 89.0\% average success on LIBERO, outperforming supervised LoRA by 8.0 points without extra inference cost.

---


### 213. [Breaking chains with trees: Deep learning with $\mathcal{O}(\log N)$ parallel time complexity](https://arxiv.org/abs/2606.21497)

**<font color=#1a73e8>作者：</font>** Neeraj Mohan Sushma, Aditya Nagarsekar, Cabrel Teguemne Fokam 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern deep neural network architectures are trained via backpropagation, which requires errors to be sequentially propagated through all layers before parameters can be updated. This introduces two limitations: locking, where layer-wise updates are strictly interdependent and cannot proceed in parallel, and the weight transport problem, which requires symmetric forward and backward pathways for exact gradient computation. These constraints restrict parallelism, increase memory and communication overhead, and pose challenges for scalable learning. In this work, we propose Hierarchical Block-Local Learning (HBLL), a framework that decomposes deep neural networks into hierarchically linked blocks trained using local learning objectives derived from variational principles, eliminating the need for full end-to-end backpropagation while maintaining effective information propagation across the network. HBLL is the first algorithm that is able to train deep neural networks in $\mathcal{O}(\log N)$ parallel time complexity, where $N$ is the number of network layers. We show that HBLL implicitly defines a family of subnetworks corresponding to different hierarchical paths, enabling flexible inference with different effective numbers of layers. We evaluate HBLL on a set of challenging vision and language modeling tasks, achieving competitive performance. We also extend HBLL to recurrent sequence architectures, applying to settings that otherwise rely on backpropagation through time.

---


### 214. [Privacy-Preserving Federated Temporal Graph Learning with Digital Twin--Guided Adaptive Deception for Cyber-Resilient IoMT](https://arxiv.org/abs/2606.21513)

**<font color=#1a73e8>作者：</font>** Syed Zeeshan Haider, Anwar Shah, Muneeb Arif 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of IoT and IoMT devices introduces critical cybersecurity vulnerabilities in healthcare and industrial environments where resource-constrained devices operate under strict latency and data-privacy regulations. This paper presents the Federated Temporal Graph Convolutional Network with Advantage Actor-Critic (Federated TGCN-A2C), a privacy-preserving defense architecture integrating four mechanisms: a PyG-based Temporal GCN using GCNConv layers with global mean pooling and a learned anomaly gate for flow-level threat classification; LSTM-based Digital Twins generating per-device anomaly scores gating the classifier via learned sigmoid coupling; a Federated A2C agent selecting among ALLOW, ISOLATE, and HONEYPOT-REDIRECT actions based on a seven-dimensional state capturing confidence, entropy, anomaly magnitude, and traffic composition; and an enhanced honeypot layer converting suspicious traffic into threat intelligence with adaptive thresholds. Federated aggregation employs EMA-smoothed per-client validation losses as inverse-weighted FedAvg coefficients to stabilize global model updates under non-IID distributions, with cosine-annealed learning rates per round. Evaluated on CICDDoS 2019 and TON-IoT benchmarks, the framework achieves 99.48% and 99.61% test accuracy with weighted-F1 scores of 0.9948 and 0.9961, converging within 25 and 10 federated rounds, outperforming Fed-Inforce-Fusion by 0.21 percentage points while covering three additional attack categories. All sixteen CICDDoS 2019 classes achieve F1 of at least 0.9237 and all ten TON-IoT classes achieve F1 of at least 0.9488, including the severely imbalanced MITM category. Post-hoc explainability via SHAP, LIME, Grad-CAM, and counterfactual analysis confirms decisions are grounded in semantically meaningful flow features, supporting regulatory accountability in clinical deployments.

---


### 215. [Towards Understanding the Power and Limits of the Muon Optimizer: A River-Valley Perspective](https://arxiv.org/abs/2606.21514)

**<font color=#1a73e8>作者：</font>** Tianqi Shen, Jinji Yang, Runze Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, Muon has gained substantial attention as an appealing alternative to Adam-like optimizers, with many works highlighting its advantages through spectral normalization and improved conditioning. Yet this positive theoretical narrative contrasts with its empirical performance in large language model (LLM) training, where Muon's gains over Adam/AdamW are often mixed, schedule-sensitive, and not uniformly superior. To address this gap, we develop a trajectory-level theory characterizing both the strengths and limitations of Muon. We introduce a mixed-spiked matrix sensing model whose sensing operator decomposes into signal, spike, and bulk components, capturing a mixture of anisotropic structure and long-tail information reminiscent of LLM training. On top of it, we adopted a river-valley perspective in which we view the landscape as composed of a river direction flowing to the desired solution and hill directions encoding nuisance or task-irrelevant information. In the momentum-free setting, we show that Muon moves faster along the information-bearing river direction during early optimization, but can converge much more slowly near the river bottom than gradient descent. We then extend the river-valley perspective to general nonconvex objectives with momentum by studying points on the spectral river. There, while Muon converges faster early on, its orthogonalized update removes residual scale information, making it prone to overshooting and oscillation near the target solution. Together, these results suggest that our characterizations extend beyond spiked matrix sensing and motivate switching to GD-like refinement optimizers in the final phase, rather than relying only on a fixed learning-rate schedule for Muon. We also provide preliminary evidence supporting this two-stage approach in language model training experiments.

---


### 216. [MedHal-Loc: Are "Explainable-by-Architecture" Medical Hallucination Detectors Faithful Localizers? A Localization Benchmark](https://arxiv.org/abs/2606.21517)

**<font color=#1a73e8>作者：</font>** Minmin Chen, Daojian Lu, Yining Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting hallucinations in clinical text is increasingly framed as an explainability problem: systems should not merely flag an unreliable response but point to the offending span. Architectures built around knowledge-graph (KG) triple decomposition are marketed for exactly this auditability, yet their localization ability is typically assumed rather than measured. We introduce MedHal-Loc, a benchmark and metric for localization faithfulness -- whether a detector's top-ranked error unit actually overlaps the erroneous span. The controlled subset comprises 300 PubMedQA-derived statements with single, span-level errors injected across four localizable types (entity substitution, relation error, mechanism misattribution, invention), yielding gold spans by construction; a complementary natural subset documents that real hallucinations are dominated by diffuse conclusion-flips that resist span localization (a human expert accepted 1/18 candidate spans). Evaluating four fine-grained paradigms, we find that NLI-per-clause, consistency-per-sentence, and the dedicated span detector FAVA all localize well above chance, whereas an elaborate KG-triple pipeline localizes no better than chance (+3.3pp, n.s.), bottlenecked by ~59% entity-extraction coverage -- despite competitive detection F1 (0.609). Detection competence does not imply faithful localization; architectural explainability must be validated, not presumed.

---


### 217. [Backpropagating Through Simulation: Analytic Policy Gradients for Sample and Learning Efficient Differentiable Continuous Control](https://arxiv.org/abs/2606.21525)

**<font color=#1a73e8>作者：</font>** Yueci Deng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-free reinforcement learning algorithms such as Proximal Policy Optimization (PPO) treat the environment as a black box, estimating policy gradients from sampled rewards; this process demands millions of interactions and relies on high-variance advantage estimates. When environment dynamics are differentiable, the return is an end-to-end differentiable function of the policy parameters, enabling exact gradient computation via backpropagation through simulation. We term this approach Analytic Policy Gradients (APG) and evaluate it against PPO on four continuous control tasks of increasing dynamical complexity: a one-dimensional point-mass target-reaching task, a 2D point-mass navigation task with obstacle avoidance, a 2D rigid-body T-block pushing task, and a 7-DOF Franka FR3 end-effector reaching task. Both algorithms share identical model architectures, observation normalization, and optimizer settings. To decouple sample efficiency from compute efficiency, we design a multi-axis evaluation protocol that records performance against environment steps and gradient steps. We report a segmented backpropagation scheme with MC and critic-based bootstrap modes that mitigates gradient degradation on long-horizon tasks, and present ablations over segment length and bootstrap strategy.

---


### 218. [Memory Is No Longer a Bottleneck: Memory-Efficient Graph Filtering for Scalable Collaborative Filtering](https://arxiv.org/abs/2606.21540)

**<font color=#1a73e8>作者：</font>** Jin-Duk Park, Won-Yong Shin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph convolutional networks (GCNs) have demonstrated significant success in capturing complex user-item relationships for collaborative filtering (CF). However, due to their reliance on extensive model training, training-free graph filtering (GF)-based CF methods have emerged as a promising alternative, offering computational efficiency by smoothing graph signals via matrix operations. In particular, polynomial GF-based approaches demonstrate improved accuracy through their ability to design more expressive and flexible filtering functions. Despite these advantages, existing GF methods suffer from a critical memory bottleneck: they necessitate storing the full item similarity graph, incurring prohibitive memory costs for large-scale datasets, which limits their practical applicability. To tackle this challenge, we propose Mem-GF (Memory-efficient GF), a new GF-based CF method that departs from conventional designs by principally leveraging the structure of Krylov subspaces as a core mechanism for approximating polynomial graph filters without explicitly storing the item similarity graph. We theoretically analyze the minimum Krylov subspace size that guarantees lossless approximation. Through extensive experiments, we demonstrate that Mem-GF achieves up to 5.74$\times$ lower memory usage and 4.38$\times$ speedup in runtime, while consistently exceeding the recommendation accuracy of state-of-the-art GF and GCN-based methods. Mem-GF robustly scales to datasets with tens of millions of interactions, establishing itself as a practically viable and theoretically grounded solution for efficient CF.

---


### 219. [PeerMathDial: A Middle School Dialogue Dataset for Student Collaborative Math Problem Solving](https://arxiv.org/abs/2606.21557)

**<font color=#1a73e8>作者：</font>** Murong Yue, Desmond Alexander Mcglone, Emily Slutz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Collaborative Problem Solving (CPS) is a core skill in education, where the process of peer interaction is highly important. However, existing educational dialogue datasets mostly focus on classroom instruction or tutoring (i.e., teacher/tutor-student interaction), yet datasets centering small-group, student-student interaction are limited. This thus leaves research with limited resources for studying how students interact, coordinate, and solve problems together in real educational settings. To address this, we introduce PeerMathDial, the first dataset of peer CPS dialogues collected from authentic middle school math classrooms. It contains 55 dialogues from 27 students, totaling 6,406 turns. To facilitate research on CPS discourse analysis, we further build a corpus-grounded dialogue act taxonomy assisted by LLMs. Using the dataset and the dialogue act taxonomy, we demonstrate the practical applications of PeerMathDial across three use cases. First, we track how dialogues evolve over time and measure the impact of teacher interventions. Second, we align dialogue actions with student surveys to reveal the connection between students' traits (e.g., confidence, leadership) and their actual behaviors. Third, by evaluating LLMs on dialogue act prediction, we glimpse at the potential of LLMs for student simulation in educational applications. Our dataset and source code will be released to the community.

---


### 220. [Monitoring Diameters of Causal Communication Graph with Spatio-Temporal Logic](https://arxiv.org/abs/2606.21558)

**<font color=#1a73e8>作者：</font>** Lydia Bakiri, Jérémy Dubut, Sergio Mover  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Verification of multi-agent systems requires the ability to check meticulous topological properties when it comes to agents that can move through space in continuous time. This demands a logic with sufficient expressiveness to capture these dynamics. MuTGL logic has interesting properties for expressing entangled space-time properties. However, this logic lacks the expressivity needed to analyse reachability within specific distance bounds, or to track the length or the cost of communication chains: these are fundamental for decentralized monitoring, or graph-theoretic analysis of distributed protocols, where algorithmic complexities often relates with the system's communication graph diameter. We then introduce an extension of muTGL, including a new operator called the space horizon. This addition allows us to bound the distance of communication chains, hence enhancing the logic's expressiveness. We show that this operator allows to encode modalities from other logics, such as reachability or escaping which were not available in vanilla muTGL, while allowing a deeper entanglement of spatial and temporal properties. We provide a centralized offline monitoring algorithm for this logic and illustrate it on several examples on simulations of Consensus-Based Bundle Algorithms, distributed protocols for task allocation.

---


### 221. [Compressing Observation History into Agent Memory: Distilling Transformers into Recurrent Transformers](https://arxiv.org/abs/2606.21562)

**<font color=#1a73e8>作者：</font>** Philippe Weinzaepfel, Christian Wolf, Bülent Mert Sariyildiz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformers are AI's workhorse with strong performance in modeling sequential data, but their computational cost becomes prohibitive when processing long sequences. We target long-horizon streaming vision and robotics applications like map-free pose estimation, where it is particularly impractical to store and maintain a history of observations. Recurrent Transformers address this limitation by maintaining fixed-size memory but their performance lags behind that of transformers operating over the full observation history. We argue that this gap does not stem from architectural limitations, but from differences in how these models learn to compress past information. Without access to an observation history, recurrent models must explicitly decide what to retain in memory at each step, a significantly harder learning problem. In this work, we propose a distillation approach that transfers the compression strategy of a classical full-history transformer to a recurrent variant. We enable this by designing a teacher model that explicitly compresses its observation history into a fixed-size bottleneck representation. By directly supervising the student's memory with this bottleneck representation, we align the two compression mechanisms. We show that this approach allows to train a recurrent latent robotic memory with linear-time complexity while substantially narrowing the performance gap to full-history transformers.

---


### 222. [LIG: Layer-wise Integrated Gradients for Within-Layer Flow Analysis in Transformers](https://arxiv.org/abs/2606.21564)

**<font color=#1a73e8>作者：</font>** Eight Suzuki, Hideitsu Hino, Noboru Murata  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers achieve strong performance, but their internal computations remain opaque. We view each Transformer layer as a dynamic graph whose nodes are token representations and per-head attention outputs, with Multi-Head Attention (ATT) and MLP as module boundaries. On this graph we use LIG (Layer-wise Integrated Gradients), which applies set-to-set Integrated Gradients (IG) at nonlinear module boundaries. Set-to-set IG applies IG to a map from a set of input token representations to a set of output representations, evaluating token-to-token contributions, which is not standard in prior IG applications. This extends IG from the usual scalar-objective setting to set-to-set maps via an L2 scalarization, and composes within-layer contributions in the spirit of Layer-wise Relevance Propagation (LRP), with IG completeness playing the role of LRP-style conservation at each boundary. We use LIG to analyze (i) the agreement between module-wise composition and layer-whole attribution under an L2 criterion, and (ii) within-layer information flow by tracing separated ATT and MLP contributions. On BERT-base and PTB, configurations that best preserved within-layer consistency used the target token's embedding as the ATT baseline and either the ATT output at a=0 or Zero as the MLP baseline. We therefore present LIG as a diagnostic XAI tool at module-boundary granularity, without model-specific retraining or per-operation interpreter design. Code is available at this https URL.

---


### 223. [A Smart Classroom Behavior Analysis Framework with a New Highly Congested Classroom Dataset](https://arxiv.org/abs/2606.21568)

**<font color=#1a73e8>作者：</font>** Wei Xu, Maoxiang Chu, Yuelong Fan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Student behavior detection is important for intelligent classroom analysis but remains challenging in large-class scenarios due to dense instance co-occurrence, asymmetric occlusion, depth-wise scale variation, and fine-grained semantic degradation in distant targets. Existing classroom behavior datasets and general-purpose detectors are insufficient to characterize and address these challenges. This paper constructs the Highly Congested Classroom Behavior (HCCB) dataset, containing 50,229 student behavior instances across seven categories: reading, writing, heads up, sleeping, looking around, bowing head, and using phone. HCCB provides a challenging benchmark that integrates dense distributions, severe occlusion, scale variation, and fine-grained behavioral semantics. To address these issues, we propose ODER-HSFNet, a YOLO-based detection framework tailored to highly crowded classrooms. At its core, ODER-HSFNet introduces three task-specific innovations: the Occlusion-aware Deformable Edge Rectifier (ODER), which strengthens boundary evidence under occlusion; the Hypergraph-State Spatial Fusion (HSSF) module, which integrates local structure enhancement, state-space contextual modeling, and high-order relation aggregation; and the Occlusion-Calibrated Detection Head (OCDetect), which suppresses low-quality Pre-NMS candidates and reduces false positives from occlusion boundaries and neighboring instances. Experiments on two classroom behavior detection datasets show that ODER-HSFNet outperforms mainstream YOLO-series methods, achieving 60.60%/80.12% mAP50:95/mAP50 on HCCB and 57.36%/74.65% on SCB-D3-S. Ablation studies further verify the effectiveness of the proposed design for highly crowded classroom behavior detection.

---


### 224. [The Unreasonable Effectiveness of VLMs for Zero-shot Procedural Mistake Detection](https://arxiv.org/abs/2606.21579)

**<font color=#1a73e8>作者：</font>** Serdar Ozsoy, Lars Doorenbos, Federico Spurio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Procedural mistake detection is important for quality control and user assistance across many disciplines. Recent work in this field has achieved significant gains by using the reasoning capabilities of Video-Language Models (VLMs) as components within multi-stage pipelines, which consist of separate modules for supervised temporal action segmentation, error detection, and explainability. Consequently, they remain dependent on tailored training datasets and require task-specific training, limiting their wider applicability. To remedy this, we introduce zero-shot procedural mistake detection and propose a unified Zero-shot Procedural Mistake detection (ZeProM) framework that jointly solves procedural mistake detection and temporal action segmentation with a single pre-trained VLM. By evaluating our framework on two canonical mistake detection benchmarks, EgoPER and CaptainCook4D, we find that ZeProM can perform these tasks successfully, while approaching, or even outperforming, the performance of fully supervised methods. For instance, we achieve a 4.4 point improvement in EDA and a 2.0 point improvement in F1@.5 on average over all five EgoPER tasks compared to the strongest supervised methods. Overall, our results show the potential of unified methods for procedural mistake detection, and we hope this will steer the field away from highly complex pipelines and toward more generally applicable solutions.

---


### 225. [The Cost Geometry of Belief: finite-resource inference under noisy observation](https://arxiv.org/abs/2606.21585)

**<font color=#1a73e8>作者：</font>** Laurent Caraffa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We equip the space of beliefs with a cost geometry (what it costs to pass from one belief to another): optimal transport in Wasserstein space, reweighted conformally by Fisher information (the price of the precision at stake), distinct from the Fisher-Rao metric. In the setting we consider, a finite machine maintains a digital twin of a system; observing the territory through finite, noisy sensors, we model its coherent output as a belief: a probability density over states, the Bayes posterior. Certainty (the perfect twin) is denied twice, by observation and by physics, both read off the Fisher information. On the conformal class, essentially location-scale, three results emerge, all invariants of one change of cost unit. A wall: a well-posed inference rejects certainty to infinite distance as soon as the cost dominates the Fisher information (necessity conjectured beyond power laws). An honesty: an honest (eikonal) cost, each nat the same length everywhere, selects the geometries proportional to the Fisher information. A rigidity: these geometries are hyperbolic, and the Stam bound crowns the Gaussian, the most hyperbolic location-scale belief. Changing the unit dilates the geometry yet preserves the wall, the curvature ordering, and the extremality of the Gaussian: an absolute cost says nothing, only relative cost carries meaning, the value -1/4 being one of its images. The cost of reaching a given precision then has a geometric floor diverging at certainty. Thermodynamics fixes the cost unit and motivates this framework; the results are geometric, in nats.

---


### 226. [FAST: A Framework for Aligned Sampling and Training in Parallel Reinforcement Learning for Autonomous Driving](https://arxiv.org/abs/2606.21587)

**<font color=#1a73e8>作者：</font>** Bonan Wang, Letian Tao, Bin Shuai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning is pivotal for closed-loop autonomous driving yet remains constrained by severe bottlenecks in sampling efficiency. Standard parallel sampling mitigates this but suffers from the straggler effect, where the premature termination of a single environment necessitates a synchronized batch re-initialization, leading to suboptimal sample utilization and prohibitive re-initialization latency. To address this, we propose FAST, a synchronous parallel framework tailored for closed-loop simulation. Specifically, FAST employs Dynamic Parallel Sampling Alignment (DPSA) to maintain vectorization synchronization by extending terminated episodes via virtual continuation, thereby decoupling the sampling loop from individual terminations. By dynamically triggering global truncation based on the termination rate of parallel clips, FAST effectively eliminates the bottleneck of premature resets without sacrificing data diversity. Furthermore, to strictly preserve theoretical consistency, we incorporate a Scaled Mask-Padding Optimization (SMPO) that leverages validity masking and adaptive loss normalization to nullify the bias from auxiliary padding data. Empirical evaluations demonstrate that FAST achieves at least a 1.78 times wall-clock speedup over the single-clip baseline while preserving statistical unbiasedness.

---


### 227. [Radial Basis Function Networks as Projection Heads in Self-Supervised Learning](https://arxiv.org/abs/2606.21590)

**<font color=#1a73e8>作者：</font>** Andreas Schliebitz, Heiko Tapken, Martin Atzmueller  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) typically relies on a backbone encoder followed by a small multilayer perceptron (MLP) projection head, which is conventionally discarded after training, while backbone quality is assessed via costly linear probing on labeled data. We argue that this approach including discarding the projector is rather computationally wasteful. Instead, we propose replacing the MLP head with a radial basis function network (RBFN), whose interpretable center and shape parameters can be exploited to judge representation quality without labels or a separate classifier. To this end, we introduce Scale-Normalized Separation (SNS), a novel label-free quality metric derived solely from the kernel centers and shapes learned during training. Across five canonical SSL architectures (MoCo, SimCLR, BYOL, SwAV and SimSiam) and four image classification datasets, we show that RBFN projection heads are competitive drop-in replacements for standard MLP projectors. We recommend constructing them with three RBF layers activated by the Gaussian radial basis function. Moreover, SNS exhibits strong to very strong positive correlation with established logistic regression metrics, demonstrating that a trained RBFN projector can act as a reliable proxy for backbone representation quality. We additionally publish a novel PyTorch compatible image classification dataset based on Google's Open Images V7 to facilitate reproducible research into representation learning.

---


### 228. [Enhancing Stateful Detection of Adversarial Attacks with Soft-labels' Temporality and Robust Similarity Approximations](https://arxiv.org/abs/2606.21592)

**<font color=#1a73e8>作者：</font>** De Zhang Lee, Han Fang, Ee-Chien Chang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Stateful Detection (SD) mitigates adversarial attacks by determining whether a sequence of queries contains queries from a black-box adversary. Recent works, such as Blacklight and PIHA utilize query similarity to detect such queries. In this paper, we observe that temporal information, in particular, the temporal correlation of the classification soft labels, is a prominent characteristic of adversarial attacks and can be leveraged to reduce false positive rates. Moreover, we point out a potential vulnerability in SD implementation. Many SD systems identify similar queries according to some implicit, computationally expensive metric. To improve efficiency, these systems often adopt an approximate similarity function as substitute. This discrepancy could be exploited by crafting queries that appear dissimilar under the approximation but are close in the intended metric, thereby evading detection. We refer to this as an ``adversarial attack'' on the approximation function, and demonstrate it through a lightweight attack on Blacklight's similarity function.
Based on the above observations, we propose a two-phase approach. The first phase identifies subsequences of queries with high similarity, incorporating randomness to prevent the aforementioned ``adversarial attacks''. The second phase analyzes temporal correlation of the soft-labels to further validate the presence of the adversary's queries. Experimental results show that the framework detects adversarial queries generated by Boundary Attack, HSJA, SimBA, Square Attack with true positive rate (TPR) reaching 1.00, while maintaining a false positive rate (FPR) of at most 0.06. Additionally, the method is robust against OARS which is an adaptive attack.

---


### 229. [Geometric and Information Compression of Representations in Deep Learning](https://arxiv.org/abs/2606.21593)

**<font color=#1a73e8>作者：</font>** Linara Adilova, Henning Petzka, Asja Fischer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks transform input data into latent representations that support a wide range of downstream tasks. These representations can be characterized along information-theoretic and geometric dimensions, but their relationship remains poorly understood. A central open question is whether low mutual information (MI) between inputs and representations necessarily implies geometrically compressed latent spaces and vice versa. We investigate this question using class-wise clustering as a measure of geometric compression and theoretically sound MI estimation in conditional entropy bottleneck (CEB) networks and continuous dropout networks. We evaluate the interplay between MI, geometric compression, and generalization on classification tasks under controlled noise injection schemes. Our findings show that low MI does not reliably correspond to geometric compression, and that the connection between the two is more nuanced than often assumed. Indeed, our experiments reveal a negative and nonlinear relationship that can reverse when varying training setup. Our results put forward a hypothesis that generalization acts as a potential confounder in this connection rather than being their direct consequence.

---


### 230. [Boundary-by-Mask: Few-Shot Instance Segmentation with Mask-Conditioned Boundary Learning for Texture-Poor Industrial Parts](https://arxiv.org/abs/2606.21594)

**<font color=#1a73e8>作者：</font>** Yutaka Yoshinaga, Naoya Chiba, Koichi Hashimoto  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in large pre-trained models have led to remarkable progress in instance segmentation on general images. However, industrial scenarios remain challenging. Instance definitions are often application-specific and inconsistent, and the domain gap from general imagery is substantial due to weak textures and limited contextual cues. Consequently, a direct application of existing models is unreliable. We propose Boundary-by-Mask, a few-shot instance segmentation framework that supervises boundaries instead of interior appearance. Given a few RGB images and corresponding instance masks, the method extracts rich visual features using a foundation-model encoder and trains a lightweight Signed Distance Function (SDF) head to predict boundary-aware distance maps. Segmentation masks are obtained through an SDF-to-mask reconstruction process. By explicitly estimating contours, the framework achieves reliable instance separation even on low-texture and color-uniform surfaces. The instance definition is conditioned by the instance mask. Replacing the mask specifies the segmentation target, such as the whole object or a sub-part. A pixel-wise shallow MLP head enables rapid training. Experiments on industrial parts and food items with ambiguous boundaries show strong few-shot generalization, robustness in feature-poor conditions, and precise control over mask-level targets.

---


### 231. [Per-Entity Bias Mapping for AI Visibility: Why Brand Mentions Require Entity-Specific Calibration](https://arxiv.org/abs/2606.21595)

**<font color=#1a73e8>作者：</font>** Zoltan Varga  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI-mediated answer systems increasingly determine how brands and organizations are represented to users. Existing approaches reduce visibility to mention rate or citation frequency. This paper argues that aggregate metrics are insufficient because entities exhibit systematically different AI visibility error profiles.
We introduce Per-Entity Bias Mapping (PEBM): a ten-dimensional framework distinguishing raw from verified mentions. Three failure modes are identified: (1) underrepresented entities suffer invisibility due to weak knowledge graph presence; (2) large entities suffer the Brand Hallucination Paradox -- model familiarity creates stronger surfaces for plausible but incorrect completions; (3) CEE entities face a structural infrastructure gap across knowledge graphs, NER, and entity linking. A fourth dimension, Parametric-Retrieval Lag Asymmetry, describes divergence between retrieval-augmented and parametric memory update cycles.
A full-scale empirical study (n=100 Hungarian B2B entities, 1,400 probe runs, 2,062 sources) finds Tier 1 brands produce 52.69% fabricated citations versus 37.87% for Tier 3 entities (+14.82 pp; p=1.67e-11), supporting the Brand Hallucination Paradox. Regulatory-framed queries elevate fabrication to 56.77% versus 37.59% baseline (+19.2 pp). We identify rejection-induced confabulation escalation: agentic quality filters function as hallucination accelerators in compliance contexts. We introduce ghost cartography as a unifying mechanism: entities in sparse latent regions produce confident output interpolated from neighboring dense regions, yielding a two-dimensional confabulation space (fabricated presence vs. frozen representation).

---


### 232. [$ϕ$-Scene: Physically Grounded Image-to-3D Scene Reconstruction](https://arxiv.org/abs/2606.21596)

**<font color=#1a73e8>作者：</font>** Haodong Li, Lulu Shao, Haolin Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing compositional 3D scenes from a single image is a fundamental challenge in 3D world modeling. Recent methods can recover high-fidelity, complete 3D objects and predict plausible scene arrangements, but most still treat scene reconstruction primarily as a visual and geometric prediction problem. Their outputs may therefore contain floating objects, interpenetrations, or unstable-contact artifacts, limiting their physical validity and downstream usability in simulation, robotics, and interactive environments. We present $\phi$-Scene, a physically grounded approach to open-vocabulary and compositional image-to-3D scene reconstruction. The key premise is that a reconstructed scene should not be treated merely as a set of objects with predicted poses, but as a stable physical system. Accordingly, $\phi$-Scene formulates reconstruction as topology-driven physical assembly: it infers how objects support one another, orders them accordingly, and progressively settles each object against its already stabilized support context. For each object in topological order, SDF-based optimization first resolves penetrations against the pre-settled support context, and rigid-body simulation then settles the object into a stable contact configuration under real-world physical constraints. Experiments on 3D-Front show that $\phi$-Scene achieves the strongest overall performance among out-of-domain methods and remains highly competitive with in-domain baselines. Human and VLM evaluations further show strong preference for $\phi$-Scene in visual quality, reference alignment, and physical plausibility. Finally, dedicated physical plausibility metrics covering static contact quality and dynamic stability demonstrate that $\phi$-Scene substantially reduces penetration artifacts while producing much lower post-simulation drift, indicating more stable and physically grounded 3D scenes.

---


### 233. [Learning to Place Guards by Reinforcement: A Geo-Free Neural Policy for the Vertex-Guard Art Gallery Problem](https://arxiv.org/abs/2606.21604)

**<font color=#1a73e8>作者：</font>** Domagoj Ševerdija, Jurica Maltar, Nathan Chappel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural combinatorial optimization (NCO) has shown that policies trained by reinforcement can construct strong solutions to NP-hard problems directly from raw instances. What such a policy actually learns, as opposed to what its decoder expresses, remains much less clear. We study this distinction on the vertex-guard Art Gallery Problem, the NP-hard task of choosing polygon vertices from which to observe an entire region. A pointer-network policy is trained from a coverage-aware reward over its own rollouts under the constraint we call geo-free inference: at test time it sees only vertex coordinates, with no visibility computation and no geometric oracle. The policy places guards economically but leaves a tail of under-covered polygons that widens far beyond the training range. To locate the cause, we freeze the trained encoder and read its embeddings with a small single-shot classifier, still geo-free at inference. The classifier closes most of the feasibility gap, in and out of distribution and at up to roughly five times the training range, cutting under-covered polygons by about an order of magnitude at an explicitly reported cost in guard count. We read this as evidence that the reinforcement-trained representation already encodes the geometry required for feasibility, and that residual failures reflect decoder calibration rather than missing knowledge. Probing a frozen encoder thus offers a practical way to ask what a neural combinatorial solver has internalized.

---


### 234. [T-MOR: Learning Motion-Aware Skeleton Representations for Human Action Recognition](https://arxiv.org/abs/2606.21607)

**<font color=#1a73e8>作者：</font>** Di Yang, Mahmoud Ali, Quan Kong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models such as CLIP have recently achieved strong performance on a wide range of visual understanding tasks. However, most existing models rely primarily on appearance-level supervision from images or videos, and do not explicitly model human motion, which is essential for fine-grained and human-centric action recognition task as actions are defined by temporally structured and physically grounded body movements. To address this problem, we propose Transferable skeleton MOtion Representation (T-MOR), a motion-aware framework that learns transferable action representations from skeleton sequences with the aid of video and language supervision during training. T-MOR adopts a multi-modal contrastive learning scheme that aligns skeleton motion with visual and textual representations, while performing inference using only lightweight skeleton inputs. To support large-scale pre-training, we construct PoseCap-1M, a new dataset that contains over one million synchronized video, skeleton, and text triplets covering diverse human activities. We evaluate T-MOR on a range of human-centric action recognition benchmarks, including action classification and frame-wise temporal detection. Experimental results show that T-MOR consistently improves performance across multiple datasets, such as Toyota Smarthome, Penn Action, UAV-Human, TSU, and Charades. In addition, T-MOR demonstrates strong generalization ability in few-shot and zero-shot settings, highlighting the effectiveness of motion-centric and embodied representations for transferable action understanding.

---


### 235. [CurvSegFlow: Time-Conditioned Flow Matching for Robust Segmentation of Curvilinear Structures in Noisy Biomedical Images](https://arxiv.org/abs/2606.21608)

**<font color=#1a73e8>作者：</font>** Sidi Mohamed Sid'El Moctar, Achraf Ait Laydi, Alexandre Beber 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of curvilinear structures remains challenging in biomedical imaging due to their thin geometry, complex topology, and sensitivity to noise. This is particularly critical for microscopy images of cytoskeletal network, where low signal-to-noise ratios and dense filament crossings often lead to fragmented or inaccurate segmentation. In this work, we propose CurvSegFlow, a segmentation framework based on time-conditioned flow matching. Instead of predicting a segmentation mask in a single pass, the method models segmentation as a dynamic process that progressively refines a noisy initialization into the target structure through a learned velocity field. The proposed model combines a U-Net backbone with triple-term loss function and temporal embeddings to guide the refinement process across reconstruction stages. This formulation enables gradual error correction and improves the continuity of thin structures. CurvSegFlow is evaluated on multiple synthetic and real microtubule datasets, as well as on public benchmarks of retinal vessels, corneal nerves and coronary arteries. Across datasets, the method achieves competitive or superior performance compared to established segmentation models, with consistent improvements in precision and structural continuity, particularly under low signal-to-noise conditions. These results show that flow-based iterative refinement provides a robust and general framework for curvilinear structure segmentation. Overall, the proposed approach improves segmentation quality in challenging imaging conditions and generalizes effectively across modalities without architectural changes.

---


### 236. [The Two-Hump Problem: Bridging the Difficulty Gap in Mathematical Reinforcement Learning](https://arxiv.org/abs/2606.21611)

**<font color=#1a73e8>作者：</font>** Lucas Fagan, Michele Tarquini, Ali Shehper 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mathematical search problems present a unique challenge for Reinforcement Learning (RL) due to vast search spaces and sparse rewards. In previous works, the Andrews-Curtis (AC) conjecture was established as an illustrative example of such problems. In this work, we identify a critical structural barrier in the AC landscape: a "Two-Hump" distribution, where problem instances are either trivially solvable or effectively impossible, with a scarcity of intermediate "hard-but-solvable" instances required for effective learning. We tackle this challenge through two primary avenues: novel data generation techniques to populate the difficulty gap, and significant algorithmic enhancements including the introduction of supermoves and Transformer-based architectures. We demonstrate substantial performance improvements over previous baselines, and release new comprehensive benchmark datasets including AC-19 (125,192 AC-trivial presentations of varying difficulty with length at most 19) and AC-1M (1,136,154 hard AC-trivial presentations of length at most 30), the first large-scale, publicly available datasets of this kind.

---


### 237. [Cross-Modal Corroboration for Annotation-Free Wildlife Monitoring](https://arxiv.org/abs/2606.21613)

**<font color=#1a73e8>作者：</font>** Bharath Pillai, Varun Viswapriyan, Christopher Stewart 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scaling wildlife monitoring for real-world conservation deployments requires automated analysis of smart sensors that operate under severe annotation scarcity. We propose leveraging expert knowledge of species activity patterns as an annotation-free validation signal for multimodal monitoring pipelines. We operationalize agreement as the alignment of independently derived hourly activity curves both with each other and with published behavioral priors-a three-way convergence that rules out shared-data confounds and dataset-internal correlation as alternative explanations. Our vision pipeline combines zero-shot species detection via BioCLIP 2, sliced inference to handle deployment-constrained camera positioning, and geometry-based geographic localization from camera trap imagery. Our acoustic pipeline detects species vocalizations via a fine-tuned classifier. We validate the pipeline on a breeding herd of Milu deer and demonstrate that both modalities independently recover activity patterns consistent with known deer behavioral ecology with minimal manual annotation. The framework applies to species detectable in both visual and acoustic modalities for which behavioral priors are documented in the literature, suggesting a practical path toward self-validating wildlife-monitoring pipelines at conservation scale.

---


### 238. [Voluntary Triggering of Shared-Autonomous Prosthetic Control via IMU-Based Motion Gestures](https://arxiv.org/abs/2606.21620)

**<font color=#1a73e8>作者：</font>** Aabira Zaman, Kaijie Shi, Xianta Jiang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recently, a shared-autonomous scheme has been introduced into prosthetic hand control field, where the user provides high-level intent by moving the hand towards the target, and the artificial intelligence system autonomously executes low-level control (e.g., grasp and release the object). This system reduces user workload but risks unintended grasp or release actions without explicit user control. In particular, release actions remain challenging, as vision-based autonomous systems typically assume that proximity to a supporting surface signals the user's intent to let go, making mid-air release tasks difficult and error-prone. This study presents an inertial measurement unit (IMU)-based gesture-triggered interface enabling voluntary initiation or override of grasp and release actions to the autonomous system. A real-time motion detection algorithm recognizes three deliberate upper-limb gestures: shoulder shrug, elbow flap, and wrist shake, across three control paradigms: autonomous, hybrid, and manual. In a controlled study with 14 able-bodied participants and one individual with an upper-limb difference, the elbow flap emerged as the most preferred gesture (66% preference) and achieved 95% mean successful rate. Manual mode produced the highest accuracy (95%), while autonomous mode and hybrid mode were most preferred for daily use (38%). Results suggest that IMU-based voluntary triggers enhance alignment between user intent and prosthetic action, improving reliability and perceived control. This approach offers a practical pathway toward safer, more adaptable prosthetic systems and can be extended to real-world applications requiring rapid, intentional overrides of autonomous behavior.

---


### 239. [Evaluating Document-Tuned Transformer Representations for Person-level Mental Health Assessment](https://arxiv.org/abs/2606.21622)

**<font color=#1a73e8>作者：</font>** Aaron Marker, Oscar Kjell, Vasudha Varadarajan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Person-level psychological assessment requires aggregating meaning across many messages from the same individual, a task that document-level training objectives were not explicitly designed for. We present a systematic, empirical comparison between architecturally matched traditional (a) base-transformers and (b) document-tuned-transformers (further contrastively fine-tuned at the document-level, sometimes referred to as "sentence transformers") under otherwise identical conditions. Comparing layer-wise and overall performance across two longitudinal mental health and psychological datasets, we find document-tuned models demonstrated a consistent improvement over base representations (increase in Pearson r of 13.4%, p=.015). Robustness analyses revealed document-tuned models remained more accurate under perturbations to word deletion, synonym replacement, typo injection, and back translation. Further, hedged language (e.g., `usually') was more characteristic of outcomes in document-tuned embeddings while abundance (e.g., `lot') was more characteristic of base-transformers, suggesting document-tuned models may better capture uncertainty. These results suggest representation choice impacts mental health prediction, document-tuned models often being more adept.

---


### 240. [A DVDrive Approach for doScenes Instructed Driving Challenge](https://arxiv.org/abs/2606.21623)

**<font color=#1a73e8>作者：</font>** Zijian Fu, Xiangyang Chu, Mengshi Qi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-conditioned trajectory prediction is an emerging problem in autonomous driving, where a model predicts the future ego trajectory not only from visual scene context and historical motion, but also from a natural-language maneuver instruction. This paper presents our submission to the doScenes Instructed Driving Challenge, built upon OmniDrive, a vision-language-action driving agent with 3D perception, reasoning, and planning capabilities. We adapt OmniDrive to the doScenes setting by training it on instruction-annotated nuScenes scenes and generating a 6-second ego trajectory represented by 12 future waypoints. To improve multi-view visual grounding, we further introduce a DVPE-style divided-view perception module into the OmniDrive perception head. Instead of attending globally to all camera features, the proposed module groups query features and image tokens into divided local view spaces and performs visibility-aware cross-attention within each view. This design reduces irrelevant cross-view interference and helps the model better align language instructions with local driving-relevant visual evidence. The code is publicly available at: this https URL.

---


### 241. [A new classification method based on Minimum Spanning Trees](https://arxiv.org/abs/2606.21639)

**<font color=#1a73e8>作者：</font>** Julio González-Díaz, Beatriz Pateiro-López, Iria Rodríguez-Acevedo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Minimum Spanning Trees have been used in unsupervised learning, particularly in clustering tasks, due to their ability to recognize clusters by removing edges that are considered inconsistent in defining those clusters. This paper aims to study the use of Minimum Spanning Trees in supervised learning. Specifically, we propose a classification algorithm based on Minimum Spanning Trees. To improve its performance, we introduce a robust version of the method that is also computationally more efficient. We evaluate the effectiveness of our proposed method through an extensive simulation study. We also apply the proposed methodology to a real-world case study involving aircraft trajectories.

---


### 242. [ChainWorld: Composing Long-Horizon Desktop Workloads from Atomic OSWorld Tasks](https://arxiv.org/abs/2606.21654)

**<font color=#1a73e8>作者：</font>** Vincent Siu, Manasi Sharma, Dawn Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer use agents are evaluated almost exclusively on atomic desktop tasks, but realistic desktop work requires sustaining state across multiple objectives. We study this gap with ChainWorld, which composes atomic OSWorld tasks into long horizon desktop workloads through directional compatibility search while preserving the source evaluators. The resulting workload contains 347 chains of length two to four and compares two renderings of the same task sequence. In single turn evaluation, all tasks are presented together in one prompt. In multi turn evaluation, tasks are revealed one at a time. Across four current computer use agents, maximum chain completion is 31%. Multi turn evaluation improves completion for three models, but both protocols remain challenging. The two protocols also expose different failure profiles. Single turn failures concentrate on artifact precision, while multi turn failures more often reflect session management problems such as fragmented progress and later turn disengagement.

---


### 243. [Chehre: An Emoji-Prompted Video Dataset for Perceptually Diverse Facial Expression Recognition](https://arxiv.org/abs/2606.21657)

**<font color=#1a73e8>作者：</font>** Bita Azari, Zoe Stanley, Avneet Batra 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial expressions are nonverbal social signals used in human interaction, but facial expression recognition datasets often focus on static images, basic emotion categories, or single deterministic annotations. We introduce Chehre, an emoji-prompted video dataset for analyzing dynamic facial expressions across a wide range of expressions for exploring inter-individual perceptual diversity. In Chehre, participants were prompted to express and record 40 facial emojis. Later, their facial motions were transferred onto synthetic faces to preserve privacy. A separate group of annotators analyzed the anonymized videos using emoji and label annotations, resulting in 2,111 high quality videos collected from 203 performers and validated by 902 annotators. We define two benchmark tasks: dominant expression recognition, which tests whether models recover the top human-rated labels, and distributional expression recognition, which tests whether models capture the diversity of human responses. We benchmark recent vision-language models using random sampling and persona prompting to generate multiple predictions per video. Results show that both tasks are challenging: among the models evaluated, the best-performing model achieves only 32.5% Top-1 accuracy on dominant expression recognition and a Spread Ratio well below the human reference on distributional recognition. Chehre provides a benchmark for evaluating diverse, dynamic, and distributional facial expression recognition

---


### 244. [UnityShots: Memory-Driven Multi-Shot Audio-Video Generation with Boundary-Aware Gating](https://arxiv.org/abs/2606.21661)

**<font color=#1a73e8>作者：</font>** Jiehui Huang, Yuechen Zhang, Bin Xia 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating a coherent multi-shot video requires structured cross-shot memory. Subject appearance, scene context, and speaker identity must persist across cuts. Existing approaches either train end-to-end over fixed-length sequences and cannot scale, generate shot-by-shot with memory banks that grow linearly, or orchestrate pretrained generators under an LLM planner without a multi-shot-aware backbone. We present UnityShots, a memory-driven multi-shot audio-video generation system built on LTX-2.3, trained on annotated cinematic and music-video shots. The video stream maintains two fixed-size slots, a long-term memory (LTM) slot anchored to the opening shot and a short-term memory (STM) slot holding the immediately preceding tail, both updated at every cut by a boundary-conditioned gate that fuses visual cut probability and beat-tracker signals. The audio stream injects a reference speaker token at every shot to preserve vocal timbre without a sliding audio bank. A discrete cut-type prior, learned through AdaLN, becomes an inference-time control knob over transition strength. We release a benchmark of $200$ multi-cultural multi-shot sequences spanning six ethnic regions and ten or more languages, with per-shot reference identities, reference audio, and per-boundary transition labels. Evaluated across I2V, T2V, and R2V conditioning modes, UnityShots leads open-source baselines on every cross-shot coherence metric and matches the strongest closed-source system on the multi-shot axes.

---


### 245. [Measuring What Matters: A Quantitative UX Evaluation Framework for AI-Assisted Home Search](https://arxiv.org/abs/2606.21663)

**<font color=#1a73e8>作者：</font>** Matilda Nkoom  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-assisted conversational search is rapidly displacing filter-based interfaces across the major home search portals. Redfin's deployment of conversational search produced a 47\% lift in tour requests, and Zillow launched "AI Mode" in March 2026. Recent consumer surveys indicate that a large majority of Americans now use AI tools for housing market information. Yet the evaluation frameworks practitioners apply to these products remain borrowed from general-purpose usability testing, tools designed for deterministic, filter-driven interfaces that do not capture the distinctive failure modes of AI-driven experiences. This paper proposes a four-layer quantitative evaluation framework purpose-built for AI-assisted home search: recommendation system quality, interaction efficiency, attitudinal measurement, and trust calibration. For each layer, validated instruments, production-derived benchmarks, and practitioner-ready implementation guidance are provided. A minimum viable metric set and a worked example illustrating the framework's application to a mid-sized portal are included to support immediate adoption.

---


### 246. [A Framework for Directed Acyclic Hypergraph Learning](https://arxiv.org/abs/2606.21668)

**<font color=#1a73e8>作者：</font>** Zhiyuan Dong, Carlos Mundo-Levano, Wei Qian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous optimization methods for learning Directed Acyclic Graphs (DAGs) operate on weighted adjacency matrices and are therefore limited to pairwise causal relationships. We propose a framework for learning Directed Acyclic Hypergraphs (DAHGs) from observational data, capturing joint parental influences that pairwise models cannot represent. Our approach rests on three components: (i) a generalized linear structural equation model (SEM) with multiplicative interaction terms whose non-zero weights correspond one-to-one with directed hyperedges; (ii) a weighted adjacency tensor representation whose acyclicity is characterized via nilpotency under the tensor t-product; and (iii) a differentiable acyclicity constraint derived through the Fourier decomposition of the t-product, which reduces tensor nilpotency to slice-wise matrix nilpotency and enables least-squares learning via the augmented Lagrangian method.

---


### 247. [Enlight: Fast Low-Light Image Enhancement via Multi-Objective Optimization and Shadow-Aware Refinement](https://arxiv.org/abs/2606.21674)

**<font color=#1a73e8>作者：</font>** Nirjhor Datta, M. Sohel Rahman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present ENLIGHT, a fast and training free framework for low-light image enhancement based on direct optimization of a perceptual objective. Unlike deep learning approaches that require large scale training data and supervision, ENLIGHT operates in a zero-shot manner by optimizing image quality at inference time. The method employs a two stage global to local optimization strategy. In the first stage, ENLIGHT performs global illumination adjustment to improve visibility while maintaining structural consistency and avoiding excessive noise enhancement. In the second stage, a shadow aware refinement selectively improves low-intensity regions through masked local optimization, enhancing visibility without overexposure. To balance quality and efficiency, we introduce two modes: Fast, which uses a multi-objective formulation combining entropy, gradient preservation, and noise regularization, and Ultrafast, which reduces computational cost via a lightweight approximation of the same objective. The framework is optimizer agnostic and supports both evolutionary and lightweight local search methods. Experiments on BAID, Backlit300, LIME, MEF, NPE, and DICM demonstrate that ENLIGHT achieves competitive perceptual quality (MUSIQ, NIQE, BRISQUE) with significantly lower inference time. Qualitative results further show improved contrast, preserved structural details, and controlled noise amplification, making ENLIGHT a practical and interpretable alternative to learning based methods.

---


### 248. [Decodable but Not Faithful: Coupling Natural-Language Rationales to Programmatic Verifiers](https://arxiv.org/abs/2606.21678)

**<font color=#1a73e8>作者：</font>** Vatsal Ananthula, Adarsh Kumarappan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models can generate plausible rationales for their predictions, but these explanations may not faithfully represent the model's internal reasoning. We propose verifier-coupled reasoning, a framework that inserts inline claims into reasoning traces and trains an auxiliary consistency head to predict programmatic verifier outputs from rationale-span hidden states. The central finding is a gap between decodability and faithfulness: consistency training reliably makes verifier information decodable from rationale representations, but decodability does not guarantee faithful generation. In LeanCheck (formal theorem proving), rationale-only and proof-only pooling achieve perfect directional separation under counterfactual conflict. In KataGo (Go engine), commentary spans encode 10-way win-rate buckets at 81% accuracy. Yet in a code setting, the model achieves 98.6% coupling while its generated explanations remain unfaithful: fluent prose with correct structured claims, but describing unrelated algorithms; a controlled pretrained-vs-from-scratch comparison shows the gap is not capacity-driven. Synthetic activation patching confirms causal influence (73-89% vs. 31% baseline), FEVER reveals that evidence-only pooling isolates genuine evidence sensitivity at the cost of raw accuracy, and per-claim analysis shows that consistency loss disproportionately benefits fine-grained claims over binary ones. These results establish that consistency losses are effective diagnostics and representation-shaping tools, but not sufficient conditions for faithful reasoning.

---


### 249. [Expressivity Saturation: Reduced Affine Region Usage Under Increasing Task Complexity](https://arxiv.org/abs/2606.21687)

**<font color=#1a73e8>作者：</font>** Xuan Qi, Yi Wei, Fanqi Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Piecewise-affine neural networks (e.g., with ReLU or LeakyReLU activations) implement continuous piecewise-affine maps, and the number of affine regions provides a natural proxy for expressive capacity. However, the gap between theoretical region capacity and the affine regions realized after training remains insufficiently understood. We study this gap from two complementary perspectives. First, we give a rigorous, architecture-dependent theorem for affine line-segment probes: for multilayer perceptrons with piecewise-affine activations, the number of affine pieces realized along an affine line-segment probe is upper bounded by an explicit product of layer-wise width terms (and activation breakpoint factors). This yields a neuron-threshold lower bound for representing target functions with prescribed one-dimensional piece complexity, formalizing the minimal region budget required for complex signals. Second, we exactly enumerate affine regions realized within bounded 2D and higher-dimensional domains under controlled task complexity. Under fixed architectures and training protocols, increasing input--label complexity yields trained solutions with markedly fewer realized regions in the evaluation domain, even though worst-case architectural capacity is unchanged; we call this reduced region usage expressivity saturation. Moreover, in the most challenging regimes, 2D visualizations show that region-usage collapse often coincides with degraded decision boundaries. Finally, we visualize the training dynamics of affine-region partitions and decision boundaries, revealing a consistent refinement process during optimization.

---


### 250. [A Hybrid, Multi-Layered Pipeline for Phishing and Threat Classification: Independently Validated URL and NLP Engines with a Calibrated Multi-Channel Fusion Stage](https://arxiv.org/abs/2606.21690)

**<font color=#1a73e8>作者：</font>** Saifelden M. Ismail, Aser O. Ibrahim, Omar A. Mahmoud  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Phishing is a multi-modal threat. We present a hybrid pipeline that scores each modality with its own engine and fuses the results. Three engines are built, deployed, and independently benchmarked: a four-stage URL stack (Domain Guard, lexical model, threat intelligence, and an asymmetric L2 fusion sidecar); a generalization-hardened DistilBERT NLP classifier whose held-out real-phishing recall rises from 0.8% to 87.3%; and a threat-intelligence synchronizer with end-to-end OpenTelemetry instrumentation confirming 1:1 message conservation. A decision-level fusion stage, characterized on a 10,677-email whole-system benchmark, reaches F1 = 0.914 with a calibrated probabilistic-OR over URL, header, and phishing-probability channels while cutting held-out real-spam false positives to 3.6%. Because that benchmark uses proxy URL and header channels and an operating point still needing recalibration, we present it as a preliminary integrated result. The binding constraint for deployable detection is generalization rather than same-distribution accuracy.

---


> [!TIP]
> 当前位于：**201-250**（第 5/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
