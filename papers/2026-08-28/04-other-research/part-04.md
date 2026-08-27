# 📦 其他研究 | 2026年08月28日

> 本类共 **171** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-171**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-171**

---

### 151. [Choose Your Game Wisely: Measuring Game-Theoretic Structures in Real-World Vehicle Interactions](https://arxiv.org/abs/2608.25917)

**<font color=#1a73e8>作者：</font>** Yueyuan Li, Rongcheng Nie, Weijie Xi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Game-theoretic models provide principled frameworks for modeling vehicle interactions, but their underlying temporal assumptions have not been systematically examined against real-world driving behavior. In particular, it remains unclear how simultaneous, sequential, and asymmetric interaction structures can be measured from vehicle trajectories. This paper develops a trajectory-based interaction measurement framework to identify interaction events and quantify behavioral change onset, temporal organization, post-onset response dynamics, and ordering stability. The framework uses behavioral deviations to verify candidate interactions. We evaluate the framework on six real-world trajectory datasets, including INTERACTION, highD, inD, rounD, Waymo Open Motion, and nuPlan, covering diverse road geometries, traffic environments, and interaction types. The results show that concurrent and sequential behavioral changes both constitute substantial proportions of observed following, merging, and conflicting interactions. Among sequential interactions, stable ordering is more prevalent than alternating ordering, indicating that persistent asymmetric roles are a common interaction structure. Importantly, temporal precedence does not necessarily coincide with a measurable behavioral response, indicating that temporal ordering alone may not be sufficient to characterize behavioral dependence. These findings show that real-world interactions exhibit concurrent, sequential, and persistently ordered temporal structures. Different game-theoretic formulations are therefore better regarded as complementary modeling abstractions for different interaction regimes rather than as a universal structure governing all vehicle interactions.

---


### 152. [Formal, Executable and Explainable Runtime Monitoring of Spoken Air Traffic Control Operational Procedures](https://arxiv.org/abs/2608.25926)

**<font color=#1a73e8>作者：</font>** Roberto Luvini, Giacomo Longo, Alessandro Armando 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Air traffic control procedures are executed through spoken exchanges between controllers and pilots. These interactions are essential to the safety of air transportation: failures in their execution can create severe operational hazards, as evidenced by past fatal accidents. Assessing whether an instruction has been followed requires relating what was said to the aircraft concerned, its state, and the obligations that pilots must meet. We present a runtime verification framework that monitors such procedures by checking controller-pilot exchanges, surveillance data, and onboard observations. The framework parses radio communications into events linked to the entities they concern and merges them with surveillance and onboard observations into a time-stamped trace. The ICAO-derived obligations as formalized as temporal formulas with explicit time bounds and evaluated over execution traces. Every violation is reported along with the breached obligations and the observations that support the verdict. With real traffic, the complete pipeline reaches an F1 of 0.85 against blind human-annotated violations; in 1,495 synthetic situations derived from two public corpora, the monitor logic returns the expected verdict in every case. In two historical accidents reconstructed from official investigation reports, the monitor identifies the same procedural deviations documented by the investigators.

---


### 153. [AI Agentic Selective Laser Sintering Process Optimization](https://arxiv.org/abs/2608.25928)

**<font color=#1a73e8>作者：</font>** Peter Pak, Victor Alvarado, Amir Barati Farimani  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agentic systems enable the intelligent automation of complex workflows, specific to additive manufacturing this is applicable for complex tasks such as process parameter optimization for mechanical properties. This work investigates the AI enabled agentic process optimization within Selective Laser Sintering (SLS) to iteratively improve the tensile and flexural properties of 3 different materials on the Inova Mk1. These materials include PA12 GF, PA11 Onyx, and PA12 Blend (volume mixture of 25% PA12 GF and 75% PA12 White) and with using knowledge from previous builds and minimal guidance from the user, the agentic system was able to optimize process parameters over a small number of iterations to achieve comparable TDS specified mechanical properties. This work showcases the ability for an agentic system to continually learn from updated data, enabling the intelligent automation of complex tasks such as process parameter optimization for selective laser sintering.

---


### 154. [Gaming Together on Discord: Teen Gamer's Cross-Platform Practices](https://arxiv.org/abs/2608.25942)

