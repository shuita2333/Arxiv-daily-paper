# 🧠 大模型相关研究 | 2026年05月23日

> 本类共 **162** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-162](./part-04.md)

---

### 1. [Teaching Language Models to Forecast Research Success Through Comparative Idea Evaluation](https://arxiv.org/abs/2605.21491)

**<font color=#1a73e8>作者：</font>** Srujan P Mule, Aniketh Garikaparthi, Manasi Patwardhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As language models accelerate scientific research by automating hypothesis generation and implementation, a new bottleneck emerges: evaluating and filtering hundreds of AI-generated ideas without exhaustive experimentation. We ask whether LMs can learn to forecast the empirical success of research ideas before any experiments are run. We study comparative empirical forecasting: given a benchmark-specific research goal and two candidate ideas, predict which will achieve better benchmark performance. We construct a dataset of 11,488 idea pairs grounded in objective outcomes from PapersWithCode. While off-the-shelf 8B-parameter models struggle (30% acc.), SFT dramatically boosts performance to 77.1%, outperforming GPT-5 (61.1%). By framing evaluation as a reasoning task via Reinforcement Learning with Verifiable Rewards (RLVR), we train models to discover latent reasoning paths, achieving 71.35% acc. with interpretable justifications. Through additional ablations and out-of-distribution tests, we show robustness to surface-level heuristics and transfer to both a cross-domain time-split test set and an independently constructed test set. Our results demonstrate that compute-efficient small language models can serve as effective, objective verifiers, offering a scalable path for autonomous scientific discovery.

---


### 2. [HealthCraft: A Reinforcement Learning Safety Environment for Emergency Medicine](https://arxiv.org/abs/2605.21496)

**<font color=#1a73e8>作者：</font>** Brandon Dent  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frontier language models are being deployed into clinical workflows faster than the infrastructure to evaluate them safely. Static medical-QA benchmarks miss the failure modes that matter in emergency medicine: trajectory-level safety collapse, tool misuse, and capitulation under sustained clinical pressure. We present HealthCraft, the first public reinforcement-learning environment that rewards trajectory-level safety under realistic emergency-medicine conditions, adapted from Corecraft. It is built on a FHIR R4 world state with 14 entity types and 3,987 seed entities, exposes 24 MCP tools, and defines a dual-layer rubric that zeroes reward whenever any safety-critical criterion is violated. We release 195 tasks across six categories, graded against 2,255 binary criteria (515 safety-critical); a post-hoc 10-task negative-class slate extends this to 205 tasks and 2,337 criteria. V8 results on two frontier models show Claude Opus 4.6 at Pass@1 24.8% [21.5-28.4] and GPT-5.4 at 12.6% [10.2-15.6], with safety-failure rates of 27.5% and 34.0%. On multi-step workflows - the closest proxy to real emergency care - performance collapses to near zero (Claude 1.0%, GPT-5.4 0.0%) despite partial competence on individual steps. Six infrastructure bugs fixed between pilots v2 and v8 re-ordered which model "looks stronger," evidence that infrastructure fidelity is part of the measurement. A deterministic LLM-judge overlay bounds evaluator noise, and a 60-run negative-class smoke pilot shows the reward signal is not drop-in training-safe: restraint criteria pass at 0.929 prevalence, a gameability an eval harness can tolerate but a training reward cannot. We scaffold coupling to a Megatron+SGLang+GRPO loop per Corecraft Section 5.2 and leave training-reward ablations as future work. Environment, tasks, rubrics, and harness are released under Apache 2.0.

---


### 3. [Harnesses for Inference-Time Alignment over Execution Trajectories](https://arxiv.org/abs/2605.21516)

**<font color=#1a73e8>作者：</font>** Boyuan Wang, Bochao Li, Minghan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Harness engineering has emerged as an important inference-time technique for large language model (LLM) agents, aiming to improve long-term performance through task decomposition and guided execution. However, more elaborate harnesses are not uniformly better: increasing decomposition or guidance can sometimes improve execution, but can also reduce final task success. We study harness design through the lens of inference-time trajectory alignment. This perspective separates harness into two mechanisms: task decomposition, which structures a task into sub-goals, and guided execution, which reshapes local action distributions during execution. This decomposition allows us to quantify how workflow granularity, retry budgets, and guidance-induced action reweighting shape the performance limits of harness design. It further reveals concrete failure modes, including over-decomposition, over-pruning, and hallucinated execution. We validate these predictions through controlled synthetic experiments and real terminal agent benchmarks. Inspired by the theory, we further show that effective harnesses can be partial: specifying only the initial steps and leaving the remaining execution to agent can achieve higher pass rate than fully structured workflows.

---


### 4. [DualOptim+: Bridging Shared and Decoupled Optimizer States for Better Machine Unlearning in Large Language Models](https://arxiv.org/abs/2605.21539)

**<font color=#1a73e8>作者：</font>** Xuyang Zhong, Qizhang Li, Yiwen Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose DualOptim+, a novel optimization framework for improving machine unlearning in large language models. It introduces a base state to capture common representations shared by forgetting and retaining objectives and delta states to preserve objective-specific residuals. This architecture allows the optimizer to adaptively bridge shared and decoupled states based on the directional conflict between forgetting and retaining gradients. We further introduce DualOptim+ 8bit, a quantized variant that reduces memory overhead without compromising performance. Extensive experiments across fictitious and real-world unlearning, safety alignment, and multi-task learning tasks demonstrate that DualOptim+ consistently achieves a superior trade-off between different objectives. Codes are available at this https URL.

---


### 5. [Provable Joint Decontamination for Benchmarking Multiple Large Language Models](https://arxiv.org/abs/2605.21543)

**<font color=#1a73e8>作者：</font>** Zhenlong Liu, Hao Zeng, Hongxin Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benchmark data contamination has become a central challenge in LLM evaluation: when evaluation examples appear in the training data of one or more audited models, reported performance can be inflated and cross-model comparisons become unreliable. A broad line of training-data detection work designs scores to quantify how strongly a model memorizes a given data point, but these score-based methods lack theoretical guarantees. Recent conformal approaches provide provable false-identification control for a single model; however, applying them separately to each model can produce model-specific benchmarks, undermining fair comparison across models. In this work, we formalize multi-model benchmark decontamination as a joint selection problem and propose Joint Envelope Conformal Selection (JECS), a conformal procedure that enables global contamination rate (GCR) control under stated assumptions. Specifically, JECS computes per-model conformal p-values, aggregates them by the per-item maximum, and reconstructs a conservative envelope of the max-p null distribution from right-tail observations above a data-driven threshold. By applying the adaptive Benjamini-Hochberg (BH) procedure to the envelope-rescaled values, we select a benchmark with provable GCR control. Extensive experiments across various models and benchmarks demonstrate that JECS achieves higher power than the max-p baseline while consistently maintaining the target GCR control.

---


### 6. [Tabular foundation models for robust calibration of near-infrared chemical sensing data](https://arxiv.org/abs/2605.21544)

**<font color=#1a73e8>作者：</font>** Robin Reiter, Denis Cornet, Fabien Michel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Near-infrared spectroscopy is increasingly used as a rapid, non-destructive chemical sensing technology for the analysis of food, pharmaceutical, biological, and environmental samples. However, the practical deployment of NIR sensors still depends on calibration models able to handle high-dimensional, collinear spectra, limited sample sizes, preprocessing dependence, spectral outliers, and extrapolation beyond the calibration domain. Here, we evaluate whether tabular foundation models can provide a new calibration strategy for NIR chemical sensing. We benchmark TabPFN on 66 NIR datasets covering 54 regression and 12 classification tasks, and compare direct inference on raw spectra with preprocessing-optimized inference against PLS/PLS-DA, Ridge, Catboost, and one-dimensional convolutional neural networks. The study uses a unified validation framework in which preprocessing and model selection are performed exclusively on calibration data before external test evaluation. In regression, preprocessing-optimized TabPFN achieves the best overall average rank and significantly outperforms PLS, CatBoost, TabPFN on raw spectra, and CNN-1D, while remaining statistically comparable to Ridge. In classification, TabPFN applied directly to raw spectra provides the best average rank, with performance close to the optimized variant. Robustness analyses show that TabPFN provides strong average predictive performance but that its advantage decreases on spectral outliers and extrapolated samples, where classical chemometric models remain competitive. These results suggest that tabular foundation models can complement established chemometric workflows for NIR chemical sensing, especially in small- to medium-sized calibration settings, while highlighting the need for spectroscopy-specific priors and uncertainty-aware deployment strategies.

---


### 7. [From Parameters to Data: A Task-Parameter-Guided Fine-Tuning Pipeline for Efficient LLM Alignment](https://arxiv.org/abs/2605.21558)

