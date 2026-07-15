# 📦 其他研究 | 2026年07月16日

> 本类共 **203** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-203](./part-05.md)

---

### 51. [Operationalising Multi-Dimensional Evaluation for Conversational Agents: A Scalable, Governed Pipeline with Selective Re-evaluation and Model Benchmarking](https://arxiv.org/abs/2607.12085)

**<font color=#1a73e8>作者：</font>** Niranjan Kumar M, Balaji Nagarajan, Karthik Nair 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating retail conversational agents requires methods beyond lexical-overlap metrics to assess intent alignment, factuality, helpfulness, clarity, tone, and overall response quality. Although LLM-as-a-judge methods provide scalable alternatives to human evaluation, production deployment introduces challenges in governance, reproducibility, cost, schema consistency, traceability, and reliability. We present GenAI Evaluation, a governed, configuration-driven pipeline for large-scale evaluation of retail conversational systems. It processes production chatbot logs through normalization, sharding, asynchronous execution, and schema-constrained LLM scoring. The framework evaluates helpfulness, truthfulness, clarity, tone alignment, and translation-specific dimensions. Selective re-evaluation processes only incomplete, malformed, or schema-invalid records, while schema locking, versioned configurations, validation logs, and record-level provenance support auditability. The framework processes approximately 50,000 records daily and has evaluated more than two million interactions. Validation used 12,980 stratified-random human-labeled records from four trained annotators. Classification covered 14 intents, 156 sub-intents, 18 major domains, and 129 sub-domains. The pipeline achieved a macro F1 score of 0.93 and 89% human-acceptability accuracy for translation.

---


### 52. [Causal Supervision of Attention for Affective Behaviour Analysis](https://arxiv.org/abs/2607.12091)

**<font color=#1a73e8>作者：</font>** Nemanja Rašajski, Konstantinos Makantasis, Antonios Liapis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Affective Behaviour Analysis aims to enable machines to infer human affective states from behavioural signals, particularly facial expressions, in real-world environments. The \textit{11th Affective Behaviour Analysis in-the-wild Competition} includes the Multi-Task Learning Challenge based on the s-Aff-Wild2 database, where participants develop a unified framework for Valence-Arousal Estimation, Expression Recognition, and Action Unit Detection. This is challenging because emotion-related cues must be distinguished from spurious factors such as identity, illumination, pose, and demographic variation. Attention mechanisms are well suited as they aggregate information from the most informative facial regions, but may still exploit dataset-specific correlations instead of true affective cues. To improve generalization, we propose an attention pooling framework that promotes subject-invariant attention while increasing feature expressiveness. Our method consists of three components. First, we introduce causal supervision to enforce attention on facial regions with invariant predictive value across subjects. Second, we apply a cross-covariance independence regularization between Key (K) and Value (V) projections to encourage complementary, non-redundant representations. Finally, we replace the linear Value projection with a gated nonlinear SwiGLU transformation to increase feature expressiveness and capture finer-grained affective cues. Our method achieves $CCC_{VA}=0.5123$ for VA estimation on the official validation set, together with $F1_{EX}=0.3116$ and $F1_{AU}=0.3974$ for expression recognition and action unit detection, respectively, resulting in an overall $P$ score (the sum of the individual task metrics) of $1.2214$.

---


### 53. [Thought Experiments for Conceptual Work: A New Application of a (Very) Old Method](https://arxiv.org/abs/2607.12092)

**<font color=#1a73e8>作者：</font>** Leah Hope Ajmani, Mo Houtti, Eric P.S. Baumer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose thought experiments (TEs) as a crucial method for Human-Computer Interaction (HCI) researchers to engage in conceptual work. As an interdisciplinary field, HCI often uses concepts as the fundamental building blocks for larger theories. However, the conceptual commitments we make in this process carry normative consequences. TEs are a well-established philosophical method, whereby a hypothetical but tractable scenario logically progresses to a conclusion. We outline TEs as an interrogative method that brings conceptualizations to their normative implications through logical moves. We illustrate the value of thought experiments through two examples: (1) original thought experiments to critique stakeholders in Value-Sensitive Design and (2) Helen Nissenbaum's use of thought experiments to generate contextual integrity. We discuss how TEs precisely anticipate the potential harms of technologies, allowing HCI to operationalize current calls for increased scrutiny of research ethics and broader implications.

---


### 54. [Sparse Autoencoders for Interpretable Out-of-Distribution Detection](https://arxiv.org/abs/2607.12094)

**<font color=#1a73e8>作者：</font>** Ayush Karmacharya, Luke Luschwitz, Lucia Romero 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable detection of out-of-distribution (OOD) samples is crucial for the safe deployment of machine learning models. Neural networks often produce overconfident predictions for inputs that deviate from their training data, leading to significant degradation in performance. While many OOD detection methods focus on the final output layer, they neglect the rich hierarchical information present in intermediate network layers. This paper introduces a novel approach that leverages sparse autoencoders (SAEs) to learn interpretable features from these intermediate activations. We find that in-distribution (ID) and OOD data activate distinct sets of these sparse features. We propose a new OOD score derived from the cosine similarity between the sparse feature activations of a test sample and the mean activations of ID classes. Our post-hoc detection method not only achieves state-of-the-art performance on standard OOD detection benchmarks, but yields interpretable insights into how distribution shift affects learned representations.

---


### 55. [Representing and Generating Levels Over Time through Playtrace Reconstructive Partitioning](https://arxiv.org/abs/2607.12097)

**<font color=#1a73e8>作者：</font>** Emily Halina, Matthew Guzdial  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Video games are a dynamic medium experienced over time. While there are many Procedural Content Generation (PCG) approaches for generating video game levels, they often use representations that abstract away this dynamic nature. In this paper, we introduce a novel, domain-independent ``cake'' representation for game levels over time which implicitly encodes dynamic information. We present a novel level generation approach Playtrace Reconstructive Partitioning (PRP) specifically developed for this cake representation. We compare against six state-of-the-art PCG approaches in the game domain of \textit{Sokoban}, and find that our approach can generate valid levels without sacrificing solution diversity. We believe our cake representation more neatly encodes the implicit dynamic nature of games compared to existing representations, which allows for our domain-agnostic level generation algorithm PRP.

---


### 56. [ACZ-GSeg: Adaptive Concentric Zone-based Two-stage Ground Segmentation for LiDAR Point Clouds](https://arxiv.org/abs/2607.12110)

**<font color=#1a73e8>作者：</font>** Ge Zhang Chunyang Wang Bin Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ground segmentation is a fundamental prerequisite for autonomous navigation, environmental perception, and object detection in ground mobile platforms. To address the under-segmentation of ground points caused by sparse long-range point clouds, ground undulations, and interference from non-ground structures in complex road scenarios, this paper proposes a two-stage ground segmentation method based on the Adaptive Concentric Zone Model. First, an Adaptive Concentric Zone Model is constructed to dynamically determine the number of sectors in each ring, thereby forming local zones with more balanced point distributions. Based on this model, a two-stage ground segmentation method is developed. In the coarse segmentation stage, a lowest-height seed constraint and height-decay weighting are introduced to establish a weighted principal component analysis plane fitting model, from which ground candidate points are extracted. In the fine segmentation stage, a reflectance intensity consistency constraint is employed to distinguish high-confidence ground points from uncertain points, and the uncertain points are further refined based on the local height stability of high-confidence neighborhoods. Experimental results show that the proposed method achieves Precision, Recall, and F1-score values of 99.12%, 96.24%, and 97.66% on the SemanticKITTI dataset, and 98.72%, 100.00%, and 99.36%, respectively, on a self-collected point cloud acquired using a RUBY-PLUS. The results demonstrate that the proposed method can effectively adapt to the range-dependent distribution characteristics of LiDAR point clouds, which are dense at near ranges and sparse at far ranges. It reduces the misclassification of non-ground points while maintaining ground point recall, thereby effectively improving the stability of ground segmentation.

---


### 57. [Faster AI, Uneven Frontier: Rapid Crossings, a Jagged Frontier, and the Repositioning of Human Judgment](https://arxiv.org/abs/2607.12125)