**<font color=#1a73e8>作者：</font>** Elena Koung, Xinning Gui, Yubo Kou  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Discord is one of the most popular communication platforms among gamers. While prior research has highlighted its role in community building, relatively little attention has been paid to its original gaming context-how it shapes gameplay and social experiences. To address this gap, we conducted semi-structured interviews with 16 teenage Discord users. Through reflexive thematic analysis, we show how players leverage Discord to create more collaborative and socially enriched experiences that extend beyond the game itself. However, gaming together on Discord also resulted in social and security risks. We conceptualize gaming together on Discord as a cross-platform practice that extends gameplay beyond a game and supports players' social needs. Additionally, cross-platform practice also introduces the 'platform gap,' where fragmented governance between platforms exposed players to risks. To address this tension, we propose design implications aimed at bridging the platform gap, strengthening communication channels, and supporting safer gaming experiences.

---


### 155. [Auditable CT Phenotyping Through Report-derived Radiological Observations](https://arxiv.org/abs/2608.25948)

**<font color=#1a73e8>作者：</font>** Riga Wu, Walter Witschey, Yicheng Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image foundation models can predict clinical phenotypes from computed tomography (CT), but strong performance leaves open whether they read disease-specific findings or shortcuts that correlate with the diagnosis. We tested this in 221 electronic-health-record (EHR) phenotypes using Auditable CT phenotyping (ACT), built on report-derived radiological observations. We trained ACT on 38,317 patients, mined 376,194 observations and evaluated it in 25,183 held-out patients. ACT exceeded five vision-language baselines on zero-shot annotation, and CT-CLIP across 221 phenotypes from unseen CT pulmonary angiography, both under zero-shot scoring (0.651 versus 0.572) and under linear probing (0.709 versus 0.662). Reading each probe exposes what accuracy conceals: only 97 observations occupy the 221 rank-1 positions, and one phrase describing aortic and coronary calcification ranks first for 20 phenotypes, including osteoporosis, urinary tract infection and major depressive disorder. Restricting the bank to clinician-specified evidence redirects those probes onto phenotype-related observations in 86 phenotypes at no accuracy cost (0.751 versus 0.741). Accurate CT-based EHR phenotyping can therefore rest on observations that are not valid evidence for the coded phenotype and that ACT can identify and intervene on.

---


### 156. [4DGS-WAM: Bridging Past and Future with an Object-Centric World Action Model based on 4D Gaussian Splatting](https://arxiv.org/abs/2608.25956)

**<font color=#1a73e8>作者：</font>** Yueen Ma, Zenglin Xu, Irwin King  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current world action models (WAMs) typically operate on 2D visual data. These models can achieve exceptional visual quality, but they lack explicit spatial structure for individual objects and repeatedly process redundant background content. Although point clouds can represent the world in 3D space, they can be difficult to align and accumulate across viewpoints. In this paper, we leverage an explicit 4D Gaussian Splatting (4DGS) representation that separately models dynamic objects and the static background of a scene. For dynamic objects, we use a policy model to predict future actor actions and a world model to predict transformations of their observed Gaussian splats. The static background need not be regenerated for future states, as much of it has already been observed in past frames. This forms an object-centric world action model, which we name 4DGS-WAM. It lifts 2D observations into a persistent 4D representation so that previously observed static content can be reused during future prediction. Future-state extrapolation can then focus on modeling the evolution of dynamic objects. Experiments on KITTI-MOT evaluate short-horizon prediction and past reconstruction.

---


### 157. [Less Contouring, More Accuracy: Lesion-Guided ROI Deep Learning for Ovarian Ultrasound Classification](https://arxiv.org/abs/2608.25965)

**<font color=#1a73e8>作者：</font>** Mehran Ahmad, Ali Abbasian Ardakani, Afshin Mohammadi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ovarian lesion classification using transvaginal ultrasound remains challenging due to overlapping imaging characteristics and the dependence on expert interpretation. This study investigates whether lesion-guided region-of-interest (ROI) deep learning can achieve competitive diagnostic performance while reducing the annotation burden associated with pixel-level lesion segmentation. Two publicly available ovarian ultrasound datasets were evaluated: the Multi-Modality Ovarian Tumor Ultrasound (MMOTU) dataset for eight-class classification and the Ovarian Ultrasound Dataset (OUD) for binary classification. Four strategies were compared under a unified framework: global image-based deep learning, lesion-guided ROI-based deep learning, lesion contour-based deep learning, and contour-based radiomics with machine learning classifiers. Four deep learning architectures, MaxViT-Tiny, Swin Transformer, EfficientNet-B7, and ResNet18, were evaluated. Radiomics models were developed using support vector machine, k-nearest neighbors, and artificial neural network classifiers, with ANOVA-based feature selection applied for the lower-sample OUD dataset. The lesion-guided ROI strategy achieved the strongest overall performance, with MaxViT-Tiny obtaining 93.10% accuracy and an AUC of 0.99 on MMOTU and 97.56% accuracy and an AUC of 0.99 on OUD. The contour-based approach achieved comparable accuracy but required substantially higher annotation effort. These findings demonstrate that lesion-guided ROI deep learning provides an effective balance between diagnostic performance and annotation efficiency, offering a practical approach for scalable AI-assisted ovarian ultrasound analysis