**<font color=#1a73e8>作者：</font>** Hao Chen, Qi Zhang, Liyao Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting Large Language Models (LLMs) to specialized domains typically incurs high data and computational overhead. While prior efficiency efforts have largely treated data selection and parameter-efficient fine-tuning as isolated processes, our empirical analysis suggests they may be intrinsically coupled. We posit the Strong Map Hypothesis: a sparse subset of attention heads plays a dominant role in task-specific adaptation, acting as keys that unlock specific data patterns. Building on this observation, we propose From Parameters to Data (P2D), a unified framework that leverages these task-sensitive attention heads as a dual compass for both sample mining and structural pruning. To rigorously quantify the total pipeline cost, we introduce the Alignment Efficiency Ratio (AER) metric for both selection latency and training time. Mechanistically, P2D identifies critical heads via a lightweight proxy and uses them as a functional filter to curate high-affinity data, establishing a synergistic pipeline. Empirically, by updating merely 10% of attention heads on 10% of the data, P2D achieves an 8.3 pp performance gain over strong baselines and delivers a 7.0x end-to-end time speedup. These results validate that precise parameter-data synchronization eliminates redundancy, offering a new paradigm for efficient alignment.

---


### 8. [AutoMCU: Feasibility-First MCU Neural Network Customization via LLM-based Multi-Agent Systems](https://arxiv.org/abs/2605.21560)

**<font color=#1a73e8>作者：</font>** Penglin Dai, Zijie Zhou, Xincao Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying neural networks on microcontroller units (MCUs) is critical for edge intelligence but remains challenging due to tight memory, storage, and computation constraints. Existing approaches, such as model compression and hardware-aware neural architecture search (HW-NAS), often depend on proxy metrics, incur high search cost, and do not fully bridge the gap between architecture design and verified deployment. This paper presents AutoMCU, a feasibility-first large language model (LLM)-based multi-agent system for automated neural network customization under MCU constraints. Given natural-language task requirements and hardware specifications, AutoMCU iteratively generates structured architecture candidates, filters infeasible designs through vendor toolchain feedback before training, evaluates feasible models under a controlled protocol, and verifies deployability through backend-grounded deployment analysis. AutoMCU includes two key mechanisms: 1) hardware-in-the-loop architecture generation for early elimination of undeployable candidates under RAM and Flash constraints, and 2) state-isolated multi-agent scheduling for stable coordination of proposal, training, evaluation, and deployment stages. Experiments on CIFAR-10 and CIFAR-100 under strict MCU constraints show that AutoMCU achieves competitive accuracy while reducing customization time to about 1--2 hours, compared with hundreds of GPU hours for representative MCU-oriented HW-NAS baselines. Comparisons with ColabNAS and the LLM-based NAS method GENIUS on NAS-Bench-201 further demonstrate the effectiveness and stability of AutoMCU. Real-device deployments on multiple STM32 microcontrollers validate its practical applicability to MCU-scale edge intelligence.

---


### 9. [Leveraging Self-Paced Curriculum Learning for Enhanced Modality Balance in Multimodal Conversational Emotion Recognition](https://arxiv.org/abs/2605.21565)

**<font color=#1a73e8>作者：</font>** Phuong-Anh Nguyen, The-Son Le, Duc-Trong Le 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal Emotion Recognition in Conversations (MERC) is a crucial task for understanding human interactions, where multimodal approaches integrating language, facial expressions, and vocal tone have achieved significant progress. However, modality misalignment and imbalanced learning remain major challenges, limiting the effective utilization of multimodal information. To address this issue, we propose a plug-and-play framework based on Self-Paced Curriculum Learning (SPCL) for MERC. We introduce a dual-level Difficulty Measurer that captures both utterance-level and conversation-level challenges. The utterance-level score models fine-grained modality-specific difficulty, while the conversation-level score captures broader dialogue structures, including emotional dependencies and modality coherence. Based on these scores, the Learning Scheduler dynamically guides training from easier to more difficult instances. By integrating SPCL into existing MERC architectures, our method alleviates modality imbalance and improves model robustness. Extensive experiments on the IEMOCAP and MELD datasets demonstrate consistent improvements across different architectures and modality settings. On IEMOCAP, SPCL improves weighted F1-score by approximately +1.2% to +6.6% over baseline models, while on MELD, gains reach up to +10.4%. These results highlight the effectiveness and generalizability of SPCL as a lightweight plug-and-play module for multimodal emotion recognition.

---


### 10. [When Support Escalates Distress: Regulation and Escalation in LLM Responses to Venting and Advice-Seeking](https://arxiv.org/abs/2605.21569)

**<font color=#1a73e8>作者：</font>** Vivienne Bihe Chi, Adithya V Ganesan, Ryan L Boyd 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used for mental health support, yet little is known about whether their responses are psychologically safe across different help-seeking styles. We examine a foundational distinction in emotional disclosure, venting vs. advice-seeking, and whether LLMs respond in ways that regulate or amplify distress. Using 178,800 Reddit posts, we first show the two help-seeking styles are linguistically distinguishable at scale. We then introduce a measurement framework grounded in interpersonal emotion regulation theory that captures Regulation and Escalation as empirically independent dimensions. Across persona conditions (default, friend, therapist), GPT-5.3 responses systematically mirror help-seeking style: venting elicits more regulation, but also more escalation. Therapist personas reduce escalation while maintaining regulation, whereas friend personas increase both. A crowdsourced human study finds no user experience penalty for the safer therapist condition, but reveals that lay raters cannot reliably detect escalation without expert knowledge. Responses that feel supportive may simultaneously intensify distress in ways standard safety evaluation cannot see, and empathy metrics alone cannot replace a framework that measures both.

---


### 11. [Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs](https://arxiv.org/abs/2605.21602)

**<font color=#1a73e8>作者：</font>** Dylan Feng, Pragya Srivastava, Cassidy Laidlaw  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many safety and alignment failures of large language models (LLMs) occur due to out-of-distribution (OOD) situations: unusual prompt or response patterns that are unforeseen by model developers. We systematically study whether LLM monitoring pipelines can detect these OOD alignment failures by introducing a benchmark called Misalignment Out Of Distribution (MOOD). It is difficult to find failures that are truly OOD for off-the-shelf models trained on vast safety datasets. We sidestep this by including a restricted training set in MOOD that we use to train our own monitors, as well as seven test sets with diverse alignment failures that are outside the training distribution. Using MOOD, we find that guard models (safety classifiers) often fail to generalize OOD. To fix this, we propose combining guard models with OOD detectors. We test four types of OOD detectors and find that a combination of a guard model with Mahalanobis distance and perplexity-based OOD detectors can improve recall from 39% to 45%. We also establish positive scaling trends across model scales for monitors that combine a guard model and OOD detector; we find that incorporating OOD detection into monitoring achieves a higher recall gain than using a guard model with 20 times more parameters. Our work suggests that OOD detection should be a crucial component of LLM monitoring and provides a foundation for further work on this important problem.

---


### 12. [Argo: Efficient Importance Labeling for Enterprise Email Systems](https://arxiv.org/abs/2605.21604)

**<font color=#1a73e8>作者：</font>** Siddhant Ray, Ganesh Ananthanarayanan, Kevin Chian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Email importance labeling has long been a critical yet challenging problem for businesses and individuals. Traditional approaches; such as keyword matching, user-defined rules, and sender-based heuristics; demand extensive manual feature engineering and fail to scale effectively or generalize. Recent advances in large language models (LLMs) demonstrate strong potential and a natural fit for this task, offering deep contextual understanding and superior labeling quality. However, using LLM models like GPT-4.1 at enterprise email volumes incurs prohibitive computational costs and hinders real-world deployment. We explore the trade-off space of using alternative labeling schemes as opposed to GPT4.1 scale LLMs, with the goal of achieving near GPT level labeling quality with significantly lower cost. We develop Argo, an enterprise email labeling framework, where we construct a profiler to efficiently search the cost quality trade-off space of labeling and identify cost-efficient alternatives to labeling emails. Additionally, we design an on-demand provisioning scheme to intelligently scale Argo with real time load, to minimize cost increases during peak load inference. Over 3 open-source email datasets, Argo achieves 148-167X inference cost reduction with negligible quality degradation and 20-640000X lower profiling costs, making large-scale, context-aware email labeling practical for enterprises.

---


### 13. [CR4T: Rewrite-Based Guardrails for Adolescent LLM Safety](https://arxiv.org/abs/2605.21609)

