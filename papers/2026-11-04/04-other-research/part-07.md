# 📦 其他研究 | 2026年11月04日

> 本类共 **633** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

---

### 301. [CST: Lightweight Risk Triage with Source-Grounded Evidence for Web Discussions](https://arxiv.org/abs/2611.01710)

**<font color=#1a73e8>作者：</font>** Zhihua Wang, Yifeng Gao, Yunhao Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web communities rely on moderators to catch harmful messages such as insults, hate speech, and scams, but no one can read every message. Existing tools give each message a risk score, which tells moderators where to look but not what to read or how to check it. Yet meaning depends on context: the same reply, "I agree.", can support or oppose removing someone from a group. Moderators therefore need source-grounded evidence, not just scores: a few key messages kept with their original wording and replies. We present CST, a lightweight triage pipeline that first decides where to look, then what to show. It scores risk by pairing character patterns, which capture exact wording, with sentence meaning from a fixed multilingual model, so it handles several languages and runs on an ordinary CPU. It then groups related messages and picks from each group in turn, so a small reading budget covers different parts of a discussion, and links every pick back to the original thread. Across six tasks from five datasets in several languages, CST ranks harmful messages more accurately than a fully fine-tuned multilingual model and, under the same budget, finds more of them than reading by score alone. In a user study, reviewers needed at least 27% less time with CST's grouped evidence while keeping decision accuracy above 94%. CST turns risk scores into evidence that moderators can read quickly and check in context. Code and dataset reconstruction resources will be released at this https URL.

---


### 302. [When Disagreement Labels Do Not Identify F1 Rankings](https://arxiv.org/abs/2611.01712)

**<font color=#1a73e8>作者：</font>** Roberto Fernández-Barrios, Iker Pastor-López, Asier González-Santocildes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agreement labels cancel from an accuracy comparison but can change an F1 ranking. We specialize partial identification to an explicit audit after labeling disagreements: two agreement counts give exact bounds, certifying a ranking or a choice within a specified F1 tolerance under every completion. Across 3,200 frozen model pairs, shared completions tighten bounds and a 0.01 tolerance reduces labeling costs. A zero-loss (weak-winner) control attributes most savings to positive tolerance, not ties. Guarantees concern the evaluated batch, not future data.

---


### 303. [A sensor-driven physics-informed neural network for real-time occupant-centric space heating control](https://arxiv.org/abs/2611.01723)

**<font color=#1a73e8>作者：</font>** Yunfei Bai, Chenghao Li, Sunku Prasad Jenne 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional space heating systems typically rely on single or sparse fixed-point temperature measurements, overlooking non-uniform indoor temperature distributions, transient thermal dynamics, and occupant-specific comfort requirements. This study explores an occupant-centric control strategy that aims to maintain the desired temperature around the occupant location. Spatially and temporally varying temperature fields, together with occupant mobility, make real-time local temperature estimation challenging. To address this challenge, we propose a control-oriented Physics-Informed Neural Network (PINN) model for indoor temperature-field prediction. Conventional PINNs rely on explicit time inputs and assume consistent temporal patterns across samples, which limits adaptability under variable initial conditions and heating sequences. The proposed model infers temporal dynamics implicitly from spatial coordinates and limited sensor measurements, improving robustness to changes in initial conditions and external disturbances. The method was validated across nine horizontal sensing planes in three controlled room-scale configurations. Against a validated COMSOL Multiphysics simulation, the PINN predicted the evaluated temperature fields with a maximum relative error below 1.85% across validation cases. These predictions supported an occupant-centric space heating control scheme. Compared with COMSOL-based offline control, the PINN-based system achieved an average prediction error of around 0.67%, and its rapid inference supports real-time occupant-centric control implementation. This work represents a move away from reliance on fixed-point temperature measurements in space heating control to an occupant-centric control strategy informed by real-time environmental feedback.

---


### 304. [Deep Learning for Cervical Cytology Screening: Methods, Algorithms, Challenges and Prospects](https://arxiv.org/abs/2611.01730)

**<font color=#1a73e8>作者：</font>** Jiang Yangbo, Zheng Nenggan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cervical cancer remains a leading cause of cancer death among women, with more than 90\% of deaths occurring in low- and middle-income countries, where cytology screening is constrained by a shortage of trained cytopathologists. Deep learning has made automated cytology screening increasingly feasible, but the literature is fragmented across cell, patch and whole-slide-image scales, task formulations and supervision regimes, hindering comparison and clinical translation. This Review synthesizes the deep learning literature for cervical cytology screening, organizing the field along three axes---data scale, functional task and supervision---and distinguishing two clinical roadmaps: whole-slide-image confidence aggregation and cell-level detection with Bethesda classification. We examine 16 publicly available or publicly documented cytology datasets alongside the CAISHI histopathology dataset, compare quantitative performance while exposing incomparable metrics and data leakage, and assess commercial systems, regulatory status, HPV-era screening pathways and low-resource deployment. Single-cell accuracy on Herlev and SIPaKMeD has plateaued, but this reflects benchmark saturation rather than clinical readiness; prospective and randomized evidence is emerging but remains limited. We consolidate the evidence into five challenge areas---data and benchmarks, architecture and label-efficient learning, trustworthy AI, clinical translation and health economics, and evaluation and reproducibility---and provide an evidence-to-agenda map and a deployment decision matrix. Progress now depends on multi-center benchmarks, externally validated label-efficient methods, calibrated and fair predictions, and pragmatic clinical trials rather than further gains on saturated single-cell benchmarks.

---


### 305. [Robust EEG-based Emotion Recognition from Coarse Trial-level Labels under Intra-trial Affective Variability](https://arxiv.org/abs/2611.01731)

**<font color=#1a73e8>作者：</font>** Xiaocong Zeng, Buxuan Wang, Xin Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG-based emotion recognition has become an active research area in brain-computer interfaces. However, fine-grained affective annotation is costly, so most datasets provide only a global label for each long EEG trial. For practical emotion recognition, trials are commonly divided into short temporal windows, with the global label propagated to all windows for training. This practice treats trial-level emotion as temporally uniform, although affective responses may fluctuate within a trial. Consequently, windows that weakly reflect or deviate from the global emotional state may receive unreliable labels, posing a key challenge to robust EEG-based emotion recognition. To address this challenge, we propose VARY, a variability-aware robust learning framework for EEG-based emotion recognition from coarse trial-level labels. VARY incorporates a Two-stage Sample Selection (TSS) strategy to identify EEG windows with reliable emotional labels, and introduces MixAug, a data augmentation method tailored for EEG to improve model robustness under limited and unreliable supervision. We comprehensively evaluate VARY under the setting of label-noise learning on two public datasets, using three network architectures and multiple label-noise settings. Our method demonstrates superior performance, achieving a maximum accuracy gain of 11.54% on the DREAMER dataset and 5.39% on the SEED dataset compared with the best-performing baseline, highlighting the effectiveness of VARY in learning from unreliable trial-level labels under intra-trial affective variability.

---


### 306. [From Single-Agent Self-Discovery to Multi-Agent Adaptation: Scaling Laws of Partner Feedback and Convention Rigidity in Meta Reinforcement Learning Algorithms](https://arxiv.org/abs/2611.01742)

**<font color=#1a73e8>作者：</font>** Haomin Luo, Ersha Li  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> A key milestone toward Recursive Self-Improvement (RSI) is replacing hand-crafted optimizers with meta-learned update rules (such as Disco103 and OPEN) that discover how agents learn. Yet when a self-discovered RL model trains with adapting teammates, does co-evolution sustain capability gains or trap agents in brittle conventions? Across 1,800+ runs in continuous collective robotics (VMAS) and discrete coordination (Overcooked), we establish five laws of multi-agent adaptation. First, four-cell counterfactual partner swaps expose an evaluation illusion: apparent team progress often masks focal regression (+1.066 team gain concealing -0.119 focal loss) and inflates transfer by +0.649 to +1.210. Second, a 288-run physical-coupling sweep ($\alpha \in [0, 1.5]$) reveals a linear scaling law ($\beta = +0.255$, $p = 0.000488$, Spearman $\rho = 1.0$): live reciprocal feedback keeps Disco103 invariant (AUC 0.297--0.322), whereas severing feedback triggers a monotonic collapse (-0.172 to -0.490), with OPEN establishing a sensitivity spectrum (Disco103 > OPEN > MAPPO). Third, extending navigation training eightfold (1.05M steps) enables Disco103 to overtake MAPPO (+0.087 team return, +0.133 bank gain), while decoupled training boosts cross-partner completion by +10.16% (56.25% vs. 46.09%). Fourth, in Overcooked, MAPPO's self-play conventions induce a 28.13% cross-partner collision rate, whereas Disco103 cuts collisions to 12.77% and achieves 3.33x higher bank return (9.96 vs. 2.99; net gain +6.43), further improved by decoupled meta-adaptation (+1.39 with scripted partners). Finally, perturbation pulses ($p=0.00098$), auxiliary entropy diagnostics (8.485 nats), and 48 multi-lifetime meta-evolved rules ($L_2 \in [2.11, 4.91]$) trace these dynamics to partner-gradient blindness and auxiliary drift, informing multi-agent self-discoverd algorithms.