---


### 158. [Quantitative Analysis of $ω$-Regular Robust MDPs](https://arxiv.org/abs/2608.25968)

**<font color=#1a73e8>作者：</font>** Ali Asadi, Krishnendu Chatterjee, Ehsan Kafshdar Goharshady 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Robust Markov Decision Processes (RMDPs) generalize classical MDPs by allowing uncertainty in transition probabilities and optimizing against their worst-case realization. We consider $(s,a)$-rectangular RMDPs with \emph{linearly defined} uncertainty sets and study parity objectives, which are a canonical representation of $\omega$-regular objectives. An uncertainty set is linearly defined if it is described by linear inequalities over the transition distribution together with auxiliary variables, which capture the standard $L_1$ and $L_\infty$ balls as well as general polytopic uncertainty sets.
The quantitative value is the supremum, over all agent policies, of the satisfaction probability guaranteed against the adversarial environment. Previous work studied the qualitative analysis, namely the almost-sure (resp. positive) problem that asks whether a single agent policy guarantees satisfaction with probability one (resp. positive probability) against every environment policy. In this work, we solve the exact quantitative problem.
Our contributions are threefold. First, we show that both the agent and the environment admit pure memoryless optimal policies. Second, we give a polynomial-time algorithm for quantitative parity on linearly defined robust Markov chains and use it as a subroutine in a policy-iteration algorithm for RMDPs. The algorithm combines quantitative one-step improvements with qualitative almost-sure improvements. Finally, we report experiments comparing our approach with the explicit reduction to stochastic games.

---


### 159. [PANDA - Prototype-Anchored Alignment for Partially Unpaired Multimodal Learning, with Applications to Alzheimers MRI and TCGA Pathology](https://arxiv.org/abs/2608.25970)

**<font color=#1a73e8>作者：</font>** Sheethal Bhat, Mahfuzur Rahman Chowdhury, Paula Andrea Perez-Toro 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal medical prediction often faces incomplete pairing: auxiliary modalities with complementary signal are available for only a subset of subjects (or none) and cannot be assumed at deployment. We introduce PANDA (Prototype Anchored Data Alignment), a two-stage framework that transfers auxiliary information to a primary-modality model without auxiliary inputs at inference. Stage 1 learns a shared embedding from the paired subset and estimates class prototypes from auxiliary modalities; Stage 2 trains the primary encoder on all subjects using cross-entropy plus alignment to the frozen prototypes. Because supervision is defined at the class-prototype level, PANDA accommodates arbitrary pairing rates, including zero subject overlap. We evaluate PANDA on two applications. On a 1,021-subject multi-scanner ADNI cohort, we perform AD/CN classification with three auxiliary modalities at distinct pairing rates: tabular scores (44.8%), FDG-PET (18.7%), and external handwriting kinematics (0% overlap). Relative to the same-backbone MRI-only baseline, PANDA attains AUC 0.868 +-0.020 (+7.9pp) and reduces 1.5T CN false positives by 24.3pp; on a fully trainable Conv5-FC3 backbone it reaches AUC 0.893 (best overall). A pairing-rate ablation shows that the joint anchor remains within seed noise from 75% to 5% pairing. On TCGA-Lung survival prediction from whole-slide images with RNA-seq as auxiliary data, PANDA improves over WSI-only on 2-year OS (AUC +3.5pp) and Cox PH (C-index +9.0pts) and outperforms full-fusion training, which underperforms WSI-only, while requiring no RNA at inference; wide confidence intervals on this smaller cohort keep the gains below conventional significance. Overall, PANDA provides a deployment-oriented mechanism for leveraging incomplete auxiliary modalities to improve primary-modality prediction.