**<font color=#1a73e8>作者：</font>** Heajun An, Qi Zhang, Vedanth Achanta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly embedded in adolescent digital environments, mediating information seeking, advice, and emotionally sensitive interactions. Yet existing safety mechanisms remain largely grounded in adult-centric norms and operationalize safety through refusal-oriented suppression. While such approaches may reduce immediate policy violations, they can also create conversational dead-ends, limit constructive guidance, and fail to address the developmental vulnerabilities inherent in adolescent-AI interactions. We argue that adolescent LLM safety should be framed not solely as a filtering problem, but as a socio-technical, developmentally aligned transformation problem. To operationalize this perspective, we propose Critique-and-Revise-for-Teenagers (CR4T), a model-agnostic safeguarding framework that selectively reconstructs unsafe or refusal-style outputs into ageappropriate, guidance-oriented responses while preserving benign intent. CR4T combines lightweight risk detection with domain-conditioned rewriting to remove risk-amplifying content, reduce unnecessary conversational shutdown, and introduce developmentally appropriate guidance. Experimental results show that targeted rewriting substantially reduces unsafe and refusal-oriented outcomes while avoiding unnecessary intervention on acceptable interactions. These findings suggest that selective response reconstruction offers a more human-centered alternative to refusal-centric guardrails for adolescent-facing LLM systems.

---


### 14. [Exploring the Effectiveness of Using LLMs for Automated Assessment of Student Self Explanations in Programming Education](https://arxiv.org/abs/2605.21614)

**<font color=#1a73e8>作者：</font>** Arun-Balajiee Lekshmi-Narayanan, Mohammad Hassany, Peter Brusilovsky  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Worked examples are step-by-step solutions to problems in a specific domain, offered to students to acquire domain-specific problem-solving skills. The effectiveness of worked examples could be enhanced by combining them with self-explanations, which ask students to explain rather than passively study each problem-solving step. The main challenge of this approach is assessing the correctness of the student's explanations. In the prevailing approach, student explanations are judged by their semantic similarity to an instructor's or domain expert's explanation. Given recent advances in LLM-based automated scoring, it remains unclear whether semantic similarity methods are still the most effective technique to automatically score textual student responses like essays or code explanations. Comparing these methods also requires quality datasets that offer distinctive features such as balanced class distributions and domain-specific labeled data for automated scoring tasks. In this paper, we present a rigorous comparison between LLMs and semantic similarity used for automated scoring, framed as a binary classification task.

---


### 15. [The Shape of Testimony: A Scalable Framework for Oral History Archive Comparison](https://arxiv.org/abs/2605.21623)

**<font color=#1a73e8>作者：</font>** Itamar Trainin, Renana Keydar, Amit Pinchevski  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Researchers in Holocaust studies have often distinguished between two styles of oral survivor testimony: the USC Shoah Foundation's interviews tend to follow a structured, interviewer-guided format, whereas the Yale Fortunoff Video Archive generally favors a more free-form, open-ended style. This distinction has influenced both scholarly research and the development of later archives. In this study, we critically examine that claim by conducting a large-scale computational analysis of more than 1,600 testimonies from both collections. Leveraging discourse segmentation, topic modeling, and large language model (LLM) based analysis, we quantify the "structuredness" level of testimonies through topic coherence, interviewer-survivor dynamics, and the distribution of question types. Our results generally corroborate the structural differences identified in earlier research, while also revealing significant overlaps between the collections, both within individual interviews and across common narrative patterns. This complicates the simple "structured vs. free-form" dichotomy often applied to these oral histories. Beyond revisiting a foundational claim in Holocaust studies, our work provides a scalable, replicable framework for comparative corpus analysis. As a proof of concept, it suggests broader applications for digital oral history, narrative analysis, and the design of citizen-science annotation platforms.

---


### 16. [Flat-Pack Bench: Evaluating Spatio-Temporal Understanding in Large Vision-Language Models through Furniture Assembly](https://arxiv.org/abs/2605.21625)

**<font color=#1a73e8>作者：</font>** Aditya Chetan, Eric Cai, Peeyush Kushwaha 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The emergence of Large Vision-Language Models (LVLMs) has significantly advanced video understanding capabilities. However, existing benchmarks focus predominantly on coarse-grained tasks such as action segmentation, classification, captioning, and retrieval. Furthermore, these benchmarks often rely on entities that can be easily identified verbally, like household objects, animals, human subjects, etc., limiting their applicability to complex, in-the-wild video scenarios. But, many applications such as furniture assembly, cooking, etc., require step-by-step fine-grained spatio-temporal understanding of the video, which is not sufficiently evaluated in current benchmarks. To address this gap, we introduce Flat-Pack Bench, a novel benchmark centered on furniture assembly tasks. Our benchmark evaluates LVLMs on nuanced tasks, including temporal ordering of assembly actions, temporal localization of assembly state, understanding part mating, and tracking, using multiple-choice questions paired with visual prompts highlighting relevant parts as references for fine-grained questions. Our experiments reveal that state-of-the-art LVLMs struggle significantly with fine-grained spatio-temporal reasoning, highlighting their limitations in effectively leveraging temporal information from videos, limited tracking ability, and understanding of spatial interactions like physical contact.

---


### 17. [Ablate-to-Validate: Are Vision-Language Models Really Using Continuous Thought Tokens?](https://arxiv.org/abs/2605.21642)

**<font color=#1a73e8>作者：</font>** Tianyi Zhang, Mahtab Bigverdi, Ranjay Krishna  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly augmented with continuous or latent non-textual tokens intended to support "visual thinking." Despite improved task accuracy, this alone does not show that models actually use these tokens for reasoning -- gains may arise from confounds such as added context length, special-token anchoring, or training-time regularization. We formalize a diagnostic principle, Ablate-to-Validate, for testing whether latent-token content is genuinely utilized, and instantiate it as the Token Replacement Test (TRT), a standardized suite of content-replacement ablations. TRT holds the prompt, image, token budget, and decoding fixed while replacing intermediate tokens with zero, random, first-repeat, or oracle alternatives, isolating whether performance depends on token content or merely on token presence. As a controlled testbed, we study relative depth reasoning with LLaVA-13B and Qwen2.5-VL-3B, training models to predict and consume continuous or discrete depth spans across multiple frozen encoders (SigLIP2, CLIP, DINOv2) and token budgets. We additionally apply TRT to three off-the-shelf visual-thinking systems (Mirage, Mull-Tokens, CoVT) on BLINK, VSP, and CV-Bench. Across all settings, accuracy gains are a misleading proxy for latent-token reasoning: VLMs retain most improvement even when token content is corrupted or replaced, revealing a persistent gap between having a latent channel and using it as an information bottleneck. We recommend TRT as a standard diagnostic alongside accuracy for any method introducing continuous thought tokens.

---


### 18. [AOP-Wiki EMOD 3.0: Data Model Expansions and Content Evaluation Framework for Using Agentic AI to Improve Integration between AOPs and New Approach Methodologies (NAMs)](https://arxiv.org/abs/2605.21645)

**<font color=#1a73e8>作者：</font>** Virginia K. Hench, J. Harry Caufield, Sierra A.T. Moxon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adverse Outcome Pathways (AOP) are logic models that causally link biological mechanisms that can be measured in a lab to adverse outcomes, relevant to chemical regulatory endpoints. AOPs contextualize new approach methodologies (NAMs), in vitro and in silico methods used as alternatives to animal testing and the sequential events in an AOP serve as multi-scale models spanning biological scales. The AOP-Wiki serves as the global repository for AOPs. While the AOP-Wiki has played a central role in AOP expansion over the past decade, constraints within the current data model and application infrastructure limit the AOP-Wiki from supporting continued AOP growth and evolution. Yet, the transformative power of agentic AI has re-invigorated AOP-Wiki data modernization efforts at a time when core AOP principles can be harnessed to inform use of AI for aggregating and structuring AOP-relevant information. Seizing upon this momentum, we present AOP-Wiki EMOD 3.0, the third in a series of evidence model prototypes, which concretely demonstrates data model expansions and our vision for how the AOP-Wiki might be transformed to better serve regulatory science and emergent use of AOPs in biomedical and One Health contexts. We aim to lay a foundation to support computationally-generated AOPs and quantitative AOPs (qAOPs) by focussing on solutions for AOP-Wiki internal quality improvement, evidence structuring to enhance AOP FAIRness and AI-readiness, and improved integration between the AOP framework and NAMs to better serve next generation risk assessment.

---


### 19. [Value-Gradient Hypothesis of RL for LLMs](https://arxiv.org/abs/2605.21654)

**<font color=#1a73e8>作者：</font>** Arip Asadulaev, Daniil Ognev, Karim Salta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning substantially improves pretrained language models, but it remains understudied why critic-free methods such as PPO and GRPO work as well as they do, and when they should provide the largest gains. We develop a value-gradient perspective of critic-free RL for LLM post-training. First, under a differentiable rollout and additive-noise parameterization, we show that the actor update is value-gradient-like in expectation: the backward pass propagates costates whose conditional expectation equals the value gradient. Second, for discrete transformer policies, we show that autodifferentiation through attention produces empirical costates that approximate this value signal, with an error controlled by the sampling gap and policy entropy. These results motivate a decomposition of RL impact into value gradient signal and reachable reward headroom, yielding a criterion for when RL should be most effective along a pretraining trajectory.

