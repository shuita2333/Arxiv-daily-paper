# 📦 其他研究 | 2026年10月20日

> 本类共 **213** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-213**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-213**

---

### 201. [DrugHarness: An Evolvable Agent Harness for Computational Drug Discovery](https://arxiv.org/abs/2610.23791)

**<font color=#1a73e8>作者：</font>** Yuxing Chen, Zhisheng Zhang, Cheng Tang 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computational drug discovery requires agents to compose scientific operations and adapt to changing evidence and constraints. Here we introduce DrugHarness, an evolvable agent harness coupling composable scientific execution with conditional skill induction. Its environment integrates over 80 scientific operations, biomedical resources and task-specific code, preserving associations among candidates, results and artifacts. From execution trajectories and outcome feedback, DrugHarness induces action hypotheses with observable applicability conditions, recommended actions and supporting evidence. An independent review agent evaluates candidate skills derived from these hypotheses through source verification and, when needed, targeted execution trials. Admitted skills guide subsequent tasks and are revised through feedback. Evaluation on MolBench and SMDD-Bench demonstrates capabilities in molecular screening, optimization and constrained design. Without evolution, DrugHarness exceeds reported MolClaw-CC results by 10.8 percentage points in affinity-comparison accuracy and 55% in mean top-three active hits on MolBench. Retrospective evaluation on skill-development tasks shows that evolution increases Qwen's affinity-comparison accuracy from 62.2% to 81.1% and optimization success from 79.5% to 87.2%. In a prospective HPK1 study, DrugHarness achieves a more favorable median docking score than Biomni among system-specific candidates. A synthesized compound achieves a cellular IC50 of 14.19 nM, a 2.64-fold potency improvement over the best input reference, with activity competitive with two selected compounds designed by experienced medicinal chemists. These results support conditional skill evolution for scientific agents and demonstrate a workflow connecting computational drug design with experimental validation.

---


### 202. [Persistent Planar Memory for Video World Models](https://arxiv.org/abs/2610.23795)

**<font color=#1a73e8>作者：</font>** Yuze He, Bin Tan, Zelin Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models that generate and explore environments at scale need a persistent 3D memory of what they have produced. Plane primitives offer a natural candidate: a compact set of oriented planes captures the dominant structural elements (e.g., walls, floors, facades) of indoor and outdoor scenes, while requiring only 7 parameters per primitive. We present PPMem, a video world model that adopts plane primitives as its persistent 3D memory. PPMem augments a video diffusion transformer with a planar prediction head and a Depth Token Fusion (DTF) module: each autoregressive chunk jointly produces RGB video and planar geometry, which merges into a persistent plane memory that conditions subsequent chunks via rendered depth. The resulting memory is three orders of magnitude more compact than per-pixel point clouds (~100K primitives, 5MB for a full scene), geometrically explicit (metric depth, normals, exportable surfaces), cross-view consistent (jointly predicted by the shared backbone), and adaptive (refined by the merging procedure as generation proceeds). On DL3DV and RealEstate10K, PPMem outperforms prior 3D-grounded world models in video quality while jointly producing metric-scale depth, surface normals, and exportable planar geometry, sustaining coherence across hundreds of frames under large viewpoint changes. Project page: this https URL.

---


### 203. [Beyond SAEs: Consistent Concept Discovery with Sparse Coding](https://arxiv.org/abs/2610.23801)

**<font color=#1a73e8>作者：</font>** Jinho Choi, Hyesu Lim, Jaegul Choo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) explain foundation model representations by decomposing activations into sparse combinations of learned dictionary atoms. However, the learned dictionaries can vary across training runs, limiting the reliability and reproducibility of SAE-based analyses. We propose Consistent Sparse Dictionary Learning (ConSDL), which replaces the standard linear encoder with per-sample sparse coding. This is motivated by our synthetic analysis showing that coefficients from a single linear encoder pass are suboptimal compared with those obtained by per-sample optimization, suggesting that sparse coding is a reliable mechanism for dictionary learning. Across 16 synthetic settings, ConSDL achieves near-perfect dictionary and coefficient recovery. These gains translate to state-of-the-art cross-seed consistency across four vision and language settings, where ConSDL improves dictionary and coefficient consistency by 17.6% and 35.9%, respectively, over the average of six SAE baselines.

---


### 204. [Explainable Machine Learning Analysis of Temperature Effects on Mechanical Strength of Fiber-Reinforced High-Performance Concrete](https://arxiv.org/abs/2610.23811)

