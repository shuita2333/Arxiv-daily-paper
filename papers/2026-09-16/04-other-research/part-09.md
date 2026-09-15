# 📦 其他研究 | 2026年09月16日

> 本类共 **416** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-416**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-416**

---

### 401. [LongAgent: History-Guided Agentic Search for Longitudinal Outcome Prediction](https://arxiv.org/abs/2609.15859)

**<font color=#1a73e8>作者：</font>** Siyao Wang, Florian Guitton, Shuojie Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Extracting informative representations from longitudinal data that can predict future outcomes remains a critical challenge in medicine. Medical datasets are inherently heterogeneous, consisting of a large number of variables collected from different sources, sampled with different temporal spacings, and representing different aspects of human health status. This requires identifying those variables with predictive value, processing longitudinal information, and integrating multiple variables for outcome prediction. Here, we propose a novel agent-based approach, LongAgent, that can autonomously search over combinations of variable sets, temporal windows and longitudinal aggregation functions, and identify candidates with promising predictive performance. LongAgent utilises a history memory of previous searches and numerical evidence to guide subsequent exploration. On synthetic data, LongAgent achieves a mean prediction RMSE of 1.7376 and improves over the strongest non-agent baseline by 0.0151 (95% CI: [0.0045,0.0260]; p=0.0273). On a real clinical dataset, it performs comparably to the best baseline.

---


### 402. [LynnReal-Omni: Native multi-modal Video Generation for Agentic Visual Workflows](https://arxiv.org/abs/2609.15863)

**<font color=#1a73e8>作者：</font>** Xiaofeng Mao, Peijia Lin, Shaohao Rui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion models are stochastic and hard to control: precise content often requires repeated sampling without guaranteed success, and long-horizon scenes drift in appearance, interactions, and temporal coherence. Agentic visual creation provides explicit references, editable 3D scenes, or executable game states for stable control, but does not by itself guarantee high object or character fidelity. Combining the two can enable stable, high-quality generation. To realize this combination, we present LynnReal-Omni, a native multimodal video generation framework built on a 32B shared multimodal diffusion transformer that unifies text-to-video, image-conditioned generation, reference-guided generation, structural control, editing, degraded video restoration, and long-video generation. It accepts heterogeneous visual inputs, including appearance references, editable 3D renders, and game recordings, allowing agents to compose visual conditions within a unified model. We also train a dedicated 27B Flash shared multimodal diffusion transformer for real-time rendering. We build a systematic data pipeline for video cleaning, subject association, multimodal annotation, and aligned control construction, yielding a curated corpus of multi-shot audiovisual segments, and introduce MSAVP, a 100-prompt, 20-metric evaluation design that separates instruction following, generating plausibility, visual quality, temporal behavior, and audio coordination. LynnReal-Omni-Flash further reduces inference cost through model and decoding acceleration, including a lightweight VAE decoder; on one H100, warm generation and decoding of a 22-frame 540p video take 843 ms with LynnReal-Omni and 377 ms with Flash. These results provide a foundation for real-time streaming video generation, making LynnReal-Omni a unified, controllable, and efficient basis for agentic visual creation.

---


### 403. [On Edge in the Dental Chair: Designing VR Support for Moments of Dental Anxiety](https://arxiv.org/abs/2609.15867)

**<font color=#1a73e8>作者：</font>** Zhu Guo, Junjie Zhao, Haofan He 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Dental anxiety can change as a procedure unfolds, yet dental virtual reality (VR) commonly provides continuous distraction or relaxation. We investigate how support can be coordinated with specific simulated dental events. Stakeholder interviews (N=36), participatory design with three returning dentists, and patient walkthroughs of a no-intervention prototype (N=12) informed five Anxiety Events and an intervention-module framework. Drawing on cognitive vulnerability and emotion regulation, we implemented a standardized event-contingent VR system with predefined event-module assignments and shared agency and safety controls. A randomized study (N=24) compared the intervention package with no-intervention VR. The adjusted intervention-minus-control difference averaged -12.83 VAS-A points across events (95% CI [-24.42, -1.70]). Physiological, behavioural, and qualitative measures contextualized participants' experiences. The findings inform timely, comprehensible support and reassuring social presence in simulated dental VR; they concern the complete package rather than individual modules or clinical effectiveness.