---


### 160. [Lost but not erased: Finding traces of a forgotten language in neural speech models](https://arxiv.org/abs/2608.25976)

**<font color=#1a73e8>作者：</font>** Peter Plantinga, Charlotte Moore, Peter W. Donhauser 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> International adoptees retain phonological traces of a birth language they can no longer speak or comprehend, a persistence typically attributed to a biologically-timed critical period. We asked whether it could instead reflect the ordinary dynamics of learning, using automatic speech recognition models that simulate the international adoptee experience without maturational confounds. Models were trained on one language and then abruptly switched to a second. We found that traces of the first language persisted throughout second-language training, but mainly in the lowest, pre-phonemic layers. These traces were functional, as models with early exposure re-learned their lost first language 14% faster than naive models; this advantage held even against models adopted early from a related language and disappeared when the earliest layers were substituted from a non-adopted model. We argue that these critical-period effects reflect entrenchment of foundational representations rather than a maturational loss of plasticity, and that experience plays a central role in critical periods in language acquisition.

---


### 161. [FRAME: separating sampling variation from representational cause in medical imaging fairness](https://arxiv.org/abs/2608.25981)

**<font color=#1a73e8>作者：</font>** Mahshad Lotfinia, Daniel Truhn, Andreas Maier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Subgroup performance differences are the standard evidence for fairness bias in medical imaging, and the usual response removes the demographic information that a model encodes. Here we introduce Fair-model Reference And Mechanism Evaluation (FRAME), a two-step framework for auditing such a claim. The first step derives a fair-model reference, the distribution of the difference under exact fairness at the observed subgroup sizes. In the second step, we test the remainder with two operators in representation space. One operator cannot change a within-group ranking by construction. Across 702,206 images and 36 encoders, the reference accounts for a median 41% of the reported race difference and 22% of the age difference. Injecting demographic decodability leaves the remainder unchanged, while entangling the group with the disease direction raises the race difference from 0.077 to 0.118. No intervention we tested changes the remainder more than a change of random seed does. Those interventions reduce a difference at the operating point and leave the within-group ranking difference at a median of 0.000. Applied to 89 differences in 9 published studies across 6 medical imaging modalities, the reference accounts for a median 25% of a rate difference and 70% of a difference in the area under the receiver operating characteristic curve. Image-text pretraining instead raises worst-group performance by about 0.05. Applying FRAME before choosing an intervention could distinguish differences that need a mechanistic explanation from differences compatible with sampling variation at the current cohort sizes.

---


### 162. [Uncertainty-Guided Latent Diffusion Models for Faithful Super Resolution](https://arxiv.org/abs/2608.25998)

**<font color=#1a73e8>作者：</font>** Ren Wang, Yung-Yu Chuang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The perception-distortion trade-off poses a fundamental challenge in single-image super-resolution (SR). Although diffusion-based SR methods excel at generating perceptually realistic images, achieving high fidelity remains a key limitation. Recent advances in diffusion-based SR have shown promise in improving fidelity, but these methods often compromise perceptual quality due to their high reliance on a high-fidelity image. To address this, we introduce UGDiff, a novel diffusion guidance paradigm designed to further improve the perception-distortion balance. In particular, we first estimate the reconstruction uncertainty of the latent features corresponding to a high-fidelity image. This uncertainty is then used to guide the diffusion process to selectively restore high-frequency details in high-uncertainty regions, while preserving fidelity elsewhere. Furthermore, our guidance method adaptively identifies the high-uncertainty regions by considering not only the estimated uncertainty but also the posterior variance of the diffusion sampler at each timestep. This relaxes the reliance on the high-fidelity image in the later stages of sampling, thereby achieving a better perception-distortion balance. Extensive experimental results demonstrate that our method performs favorably against state-of-the-art diffusion-based SR methods.

---


### 163. [Imitation Learning for Connection-Tableau Construction](https://arxiv.org/abs/2608.26009)