**<font color=#1a73e8>作者：</font>** Jagaran Chakma, Zhiguang Zhou, Badhan Chakma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting the compressive strength of fiber-reinforced high-performance concrete subjected to temperature exposure is challenging because to the intricate interdependencies of mixture composition, fiber properties, curing conditions, and temperature. A data-driven framework to predict compressive strength utilizing 1,204 experimental records containing a diverse array of material designs and exposure situations. This study evaluates eight machine-learning models and demonstrate that ensemble approaches routinely surpass individual learners. Both gradient boosting and extreme gradient boosting exhibit superior performance on unseen data, each attaining a R^2 of 0.903. Gradient boosting produces the minimal root mean square error (6.67 MPa), whereas extreme gradient boosting achieves the lowest mean absolute error (3.97 MPa) and mean absolute percentage error (10.60%). The models are further interpreted utilizing Shapley additive explanations and partial dependence analysis, which reveal temperature as the primary factor influencing compressive strength, succeeded by fine aggregate, superplasticizer, cement content, water-to-binder ratio, and water content. Strength diminishes significantly with rising temperature, albeit the extent of deterioration is contingent upon the specific combination design. The best performing models are subsequently implemented in a Python-based graphical user interface for expedited prediction. Our findings offer a precise and comprehensible methodology for evaluating temperature-dependent compressive strength and facilitate the practical, data-driven design of fiber-reinforced high-performance concrete.

---


### 205. [Acceptance Is Not Speed: Length Inflation in Training-Free Lossy Speculative Decoding](https://arxiv.org/abs/2610.23818)

**<font color=#1a73e8>作者：</font>** Chiatzen Wang, Bill Xu, Haochen Gu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding typically characterizes speedup by draft tokens accepted per verification round. Lossless verification preserves the target model's output distribution and thus expected completion length, making this metric a meaningful efficiency proxy. Relaxed (lossy) verification accepts tokens that lossless verification would reject, potentially altering that distribution. We identify a length inflation phenomenon: relaxed verification lengthens completions, primarily by extending reasoning traces, largely offsetting apparent gains in accepted tokens per round. We evaluate existing training-free relaxed verification rules on twelve target-drafter pairs against lossless verification on identical prompts, measuring completion length, verifier rounds, wall-clock time, and task accuracy. At each rule's most relaxed evaluated setting, relaxed verification on average accepts $1.34\times$ as many tokens per round but produces $1.54\times$ longer completions. For rules with higher acceptance lengths, tokens accepted only under relaxed verification tend to have low target-model probability, contributing to length inflation. For rules that reduce verifier rounds, accuracy typically drops substantially. Further analysis traces some failures to continued reasoning that exhausts the budget needed to deliver a final answer. Overall, accepted tokens per round alone is an unreliable measure of decoding speed under relaxed verification. Completion length and verifier rounds must also be reported to assess actual efficiency.

---


### 206. [CocoRNA: Collective RNA Design with Cooperative Multi-agent Reinforcement Learning](https://arxiv.org/abs/2610.23820)

**<font color=#1a73e8>作者：</font>** Tianmeng Hu, Biao Luo, Ke Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing RNA sequences that reliably fold into specific secondary structures is essential for understanding their biological functions but remains a challenging computational problem. We propose CocoRNA, a cooperative multi-agent reinforcement learning framework for RNA inverse design. CocoRNA simplifies the design task by decomposing it into smaller sub-problems, each solved collaboratively by multiple agents. This approach reduces the complexity of the problem and improves the exploration of design policies. During training, a centralized critic uses global structural information to guide the agents, enabling them to jointly optimize their design strategies. As a result, CocoRNA learns high-quality RNA design policies that generalize effectively to unseen structures without additional training. Experiments on the Rfam dataset demonstrate that CocoRNA substantially outperforms state-of-the-art methods in both success rate and design speed. Further experiments on other biological sequence design tasks highlight the effectiveness and broad potential of CocoRNA for complex design tasks.

---


### 207. [Self-Building Labs](https://arxiv.org/abs/2610.23826)

