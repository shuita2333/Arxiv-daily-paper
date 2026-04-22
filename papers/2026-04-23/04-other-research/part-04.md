# 📦 其他研究 | 2026年04月23日

> 本类共 **244** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-244](./part-05.md)

---

### 151. [FairTree: Subgroup Fairness Auditing of Machine Learning Models with Bias-Variance Decomposition](https://arxiv.org/abs/2604.19357)

**<font color=#1a73e8>作者：</font>** Rudolf Debelak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The evaluation of machine learning models typically relies mainly on performance metrics based on loss functions, which risk to overlook changes in performance in relevant subgroups. Auditing tools such as SliceFinder and SliceLine were proposed to detect such groups, but usually have conceptual disadvantages, such as the inability to directly address continuous covariates. In this paper, we introduce FairTree, a novel algorithm adapted from psychometric invariance testing. Unlike SliceFinder and related algorithms, FairTree directly handles continuous, categorical, and ordinal features without discretization. It further decomposes performance disparities into systematic bias and variance, allowing a categorization of changes in algorithm performance. We propose and evaluate two variations of the algorithm: a permutation-based approach, which is conceptually closer to SliceFinder, and a fluctuation test. Through simulation studies that include a direct comparison with SliceLine, we demonstrate that both approaches have a satisfactory rate of false-positive results, but that the fluctuation approach has relatively higher power. We further illustrate the method on the UCI Adult Census dataset. The proposed algorithms provide a flexible framework for the statistical evaluation of the performance and aspects of fairness of machine learning models in a wide range of applications even in relatively small data.

---


### 152. [Detection of T-shirt Presentation Attacks in Face Recognition Systems](https://arxiv.org/abs/2604.19365)

**<font color=#1a73e8>作者：</font>** Mathias Ibsen, Loris Tim Ide, Christian Rathgeb 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face recognition systems are often used for biometric authentication. Nevertheless, it is known that without any protective measures, face recognition systems are vulnerable to presentation attacks. To tackle this security problem, methods for detecting presentation attacks have been developed and shown good detection performance on several benchmark datasets. However, generalising presentation attack detection methods to new and novel types of attacks is an ongoing challenge. In this work, we employ 1,608 T-shirt attacks of the T-shirt Face Presentation Attack (TFPA) database using 100 unique presentation attack instruments together with 152 bona fide presentations. In a comprehensive evaluation, we show that this type of attack can compromise the security of face recognition systems. Furthermore, we propose a detection method based on spatial consistency checks in order to detect said T-shirt attacks. Precisely, state-of-the-art face and person detectors are combined to analyse the spatial positions of detected faces and persons based on which T-shirt attacks can be reliably detected.

---


### 153. [Mind2Drive: Predicting Driver Intentions from EEG in Real-world On-Road Driving](https://arxiv.org/abs/2604.19368)

**<font color=#1a73e8>作者：</font>** Ghadah Alosaimi, Hanadi Alhamdan, Wenke E 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting driver intention from neurophysiological signals offers a promising pathway for enhancing proactive safety in advanced driver assistance systems, yet remains challenging in real-world driving due to EEG signal non-stationarity and the complexity of cognitive-motor preparation. This study proposes and evaluates an EEG-based driver intention prediction framework using a synchronised multi-sensor platform integrated into a real electric vehicle. A real-world on-road dataset was collected across 32 driving sessions, and 12 deep learning architectures were evaluated under consistent experimental conditions. Among the evaluated architectures, TSCeption achieved the highest average accuracy (0.907) and Macro-F1 score (0.901). The proposed framework demonstrates strong temporal stability, maintaining robust decoding performance up to 1000 ms before manoeuvre execution with minimal degradation. Furthermore, additional analyses reveal that minimal EEG preprocessing outperforms artefact-handling pipelines, and prediction performance peaks within a 400-600 ms interval, corresponding to a critical neural preparatory phase preceding driving manoeuvres. Overall, these findings support the feasibility of early and stable EEG-based driver intention decoding under real-world on-road conditions. Code: this https URL.

---


### 154. [IonMorphNet: Generalizable Learning of Ion Image Morphologies for Peak Picking in Mass Spectrometry Imaging](https://arxiv.org/abs/2604.19369)

**<font color=#1a73e8>作者：</font>** Philipp Weigand, Niels Nawrot, Nikolas Ebert 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Peak picking is a fundamental preprocessing step in Mass Spectrometry Imaging (MSI), where each sample is represented by hundreds to thousands of ion images. Existing approaches require careful dataset-specific hyperparameter tuning, and often fail to generalize across acquisition protocols. We introduce IonMorphNet, a spatial-structure-aware representation model for ion images that enables fully data-driven peak picking without any task-specific supervision. We curate 53 publicly available MSI datasets and define six structural classes capturing representative spatial patterns in ion images to train standard image backbones for structural pattern classification. Once trained, IonMorphNet can assess ion images and perform peak picking without additional hyperparameter tuning. Using a ConvNeXt V2-Tiny backbone, our approach improves peak picking performance by +7 % mSCF1 compared to state-of-the-art methods across multiple datasets. Beyond peak picking, we demonstrate that spatially informed channel reduction enables a 3D CNN for patch-based tumor classification in MSI. This approach matches or exceeds pixel-wise spectral classifiers by up to +7.3 % Balanced Accuracy on three tumor classification tasks, indicating meaningful ion image selection. The source code and model weights are available at this https URL.

---


### 155. [TACENR: Task-Agnostic Contrastive Explanations for Node Representations](https://arxiv.org/abs/2604.19372)

**<font color=#1a73e8>作者：</font>** Vasiliki Papanikou, Evaggelia Pitoura  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph representation learning has achieved notable success in encoding graph-structured data into latent vector spaces, enabling a wide range of downstream tasks. However, these node representations remain opaque and difficult to interpret. Existing explainability methods primarily focus on supervised settings or on explaining individual representation dimensions, leaving a critical gap in explaining the overall structure of node representations. In this paper, we propose TACENR (Task-Agnostic Contrastive Explanations for Node Representations), a local explanation method that identifies not only attribute features but also proximity and structural ones that contribute the most in the representation space. TACENR builds on contrastive learning, through which we learn a similarity function in the representation space, revealing which are the features that play an important role in the representation of a node. While our focus is on task-agnostic explanations, TACENR can be applied to supervised scenarios as well. Experimental results demonstrate that proximity and structural features play a significant role in shaping node representations and that our supervised variant performs comparably to existing task-specific approaches in identifying the most impactful features.

---


### 156. [Towards Energy Impact on AI-Powered 6G IoT Networks: Centralized vs. Decentralized](https://arxiv.org/abs/2604.19377)

**<font color=#1a73e8>作者：</font>** Anjie Qiu, Donglin Wang, Sanket Partani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The emergence of sixth-generation (6G) technologies has introduced new challenges and opportunities for machine learning (ML) applications in Internet of Things (IoT) networks, particularly concerning energy efficiency. As model training and data transmission contribute significantly to energy consumption, optimizing these processes has become critical for sustainable system design. This study first conduct analysis on the energy consumption model for both centralized and decentralized architecture and then presents a testbed deployed within the German railway infrastructure, leveraging sensor data for ML-based predictive maintenance. A comparative analysis of distributed versus Centralized Learning (CL) architectures reveals that distributed models maintain competitive predictive accuracy (~90%) while reducing overall electricity consumption by up to 70%. These findings underscore the potential of distributed ML to improve energy efficiency in real-world IoT deployments, particularly by mitigating transmission-related energy costs.

---