---


### 307. [A Deep Reinforcement Learning Framework for Real-Time Electric Vehicle Charging Management in IoEV-Enabled Smart Cities](https://arxiv.org/abs/2611.01751)

**<font color=#1a73e8>作者：</font>** Nour-Eddine Moumni, Rachid Alaoui, Driss Kiouach  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid growth of electric vehicles (EVs) in urban environments demands intelligent, decentralised charging management strategies that operate under strict real-time constraints. This paper proposes an Edge-Intelligent architecture in which each EV selects a charging station (CS) by querying a shared, centrally trained Deep Q-Network (DQN) policy over a lightweight MQTT publish-subscribe backbone; independent per-EV edge inference is the deployment target, not the configuration evaluated here. The reported simulation evaluates that shared DQN policy applied sequentially to each vehicle's observations within a single SUMO run, using MQTT for KPI telemetry while observations are obtained through TraCI. The system is evaluated on two real-world road networks from OpenStreetMap (Rabat Agdal-Hay Riad and Tangier, Morocco); the primary network carries four geolocated public charging stations with heterogeneous power levels (50 kW and 150 kW). Three traffic demand profiles (morning, midday, evening peak) are simulated, and four decision policies are compared: an Adaptive Heuristic, a Tabular Q-Learning agent, the proposed DQN agent, and a Double DQN variant. A multi-seed statistical protocol (7 seeds, Wilcoxon signed-rank test, Cohen's d) evaluates the results. The DQN agent achieves a 6.8% relative improvement in charge rate and a 5.4% increase in delivered energy over the Adaptive Heuristic under Evening Peak demand ($p = 0.016$, Cohen's $d = 0.99$ and $1.51$), while showing no advantage in waiting time; on the second network the heuristic leads on waiting time, so the ranking is not stable across geographies. A scalability analysis shows linear state-space growth with station count and sub-millisecond inference; all runs include intermittent station outages under a Markov failure process.

---


### 308. [ReCoG: Relative Node Contexts for Multi-Domain Graph Pre-training](https://arxiv.org/abs/2611.01753)

**<font color=#1a73e8>作者：</font>** Yupeng Tong, Lianze Shan, Jitao Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The success of foundation models in language and vision has motivated Graph Foundation Models (GFMs), which learn transferable knowledge through multi-domain graph pre-training. Existing methods advance GFMs through feature unification and structural learning, and in doing so they rely on the raw graph structure to organize node contexts. However, we observe that removing a large proportion of edges from source graphs during pre-training improves cross-domain transfer accuracy across four representative methods. Our theoretical analysis identifies the raw graph structure as a source of conflict in cross-graph model sharing. We therefore advocate defining node contexts using criteria consistent across graphs. Achieving this requires (1) constructing node contexts consistently across graphs without a shared positional structure, such as the token order of text or the pixel grid of images, and (2) retaining the structural and neighborhood information of the original graphs. To this end, we introduce Relative Contexts for Graphs (ReCoG) for multi-domain graph pre-training. Specifically, we first construct attribute contexts to provide a comparison rule independent of the raw graph structure. Furthermore, we construct structural contexts based on common neighbors and semantic contexts based on neighborhood attribute summaries to retain the topological and neighborhood information of the original graphs. Since all graphs share these construction rules, we pre-train a single graph encoder by reconstructing node attributes over these contexts, without domain-specific modules. We conduct extensive experiments on 18 target datasets, which demonstrate the effectiveness of ReCoG. In particular, ReCoG exceeds the strongest baseline by 7.61 percentage points in mean 1-shot cross-domain node classification accuracy and by 4.47 points in cross-type transfer to heterophilous graphs.

---


### 309. [A Bounded Evaluation Protocol for Representational Systematicity](https://arxiv.org/abs/2611.01755)

**<font color=#1a73e8>作者：</font>** Boyu Cao, Wenshuo Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multiple studies have shown that neural networks can be behaviorally systematic, producing correct outputs for novel combinations of familiar parts. Whether they are also representationally systematic, that is, whether they represent these parts and their roles and use them to produce the outputs, remains hard to test, because each kind of evidence can mislead on its own: correct outputs can come from shortcuts, a decodable signal need not be used, an intervention can act through unintended pathways, and a failed search does not show absence. We propose a bounded evaluation protocol for representational systematicity (Bounded-RS): for an explanation that attributes a systematic behavior to a declared representation, it tests on a matched behavioral contrast whether that representation is recoverable and whether it is causally used, checks the validity of this evidence, and assigns the explanation one of four bounded states, Unsupported, Present-only, Causal-use, or Undetermined, through control-calibrated scores, gates, and stop rules. On a semantic-parsing testbed of 96 matched sets that we release, the tested role-filler Binding explanation of fine-tuned T5 models is Causal-use and the distributed Geometry explanation is Unsupported within its declared search space, verdicts that hold across calibration-compatible parameter configurations, training seeds, and T5-base. On 41 cases with known causal status, full adjudication licenses a false Causal-use in 1 of 34 noncausal cases, against 13 when recoverability is taken as use, without missing any causal case. Bounded-RS thus turns the question of representational systematicity, debated since Fodor and Pylyshyn, into comparable and falsifiable verdicts on declared explanations, each reported with the evidence pattern that licenses it and, for a negative, the search space that bounds it.

---


### 310. [Teleoperation System for Service Robots using Virtual Reality Headset and Pose Estimation](https://arxiv.org/abs/2611.01759)

**<font color=#1a73e8>作者：</font>** Eduardo Fernandes, Tiago Ribeiro, Antonio Ribeiro 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a teleoperation system for service robots that integrates human pose estimation with virtual reality (VR) to enable intuitive remote control. By using the Mediapipe framework for 2D pose detection and extending it with RGB-D data from the Intel RealSense D455 camera, a comprehensive 3D human pose estimation is achieved. This data is then mapped to the robot's kinematics, allowing the operator to control the robot's movements naturally. A VR interface was developed to provide an immersive perspective, enhancing the operator's situational awareness. Real-world experiments were conducted using the CHARMIE service robot to validate the system's effectiveness in tasks involving object manipulation. While the current system successfully demonstrates the potential of VR-based teleoperation, challenges remain in accurately capturing certain joint angles (e.g., wrist yaw) and ensuring precise mapping between human and robot movements. Future work includes the integration of inertial measurement units (IMUs) for improved rotational tracking and the implementation of more advanced control algorithms. Overall, this research contributes to the development of more intuitive and effective teleoperation systems for service robots, facilitating their deployment in complex and dynamic environments. This work further introduces a novel approach to teleoperation by combining RGB-D sensing with an innovative algorithm for real-time joint angle computation using Mediapipe, enhancing the precision of human-robot motion mapping and enabling immersive control through a VR interface. These contributions represent significant advancements in the field of human-robot interaction, particularly for service robot applications.

---


### 311. [Silent Reward and Environment Defects in EV Charging Simulation Benchmarks: A Diagnostic Checklist](https://arxiv.org/abs/2611.01769)

**<font color=#1a73e8>作者：</font>** Nour-Eddine Moumni, Rachid Alaoui, Driss Kiouach  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement-learning (RL) benchmarks built on microscopic traffic simulators such as SUMO are increasingly used to compare agent architectures for electric vehicle (EV) charging assignment. Unlike crashes, defects in the reward function, the environment's stochastic model, or the state encoding often fail silently: the simulation completes, produces plausible numbers, and the comparison is biased. We report five such defects, found by auditing a five-agent benchmark on OpenStreetMap road networks, stated generically: a shared random generator that desynchronises seed-paired comparisons, an ablation-specific reward clip applied unconditionally, a normalisation mismatch that zeroes a reward term, a per-timestep penalty that should fire once per event, and a state dimensionality documented but never wired into the network. We quantify three: a rejection counter inflated up to 125x across agents/cities, a reward term bounded at about $10^{-4}$ of its intended scale, and a 16.6%/16.3% greedy-action divergence from a state-encoding mismatch. Re-analysing a historical ablation, no A1-A2 effect survives family-wise correction; a 56-run campaign confirms the RNG defect's mechanism directly while showing its correction does not change that conclusion. We provide an eight-item checklist as a low-cost first-pass audit; in a later regeneration, three checks caught two new defects while three further process/artefact defects fell outside its boundary.

---


### 312. [Spectral Signatures of Memorization Basins in Diffusion Trajectories](https://arxiv.org/abs/2611.01775)