**<font color=#1a73e8>作者：</font>** Jiaru Bai, Yuchi Zhao, Han Hao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-driving laboratories (SDLs) accelerate scientific discovery by automating experimental execution and optimization. AI agents can increasingly propose new experiments, but existing SDLs can only run the procedures they were built for. Adapting them to a new experiment still takes extensive manual engineering, which makes laboratory flexibility the bottleneck for scaling discovery. We introduce the self-building laboratory (SBL), which designs, configures, and operates its own laboratory setup given a high-level scientific goal. SBL starts from whatever already exists, from an empty room to a working SDL, and builds the missing capabilities: the lab layout, its digital twin, robot skills, and experimental workflows. We demonstrate the system working across different robots and setups, scaling from a single workstation to laboratories with several robots working together. We validate SBL's end-to-end capabilities through a real-world quantum-dot synthesis experiment. By shifting the role of human researchers from manually configuring and programming device automation to specifying scientific objectives, SBL makes scientific automation more accessible, flexible, and scalable. Project website: this https URL

---


### 208. [Waiting Buys Exactly Two Moments: Endogenous Identification in Prediction-Driven Allocation](https://arxiv.org/abs/2610.23830)

**<font color=#1a73e8>作者：</font>** Rama AlHamidi, Rasul Khanbayov, Erchin Serpedin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A planner with a fixed budget of preventive help must decide whom to help and when. Waiting reveals risk but removes intervention opportunities as higher-risk individuals leave first. We characterize this tradeoff under repeated noisy signals and risk-dependent attrition: in the canonical model, a length-$\tau$ observation prefix identifies exactly the latent risk moments $m_j=\mathbb E[p^j]$ for $j=0,\ldots,2\tau-1$, buying two new moments per additional period. These identify average next-period attrition among survivors but need not identify allocation welfare or attrition among those prioritized for treatment. Our observationally equivalent constructions establish unavoidable timing regret at any sample size for a fixed observation length, while exact certificates determine whether all compatible populations share a unique optimal date. Matched experiments separate the effects of estimation, bootstrap averaging, and regret weighting. Longer observation often resolves timing ambiguity, but the optimal date may already have passed. In our experiments, bootstrap averaging and early stopping improve decisions, while regret weighting adds no improvement in pooled mean squared regret: better statistical fit need not yield better allocation welfare. The code and artifacts are available at this https URL.

---


### 209. [Beyond the Answer: Student-Conditioned Trace Construction for Reasoning Distillation](https://arxiv.org/abs/2610.23831)

**<font color=#1a73e8>作者：</font>** Shaoang Li, Yanhang Shi, Yufei Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A reasoning trace can accompany a correct answer without providing effective supervision for a particular student. We study how to construct traces that improve learning beyond answer-only supervision by considering both their intermediate content and their accessibility to the target learner. We introduce ReDiST, a student-conditioned trace-construction and distillation framework for evidence-rich reasoning. Starting from the student's own attempts, ReDiST revises answer-correct drafts against the supplied evidence and repairs unsuccessful drafts with additional guidance from the verified answer. A frozen student-matched reader screens and ranks original and edited candidates using answer recovery and verified-answer probability, given the question, evidence, and candidate trace. We distill the selected targets while balancing trace and final-answer supervision with an auxiliary answer loss. Construction and selection occur offline, and inference uses only the distilled student. Experiments on question-answering benchmarks show that ReDiST can improve both source-task and cross-benchmark performance over answer-only, original-trace, and the evaluated trace-selection and rewriting baselines. Across supervision recipes, performance rankings can differ between source and transfer benchmarks, highlighting the importance of evaluating trace teaching utility across distributions.

---


### 210. [Sensory Comfort Across Multisensory XR Prototypes for Autistic Adults](https://arxiv.org/abs/2610.23833)

**<font color=#1a73e8>作者：</font>** Yibo Meng, Xiujun Chen, Bingyi Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Multisensory XR may support informal learning for autistic adults, but sensory-friendly design often emphasizes reducing input. We conducted a mixed-methods, counterbalanced within-subjects study with 20 Chinese autistic adults who evaluated five complete XR configurations presenting the same popular-science content. Comfort differed substantially across the configurations (Friedman chi-square(4) = 46.39, p < .001, Kendall's W = .58). L3 received the lowest mean rating (2.97/5) and was tied for lowest for 16/20 participants, whereas L5 received the highest mean rating (4.43/5) and was tied for highest for 17/20. Participants described the static configurations in terms of clarity and self-pacing, L3 in terms of abruptness, simultaneous demands, insufficient warning, and limited disengagement, and L4/L5 in terms of gradual transitions, opportunities to disengage, and coordinated narrative cues. The study provides a configuration-level account of sensory comfort and identifies participant-described qualities that can inform future controlled studies of multisensory XR.