### 157. [HarmoniDiff-RS: Training-Free Diffusion Harmonization for Satellite Image Composition](https://arxiv.org/abs/2604.19392)

**<font color=#1a73e8>作者：</font>** Xiaoqi Zhuang, Jefersson A. Dos Santos, Jungong Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Satellite image composition plays a critical role in remote sensing applications such as data augmentation, disaste simulation, and urban planning. We propose HarmoniDiff-RS, a training-free diffusion-based framework for harmonizing composite satellite images under diverse domain conditions. Our method aligns the source and target domains through a Latent Mean Shift operation that transfers radiometric characteristics between them. To balance harmonization and content preservation, we introduce a Timestep-wise Latent Fusion strategy by leveraging early inverted latents for high harmonization and late latents for semantic consistency to generate a set of composite candidates. A lightweight harmony classifier is trained to further automatically select the most coherent result among them. We also construct RSIC-H, a benchmark dataset for satellite image harmonization derived from fMoW, providing 500 paired composition samples. Experiments demonstrate that our method effectively performs satellite image composition, showing strong potential for scalable remote-sensing synthesis and simulation tasks. Code is available at: this https URL.

---


### 158. [Does Self-Consistency Improve the Recall of Encyclopedic Knowledge?](https://arxiv.org/abs/2604.19395)

**<font color=#1a73e8>作者：</font>** Sho Hoshino, Ukyo Honda, Peinan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While self-consistency is known to improve performance on symbolic reasoning, its effect on the recall of encyclopedic knowledge is unclear due to a lack of targeted evaluation grounds. To address this, we establish such a knowledge recall split for the popular MMLU benchmark by applying a data-driven heuristic from prior work. We validate this split by showing that the performance patterns on the symbolic reasoning and knowledge recall subsets mirror those of GSM8K and MedMCQA, respectively. Using this solid ground, we find that self-consistency consistently improves performance across both symbolic reasoning and knowledge recall, even though its underlying CoT prompting is primarily effective for symbolic reasoning. As a result, we achieve an 89\% accuracy on MMLU, the best performance to date with the use of GPT-4o.

---


### 159. [VIVA Stimuli: A Web-Based Platform for Eye Tracking Stimuli](https://arxiv.org/abs/2604.19397)

**<font color=#1a73e8>作者：</font>** Suleyman Ozdel, Virmarie Maquiling, Kadir Burak Buldu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Reproducibility in eye-tracking research is increasingly important as researchers conduct diverse experiments and seek to validate or replicate findings. However, exact replication remains challenging due to differences in laboratory practices and experimental setups. Inconsistent stimulus presentation can yield divergent metrics from identical oculomotor behavior, yet the stimulus layer remains largely unstandardized. Existing tools often require programming expertise or depend on specific hardware vendors. We introduce VIVA Stimuli, a web-based platform for standardized eye-tracking stimulus presentation. It provides configurable task types, including fixation, smooth pursuit, cognitive load, blink, slippage, content display, and questionnaires within a unified environment. The platform supports any eye-tracking technology, including wearable and screen-based VOG trackers, LFI sensors, and EOG devices. ArUco markers enable synchronization for trackers with scene cameras, while a WebSocket architecture ensures temporal synchronization for those without. A visual experiment flow editor allows protocols to be exported and shared, enabling identical stimulus replication across laboratories.

---


### 160. [Optimal Routing for Federated Learning over Dynamic Satellite Networks: Tractable or Not?](https://arxiv.org/abs/2604.19399)

**<font color=#1a73e8>作者：</font>** Yi Zhao, Di Yuan, Tao Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is a key paradigm for distributed model learning across decentralized data sources. Communication in each FL round typically consists of two phases: (i) distributing the global model from a server to clients, and (ii) collecting updated local models from clients to the server for aggregation. This paper focuses on a type of FL where communication between a client and the server is relay-based over dynamic networks, making routing optimization essential. A typical scenario is in-orbit FL, where satellites act as clients and communicate with a server (which can be a satellite, ground station, or aerial platform) via multi-hop inter-satellite links. This paper presents a comprehensive tractability analysis of routing optimization for in-orbit FL under different settings. For global model distribution, these include the number of models, the objective function, and routing schemes (unicast versus multicast, and splittable versus unsplittable flow). For local model collection, the settings consider the number of models, client selection, and flow splittability. For each case, we rigorously prove whether the global optimum is obtainable in polynomial time or the problem is NP-hard. Together, our analysis draws clear boundaries between tractable and intractable regimes for a broad spectrum of routing problems for in-orbit FL. For tractable cases, the derived efficient algorithms are directly applicable in practice. For intractable cases, we provide fundamental insights into their inherent complexity. These contributions fill a critical yet unexplored research gap, laying a foundation for principled routing design, evaluation, and deployment in satellite-based FL or similar distributed learning systems.

---


### 161. [Revisiting Catastrophic Forgetting in Continual Knowledge Graph Embedding](https://arxiv.org/abs/2604.19401)

**<font color=#1a73e8>作者：</font>** Gerard Pons, Carlos Escolano, Besim Bilalli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge Graph Embeddings (KGEs) support a wide range of downstream tasks over Knowledge Graphs (KGs). In practice, KGs evolve as new entities and facts are added, motivating Continual Knowledge Graph Embedding (CKGE) methods that update embeddings over time. Current CKGE approaches address catastrophic forgetting (i.e., the performance degradation on previously learned tasks) primarily by limiting changes to existing embeddings.
However, we show that this view is incomplete. When new entities are introduced, their embeddings can interfere with previously learned ones, causing the model to predict them in place of previously correct answers. This phenomenon, which we call entity interference, has been largely overlooked and is not accounted for in current CKGE evaluation protocols. As a result, the assessment of catastrophic forgetting becomes misleading, and CKGE methods performance is systematically overestimated.
To address this issue, we introduce a corrected CKGE evaluation protocol that accounts for entity interference. Through experiments on multiple benchmarks, we show that ignoring this effect can lead to performance overestimation of up to 25%, particularly in scenarios with significant entity growth. We further analyze how different CKGE methods and KGE models are affected by the different sources of forgetting, and introduce a catastrophic forgetting metric tailored to CKGE.

---


### 162. [VecHeart: Holistic Four-Chamber Cardiac Anatomy Modeling via Hybrid VecSets](https://arxiv.org/abs/2604.19403)

**<font color=#1a73e8>作者：</font>** Yihong Chen, Pascal Fua  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate cardiac anatomy modeling requires the model to be able to handle intricate interrelations among structures. In this paper, we propose VecHeart, a unified framework for holistic reconstruction and generation of four-chamber cardiac structures. To overcome the limitations of current feed-forward implicit methods, specifically their restriction to single-object modeling and their neglect of inter-part correlations, we introduce Hybrid Part Transformer, which leverages part-specific learnable queries and interleaved attention to capture complex inter-chamber dependencies. Furthermore, we propose Anatomical Completion Masking and Modality Alignment strategies, enabling the model to infer complete four-chamber structures from partial, sparse, or noisy observations, even when certain anatomical parts are entirely missing. VecHeart also seamlessly extends to 3D+t dynamic mesh sequence generation, demonstrating exceptional versatility. Experiments show that our method achieves state-of-the-art performance, maintaining high-fidelity reconstruction across diverse challenging scenarios. Code will be released.

---


### 163. [Understanding Password Preferences, Memorability, and Security through a Human-Centered Lens](https://arxiv.org/abs/2604.19410)