**<font color=#1a73e8>作者：</font>** Achref Jaziri, Martin Mundt, Ahmed Imtiaz Humayun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models are known to reproduce individual examples from their training data as a form of memorization with implications for generalization, privacy, and downstream use. Recent work demonstrated that memorized training samples reside inside contiguous regions of the data/latent space known as basins of memorization -- once a denoising trajectory enters a basin, under finite perturbations it irreversibly reproduces a memorized example. Prior empirical work on such basins in trained models has primarily focused on classifier-free guidance based detection and mitigation strategies in text-to-image models, leaving basin entry and their formation largely uncharacterized. In this paper, we present a geometric characterization of memorization basins for conditional, unconditional, and rectified-flow-based diffusion models. We observe a characteristic signature in the local spectrum of the function geometry that distinguishes basin entry: the emergence of a dominant singular mode followed by a sharp spectral recovery. This signature appears at two timescales: along denoising trajectories during inference and over the course of training. We further investigate whether these geometric signatures can be used to intervene on memorization. During training, we suppress memorization by acting on the dominant mode. At inference, we develop methods to identify trajectories entering memorization basins and steer them away. We find that these interventions remain effective even with low-dimensional approximations of the underlying geometry, and demonstrate that geometry-informed steering extends to large-scale text-to-image diffusion models. Together, our results corroborate that local spectral geometry provides a common basis for characterizing memorization and for suppressing, detecting, and steering away from it across training and generation.

---


### 313. [OCBI: Order-Sensitive Cross-Branch Interaction for Image Manipulation Localization](https://arxiv.org/abs/2611.01783)

**<font color=#1a73e8>作者：</font>** Zhouli Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image manipulation localization combines semantic structure with forensic traces to identify modified pixels. Within-branch spatial mixing and RGB-guided cross-branch mixing can produce different messages when composed in opposite orders. We propose OCBI, an extension of Co-Transformers that models the discrepancy between these two composition orders for localization. A local cross-branch fusion module uses the commutator of RGB-guided cross-attention and forensic self-attention to add a learnable signed correction to feature transfer. Pixelwise adaptive multiscale aggregation then combines spatial contexts before prediction. OCBI uses the Co-Transformers backbone and supervision. We compare OCBI with retrained Co-Transformers using CASIA-only task training, a 50-epoch budget, and final-epoch evaluation. Across five clean test datasets, OCBI achieves a macro PixelF1 of 0.5773, exceeding the baseline by 0.43 percentage points. Under JPEG compression, Gaussian blur, and resizing on three datasets, its average PixelF1 over 21 dataset-transformation conditions exceeds the baseline by 0.95 percentage points.

---


### 314. [Detection Instead of Inversion: T1-T2 Microstructure Quantification With Detection Transformers](https://arxiv.org/abs/2611.01790)

**<font color=#1a73e8>作者：</font>** Sebastian Endt, Fatih Özkan, Marion I. Menzel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> T1-T2 correlation MRI has strong potential to quantify microstructural compartments without imposing a biological model. Traditionally, full T1-T2 spectra per voxel are reconstructed with an ill-conditioned and time-consuming Inverse Laplace Transform. We propose to view this challenge as an object detection task: A Detection Transformer (DETR) takes 64 TI/TE signals and directly predicts a set of compartments specified by T1, T2, and signal fraction. We achieve a mean average precision mAP@10 of 76.8% on simulated data, outperforming both our previous model design (53.8%) and regularized NNLS (66.1%). We show that our DETR approach outperforms NNLS in almost every setting across compartment count, compartmental signal fraction, and SNR. Reconstruction is orders of magnitude faster than NNLS. The results are fully reproducible from our public code: this http URL

---


### 315. [RIFT: Residual-Informed Flow Transfer for One-Step Generative Video Compression](https://arxiv.org/abs/2611.01791)

**<font color=#1a73e8>作者：</font>** Qizhe Wang, Jiaye Fu, Feng Ye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video generation have enabled generative video compression to reconstruct details lost during coding using pretrained spatiotemporal priors. However, a substantial gap remains between codec-induced degradation and the perturbation trajectories learned by flow-matching models. In this paper, we identify a compression-dependent directional mismatch that degradation-strength-based timestep calibration alone cannot resolve. Compressed latents remain strongly aligned across codec operating points, while their reconstruction residuals vary substantially in magnitude and direction. To bridge this gap, we propose RIFT, a Residual-Informed Flow Transfer framework for one-step generative video compression. At its core, RIFT introduces a Residual Geometry Inducer (RGI) that converts the pretrained flow prediction into a content-adaptive restoration update using decoder-visible codec cues. RGI integrates flow-timestep conditioning with a learned full-band residual-strength estimate and content-conditioned direction and gain modulation, aligning the orientation and magnitude of the update with the compression-dependent residual geometry. Extensive experiments on three public video compression benchmarks show that RIFT outperforms competing generative video compression methods. The code is publicly available on RIFT.

---


### 316. [Reddit Community Signals as a Supplementary Domain-Reputation Feature in Spam Classification: A Conservative Controlled Evaluation](https://arxiv.org/abs/2611.01813)

**<font color=#1a73e8>作者：</font>** Fatima Salcedo, Jide Edu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Email spam and phishing remain persistent threats, and purely algorithmic classifiers may struggle with unfamiliar senders, evolving message content, and cold-start domains. This study evaluates whether Reddit-derived community signals can serve as a supplementary domain-reputation feature in email spam classification. We use a preprocessed SpamAssassin-derived corpus of 5,582 emails and compare three feature configurations: (1) a baseline using TF-IDF and structural features; (2) a traditional-enhanced configuration adding urgency and action scores; and (3) a Reddit-enhanced configuration adding a binary discussion-presence indicator, a keyword-based Reddit score, and an urgency-Reddit interaction term. We train Logistic Regression, Random Forest, and Support Vector Machine models. In the preliminary single-split evaluation, the Random Forest model with Reddit-enhanced features achieves 97.94% accuracy, a 0.55 percentage-point improvement over the baseline, although the improvement is not statistically significant in the primary test split. Logistic Regression performance declines when additional features are introduced, and the SVM performs poorly and is treated as a negative control. Reddit signals appear most informative for rare domains, but approximately 70% of emails receive no Reddit-derived signal. Because the Reddit data are temporally later than the email corpus, we do not interpret the results as evidence of real-time detection. Instead, the study provides a conservative evaluation of community-derived signals as a supplementary, asynchronous domain-reputation feature and identifies the additional validation required before production deployment, including domain-grouped validation, temporally aligned contemporary data, and adversarial robustness testing.

---


### 317. [When Does Latent Prediction Error Support Physical Surprise Claims in Video World Models?](https://arxiv.org/abs/2611.01815)

**<font color=#1a73e8>作者：</font>** Anton Hristov, Aleksandar Slavov, Vasil Vasilev  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prediction errors from video world models are often treated as physical surprise, but they can also reflect appearance, static content, motion, or ordinary prediction difficulty. We present an evaluation framework that separates what frozen representations contain, how they organize appearance and physical differences, and what changes a model's own prediction error. On IntPhys2, a benchmark of physically possible and impossible events, we compare representations from latent prediction, masked pixel reconstruction, and simple visual statistics. Appearance remains easy to decode, while V-JEPA2 exposes modest information about whether events are possible or impossible. Looking at the latent geometry, appearance changes become smaller compared with differences between videos, their directions line up more consistently across scenes, and their overlap with physical changes decreases in deeper layers. Across action-conditioned models, incorrect actions raise prediction error, while appearance changes also produce substantial responses. In Physion++ video clips, repeating a single frame can produce higher error than the original clip, while changing color throughout the clip can lower it. Using Kubric, a simulation and rendering framework, we find that impossible events can produce lower error than possible events. A fixed error threshold also incorrectly flags many possible events as impossible. A model can therefore represent physical information and respond to incorrect actions without its native prediction error reliably measuring physical surprise.

---


### 318. [CoGSeq-LTV: Scalable Missing-Aware Graph-Sequence Modeling for Multi-Business Transaction Analytics](https://arxiv.org/abs/2611.01817)

**<font color=#1a73e8>作者：</font>** Ziyang Su, Yao Zhou, Kelin Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-scale super-apps generate heterogeneous transaction logs in which users interact with multiple businesses, item identifiers are only partially available, and future value targets are sparse, heavy-tailed, and cumulative over time. We study multi-business, multi-horizon value prediction as a data-intensive analytics problem over such logs, rather than as a single-table task. (i) a batch-induced user-item graph that provides collaborative signals without materializing a global graph and remains applicable when item identifiers are missing through reserved unknown-item handling, (ii) business-aware sequence encoders that preserve recency, inter-event gaps, payment context, and goods-table availability, and (iii) cross-view contrastive alignment that transfers user-level intent across businesses while retaining business-specific temporal patterns. To handle zero-inflated and long-tailed cumulative targets, CoGSeq-LTV adopts a zero-inflated mixture log-normal head with MAE-aligned point supervision and validation-calibrated zero-aware inference. Experiments on the BiBiSheng transaction-log dataset show that CoGSeq-LTV improves over representative LTV baselines across businesses and horizons, including under a later out-of-time evaluation window.

---