**<font color=#1a73e8>作者：</font>** Ancuta Margondai, Julie Rader, Emma Rader 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Between 2023 and 2026, frontier AI systems crossed documented human expert baselines on a growing set of bounded, well-specified, evaluable cognitive tasks, including graduate-level science questions, competition mathematics, software-engineering benchmarks, and structured diagnostic reasoning, while the length of tasks such systems can complete at 50% reliability doubled roughly every seven months. These crossings are rapid and broad, but the frontier is jagged: humans retain decisive advantages in long-horizon reliability, genuinely novel problems, calibrated self-knowledge, sample-efficient learning, and embodied action, and benchmark results overstate deployed capability for reasons that are themselves now documented, namely contamination, construct validity, vendor self-evaluation, and the gap between 50% reliability and the reliability that economic work requires. Concurrently, humans increasingly use these systems as cognitive extensions. The offloading literature predicts costs to unaided skill, and early field evidence is consistent with such costs, though the largest meta-analytic evidence on prior technologies points the other way, and the question of whether generative AI differs is open. Finally, the experimental record on human-AI collaboration shows that naive combination often underperforms the stronger partner, implying that the human contribution must be repositioned toward specification, verification, and oversight, a shift visible in experiments but, so far, barely visible in field labor-market data. This paper states the resulting position, rapid crossings on a jagged frontier with a human role that must be redesigned rather than defended, and draws out its theoretical and practical implications.

---


### 58. [Connected by Construction: Learning Tractable Near-Tour Marginals for Traveling Salesman Problems](https://arxiv.org/abs/2607.12127)

**<font color=#1a73e8>作者：</font>** Ke Sun, Xinyuan Zhang, Xinwu Qian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning-based methods for the traveling salesman problem (TSP) are often evaluated through the tours produced after decoding or search, but the learned object itself frequently lives in a surrogate space such as heatmaps, assignments, construction policies, or search-guidance scores. This hides the fundamental question: what Hamiltonian structure has actually been learned before decoding? In this study, we directly answer this question by learning TSP through a structurally meaningful latent object, rather than leaving most of the Hamiltonian structure to the final decoding stage. Based on a connected-by-construction rooted $1$-tree Gibbs family, we propose an end-to-end unsupervised learning pipeline called \emph{C2TSP}. The pipeline learns residual edge perturbations from unbiased TSP cost through implicit differentiation. For structural correction, a smoothed Held--Karp layer restores expected degree balance, while certificate-guided sharpening further pushes the connected distribution toward more tour-like structures. Experiments show that C2TSP yields strong decoding performance while preserving interpretable structural information. Ablations further verify that edge perturbation and certificate-guided sharpening jointly improve both tour cost and tour-like structure.

---


### 59. [Token Reduction Is Not Cost Reduction](https://arxiv.org/abs/2607.12161)

**<font color=#1a73e8>作者：</font>** Sarel Weinberger, Amir Hozez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Context-reduction layers for API-based coding agents, including command-output compressors, retrieval rankers, and payload-optimizing proxies, are usually evaluated by how much text they remove. We ask instead: when does reducing retrieved context or tool output lower the actual billed cost of a coding agent without reducing task success or lengthening its trajectory?
Our primary evidence is a pre-specified, hash-frozen, paired campaign of 2,908 provider-billed Claude Code runs, of which 2,848 were analyzed, covering 103 tasks, seven repositories, and three models. The campaign compared a baseline with two generations of hook-based compression and an API-boundary proxy, within a broader measured program of roughly 5,500 billed executions.
Three findings emerge. First, prompt-cache traffic dominated cost composition. Cache creation and reads accounted for about 87% of reconstructed four-component cost, or about 80% of the actual bill, with an 8.7% dollar-weighted residual that retained telemetry could not attribute. On Haiku 4.5, this residual scaled with thinking effort.
Second, tool-output reduction did not reliably predict billed-cost reduction. An arm that removed 38% of estimated raw tool-output tokens had 6.8% higher paired cost (95% CI: +2.8% to +11.3%), while per-task reduction was only weakly associated with cost change (Pearson r = 0.15, CI crossing zero).
Third, compression can harm task completion by removing action-critical evidence. In a small single-shot study on SWE-bench-derived Go tasks, compression reduced patch application from 27/40 to 15/40 by corrupting verbatim edit anchors, and the compressed grounded arm produced fewer solves at higher observed cost per solve.
We propose a layered evidence standard centered on success-adjusted billed cost rather than token reduction alone.

---


### 60. [Data Safety: Synthetic Data Quality Analysis Using CIFAKE Dataset](https://arxiv.org/abs/2607.12165)

**<font color=#1a73e8>作者：</font>** Kuniko Paxton, Amila Akagić, Koorosh Aslansefat 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, the societal implementation of high-performance image classification models has expanded rapidly. While these models require vast amounts of training data to improve performance, securing sufficient real images is often impractical. As a means to compensate for this shortage, the use of synthetic data is becoming widespread. However, synthetic images are not necessarily equivalent to real images for training purposes. This study systematically analyzes the differences between two types of synthetic images created by different generation methods and real images from three perspectives: high-dimensional feature space, low-level statistics in color space, and the model training process. Furthermore, it experimentally verifies how synthetic data should be utilized by considering realistic data mixing scenarios. This enables the proposal of an evaluation and application strategy for performing preliminary assessments on synthetic images of unknown quality and safely incorporating them into training. This research aims to contribute to enhancing the reliability and safety of image classification models utilizing synthetic images.

---


### 61. [From Geometric Recovery to Causal Validation: A Reproducible Audit of Sparse Autoencoder Features, from Superposition Geometry to Causal Inertness](https://arxiv.org/abs/2607.12166)

**<font color=#1a73e8>作者：</font>** Mohamed Abdessalem Bal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) are the standard for decomposing superposed neural representations into interpretable features, and evaluation relies predominantly on correlational recovery metrics -- cosine similarity between ground-truth directions and decoder atoms. We show this conflates two distinct claims: decoder-geometry alignment and encoder-activation behavior. We reproduce the superposition phase diagram of Elhage et al. (2022), identifying a convergence artifact at high sparsity and an under-described diffuse sharing regime at extreme overcompleteness. We reproduce the TopK-versus-L1 comparison of Gao et al. (2024), with direct evidence of L1 shrinkage. Our central result is causal: subjecting every recovered feature to ablation and steering, we find up to 77% of features passing a recovery bar (cosine >= 0.90) in a degraded SAE -- and 9% in a well-trained one -- are causally inert: the matched atom never fires when the feature is present, including matches at cosine ~1.000. We package the method as sae-causal-audit, a model-agnostic instrument with a deterministic pipeline. Re-auditing refines the finding: inertness decomposes by cause into structural inertness (antipodal-pair geometry, present in good SAEs) and competitive inertness (a TopK pathology of degraded SAEs), and by direction into read- and write-inertness, which five antipodal pairs dissociate completely -- unmonitorable yet steerable through the same atom, with steering specificities of 143-310 attached to zero ablation effects. We document why byte-exact reproducibility is unavailable by construction, and propose reporting it as a stack of claims with explicit scopes. Applying the instrument to a production SAE reproduces the pattern at small scale (14% inert) and surfaces an atom-collision signal: a handful of atoms recur as the nearest match for dozens of unrelated concepts, replicated across three batches.

---


### 62. [We Hebben Een Serieus Translatie: Modeling Intercomprehension as Probabilistic Inference](https://arxiv.org/abs/2607.12169)

**<font color=#1a73e8>作者：</font>** Thomas Hikaru Clark, Edward Gibson, Roger Levy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Intercomprehension refers to partial intelligibility of an unfamiliar language (L2) by a speaker of a related language (L1). How is this zero-shot cross-language comprehension possible? In this work, we extend past work on algorithmic models of noisy-channel inference to model intercomprehension in a Bayesian framework. The model uses an LM in L1 only for scoring latent hypotheses about the translations of observed L2 utterances, and a general-purpose noise model to infer a mapping between L2 and L1 words based on either form-based similarity or symbolic rules. We then conduct a human behavioral experiment, eliciting inferences for utterances in Dutch, Italian, and Ukrainian from speakers of English, Spanish, and Russian, respectively. Our full model shows a closer alignment to the distribution of human intercomprehension performance than ablations, and also compares favorably to zero-shot prompting of much larger models. These results provide a cognitively plausible computational model of intercomprehension, and highlight the flexible inferences made by comprehenders under wide uncertainty in real-world cross-language scenarios. We share our code publicly.

---


### 63. [Self-Consistent Flow: Unifying Velocity and Endpoint Prediction for Rectified Flow Models](https://arxiv.org/abs/2607.12171)