---


### 404. [Learning Multimodal One-step Flow Policy via Value-weighted Optimal Transport](https://arxiv.org/abs/2609.15883)

**<font color=#1a73e8>作者：</font>** Jaehun Shon, Jinha Choi, Jongwook Jeon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning aims to learn a policy solely from fixed datasets, which often contain multimodal action distributions. Flow policies can naturally represent such multimodal behaviors, but learning an efficient one-step flow policy remains challenging: standard value guidance often leads to mode collapse or exploits overestimation bias in out-of-distribution regions. To address this, we introduce One-step Flow policy via Optimal Transport (OptiFlow), a framework for one-step flow policy learning as a structured sample-allocation problem. OptiFlow jointly trains a value-aware reference flow policy and an efficient one-step policy, coupling their action samples through state-wise entropic optimal transport. For each state, critic-estimated values define the priority of distillation target actions, while the action-distance cost ensures geometrically compatible pairings. By avoiding direct critic maximization, our transport-guided approach enables in-distribution exploitation by anchoring the one-step policy to high-value, dataset-supported modes without the risk of out-of-distribution divergence. Experimental results demonstrate that OptiFlow effectively captures optimal multimodal behaviors and achieves strong performance across diverse offline RL benchmarks. Our code is available at this https URL.

---


### 405. [Privacy-enhanced federated learning via asynchronous aggregation and local differential perturbation](https://arxiv.org/abs/2609.15885)

**<font color=#1a73e8>作者：</font>** Zhen Zhong, Shini Yang, Liesheng Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study proposes a privacy-enhanced federated learning framework to address secure collaborative training in distributed data environments. The framework integrates Dynamic Differential Privacy (DDP), lightweight Homomorphic Encryption (HE), and Local Differential Privacy (LDP) mechanisms to ensure data privacy protection during model training. Additionally, the framework employs an asynchronous aggregation strategy with version control to support distributed training in asynchronous environments. Experimental validation on the CIFAR-10 and Purchase-100 benchmark datasets demonstrates that the method maintains high classification accuracy (up to 82.6%) even under stringent privacy constraints ({\epsilon} = 0.1), while reducing communication overhead by 21.3% compared to FedAvg. Experimental results demonstrate that this framework effectively balances privacy protection and model performance in distributed machine learning scenarios, providing a scalable technical foundation for large-scale distributed collaborative computing.

---


### 406. [Anatomical Grounding and Leakage-Aware Multimodal Contrastive Learning for Alzheimer's Disease Classification from Structural MRI](https://arxiv.org/abs/2609.15888)

**<font color=#1a73e8>作者：</font>** Paul-Gabriel Nicolae, Irina Georgiana Mocanu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep networks trained on structural MRI for Alzheimer's disease (AD) staging often reach reasonable accuracy while attending to anatomically irrelevant regions, and multimodal models that add clinical tables frequently rely on variables that were used to assign the diagnostic label in the first place. We study both issues with a deliberately lightweight slice-based encoder (ResNet18 with a one-layer Transformer over slices) on 1,075 baseline T1-weighted scans from ADNI-1. First, we use FastSurfer segmentations as an anatomical reference: YOLOv8 models trained on segmentation-derived labels localize Alzheimer-relevant structures with mAP_50 above 0.96, and a Grad-CAM comparison shows that the image-only classifier frequently attends to the skull, orbits and background. Second, we adapt a CLIP-style image - tabular contrastive framework and organize ADNIMERGE variables along a label-leakage spectrum. Fusion with cognitive scores yields 87.3% three-way accuracy, which we treat as a leakage-driven upper bound rather than an imaging result; fusion with regional volumes yields 73.0%. We observe that the choice of contrastive target changes what the image encoder learns: on MCI vs. CN, the image-only head reaches 52.4% when the encoder is aligned to cognitive scores and 73.8\% when aligned to volumes, although no tabular input is used at inference. Third, restricting the input to a per-subject crop of the medial temporal lobe raises image-only three-way accuracy from 58.7% to 65.1%. All results come from single runs on a small balanced test set, and we report confidence intervals and the protocol differences that prevent direct comparison with published numbers.