### 319. [RCFormer: Reliability-aware Context Transformer for Occlusion-Robust Facial Landmark Detection](https://arxiv.org/abs/2611.01822)

**<font color=#1a73e8>作者：</font>** Ashish Kumar, Prashant Kumar, Mallika Garg  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial landmark detection has advanced substantially under regular imaging conditions, yet occlusion, poor illumination, and large pose changes remain major sources of error because local facial evidence can become incomplete or misleading. Context-guided latent patch recovery offers a promising way to address this issue by inferring unreliable patch representations from surrounding facial context before heatmap prediction. However, the recovered context can itself be unreliable when it is weakly adapted to the input face, influenced by corrupted neighboring patches, or blended without preserving local spatial coherence. We propose RCFormer, a Reliability-aware Context Transformer for occlusion-robust facial landmark detection. RCFormer strengthens latent patch recovery with three reliability-oriented components: visible-context conditioning (VCC), which adapts the context representation using a visibility-weighted global facial summary; visibility-guided context aggregation (VGCA), which reduces the influence of unreliable source patches during attention; and spatial residual correction (SRC), which refines blended latent features using neighboring patch information. The recovered heatmaps are then used as reliability-aware structural cues for existing landmark detection networks. Experiments show that RCFormer improves heatmap recovery and achieves strong landmark localization results on the WFLW, COFW, and 300W datasets.

---


### 320. [LUMEN: Geometry-Guided Diffusion Model for Spatially-Varying HDR Illumination Estimation](https://arxiv.org/abs/2611.01823)

**<font color=#1a73e8>作者：</font>** Hongze Chen, Fangyu Lin, Runze Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating scene illumination from images is challenging as lighting is inherently spatially varying, depending on geometry, occlusion, and light sources. Existing methods incorporate geometric cues by deriving local environment maps or probe-based representations, but largely rely on regression or parametric models, resulting in over-smoothed lighting and limited realism. We revisit spatially-varying illumination estimation from a generative perspective and introduce LUMEN, a geometry-conditioned diffusion framework for synthesizing high-dynamic-range (HDR) environment maps at arbitrary spatial locations from single or multi-view images. Specifically, we reconstruct a coarse 3D scene from input images and render partial environment maps at arbitrary locations to encode visibility and spatial structure. These signals are fused with multi-view image features and fed into a diffusion transformer to generate full HDR environment maps. To train the model, we build a synthetic dataset of 700 indoor scenes with dense spatial supervision, including multi-view RGB images, depth, and HDR illumination at multiple sampled locations. This dataset enables the model to learn spatially consistent lighting distributions across diverse scenes. Extensive experiments demonstrate that LUMEN significantly improves visual fidelity and spatial coherence compared to prior approaches.

---


### 321. [Z-Cache: Accelerating Diffusion Transformers via Self-Reflection](https://arxiv.org/abs/2611.01846)

**<font color=#1a73e8>作者：</font>** Zegang Cheng, Zhikai Wang, Jiacheng Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion transformers have become the most powerful models for visual generation, but still suffer from massive computation costs. To solve this problem, feature caching has been proposed to cache the features of diffusion models in the previous computation steps and then reuse them in the following caching steps, which brings significant acceleration but also degradation in generation quality. To address this problem, this paper proposes Z-cache as a feature caching method that can maintain high-quality generation through self-reflection. Concretely, we observe that the error from feature caching tends to be sharply reduced after each full computation. Based on this observation, Z-Cache is designed to first predict the features in the future caching steps and then perform a full computation. After that, Z-Cache returns to the caching steps and re-predicts them based on the previous and the current computation steps, which brings correction in features. Experiments demonstrate that with Z-Cache, diffusion transformers achieve comparable generation quality to the original model but with faster inference speed, for instance, 6.22X acceleration on FLUX-dev for text-to-image generation. Our code is released on GitHub.

---


### 322. [Biological Congruence: Evaluating Microscopy Generation Across Representations](https://arxiv.org/abs/2611.01850)

**<font color=#1a73e8>作者：</font>** Duway Nicolas Lesmes-Leon, Shumpei Takezaki, Fabian Schmeisser 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models increasingly produce realistic microscopy images, yet conventional evaluation primarily characterizes visual fidelity and distributional coverage rather than the biological information represented by synthetic data. We introduce biological congruence as an evaluation principle describing whether biologically relevant information forms a coherent description across representations and remains consistent with its empirical biological context. To study this principle, we develop a text-conditioned diffusion framework that jointly generates microscopy images and instance masks, exposing the same generated biological state through conditioning, visual appearance, and instance structure. Across prompt--mask, prompt--image, image--mask, and population-level analyses, we find strongly feature-dependent behavior: density and confluency are consistently preserved, morphology exhibits recurrent disagreement, while nearest-neighbor distance reveals that strong image--mask agreement can coexist with weaker conditioning and population fidelity. Stress testing increasingly unsupported phenotype combinations further shows that target controllability can increase while untargeted phenotypes reorganize and the complete generated state moves toward configurations better supported by real data. These findings demonstrate that generative quality, controllability, cross-representation agreement, and population fidelity capture complementary properties, motivating biological congruence as a relational perspective for evaluating scientific generative models.

---


### 323. [Missingness-Aware Prior-Data Fitted Network for Irregular Clinical Time-Series](https://arxiv.org/abs/2611.01851)

**<font color=#1a73e8>作者：</font>** Hadi Mehdizavareh, Gabriele Santangelo, Giovanna Nicora 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical time series are irregularly observed with laboratory measurements recorded at uneven intervals and observation patterns often reflecting patient state, clinical concern, and site-specific practice. Consequently, missingness is not merely a nuisance factor but an informative signal for prediction. We propose a Missingness-Aware Prior-Data Fitted Network (MA-PFN) for irregular clinical time-series prediction. MA-PFN first learns a diffusion-based prior over joint laboratory value and observation-mask trajectories from source-domain electronic health records, capturing both physiological dynamics and measurement processes. Synthetic trajectories sampled from this prior are then transformed into context-query tasks to train a PFN-style conditional predictor. Once trained, the model performs prediction for new admissions in a single forward pass, requiring neither retraining nor parameter adaptation on target datasets. The framework naturally supports both imputation and forecasting through different context-query constructions. We conduct internal validation on a held-out MIMIC-III test set and external validation on eICU, evaluating both imputation and forecasting and assessing cross-domain generalization under shifts in patient populations, clinical practices, and observation mechanisms. MA-PFN achieves the best performance across all evaluated settings, with Overall/Macro nRMSD ranging from (0.193/0.186) for internal imputation to (0.297/0.297) for external forecasting, without target-domain adaptation. These results demonstrate that learning missingness-aware task priors enables accurate and transferable clinical time-series prediction under informative missingness.

---


### 324. [Privacy-Preserving ECG-HRV Emotion Classification for Mood Swing Detection using Federated Learning on Constrained Edge Devices](https://arxiv.org/abs/2611.01853)

**<font color=#1a73e8>作者：</font>** Chidike Vincent, Muhammad Aslam Jarwar, Najam Ul Hasan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a privacy-preserving mood monitoring framework that classifies emotional states from ECG-derived heart rate variability (HRV) features. The framework is evaluated on three public datasets comprising 74 participants and further validated using a wearable device in a pilot study. Leave-One-Participant-Out cross-validation (LOPO-CV) is used to assess generalization to unseen individuals. A series of experiments investigates the impact of temporal windowing, HRV feature selection, and class balancing on both four-class valence-arousal and binary valence classification. Results show that class balancing substantially improves minority-class recall, while Logistic Regression consistently outperforms five alternative classifiers and achieves competitive performance against HRV-based baselines. Pilot validation using a Polar H10 wearable achieves 75% binary valence accuracy on an unseen individual without calibration, demonstrating the feasibility of real-world deployment. To preserve privacy, the framework is also implemented using federated learning on a six-node Raspberry Pi cluster. Federated Logistic Regression achieves performance comparable to centralized training without sharing raw physiological data. These results demonstrate the potential of interpretable and privacy-preserving mood monitoring for continuous mental health assessment in clinical and community settings.

---


### 325. [A Compute Center Anyone Can Join: A Peer-to-Peer System for AI Inference](https://arxiv.org/abs/2611.01865)

**<font color=#1a73e8>作者：</font>** Yimo Lin, Zhen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Today, most people obtain AI inference by buying it from a small number of organizations that run large data centers, while many GPUs owned by individuals and small institutions sit idle for much of the day. Bitcoin showed that strangers can contribute resources under shared rules and receive checkable rewards, but it relies on an asymmetry: proof-of-work is expensive to produce and cheap to verify. Useful inference has no such asymmetry. We propose the Open Inference Market (OIM), which replaces the missing asymmetry with an economic mechanism. A worker delivers a result without knowing whether it will be audited; its unsettled earnings serve as collateral during a challenge window; and confirmed cheating forfeits all of it. We call this principle earnings as collateral. In a simplified model we show three things. The number of audits needed for deterrence is a constant per worker per day, independent of the worker's throughput, so the audited share falls as the network gets busier. A new worker can join with a short period of intensive auditing and a very small bond. And whether the mechanism works at all depends only on the ratio of the audit judge's false-flag rate to its detection rate. Under example parameters, about 0.3 replays per worker per day are enough to make cheating unprofitable for a rational worker. On this basis we lay out a path that hands four powers back to participants one at a time: owning compute, writing history, judging work, and releasing value. A compute center need not be a building; it can be a protocol that anyone can join.