**<font color=#1a73e8>作者：</font>** Xu Han, Jiajing Hu, Li-Ping Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In rectified-flow-based generative models, the neural network can be trained to predict two different targets, such as the instantaneous velocity or the data endpoint, to perform denoising. Although prior work shows that these parameterizations lead to different empirical behaviors, the mechanisms underlying their respective advantages remain to be underexplored, and how to combine them effectively is still unclear. In this work, we analyze how learning errors from different parameterizations affect the generation performance. We show that predicting the data endpoint has a clear training signal that stabilizes training, whereas predicting the velocity maintains stable sampling dynamics near the data manifold. Motivated by these insights, we propose Self-Consistent Flow (SC-Flow), a new method that unifies the benefits of both parameterizations. By employing a lightweight consistency loss, SC-Flow jointly trains a single network to predict both the local velocity and the data endpoint, and the consistency between the two predictions improves the model's performance. The method requires no major architectural changes and adds minimal computational overhead. Extensive experiments on image generation tasks demonstrate that SC-Flow substantially stabilizes optimization and improves the straightness of generation paths, leading to significant gains in generation quality over standard rectified-flow baselines.

---


### 64. [From Reconstruction to Interpretation: Zero-Setup Multi-Phase Segmentation of X-ray Tomography Data](https://arxiv.org/abs/2607.12175)

**<font color=#1a73e8>作者：</font>** Pradyumna Elavarthi, Arun J. Bhattacharjee, Harrison Lisabeth 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> X-ray tomography enables nondestructive characterization of material microstructures, while advances in micro-CT imaging have accelerated volumetric data acquisition and reconstruction. However, rapid interpretation remains limited by image segmentation, which often requires manual thresholding, user prompting, or material-specific model training. We present a zero-setup framework for multi-phase segmentation of synchrotron X-ray tomography data that generates interpretable masks for previously unseen datasets without user input or retraining during deployment. The framework combines a material-agnostic mask preparation strategy with a pretrained semantic segmentation network. It represents commonly occurring structural regions as background, sample, bright, dark-gray, light-gray, and porosity masks. Unlike conventional deep learning pipelines that require dataset-specific annotations and retraining, the proposed framework can be applied directly to new scans and produce diagnostic-level segmentations within minutes of reconstruction. This enables rapid assessment of scan quality, sample morphology, porosity, and attenuation variations during ongoing beamline experiments. The generated masks can later be manually refined or used to fine-tune application-specific models when greater accuracy or material-specific labeling is required. Evaluation on held-out synchrotron micro-CT images and qualitative testing on additional datasets demonstrate consistent and physically meaningful segmentations across varying samples and imaging conditions. The framework also substantially outperforms conventional intensity-based thresholding. By connecting high-speed reconstruction with immediate interpretation, the approach supports near-real-time beamline feedback and scalable AI-assisted scientific imaging workflows.

---


### 65. [TRAIL: A Platform for Configurable Human--AI Teaming Experiments](https://arxiv.org/abs/2607.12180)

**<font color=#1a73e8>作者：</font>** Mohammad Amin Samadi, Pedro Martins De Bastos, Jaeyoon Choi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> An AI teammate's design properties (personality, communication style, when it speaks) can shape a team's trust, coordination, and decisions. Studying this rigorously demands infrastructure no existing tool provides: reproducible configuration of an AI teammate embedded in instrumented, real-time collaboration sustained over time. We present the Team Research and AI Integration Lab (TRAIL), a web platform that makes the AI teammate a configurable, reproducible design object, pairing a Big Five persona with a selective-participation message pipeline, dual memory, chained longitudinal experiments, and export-ready analytics. In a real six-session classroom deployment (about 51 students), TRAIL sustained longitudinal chaining, held the AI to a stable minority of the conversation, and enabled export-driven AI-human text-similarity analysis. A single blind persona change produced a design-consistent double dissociation: a cognitive-scaffolding agent drew stronger contribution ratings and closer linguistic alignment; a socially-supportive agent, a warmer team climate and lower over-reliance.

---


### 66. [Entropy in Semantic Memory Navigation in Blind and Sighted Individuals: The Effect of Visual Experience](https://arxiv.org/abs/2607.12185)

**<font color=#1a73e8>作者：</font>** Felipe D. Toro-Hernández, Rodrigo Lagos, Sergio E. Chaigneau  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Embodied accounts of semantic memory highlight the role of sensorimotor systems in acquiring and storing knowledge. Congenitally blind populations offer a critical test bed for these assumptions, providing an opportunity to assess whether conceptual grounding requires visual experience. In this study, we assessed semantic memory navigation differences between blind and sighted individuals using a property listing task with concrete and abstract concepts. We computed semantic entropy, an embedding-based natural language processing metric that captures the predictability of retrieval. Generalized linear mixed models revealed distinct navigation patterns across groups: while sighted individuals showed higher entropy for abstract than concrete concepts, blind participants did not. Instead, blind individuals exhibited higher entropy for visually salient concrete concepts (e.g., penguin). These results underscore the role of visual experience in the organization and dynamic navigation of semantic memory.

---


### 67. [Overview of Cross-Component In-loop Filters in Video Coding Standards](https://arxiv.org/abs/2607.12186)

**<font color=#1a73e8>作者：</font>** Zhaoyu Li, Xuewei Meng, Jiaqi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-loop filters have been comprehensively explored during the development of video coding standards due to their remarkable noise-reduction capability. In the early stage of video coding, in-loop filters, such as Deblocking Filter, Sample Adaptive Offset, and Adaptive Loop Filter, were performed separately for each component. Recently, cross-component filters were studied to improve the chroma fidelity by exploiting correlations between the luma and chroma channels. This paper summarizes the cross-component filters used in the state-of-the-art video coding standard. Specifically, it includes the Cross-Component Adaptive Loop Filter and Cross-Component Sample Adaptive Offset. Cross-component filters aim to reduce compression artifacts based on the correlation between different components and provide more accurate pixel reconstruction values. In this paper, we introduce the origin, development, and status of cross-component filters in the current video coding standards. Finally, we had some discussions on the further evolutions of cross-component filters.

---


### 68. [Compos3D: Interactive Part-Based Composition for Creative Control in Generative 3D Models](https://arxiv.org/abs/2607.12193)

**<font color=#1a73e8>作者：</font>** Faraz Faruqi, Sean J. Liu, George Fitzmaurice 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While generative AI has unlocked new opportunities for 3D content creation, current workflows often rely on multiple regenerations, which provides limited control and unpredictable outcomes. We present Compos3D, a system that introduces a compositional workflow for generative 3D modeling through remixing. Instead of repeatedly regenerating models, users generate multiple candidates from text or image prompts, select parts of interest via 2D image regions or 3D mesh segments, and assemble them into a coherent design. The system synthesizes these compositions into a refined 3D model, preserving high-level intent while resolving low-level geometry. To evaluate this approach, we conducted a controlled user study comparing remixing and regeneration workflows across both 2D and 3D modalities. Results show that the remixing workflow provides participants with greater creative control, stronger alignment with their intent, and higher satisfaction. We conclude with design recommendations for future AI-assisted 3D modeling workflows.

---


### 69. [MTD-Playground: An Attacker-Aware Evaluation Framework for Network Moving Target Defense](https://arxiv.org/abs/2607.12199)

**<font color=#1a73e8>作者：</font>** Mohammad Farhad, Mohoshin Ara Tahera, Padam Jung Thapa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Moving Target Defense (MTD) has emerged as a proactive network cyber defense paradigm that increases attacker uncertainty through dynamic network reconfiguration techniques such as Software-Defined Networking (SDN)-enabled path randomization. However, existing evaluations remain fragmented due to inconsistent attacker assumptions, attack scenarios, and evaluation metrics, limiting reproducibility and deployment-oriented comparison. In this paper, we present MTD-Playground, an attacker-aware evaluation framework for benchmarking SDN-enabled path-randomization (PR) MTD techniques under realistic enterprise-style multi-stage attack scenarios. Beyond isolated security and performance metrics, MTD-Playground introduces a composite evaluation methodology for analyzing deployment effectiveness, mutation-interval trade-offs, and defender-attacker operational balance. Using periodic path randomization as a representative PR-MTD strategy, our evaluation shows that aggressive mutation intervals reduce attack success rates to 4-20% while increasing attack completion time to 160-311s across evaluated attack scenarios. At the same time, PR-MTD improves throughput by up to 30.9% and reduces internal-path latency without service interruption. Composite analysis further shows that shorter mutation intervals consistently achieve the highest deployment effectiveness and positive defender advantage. These results demonstrate that SDN-based PR-MTD can substantially disrupt multi-stage attack progression while remaining practically deployable in enterprise environments.

---


### 70. [Explaining Intrusion Alert Decisions of Deep Learning-based Network Intrusion Detection Systems for Security Analysts](https://arxiv.org/abs/2607.12203)