**<font color=#1a73e8>作者：</font>** Duru Paker, Suleyman Ozdel, Enkelejda Kasneci  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Passwords remain the primary authentication method, yet user-created passwords are often the weakest due to the security-usability trade-off. Although AI-based password generators are emerging, little is known about their effectiveness and user perceptions. This eye-tracking study examined how behavior during password creation, selection, and memorization relates to objective and subjective password quality. Four password models, three AI-based (DeepSeek-API, ChatGPT-API, PassGPT) and one rule-based random generator, generated suggestions from participants' self-generated passwords across four website contexts. Eye movements were recorded throughout the experiment. Results confirm the expected trade-off between AI-generated password strength and human memorability but also reveal a novel behavioral link. Despite stronger AI-generated passwords, participants favored self-generated ones. Notably, visual attention to contextual cues was significantly correlated with higher password entropy. This suggests that security is shaped not only by the generation tool but also by users' visual engagement with contextual cues, highlighting the potential of attention-driven security design.

---


### 164. [GOLD-BEV: GrOund and aeriaL Data for Dense Semantic BEV Mapping of Dynamic Scenes](https://arxiv.org/abs/2604.19411)

**<font color=#1a73e8>作者：</font>** Joshua Niemeijer, Alaa Eddine Ben Zekri, Reza Bahmanyar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding road scenes in a geometrically consistent, scene-centric representation is crucial for planning and mapping. We present GOLD-BEV, a framework that learns dense bird's-eye-view (BEV) semantic environment maps-including dynamic agents-from ego-centric sensors, using time-synchronized aerial imagery as supervision only during training. BEV-aligned aerial crops provide an intuitive target space, enabling dense semantic annotation with minimal manual effort and avoiding the ambiguity of ego-only BEV labeling. Crucially, strict aerial-ground synchronization allows overhead observations to supervise moving traffic participants and mitigates the temporal inconsistencies inherent to non-synchronized overhead sources. To obtain scalable dense targets, we generate BEV pseudo-labels using domain-adapted aerial teachers, and jointly train BEV segmentation with optional pseudo-aerial BEV reconstruction for interpretability. Finally, we extend beyond aerial coverage by learning to synthesize pseudo-aerial BEV images from ego sensors, which support lightweight human annotation and uncertainty-aware pseudo-labeling on unlabeled drives.

---


### 165. [TESO: Online Tracking of Essential Matrix by Stochastic Optimization](https://arxiv.org/abs/2604.19420)

**<font color=#1a73e8>作者：</font>** Jaroslav Moravec, Radim Šára, Akihiro Sugimoto  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Maintaining long-term accuracy of stereo camera calibration parameters is important for autonomous systems' perception. This work proposes Online Tracking of Essential Matrix by Stochastic Optimization (TESO). The core mechanisms of TESO are: 1) a robust loss function based on kernel correlation over tentative correspondences, 2) an adaptive online stochastic optimization on the essential manifold. TESO has low CPU and memory requirements, relies on a few hyperparameters, and eliminates the need for data-driven training, enabling the usage in resource-constrained online perception systems. We evaluated the influence of TESO on geometric precision, rectification quality, and stereo depth consistency. On the large-scale MAN TruckScenes dataset, TESO tracks rotational calibration drift with 0.12 deg precision in the Y-axis (critical for stereo accuracy) while the X- and Z-axes are five times more precise. Tracking applied to sequences with simulated drift shows similar precision with respect to the reference as tracking applied to no-drift sequences, indicating the tracker is unbiased. On the KITTI dataset, TESO revealed systematic inconsistencies in extrinsic parameters across stereo pairs, confirming previous published findings. We verified that intrinsic decalibration affected these errors, as evidenced by the conflicting behavior of the rectification and depth metrics. After correcting the reference calibration, TESO improved its rotation precision around the Y-axis 20 times to 0.025 deg and its depth accuracy 50 times. Despite its lightweight design, direct optimization of the proposed TESO loss function alone achieves accuracy comparable to that of neural network-based single-frame methods.

---


### 166. [Allow Me Into Your Dream: A Handshake-and-Pull Protocol for Sharing Mixed Realities in Spontaneous Encounters](https://arxiv.org/abs/2604.19423)

**<font color=#1a73e8>作者：</font>** Botao Amber Hu, Yilan Elan Tao, Bernhard Riecke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mixed reality systems support shared anchors and co-located interaction, yet they lack a socially legible protocol for entering another person's mixed reality in public settings. We frame this as a protocol problem: co-located MR sharing requires a staged sequence -- Discover, Consent, Confirm, Allow, Spatial Colocation, Sync Objects, Permission Management -- each demanding user understanding and agreement. Using AirDrop and Apple Vision Pro SharePlay as a baseline, we show that MR encounter complexity far exceeds file transfer, yet must feel equally effortless. We present TouchPort, an embodied sharing protocol that collapses this multi-stage sequence into a single gesture: a handshake and pull that simultaneously signals intent, negotiates consent, and initiates a temporary shared encounter layer between otherwise separate mixed realities. Through three implied scenarios, we demonstrate the protocol's expressive range in the transition from isolated to spontaneously shared realities. We discuss how embodied gestures can address the consent problem in ubiquitous MR and examine the ethical tensions of encounter protocols for MR futures.

---


### 167. [Seeing Your Mindless Face: How Viewing One's Live Self Interrupts Mindless Short-Form Video Scrolling](https://arxiv.org/abs/2604.19424)

**<font color=#1a73e8>作者：</font>** Kyungjin Kim, Minjeong Kim, Soobeen Jeong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The widespread, addictive consumption of short-form videos, which allegedly causes "brain rot," has become an urgent public concern. This study proposes that self-related cues serve as an intrinsic, self-reflective strategy that enhances self-control over media overuse. We developed an app that de-immerses users by periodically displaying different self-related cues (live camera, selfie, name in text, and black screen) and tested their effects in a laboratory experiment (N=84). Overall, findings show that self-related cues effectively disrupt mindless viewing, enabling users to voluntarily stop short-form video consumption. Interestingly, the black screen, intended as a control, elicited the greatest intention to use the app: Participants noted in the follow-up interview that they preferred the subtler reflection on a black screen over the explicit image from a live camera. The findings offer practical design guidelines for implementing self-awareness interventions in mobile contexts, including which modalities work best and how real-time contextual anchoring enhances effectiveness.

---


### 168. [seneca: A Personalized Conversational Planner](https://arxiv.org/abs/2604.19425)

**<font color=#1a73e8>作者：</font>** Simon Bohnen, Gabriel Garbers, Lukas Ellinger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Knowledge work demands sustained self-regulation, prioritization, and reflection-yet existing planning tools only partially support these needs. Digital to-do list applications feature task persistence but lack goal representation. Paper-based planning frameworks offer effective planning strategies but cannot adapt to individual users. Conversational AI systems enable flexible reflection but lack persistence and accountability. Moreover, none of these tools address a fundamental challenge: users' expressed demands often diverge from their underlying needs.
This paper introduces seneca, a conceptual framework for a personalized, AI-assisted planner that integrates the complementary strengths of these three approaches. seneca combines a conversational agent that scaffolds reflection and asks clarifying questions, a persistent database that tracks goals and behavioral patterns, and a processor that synchronizes information between them. We describe this architecture and outline a phased evaluation strategy combining automated testing with simulated users and longitudinal human studies measuring goal attainment, planning realism, and goal-value alignment.

---


### 169. [Discerning Authorship in Online Health Communities: Experience, Trust, and Transparency Implications for Moderating AI](https://arxiv.org/abs/2604.19429)