---


### 20. [Investigating Concept Alignment Using Implausible Category Members](https://arxiv.org/abs/2605.21683)

**<font color=#1a73e8>作者：</font>** Sunayana Rane, Brenden M. Lake, Thomas L. Griffiths  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Developing AI systems with a human-like understanding of everyday concepts is a key step towards developing safe, reliable systems whose behavior makes sense to humans. When probing concept understanding, asking questions about plausible category members (e.g., "Is a car a vehicle?") is likely to recall patterns in the model's vast training data. We pursue an alternative strategy, characterizing the boundaries of conceptual categories by asking about implausible category members (e.g., "Is an olive a vehicle?") to probe the kind of concept-level knowledge we take for granted in fellow humans. We characterize concept boundaries for a set of fundamental concepts by studying AI systems' assignments of objects to superordinate categories from a classic psychological study by Rosch and Mervis, as well as their assignments of the same objects to mismatched superordinate categories. We compare these assignments to those made by human participants on the full range of within-category and cross-category assignment tasks. Our results reveal a range of concepts for which which models differ in meaningful and surprising ways from humans, including treating "words" as belonging to categories like "vehicles" and "clothing," identifying several "vegetable" category members as "fruit," and assigning exemplars from non-weapon categories to the "weapons" category. We also demonstrate how these instances of concept misalignment translate into problematic downstream behavior with implications for AI safety.

---


### 21. [X-Token: Projection-Guided Cross-Tokenizer Knowledge Distillation](https://arxiv.org/abs/2605.21699)

**<font color=#1a73e8>作者：</font>** Sharath Turuvekere Sreenivas, Adithyakrishna Venkatesh Hanasoge, Mingyu Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-tokenizer knowledge distillation allows a student model to learn from teachers with incompatible vocabularies. Prior work operates on hidden states or logits; the latter is preferred as a drop-in replacement requiring no auxiliary components. Logit-based methods either use only the correct-token probability, missing the full 'dark knowledge' in the teacher's distribution, or operate on the full output distribution, relying on strict token partitioning and/or unprincipled heuristic ranking. We identify two key shortcomings of full-distribution, logit-based methods: (i) an uncommon-token failure, where critical tokens fall into the unmatched subset (e.g., Llama's 1100 multi-digit numerals under digit-splitting Qwen supervision) and are suppressed during training, reducing GSM8k from 12.89 to 2.56 compared to same-tokenizer KD from a weaker teacher; and (ii) over-conservative matching, where strict 1-to-1 matching excludes near-equivalent tokens across surface forms. These failures require distinct remedies: eliminating the partition when critical tokens are misaligned, and refining it when alignment is reliable. We propose X-Token, an approach with two complementary loss formulations targeting these issues. P-KL removes partitioning and aligns the student's distribution with the teacher's via a sparse projection matrix W (initialized from tokenizer-level string rules) to address the uncommon-token failure. H-KL retains the hybrid form while relaxing matching to align each student token with its top-ranked teacher mapping under W. Both objectives share W and extend naturally to multiple teachers. Empirically, on Llama-3.2-1B, X-Token outperforms the current state of the art GOLD by +3.82 average points with a Qwen3-4B teacher and by +0.5 with a Phi-4-Mini teacher. Further, a two-teacher setup (Phi-4-mini + Llama-3B) improves over single-teacher distillation by +1.3 points.

---


### 22. [Latent-space Attacks for Refusal Evasion in Language Models](https://arxiv.org/abs/2605.21706)

**<font color=#1a73e8>作者：</font>** Giorgio Piras, Raffaele Mura, Fabio Brau 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety-aligned language models are trained to refuse harmful requests, yet refusal behavior can be suppressed by steering their internal representations. Existing methods do so by ablating a refusal direction from model activations, aiming to remove refusal from the model's residual stream. Despite their empirical success, these methods lack a principled account of the latent-space transformation they induce and why it suppresses refusal. In this work, we recast refusal suppression as a latent-space evasion attack against linear probes trained to separate refused from answered prompts. Under this view, prior work's difference-in-means direction naturally defines such a probe, and its ablation is exactly a projection onto its decision boundary, i.e., a minimum-confidence evasion attack. This perspective not only explains the empirical success of prior work but also admits a key limitation: evasion stops at the decision boundary, motivating the need to push representations further into the compliant region, i.e., where the model answers. We leverage this by proposing a Controlled Latent-space Evasion attack that projects representations past the boundary with an optimized confidence. We achieve state-of-the-art attack success rate across 15 instruction-tuned, multimodal, and reasoning models, outperforming existing refusal-ablation baselines and specialized jailbreak attacks.

---


### 23. [Probabilistic Attribution For Large Language Models](https://arxiv.org/abs/2605.21726)

**<font color=#1a73e8>作者：</font>** Shilpika Shilpika, Carlo Graziani, Bethany Lusch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The generative nature of Large Language Models (LLMs) is reflected in the conditional probabilities they compute to sample each response token given the previous tokens. These probabilities encode the distributional structure that the model learns in training and exploits in inference. In this work, we use these probabilities to situate LLMs within the mathematical theory of stochastic processes. We use this framework to design a model-agnostic probabilistic token attribution measure, using Bayes rule to invert the next-token log-probabilities so as to capture the models internal representation of the distribution over token sequences. The representation is independent of the models computational structure. This representation yields the conditional probability of the response given the prompt, and of the response given the prompt with a token marginalized away. Our attribution score is the log of the ratio of these probabilities. We further compute the entropies of a single prompts token distributions, conditioned on the remaining context. The interplay between entropy and attribution score sheds light on LLM behavior. We evaluate 8 models across 7 prompts and investigate anomalies, token sensitivity, response stability, model stability, and training convergence, thereby improving interpretability and guiding users to focus on uncertain or unstable parts of the generation.

---


### 24. [BEiTScore: Reference-free Image Captioning Evaluation with an Efficient Cross-Encoder Model](https://arxiv.org/abs/2605.21728)

**<font color=#1a73e8>作者：</font>** Gonçalo Gomes, Bruno Martins, Chrysoula Zerva  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image captioning evaluation remains a significant challenge, as vision-language models evolve toward more challenging capabilities such as generating long-form and context-rich descriptions. State-of-the-art evaluation metrics involve extensive computational costs associated with the use of Large Language Models (LLMs) as judges, or instead suffer from the limitations of standard CLIP-based encoders, such as strict token limits, lack of fine-grained sensitivity, or lack of compositional generalization by treating captions as ``bags-of-words.'' We propose a new learned metric that tackles the aforementioned challenges, based on a lightweight cross-encoder that is initialized from a visual question-answering model checkpoint, balancing a strong weight initialization with computational efficiency. Our training scheme uses a carefully assembled data mixture for supervised learning, featuring adversarial LLM-based data augmentations to enhance model sensitivity to fine-grained visual-linguistic errors. We also introduce a new benchmark designed to assess detailed captioning evaluation across diverse scenarios. Experimental results demonstrate that the proposed metric achieves state-of-the-art performance while maintaining the efficiency required for large-scale benchmarking, quality-aware decoding, or reward guidance.

---


### 25. [AttuneBench: A Conversation-Based Benchmark for LLM Emotional Intelligence](https://arxiv.org/abs/2605.21739)

**<font color=#1a73e8>作者：</font>** Kate M. Lubrano, Faisal Sayed, Ankita Rathod 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emotional intelligence (EI), the ability to perceive, understand, and respond appropriately to others' emotional states, is central to human communication, and increasingly important to assess as LLMs assume conversational roles in everyday life. Existing EI benchmarks rely on synthetic prompts, single-turn cases, or third-party annotation. These approaches do not directly measure how models infer and respond to a participant's emotional state over the course of a real conversation. We introduce AttuneBench, a benchmark grounded in 200 genuine multi-turn human-model conversations in which participants conversed with anonymized LLMs and provided turn-by-turn annotations of their emotional state, the model's behavior, and their preferred responses. Across 11 evaluated models, we find that model rankings on emotion recognition, behavioral classification, preference prediction, and judged response quality are largely independent, indicating that emotionally intelligent behavior decomposes into separable capabilities. Preference alignment and response-quality judgments are substantially more model-discriminating than emotion-label accuracy. These results indicate that emotionally intelligent behavior requires predicting what kind of response a specific user wants in context, a distinction that aggregate scoring can obscure and that single-turn or synthetic formats cannot directly capture across turns. AttuneBench provides a framework for assessing each of these capabilities and for diagnosing model-specific strengths and failure modes in emotionally salient conversation.

---


### 26. [SMDD-Bench: Can LLMs Solve Real-World Small Molecule Drug Design Tasks?](https://arxiv.org/abs/2605.21740)