---


### 326. [The (Butter)fly Dream: Linear Separability of World-Model Rollouts in a Connectome-Constrained Visual Model](https://arxiv.org/abs/2611.01866)

**<font color=#1a73e8>作者：</font>** Junichiro Niimi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zhuangzi dreamt he was a butterfly and, on waking, could not tell which was the dream. We ask a version of his question of a model of the fly brain: placed inside a world generated by a world model, can a fixed brain tell that the world is a dream? We treat it as a question about what a connectome-constrained model trained on one task makes available beyond that task: do its responses make the defects of a dream linearly decodable? The observer is a published model of the fly visual system trained only for optic-flow estimation; reality is the MPI-Sintel movie on the model's 721-column retina; dreams are continuations of five real frames by three small world models (a persistence random walk, an MDN-RNN and an RSSM) at three temperatures. The judge is a classifier two-sample test on temporal statistics of cell-type responses, with sequence-level cross-validation. In the trained observer's responses all nine dreams are separable from reality (AUC 0.85-0.99, mean over 50 trained models), in those of the same network before training much less so (0.58-0.75 for the learned world models; paired difference 0.20-0.37), equally on sequences the observer never saw, and in an order unrelated to pixel error. Because these AUCs are near ceiling, we add graded probes made of each window's own real frames with only their order broken. Swapping one adjacent pair of the 14 generated frames gives 0.73 on the trained responses against 0.54 before training and 0.56 for pixel statistics; the trained curve reaches 0.75 at 1.1 swapped pairs of seven, the pixel statistics at 4.7, and the untrained network not at all. A detection horizon, the test on the first k generated frames, orders the world models where the full-length AUC saturates.

---


### 327. [Fairness-Aware Design for Contextual Experiments: Guaranteeing Reliability and Equity in Heterogeneous Subgroups](https://arxiv.org/abs/2611.01867)

**<font color=#1a73e8>作者：</font>** Guangyan Gan, Ling Zhang, Yanhua Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Experimental design is critical for evidence-based decision-making in healthcare, marketing, and public policy. However, designing efficient experiments across heterogeneous subgroups presents significant challenges. Existing methods often optimize for statistical power or overall sample efficiency, overlooking crucial fairness considerations across these different subgroups. To address this gap, we introduce a Fairness-Aware Contextual Track-and-Stop Design (F-CTSD) algorithm. The proposed F-CTSD algorithm provides statistical guarantees on subgroup fairness while minimizing required sample sizes. We quantify the fairness-efficiency trade-off and derive the exact sample complexity for the proposed F-CTSD algorithm under its fairness constraints. We further theoretically prove that the proposed F-CTSD algorithm consistently produces accurate treatment effect estimates even under fairness requirements, enhancing statistical reliability. Numerical experiments show that the proposed F-CTSD algorithm outperforms existing methods, achieving higher sample efficiency while reducing subgroup fairness violations by 4.95%.

---


### 328. [A Self-Generated Floor on Adam's $\varepsilon$: Evidence from Power-Law Matrix Sensing](https://arxiv.org/abs/2611.01868)

**<font color=#1a73e8>作者：</font>** Lngel Kyo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In nonconvex Burer--Monteiro low-rank matrix sensing of $U^\ast \in \mathbb{R}^{V \times D}$ under power-law covariance $\Sigma = \mathrm{diag}(j^{-s})_{j=1}^V$, the precision-wall approximation predicts that Adam stalls when the smallest non-gauge Hessian eigenvalue drops below its denominator floor, giving $s^\ast(V,D) = [\log(1/\varepsilon_{\mathrm{eff}}) - \log V]/\log(VD) + \delta_{\mathrm{Adam}}$. If $\varepsilon_{\mathrm{eff}}$ were set by $\varepsilon_0$, lowering $\varepsilon_0$ from $10^{-10}$ to $10^{-12}$ would raise $s^\ast$ by $0.95\text{--}1.33$. Instead, across six values of $\varepsilon_0$ two decades apart, $10^{-2}$ to $10^{-12}$, the boundary follows the $\varepsilon_0$ slope down to $10^{-6}$, bends near $10^{-8}$, and is flat below $10^{-8}$, while warm-started L-BFGS and Gauss--Newton reach machine precision on stalled instances. We trace this saturation to a self-generated dynamical floor $\varepsilon_{\mathrm{dyn}} \propto \alpha$: high-curvature modes oscillate persistently near the adaptive edge of stability with amplitude $\propto \alpha(1-\beta_1)/(1+\beta_1)$ and leak gradient fluctuations of scale $\kappa\alpha$ into rare modes via measurement coupling, pinning $\sqrt{\hat{v}_V} \approx \kappa\alpha \gg \varepsilon_0$. Fitting a single threshold-crossing wall parameter $\varepsilon_{\mathrm{dyn}} = 4.76\times 10^{-9}$ (with the detection lag frozen at its companion calibration) predicts the saturated failure boundary for $D \ge 4$ across five $(V,D)$ scales to RMS $0.098$ (breaking down at $D = 2$), while shrinking $\varepsilon_0$ below $10^{-8}$ is ineffective and lowering the step size $\alpha$ reduces the floor directly.

---


### 329. [Automated Stateful Specialization for Adaptive Agent Systems](https://arxiv.org/abs/2611.01870)

**<font color=#1a73e8>作者：</font>** Myan Vu, Harrish Ayyanar, Jiang Pang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Current automated agent design frameworks produce either static workflows that lack adaptability or per-query optimizers that prevent the accumulation of deep, agent-level task expertise. We propose a new direction that reconciles these paradigms: creating stateful teams of specialist agents that accumulate knowledge over time and can be reconfigured for novel tasks entirely without human intervention. To this end, we introduce ASpec, a framework that manages this full agent lifecycle by first autonomously discovering specialist archetypes via evolutionary search and then cultivating their expertise through experience, mirroring how human experts learn through practice and reflection. We further introduce a lightweight hierarchical control policy, "retain-then-escalate," which governs when to leverage the established agent system versus when to adapt its structure. Through comprehensive experiments, we demonstrate that this approach leads to significant performance gains on expert-level scientific benchmarks like GPQA while matching the state-of-the-art on broader domain tasks, demonstrating a promising path toward agent systems that are simultaneously expert, adaptive, and efficient. We will release the code at this https URL.

---


### 330. [Prior-Guided Physics-Informed Deep Learning for Fast 4D MRI Reconstruction](https://arxiv.org/abs/2611.01888)

**<font color=#1a73e8>作者：</font>** Mojtaba Safari, Parag J. Parikh, Shansong Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background and purpose: We propose PGPI4MR (prior-guided, physics-informed 4D MRI reconstruction), a deep learning method that leverages information from other respiratory phases or a setup scan, the first 30 s of the same scan, to improve 4D MRI reconstruction without extra scan time. Materials and methods: PGPI4MR is an unrolled network that reconstructs 16 respiratory phases from 60, 30, or 15 s of data, and single 3D volumes, each from 0.29-0.49 s of data, using a setup-scan image. The networks were trained once, on other volunteers, and were not retrained for new volunteers. We evaluated PGPI4MR on measured k-space from three datasets: free-breathing MR-linac (1.5T) and abdominal (3T) scans, and thigh scans with cuff compression (1.5T). All methods, including comparative models, received identical samples and were scored similarly. Results: In vivo, PGPI4MR had the lowest held-out error for 4D MRI at every scan time, and its 16 phases were ready a median of 7.5-13 s after the scan on the 2 GPUs tested. Coupling the 16 respiratory phases reduced the error at 60 s by 9.1% compared with reconstructing each phase alone. For sub-second MRI, the error at 0.49 s was 15.5% lower than that of the best comparison method, classical reconstruction toward the same prior, and on the faster GPU, every 0.29 s window was acquired and reconstructed within 0.5 s. Without retraining, PGPI4MR matched the best methods on the 3T abdominal scans but not on the thigh scans; after retraining on thigh data, it reduced the held-out error by 6.6% relative to the best comparison method. Conclusion: Prior information allowed PGPI4MR to reconstruct 4D and sub-second MRI more accurately than compressed sensing and a published 4D network, within seconds and without extra scan time. This could support 4D MRI for treatment planning and 3D motion monitoring during MR-guided radiotherapy.

---


### 331. [Robust Remote ECG Monitoring under Energy Constraints: Anomaly Filtering versus Predictive Uncertainty](https://arxiv.org/abs/2611.01898)