**<font color=#1a73e8>作者：</font>** Yefim Shulman, Agnieszka Kitkowska, Mark Warner  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> For online health communities, community trust is paramount. Yet, advances in Large Language Models (LLMs) generating advice may erode this trust, especially if users cannot identify whether LLMs have been used. We investigate the feasibility of community-based detection of health advice authorship and how self-moderation of LLMs could help enhance advice utilization. In an online experiment, we evaluate people's ability to distinguish AI-generated from human-written advice across two health conditions, considering lived experience with a condition, AI-recognition training, and user attitudes towards transparency and trust around AI use. Our results indicate the need for transparency coupled with trust. We find little evidence of people's ability to discern advice authorship. However, we find a consistent effect of the health condition. Our qualitative findings identify unreliable signals, resulting in flawed heuristic evaluations of the advice. Our findings point to opportunities to improve the self-moderation of LLM-based AI and aid community-based AI moderation.

---


### 170. [DINO Eats CLIP: Adapting Beyond Knowns for Open-set 3D Object Retrieval](https://arxiv.org/abs/2604.19432)

**<font color=#1a73e8>作者：</font>** Xinwei He, Yansong Zheng, Qianru Han 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models have shown great promise for open-set 3D object retrieval (3DOR) through efficient adaptation to multi-view images. Leveraging semantically aligned latent space, previous work typically adapts the CLIP encoder to build view-based 3D descriptors. Despite CLIP's strong generalization ability, its lack of fine-grainedness prompted us to explore the potential of a more recent self-supervised encoder-DINO. To address this, we propose DINO Eats CLIP (DEC), a novel framework for dynamic multi-view integration that is regularized by synthesizing data for unseen classes. We first find that simply mean-pooling over view features from a frozen DINO backbone gives decent performance. Yet, further adaptation causes severe overfitting on average view patterns of known classes. To combat it, we then design a module named Chunking and Adapting Module (CAM). It segments multi-view images into chunks and dynamically integrates local view relations, yielding more robust features than the standard pooling strategy. Finally, we propose Virtual Feature Synthesis (VFS) module to mitigate bias towards known categories explicitly. Under the hood, VFS leverages CLIP's broad, pre-aligned vision-language space to synthesize virtual features for unseen classes. By exposing DEC to these virtual features, we greatly enhance its open-set discrimination capacity. Extensive experiments on standard open-set 3DOR benchmarks demonstrate its superior efficacy.

---


### 171. [Malicious ML Model Detection by Learning Dynamic Behaviors](https://arxiv.org/abs/2604.19438)

**<font color=#1a73e8>作者：</font>** Sarang Nambiar, Dhruv Pradhan, Ezekiel Soremekun  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Pre-trained machine learning models (PTMs) are commonly provided via Model Hubs (e.g., Hugging Face) in standard formats like Pickles to facilitate accessibility and reuse. However, this ML supply chain setting is susceptible to malicious attacks that are capable of executing arbitrary code on trusted user environments, e.g., during model loading. To detect malicious PTMs, state-of-the-art detectors (e.g., PickleScan) rely on rules, heuristics, or static analysis, but ignore runtime model behaviors. Consequently, they either miss malicious models due to under-approximation (blacklisting) or miscategorize benign models due to over-approximation (static analysis or whitelisting). To address this challenge, we propose a novel technique (DynaHug) which detects malicious PTMs by learning the behavior of benign PTMs using dynamic analysis and machine learning (ML). DynaHug trains an ML classifier (one-class SVM (OCSVM)) on the runtime behaviours of task-specific benign models. We evaluate DynaHug using over 25,000 benign and malicious PTMs from different sources including Hugging Face and MalHug. We also compare DynaHug to several state-of-the-art detectors including static, dynamic and LLM-based detectors. Results show that DynaHug is up to 44% more effective than existing baselines in terms of F1-score. Our ablation study demonstrates that our design decisions (dynamic analysis, OCSVM, clustering) contribute positively to DynaHug's effectiveness.

---


### 172. [LoViF 2026 Challenge on Real-World All-in-One Image Restoration: Methods and Results](https://arxiv.org/abs/2604.19445)

**<font color=#1a73e8>作者：</font>** Xiang Chen, Hao Li, Jiangxin Dong 等 57 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a review for the LoViF Challenge on Real-World All-in-One Image Restoration. The challenge aimed to advance research on real-world all-in-one image restoration under diverse real-world degradation conditions, including blur, low-light, haze, rain, and snow. It provided a unified benchmark to evaluate the robustness and generalization ability of restoration models across multiple degradation categories within a common framework. The competition attracted 124 registered participants and received 9 valid final submissions with corresponding fact sheets, significantly contributing to the progress of real-world all-in-one image restoration. This report provides a detailed analysis of the submitted methods and corresponding results, emphasizing recent progress in unified real-world image restoration. The analysis highlights effective approaches and establishes a benchmark for future research in real-world low-level vision.

---


### 173. [Heterogeneity-Aware Personalized Federated Learning for Industrial Predictive Analytics](https://arxiv.org/abs/2604.19451)

**<font color=#1a73e8>作者：</font>** Yuhan Hu, Xiaolei Fang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated prognostics enable clients (e.g., companies, factories, and production lines) to collaboratively develop a failure time prediction model while keeping each client's data local and confidential. However, traditional federated models often assume homogeneity in the degradation processes across clients, an assumption that may not hold in many industrial settings. To overcome this, this paper proposes a personalized federated prognostic model designed to accommodate clients with heterogeneous degradation processes, allowing them to build tailored prognostic models. The prognostic model iteratively facilitates the underlying pairwise collaborations between clients with similar degradation patterns, which enhances the performance of personalized federated learning. To estimate parameters jointly using decentralized datasets, we develop a federated parameter estimation algorithm based on proximal gradient descent. The proposed approach addresses the limitations of existing federated prognostic models by simultaneously achieving model personalization, preserving data privacy, and providing comprehensive failure time distributions. The superiority of the proposed model is validated through extensive simulation studies and a case study using the turbofan engine degradation dataset from the NASA repository.

---


### 174. [ZC-Swish: Stabilizing Deep BN-Free Networks for Edge and Micro-Batch Applications](https://arxiv.org/abs/2604.19453)

**<font color=#1a73e8>作者：</font>** Suvinava Basak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Batch Normalization (BN) is a cornerstone of deep learning, yet it fundamentally breaks down in micro-batch regimes (e.g., 3D medical imaging) and non-IID Federated Learning. Removing BN from deep architectures, however, often leads to catastrophic training failures such as vanishing gradients and dying channels. We identify that standard activation functions, like Swish and ReLU, exacerbate this instability in BN-free networks due to their non-zero-centered nature, which causes compounding activation mean-shifts as network depth increases. In this technical communication, we propose Zero-Centered Swish (ZC-Swish), a drop-in activation function parameterized to dynamically anchor activation means near zero. Through targeted stress-testing on BN-free convolutional networks at depths 8, 16, and 32, we demonstrate that while standard Swish collapses to near-random performance at depth 16 and beyond, ZC-Swish maintains stable layer-wise activation dynamics and achieves the highest test accuracy at depth 16 (51.5%) with seed 42. ZC-Swish thus provides a robust, parameter-efficient solution for stabilizing deep networks in memory-constrained and privacy-preserving applications where traditional normalization is unviable.

---


### 175. [API Security Based on Automatic OpenAPI Mapping](https://arxiv.org/abs/2604.19471)