**<font color=#1a73e8>作者：</font>** Fredrik Rømming, Mantas Bakšys, Martin S. Fixman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An automated theorem prover builds a proof step by step, choosing at each point what to add and what to remove. We cast this construction as a policy acting in a transition system induced by a formal calculus, which fixes which steps are sound: for clausal connection tableaux, leanCoP-style search and plCoP/rlCoP-style planning then become stateful policies over one interface, and policy-learning methods apply directly. We equip such policies with a graph neural network that scores proof edits from structure that transfers across problems, train it by imitation learning from found proofs, and measure how performance holds as we remove search scaffolding, from full symbolic backtracking to a policy the network drives alone. Within a fixed step budget on M2k, MPTP2078-bushy, and TPTP v9.2.1, learned policies solve up to 46% more problems than leanCoP, and reach proofs in an order of magnitude fewer steps.

---


### 164. [Beyond Local Surprise: Grounded Dialogue as Selective Belief Revision under Referential Uncertainty](https://arxiv.org/abs/2608.26035)

**<font color=#1a73e8>作者：</font>** Ziming Liu, Bhanu Chaitanya Jasti, Ziyang Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a speaker refers to a scene that the listener cannot directly see, the listener must decide whether to preserve its current understanding or revise it as new utterances arrive. Many language systems treat local mismatch as a cue for updating: divergence from the current understanding encourages adjustment. Yet conversational understanding may be more conservative, interpreting mismatching evidence relative to prior understanding rather than immediately revising it. We introduce a controlled, data-driven framework for turn-by-turn preserve/revise decisions in dialogue, where competing revision policies are learned under otherwise identical conditions. We compare four theory-driven revision strategies, each reflecting a different assumption about when listeners should preserve or revise. Two findings stand out. First, a mismatch-driven policy that updates solely based on local divergence reacts strongly to mismatch but destabilizes grounding and degrades retrieval. Second, an uncertainty-sensitive policy extends mismatch-based updating with accumulated evidence, preserving coherent understanding while maintaining strong retrieval performance. Surprisingly, coherent understanding emerges from a counterintuitive pattern: local mismatch promotes preservation, whereas accumulated uncertainty promotes revision, suggesting that listeners maintain prior understanding despite local mismatch and revise only when uncertainty sufficiently accumulates. This pattern is consistent with conceptual pact theory.

---


### 165. [How Much Rank Does LoRA Need? Rank-Error Bounds for Transformer Attention](https://arxiv.org/abs/2608.26052)

**<font color=#1a73e8>作者：</font>** Gerard Conangla Planes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Choosing the rank of a low-rank adaptation (LoRA) update is usually an empirical task. In this paper, we provide a task-dependent theory of the approximation error achievable at each LoRA rank for Transformer attention. We fix a pretrained attention head, a target attention function, and a distribution over inputs from the downstream task, and bound the smallest expected Kullback--Leibler (KL) error achievable by a rank-$r$ query LoRA update. When target attention probabilities are bounded away from zero, we prove a lower bound of the error proportional to $\psi(\|d\|_2)$, where $d$ is the difference between candidate and target attention scores and $\psi(t)=\min\{t^2,t\}$. We also prove an unconditional upper bound $\min\{\|d\|_2^2/4,\sqrt2\|d\|_2\}$. Under explicit realizability, geometry, and moment conditions, we then bound the best rank-$r$ error between an explicit multiple of $\psi(\sqrt{T_r})$ and $\min\{T_r/4,\sqrt{2T_r}\}$, where $T_r$ is the downstream-weighted tail energy of the target update. We also provide target-Fisher bounds when candidate scores remain within a fixed range of the target scores, and an unrestricted lower bound when a subset of tokens carries most of the probability mass. These spectral bounds describe finite-score approximation. We then construct explicit families in which softmax saturation makes the rank required to match the attention function strictly smaller than the rank required to match the finite logits. Finally, we extend the analysis to fused multi-head LoRA and joint query/key updates, exposing the effects of rank sharing and query/key factorization constraints.

---


### 166. [Fine-Tuning Whisper for Automatic Speech Recognition in Baniwa: A Preliminary Study](https://arxiv.org/abs/2608.26060)

**<font color=#1a73e8>作者：</font>** Leonardo Duart, Tiago Fonseca, Thiago Chacón  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Speech Recognition (ASR) technologies have achieved remarkable performance in recent years through the use of large multilingual foundation models. However, most advances remain concentrated on high-resource languages, while indigenous languages continue to suffer from a lack of speech resources and language technologies. This work presents a preliminary study on the adaptation of Whisper for Automatic Speech Recognition in Baniwa, an indigenous Arawakan language spoken in Brazil, Colombia, and Venezuela. The experiments were conducted using a corpus of 1,373 manually transcribed recordings obtained from a linguistic documentation project. The corpus contains approximately 0.54 hours of speech and consists primarily of isolated words and short elicited utterances. The Whisper Small model was fine-tuned using supervised learning and evaluated using Word Error Rate (WER) and Character Error Rate (CER). The best model achieved a WER of 37.5% and a CER of 7.45%, demonstrating that multilingual foundation models can be successfully adapted to extremely low-resource indigenous languages. The results establish an initial baseline for Baniwa Automatic Speech Recognition and provide a foundation for future research involving larger datasets, language-specific adaptation strategies, and post-processing techniques.