---


### 211. [Bad Diagnosis: Analyzing Consent and Data Collection Practices of Mobile Medical Apps](https://arxiv.org/abs/2610.23851)

**<font color=#1a73e8>作者：</font>** Ethan Myers, Lorenzo De Carli, Shantanu Sharma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mobile health (mHealth) apps collect personally-identifiable information while handling uniquely sensitive medical data, ranging from mental health records to real-time glucose or heart rate monitoring -- yet they remain poorly understood at scale. We present the first comprehensive analysis of consent and data collection practices across 10,000+ mHealth apps on the Google Play Store, combining static analysis and privacy policy examination. We develop a rigorous operational definition to distinguish health apps from general wellness programs, and design a measurement framework to detect misuse of permissions and violations of consent. Our analyses reveal a troubling ecosystem: 69.15% of apps request at least one permission unrelated to their stated purpose, with over 52.9% apps requesting location data, and 50.5% and 34.9% apps requesting camera and microphone access, respectively -- despite no functional justification based on app descriptions and stated purposes. Most alarmingly, nearly 93% of apps fail to provide users with a consent form, directly violating regulatory requirements such as GDPR; and even among the remaining 7%, 1 in 14 demonstrate a gap between the obtained consent and collection of personally identifiable information. These findings demonstrate an urgent need for stronger enforcement of privacy regulations in mHealth apps. We plan to release our dataset and measurement tools for continued monitoring of this critical space.

---


### 212. [Rethinking the design space of Vanilla Pixel Diffusion Transformers](https://arxiv.org/abs/2610.23854)

**<font color=#1a73e8>作者：</font>** Soumik Mukhopadhyay, Long Mai, Abhinav Shrivastava 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-space diffusion models have recently re-emerged as a compelling alternative to latent diffusion, avoiding the lossy latent bottleneck and separately trained autoencoder. JiT shows that a vanilla diffusion transformer can generate directly in pixel space by replacing the commonly used velocity prediction ($\boldsymbol{u}$-prediction) with clean image prediction ($\boldsymbol{x_0}$-prediction). In this work, we revisit this choice and introduce MFlow, an adaptive parameterization that learns to interpolate between $\boldsymbol{x_0}$- and $\boldsymbol{u}$-prediction across principal directions of the data, learned end-to-end with diffusion training. We find that the preferred parameterization varies systematically with the data representation and model capacity -- notably, increasing model capacity shifts preference toward velocity prediction. We evaluate MFlow across ImageNet, UCF-101 video, and large-scale text-to-image generation, demonstrating competitive or improved generative performance across diverse settings. In addition, we find that vanilla pixel diffusion transformers, irrespective of parameterization, retain a persistent high-frequency deficit relative to real images. To address this, we introduce ConvRefiner, a lightweight convolutional module trained post-hoc with an adversarial loss while keeping the diffusion backbone frozen. With only a small amount of additional training, ConvRefiner restores the high-frequency statistics of generated images while preserving FID. Project webpage: this https URL.

---


### 213. [Learning to Correct Geometry in Generated Videos](https://arxiv.org/abs/2610.23856)

**<font color=#1a73e8>作者：</font>** Weijie Lyu, Tiancheng Shen, Jason Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generated videos often lose geometric consistency under camera motion: structures warp under viewpoint change, parallax becomes inconsistent, and smooth camera movement may collapse into shot-like transitions. We argue that this failure is largely a data problem. In web-scale video corpora, most visible motion comes from dynamic objects captured by static or weakly moving cameras, leaving only sparse supervision for viewpoint-induced appearance changes. To address this, we propose Video Geometry Corrector (VGC), a post-hoc video-to-video model trained on synthetic paired supervision. Starting from real videos with diverse camera motion and pose annotations, we construct VG-Pairs with a synthetic paired-supervision data generation pipeline. Each video clip is treated as a geometry-consistent target and paired with a distorted counterpart synthesized by a pretrained image-to-video inpainting model using trajectory-adaptive keyframes. VGC learns to map the distorted input to the geometry-consistent target without modifying the source generator, and uses optical flow as an auxiliary cue to help disentangle camera motion from object motion. Experiments on pose-conditioned and prompt-driven benchmarks show that VGC improves geometric consistency across multiple source generators, and scaling to a larger backbone further extends the framework toward more general video refinement.

---


> [!TIP]
> 当前位于：**201-213**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-213**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