**<font color=#1a73e8>作者：</font>** Kevin Han, Renfei Zhang, Kathy Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents have incredible potential for scientific discovery applications. However, the performance of LLM agents on real-world, small molecule drug design (SMDD) tasks across diverse chemistries and targets is unclear. Current evaluation methods are either ad hoc, too simple for real-world discovery, limited in scale, or restricted to single-turn question answering. In effort to standardize the evaluation of LLM agents on small molecule design, we introduce SMDD-Bench, a challenging, multi-turn, long-horizon agentic benchmark consisting of 502 guaranteed-solvable task instances spanning 5 task types: 2D Pharmacophore Identification, Interaction Point Discovery, Scaffold Hopping, Lead Optimization, and Fragment Assembly. SMDD-Bench tasks span a wide region of chemical space and involve 102 unique protein targets. Completely solving the benchmark would require having strong chemical and biological reasoning and 3D intuition, understanding specialized tool use, and displaying planning expertise over a limited number of oracle calls. We benchmark 7 frontier open and closed source LLMs and find even the most performant LLM, GPT5.4, solves only 40.2\% of tasks. We hope SMDD-Bench provides a standardized testbed to invigorate the field towards training and evaluating LLM agents for fully autonomous computational drug design. We host a public leaderboard at this http URL .

---


### 27. [Improving 3D Labeling in Self-Driving by Inferring Vehicle Information using Vision Language Models](https://arxiv.org/abs/2605.21747)

**<font color=#1a73e8>作者：</font>** Steven Chen, Shivesh Khaitan, Nemanja Djuric  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present an approach to improve 3D vehicle labeling in self-driving applications through zero-shot inference of vehicle information, leveraging Vehicle Make and Model Recognition (VMMR) methods. The proposed approach utilizes a Vision Language Model (VLM) to both infer a vehicle's make, model, and generation from image crops, and output accurate 3D bounding box dimensions to seed manual labeling. We evaluate the impact of iterative prompt engineering and the choice of different VLMs on both vehicle bounding box inference and make/model/generation recognition. When compared to strong baselines, the proposed approach not only shows high accuracy, but also excels in mitigating specific failure modes where VLMs provide better dimensions than initial lidar-aided human annotated labels (e.g., in cases of significant vehicle occlusion). Experiments on both public and proprietary data strongly suggest that our conclusions are generalizable across different labelers and datasets. The results demonstrate that integrating VLMs into the labeling process can reduce manual labeling time while increasing label quality.

---


### 28. [RankJudge: A Multi-Turn LLM-as-a-Judge Synthetic Benchmark Generator](https://arxiv.org/abs/2605.21748)

**<font color=#1a73e8>作者：</font>** Zhenwei Tang, Zhaoyan Liu, Rasa Hosseinzadeh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As interactive LLM-based applications are created and refined, model developers need to evaluate the quality of generated text along many possible axes. For simpler systems, human evaluation may be practical, but in complicated systems like conversational chatbots, the amount of generated text can overwhelm human annotation resources. Model developers have begun to rely heavily on auto-evaluation, where LLMs are also used to judge generation quality. However, existing LLM-as-a-judge benchmarks largely focus on simple Q\&A tasks that do not match the complexity of multi-turn conversations. We introduce RankJudge, a benchmark generator for evaluating LLM-as-a-judge on multi-turn conversations grounded in reference documents. RankJudge creates pairs of conversations where one conversation has a single flaw injected into one turn. This construction allows paired conversations to be labeled unambiguously as better or worse, and precisely isolates failure categories to individual turns, enabling a strict joint correctness criterion for judging. We implement RankJudge across the domains of machine learning, biomedicine, and finance, evaluate 21 frontier LLM judges, and rank those judges via the Bradley-Terry model. Our formulation also allows ranking each conversation pair with difficulty ratings, which we use to dynamically curate the evaluation slice to reduce label noise, as confirmed via human annotation. We find that judge rankings are stable under partial observability, coarser correctness criteria, and an alternative random-walk rating algorithm.

---


### 29. [Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents](https://arxiv.org/abs/2605.21768)

**<font color=#1a73e8>作者：</font>** Sikuan Yan, Ahmed Bahloul, Ercong Nie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Memory-augmented LLM agents enable interactions that extend beyond finite context windows by storing, updating, and reusing information across sessions. However, training such agents with reinforcement learning in multi-session environments is challenging because memory turns the agent's past actions into part of its future environment. Once different rollouts write, update, or delete different memories, they no longer share the same intermediate memory state, making trajectory-level comparisons fundamentally unfair. This violates a key assumption behind group-relative methods such as GRPO, where rollouts are compared as if they were sampled from the same effective environment. Consequently, trajectory-level rewards provide noisy or biased credit signals for long-horizon memory operations. To address this challenge, we introduce Memory-R2, a training framework for long-horizon memory-augmented LLM agents. Its core algorithm, LoGo-GRPO, combines local and global group-relative optimization. The global objective preserves end-to-end learning from long-horizon trajectory-level rewards, while local rerollouts compare different memory-operation outcomes from the same intermediate memory state, yielding fairer group comparisons and more precise supervision for memory construction. Beyond credit assignment, Memory-R2 jointly optimizes memory formation and memory evolution with a shared-parameter co-learning design, where a fact extractor and a memory manager are instantiated from the same LLM backbone through role-specific prompts. To stabilize multi-step RL over long memory horizons, we adopt a progressive curriculum that increases the training horizon from 8 to 16 to 32 sessions. Together, these components provide an effective training paradigm for memory-augmented LLM agents in long-horizon multi-session settings.

---


### 30. [PromptNCE: Pointwise Mutual Information Predictions Using Only LLMs and Contrastive Estimation Prompts](https://arxiv.org/abs/2605.21776)

**<font color=#1a73e8>作者：</font>** Juliette Woodrow, Chris Piech  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Estimating mutual information from text usually requires training a task-specific critic, which limits its use in low-data settings. We ask whether large language models can instead estimate pointwise mutual information zero-shot, using only prompts and elicited probabilities. We introduce a benchmark with human-derived ground-truth PMI across three publicly available datasets, and evaluate five information-theoretic prompting-based estimators. Our main method, PromptNCE, frames conditional probability estimation as a contrastive task and augments the candidate set with an explicit OTHER category. We show theoretically that adding OTHER recovers the true conditional P(y | x) rather than just a ranking over listed candidates, turning a contrastive prompt into a general-purpose zero-shot probability estimator. PromptNCE is the best zero-shot method on all three datasets, reaching Spearman correlation up to 0.82 with human-derived PMI. We also present a case study in computer science education showing how these estimators can be used to score student knowledge summaries in a low-data setting.

---


### 31. [What Counts as AI Sycophancy? A Taxonomy and Expert Survey of a Fragmented Construct](https://arxiv.org/abs/2605.21778)

**<font color=#1a73e8>作者：</font>** Meryl Ye, Lujain Ibrahim, Jessica Y. Bo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI sycophancy has become a prominent concern in large language model (LLM) research. Yet the term lacks a consistent definition and has been applied to behaviors ranging from agreeing with a user's false claim to excessively praising the user to withholding corrective feedback. When researchers, companies, and policymakers use the same term to describe different behaviors, evaluation results become difficult to compare, mitigation strategies fail to transfer, and systems that are resistant to one form of sycophancy continue exhibiting other forms. To address this, we make two contributions. First, we reviewed 70 papers on AI sycophancy to develop a taxonomy of how the behavior has been defined and measured. The taxonomy distinguishes (1) whether a model is sycophantic toward a user's positions and beliefs, or toward the user's broader personal traits and emotions, and (2) whether this occurs through explicit, direct language or more implicit, subtle behaviors such as framing, omission, or tone. Mapping existing literature to our taxonomy reveals that current research has focused on overt forms of sycophancy toward users' beliefs, leaving more subtle and person-directed behaviors relatively understudied. Second, we surveyed 106 experts in AI sycophancy and related fields to examine whether researchers agree on which model behaviors are sycophantic. While experts are nearly unanimous in believing that sycophancy is a significant problem in current AI systems (94.3% agree), they disagree substantially on which specific behaviors qualify. Together, these findings demonstrate that AI sycophancy is a broad family of behaviors with different measurement challenges, intervention requirements, and governance implications. Our taxonomy provides a shared vocabulary for understanding and addressing these behaviors.

---


### 32. [Reflective Prompt Tuning through Language Model Function-Calling](https://arxiv.org/abs/2605.21781)