**<font color=#1a73e8>作者：</font>** Mustafa Fuad Rifet Ibrahim, Maurice Meijer, Alexander Schlaefer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning for remote electrocardiogram monitoring must handle noise and diseases absent from training under tight resource constraints. We investigate whether upstream unsupervised anomaly detection can improve monitoring decisions more efficiently than classifier-derived uncertainty. We evaluate five detectors on PTB-XL and BUT QDB and compare a two-stage filter-classifier system with Monte Carlo Dropout and deep ensembles under unseen-disease and noise conditions. Performance is averaged over five training seeds. We measure single-pass energy, latency, and graph memory on a microcontroller's central processing unit (CPU) and neural processing unit (NPU). Per-score neural network costs account for repeated evaluations but exclude scoring outside deployed graphs. Energy equations relate filtering and rejection to avoided classifier execution. Across four disease scenarios, Deep Support Vector Data Description (Deep SVDD) achieves the highest mean area under the receiver operating characteristic curve within all tested finite CPU energy budgets. On the NPU, it leads at 1 mJ, while Monte Carlo Dropout has slightly higher means at 10 and 100 mJ. With a narrow CPU classifier, the Deep SVDD two-stage system increases the fraction of correctly classified or correctly rejected inputs by 15.0-19.4 percentage points over classification without rejection. Estimated energy per input is 1.93-6.99 mJ, compared with 52.53 mJ for Monte Carlo Dropout and 8.76-17.51 mJ for deep ensembles, at each method's retrospectively selected test accuracy peak. These results support upstream filtering for efficient remote monitoring, while independent validation and complete-system measurements remain necessary.

---


### 332. [Systematic Evaluation of Robustness in Fine-tuned Models](https://arxiv.org/abs/2611.01900)

**<font color=#1a73e8>作者：</font>** Angela John, Hamayoon Behmanush  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Our study systematically evaluates the robustness of fine-tuned pre-trained models across different datasets and attack types, aiming to provide insights for researchers in selecting pre-trained models for image classification tasks while prioritizing robustness against potential attacks. Our work explores the influence of fine-tuning pre-trained models with different datasets and attack types on their robustness and overview of the appropriate pre-trained model for image classification based on factors such as computation resources, memory usage, and accuracy on clean data. We fine-tune the models with weights. Evaluate the models on data before any attack and after different attack cases. The study utilizes publicly available image datasets such as MNIST, CIFAR10, CIFAR100, and SVHN to assess the robustness of pre-trained models. The results indicate that the robustness of fine-tuned models varies across different data distributions and sample sizes, emphasizing the need for tailored selection based on specific task requirements. The findings also highlight the varying performance of ResNet50, DenseNet, and MobileNet in defending against attacks on different datasets. Overall, this research provides valuable insights into the robustness of fine-tuned pre-trained models and their suitability for real-world applications in image classification.

---


### 333. [Training-Free Motion-Corrected 3D Brain MRI Reconstruction via Event-Guided References](https://arxiv.org/abs/2611.01902)

**<font color=#1a73e8>作者：</font>** Wei Jiang, Hongli Chen, Tianyi Ding 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Head motion causes artefacts in 3D brain MRI and can bias structural measurements. Model-based correction alternates between image and motion estimation, but artefacts in the reconstructed reference can reinforce motion errors. Learned priors can reduce these artefacts but require pretraining and may add test-time computation. We propose EventMC (event-guided motion correction), a training-free method for interleaved Cartesian acquisitions. It iteratively detects motion events and estimates motion using reference images reconstructed from stable intervals. It then refines the image and motion from low to high spatial frequencies. In a fair comparison in simulation (same reconstruction), EventMC's motion estimates improve mean PSNR by up to 4.0 dB over those of the learning-based MotionTTT. A single run of EventMC is up to 7.5 times faster than MotionTTT with less than half the GPU memory. On in vivo motion-corrupted scans, EventMC achieves similar mean image quality to MotionTTT without any training. Code is available at this https URL.

---


### 334. [Online Active Learning Architecture for Safety-Critical Control Systems](https://arxiv.org/abs/2611.01907)

**<font color=#1a73e8>作者：</font>** Shuiwen Shen, Jinhua Zhang, Yan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The transition of information-centric artificial intelligence to safety-critical applications is impeded by the limitations of conventional offline-training paradigms in open-world environments. This paper presents Control AI, an architecture for Online Active Learning (OAL) inspired by the continuous Prediction-Evaluation-Correction process of biological intelligence. The framework combines the hierarchical representation capacity of deep neural networks with the real-time error-feedback adaptation of adaptive control. A prediction model maps sensory input into a latent manifold, an optional latent model represents transitions in that space, and a reconstruction model maps the latent state back to observable signals. Residuals between predictions and measurements provide the internal learning signal. Spatial and temporal cross-reconstruction architectures prevent OAL from collapsing to a trivial identity mapping, while coupled, dual, and localized variants shorten error-transmission paths. Localized predictive coding style OAL is implemented through guidance-backpropagation and target-backpropagation architectures, and hybrid and scaled variants support high-dimensional deployment. The paper focuses on the architectural rationale and the progression from a conceptual feedback loop to practical large-scale configurations.

---


### 335. [Machine Learning Beyond Statistical Consistency for Hybrid AI](https://arxiv.org/abs/2611.01914)

**<font color=#1a73e8>作者：</font>** Jinsook Kim, Jinho Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a new definition of machine learning, according to which a machine learns a function when it computes the function successfully, that is, when the value it returns for each input has a proper derivation in a formal system. We extend Gödel's Representability Theorem, which equates computation with derivation, to empirical targets in two ways: the theorem is extended to the computable reals, and the data are admitted into the system as empirical definitions that record what has been observed. We prove that a machine learns a true probability if and only if two conditions are met. The Truth Condition is that its estimate converges to the true probability, which is statistical consistency. The Assurance Condition is that the machine properly derives its own convergence inside the system. Learning thus lies beyond statistical consistency, for it requires a derivation of the convergence from the record. A global assumption about the data, such as the i.i.d. assumption, does not supply such a derivation, because it leads only to a circular one, as we show for PAC learning. On the other hand, the two conditions are met for the probability of a sentence over a finite ideal corpus. A real machine can approximate a true probability only if an ideal machine can learn it precisely, that is, only in a domain that meets the two conditions. Modern AI works in such a domain, and we offer this as a clue to its success. Modern AI is hybrid as well, in two senses: First, it performs two kinds of tasks, namely probabilistic ones such as predicting the next word and deductive ones such as proving and coding. Second, it combines two parts of different kinds, a statistical proposer and a deductive verifier, for proving and coding. Our framework explains both senses of hybridity in one formal system.

---


### 336. [Watch Your Step: Adam's Margin Maximization Bias Depends on the Learning Rate Schedule](https://arxiv.org/abs/2611.01929)

**<font color=#1a73e8>作者：</font>** Eitan Gronich, Gal Vardi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the implicit bias of Adam and its similarity to sign gradient descent on homogeneous models in binary classification tasks. Perhaps surprisingly, we uncover that these depend on the learning rate schedule. While previous works studied strongly decaying learning rate schedules $\eta(t)=\mathrm o \left(t^{1/L-1}\right)$, where $L$ is the homogeneity degree, and showed $\ell_\infty$-margin-maximization biases, we focus on the more common complementary regime, including constant and weakly decaying schedules. For a polynomial schedule $t^{\alpha}$ and homogeneity degree $L$, we show that when $\alpha > \frac 1L - \frac12$, Adam has no trajectory-independent margin-maximization bias for deep linear networks (in the KKT sense): first, there is no non-trivial, locally Lipschitz, convex implicit regularizer in this setting, including any squared norm. Second, on width-$1$ networks, the result holds without requiring convexity, implying that any implicit regularizer for wide networks must be trivial when restricted to a width-$1$ network. Nevertheless, we positively characterize the implicit bias in this regime as maximizing a trajectory-dependent weighted-$\ell_2$ margin for any $L$-homogeneous model. The fundamental mechanism behind our results is convergence of Adam's preconditioner to a trajectory-dependent vector, which also allows showing that the limiting parameter direction depends on initialization. In the intermediate regime $\frac 1L - 1 \leq \alpha \leq \frac1L - \frac12$ we prove an $\ell_\infty$ bias, conditional on gradient directional convergence to a full-support vector. Of independent interest, we establish a loss decay rate for full batch Adam on general homogeneous models, whose leading order depends only on the second-moment parameter.

---


### 337. [Spade-SLAM: Sparse Correspondence Anchors for Dense Self-Supervised Visual SLAM](https://arxiv.org/abs/2611.01937)