---


### 407. [How do people plan digitally: An in-the-wild investigation of task planning through a smartphone app](https://arxiv.org/abs/2609.15904)

**<font color=#1a73e8>作者：</font>** Srija Halder, Isabella Zimmermann, Linnea Körte 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Daily planning supports goal attainment and productivity, and people increasingly delegate it to digital tools. Plans are postponed, revised, and left unresolved rather than executed as intended. Understanding these changes requires following tasks from creation through later updates and recorded outcomes. We report an in-the-wild study of task planning using time-stamped logs of 24,265 tasks from 957 users of a widely used daily planner app, observed over six weeks alongside self-reported surveys. Following each task across its lifecycle, only 26.4% moved directly from creation to completion and 32.0% were abandoned; all-day and longer tasks were abandoned disproportionately, and 77.6% of timed tasks were marked complete later than intended. Latent profile analysis of 909 users indicated High Engagement (11.1%), Low Engagement (19.7%), and Passive (69.2%) profiles; active days on app distinguished the profiles and were associated with post-survey completion. These findings support evaluating planning tools across the task lifecycle.

---


### 408. [Safe Meta-Reinforcement Learning via Information Space Reachability](https://arxiv.org/abs/2609.15915)

**<font color=#1a73e8>作者：</font>** Zeyang Li, Sunbochen Tang, Navid Azizan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Meta-reinforcement learning (meta-RL) enables agents to adapt to unseen tasks with limited experience. Despite its promise, the application of meta-RL in real-world tasks is hindered by safety requirements, which have been underexplored in prior work. In this paper, we propose a safe meta-RL framework that explicitly accounts for safety during adaptation. Our key insight is to reason about safety in the information space, which captures both the physical state and the agent's belief over the underlying task. Within this space, we introduce a safety value function that measures the probability of the agent avoiding unsafe regions indefinitely. We show that this function satisfies a self-consistency condition and a Bellman equation, which make it learnable via meta-RL. Based on this formulation, we develop a safe meta-RL algorithm that learns the safety value function and leverages it for safety filtering and constrained policy optimization. Experiments on meta-RL benchmarks demonstrate the effectiveness of the proposed method.

---


### 409. [Pilot Early, Commit Late: A Real-Options Model of Enterprise AI Adoption under Rapid Technological Progress](https://arxiv.org/abs/2609.15919)

**<font color=#1a73e8>作者：</font>** Gaurav Tewari  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence presents firms with an unusual timing problem. The technology frontier is improving rapidly, implementation is partly irreversible, and organization-specific capabilities are accumulated through action. This paper develops a two-period decision model of AI deployment under uncertainty in which a firm chooses among immediate deployment, a limited pilot, and waiting. Deployment earns current operating value but exposes the firm to architectural obsolescence; waiting preserves the option to adopt after the frontier is observed; a pilot sacrifices current operating value to build organization-specific learning without full commitment. The model yields five central timing results and a sixth comparative result on where learning occurs. First, a mean-preserving increase in frontier uncertainty raises the value of waiting and piloting but leaves immediate deployment unchanged when its payoff is affine in the frontier. Second, faster expected frontier progress can reduce the relative attractiveness of immediate deployment when deployed architecture captures only a limited share of future improvement. Third, a pilot dominates waiting exactly when the expected value of the capability it builds exceeds its cost. Fourth, sufficiently valuable organization-specific learning creates a nonempty region in which "pilot early, commit late" is optimal. Fifth, there is a closed-form modularity threshold above which immediate deployment dominates the best outside option. Sixth, production learning and pilot-specific learning affect the timing margin differently. A continuous-time extension recovers the standard result that uncertainty raises the adoption threshold while capability and modularity lower it. The paper separates deploying, experimenting, and waiting, and shows why rapid progress can rationally increase experimentation without justifying irreversible commitment.

---


### 410. [Recurrent GraphNeural NetworkswithSet-BasedAggregation](https://arxiv.org/abs/2609.15932)