**<font color=#1a73e8>作者：</font>** Farima Fatahi Bayat, Moin Aminnaseri, Pouya Pezeshkpour 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have become increasingly capable of following instructions and complex reasoning, making prompting a flexible interface for adapting models without parameter updates. Yet prompt design remains labor-intensive and highly sensitive to formatting, phrasing, and instruction order, motivating automated prompt optimization methods that reduce manual effort while preserving inference-time flexibility. However, existing methods often search over prompt candidates or use fixed critique-refine pipelines driven by individual examples or small batches, limiting their ability to capture systematic error patterns and make targeted edits grounded in failure history. We propose Reflective Prompt Tuning (RPT), a framework that uses LLM function calling to simulate the iterative workflow of human prompt engineers. An LLM optimizer calls a diagnostic function that evaluates the target model over an entire optimization set, summarizes recurring failure modes, and returns a structured diagnostic report. The optimizer uses this report, together with an accumulated memory of prior reports, to revise the prompt for the next iteration. RPT further supports confidence-aware optimization by using calibration signals in diagnostic feedback and final prompt selection. Across three reasoning tasks, RPT improves over initial prompts by up to 12.9 points, remains competitive with state of the art, and improves confidence calibration. Our analyses show that RPT is especially effective on multi-hop and mathematical reasoning, producing targeted prompt revisions that align with diagnosed failure patterns and lead to gains in task performance and calibration.

---


### 33. [MM-Conv: A Multimodal Dataset and Benchmark for Context-Aware Grounding in 3D Dialogue](https://arxiv.org/abs/2605.21796)

**<font color=#1a73e8>作者：</font>** Anna Deichler, Jim O'Regan, Fethiye Irmak Dogan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grounding language in the physical world requires AI systems to interpret references that emerge dynamically during conversation. While current vision-language models (VLMs) excel at static image tasks, they struggle to resolve ambiguous expressions in spontaneous, multi-turn dialogue. We address this gap by introducing (1) a benchmark for referential communication in dynamic 3D environments, built from 6.7 hours of egocentric VR interaction with synchronized speech, motion, gaze, and 3D scene geometry, and (2) a two-stage grounding pipeline that explicitly resolves conversational ambiguity before visual localization. The benchmark includes over 4,200 manually verified referring expressions spanning full, partitive, and pronominal types. Our contextual rewriting approach improves grounding performance by 11-22 percentage points on average, with a pure detector (GroundingDINO) reaching 56.7% on pronominals after rewriting, nearly double the best end-to-end baseline. Results demonstrate that decoupling linguistic reasoning from visual perception is more effective than end-to-end approaches for conversational grounding.

---


### 34. [stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation](https://arxiv.org/abs/2605.21800)

**<font color=#1a73e8>作者：</font>** Lucas Maes, Quentin Le Lidec, Luiz Facury 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models are central to building agents that can reason, plan, and generalize beyond their training data. However, research on world models is currently fragmented, with disparate codebases, data pipelines, and evaluation protocols hindering reproducibility and fair comparison. Current practice is further limited by three key bottlenecks: fragile one-off codebases, slow video data loading, and the lack of standardized generalization benchmarks. We present stable-worldmodel (swm), an open-source platform for standardized and reproducible world modeling research and evaluation. It delivers (1) a high-performance Lance-based data layer with native support and conversion tools for MP4, HDF5, and LeRobot datasets, (2) clean, well-tested implementations of modern world model baselines and planning solvers, and (3) a broad suite of environments and tasks extended with controllable visual, geometric, and physical factors of variation for systematic in-silico evaluation of dynamics understanding, control performance, representation quality, and out-of-distribution generalization. By unifying the full pipeline under a single, scalable framework, \texttt{swm} dramatically reduces research overhead and accelerates trustworthy progress toward reliable world models.

---


### 35. [Why Semantic Entropy Fails: Geometry-Aware and Calibrated Uncertainty for Policy Optimization](https://arxiv.org/abs/2605.21801)

**<font color=#1a73e8>作者：</font>** Zheyuan Zhang, Kaiwen Shi, Han Bao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training has become central to improving reasoning and alignment in large language models, where critic-free models enable scalable learning from model-generated outputs but lack principled mechanisms to distinguish informative from noisy signals. Recent approaches leverage response-level measures as uncertainty signals to regulate group-based optimization methods such as GRPO. Yet their empirical success remains unstable and unclear in how they influence optimization dynamics. In this paper, we provide, to our knowledge, the first principled formulation that interprets uncertainty signals as mechanisms for characterizing and regulating gradient variance and learning signal quality. Based on both empirical and theoretical analysis, we identify two critical gaps of current entropy-based estimators: The anisotropic gap and The calibration gap. Motivated by this analysis, we propose Geometric-aware Calibrated Policy Optimization (GCPO), a novel framework integrating geometry-aware measures to capture semantic disagreement with reward-based calibration to align uncertainty with learning signal strength. Experiments on multiple benchmarks show that our approach more faithfully tracks gradient variability and consistently improves post-training performance. Our results highlight the importance of designing uncertainty signals that are aligned with optimization dynamics, offering a principled perspective for robust post-training.

---


### 36. [When Cases Get Rare: A Retrieval Benchmark for Off-Guideline Clinical Question Answering](https://arxiv.org/abs/2605.21807)

**<font color=#1a73e8>作者：</font>** Doeun Lee, Muge Zhang, Yi Yu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Across medical specialties, clinical practice is anchored in evidence-based guidelines that codify best studied diagnostic and treatment pathways. These pathways routinely fall short for the long tail of real-world care not covered by guidelines. Most medical large language models (LLMs), however, are trained to encode common, guideline-focused medical knowledge in their parameters. Current evaluations test models primarily on recalling and reasoning with this memorized content, often in multiple-choice settings. Given the fundamental importance of evidence-based reasoning in medicine, it is neither feasible nor reliable to depend on memorization in practice. To address this gap, we introduce OGCaReBench, a free-form retrieval-focused benchmark aimed at evaluating LLMs at answering clinical questions that require going beyond typical guidelines. Extracted from published medical case reports and validated by medical experts, OGCaReBench contains long-form clinical questions requiring free-text answers, providing a systematic framework for assessing open-ended medical reasoning in rare, case-based scenarios. Our experiments reveal that even the best-performing baseline (GPT-5.2) correctly answers only 56% of our benchmark with specialized models only reaching 42%. Augmenting models with retrieved medical articles improves this performance to up to 82% (using GPT-5.2) highlighting the importance of evidence-grounding for real-world medical reasoning tasks. This work thus establishes a foundation for benchmarking and advancing both general-purpose and medical LLMs to produce reliable answers in challenging clinical contexts.

---


### 37. [Implicit Safety Alignment from Crowd Preferences](https://arxiv.org/abs/2605.21822)

**<font color=#1a73e8>作者：</font>** Qian Lin, Daniel S. Brown  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Human Feedback (RLHF) can reveal implicit objectives such as safety considerations that go beyond task completion. In this work, we focus on the common safety criteria embedded in crowd preference datasets, where different users may express distinct preferences or objectives, yet follow similar safety principles. Our aim is to discover shared safety criteria from crowd preferences and then transfer them to downstream RL tasks to regularize agent behavior and enforce safety. We first show that direct reward combination-optimizing a preference-learned reward model together with downstream task rewards-has inherent limitations. Motivated by this, we propose Safe Crowd Preference-based RL, a hierarchical framework that extracts safety-aligned skills from crowd preferences and composes them via a high-level policy to safely solve downstream tasks. Experiments across safe RL environments and a preliminary LLM-style task with diverse user goals and shared safety constraints demonstrate that our approach substantially lowers safety costs without access to explicit safety rewards, while achieving task performance comparable to oracle methods trained with ground-truth safety signals.

---


### 38. [Does Slightly Mean Somewhat? Measuring Vague Intensity Words in LLM Numeric Actions](https://arxiv.org/abs/2605.21827)

**<font color=#1a73e8>作者：</font>** Daniel Tabach  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Do language models preserve the ordinal meaning of intensity words when those words must produce numeric actions? I study a researcher-constructed scale of 10 English degree modifiers, from slightly to drastically, informed by the Quirk et al. degree-modifier taxonomy, in a controlled resource-allocation environment where Claude Haiku receives a natural-language instruction, produces a numeric allocation, and a deterministic backend converts that allocation into a measurable outcome. The only variable that changes between runs is the intensity word or the starting system state, isolating their effects on the model's numeric output.
Across 6,620 runs at T=0.0 and T=0.7, three patterns emerge. First, the model compresses 10 intensity words into 5 distinct median outputs: four lower-tier words all map to the same value, while stronger words break into higher regimes (Spearman rho = 0.845, p < 0.001). Second, when the current system state is supplied as context, separate Kruskal-Wallis tests show that grouping by starting allocation captures far more rank-based variance than grouping by word (epsilon-squared baseline = 0.782 vs. epsilon-squared word = 0.079), and lexical differentiation collapses to zero as the system approaches capacity. Third, near feasibility limits the model exhibits three behavioral modes: weak words hedge with small adjustments, strong words abstain entirely, and the word drastically pushes to the local ceiling. These patterns persist across temperature, with stochastic sampling broadening distributions but not restoring ordinal distinctions between words. In this model and domain, the model's numeric interpretation of vague intensity words is compressed, state-dependent, and discontinuous near operational boundaries.