**<font color=#1a73e8>作者：</font>** Yarin Levi, Ran Dubin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents Map Reduce Graph (MRG), a novel unsupervised method for modeling and securing HTTP REST APIs. MRG learns API structure from real-world traffic without prior knowledge or labels, automatically generating OpenAPI-compliant documentation by reconstructing routes, methods, and parameter formats. MRG enables real-time updates, explainable visualization, and anomaly detection, helping identify undocumented or evolving behaviors. It detects malformed requests, structural deviations, and injection attacks using graph-based validation and a deep autoencoder for payload analysis. Compared to state-of-the-art methods like HRAL and FT-ANN, MRG achieves up to 11.4% higher recall, over 20 times faster inference, and perfect precision (100%) on multiple API-layer attacks. Designed for dynamic microservice environments, MRG operates in three phases - training, updating, and detection - and integrates smoothly with observability and security tools. This work contributes a fully automated, efficient pipeline for real-time API visibility, schema inference, and anomaly detection without manual tuning or labeled data.

---


### 176. [TS-Attn: Temporal-wise Separable Attention for Multi-Event Video Generation](https://arxiv.org/abs/2604.19473)

**<font color=#1a73e8>作者：</font>** Hongyu Zhang, Yufan Deng, Zilin Pan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating high-quality videos from complex temporal descriptions that contain multiple sequential actions is a key unsolved problem. Existing methods are constrained by an inherent trade-off: using multiple short prompts fed sequentially into the model improves action fidelity but compromises temporal consistency, while a single complex prompt preserves consistency at the cost of prompt-following capability. We attribute this problem to two primary causes: 1) temporal misalignment between video content and the prompt, and 2) conflicting attention coupling between motion-related visual objects and their associated text conditions. To address these challenges, we propose a novel, training-free attention mechanism, Temporal-wise Separable Attention (TS-Attn), which dynamically rearranges attention distribution to ensure temporal awareness and global coherence in multi-event scenarios. TS-Attn can be seamlessly integrated into various pre-trained text-to-video models, boosting StoryEval-Bench scores by 33.5% and 16.4% on Wan2.1-T2V-14B and Wan2.2-T2V-A14B with only a 2% increase in inference time. It also supports plug-and-play usage across models for multi-event image-to-video generation. The source code and project page are available at this https URL.

---


### 177. [Deep sprite-based image models: An analysis](https://arxiv.org/abs/2604.19480)

**<font color=#1a73e8>作者：</font>** Zeynep Sonat Baltacı, Romain Loiseau, Mathieu Aubry  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While foundation models drive steady progress in image segmentation and diffusion algorithms compose always more realistic images, the seemingly simple problem of identifying recurrent patterns in a collection of images remains very much open. In this paper, we focus on sprite-based image decomposition models, which have shown some promise for clustering and image decomposition and are appealing because of their high interpretability. These models come in different flavors, need to be tailored to specific datasets, and struggle to scale to images with many objects. We dive into the details of their design, identify their core components, and perform an extensive analysis on clustering benchmarks. We leverage this analysis to propose a deep sprite-based image decomposition method that performs on par with state-of-the-art unsupervised class-aware image segmentation methods on the standard CLEVR benchmark, scales linearly with the number of objects, identifies explicitly object categories, and fully models images in an easily interpretable way.

---


### 178. [Translating Ethical Frameworks Into User-Centred Anti-Social Behaviour Interventions](https://arxiv.org/abs/2604.19492)

**<font color=#1a73e8>作者：</font>** Rachel Hill, Tom Owen, Julian Hough  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In 2025 one million Anti-Social Behaviour (ASB) cases were recorded in England & Wales, impacting community cohesion. Statutory guidance presents punitive interventions that lack technological input and does not often root ethical frameworks within government system design. This work takes a novel approach in framing ASB intervention as a human-computer interaction problem by embedding an ethical framework into two digital designs, aiming to increase public responsibility and prevent ASB. The first design is extracted from UK public opinion research, the ethical themes include punitive proportionality, personalisation, and responsibility. The second are digital interventions that present a set of QR-based public reporting interfaces and a web-based ASB awareness course that precedes punitive escalation. Our methodology involves structured interviews and online surveys. Results positively evaluated the framework and QR interfaces. Such outcomes could inform the expansion of technological intervention utilisation that does not replace existing punitive approaches, but balances them.

---


### 179. [EvoPatch-IoT: Evolution-Aware Cross-Architecture Vulnerability Retrieval and Patch-State Profiling for BusyBox-Based IoT Firmware](https://arxiv.org/abs/2604.19496)

**<font color=#1a73e8>作者：</font>** Yinhao Xiao, Huixi Li, Yongluo Shen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> BusyBox is one of the most widely reused userland components in Linux-based Internet-of-Things (IoT) firmware, yet its security assessment remains difficult because firmware images are frequently stripped, vendor patch practices are inconsistent, and the same source component is compiled for heterogeneous architectures. We propose EvoPatch-IoT, an evolution-aware cross-architecture retrieval framework for stripped BusyBox firmware binaries. EvoPatch-IoT combines anonymous instruction/context features, graph-level statistics, per-binary geometric priors, and historical function prototypes to localize homologous and potentially vulnerable functions without relying on symbols, source paths, or version strings at test time. We further construct a large-scale BusyBox benchmark from 57 historical versions, 270 unstripped binaries, 285 stripped binaries, and 130 source releases, yielding 1,550,752 function-symbol rows, 1,290,369 analysis-function rows, and 155,845 high-confidence stripped-to-unstripped matches. On 57 fully covered versions and 1,020 directed architecture pairs, EvoPatch-IoT achieves a weighted Hit@1 of 34.56\% and Hit@10 of 56.24\%, outperforming the strongest baseline by 16.04\% and 26.85\%, respectively, and reducing the expected manual inspection space by 98.98\%. The method is best on 56 of 57 versions and maintains consistent advantages on difficult architecture pairs. In addition, a version-change transfer study reaches a mean ROC-AUC of 0.9887, and a CVE-2021-42386 patch-state proxy obtains 82.44\% mean accuracy and 88.47\% mean F1 across held-out architectures. These results show that evolution-aware binary retrieval is a practical foundation for scalable IoT firmware vulnerability auditing.

---


### 180. [Rank-Turbulence Delta and Interpretable Approaches to Stylometric Delta Metrics](https://arxiv.org/abs/2604.19499)

**<font color=#1a73e8>作者：</font>** Dmitry Pronin, Evgeny Kazartsev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This article introduces two new measures for authorship attribution - Rank-Turbulence Delta and Jensen-Shannon Delta - which generalise Burrows's classical Delta by applying distance functions designed for probabilistic distributions. We first set out the theoretical basis of the measures, contrasting centred and uncentred z-scoring of word-frequency vectors and re-casting the uncentred vectors as probability distributions. Building on this representation, we develop a token-level decomposition that renders every Delta distance numerically interpretable, thereby facilitating close reading and the validation of results. The effectiveness of the methods is assessed on four literary corpora in English, German, French and Russian. The English, German and French datasets are compiled from Project Gutenberg, whereas the Russian benchmark is the SOCIOLIT corpus containing 755 works by 180 authors spanning the eighteenth to the twenty-first centuries. Rank-Turbulence Delta attains attribution accuracy comparable with Cosine Delta; Jensen-Shannon Delta consistently matches or exceeds the performance of canonical Burrows's Delta. Finally, several established attribution algorithms are re-evaluated on the extended SOCIOLIT corpus.

---


### 181. [Bangla Key2Text: Text Generation from Keywords for a Low Resource Language](https://arxiv.org/abs/2604.19508)