---


### 167. [Group-Shared Low-Rank Approximation for Mobile-Efficient Pointwise Convolutions in Large-Kernel CNNs](https://arxiv.org/abs/2608.26069)

**<font color=#1a73e8>作者：</font>** Hao Luo, Yiting Yang, Wenyi Zhao 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-kernel Convolutional Neural Networks (CNNs) deliver remarkable performance in vision tasks by significantly expanding receptive fields, yet their quadratic parameter growth critically impedes storage-efficient edge deployment. While existing efficient architectures adopt parameter-efficient depthwise separable convolution backbones that leverage techniques like low-rank approximation and weight sharing to compress depthwise convolutions, we identify a critical oversight: pointwise convolutions dominate parameter volume (>87% in models like RepLKNet-31B) and constitute the primary deployment bottleneck on resource-constrained edge devices. This results in prohibitive storage costs and severe memory-loading constraints on resource-limited devices (e.g., smartphones with 4-12 GB Random Access Memory (RAM)). To overcome this, we propose Channel Group-Shared (CGS) low-rank approximation, a novel Singular Value Decomposition (SVD)-based parameter-sharing strategy. CGS constructs a structured low-rank paradigm isomorphic to SVD decomposition, comprising shared (high-parameter-cost) down/up-projection matrices across channel groups within a layer and channel-group-specific (low-parameter-cost) scalable diagonal matrices. This group-sharing design achieves significant parameter reduction. Extensive experiments demonstrate that large-kernel CNNs (RepLKNet, ConvNeXt, SLaK) enhanced with CGS strike an empirically favorable balance between competitive performance and substantially reduced storage costs. Crucially, by alleviating storage constraints, reducing memory bandwidth pressure during loading, and minimizing model loading latency, CGS enables the feasible deployment of pre-trained large-kernel CNN models on edge devices, thereby bridging the gap between high-performance vision models and practical edge deployment.

---


### 168. [From Fleet to Lab: Revisiting the Security and Complexity of Industrial Rowhammer Mitigation](https://arxiv.org/abs/2608.26072)

**<font color=#1a73e8>作者：</font>** Hritvik Taneja, Moinuddin Qureshi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper studies efficient and secure Rowhammer mitigation at the Memory-Controller (MC). Rowhammer mitigation faces a fundamental tradeoff between tracking storage and mitigation rate: precise trackers (such as Misra-Gries) avoid unnecessary mitigations but require large CAM structures, whereas sampling-based schemes (such as PARA) require no storage but incur frequent mitigations even when not under attack. Microsoft recently deployed Sigries, an MC-side Rowhammer defense that combines an under-provisioned Misra-Gries tracker with a row-sampling fallback, in its Azure Cobalt 200 SoC. Sigries observed that the tracker-to-sampling transition can be insecure, and claimed the reverse transition is always safe. Our analysis shows that this transition is also vulnerable, and a Round-Robin Attack across sub-banks reduces the MTTF of Sigries to about 1 second, 8 orders of magnitude below the 13 years with PARA. Sigries also suffers from CAM complexity and high storage overheads.
Our proposal, FiRM (Filtered Rowhammer Mitigation), is based on the insight that, for a secure design, the tracking-mode and sampling-mode should not be configured independently but co-designed to ensure the system remains secure not only in both modes but also during transitions. FiRM incurs zero slowdown for benign workloads, since they do not exceed the filtering threshold, and also replaces the complex CAM-based tracker with simple SRAM filters. To handle stressful patterns, we propose FiRM-P (probabilistic) and FiRM-D (deterministic). FiRM-P uses varying probabilities during transitions and steady state to ensure both security and low performance overhead. FiRM-D provides guaranteed deterministic security by modulating the rate of mitigation. Both FiRM-P and FiRM-D have less storage overhead than Sigries. Our paper shows that a principled approach can avoid both the insecurity and the complexity of Sigries.