**<font color=#1a73e8>作者：</font>** Julian Philipp Schmitt, Weirong Chen, Ganlin Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Spade-SLAM, a self-supervised dense visual SLAM framework that substantially narrows the long-standing performance gap to supervised methods in a zero-shot setting. By demonstrating that high-fidelity tracking can be achieved without explicit ground-truth pose and depth labels, our approach offers a highly effective and label-efficient alternative to fully supervised pretraining. Our core contribution is a complementary sparse-to-dense training regime: While a warping-based photometric loss provides a dense training signal, we stabilize the optimization and suppress drift in ambiguous regions using a sparse correspondence loss derived from image feature matches. Extensive experiments demonstrate that Spade-SLAM significantly improves robustness and accuracy compared to existing self-supervised baselines, closely rivaling SLAM systems trained with explicit pose and depth supervision. The code will be made publicly available at this https URL.

---


### 338. [Hippocampal consolidation without replay in fully fine-tuned networks](https://arxiv.org/abs/2611.01952)

**<font color=#1a73e8>作者：</font>** Keuntae Kim, Yong Suk Choi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Networks that keep learning overwrite what they know. Prevailing remedies replay stored data, distil from old models or freeze the backbone. The brain suggests a different division of labour: the hippocampus indexes where experience lies in cortex while the cortex keeps learning. We show that this division lets a fully trainable network keep learning without cross-task replay, a teacher or inference-time memory. After each task, a training-only hippocampal memory indexes the input geometry of every group of synapses sharing an input, residual energy included, and limits each synapse's movement per direction before and after the optimizer. This class-free geometry carries most of the protection; with conflict detection on top, the method cuts absorption of established classes by near-duplicates several-fold against every compared method. To our knowledge, this is the first demonstration of one principle keeping whole networks learning across four architecture families and models up to 8 billion parameters. Methods that freeze the backbone hold up only as far as its representation already separates the classes; here the whole network keeps learning to tell near-duplicates apart, leading the frozen-backbone baseline by 17.5 points on TACRED. Without the memory, much old knowledge stays decodable but beyond the network's reach.

---


### 339. [Event-Based Optical Flow Constraint via Time-Sliced Plane Fitting](https://arxiv.org/abs/2611.01960)

**<font color=#1a73e8>作者：</font>** Masaki Koike, Yusuke Kameda, Shunichi Sato 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event-based optical flow estimation using spatiotemporal planar approximation inherently assumes constant velocity and tends to average out temporal velocity variations. In this paper, we propose a flow estimation method that extends this planar approximation along the temporal axis. The resulting event-based optical flow constraint allows existing variational optical flow formulations to model temporal motion variation. Specifically, we partition the space-time volume into sub-intervals and apply a two-step planar approximation to track object edges consistently. Moreover, a spatial compensation mechanism and a temporal regularization term are incorporated to compensate for edge displacements and temporally stabilize the flow estimation, respectively. The experimental results show that modeling temporal motion variation improves flow estimation accuracy over conventional methods.

---


### 340. [Object-Only Is Not Context-Free: A Counterfactual Diagnostic for Context Removal in Object Retrieval](https://arxiv.org/abs/2611.01962)

**<font color=#1a73e8>作者：</font>** Boaz Meivar, Shai Avidan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object-centric retrieval pipelines often mask the background before pooling backbone features, aiming for a descriptor that reflects the object rather than its scene. Whether this truly yields an object-only descriptor, however, is rarely tested. We introduce the Keyhole Aperture Probe (KAP), a counterfactual diagnostic that repurposes the ground-truth masks of existing panoptic segmentation datasets (COCO, ADE20K) for retrieval: it holds the pooled object region fixed and varies only the pixels outside it, summarizing a backbone's context dependence in a single number. We find that the pooled object region has already integrated its surround. Replacing the context, with a neutral fill or even a different real scene, changes the descriptor, and when retrieval fails under a blank fill, the descriptor matches plain-background images rather than its own object. Object-only is not context-free. Across ten modern backbones, object-only descriptors retain only about a quarter to two-thirds of their full-image accuracy, and the effect is not unique to Transformer self-attention: a convolutional backbone shows it too. The dependence is also reducible: a lightweight adapter that encourages the descriptor to stay stable as context is removed lowers it and improves full-image instance retrieval on INSTRE, transferring to ILIAS with accuracy improved or preserved. A matched contrastive-fine-tuning control does not reproduce those gains. We release KAP as a simple, backbone-agnostic evaluation protocol to measure and reduce this dependence before deployment.

---


### 341. [Supporting Orthographic Recall of Chinese Characters through Self-Generated Compositional Mnemonic Stories: A Mixed-Methods Pilot Study](https://arxiv.org/abs/2611.01973)

**<font color=#1a73e8>作者：</font>** Aaron Friedrich Kurz  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mnemonic studies on Chinese characters have mostly tested provided mnemonics against writing outcomes and self-generated mnemonics against meaning recall; whether writing one's own component-based story helps learners write the character has received little attention. I present Nuome, a tool that shows a character's component decomposition next to an editor in which learners write their own story, with live checks on whether the story covers every component and the character's meaning. In a within-subjects pilot, eight L2 learners each learned four self-chosen characters with the story builder and four with a read-only panel showing the same decomposition, with identical writing practice. Descriptively, partial-credit written-recall scores favoured the story builder by 18.8 percentage points immediately (N = 8) and 17.9 points after two days (N = 7); mean study time per character was 1.69 times as long (n = 6); usability was high (SUS 88.1). Interviews yielded three themes: participants felt that composing a story made them attend to components; knowing the components is not the same as being able to write them; and characters differ in how well they suit a story.

---


### 342. [MUPA${}^2$S: Multimodal Unified Perception with Asymmetric Attention for Stress Assessment](https://arxiv.org/abs/2611.01974)

**<font color=#1a73e8>作者：</font>** Stefanos Gkikas, Thomas Kassiotis, Yu Fang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stress is a leading contributor to long-term physical and mental health decline. The automatic assessment of stress is a promising approach for continuous monitoring and mitigating human biases. However, the development of automated systems remains challenging due to the heterogeneity of physiological and behavioral signals. This paper presents MUPA${}^2$S, a multimodal framework for automatic stress assessment that combines facial video and ECG signals within a unified perception architecture. Both modalities are mapped into a shared token representation without modality-specific components, and processed through asymmetric attention comprising segment-local cross-attention and global self-attention across segment states. Experiments on a newly collected 58-subject stress dataset, evaluated under a stratified subject-level protocol, show that facial video achieves 69.44% test accuracy, while ECG-only performance remains close to chance under the proposed representation. Unified Video-ECG fusion achieves a test accuracy of 69.58% at approximately half the number of parameters of feature-level fusion, with negligible additional computational cost. Feature-level fusion does not exceed the video-only baseline, while unified input-level integration provides a parameter-efficient mechanism for jointly processing the two modalities.

---


### 343. [Multimodal BVP and Respiration for Automated Pain Recognition with Hankel-FCN](https://arxiv.org/abs/2611.01978)

**<font color=#1a73e8>作者：</font>** Valentina Becchetti, Muhammad Umar Khan, Stefanos Gkikas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated pain recognition is a fundamental challenge for the advancement of clinical care and empathetic human-computer interaction, due to the subjective and dynamic nature of pain. In this study, we propose a deep learning framework for objective pain assessment based on multimodal physiological signals from the AI4Pain dataset. The approach focuses on Blood Volume Pulse (BVP) and Respiration (RESP), capturing complementary aspects of autonomic responses to nociceptive stimulation. To explicitly model their temporal dynamics, the signals are transformed into structured trajectory representations using Hankel matrix embeddings, enabling the learning of dynamical patterns beyond conventional time-series representations. These embeddings are processed by modality-specific Fully Convolutional Networks, and their outputs are integrated through a late fusion strategy for three-class classification (No Pain, Low Pain, High Pain). Experimental results demonstrate that the proposed method achieves an accuracy of 67.09% and an F1-score of 66.41%, providing competitive performance compared to existing approaches, while relying on no handcrafted feature engineering. Multimodal fusion significantly outperformed either modality alone, and the Hankel embedding showed a trend towards further improvement. Further validation is required to establish generalisability to broader populations and clinical settings.

---


### 344. [Opening the Black Box of Neural Auction Mechanisms](https://arxiv.org/abs/2611.01981)

**<font color=#1a73e8>作者：</font>** Li Kong, Zilong Liu, Haoyang Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural auction design has emerged as a powerful paradigm within automated mechanism design for modern Web platforms. Because these learned mechanisms directly dictate critical economic outcomes, their lack of internal transparency raises significant auditability and trust concerns. Opening this black box \textit{post-hoc} is therefore essential, yet presents two distinctive challenges: (1) activation contexts are dense, correlated numerical profiles devoid of explicit semantic structure, and (2) feature interpretations can only be falsifiably audited if they map to measurable auction states or outcomes. In this paper, we propose a post-hoc white-box auditing framework for unpacking trained neural auctions. Using CITransNet as a representative testbed, we first employ sparse autoencoders to decompose hidden representations while faithfully preserving downstream auction behavior. Anchoring feature interpretations to native economic targets, we validate them through activation prediction and causal interventions to isolate verified features from the reconstruction dictionary. Finally, applying this pipeline across varied auction settings, we show that the verified features can serve as analytical instruments to examine how internal representations modulate strategic misreporting incentives, align with Myerson's optimal auction, and support the diagnosis of individual auctions. Our work highlights the potential of white-box mechanism auditing to build the foundational trust necessary for neural auctions to be deployed as widely adopted Web technologies. To enhance research transparency and facilitate independent inspection, we publicly release the experimental results supporting our findings at this https URL