**<font color=#1a73e8>作者：</font>** Tonmoy Talukder, G M Shahariar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces \textit{Bangla Key2Text}, a large-scale dataset of $2.6$ million Bangla keyword--text pairs designed for keyword-driven text generation in a low-resource language. The dataset is constructed using a BERT-based keyword extraction pipeline applied to millions of Bangla news texts, transforming raw articles into structured keyword--text pairs suitable for supervised learning. To establish baseline performance on this new benchmark, we fine-tune two sequence-to-sequence models, \texttt{mT5} and \texttt{BanglaT5}, and evaluate them using multiple automatic metrics and human judgments. Experimental results show that task-specific fine-tuning substantially improves keyword-conditioned text generation in Bangla compared to zero-shot large language models. The dataset, trained models, and code are publicly released to support future research in Bangla natural language generation and keyword-to-text generation tasks.

---


### 182. [Evaluating Histogram Matching for Robust Deep learning-Based Grapevine Disease Detection](https://arxiv.org/abs/2604.19510)

**<font color=#1a73e8>作者：</font>** Ruben Pascual, Inés Hernández, Salvador Gutiérrez 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Variability in illumination is a primary factor limiting deep learning robustness for field-based plant disease detection. This study evaluates Histogram Matching (HM), a technique that transforms the pixel intensity distribution of an image to match a reference profile, to mitigate this in grapevine classification, distinguishing among healthy leaves, downy mildew, and spider mite damage. We propose a dual-stage integration of HM: (i) as a preprocessing step for normalization, and (ii) as a data augmentation technique to introduce controlled training variability. Experiments using 1,469 RGB images (comprising homogeneous leaf-focused and heterogeneous canopy samples) to train ResNet-18 models demonstrate that this combination significantly enhances robustness on real-world canopy images. While leaf-focused samples showed marginal gains, the canopy subset improved markedly, indicating that balancing normalization with histogram-based diversification effectively bridges the domain gap caused by uncontrolled lighting.

---


### 183. [When Graph Structure Becomes a Liability: A Critical Re-Evaluation of Graph Neural Networks for Bitcoin Fraud Detection under Temporal Distribution Shift](https://arxiv.org/abs/2604.19514)

**<font color=#1a73e8>作者：</font>** Saket Maganti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The consensus that GCN, GraphSAGE, GAT, and EvolveGCN outperform feature-only baselines on the Elliptic Bitcoin Dataset is widely cited but has not been rigorously stress-tested under a leakage-free evaluation protocol. We perform a seed-matched inductive-versus-transductive comparison and find that this consensus does not hold. Under a strictly inductive protocol, Random Forest on raw features achieves F1 = 0.821 and outperforms all evaluated GNNs, while GraphSAGE reaches F1 = 0.689 +/- 0.017. A paired controlled experiment reveals a 39.5-point F1 gap attributable to training-time exposure to test-period adjacency. Additionally, edge-shuffle ablations show that randomly wired graphs outperform the real transaction graph, indicating that the dataset's topology can be misleading under temporal distribution shift. Hybrid models combining GNN embeddings with raw features provide only marginal gains and remain substantially below feature-only baselines. We release code, checkpoints, and a strict-inductive protocol to enable reproducible, leakage-free evaluation.

---


### 184. [From Experience to Skill: Multi-Agent Generative Engine Optimization via Reusable Strategy Learning](https://arxiv.org/abs/2604.19516)

**<font color=#1a73e8>作者：</font>** Beining Wu, Fuyou Mao, Jiong Lin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative engines (GEs) are reshaping information access by replacing ranked links with citation-grounded answers, yet current Generative Engine Optimization (GEO) methods optimize each instance in isolation, unable to accumulate or transfer effective strategies across tasks and engines. We reframe GEO as a strategy learning problem and propose MAGEO, a multi-agent framework in which coordinated planning, editing, and fidelity-aware evaluation serve as the execution layer, while validated editing patterns are progressively distilled into reusable, engine-specific optimization skills. To enable controlled assessment, we introduce a Twin Branch Evaluation Protocol for causal attribution of content edits and DSV-CF, a dual-axis metric that unifies semantic visibility with attribution accuracy. We further release MSME-GEO-Bench, a multi-scenario, multi-engine benchmark grounded in real-world queries. Experiments on three mainstream engines show that MAGEO substantially outperforms heuristic baselines in both visibility and citation fidelity, with ablations confirming that engine-specific preference modeling and strategy reuse are central to these gains, suggesting a scalable learning-driven paradigm for trustworthy GEO. Code is available at this https URL

---


### 185. [Accelerating Optimization and Machine Learning through Decentralization](https://arxiv.org/abs/2604.19518)

**<font color=#1a73e8>作者：</font>** Ziqin Chen, Zuang Wang, Yongqiang Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized optimization enables multiple devices to learn a global machine learning model while each individual device only has access to its local dataset. By avoiding the need for training data to leave individual users' devices, it enhances privacy and scalability compared to conventional centralized learning, where all data has to be aggregated to a central server. However, decentralized optimization has traditionally been viewed as a necessary compromise, used only when centralized processing is impractical due to communication constraints or data privacy concerns. In this study, we show that decentralization can paradoxically accelerate convergence, outperforming centralized methods in the number of iterations needed to reach optimal solutions. Through examples in logistic regression and neural network training, we demonstrate that distributing data and computation across multiple agents can lead to faster learning than centralized approaches, even when each iteration is assumed to take the same amount of time, whether performed centrally on the full dataset or decentrally on local subsets. This finding challenges longstanding assumptions and reveals decentralization as a strategic advantage, offering new opportunities for more efficient optimization and machine learning.

---


### 186. [Revac: A Social Deduction Reasoning Agent](https://arxiv.org/abs/2604.19523)

**<font color=#1a73e8>作者：</font>** Mihir Shriniwas Arya, Avinash Anish, Aditya Ranjan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Social deduction games such as Mafia present a unique AI challenge: players must reason under uncertainty, interpret incomplete and intentionally misleading information, evaluate human-like communication, and make strategic elimination decisions. Unlike deterministic board games, success in Mafia depends not on perfect information or brute-force search, but on inference, memory, and adaptability in the presence of deception. This work presents the design and evaluation of Revac-8, an AI agent developed for the Social Deduction track of the MindGames Arena competition, where it achieved first place. The final agent evolved from a simple two-stage reasoning system into a multi-module architecture that integrates memory-based player profiling, social-graph analysis of accusations and defenses, and dynamic tone selection for communication. These results highlight the importance of structured memory and adaptive communication for achieving strong performance in high-stakes social environments.

---


### 187. [Revisiting RaBitQ and TurboQuant: A Symmetric Comparison of Methods, Theory, and Experiments](https://arxiv.org/abs/2604.19528)

**<font color=#1a73e8>作者：</font>** Jianyang Gao, Yutong Gou, Yuexuan Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This technical note revisits the relationship between RaBitQ and TurboQuant under a unified comparison framework. We compare the two methods in terms of methodology, theoretical guarantees, and empirical performance, using a reproducible, transparent, and symmetric setup. Our results show that, despite the claimed advantage of TurboQuant, TurboQuant does not provide a consistent improvement over RaBitQ in directly comparable settings; in many tested configurations, it performs worse than RaBitQ. We further find that several reported runtime and recall results in the TurboQuant paper could not be reproduced from the released implementation under the stated configuration. Overall, this note clarifies the shared structure and genuine differences between the two lines of work, while documenting reproducibility issues in the experimental results reported by the TurboQuant paper.

---


### 188. [FOCAL: Filtered On-device Continuous Activity Logging for Efficient Personal Desktop Summarization](https://arxiv.org/abs/2604.19541)