---


### 39. [FLUID: From Ephemeral IDs to Multimodal Semantic Codes for Industrial-Scale Livestreaming Recommendation](https://arxiv.org/abs/2605.21832)

**<font color=#1a73e8>作者：</font>** Xinhang Yuan, Zexi Huang, Anjia Cao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern recommender systems rely heavily on ID-based collaborative filtering: each item is represented by a unique ID embedding that accumulates collaborative signals from user interactions. Livestreaming recommendation, however, faces a unique challenge in this paradigm: a live room typically broadcasts for only tens of minutes, so its item ID remains poorly learned in a persistent cold-start state and ID-centric ranking models fail to generalize. We present FLUID, the first framework to fully retire the candidate-side item ID from a production-scale livestreaming ranker. FLUID couples a cross-domain multimodal encoder, jointly trained on short videos and livestreams to produce discrete hierarchical codes (LUCID), with a late-fusion, ID-free design that injects slice-level and room-level LUCID as independent tokens, stabilized by a staged warmup under online incremental training. Deployed on our industrial livestreaming recommenders with a cross-platform combined user base of over one billion globally, FLUID delivers significant online gains of +0.55% Quality Watch Duration, +2.05% Cold-Start Room Views, and +0.05% Active Hours.

---


### 40. [On-Policy Consistency Training Improves LLM Safety with Minimal Capability Degradation](https://arxiv.org/abs/2605.21834)

**<font color=#1a73e8>作者：</font>** Andy Han, Kristina Fujimoto, Avidan Shah 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aligned models can misbehave in several ways: they are often sycophantic, fall victim to jailbreaks, or fail to include appropriate safety warnings. Consistency training is a promising new alignment paradigm to mitigate such failures by training invariants into the model using contrastive input pairs. Existing consistency training procedures generate the supervision signal once, offline, and use supervised fine-tuning (SFT) to update the model. Unfortunately, the resulting models tend to merely memorize the surface forms of the training distribution and thus generalize poorly and regress in their capabilities. We introduce On-Policy Consistency Training (OPCT), a new consistency training approach where the objective is computed over the model's own responses to prompts, supervised by itself conditioned on corresponding contrastive prompts. We evaluate OPCT on three safety axes: sycophancy, jailbreaking, and safety awareness. Across three model families, OPCT outperforms its SFT counterpart on all safety desiderata. It nearly halves the sycophancy rate relative to baseline (8.1% vs. 15.4%, compared to 11.2% for SFT). Under an adaptive per-target attacker, OPCT holds jailbreak defense success near 99% on held-out jailbreak behaviors, whereas SFT achieves 87% on average. On safety awareness, OPCT outperforms SFT in two out of three models, and matches it on the other. OPCT also largely avoids the capability regressions that SFT induces, such as a 28-point drop on MATH-500. Our results suggest that consistency training is best implemented as OPCT rather than as SFT, especially when generalization beyond the training distribution is desired.

---


### 41. [Comparing LLM and Fine-Tuned Model Performance on NVDRS Circumstance Extraction with Varying Prompt Complexity](https://arxiv.org/abs/2605.21845)

**<font color=#1a73e8>作者：</font>** Geoffrey Martin, Xuan Zhong Feng, Yifan Peng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Suicide is a leading cause of death in the United States, and understanding the circumstances that precede it requires extracting structured information from death investigation narratives. Many of these circumstances require semantic inference beyond simple keyword matching. We develop a ``Complexity Score'' algorithm that analyzes coding manual structure to predict when detailed prompts with full coding guidelines improve over name-only prompts. We then construct a hybrid approach that selects prompt strategy per circumstance. We evaluate large language models (LLMs) against fine-tuned RoBERTa on 25 inferentially complex circumstances from the National Violent Death Reporting System (NVDRS). We found that LLMs substantially outperform on low-prevalence circumstances where training data is insufficient. We further demonstrate that our framework generalizes across frontier LLMs, with GPT-5.2, Gemini 2.5 Pro and Llama-3 70B showing consistent performance patterns. These findings support a hybrid architecture where LLMs handle rare, inferentially complex circumstances while fine-tuned models handle common ones.

---


### 42. [ACC: Compiling Agent Trajectories for Long-Context Training](https://arxiv.org/abs/2605.21850)

**<font color=#1a73e8>作者：</font>** Qisheng Su, Zhen Fang, Shiting Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent development of agents has renewed demand for long-context reasoning capacity of LLMs. However, training LLMs for this capacity requires costly long-document curation or heuristic context synthesis. We observe that agents produce massive trajectories when solving problems, invoking tools and receiving environment observations across many turns. The evidence needed to answer the original question is thus scattered throughout these turns, requiring integration of distant context segments. Nevertheless, standard agent SFT masks tool responses and only trains turn-level tool selection, creating a supervision blind spot where these scattered signals go unused. We propose Agent Context Compilation (ACC), which converts trajectories from search, software engineering, and database querying agents into long-context QA pairs that combine the original question with tool responses and environment observations gathered across multiple turns, training the model to answer directly without tool use. This makes the dependencies between the question and the evidence explicit, enabling direct supervision of long-context reasoning over distant segments without additional annotation. ACC is a simple but effective approach that can be combined with any existing long-context extension or training method, providing scalable supervised fine-tuning data. We validate ACC on long-range dependency modeling tasks through MRCR and GraphWalks, challenging benchmarks requiring cross-turn coreference resolution and graph traversal over extended contexts. Training Qwen3-30B-A3B with ACC achieves 68.3 on MRCR (+18.1) and 77.5 on GraphWalks (+7.6), results comparable to Qwen3-235B-A22B, while preserving general capabilities on GPQA, MMLU-Pro, AIME, and IFEval. Further mechanism analysis reveals that the ACC-trained model exhibits task-adaptive attention restructuring and expert specialization.

---


### 43. [OPPO: Bayesian Value Recursion for Token-Level Credit Assignment in LLM Reasoning](https://arxiv.org/abs/2605.21851)

**<font color=#1a73e8>作者：</font>** Yu Li, Rui Miao, Tian Lan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards has become the standard recipe for improving LLM reasoning, but the dominant algorithm GRPO assigns a single trajectory-level advantage to every token, diluting the signal at pivotal reasoning steps and injecting noise at uninformative ones. Critic-free alternatives derived from on-policy distillation supply per-token signals through oracle-conditioned likelihood ratios, yet apply each signal in isolation from the trajectory-level evidence accumulated up to that position. We propose Oracle-Prompted Policy Optimization (OPPO), which rests on a single observation: the oracle signal used by prior distillation-style methods for local discrimination is also the natural Bayesian update of the model's belief about eventual success. Accumulating the signal along a trajectory yields, in closed form and at the cost of one extra forward pass, a running estimate of the success probability at every position, together with a token-level advantage that requires no learned value network and no additional rollouts. A first-order analysis factorizes the advantage into the per-token discrimination signal used by distillation methods modulated by a state weight that concentrates credit on genuinely pivotal tokens, with a directional variance-reduction guarantee. The framework admits two estimators differing only in which model scores the evidence: a \textit{self-oracle} that reuses the student and recovers the on-policy distillation reward as a strict special case, and a \textit{teacher-oracle} that delegates scoring to a stronger frozen model. On two base LLMs across seven mathematics, science, and code reasoning benchmarks, OPPO improves over GRPO, DAPO, and SDPO by up to $+6.0$ points on AMC'23 and $+5.2$ points on AIME'24, with gains that widen monotonically with response length.

---


### 44. [Seizure-Semiology-Suite (S3): A Clinically Multimodal Dataset, Benchmark, and Models for Seizure Semiology Understanding](https://arxiv.org/abs/2605.21852)

**<font color=#1a73e8>作者：</font>** Lina Zhang, Tonmoy Monsoor, Peizheng Li 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) have demonstrated remarkable proficiency in general video understanding, their capacity to interpret involuntary, and spatio-temporally evolving pathologic motor behaviors such as seizure semiology remains largely untested. To address this gap, we introduce Seizure-Semiology-Suite, a clinically grounded dataset and benchmark for fine-grained, structured seizure semiology understanding. The dataset includes 438 seizure videos annotated with over 35,000 dense labels covering 20 ILAE-defined semiological features. Building on this dataset, we propose a seven-task hierarchical benchmark that systematically evaluates MLLMs from low-level visual perception to temporal sequencing, narrative report generation, and seizure diagnosis. To enable clinically meaningful evaluation of generated reports, we further introduce the Report Quality Index for Seizure Semiology (Seizure-RQI). Extensive baselines across 11 open-weight MLLMs reveal systematic weaknesses in laterality reasoning, temporal localization, symptom sequencing, and clinically faithful reporting. We show that seizure-specific fine-tuning substantially improves performance across tasks, and that a two-stage neuro-symbolic framework achieves an F1 score of 0.96 on epileptic versus non-epileptic seizure classification. Seizure-Semiology-Suite establishes a rigorous benchmark for evaluating multimodal models in safety-critical medical video understanding and guides the development of clinically reliable, domain-adaptive multimodal intelligence.