---


### 345. [SurgStream: A Workflow-Anchored Proactive Streaming Framework and Benchmark for Real-Time Surgical Video Understanding](https://arxiv.org/abs/2611.01982)

**<font color=#1a73e8>作者：</font>** Ruipeng Ma, Qing Xu, Jie Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical video understanding is essential for intraoperative assistance such as workflow monitoring, instrument preparation and procedural documentation. Delivering such assistance in real time requires a model to jointly perceive the ongoing scene, remember past surgical events, and respond before clinically relevant moments pass. Existing approaches provide limited support for jointly retaining procedural evidence and deciding when to respond in streaming surgical video. In this work, we propose SurgStream, a workflow-anchored proactive streaming framework for real-time surgical video understanding. We first introduce Workflow-Anchored Memory (WAM) to record structured instrument-action-target observations and fold them into phase-level summaries, providing compact and queryable surgical memory. Deadline-aware Transition Learning (DTL) is then devised to supervise response states within clinical windows, enabling timely responses before procedural deadlines. We further introduce SurgStream-Bench, comprising 11.7K streaming interactions across various tasks covering real-time perception, backward memory queries, forward proactive QA, proactive alerts and caption memory. Experiments on SurgStream-Bench show gains over state-of-the-art methods, especially in memory and forward proactive QA. The source code will be available.

---


### 346. [Large-Scale Bayesian Optimisation Using Uncertainty-Calibrated Product-of-Experts Gaussian Process Models with Trust Regions](https://arxiv.org/abs/2611.01984)

**<font color=#1a73e8>作者：</font>** Yean Hoon Ong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The use of collections of independent local Gaussian processes (GP-ind) combined with trust regions is a widely adopted approach for large-scale and high-dimensional Bayesian optimisation (BO). However, this approach suffers from several limitations, including discontinuities at the boundaries of disjoint regions, an inability to capture long-range spatial correlations, potential information loss, and abrupt increases in computational overhead. To address these limitations, this paper introduces a novel BO algorithm, termed BO-pro-c-tr. The proposed method employs a product-of-experts Gaussian process model with uncertainty calibration (GP-pro-c) as its surrogate model and incorporates a one-to-many association strategy for integrating GP-pro-c with trust regions. Empirical results suggest that, when combined with the GP-LCB acquisition function, BO-pro-c-tr achieves an average reduction of 2.6% in simple regret and 34.9% in computational overhead relative to BO algorithms based on independent local GP models coupled with trust regions.

---


### 347. [Accelerating QUIC Encryption in WebAssembly Using WASM-SIMD](https://arxiv.org/abs/2611.01989)

**<font color=#1a73e8>作者：</font>** Sota Yamawaki, Yasuo Okabe  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> WebAssembly (Wasm) runs untrusted code in a portable, lightweight sandbox and is increasingly used to host services on shared servers and edge platforms. Running the QUIC transport protocol inside Wasm would let each application choose and update its own transport without changing the host. QUIC, however, encrypts every packet, and Wasm offers neither dedicated AES instructions nor carry-less multiplication; a Wasm QUIC stack has been reported to reach only 17.6% of native goodput, with cryptography as its largest cost. Whether the 128-bit SIMD extension of Wasm (WASM-SIMD) can recover this cost, and what limits a pure-Wasm stack once it does, has remained unclear. Here we show that explicit WASM-SIMD kernels recover much of the cryptographic cost, after which non-cryptographic costs become the limit. On two hosts connected by 10-Gigabit Ethernet, kernels that process eight AES blocks or four ChaCha20 blocks per pass raise receiver goodput over a non-SIMD baseline by 61.34% for AES-128-GCM and 31.55% for ChaCha20-Poly1305, whereas compiler auto-vectorization gains only 1.28% for AES-128-GCM. ChaCha20-Poly1305 still delivers 1.99 times the goodput of AES-128-GCM, confirming end to end the preference that stand-alone cipher benchmarks suggest. Receiver-side profiling combined with Amdahl's law predicts that even native-speed cryptography would leave Wasm at roughly one third of the goodput of the fastest native stack. Cryptographic acceleration is therefore necessary but not sufficient: memory allocation, runtime overhead and per-datagram UDP I/O now bound pure-Wasm transports. We anticipate that this per-category cost breakdown will guide further optimization of Wasm network stacks and the design of system interfaces for batched I/O.

---


### 348. [MIRA: Mutual Information guided calibration for Reliable Test-Time Adaptation](https://arxiv.org/abs/2611.02003)

**<font color=#1a73e8>作者：</font>** Hyeongyu Kim, Mingyeong Jang, Youngjun Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) updates a deployed model using only unlabeled target data, but standard entropy-based methods often rely on deterministic confidence and can reinforce overconfident errors under distribution shift. We propose MIRA, Mutual Information guided calibration for Reliable Test-Time Adaptation, a source-free online adaptation method that uses lightweight last-layer Gaussian perturbations to probe prediction reliability. For each target batch, MIRA reuses a single feature extraction pass and samples perturbed classifiers around the source classifier, forming an efficient local predictive distribution. Rather than fitting a Bayesian posterior, MIRA treats the perturbation scale as a local probing radius and selects a batch-specific scale using mutual information (MI) and prediction agreement. The resulting perturbation-sensitivity signal identifies predictions that are confident and locally stable under classifier perturbations, while suppressing brittle predictions with high stochastic disagreement. MIRA then performs adaptation with an MI-confidence weighted entropy loss, which down-weights perturbation-sensitive or low-confidence samples before they drive entropy minimization. This weighted loss reduces the influence of brittle predictions that can otherwise cause harmful adaptation under distribution shift. The method requires no source data, retraining, model ensembles, or offline posterior fitting, and can be applied as a plug-and-play modification to entropy-minimization TTA. Experiments on distribution-shift benchmarks show improvements in accuracy, calibration, and negative log-likelihood, suggesting that mutual-information-guided perturbation probing and weighted adaptation yield more robust online TTA than deterministic confidence.

---


### 349. [One String to Rule Them All: Measuring Consent Under the IAB Global Privacy Platform](https://arxiv.org/abs/2611.02014)

**<font color=#1a73e8>作者：</font>** Muhammad Abu Bakar Aziz, Christo Wilson  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Many privacy regulations, including the California Consumer Privacy Act (CCPA), require websites to honor users' opt-out choices. To facilitate this process, industry has introduced technical standards such as the IAB Global Privacy Platform (GPP), which aims to standardize collection and transmission of user consent information across multiple jurisdictions. However, it remains unclear whether these standards consistently and correctly transmit user opt-out choices, or whether opt-out choices are respected by advertisers.
In this study, we conduct an in-depth analysis of consent propagation under the GPP framework. We collect data from four web crawls across four experimental settings to analyze how widely the standard is adopted, the extent to which opt-out signals propagate from publishers to third parties, and whether these signals reach and alter third-party advertiser behavior. Our analysis reveals several inconsistencies in the implementation and adoption of the standard that result in user consent signals being lost and user opt-out choices not being respected by the advertisers.

---


### 350. [CULTURE-CMT: Benchmarking Contextualized Social Media Translation](https://arxiv.org/abs/2611.02018)

**<font color=#1a73e8>作者：</font>** Linjuan Wu, Dingming Li, Yiwen Qiu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social-media comments are interactions, yet they are often translated and evaluated as isolated text. This mismatch is especially problematic when meaning depends on surrounding discussion, community-specific slang, or culturally situated expressions. We introduce CULTURE-CMT, a Chinese-English benchmark for contextualized social-media comment translation that restores the post and conversational context naturally available to users. Its 572 manually verified examples are organized into Slang, Context, and Both, enabling diagnostic analysis of distinct and interacting sources of translation difficulty. To support scalable evaluation, we further develop a retrieval-augmented cultural-effectiveness Judger that combines a calibrated scoring model with dynamically retrieved cultural knowledge. CULTURE-CMT reveals several non-trivial patterns. Providing interaction context improves most model configurations, but does not eliminate culturally ineffective translations. Examples requiring both contextual grounding and culturally situated language remain substantially more difficult than either source of difficulty alone. Moreover, larger models are not consistently better, and thinking produces highly model-dependent gains, including occasional degradation. In contrast, a 27B model adapted on benchmark-disjoint social-media data achieves the lowest observed invalidity rate among the evaluated configurations under thinking inference with context. Together, these results suggest that realistic social-media translation is not simply a matter of scaling models or reasoning longer, but of learning to translate meaning as it is constructed within evolving online interactions.

---


> [!TIP]
> 当前位于：**301-350**（第 7/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