**<font color=#1a73e8>作者：</font>** Ayush Kumar, Vrizlynn L.L. Thing  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In this paper, we present EXP-SEC, a novel framework which can explain the intrusion detection decisions of DL-based NIDS (which lead to security alerts) in a way that is aligned with the domain knowledge of analysts working in Security Operations Center (SOC). We highlight the following features of our framework: (1) a forensic module that isolates the suspect packets/flow which likely caused an alert (2) an explanation module which can handle much more complex feature dependencies in network traffic than existing methods (features can be divided into overlapping groups and some groups are more important than others), and (3) a multi-stage mapping module which translates the feature/group-based explanations generated by explanation module to domain-specific explanations suitable for processing by security analysts. We evaluate EXP-SEC with state-of-the-art DL-based NIDS and our evaluation results show that EXP-SEC outperforms xNIDS (existing best performing explanation framework) in terms of group-level and overlap-aware explanation utility metrics while performing similarly in terms of conventional feature-level metrics such as descriptive accuracy, sparsity and stability. Moreover, taking the case of a state-of-the-art DL-based NIDS, we demonstrate the security analyst-friendly explanation format generated by EXP-SEC.

---


### 71. [Forgetful Attention: A Trainable Support-Vector Memory with Certified Selection and Exact Unlearning](https://arxiv.org/abs/2607.12204)

**<font color=#1a73e8>作者：</font>** Vishwajith Ramesh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention can be viewed as an online learner over context, yet existing test-time memories cannot certify that dropping a token leaves outputs unchanged or delete its influence outright. We introduce Support Vector Attention (SV-Attention), a max-margin memory whose weights are support coefficients of a one-class SVM with fixed box parameter C. Its active-set partition gives reserve tokens exactly zero weight, certifying output-preserving eviction; a reversible incremental solver deletes a token to recover the state produced by retraining without it under the same C. In fp64 experiments, decrement and refit recover identical partitions whenever the optimum is unique, and their decision functions match to a median deviation of about 10^-9 (10^-13 on learned keys); the 10^-2 worst case is confined to ill-conditioned duplicates and remains below coefficient decay in every regime. The exact path reuses the maintained KKT inverse in a custom backward. Training uses a separate stabilized batched approximation and does not carry the exact-deletion certificate; it reaches 9,125 tokens/s on a 3.22M-parameter model, while remaining 35.8 times slower than an MPS softmax reference. At matched budgets, certified selection reaches 0.86 vs. 0.32 rare-item recall and retains 0.80 vs. 0.05 deterioration hours on real MIMIC-IV streams. We also demonstrate surgical forgetting, exact editing, patient-record deletion, and a forgettable retrieval memory over real sentence embeddings. On enwik8, the hybrid obtains 2.178 BPC vs. 2.383 for a matched-state sliding-window Transformer across seven seeds (8.6% paired improvement, p=0.001); a three-seed TinyStories result is directionally positive but not significant (p=0.057).

---


### 72. [RegHead: Non-Humanoid Head Blendshapes via Feed-Forward Registration](https://arxiv.org/abs/2607.12206)

**<font color=#1a73e8>作者：</font>** Jiahao Luo, Hao Zhang, Jianqi Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present RegHead, a framework for constructing semantic blendshape sets for animatable non-humanoid head avatars. With a fixed expression vocabulary, semantic blendshapes provide a low-dimensional and interpretable animation interface and support cross-identity retargeting. Building such blendshape sets remains expensive because (i) expression-consistent supervision is scarce, (ii) generated 4D assets typically lack correspondence, and (iii) facial motion is highly localized. We propose (1) a large-scale dataset of non-humanoid identities paired with a shared expression vocabulary, obtained by expanding a small artist-rigged library via fine-tuned image editing; (2) a dense stochastic anchor motion representation tailored to localized facial deformations; and (3) a fast feed-forward registration model that converts unregistered expression meshes into a corresponded blendshape basis by predicting anchor-based deformations from the neutral shape. Experiments show that our approach produces higher-fidelity expression meshes than baselines, while running orders of magnitude faster than optimization. We further demonstrate real-time retargeting from human face tracking signals to non-humanoid characters, capturing both head pose and localized facial motions. Our project page is available at this https URL.

---


### 73. [Beyond Perfect Priors: Adaptive Gaussian Graph for 4D Driving Reconstruction in the Wild](https://arxiv.org/abs/2607.12214)

**<font color=#1a73e8>作者：</font>** Xiaoyun Dong, Qian Xu, Yun Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing 4D driving scenes in the wild (e.g., internet and AI-generated videos) is critical for diverse autonomous driving simulation. While recent Gaussian Scene Graph (GSG) methods achieve impressive visual quality, they heavily rely on precise priors, such as accurate camera poses and LiDAR depth, or manual annotations. When initialized with noisy priors estimated from in-the-wild videos, existing GSG methods suffer from optimization ambiguity (e.g., entangling camera and agent poses) and topological failures (e.g., missing objects), causing severe rendering artifacts. To enable robust in-the-wild reconstruction, we introduce Adaptive Gaussian Graph (AGG), a self-correcting 4D framework. Our Semantically-Guided Tick-Tock Strategy leverages 2D foundation features to explicitly decouple static background and camera pose updates from dynamic agent learning. Concurrently, our Adaptive Topology Evolution module actively rectifies graph structures by spawning missing agents, reassigning misclassified Gaussians, and pruning false positives. To rigorously evaluate this in-the-wild setting, we introduce Wild-30, a challenging benchmark of internet and generative videos. Extensive experiments on KITTI and Wild-30 validate that AGG consistently outperforms state-of-the-art approaches in visual fidelity and robustness under noisy priors.

---


### 74. [Fine-Tuned Multi-Agent Framework for Detecting OCEAN in Life Narratives](https://arxiv.org/abs/2607.12215)

**<font color=#1a73e8>作者：</font>** Rasiq Hussain, Darshil Italiya, Joshua Oltmanns 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accurately assessing personality from text is challenging because traits are latent, context-dependent, and often subtly expressed across long narratives. Large language models (LLMs) offer new opportunities by processing extensive textual contexts, but pretraining of these models can induce latent "personality-like" biases, making single-model inferences inconsistent. We propose a fine-tuned multi-agent framework for detecting OCEAN personality traits, in which sub-agents are conditioned to adopt high, low, or neutral perspectives for each trait through masked language modeling (MLM) and psychometric supervision. A judge LLM aggregates and compares sub-agent outputs to generate final trait predictions, capturing multiple complementary perspectives while mitigating individual model biases. We evaluate the framework on life narrative dataset through quantitative and qualitative experiments, including baselines, ablations, and inference quality analyses. Our approach offers a scalable and interpretable method for text-based personality inference, highlighting the benefits of multi-agent reasoning grounded in psychometric supervision.

---


### 75. [Good Benchmarks](https://arxiv.org/abs/2607.12217)

**<font color=#1a73e8>作者：</font>** Ivan Bercovich  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Good tasks are correct, solvable, verifiable, well-specified, and hard for interesting reasons. The best tasks describe a real problem an experienced practitioner would recognize, in language a practitioner would use, with tests that verify the outcome rather than the approach.

---


### 76. [From Chaos to Clarity: A Framework for Program-Level AI Learning Outcomes](https://arxiv.org/abs/2607.12221)

**<font color=#1a73e8>作者：</font>** Grace Barkhuff, Ian Pruitt, William Gregory Johnson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Industry is leaning into generative artificial intelligence (GenAI), and higher education is under pressure to prepare graduates for a GenAI-augmented workforce. Yet, there is still no clear structure for defining AI readiness across disciplines, programs, courses, and assignments. Current approaches often rely on broad institutional policies or individual course-level decisions, which can also create mixed messages for students, fragmented expectations across programs, and limited visibility for university leaders. In this paper, we argue that higher education needs a more coherent way to connect institutional priorities to curriculum-level action. We propose Program-Level AI Learning Outcomes (PLAI-LOs) as a framework for defining what students graduating from a program should know and be able to do with, without, and about GenAI in a given discipline. The PLAI-LOs framework complements existing program-level learning outcomes and supports alignment across institutional priorities, program-level AI learning outcomes, course-level learning outcomes, and assignment-level objectives. We illustrate the framework with examples from computing and music and show how PLAI-LOs can be implemented through artifact-level GenAI policies, helping programs decide where GenAI should be taught and used, and when students should be expected to work without GenAI. We offer PLAI-LOs as a concrete, measurable, and adaptable path for moving higher education from scattered GenAI rules toward a strategy with clear, learning-centered alignment.

---