---


### 45. [CrossVLA: Cross-Paradigm Post-Training and Inference Optimization for Vision-Language-Action Models](https://arxiv.org/abs/2605.21854)

**<font color=#1a73e8>作者：</font>** Zhi Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have rapidly converged on a small set of architectural patterns: discrete-token autoregression (e.g. OpenVLA) and continuous-action flow-matching (e.g. pi-0.5). Yet preference alignment via Direct Preference Optimisation (DPO) -- the de-facto post-training step in language models -- has been studied almost exclusively on autoregressive VLAs. We present CrossVLA, an empirical study of cross-paradigm VLA post-training. Three contributions: (i) a surrogate flow-matching log-probability estimator that lets DPO operate on continuous-action backbones without probability-flow ODE integration; (ii) a head-to-head comparison of LoRA and DoRA as the parameter-efficient layer for VLA DPO, finding DoRA improves over OpenVLA SFT by a mean +10.4 pp across LIBERO 4-suite (600 trials, 3 seeds) -- per-suite +20.0 Object, +11.0 Long-horizon, +8.0 Goal, +2.7 Spatial -- with zero seed variance on Object (38/50 on each of 3 seeds); (iii) an inference-time anatomy showing the denoise loop dominates 78.6% of sample_actions latency and prefix-K/V caching a la VLA-Cache caps at a 21% acceleration ceiling -- both chunk-level and token-level cache strategies degrade success rate to 0-80% in our benchmarks. We further pretrain a multi-view + temporal projection head on 6000 LIBERO frames, achieving 99.5% k-NN recall@1 for same-task retrieval (36x over random), available as a downstream initialisation. All code, ckpts, training logs, and reproduction scripts are open at this https URL.

---


### 46. [The Illusion of Reasoning: Exposing Evasive Data Contamination in LLMs via Zero-CoT Truncation](https://arxiv.org/abs/2605.21856)

**<font color=#1a73e8>作者：</font>** Yifan Lan, Yuanpu Cao, Hanyu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated impressive reasoning abilities across a wide range of tasks, but data contamination undermines the objective evaluation of these capabilities. This problem is further exacerbated by malicious model publishers who use evasive, or indirect, contamination strategies, such as paraphrasing benchmark data to evade existing detection methods and artificially boost leaderboard performance. Current approaches struggle to reliably detect such stealthy contamination. In this work, we uncover a critical phenomenon: a model's generated reasoning steps actively mask its underlying memorization. Inspired by this, we propose the Zero-CoT Probe (ZCP), a novel black-box detection method that deliberately truncates the entire Chain-of-Thought (CoT) process to expose latent shortcut mappings. To further isolate memorization from the model's intrinsic problem-solving capabilities, ZCP compares the model's zero-CoT performance on the original benchmark against an isomorphically perturbed reference dataset. Furthermore, we introduce Contamination Confidence, a metric that quantifies both the likelihood and severity of contamination, moving beyond simple binary classifications. Extensive experiments on both previously identified contaminated models and specially fine-tuned contaminated models demonstrate that ZCP robustly detects both direct and evasive data contamination. The code for ZCP is accessible at this https URL.

---


### 47. [Hypergraph as Language](https://arxiv.org/abs/2605.21858)

**<font color=#1a73e8>作者：</font>** Mengqi Lei, Guohuan Xie, Shihui Ying 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have recently shown strong potential in modeling relational structures. However, existing approaches remain fundamentally graph-centric: they focus on processing pairwise graph structures into tokens that LLMs can understand. In contrast, many real-world relational patterns do not naturally conform to the pairwise-edge assumption, and are better modeled as high-order associations in hypergraphs. For hypergraph structures, existing methods often fail to preserve the native semantics that multiple objects are jointly connected by the same high-order relation, limiting their ability to exploit complex structures. To address this limitation, we put forth the "Hypergraph as Language" perspective and propose Hyper-Align, a hypergraph-native alignment framework for large language models. Hyper-Align compiles the query-object-centered hypergraph context into hypergraph tokens directly consumable by a base LLM. Specifically, we introduce Hypergraph Incidence Detail Template with Overview (HIDT-O), which serializes high-order association structures into a fixed-shape hybrid template combining local incidence details and overview-level summaries. We then design a Hypergraph Incidence Projector (HIP), which maps native high-order incidence structures into the LLM token space through explicit semantic-structural decoupling and bidirectional message passing between vertices and hyperedges. We further define a concrete Hypergraph-as-Language input protocol, which jointly feeds hypergraph tokens and textual prompts into a frozen base LLM, supporting both vertex-level and hyperedge-level tasks under a unified question-answering paradigm. To systematically evaluate different methods in hypergraph structural modeling, we introduce HyperAlign-Bench. Extensive experiments show that Hyper-Align significantly outperforms existing methods across in-domain and zero-shot evaluations.

---


### 48. [Learning Emergent Modular Representations in Multi-modality Medical Vision Foundation Models](https://arxiv.org/abs/2605.21861)

**<font color=#1a73e8>作者：</font>** Yuting He, Chenyu You, Shuo Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modality medical vision (MV) foundation models (FM) are fundamentally challenged by pronounced Non-IID feature statistics across heterogeneous imaging modalities. Monolithic self-supervised optimization on such data induces conflicting gradients, driving representations to collapse toward modality-dominant shortcuts. This work reframes this failure as an imbalance between specialization and coordination in emergent modularity, and proposes Director-Experts (DEX), a modular network that explicitly regulates these dynamics in stacked modules. Each DEX module comprises a pool of experts, dynamically adapted by our image-wise activation strategy, autonomously specializing in modality-dominant statistics, together with a director, updated via our group exponential moving average, which distills multi-expert knowledge into a shared space for semantic integration across modalities, thus driving the emergence of modular representations. We curate a new benchmark, Medical Vision Universe, over 4 million images across 10 modalities, which provides a FM-level pre-training with the broadest coverage of distinct imaging modalities to our DEX. Extensive evaluations on 26 downstream tasks demonstrate improved optimization behavior and transferability, indicating DEX as a principled step toward general-purpose multi-modality medical AI. Our code and dataset will be opened at this https URL.

---


### 49. [Two-Stage Multimodal Framework for Emotion Mimicry Intensity Prediction](https://arxiv.org/abs/2605.21869)

**<font color=#1a73e8>作者：</font>** Dinithi Dissanayake, Shaveen Silva, Ovindu Atukorala 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present our submission to the Hume-ABAW10 Emotional Mimicry Intensity (EMI) Challenge, which aims to predict six continuous emotion intensity dimensions: Admiration, Amusement, Determination, Empathic Pain, Excitement, and Joy, from in-the-wild multimodal video clips. We propose a staged multimodal framework that combines textual, acoustic, and visual representations, with an optional motion branch. Our approach first trains modality-specific encoders independently and then fuses their learned representations through a lightweight regressor with modality dropout and controlled encoder adaptation. Across our submitted systems, the best validation performance is obtained by the text--audio--vision--motion fusion model under the expanded 4:1 split, achieving an average Pearson correlation of 0.4722. Although the motion branch yields only very slight gains, its behavior can be interesting to study. Our team was placed third in the EMI challenge, achieving an average Pearson correlation of 0.57 for the test set. Overall, we provide a practical and reproducible baseline for EMI prediction.

---


### 50. [Thermo-VL: Extending Vision-Language Models to Thermal Infrared Perception](https://arxiv.org/abs/2605.21882)

**<font color=#1a73e8>作者：</font>** Rusiru Thushara, Yasiru Ranasinghe, Jay Paranjape 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) often fail under low illumination because their visual grounding is learned predominantly from RGB imagery, whereas thermal infrared preserves complementary scene structure when visible cues degrade. We present Thermo-VL, a wavelength-aware VLM that augments a frozen Molmo-7B backbone with a trainable thermal encoder and a text-guided dual-attention fusion module. Given aligned RGB tokens, thermal tokens, and prompt embeddings, the fusion module conditions thermal features on both language and RGB context, then injects a gated residual into the frozen RGB stream so thermal evidence can be incorporated without disrupting Molmo's pretrained RGB-language interface. We train the model with the standard language-modeling objective together with auxiliary alignment and regularization losses that improve cross-modal grounding and reduce over-reliance on RGB. We also introduce a pixel-aligned RGB-thermal instruction-tuning dataset and Thermo-VL-Bench, a manually screened RGB-thermal VQA benchmark for low-light and cross-spectrum reasoning. Experiments show strong gains on challenging thermal-only and RGB+thermal reasoning tasks, highlighting the value of prompt-conditioned multispectral fusion. Our dataset and code are publicly available at: this https URL

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-162](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