**<font color=#1a73e8>作者：</font>** Blai Bonet  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recurrent GNNs iterate message passing to convergence, and their logical characterizations to date rely on multi-set aggregation, graded (counting) logics, and halting or acceptance conditions that cannot be verified from the network's parameters. We study recurrent GNNs with set-based aggregation and identify sufficient conditions checkable from the weights for networks to compile into formulas and formulas into networks. The main result is an effective, two-directional equivalence between a class of networks and the Boolean closure of reachability and safety properties, the fragment B$\Sigma^{\circ}_1$ of the modal $\mu$-calculus. The fragment is not an artifact: it is the exact expressive level of stabilization over finite vocabulary, which supports fixed points of a single polarity and Boolean combinations thereof, but not the composition of fixed points of opposite polarities. The correspondence needs no counting logic, no external halting signal, and no non-effective acceptance condition, yielding a verifiable path from weights to symbolic explanations for networks meeting the conditions.

---


### 411. [Pulla: A Parsons Problem Tool for Fine-Grained Behavioral Tracing and Instructor-Facing Problem-Solving Analysis](https://arxiv.org/abs/2609.15944)

**<font color=#1a73e8>作者：</font>** Daniel Prol, Juho Leinonen, Arto Hellas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Existing Parsons problem tools primarily focus on correctness, indicating whether a student solved a problem, but providing limited visibility into the underlying problem-solving process. We address this gap by introducing Pulla, a Parsons problem tool that instruments programming assignments to capture fine-grained interaction data. These behavioral traces allow the system to surface recurring difficulty patterns, giving instructors actionable insights to inform targeted intervention decisions. This paper describes our experience in developing and deploying Pulla. We deployed the tool in two university courses: an upper-division software design course at the University of Houston (United States) and an introductory programming course at Aalto University (Finland). By analyzing the data collected, we identified common difficulty patterns, including misidentifying exception types, confusing return with the throw/raise mechanism, and incorrect control-flow ordering.

---


### 412. [Privacy-Aligned Personalized Federated Learning with Compact Adaptation and Variable-Length Gaussian Communication](https://arxiv.org/abs/2609.15950)

**<font color=#1a73e8>作者：</font>** Yilin Xu, Chun Hei Michael Shiu, Chih Wei Ling 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Record-level differential privacy exposes a structural misalignment in personalized federated learning when client-specific variation is low-dimensional while training repeatedly releases high-dimensional updates. In this paper, we address this misalignment by releasing a private client context once and confining repeated adaptation to a fixed coefficient space. Beyond dimensionality reduction, the factorized generator induces an adaptive optimization geometry that reshapes noisy updates, and controlled ablations show that most of its private-training gain is retained by radial evolution. To further reduce the communication cost, we realize the Gaussian mechanism for coefficient updates directly through variable-length quantization with finite expected code length, so that the quantization error itself serves as the required privacy perturbation rather than extra distortion. Across MNIST and CIFAR-10, our design matches or outperforms full-model private adaptation across privacy budgets and client heterogeneity, while reducing protected uplink by a factor of 2.67 at \(\varepsilon=16\) on CIFAR-10 with comparable future-client accuracy.

---


### 413. [Disentangling Representation Evolution in Transformers through Directional Decomposition](https://arxiv.org/abs/2609.15975)

**<font color=#1a73e8>作者：</font>** Shwai He, Haichao Zhang, Shen Yan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer representations evolve through learned additive transformations that either preserve their current direction or redirect it. We study this evolution as a functional geometry, decomposing learned updates into parallel and perpendicular components. Across pretrained models, we find substantial parallel components beyond the residual identity path. We then apply the decomposition in two spaces: to attention and MLP updates relative to the hidden state, and to attention value aggregation relative to the current token's value. Targeted edits reveal a strongly space-dependent asymmetry: exclude-self value-space parallel manipulation is markedly more robust than residual-space and perpendicular counterparts, preserving the direct self message while scaling only the non-self aggregate. The same decomposition gives a component-resolved description of compression-induced update error: perpendicular error separates compression methods more clearly than parallel error. Extensive experiments further demonstrate that full-aggregate parallel suppression during from-scratch pretraining lowers validation-loss trajectories and improves downstream averages, with the value-space variant strongest. Together, these results connect representation geometry to editing robustness, compression diagnosis, and training-time intervention. Code is available in the \href{this https URL}{project repository}.