### 77. [The GEST-Engine: From Event Graphs to Synthetic Video. A Full Technical Report](https://arxiv.org/abs/2607.12231)

**<font color=#1a73e8>作者：</font>** Nicolae Cudlenco, Mihai Masala, Marius Leordeanu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present the GEST-Engine, a complete system that goes from natural-language text to fully-annotated multi-actor video. At its core is an explicit world model: rather than encoding state as a learned latent, the engine maintains a complete, inspectable representation of the world (which actors exist, where they are, what they are doing, which objects they hold, and how events relate in time and space), expressed as a formal Graph of Events in Space and Time (GEST) and realized deterministically inside the open world of a commercial game engine driven through an open-source multiplayer scripting framework. GESTs are produced either procedurally or by an agentic text-to-GEST system in which an LLM Director plans a story through tool calls validated by a programmatic state backend, so every generated specification is executable by construction. A GEST then enters a four-stage execution pipeline: graph parsing and validation, entity and action grounding, temporal orchestration (Allen-style constraints resolved by Floyd-Warshall transitive closure), and execution and capture. In a single simulation pass the engine emits frame-aligned RGB video, dense per-pixel depth, instance segmentation, per-actor skeletal pose, per-frame pairwise spatial-relation graphs, 2D bounding boxes, event-to-frame temporal mappings, and natural-language descriptions, all at zero marginal annotation cost. We further describe an in-game world editor, runtime capability extraction, a text-generation pipeline, and a production system that renders corpora at scale across parallel virtual machines. Because every frame traces back to a semantic specification, the engine guarantees object permanence, multi-actor coordination, and temporal consistency by construction, making its output valuable as training data, evaluation benchmarks, and diagnostic tools for video understanding.

---


### 78. [Towards Knitted Textile Electromechanical Systems](https://arxiv.org/abs/2607.12237)

**<font color=#1a73e8>作者：</font>** John Martins, Abigail Hou, Brandon Tendilla 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> E-textiles and wearable sensing technologies enable flexible, customizable interfaces for human-computer interaction, with capacitive sensing offering precise touch and pressure detection. While machine knitting provides scalable, mechanically tunable structures ideal for such sensors, few studies develop or characterize insulated conductive yarns engineered for knitting's complex structural geometry and high flexure strain. In this work, we present a yarn dip-coating process, driven by an adjusted dip-coating fluid dynamics model, that enables scalable, machine knittable fabrication of capacitive tactile pressure sensing arrays. We establish optimal dip-coating parameters and concentrations of thermoplastic polyurethane (TPU) dissolved in dimethylformamide (DMF) to create knitting-optimized coatings (~630 um thickness). These fabricated yarns are shown to maintain electromechanical characteristics with minimal deviation after knitting and washing, thus allowing the creation of knitted pressure sensors through multi-layered structures. This process demonstrates that machine knitting with insulated yarns is a viable and reliable manufacturing approach to integrate sensing functionality into wearable textiles.

---


### 79. [Cluster-Weighted EDMD](https://arxiv.org/abs/2607.12243)

**<font color=#1a73e8>作者：</font>** Lorenzo Tomaz, Judd Rosenblatt, Flavio Kicis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extended Dynamic Mode Decomposition (EDMD) approximates Koopman operators from data, but a single global operator is inefficient when different state-space regions exhibit distinct local dynamics. We introduce Cluster-Weighted EDMD (CW-EDMD), which jointly learns a soft phase-space partition and a per-cluster EDMD operator. Its Expectation-Maximization (EM) objective assigns each transition based on both geometric proximity and prediction residuals, so clusters specialize where local Koopman models are accurate rather than where the data are dense. On Lorenz, damped pendulum, and Duffing systems, across 36 configurations and 10 seeds, CW-EDMD improves matched-degree EDMD in one-step and 5s-rollout prediction. Across 288 paired comparisons, there are significant error reductions in 258 cases, increases in 4, and no differences in 26. Median one-step error reductions are 57x, 2.7x, and 12x on pendulum, Duffing, and Lorenz, respectively.

---


### 80. [Rough Path Signature-Guided Geometry Augmentation for Few-Shot Industrial Surface Defect Detection](https://arxiv.org/abs/2607.12245)

**<font color=#1a73e8>作者：</font>** Jiaqi Kuang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot industrial defect detection remains difficult for standard supervised detectors, which achieve poor performance on boundary-dominated industrial defects. This paper proposes rough path signature-guided geometry augmentation (RPS-GA), a geometry-aware approach in which Canny edge contours are treated as ordered planar paths whose truncated second-order signature responses, especially the antisymmetric Lévy-area term, are aggregated into a spatial map that highlights boundary-related structure through two fusion operators, SIG-AUG and SGAA. The approach is evaluated on NEU-DET and PCB-Defect under a few-shot protocol with 5, 10, 20, or 50 labeled images per class, using an unmodified YOLOv8n detector throughout. Compared with the baseline, RPS-GA delivers large gains when supervision is limited, although the margin shrinks as more labels become available. On NEU-DET, SIG-AUG raises 10-shot mAP@0.5 from 0.341 to 0.583, whereas on PCB-Defect, SGAA improves 10-shot mAP@0.5 from 0.086 to 0.299 and yields usable detection at 5-shot where the baseline fails entirely. These trends are confirmed by multi-seed evaluation across independent random partitions. Overall, the results indicate that second-order path-signature geometry offers a practical way to strengthen few-shot industrial defect detection without meta-learning or detector redesign.

---


### 81. [Proximity Features: Privacy-Compliant Cold-Start Personalization at Airbnb](https://arxiv.org/abs/2607.12246)

**<font color=#1a73e8>作者：</font>** Wei Jiang, Bin Xu, Hui Gao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalization in two-sided marketplaces relies heavily on user-level features, yet for platforms with infrequent, high-consideration purchases, a large fraction of users lack sufficient history for effective recommendation, spanning both paid and organic channels. At Airbnb, a substantial share of search requests comes from logged-out or first-time users, with this challenge especially pronounced on paid-channel landing pages, leaving traditional user-level features unavailable for a large fraction of traffic. Privacy regulations and increasing restrictions on third-party cookies further limit identifier-based tracking for non-essential use cases. This paper introduces Proximity Features, a privacy-compliant feature system that groups users by geographic proximity using geo-IP data and an adaptive clustering algorithm, producing aggregated user-level signals for groups of approximately 1,000 nearby users without requiring a persistent individual identifier at inference time. Privacy is preserved by design: the pipeline operates on consented, aggregated data only within consent-gated privacy controls.
The system is deployed in production at Airbnb, serving multiple surfaces including marketing landing pages and destination recommendation, with engagement emails integration under way. Online A/B experiments demonstrate statistically significant lifts in bookings, with the largest gains observed among users with absent or stale history.

---


### 82. [FinResearchBench II: A Deep Research Benchmark with Consensus-Derived Gold Rubrics for Distinguishing Financial Report Quality](https://arxiv.org/abs/2607.12252)

**<font color=#1a73e8>作者：</font>** Beidi Luan, Rui Sun, Sinuo Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep research agents are increasingly used to produce long-form financial reports, yet large-scale evaluation remains bottlenecked by the need for human experts to define and execute high-quality rubrics. We address this problem by proposing a scalable pipeline for generating high-quality rubrics without human experts in the final loop. We build a financial deep research benchmark from 104 real-world user queries and automatically synthesize 14,450 query-specific candidate rubrics from model-generated reports. To justify removing human experts from rubric execution, we compare rubric judgments from three human experts with those from a three-LLM judge panel on a sampled subset, and show that LLM-based evaluation is sufficiently consistent with human evaluation to replace it for large-scale rubric screening, including 98.67\% label-level agreement on jointly unanimous items. We then derive consensus-derived gold rubrics through two filters: a strict consistency filter, which keeps a rubric only if the three LLM judges unanimously agree on every report under the same query, and a distinguishability filter, which keeps a rubric only if it assigns at least one majority-yes and at least one majority-no label across the evaluated systems. This process retains 3,687 consistency-passed rubrics, of which 2,600 remain distinguishable and form the final set of consensus-derived gold rubrics. Using this final rubric set, we obtain clearly differentiated rankings across 10 deep research systems, with item-level pass rates ranging from 58.58\% to 22.23\%. More broadly, because the pipeline removes human-expert execution from rubric generation and evaluation, it is naturally scalable for benchmark evaluation, automatic system comparison, and future studies of evaluation-driven system improvement.

---