**<font color=#1a73e8>作者：</font>** Haoran Yin, Zhiyuan Wen, Jiannong Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Desktop interaction streams provide a continuous, privacy-sensitive record of interleaved user tasks. Transforming these streams into task-organized personal logs on-device faces two main challenges: exhaustive Vision-Language Model (VLM) processing strains local resources, and global stream processing causes cross-task context pollution. We present FOCAL (Filtered On-device Continuous Activity Logging), a privacy-first multi-agent system utilizing a unified filter-plan-log architecture. It cascades a lightweight Filter Agent for noise suppression, a text-only Brain Agent for task attribution, a Record Agent for selective visual reasoning, and a task-isolated Memory Agent for context-coherent summarization. Experiments on DesktopBench (comprising 2,572 screenshots across 420 complex sessions) show FOCAL reduces total token consumption by 60.4% and VLM call count by 72.3% versus a baseline, while boosting Key Information Recall (KIR) from 0.38 to 0.61. Crucially, under $A{\to}B{\to}A$ task interruptions, FOCAL maintains Task Acc 0.81 and KIR 0.80, whereas the baseline collapses to Task Acc 0.03. FOCAL pioneers the efficient, on-device summarization of instruction-free desktop streams into multi-perspective personal logs.

---


### 189. [Paparazzo: Active Mapping of Moving 3D Objects](https://arxiv.org/abs/2604.19556)

**<font color=#1a73e8>作者：</font>** Davide Allegro, Shiyao Li, Stefano Ghidoni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current 3D mapping pipelines generally assume static environments, which limits their ability to accurately capture and reconstruct moving objects. To address this limitation, we introduce the novel task of active mapping of moving objects, in which a mapping agent must plan its trajectory while compensating for the object's motion. Our approach, Paparazzo, provides a learning-free solution that robustly predicts the target's trajectory and identifies the most informative viewpoints from which to observe it, to plan its own path. We also contribute a comprehensive benchmark designed for this new task. Through extensive experiments, we show that Paparazzo significantly improves 3D reconstruction completeness and accuracy compared to several strong baselines, marking an important step toward dynamic scene understanding. Project page: this https URL

---


### 190. [Enhancing Construction Worker Safety in Extreme Heat: A Machine Learning Approach Utilizing Wearable Technology for Predictive Health Analytics](https://arxiv.org/abs/2604.19559)

**<font color=#1a73e8>作者：</font>** Syed Sajid Ullah, Amir Khan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Construction workers are highly vulnerable to heat stress, yet tools that translate real-time physiological data into actionable safety intelligence remain scarce. This study addresses this gap by developing and evaluating deep learning models, specifically a baseline Long Short-Term Memory (LSTM) network and an attention-based LSTM, to predict heat stress among 19 workers in Saudi Arabia. Using Garmin Vivosmart 5 smartwatches to monitor metrics such as heart rate, HRV, and oxygen saturation, the attention-based model outperformed the baseline, achieving 95.40% testing accuracy and significantly reducing false positives and negatives. With precision, recall, and F1 scores of 0.982, this approach not only improves predictive performance but also offers interpretable results suitable for integration into IoT-enabled safety systems and BIM dashboards, advancing proactive, informatics-driven safety management in the construction industry.

---


### 191. [Separating Geometry from Probability in the Analysis of Generalization](https://arxiv.org/abs/2604.19560)

**<font color=#1a73e8>作者：</font>** Maxim Raginsky, Benjamin Recht  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The goal of machine learning is to find models that minimize prediction error on data that has not yet been seen. Its operational paradigm assumes access to a dataset $S$ and articulates a scheme for evaluating how well a given model performs on an arbitrary sample. The sample can be $S$ (in which case we speak of ``in-sample'' performance) or some entirely new $S'$ (in which case we speak of ``out-of-sample'' performance). Traditional analysis of generalization assumes that both in- and out-of-sample data are i.i.d.\ draws from an infinite population. However, these probabilistic assumptions cannot be verified even in principle. This paper presents an alternative view of generalization through the lens of sensitivity analysis of solutions of optimization problems to perturbations in the problem data. Under this framework, generalization bounds are obtained by purely deterministic means and take the form of variational principles that relate in-sample and out-of-sample evaluations through an error term that quantifies how close out-of-sample data are to in-sample data. Statistical assumptions can then be used \textit{ex post} to characterize the situations when this error term is small (either on average or with high probability).

---


### 192. [Structure-guided molecular design with contrastive 3D protein-ligand learning](https://arxiv.org/abs/2604.19562)

**<font color=#1a73e8>作者：</font>** Carles Navarro, Philipp Tholke, Gianni de Fabritiis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structure-based drug discovery faces the dual challenge of accurately capturing 3D protein-ligand interactions while navigating ultra-large chemical spaces to identify synthetically accessible candidates. In this work, we present a unified framework that addresses these challenges by combining contrastive 3D structure encoding with autoregressive molecular generation conditioned on commercial compound spaces. First, we introduce an SE(3)-equivariant transformer that encodes ligand and pocket structures into a shared embedding space via contrastive learning, achieving competitive results in zero-shot virtual screening. Second, we integrate these embeddings into a multimodal Chemical Language Model (MCLM). The model generates target-specific molecules conditioned on either pocket or ligand structures, with a learned dataset token that steers the output toward targeted chemical spaces, yielding candidates with favorable predicted binding properties across diverse targets.

---


### 193. [EgoSelf: From Memory to Personalized Egocentric Assistant](https://arxiv.org/abs/2604.19564)

**<font color=#1a73e8>作者：</font>** Yanshuo Wang, Yuan Xu, Xuesong Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric assistants often rely on first-person view data to capture user behavior and context for personalized services. Since different users exhibit distinct habits, preferences, and routines, such personalization is essential for truly effective assistance. However, effectively integrating long-term user data for personalization remains a key challenge. To address this, we introduce EgoSelf, a system that includes a graph-based interaction memory constructed from past observations and a dedicated learning task for personalization. The memory captures temporal and semantic relationships among interaction events and entities, from which user-specific profiles are derived. The personalized learning task is formulated as a prediction problem where the model predicts possible future interactions from individual user's historical behavior recorded in the graph. Extensive experiments demonstrate the effectiveness of EgoSelf as a personalized egocentric assistant. Code is available at \href{this https URL}{this https URL\_project/}.

---


### 194. [Lyapunov-Certified Direct Switching Theory for Q-Learning](https://arxiv.org/abs/2604.19569)

**<font color=#1a73e8>作者：</font>** Donghwan Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Q-learning is one of the most fundamental algorithms in reinforcement learning. We analyze constant-stepsize Q-learning through a direct stochastic switching system representation. The key observation is that the Bellman maximization error can be represented exactly by a stochastic policy. Therefore, the Q-learning error admits a switched linear conditional-mean recursion with martingale-difference noise. The intrinsic drift rate is the joint spectral radius (JSR) of the direct switching family, which can be strictly smaller than the standard row-sum rate. Using this representation, we derive a finite-time final-iterate bound via a JSR-induced Lyapunov function and then give a computable quadratic-certificate version.

---


### 195. [RF-HiT: Rectified Flow Hierarchical Transformer for General Medical Image Segmentation](https://arxiv.org/abs/2604.19570)

**<font color=#1a73e8>作者：</font>** Ahmed Marouane Djouama, Abir Belaala, Abdellah Zakaria Sellam 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate medical image segmentation requires both long-range contextual reasoning and precise boundary delineation, a task where existing transformer- and diffusion-based paradigms are frequently bottlenecked by quadratic computational complexity and prohibitive inference latency. We propose RF-HiT, a Rectified Flow Hierarchical Transformer that integrates an hourglass transformer backbone with a multi-scale hierarchical encoder for anatomically guided feature conditioning. Unlike prior diffusion-based approaches, RF-HiT leverages rectified flow with efficient transformer blocks to achieve linear complexity while requiring only a few discretization steps. The model further fuses conditioning features across resolutions via learnable interpolation, enabling effective multi-scale representation with minimal computational overhead. As a result, RF-HiT achieves a strong efficiency-performance trade-off, requiring only 10.14 GFLOPs, 13.6M parameters, and inference in as few as three steps. Despite its compact design, RF-HiT attains 91.27% mean Dice on ACDC and 87.40% on BraTS 2021, achieving performance comparable to or exceeding that of significantly more intensive architectures. This demonstrates its strong potential as a robust, computationally efficient foundation for real-time clinical segmentation.