---


### 414. [The CAST-framework: Measure and model social media use as a multi-level phenomenon through real-world applications](https://arxiv.org/abs/2609.15978)

**<font color=#1a73e8>作者：</font>** David Grüning, Jasper Doeninghaus, Zina Efchary 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Designing social media experiences that support well-being requires understanding when, how, and for whom use matters. Screen-time totals omit content and context, and connecting these with behavior and experience requires coordinating measurements across timescales. We introduce the CAST framework to connect measurement choices with person-specific models of exposure, behavior, physiology, and experience. Its dimensions specify where observations occur, how they are obtained, what they measure, and at what temporal resolution. Responses to interventions, such as whether to proceed after an app-opening pause, enter as behavioral measurements. We propose four synchronized measurement modules linking mobile and wearable data with self-reports and intervention responses. A synthetic demonstration with 120 simulated participants over 28 days illustrates how daily aggregation can obscure opposing effects of different activities under specified generating assumptions. The framework guides selection of measures and outcomes for evaluating social media interfaces and interventions.

---


### 415. [A Chosen Future Can Still Be Rewritten: Causal Writability in Video Models](https://arxiv.org/abs/2609.15980)

**<font color=#1a73e8>作者：</font>** Xingyun Wang, Haomin Zheng, Man Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a video model generates physically incorrect motion, did it fail to learn the correct motion, or did it learn it but fail to use it? We show the latter: the correct motion remains available inside the model and can still be made to control the generated video. We train on videos where red masses oscillate slowly and blue masses oscillate quickly, then test a red mass with fast observed motion. Even when the model generates slow motion in this conflicting case, a low-dimensional edit predicted from simple physical variables restores the correct fast motion. We call this ability causal writability. At fixed strength, we find a sharp depth boundary: the same edit changes the video before the boundary but not after it. This closure marks commitment for that write. The motion signal nevertheless remains, and a stronger downstream write can restore physical motion, while excessive gain overshoots. Early causal writability predicts which errors training later corrects: those errors are writable at more network depths than errors that persist. We reproduce both causal writability and its sharp closure in a pretrained 1.3B video model, supporting generality across model scale and training regime.

---


### 416. [Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science](https://arxiv.org/abs/2609.15983)

**<font color=#1a73e8>作者：</font>** Honghao Lin, David P. Woodruff, Yuan Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models can produce plausible short proofs, but may still be unreliable on long-horizon research problems, where progress depends on a sequence of uncertain and interdependent decisions. We introduce Stellar Colosseum, a model-agnostic harness for allocating inference across research in mathematics and theoretical computer science. Colosseum explores alternative strategies before proof construction, uses a readiness gate to decide when a route is mature enough to decompose, represents the proof plan as interdependent section-level subproblems, and routes verifier findings back to the affected part of the argument. Across these stages, it generates candidates in parallel, attacks them with targeted falsification, and combines candidates and their critiques into a single research artifact through overlapping random-sample tree aggregation. The Colosseum workflow has also been integrated into Google Antigravity's Teamwork framework as the Long Proof pattern.
We demonstrate the capabilities of Colosseum through open-ended research and evaluations on theorem-proving and competitive programming benchmarks. Using Colosseum with Gemini 3.1 Pro, we obtain several new results that address open problems arising from papers published at top venues such as FOCS and JMLR. On TCS-Bench, a benchmark of research-level theorem-proving tasks drawn from papers published at FOCS, STOC, and SODA, Colosseum achieves 71.0% accuracy using Gemini 3.1 Pro and Gemini 3.7 Flash. In a separate Codeforces evaluation using Gemini 3.1 Pro, the proof-oriented pipeline with execution feedback solves 218 of 222 problems.

---


> [!TIP]
> 当前位于：**401-416**（第 9/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-416**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