### 83. [How to Realize Recursively Self-Improving Agents and Personal Singularity: A Goal-, Scope-, Tool-, and Benchmark-Driven Multi-Agent Architecture](https://arxiv.org/abs/2607.12254)

**<font color=#1a73e8>作者：</font>** Chengshuai Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents can increasingly plan, use tools, maintain memory, and execute long-horizon tasks. These advances motivate two linked questions: how can an agent improve the mechanisms by which it learns and acts, and how can that improvement increase the durable capabilities of its user rather than only the software itself? This paper proposes a governed multi-agent architecture for recursively self-improving agents and introduces personal singularity as a bounded human-AI co-development objective: helping a user approach an expanding, user-defined capability frontier across selected domains. Each agent is defined by a goal contract, bounded scope, validated tool registry, tool-level tests, end-to-end benchmarks, an owner-controlled autonomy policy, a routing policy, memory, and an improvement policy. Out-of-scope tasks are transferred to another accountable agent or to a newly created niche agent. A user-facing Auto-Index selects interactive, hybrid, autonomous, or scheduled operation without overriding external permissions. The architecture combines a fast planner-executor-verifier loop, a slower evidence-gated improvement loop, an external governance plane, decentralized agent lineages, an owner-directed agent foundry, and a Personal Singularity OS coordinating working, computational-imaging, process-learning, and personal-learning agents. We formalize scope, routing, improvement acceptance, bounded goal evolution, tool-first execution, and human capability transfer, and provide safety invariants, benchmark design, and an implementation roadmap. This is a position and systems-design paper, not evidence that unrestricted recursive self-improvement or personal singularity has already been achieved.

---


### 84. [Understanding Structured Health Data through Interaction-Aware Mixture-of-Experts](https://arxiv.org/abs/2607.12255)

**<font color=#1a73e8>作者：</font>** Ji Hwan Park, Ying Ding, Tianjin Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study interaction-aware mixture-of-experts for post-stroke rigidity prediction using multi-level views of structured health records. Despite minimal performance gains, routing attribution reveals systematic importance differences across views, underscoring view construction as key to interpretability.

---


### 85. [Track, Rank, Crack: Epistemic Working Memory Scales Multi-Hop Reasoning in Language Agents](https://arxiv.org/abs/2607.12267)

**<font color=#1a73e8>作者：</font>** Ning Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language agents that interleave reasoning and tool use degrade sharply as reasoning chains lengthen, even when each individual step is easy. We trace this to context dilution: an agent's investigative state (what it has confirmed, what it suspects, and what it still needs) lives only implicitly in a growing context window, where early discoveries are buried under later retrievals. We introduce SLEUTH, which makes this state explicit and actionable through a structured epistemic working memory: the agent maintains Confirmed Facts grounded to sources, Active Hypotheses ranked by evidence, and Open Questions that directly drive its next action. Across five multi-hop benchmarks and five established baselines, SLEUTH's advantage grows with difficulty, from +5 points on HotpotQA to +11 on 4-hop chains, surpassing Reflexion without multiple episodes. Analyzing where the remaining gap lies, we identify the evidence sufficiency problem: agents often find the answer but fail to commit, exhausting their budget on needless verification. A lightweight commitment trigger fixes this, but only when the agent already maintains structured state: the identical trigger applied to an unstructured agent yields no improvement, isolating organized epistemic state as the necessary condition for effective commitment. Finally, enforcing protocol adherence on a weaker model recovers up to +19 points on the hardest problems, showing that how an agent organizes its reasoning, not raw model capability, is the active ingredient for scaling multi-hop reasoning.

---


### 86. [Quantum Port-Hamiltonian Neural Networks: Learning Conservative and Dissipative Dynamics via Measurement-Induced Nonlinearity](https://arxiv.org/abs/2607.12269)

**<font color=#1a73e8>作者：</font>** Dibakar Sigdel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Quantum Port-Hamiltonian Neural Networks (Q-pHNNs), a family of parameterised quantum circuits that learn classical dynamics in a structure-preserving manner. The framework relies on the Isomorphic Hamiltonian Mapping (IHM): the skew-symmetric interconnection matrix $\mathbf{J}$ corresponds to unitary gate evolution, and the positive-semidefinite dissipation matrix $\mathbf{R}$ corresponds to Measurement-Induced NonLinearity (MINL) realised via mid-circuit measurement and classical feedforward. This ensures conservation and passivity are enforced by construction rather than penalty terms. We instantiate the IHM in four architectures: (1) a Quantum HNN that learns conservative energy manifolds and extracts Hamilton's equations exactly via the Parameter-Shift Rule; (2) a Q-pHNN using Born-rule measurement for dissipation; (3) a Q-pHNN jointly learning the energy ansatz and damping coefficient; and (4) a topology-entangled Quantum Graph Neural Network for $N$-node coupled-phasor networks. Experiments on the nonlinear pendulum and damped harmonic oscillator demonstrate: (i)~$1.35\%$ relative energy drift with a symplectic integrator and scale correction; (ii)~$100\%$ energy monotonicity for the MINL circuit; and (iii)~$12.1\%$ error in damping-coefficient identification from vector-field snapshots with no direct supervision on the damping coefficient.

---


### 87. [A hybrid analytical-PINN model for subsurface simulation of geothermal heat exchangers in heterogeneous underground](https://arxiv.org/abs/2607.12271)

**<font color=#1a73e8>作者：</font>** Moke Rao, Thomas Hamacher, Smajil Halilovic  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, a parametric physics-informed neural network for solving the heterogeneous soil thermal problem with borehole heat exchangers (BHEs) as singular sources is developed. There are three novel features in the present framework; namely, (i) the singularity is naturally removed by using analytical line source models; (ii) using the explicit formulation for gradient thermal conductivity enables physics-informed learning of the parametrization featuring the conductivity; (iii) the learned correction is utilized as an efficient universal corrector via superposition principles. We first introduce the decomposition of the temperature change and transform the approximation of the entire heterogeneous response to the correction compensating the difference between the practical solution and idealized homogeneous approximation. In such a way, the delta function singularity is excluded and the bulk heat transfer is captured for the sake of facilitating the effective training of the neural network. The original problem is then reformulated as a governing correction diffusion or advection-diffusion equation subject to a homogeneous initial condition. The linearly varying thermal conductivity is used to model the soil heterogeneity. We propose a physics-informed neural network to approximate a universal corrector with respect to a single borehole with unit heat extraction rate. As a result, the network is trained by minimizing the physics-informed and data-anchored loss function that is evaluated for sampled conductivity parameters on adaptively selected training points. In addition, we include the location indicator function regarding the source as a feature input of network and find that it helps the network to process the local information. We perform numerical tests to exhibit the effectiveness of the proposed method based on three different analytical models.

---


### 88. [GeoSEAN: Explainable Country-Level Image Geolocation for ASEAN Regions](https://arxiv.org/abs/2607.12284)

**<font color=#1a73e8>作者：</font>** Muhamad Syukron, Danish Rafie Ekaputra, Tintrim Dwi Ary Widhianingsih  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image geolocation aims to infer the geographic origin of an image from visual content alone. However, this task remains challenging in regions where countries share similar urban, roadside, architectural, and environmental characteristics. Many existing geolocation models focus on coordinate level prediction or classification performance while providing limited insight into how visual evidence contributes to location predictions. This study presents an explainable country level image geolocation pipeline for 11 ASEAN countries. First, we collected 4,850 images from GeoGuessr style sources, Google Images, and additional street level imagery. We then evaluated three approaches on this dataset: CLIP zero shot classification, a LightGBM classifier, and an MLP classifier. The MLP achieved the best test performance, attaining an accuracy and F1 score of 85.91%. For explainability, predictions generated by the MLP classifier were analyzed post hoc using CLIP attention rollout, YOLO26 object detection on the original images, and Energy Based Pointing Game (EBPG) overlap metrics. Object level analysis indicates that frequently detected objects are not necessarily associated with the highest attention density, suggesting that object frequency and attention based visual evidence capture different aspects of a scene. These results demonstrate that the proposed model can support accurate regional image geolocation while enabling object level inspection of the visual cues underlying its predictions.

---


### 89. [$\mathrm{P}^{3}$CDA: Privacy-Preserving and Provably Secure Cross Domain Authentication Scheme for Internet of Drones](https://arxiv.org/abs/2607.12288)