---


### 196. [TransSplat: Unbalanced Semantic Transport for Language-Driven 3DGS Editing](https://arxiv.org/abs/2604.19571)

**<font color=#1a73e8>作者：</font>** Yanhui Chen, Jiahong Li, Jingchao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-driven 3D Gaussian Splatting (3DGS) editing provides a more convenient approach for modifying complex scenes in VR/AR. Standard pipelines typically adopt a two-stage strategy: first editing multiple 2D views, and then optimizing the 3D representation to match these edited observations. Existing methods mainly improve view consistency through multi-view feature fusion, attention filtering, or iterative recalibration. However, they fail to explicitly address a more fundamental issue: the semantic correspondence between edited 2D evidence and 3D Gaussians. To tackle this problem, we propose TransSplat, which formulates language-driven 3DGS editing as a multi-view unbalanced semantic transport problem. Specifically, our method establishes correspondences between visible Gaussians and view-specific editing prototypes, thereby explicitly characterizing the semantic relationship between edited 2D evidence and 3D Gaussians. It further recovers a cross-view shared canonical 3D edit field to guide unified 3D appearance updates. In addition, we use transport residuals to suppress erroneous edits in non-target regions, mitigating edit leakage and improving local control precision. Qualitative and quantitative results show that, compared with existing 3D editing methods centered on enhancing view consistency, TransSplat achieves superior performance in local editing accuracy and structural consistency.

---


### 197. [A Self-Evolving Framework for Efficient Terminal Agents via Observational Context Compression](https://arxiv.org/abs/2604.19572)

**<font color=#1a73e8>作者：</font>** Jincheng Ren, Siwei Wu, Yizhi Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As model capabilities advance, research has increasingly shifted toward long-horizon, multi-turn terminal-centric agentic tasks, where raw environment feedback is often preserved in the interaction history to support future decisions. However, repeatedly retaining such feedback introduces substantial redundancy and causes cumulative token cost to grow quadratically with the number of steps, hindering long-horizon reasoning. Although observation compression can mitigate this issue, the heterogeneity of terminal environments makes heuristic-based or fixed-prompt methods difficult to generalize. We propose TACO, a plug-and-play, self-evolving Terminal Agent Compression framework that automatically discovers and refines compression rules from interaction trajectories for existing terminal agents. Experiments on TerminalBench (TB 1.0 and TB 2.0) and four additional terminal-related benchmarks (i.e., SWE-Bench Lite, CompileBench, DevEval, and CRUST-Bench) show that TACO consistently improves performance across mainstream agent frameworks and strong backbone models. With MiniMax-2.5, it improves performance on most benchmarks while reducing token overhead by around 10%. On TerminalBench, it brings consistent gains of 1%-4% across strong agentic models, and further improves accuracy by around 2%-3% under the same token budget. These results demonstrate the effectiveness and generalization of self-evolving, task-aware compression for terminal agents.

---


### 198. [Remindful: Designing Reminder Systems for Caregiver Interpretation in Dementia Care](https://arxiv.org/abs/2604.19574)

**<font color=#1a73e8>作者：</font>** Joy Lai, Alex Mihailidis  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital reminder systems are widely used in dementia care to support everyday tasks, but they are typically designed for one-way prompting rather than helping caregivers interpret engagement over time. We present Remindful, a caregiver-informed reminder platform that extends task prompting with caregiver-facing alerts, summaries, and review features to support awareness in home-based dementia care. Drawing on formative caregiver interviews, lived-experience advisor input, and in-home deployments with two caregiver-PLwD dyads, we examine how reminder-based caregiver awareness functions in practice. Our findings show that reminder systems can support caregiver reassurance, household coordination, and awareness of routines over time, but that reminder interaction data is highly context-dependent. Household participation, prompt attribution, routine mismatch, accessibility barriers, and technical failures all shaped what reminder logs could reasonably mean. We argue that reminder systems should not be treated as neutral behavioral sensors, but designed as assistive infrastructures for caregiver interpretation that preserve uncertainty and support contextual sensemaking in real homes.

---


### 199. [A Bolu: A Structured Dataset for the Computational Analysis of Sardinian Improvisational Poetry](https://arxiv.org/abs/2604.19584)

**<font color=#1a73e8>作者：</font>** Silvio Calderaro, Johanna Monti  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The growing interest of Natural Language Processing (NLP) in minority languages has not yet bridged the gap in the preservation of oral linguistic heritage. In particular, extemporaneous poetry - a performative genre based on real-time improvisation, metrical-rhetorical competence - remains a largely unexplored area of computational linguistics. This methodological gap necessitates the creation of specific resources to document and analyse the structures of improvised poetry. This is the context in which A Bolu was created, the first structured corpus of extemporaneous poetry dedicated to cantada logudorese, a variant of the Sardinian language. The dataset comprises 2,835 stanzas for a total of 141,321 tokens. The study presents the architecture of the corpus and applies a multidimensional analysis combining descriptive statistical indices and computational linguistics techniques to map the characteristics of the poetic text. The results indicate that the production of Sardinian extemporaneous poets is characterised by recurring patterns that support Parry and Lord's theory of formulaicity. This evidence not only provides a new key to understanding oral creativity, but also offers a significant contribution to the development of NLP tools that are more inclusive and sensitive to the specificities of less widely spoken languages.

---


### 200. [SmartPhotoCrafter: Unified Reasoning, Generation and Optimization for Automatic Photographic Image Editing](https://arxiv.org/abs/2604.19587)

**<font color=#1a73e8>作者：</font>** Ying Zeng, Miaosen Luo, Guangyuan Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional photographic image editing typically requires users to possess sufficient aesthetic understanding to provide appropriate instructions for adjusting image quality and camera parameters. However, this paradigm relies on explicit human instruction of aesthetic intent, which is often ambiguous, incomplete, or inaccessible to non-expert users. In this work, we propose SmartPhotoCrafter, an automatic photographic image editing method which formulates image editing as a tightly coupled reasoning-to-generation process. The proposed model first performs image quality comprehension and identifies deficiencies by the Image Critic module, and then the Photographic Artist module realizes targeted edits to enhance image appeal, eliminating the need for explicit human instructions. A multi-stage training pipeline is adopted: (i) Foundation pretraining to establish basic aesthetic understanding and editing capabilities, (ii) Adaptation with reasoning-guided multi-edit supervision to incorporate rich semantic guidance, and (iii) Coordinated reasoning-to generation reinforcement learning to jointly optimize reasoning and generation. During training, SmartPhotoCrafter emphasizes photo-realistic image generation, while supporting both image restoration and retouching tasks with consistent adherence to color- and tone-related semantics. We also construct a stage-specific dataset, which progressively builds reasoning and controllable generation, effective cross-module collaboration, and ultimately high-quality photographic enhancement. Experiments demonstrate that SmartPhotoCrafter outperforms existing generative models on the task of automatic photographic enhancement, achieving photo-realistic results while exhibiting higher tonal sensitivity to retouching instructions. Project page: this https URL.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-244](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