---


### 169. [ICON Decomposition: Multivariate Concept-Level Explanations of Deep Representations for Model Auditing](https://arxiv.org/abs/2608.26083)

**<font color=#1a73e8>作者：</font>** Roshan Prakash Rane, Marco Simnacher, Manuel Pfeuffer 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks often exploit spurious associations in their training data, a failure known as shortcut learning. Concept-based explainability methods screen for shortcuts by testing whether concepts such as a patient's sex or scanner settings can be decoded from a network layer. Because each concept is evaluated in isolation, these methods can mistake correlations between concepts as evidence that the model uses them. We introduce ICON decomposition, which instead quantifies how much of a layer's variance each concept explains after accounting for all other concepts and the outcome. On synthetic data with known ground truth, ICON recovers concept importance more accurately than seven alternative baseline methods. On skin-lesion and brain-imaging models, it isolates the concepts on which a model genuinely relies, quantifies the representation unexplained by any of the supplied concepts, and yields sparse explanations that we validate by retraining and out-of-distribution testing.

---


### 170. [MyoMechanix: Biomechanically-Grounded Compositional Skilled Activity Understanding and Coaching](https://arxiv.org/abs/2608.26094)

**<font color=#1a73e8>作者：</font>** Hao Yin, Paritosh Parmar, Lijun Gu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing action quality assessment (AQA) datasets and methods rely primarily on visual inputs such as RGB and pose, overlooking physiological dynamics such as muscle mechanics and often modeling actions as monolithic patterns. These limitations hinder fine-grained, biomechanically grounded feedback. We introduce MyoMechanix, a multimodal ecosystem for weight-loaded actions that aligns motion with muscle activity. Expert-annotated, it contains 7,500+ samples of 20 actions from 38 subjects, with synchronized multiview RGB video, 3D pose, sEMG, and additional physiological signals, forming the largest multimodal AQA benchmark to date. We further construct the Fitness Knowledge Graph (FKG), which organizes expert annotations into structured relationships among actions, phases, key steps, errors, and corrective feedback, enabling compositional scoring and interpretable assessment. Building on these representations, we develop CUBIST (Compositional Ontological Reasoning Engine), which performs decomposition-analysis-recomposition for fine-grained error attribution and feedback generation. We also establish MyoMechanix-AQA, MyoMechanix-VideoQA, and a novel MyoMechanix-Video2EMG task. Experiments show that multimodal sensing and structured representations improve performance, interpretability, and error attribution, with CUBIST achieving state-of-the-art results; VideoQA enhances language-grounded action understanding; and Video2EMG suggests video-based alternatives to costly EMG sensing. MyoMechanix advances skilled activity understanding toward biomechanically grounded, multimodal, and compositional reasoning for Physical AI applications in fitness, rehabilitation, healthcare, and machine learning. Project page: this https URL

---


### 171. [RefVideo-6M: A Reliable Reference-Based Dataset for Instructional Video Editing](https://arxiv.org/abs/2608.26101)

**<font color=#1a73e8>作者：</font>** Bojia Zi, Xiaoyan Yang, Yu Zhou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video editing have been largely driven by large-scale instruction-based datasets. However, existing datasets still suffer from two critical limitations. First, target videos are commonly produced by automatic editing models, which may introduce visible artifacts and unreliable supervision signals. Second, most public datasets rely primarily on textual instructions, while lacking visual references that are crucial for precise, identity-preserving, and controllable editing. To address these limitations, we introduce RefVideo-6M, a large-scale reference-guided editing dataset containing 5 million video editing samples and 1 million image editing samples. To ensure reliable supervision, our dataset uses a construction pipeline that treats artifact-free real videos as editing targets and generates quality-filtered input conditions with multiple editing experts. In addition, it provides approximately 6 million visual references, covering diverse reference types and editing scenarios, thereby enabling models to learn fine-grained visual correspondence beyond text-only instructions. Based on RefVideo-6M, we further train a reference-guided video editing model, Ref-MoT, to evaluate the effectiveness and scalability of the proposed dataset. Extensive experiments demonstrate that RefVideo-6M provides substantially more reliable supervision than existing datasets and enables the training of powerful editing models with improved visual quality, controllability, and reference consistency. The open-source dataset is available at this https URL.

---


> [!TIP]
> 当前位于：**151-171**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-171**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