**<font color=#1a73e8>作者：</font>** Chengqi Hou, Beibei Li, Ziqing Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the rapid expansion of the Internet of Drones (IoD) and the increasing mobility of drones, cross-domain interactions among geographically distributed domains have become inevitable. Cross-domain authentication is therefore a fundamental security requirement for IoD. However, existing authentication schemes often struggle to simultaneously achieve strong security, high efficiency, and identity privacy, making them unsuitable for the stringent requirements of highly dynamic and resource-constrained IoD environments. To address this challenge, we propose $\mathrm{P}^{3}$CDA, a privacy-preserving and provably secure cross-domain authentication scheme. First, we design an efficient pseudonym management mechanism that supports adaptive pseudonym generation as well as batch registration, verification, and revocation. Second, we propose a structurally enhanced Merkle Hash Tree (MHT) that supports batch pseudonym updates, thereby reducing the pseudonym storage overhead of drones. Building on these components, we develop a cryptographic accumulator-based cross-domain authentication protocol that enables anonymous authentication with authorized pseudonyms while preserving the traceability and efficient revocation of malicious drones. We rigorously analyze the security of $\mathrm{P}^{3}$CDA and formally prove its security under the Canetti--Krawczyk (CK) adversary model. Extensive experiments demonstrate that $\mathrm{P}^{3}$CDA achieves lower computational, communication, and storage overhead than state-of-the-art schemes.

---


### 90. [Semantic-Edge Response Decoding of SAM3 for Zero-Shot Crack Segmentation](https://arxiv.org/abs/2607.12292)

**<font color=#1a73e8>作者：</font>** Shipeng Liu, Zhanping Song, Liang Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Crack segmentation is essential for infrastructure inspection and structural health assessment, but existing high-performance methods typically require task-specific pixel-level annotations and training. Text-promptable vision foundation models enable zero-shot deployment, yet their final mask proposals are poorly suited to thin, fragmented, and low-contrast cracks, whose evidence may be suppressed, truncated, or over-expanded during mask generation. We find that language-conditioned semantic responses within the SAM3 decoder preserve more continuous and complete crack evidence than its final masks. Based on this observation, we propose Semantic-Edge Response Decoding (SERD), which interprets internal responses as a dense crack-likelihood field, calibrates them with a lightweight edge prior, and generates crack masks using a unified global threshold, without annotation or fine-tuning. Experiments on six public datasets show that SERD consistently improves over native SAM3 and outperforms the compared zero-shot and open-vocabulary segmentation methods, achieving an average Crack IoU of 61.14\%, 4.63 points higher than SAM3. Further analyses show that most gains arise from directly decoding internal semantic responses, while edge calibration improves structural recovery and false-positive control without increasing end-to-end inference overhead. These results suggest that, for thin and non-compact targets, internal continuous responses can provide a more transferable interface than the final masks of foundation models. Code is available at: this https URL

---


### 91. [Adaptive Cross-Modal Fusion with Sparse Attention for Pedestrian Crossing Intention Prediction](https://arxiv.org/abs/2607.12293)

**<font color=#1a73e8>作者：</font>** Md Mahfuzur Rahman, Pengzhan Zhou, A F M Abdun Noor 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting pedestrian crossing intention is a safety-critical task for autonomous driving, yet existing approaches often rely on single-modal inputs or dense multimodal fusion strategies that inadequately capture complementary visual and kinematic information while introducing redundant inter-modal interactions. We propose ADAPT (Adaptive Domain-Aware Pedestrian Crossing Transformer), a multimodal framework that jointly models local and global visual context together with temporal motion dynamics for accurate pedestrian crossing intention prediction. ADAPT processes four spatially aligned visual modalities, including RGB images, local depth maps, global semantic maps, and global depth maps, together with ego-vehicle speed, pedestrian bounding boxes, and skeleton pose information through five specialized modules: a weight-shared Swin Transformer V2 backbone for visual feature extraction, a Cross-Modality Guided Attention module for hierarchical visual fusion, a Mamba-based Motion Feature Encoding module for efficient temporal modeling, a Sparse Cross-Modal Attention module that selectively preserves the most informative inter-modal interactions, and a Vision Transformer-based Temporal Feature Fusion module for sequence-level prediction. Extensive experiments on the JAAD and PIE benchmark datasets demonstrate that ADAPT consistently outperforms existing state-of-the-art methods while maintaining low computational complexity. On JAAD, the proposed method achieves an AUC of 0.73 on JAADbeh and 0.85 on JAADall, while on PIE it achieves an accuracy of 0.92 and an AUC of 0.90. Furthermore, ADAPT performs inference in only 17.23 ms per sample, offering an effective balance between predictive accuracy and real-time deployment efficiency for intelligent transportation and autonomous driving applications.

---


### 92. [MobileSAM2: Lightweight Segment Anything for Spatial Intelligence](https://arxiv.org/abs/2607.12297)

**<font color=#1a73e8>作者：</font>** Kai Jiang, Jiaxing Huang, Jingyi Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The recent large video foundation model, SAM2, enables segment anything in both images and videos, serving as a powerful base model for various applications. However, many of such use cases require to operate on resource-constrained devices like mobile phones and laptops. In this work, we aim to make SAM2 more mobile-friendly by distilling the heavyweight SAM2 into a lightweight model, facilitating segment anything in both images and videos on mobile devices. To this end, we propose Hypergraphical Knowledge Distill (HyperKD), which introduces the idea of hypergraph into knowledge distillation, aiming to effectively model and transfer SAM2's generalizable and comprehensive knowledge. HyperKD consists of Temporal HyperKD and Granularity HyperKD that construct hypergraphs to explicitly model and extract the generalizable temporal knowledge and the comprehensive multi-granularity knowledge from SAM2 respectively, which are then distilled into the lightweight student model by aligning it with the constructed hypergraphs. Besides, we present MobileSAM2, a new family of lightweight SAM2 that balances efficiency and effectiveness via searching the best model architectures with HyperKD during model size reduction. Extensive experiments validate MobileSAM2 across multiple benchmarks and show promising generalization performance on embodied AI tasks.

---


### 93. [What Does a Temporal Benchmark Score Measure? Decomposing Channel Use in Video VLM Evaluation](https://arxiv.org/abs/2607.12304)

**<font color=#1a73e8>作者：</font>** Farrukh Rahman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A score on a temporal video question answering benchmark is meant to measure that a model has temporal understanding, but it conflates two questions. 1. The task question: is the question even temporal, does it need several frames and their order? and 2. The channel question, when it does, does the model recover the order from the pixels, or read it off the positional encoding (RoPE)? Most of a temporal score answers neither, a single frame and answer priors often carry it. The field's validity checks, frame-shuffle sensitivity and the accuracy gained from the full video, speak only to the task question. We contribute a label-free screen for the channel question, the reversal-drop: the accuracy lost when the visual sequence is reversed while RoPE remains forward. It can be applied to compatible temporal benchmarks without new annotations. Paired reverse labels, or tasks whose labels transform deterministically under reversal, distinguish models that follow reversed content from those merely disrupted by the conflict. Molmo2 answers the forward event reading order off positions, while Qwen3-VL answers the reversed event it actually sees, reading visual order (comparatively). We call them position-dominant and visual-sequence-dominant. The split holds across two benchmarks and several temporal tasks at two scales, and activation patching shows it is a real internal property, not an artifact of the conflict. The distinction matters, the two channels fail on opposite inputs so two models with similar score are not interchangable, i.e. an aggregate score does not reflect potential failure modes.

---


### 94. [Antiproof: Synthesizing Vulnerability Detectors and Proofs of Exploitability](https://arxiv.org/abs/2607.12316)

**<font color=#1a73e8>作者：</font>** Alon Shakevsky, Corban Villa, Ion Stoica 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Discovering vulnerabilities before attackers exploit them requires high recall and reliable automatic validation, but existing approaches struggle to achieve both without prohibitive cost. We present Antiproof, an end-to-end vulnerability discovery system that combines neuro-symbolic detector synthesis for high-recall discovery with proof-of-exploitability oracles for automatic validation. Antiproof learns and iteratively refines static detectors from vulnerability datasets, then validates candidates by verifying whether executable proofs demonstrate concrete attacker capabilities. Evaluated on BountyBench and our curated KEVBench dataset, Antiproof detects 64 of 66 vulnerabilities, improving recall by more than 60 percentage points over static-analysis and neuro-symbolic baselines. In a scan of 50 widely deployed systems, Antiproof uncovered several hundred previously unknown vulnerabilities. We are responsibly disclosing all confirmed zero-days and have received 12 CVE assignments to date, including remote code execution vulnerabilities in Ray, SGLang, vLLM, and LiteLLM that could allow attackers to take over LLM training and inference systems.

---


### 95. [Real-time Generation of Listener Nodding via Prediction of Kinematic Parameters for Avatar Dialogue Systems](https://arxiv.org/abs/2607.12329)

**<font color=#1a73e8>作者：</font>** Kazushi Kato, Koji Inoue, Taiga Mori 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In human dialogue, we achieve smooth communication by expressing nonverbal cues such as eye contact, nodding, and facial expressions with precise timing. It is expected for conversational avatars to express these cues appropriately to realize natural and human-like interactions. This study focuses on nodding, which is crucial for demonstrating active listening and encouraging further user utterances. We propose a model that predicts both timing and kinematic parameters representing the motion features of listener nodding in real time. The proposed model consists of a timing prediction module and a kinematic parameter prediction module. Each implements a dyadic attention network over the speaker and listener channels based on the technique of Voice Activity Projection (VAP). Unlike conventional models, this approach enables real-time prediction of kinematic parameters based on the specific context of the dialogue rather than just predicting the timing. Furthermore, we demonstrate the effectiveness of fine-tuning the kinematic parameter prediction module initialized from the trained timing prediction module. The proposed model is lightweight and capable of real-time operation, and it has been integrated into an avatar dialogue system. Subjective evaluation experiments shows that our proposed method significantly outperforms both a baseline with stochastic timing and another with fixed-motion nodding. The code and trained models are available at this https URL.

---


### 96. [Gradient Flow Dynamics and Implicit Bias of Diagonal Linear Networks under Infinitesimal Initialization](https://arxiv.org/abs/2607.12332)

**<font color=#1a73e8>作者：</font>** Jiajie Zhao, Jianxing Wang, Junjie Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the gradient flow dynamics of diagonal linear networks for regression tasks under infinitesimal initialization. Extending Theorem 1 from Pesme & Flammarion (2023), we generalize the analysis to both deep diagonal linear networks and a broader class of two-layer diagonal linear networks (as defined in Definition 4.1). Specifically, we demonstrate that the training trajectories of these models can be equivalently characterized by the proposed Algorithm 1. We further prove that this algorithm converges to the solution of a modified $ \mathcal{l}_1 $ norm minimization problem. As a result, we establish that the implicit bias of both network architectures corresponds to a modified $ \mathcal{l}_1 $ norm in the regime of infinitesimal initialization. Additionally, we provide insights into the underlying mechanisms governing these dynamics by identifying the Structural Invariant Manifold (SIM) (Zhao et al., 2026) as the key geometric structure that shapes the learning process.

---


### 97. [QUBO-Optimized Evidence Selection for Retrieval-Augmented Question Answering with Unconventional Solvers](https://arxiv.org/abs/2607.12334)

**<font color=#1a73e8>作者：</font>** Rahul Singh, Madhav Vadlamani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented question answering depends on selecting evidence passages that jointly support answer generation. However, many RAG pipelines rely on top-\(k\) ranking, where passages are selected mainly by individual relevance scores, even though multi-hop questions often require complementary evidence satisfying multiple information requirements. Recent LLM-based selectors address this by treating retrieval as set selection, but using an LLM for this intermediate stage can be costly and difficult to scale. In this work, we formulate evidence selection as a Quadratic Unconstrained Binary Optimization (QUBO) problem. Given a question, candidate passages, and decomposed information requirements, our method constructs an energy function that balances relevance, requirement coverage, support strength, redundancy, complementarity, and compactness. Low-energy solutions correspond to compact evidence subsets that cover the needed requirements while avoiding unnecessary or repetitive context. The selected passages are then passed to a downstream language model for answer generation, separating combinatorial evidence selection from semantic answer generation. We evaluate the proposed QUBO selector on HotpotQA and compare it with LLM-based set selectors and non-LLM baselines including BM25, relevance top-\(k\), maximal marginal relevance, hybrid lexical--semantic ranking, greedy coverage, and random selection. The QUBO selector achieves competitive exact-match and token-F1 performance relative to LLM-based selectors while providing a solver-compatible formulation for structured evidence selection. These results suggest that multi-hop evidence selection can be cast as discrete optimization, opening a path toward RAG pipelines where LLMs are reserved for semantic processing and answer generation, while context selection is handled by Ising/QUBO-compatible solvers.

---


### 98. [ProtoPointNet: Prototype-Based Interpretable Classification of 3D Dental Point Clouds with Verifiable Spatial Activations](https://arxiv.org/abs/2607.12335)

**<font color=#1a73e8>作者：</font>** George V. Jose, Thao Liang Chiam, Toby Hughes 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prototype-based networks provide inherently interpretable classification by linking predictions to learned exemplars, but their use in 3D point clouds and clinical surface-pair reasoning remains limited. We introduce ProtoPointNet, a prototype-based model for dental occlusion classification from registered upper--lower intraoral arch pairs. Each point is encoded by a 14-dimensional descriptor combining local surface geometry, curvature, and explicit inter-arch displacement and clearance, exposing occlusal relationships to prototype matching. A shared multi-task point-cloud backbone learns axis-specific prototype heads for sagittal-left, sagittal-right, vertical, transverse, and midline classification. To support limited clinical data, we train prototypes from scratch using auxiliary supervision and encoder-freeze hand-off. On Bits2Bites, ProtoPointNet achieves mean test macro-F1 of 0.724 and AUROC of 0.825, with strongest performance on vertical (F1 0.828) and sagittal-left classification (F1 0.807). Projected prototype activations localise to anatomically plausible regions, including posterior molars and premolars for cross-bite evidence and anterior incisors for bite-depth evidence. These results support prototype-based reasoning as a transparent, spatially grounded alternative to black-box 3D classifiers for dental surface-pair analysis.

---


### 99. [Policy-Conditioned Constrained Decoding for Column-Level Access Control in Text-to-SQL](https://arxiv.org/abs/2607.12341)

**<font color=#1a73e8>作者：</font>** Ryoto Miyamoto, Xin Fan, Hayato Yamana  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL is increasingly deployed across trust boundaries between data providers and users. Such deployment must balance three competing requirements: policy compliance, answer coverage, and bounded cost. Existing approaches typically decide refusal based on which columns a query mentions and enforce it stochastically. Whether a query is compliant, however, depends not only on which columns appear but on how they are used, and stochastic enforcement cannot deterministically rule out violations. We formalize this requirement as a column-use policy over semantic use: output, filter condition, and aggregation argument. We integrate the policy by aligning each role with grammar productions tracked by the decoder. The resulting system, PCC-SQL, applies a per-token logits mask that deterministically eliminates single-query column-use violations on the supported SQL fragment in a single decoding pass. Across three benchmarks and three open-source models, PCC-SQL achieves 0% Leakage Rate and Coverage up to 88.7% on Spider-CU, while staying within +10% tokens of direct prompting. We additionally assess semantic alignment with execution accuracy.

---


### 100. [Generating Developable 3D Molecules via Pocket-Conditioned Diffusion and Property-Aware Optimization](https://arxiv.org/abs/2607.12349)

**<font color=#1a73e8>作者：</font>** Ruoxi Gao, Jiangweizhi Peng, Ziqi Chen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drug discovery and development is time-consuming and resource-intensive, motivating computational approaches such as diffusion models for de novo drug design. Many such models follow the structure-based drug design (SBDD) paradigm, generating molecules to fit a target binding pocket. However, existing diffusion-based SBDD methods typically couple pocket and ligand representation learning, model interactions only at the atom level, and prioritize binding affinity over other developability properties. Here, we introduce conDitar-dev, a conditional diffusion-based SBDD framework for generating ligands with strong binding affinities and favorable ADMET properties. It consists of three modules: msPRL, a pretrained multi-scale pocket representation learning module; conDitar, a pocket-conditioned diffusion model guided by msPRL representations; and paOPT, a generation-time method for optimizing ligand developability. On a newly curated benchmark of human disease targets, conDitar outperforms state-of-the-art SBDD baselines, achieving an average binding score of -8.85 kcal/mol. Across five ADMET properties, conDitar-dev improves performance by up to 73% over conDitar. To further validate the abilities of conDitar-dev to generate developable molecules, we have applied it to two validated druggable targets: programmed death-ligand 1 (PD-L1) and colony-stimulating factor 1 receptor (CSF1R) proteins. Top-ranked generatively designed molecules and their analogs have been experimentally synthesized and biologically tested. Two molecules generated directly by conDitar-dev for PD-L1 exhibited SPR-derived $K_D$ values of 3.49 and 3.75 $\mu$M, respectively. Hit expansion based on conDitar-dev-designed molecules identified selective CSF1R inhibitors with IC$_{50}$ values as low as 200 nM, while also uncovering opportunities for drug repositioning.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-203](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
