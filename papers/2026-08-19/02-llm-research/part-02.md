# 🧠 大模型相关研究 | 2026年08月19日

> 本类共 **358** 篇论文：已确认 **337** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-358](./part-08.md)

---

### 51. [AeroGround: A Comprehensive Benchmark for Aerial-Ground Collaborative Reasoning](https://arxiv.org/abs/2608.14721)

**<font color=#1a73e8>作者：</font>** Shenghong Yi, Lin Zhang, Muzian Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have been widely employed in understanding and reasoning tasks for unmanned aerial vehicles (UAVs). Existing UAV benchmarks primarily focus on aerial-view scenarios. However, whether current VLMs can perform well on understanding and reasoning tasks in aerial-ground collaborative scenarios which are practical in real-world applications like rescue and infrastructure inspection remains underexplored. To address this gap, we introduce AeroGround, a comprehensive benchmark for evaluating VLMs in aerial-ground collaborative reasoning. AeroGround is built upon a simulated aerial-ground dataset containing approximately 29,000 multimodal observation groups from diverse open environments, and provides 2,250 high-quality question-answering instances covering cross-view correspondence, spatial understanding, and reasoning. Experiments on 16 pretrained VLMs, together with two domain-adapted variants, reveal a substantial gap between current models and human performance: the best model achieves an average accuracy of 54.4%, whereas humans reach 93.3%. By systematically revealing the strengths and limitations of existing models in aerial-ground collaborative reasoning, AeroGround provides a foundation for developing more capable aerial-ground collaborative embodied intelligence systems.

---


### 52. [Tail-Aware Top-$k$ On-Policy Distillation](https://arxiv.org/abs/2608.14728)

**<font color=#1a73e8>作者：</font>** Huipeng Huang, Hongxin Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has emerged as an effective paradigm for transferring knowledge between language models, where a student is trained to align its next-token distribution with the teacher's along its own trajectories. To provide dense supervision at tractable cost, many works minimize the reverse Kullback-Leibler (KL) divergence between the student and teacher's normalized distributions over the teacher's top-$k$ tokens. However, this normalized objective discards the information about tail probability: the total probability outside the teacher's top-$k$ tokens. As a result, the optimization can steadily increase the student's tail probability and entropy, empirically degrading downstream accuracy. To address this issue, we propose Tail-Aware Top-$k$ OPD (\textbf{TA-OPD}), a novel distillation method that restores the missing tail probability signal. In particular, TA-OPD minimizes the reverse KL divergence over the top-$k$ tokens plus a tail token that carries the tail probability. In effect, TA-OPD better aligns the student's next-token distribution with the teacher's, preventing the increase in tail probability and entropy caused by top-$k$ normalization. Extensive experiments demonstrate the superiority of TA-OPD, improving Avg@8 by up to 8.05 points on common benchmarks. Our code is available at this https URL.

---


### 53. [IP Protection in the Era of Visual Generative AI: A Survey](https://arxiv.org/abs/2608.14730)

**<font color=#1a73e8>作者：</font>** Zhuan Shi, Shunchang Liu, Alireza Dehghanpour Farashah 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid evolution of visual generative AI has introduced a wide range of intellectual property risks, spanning the unauthorized learning, reproduction, extraction, misuse, and redistribution of protected data and model assets. To address these risks, a growing body of technical defenses has been proposed. However, existing surveys typically organize this literature by lifecycle stage or technical mechanism, which can obscure the protective intent of different methods. This survey presents a two-dimensional taxonomy for IP protection in visual generative models. The primary axis is a Control Logic View, which classifies methods into Information Exposure Control, Generative Behavior Constraint, and Attribution & Accountability according to the risk variable they regulate. The secondary axis distinguishes Data IP from Model IP as cross-cutting asset dimensions. Under this framework, we systematically review protection methods, align evaluation protocols with protection objectives, and discuss open challenges including proactive model-level safeguards, standardized evaluation, robustness against adaptive attacks, and explainable evidence. This survey aims to offer a principled, systematic, and easy-to-follow overview for both new and experienced researchers in visual generative AI IP protection.

---


### 54. [Class Imbalance and Batch Effects in LLM-Based Screening for Systematic Reviews](https://arxiv.org/abs/2608.14737)

**<font color=#1a73e8>作者：</font>** Gilberto Sussumu Hida, Danilo Monteiro Ribeiro, Clayton Suguio Hida  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study analyses LLMs in imbalanced binary classification, using study screening in systematic reviews as the application domain. An experiment was conducted in five reviews, comparing individual and batch processing, with and without prevalence metadata. The results indicate a limited influence of the prevalence metadata, with no evidence that it improves performance. In contrast, batch processing produced larger behavioral changes that varied according to the prevalence of the class. The aggregate and item-level analyses did not always coincide. Therefore, batch processing should be evaluated not only in terms of cost, but also in relation to its effects on decision-making behavior.

---


### 55. [PolyComp: A Polycube-based Benchmark for Compositional 3D Spatial Reasoning in Multimodal Models](https://arxiv.org/abs/2608.14741)

**<font color=#1a73e8>作者：</font>** Siddharth Patel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce PolyComp, a procedurally generated and verified benchmark that stresses visual recognition and compositional spatial reasoning. In each problem, a model must identify which of four options shows a pair of polycube components that can be combined to form a target solid. The benchmark contains 120 problems across four geometry families, and each problem has three different presentation formats using either a single image or multiple images. The random guessing baseline is 25%. Across the three presentations (360 presented problems per model), GPT-5.6 Sol with max effort attains 50.0% accuracy (95% problem-cluster CI 43.3-56.7%) at a mean cost of \$0.951 per presented problem, Claude Fable 5 with max effort attains 39.4% (33.1-46.1%) at \$0.701, and Gemini 3.1 Pro Preview with thinking level high attains 27.5% (22.8-32.5%), near the 25% random guessing baseline, at \$0.350. The observed accuracy spread across geometry families is larger than across presentation formats. We present a problem development and evaluation protocol, cost and token accounting, and release the 120 problems.

---


### 56. [Agentic Data Cleaning Without a Clean Reference: An Experimental Study of Capabilities and Trade-offs](https://arxiv.org/abs/2608.14765)

**<font color=#1a73e8>作者：</font>** Hadi Fadlallah  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data cleaning without a trusted clean reference is challenging because unusual values may represent either genuine errors or valid observations. This paper studies how different agent capabilities affect reference-free data cleaning and proposes an evidence-grounded framework that combines structured context, profiling, LLM reasoning, executable checks, controlled evidence retrieval, source ranking, citation alignment, conservative repair, reversible scripts, and provenance logging. Seven configurations are evaluated across financial, clinical, and environmental-monitoring datasets using controlled synthetic corruption and original-data descriptive analysis, resulting in 126 completed runs. The evaluation includes two comparison baselines and a progressive LLM-based sequence that adds executable tools, evidence retrieval, evidence controls, and conservative repair. In the synthetic evaluation, the deterministic profiling baseline achieved the highest detection F1-score of 0.561. Among the LLM-based configurations, the full conservative configuration achieved the highest F1-score of 0.421, but no configuration performed best across all evaluation criteria. The source-ranked configurations achieved the lowest unsupported-rule rates, while decision-level citation alignment remained weak. The full conservative configuration produced no unsafe or unnecessary modifications, although these rates were already zero before the conservative policy was added, and it performed no direct repairs. Overall, the results show that additional capabilities introduce trade-offs among detection, repair, evidence grounding, conservative behaviour, reproducibility, and operational cost rather than producing consistent improvements. The study provides a structured framework and empirical methodology for evaluating these trade-offs in reference-free agentic data cleaning.

---


### 57. [From Errors to Proofs: Minimal-Core-Guided Repair for Neuro-Symbolic Constraint Solving](https://arxiv.org/abs/2608.14771)

**<font color=#1a73e8>作者：</font>** Dipankar Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Making language models solve constraint problems reliably often means having them translate the problem into a formal specification and delegating the search to a sound solver. But the translation is itself a language-model task, and an unfaithful translation makes the solver faithfully solve the wrong problem. Existing pipelines repair only translations that crash, returning the solver's error message and falling silent when the program runs but is wrong. We replace the error message with a proof: when the generated program is unsatisfiable, we extract a minimal unsatisfiable core over the model's own constraints and hand it back the exact set that cannot hold together, a leakage-free signal that localizes the fault. On a new benchmark of 77 problems with an exact oracle, translation to Answer Set Programming is faithful on six of seven domains and fails only on aggregate coverage scheduling, which concentrates the translation tax in one diagnosable pattern. A minimal core, rather than a bare error, is what stops a weaker model from fabricating solutions to infeasible problems, cutting fabrication from 79% to 7%. A strong chain-of-thought baseline meanwhile matches the symbolic route on accuracy, so the route's value is not accuracy but certificates and its refusal to fabricate.

---


### 58. [MegaParts: Scaling Part-Aware 3D Object Generation to 300 Parts via Token-Efficient Autoregressive Modeling](https://arxiv.org/abs/2608.14783)

**<font color=#1a73e8>作者：</font>** Manwen Liao, Xinyu Lian, Jian Mao 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Part-aware 3D object generation is essential for graphics applications such as controllable modeling, editing, and articulation, where objects are represented as coherent assemblies of semantic parts. However, existing part-aware generation methods, do not scale well to highly complex objects. As the number of parts increases, generating detailed geometry becomes prohibitively expensive in token length and memory. We introduce MegaParts, a scalable autoregressive 3D generation framework to address this challenge by combining structured sequence modeling with a token-efficient vector-quantized shape tokenizer. Our tokenizer learns discrete latent representations for part-level geometry by minimizing token usage subject to high-fidelity reconstruction, enabling adaptive-length tokenization based on geometric complexity. On top of this compact representation, we train a large language model to generate object bounding boxes, part bounding boxes, and part shape tokens within a unified structured sequence. Combined with efficient long-context training strategy, our token-efficient formulation scales to objects with up to 300 parts and sequence lengths up to 256k tokens. This substantially extends the scale of part-aware 3D generation while preserving compositional structure and enabling fine-grained part-level control. Our method achieves higher mesh quality than baseline autoregressive and diffusion models, showing that compressed discrete part tokens improve not only scalability but also the achievable fidelity of generated geometry. These results suggest that LLM native token-efficient autoregressive modeling is a compelling alternative to diffusion for large-scale part-aware 3D generation. The project page is available at this https URL.

---


### 59. [From Positionwise Confidence to Prefix Scheduling: Verifier Skipping in Speculative Decoding](https://arxiv.org/abs/2608.14787)

**<font color=#1a73e8>作者：</font>** Haoxuan Luo, Jameson Sandler, Ferdinando Fioretto  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Speculative decoding is a leading technique to reduce the cost of autoregressive generation by using a small drafter to propose several tokens, which are then verified in parallel by a larger target model. Speculative diffusion decoding (SDD) further removes sequential drafting by generating every position in a draft block in parallel with a discrete diffusion model. However, SDD still invokes the target on every block, leaving verification as a potential bottleneck. This paper recognizes that this creates a new control handle: whether to invoke the verifier at all. Thus, we study verifier skipping, a lossy policy that commits a selected draft prefix directly, and ask which confidence signal should schedule it. Interestingly, our study finds that better token predictors need not yield better schedulers: skips require contiguous high-confidence prefixes, while short skips can induce additional drafting rounds. To study this mismatch, we compare raw confidence with learned marginal and conditional survival scores under the same policy, using Strict SDD, lenience, and top-$k$ acceptance as baselines. On HumanEval with DiffuCoder-7B-Instruct and Qwen3-32B, all three confidence signals save $9.6\%$ to $13.5\%$ of verifier calls at the same observed pass@1 as Strict SDD. Surprisingly, raw confidence saves the most; marginal survival has higher positionwise AUROC than raw confidence at most positions, yet neither learned signal dominates online. Our analysis shows that verifier skipping is a useful new lossy axis and, surprisingly, its key challenge is prefix scheduling rather than token prediction alone.

---


### 60. [Qwen-Video-Edit: Instruction-Based Video Editing by Repurposing an Image Editing Model](https://arxiv.org/abs/2608.14790)

**<font color=#1a73e8>作者：</font>** Yunpeng Bai, Yossi Gandelsman, Michaël Gharbi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-based video editing is commonly built on video-pretrained generative backbones: a video diffusion transformer is adapted, at considerable cost, to condition on a source video and an editing instruction. In this report we explore a different route and show that a strong instruction-based image editing model can edit videos by operating directly on video-VAE latents. Starting from Qwen-Image-Edit, we arrange the latent frames of a Wan~2.1 video VAE as tiles of one large virtual image, reuse the editor's image positional encoding for every tile, and bridge the two latent spaces with a pair of lightweight input/output projections warm-started from the editor's own patchify and unpatchify layers, so that at initialization a (static) video is embedded exactly as an image the model already understands. The whole system is then fine-tuned on the public Ditto-1M editing triplets, and a few denoising steps of Wan~2.2 serve as an optional temporal enhancer. We motivate the design with a chain of zero-training observations: the stock image editor already edits a video presented as a contact sheet; it is indifferent to whether the sheet's tokens come from one joint encode or from per-frame encodes stitched in latent space; and it even edits genuine video latents zero-shot to a clearly recognizable degree, leaving fine-tuning only a fidelity gap to close. Our results suggest that, despite the large investment in training video latent spaces, per-frame video latents remain close enough to the image domain that mature image editing priors transfer with minimal adaptation. Project Page: this https URL Code: this https URL Model: this https URL.

---


### 61. [CEDAR-GRPO: Process-Aware Reinforcement Learning for General Abductive Reasoning in LLMs](https://arxiv.org/abs/2608.14791)

**<font color=#1a73e8>作者：</font>** Moein Salimi, Danial Parnian, Shaygan Adim 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Abductive reasoning, often characterized as inference to the best explanation, is central to explanation under uncertainty, from everyday sense-making and investigation to scientific discovery. Yet LLM research has mostly studied abduction through narrow, task-specific benchmarks, making it unclear whether observed gains transfer beyond the benchmark family used for training or evaluation. We ask whether RL post-training can improve abduction as a transferable reasoning capability. We introduce CEDAR-GRPO, a process-aware framework that combines final-answer correctness with abductive rewards for evidence coverage and evidence-to-explanation directionality. Four open-weight LLMs are post-trained on a controlled, domain-neutral mixture of abductive hypothesis-generation and hypothesis-selection tasks. We evaluate them on 11 unseen tasks spanning hypothesis selection, missing-fact generation, defeasible inference, long-context investigation, clinical reasoning, code debugging, and non-abductive controls. CEDAR- GRPO improves every model on every held-out task over both base models and correctness-only GRPO, with average gains of 7.4 and 2.7 points, respectively, and a maximum gain of 30.8 points. Ablations confirm that RL, abductive reward design, and task diversity each contribute to transfer. Process-level metrics further show stronger abductive behavior, including exploration of alternatives, elimination of rivals, backtracking, and uncertainty marking.

---


### 62. [Prompting is not enough: supervised baselines and leakage control for measuring shared decision-making with LLMs in pediatric encounters](https://arxiv.org/abs/2608.14792)

**<font color=#1a73e8>作者：</font>** Bernardo Modenesi, Jody Lin, Kimberly Kaphingst 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Objectives: To determine whether zero-shot prompting of a large language model (LLM) is sufficient to detect shared decision-making (SDM) behaviors in real clinical encounters, and whether supervised learning adds value under patient-grouped, nested evaluation.
Methods: We analyzed 21 audio-recorded outpatient surgical decision encounters (19 unique patients; 7,566 utterance segments; ~6.1 hours) between families of children with multiple long-term conditions and their surgical providers. Trained coders labeled segments for 12 SDM behaviors (human-human macro Cohen's kappa = 0.695). We compared a zero-shot local LLM (Qwen 2.5 32B), a supervised classifier over frozen sentence embeddings, and their logistic stack, under patient-grouped outer folds with inner cross-fitted thresholds and patient-resampled confidence intervals.
Results: The zero-shot LLM reached macro kappa = 0.139 (95% CI 0.111-0.164). The supervised classifier reached kappa = 0.227 (0.186-0.262), a paired improvement of 0.088 (0.051-0.119). A logistic stack of the two reached kappa = 0.242 (0.198-0.284). We identified multiple corpus-specific leakage paths, including grouping sibling recordings separately and allowing labels from an outer held-out patient to enter few-shot exemplars used while fitting downstream models.
Conclusion: Zero-shot prompting alone is not sufficient to measure SDM behavior as reliably as a small supervised model, and patient-level grouping alone does not prevent leakage when labeled prompt exemplars are precomputed outside the outer evaluation loop. Reported performance is sensitive to the unit of data splitting and to where labeled exemplars enter the pipeline. External validation is needed before these findings generalize beyond this population, model, prompt, and codebook.

---


### 63. [Beyond Tokens: A Survey on Decoding Methods for Large Language and Vision-Language Models](https://arxiv.org/abs/2608.14797)

**<font color=#1a73e8>作者：</font>** Haoran Wang, Xiongxiao Xu, Philip S. Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) and large vision-language models (LVLMs) have demonstrated impressive generative capabilities, yet ensuring their outputs align with user intent is still challenging. While most existing approaches address this issue at the training stage, inference-time approaches like decoding methods offer a more efficient and scalable solution. Decoding methods control model generation by guiding token-level selection, performing sequence-level generation, or generating tokens in parallel to accelerate the process. In this survey, we identify three emerging paradigms from recent works on decoding methods for LLMs and LVLMs, provide a systematic review of these methods, highlight ongoing challenges, and discuss potential future research directions. Our goal is to underscore the efficiency and effectiveness of decoding methods and offer a practical view of their applications. Paper lists and more resources on decoding methods for LLMs and LVLMs can be found at this https URL.

---


### 64. [Generated Context versus Governed State: Functional Conditions for Accountable Longitudinal Clinical Reasoning](https://arxiv.org/abs/2608.14804)

**<font color=#1a73e8>作者：</font>** Augusto Bernardo Pissarra, Victor Lorena de Farias Souza  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have become the dominant interface of clinical artificial intelligence, yet the interface they expose (text in, text out, one context window at a time) maintains no explicit, persistent, governed representation of what is currently true about a patient. This paper argues that longitudinal clinical reasoning is a state-estimation problem under partial observability, and that the axis on which clinical AI succeeds or fails is not the fluency of the model reading the record but the governance of the patient state it reasons over. We distinguish generated context from governed state; separate five objects that clinical AI habitually conflates (true state, observations, evidence, belief, and simulated state); define a tiered governance standard against which any clinical AI system can be audited; and show that an operational definition of accountability decomposes into four information requirements: an immutable evidence ledger with awareness-time versioning, a belief state distinct from accumulated evidence, an observation-process model, and claim-level causal typing. We are explicit that this decomposition is analytic rather than a necessity theorem, and that its value is conceptual hygiene: it converts "accountable clinical AI" from a slogan into an audit instrument. A six-level maturity framework separates what a system makes governable from what it can compute, locating current LLM-centric practice at high capability but low maturity. The paper is fully self-contained: the four research questions the framework poses are stated in the introduction, and the conclusion records what the paper establishes toward each; future work develops the buildable core of the architecture and the research program toward full Clinical World Models. No empirical result is claimed here.

---


### 65. [Do LLMs Know What to Ask and When? Evaluating Multi-Turn Information Seeking](https://arxiv.org/abs/2608.14808)

**<font color=#1a73e8>作者：</font>** Yepeng Huang, Jiawen Zhang, Michelle Dai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a user question is underspecified, a capable model should recognize that its context is insufficient, identify the missing information, ask for it, and respond only once that information determines a unique answer. We formalize multi-turn information seeking as solving a k-underspecified constraint satisfaction problem, where k is the number of variables jointly required to determine the target and therefore measures the degree of missing information. We instantiate the formulation in MT-InfoSeek, a controlled evaluation suite of 5,251 problems and 9,006 task instances spanning mathematics, logic, biology, medicine, and general knowledge. We evaluate models along three axes: what they ask, when they ask it, and how the acquired information affects the final answer. Performance degrades across models and domains as underspecification increases. Models recognize that additional information is needed but underestimate how much, and in logical problems at k = 2 they under-predict the degree of missing information about four times as often as they over-predict it. They also fail to identify a minimal sufficient set of queries, improve only marginally when given the true k, and often stop before acquiring sufficient information. In tasks with ordered dependencies, an incorrect query order reduces final accuracy even when the model eventually acquires all necessary information. We measure information seeking directly through final sufficiency, which records whether the acquired information determines the target independent of answer generation. This separation shows differences between models that final accuracy alone does not capture, and indicates that the ability to seek information over multiple turns is distinct from the ability to generate answers and is not measured by current LLM evaluations.

---


### 66. [Beyond the pale: Assessing prevalence and contents of extremist speech in LLM training data](https://arxiv.org/abs/2608.14813)

**<font color=#1a73e8>作者：</font>** Dmitry Nikolaev, Ashley A. Mattheis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite a strong interest on the part of the research community in the topic of trustworthy and safe AI, the composition of the text corpora that large language models (LLMs) encounter in pre- and post-training has not yet drawn much attention. In this work, we address the question of whether LLMs are exposed to unfiltered, uncontextualised extremist speech. Using several definitions of extremist speech, stemming from official documents and research literature, and an extraction pipeline combining automated text processing with expert verification, we provide a lower bound on the prevalence of extremist documents in Dolma, an open training corpus underpinning the OLMo series of models. We show that Dolma is likely to include hundreds of thousands of documents containing extremist content and hate speech of several types, including direct calls for violence, and discuss the implications of this for data curation and model pre-training.

---


### 67. [Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce](https://arxiv.org/abs/2608.14825)

**<font color=#1a73e8>作者：</font>** Zeyuan Li, Lukas Petersson, Alessandro Acquisti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Frontier LLM agents increasingly transact on behalf of separate principals, often using natural language rather than structured APIs. Much of the safety literature studies misaligned LLM behavior through adversarial-elicitation evaluations on single agents or stylized tasks. Its prevalence and structure in settings that combine long horizons, separate principals, real operational state, and inter-agent natural-language exchange remain insufficiently measured. We study 2,583 inter-agent emails from 20 one-year simulation runs of Vending-Bench Arena, a competitive vending environment spanning 13 frontier LLMs. We operationalize speech-act misalignment as emails containing false factual claims, manipulation, collusion, or threats, combining message content with ground-truth simulator state and logged reasoning traces to classify and validate such behavior. Under our primary classifier, 12.6% of emails are labeled misaligned; misalignment appears in all 20 runs and 74.7% of individual agent-runs. Both the magnitude and composition of this misalignment are preserved under repeated classification at different sampling temperatures and under full-pipeline replication with judges from two other frontier-model families. Misalignment is also reciprocal and stress-conditioned: receiving a misaligned email from a counterparty raises the odds of a misaligned reply by 1.65x, and low-inventory conditions raise them by 1.58x. Across tests of capability-asymmetric exploitation, we find no evidence that higher-capability models differentially exploit weaker counterparties, and model performance rank does not predict misalignment rates. Together, these results indicate that measurable, state-dependent misalignment can arise in competitive multi-agent environments without engineered elicitation, in patterns associated with operational scarcity and counterparty behavior rather than model capability alone.

---


### 68. [MINT: Min-Selection Preference Distillation for Balanced Multi-Objective Alignment](https://arxiv.org/abs/2608.14828)

**<font color=#1a73e8>作者：</font>** Tony Tu, Sayan Chakraborty, Ruomeng Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aligning a language agent to several objectives at once is a persistent failure mode of preference-based training: when objectives are combined additively, optimization collapses onto whichever is cheapest to improve and sacrifices the rest, so a support agent learns to sound warm while giving no real help. The root issue is that an additive reward has no notion of balance. We introduce Mint (MIN-selection preference disTillation), a one-line change to preference distillation: rather than ranking sampled candidates by a weighted sum of rewards, we rank them by their weakest objective, distilling the best-balanced candidate over the most lopsided one with an unchanged DPO objective. This is the p -> negative infinity limit of a generalized-mean family spanning additive to worst-case selection. Across cooperative emotional support and adversarial negotiation, min-selection lifts both objectives while sharply cutting their imbalance; on emotional support it raises the weaker axis from 0.37 to 0.64 (p < 10^-40), surpassing human experts and persisting across full multi-turn rollouts. A turn-by-turn analysis yields our central finding: min-selection corrects imbalance in proportion to how imbalanced the reference policy is, and its benefit endures over an interaction precisely as long as that imbalance does.

---


### 69. [OvDSGG: End-to-End Open-Vocabulary Dynamic Scene Graph Generation](https://arxiv.org/abs/2608.14835)

**<font color=#1a73e8>作者：</font>** John Helsby, Yi Yang, Bodo Rosenhahn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic scene graphs (DSGs) capture spatio-temporal interactions across videos as $\langle$subject, predicate, object$\rangle$ triplets, and underpin downstream tasks such as video captioning, video question answering, and action analysis. However, end-to-end dynamic scene graph generation (DSGG) methods are closed-set: they recognize only objects and predicates from a fixed training vocabulary and struggle with the long-tailed distribution of rare concepts, severely limiting their real-world applicability. Existing open-vocabulary models typically inherit pretrained large language models, resulting in multi-stage training and inference with substantial cost. We introduce OvDSGG, the first end-to-end framework for open-vocabulary DSGG. OvDSGG builds on top of an open-vocabulary Spatial Backbone and a Temporal Backbone; we further propose a Triplet Feature Extraction Module that bridges them, and a Visual-Language Alignment Module that preserves open-vocabulary recognition by learning an adaptive decision boundary in the joint visual-language feature space, without expensive knowledge distillation in existing methods. We further introduce a rigorous open-vocabulary DSGG benchmark adapted from Action Genome, with disjoint Base/Novel splits for both objects and predicates. OvDSGG significantly outperforms open-vocabulary baselines across all metrics, with zero-shot Recall@$K$ scores 10.0--20.4 percentage point higher than the next-best baseline, while on closed-set DSGG remaining competitive with state-of-the-art models. Code and benchmark are publicly available at this https URL.

---


### 70. [What the Reranker Sees: Multi-Aspect Page Annotation for Long-Document Multimodal Question Answering](https://arxiv.org/abs/2608.14841)

**<font color=#1a73e8>作者：</font>** Guanchen Wu, Jiayuan Ding, Subhabrata Mukherjee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-document visual question answering (VQA) over documents of tens to hundreds of pages mixing text, tables, charts, and figures typically follows retrieve-then-read pipelines. In our setting, the bottleneck shifts from retrieval recall to reranker-side evidence selection: on MMLongBench-Doc, BGE-M3 reaches Recall@20 = 0.86 but only F1@5 = 0.254, and even the visual retriever ColPali reaches only F1@5 = 0.332; a text-only rerank LLM seeing only raw snippets misses table, chart, and layout evidence even when the upstream retriever encoded images. We propose Trident, with two complementary components: Trident-R, a retriever-agnostic LLM reranker that converts each candidate into an LLM-readable semantic record, including a visual caption, section path, entity tags, multi-axis concept hits, and a text snippet, then performs a single adaptive-K rerank call; and Trident-S, a generation-side module that prompts the VLM under topical, entity, and structural lenses before synthesis. On two long-document datasets, the annotation+rerank protocol substantially improves retrieval F1 across five heterogeneous pools, with every reranked pool exceeding the strongest adaptive-K baseline PageIndex. An LLM rerank without the annotation barely changes first-hit ranking, indicating the lift comes from the structured annotation. Trident-S targets open-ended synthesis questions by design, adding up to 6.6 points in generation accuracy on these questions. The best Trident configuration is the strongest downstream QA pipeline in our evaluation, with rankings consistent across two LLM judges (kappa = 0.913).

---


### 71. [Zero-MELO: Test-Time Evidence Calibration with Multimodal LLMs for Zero-Shot Micro-Gesture Recognition](https://arxiv.org/abs/2608.14854)

**<font color=#1a73e8>作者：</font>** Chengyan Wang, Hanliang Xie, Yueyi Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) excel in general video understanding, their capability in fine-grained and motion-centric tasks remains limited. This limitation is particularly critical in micro-gesture recognition (MGR), where micro-gestures (MGs) - subtle, short-duration, and spatially localized human movements - serve as key discriminative signals for implicit affective analysis, yet are easily neglected following common prompting practices. Although MGR has been intensively studied by many discriminative approaches, the use of MLLMs for MGR is underexplored, with notably poor performance. We hypothesize that the motion-sensitive representation ability of MLLMs is constrained by their inherent single-pass forward inference, which can be substantially enhanced through carefully designed test-time guidance. Motivated by this, building on our prior findings regarding temporal insensitivity in Video LLMs, we diagnose zero-shot MGR errors in the Negative Log-Likelihood (NLL) space. We observe that MLLMs suffer from two bottlenecks: 1) insufficient localized evidence and 2) severe score biases driven by language and motion-agnostic appearances. Thus, we propose a novel test-time evidence calibration framework that improves both reasoning details and prediction reliability. Specifically, we introduce a tree search mechanism to progressively acquire localized, fine-grained visual evidence, coupled with a test-time calibration module to mitigate score biases. The multi-cue fusion module then integrates evidence from multiple cues without relying on a single cue for final prediction. Our framework achieves mean-class accuracies of 26.84\% on iMiGUE and 22.10\% on MA-52, significantly outperforming the Qwen2.5-VL baseline, which produces 16.15\% and 10.20\%, respectively. The code will be available at this https URL.

---


### 72. [What to Forget in Unlearning? Forget Set Curation for Language Models](https://arxiv.org/abs/2608.14855)

**<font color=#1a73e8>作者：</font>** Animesh Jha, Arpandeep Khatua, Youssef Allouah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove targeted data or behaviors from a trained model without retraining from scratch. Yet most evaluations assume that the examples to forget are already known. In realistic language-model deployments, a requester may ask a model to stop reproducing a song or book without knowing which spans, documents, quotations, or near-duplicates in a trillion-token corpus support that behavior. We study this missing upstream problem, forget set curation: mapping a suppression request to the data passed to an unlearning algorithm. We introduce CleanSlate, a benchmark for verbatim output suppression over songs and books, with model-specific extraction profiles, content-grounded QA, and capability-retention evaluations. CleanSlate exposes two failure modes. Natural lexical and exact-substring curators often yield forget sets that lead to weak suppression. An evaluation-aware curator suppresses requested continuations almost completely, but causes collateral regression on non-requested content and model-dependent capability loss. These results show that practical unlearning is not only an optimization problem once a forget set is given: the data chosen for forgetting determines both what can be unlearnt and what else is damaged.

---


### 73. [RaivenTracks: Branching Provenance for Conversational Visualization Workflows](https://arxiv.org/abs/2608.14869)

**<font color=#1a73e8>作者：</font>** Ella Hugie, Alexandra Irger, Grace Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI agents increasingly participate in scientific workflows, scientists are shifting from direct authorship toward oversight, inspection, and steering. LLM-driven visualization systems are a promising interface for this hand-off, yet they remain largely stateless, forcing users to reconstruct context across refinements and offering little support for revisiting prior decisions or exploring alternatives. We present RaivenTracks, a workflow-aware extension of the Raiven DSL-mediated visualization pipeline that treats validated visualization specifications as persistent, branchable checkpoints. Because each checkpoint is a verifiable RaivenDSL specification rather than a dialogue transcript, restoring a node recompiles a known artifact rather than re-interpreting prior context. RaivenTracks contributes a two-level state management architecture that pairs a persistent, branchable version tree with a fine-grained undo/redo stack over runtime visualization settings, across both InfoVis and SciVis backends. A formative pilot study with three visualization researchers shows early promise, with all participants adopting the version tree for branching and recovery, and surfaces design directions for tree navigation, node labeling, and scalability that inform a planned controlled comparison against Raiven without version history. We frame branchable conversational visualization history as a step toward provenance support for future scientist-in-the-loop oversight of AI-driven scientific workflows.

---


### 74. [Where Does Retrieval Fail? Evaluating RAG Architectures for Agricultural Advisory](https://arxiv.org/abs/2608.14886)

**<font color=#1a73e8>作者：</font>** Khan Raiyan Ibne Reza, Sanjana Aktar Maria, Sumaiya Tabassum Nimi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval quality in RAG systems is commonly reported as a single aggregate score, which can hide large differences across query types and language conditions. We study this problem in Bengali agricultural advisory, where farmer queries are often colloquial while official advisory documents use formal scientific terminology. We construct a test collection of 1,000 queries and 2,882 knowledge nodes extracted from 284 official Bangladeshi agricultural publications, and use it to evaluate five retrieval architectures and six embedding models under three controlled language conditions.
The results show that no single retrieval method is consistently best. For native Bengali queries, BM25 is the strongest single retriever (R@10 = 0.506) while Hybrid RRF reaches the highest overall R@10 of 0.539. However, dense retrieval performance varies sharply by query type: R@10 is 0.093 on colloquial farmer queries and 0.970 on formal safety queries. Across language conditions, BM25 R@10 drops from 0.506 on Bengali queries to 0.004 when English queries are matched against the Bengali corpus, while dense retrieval falls only from 0.464 to 0.425. We also find that embedding task configuration and passage length can each change reported R@10 by a factor of seven, independent of architecture. These results show why low-resource RAG evaluation should report performance by language condition and query type rather than relying on aggregate scores alone. The dataset and evaluation scripts are available at this https URL.

---


### 75. [Interpretable Cross-Lingual Alignment in Small Language Models: Probing Cultural and Pragmatic Reasoning in Japanese-English Bilingual LLMs](https://arxiv.org/abs/2608.14896)

**<font color=#1a73e8>作者：</font>** Florian Braun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models work well on English and behave in poorly understood ways on languages typologically far from it. Japanese is a clean example, where evaluation still leans on translation quality and JGLUE-style benchmarks, which roll lexical, syntactic and pragmatic competence into a single score. The phenomena on which general-purpose models fail Japanese users are pragmatic: honorifics, in-group and out-group reference, context-sensitive politeness, zero anaphora.
I introduce J-PragEval-v0, a minimal-pair benchmark isolating four such phenomena from surface fluency, and combine it with linear probes and teacher-forced log-probability evaluation to ask where inside TinySwallow-1.5B (28 layers, hidden size 1536) the corresponding contrasts live. The four features split three ways. Honorific register sits cleanly in the residual stream: 0.96 balanced accuracy at layer 15, and the model flips its preferred continuation with the scenario on 93 percent of items. Implicit subject and in-group reference are not linearly decodable at the final prompt token (0.48 and 0.38), yet flip rates are 0.77 and 0.79, so the contrast is worked out during generation rather than stored at the prompt. Indirect refusal is the negative case: 0.95 probe accuracy collapsing to a 0.43 flip rate under length-normalised teacher forcing, because the current minimal pairs conflate politeness with continuation length.
I also specify Pragmatic Representation Steering, a parameter-free inference-time method that edits residual-stream activations along the class-mean-difference directions probing identifies. Feasibility is argued indirectly rather than demonstrated: the contrastive activation addition baseline, the same geometry the method would inject, recovers probe accuracy within one to two points of logistic regression wherever a linear signal exists. Scaling to Llama-3.1-Swallow-8B is the next step.

---


### 76. [How Do Agents Fail on AutoResearch: End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks](https://arxiv.org/abs/2608.14905)

**<font color=#1a73e8>作者：</font>** Yanlin Fei, Nazhou Liu, Xinmiao Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI has long assisted scientific research, but the rapid advance of LLMs and agentic scaffolds is reshaping the landscape; a single system can now carry whole-stage research from an initial hypothesis all the way to final published paper, which is a paradigm now referred to as AutoResearch. Existing evaluations reveal little about how these agents operate or where they break down. Tasks are narrowly-scoped, evaluation measures performance but not process, and failure diagnoses lack systematic coverage or artifact-level visibility. To address this gap, we introduce AutoResearchEval, featuring 100 tasks grounded in published frontier science across 7 scientific domains and the full research lifecycle, including ideation, retrieval, execution, analysis, writing, and review. Evaluating 8 harness-model combinations yields 800 autoresearch agent trajectories, with process-level annotation. We organize these insights into AutoResearch Failure Taxonomy or ARFT, a framework of 45 empirically-grounded failure patterns. To enable scalable fine-grained attribution, we leverage a human-calibrated agent-as-a-judge pipeline to inspect complete trajectories and intermediate artifacts. Failure patterns converge on a single overarching limitation, namely that current agents lack a metacognitive loop, which entails the ability to check what they produced against what they found, revise when it does not hold up, and question whether the path they took was sound. The same patterns recur across all 8 harness-model combinations, including the strongest models tested, locating the deficit at the model level rather than in any particular scaffold; whether orchestration-level interventions can close it is an open question this work does not test. We publicly release AutoResearchEval and ARFT to facilitate continued research and development in autonomous scientific discovery.

---


### 77. [LLMs Can Predict Failure Risk, But Struggle to Predict Which Collaboration Protocol Pays Off: Cost-Aware Protocol Routing Across Reasoning Tasks](https://arxiv.org/abs/2608.14927)

**<font color=#1a73e8>作者：</font>** Chih-Hsuan Yang, Jingyan Jiang, Cheng-Hau Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent large language model (LLM) systems can improve reasoning by spending more computation, but deployment requires deciding when extra collaboration is worth its cost. We isolate this decision by running every problem under four protocols while holding the solver fixed within each setting: direct solving (Baseline), iterative self-correction (Single), planner-executor-reviewer collaboration (PER), and multi-agent deliberation (Broadcast). The primary benchmark comprises 4,181 competition-level math problems; paired robustness checks cover four benchmarks spanning competition math, biology, and broader science with two solver families. Across fixed policies, trained routers, and frozen LLM routers, conservative policies under-escalate, whereas higher-solve frozen routers often over-escalate. A post-answer, pre-collaboration gpt-oss-120b probe ranks Baseline failures with 0.8847 AUROC (4,151 parseable cases; 95% CI [0.8732, 0.8955]). The same score remains informative for predicting whether any collaboration helps (0.7683 AUPRC), but is much weaker for identifying PER- or Broadcast-specific value (0.1674 and 0.1041 AUPRC). Separately, the pre-answer self-confidence gate reaches 78.0% solve at 45K tokens, compared with 73.8% at 71.3K for a frozen gpt-oss-120b router and 92.4% for a retrospective fixed-order oracle. Across 10 paired model-condition settings, the oracle adds 23.2-58.3 points of retrospective coverage over Baseline, but protocol profiles vary by task. In the six settings with held-out router evaluations, oracle gaps remain 18.5-28.9 points. Confidence can therefore support initial escalation, while protocol-specific cost-aware routing remains unresolved.

---


### 78. [Training Leaves Traces: Centered Residual Signatures for Language Model Lineage Verification](https://arxiv.org/abs/2608.14929)

**<font color=#1a73e8>作者：</font>** Aman Singh Thakur, Rayan Khoury  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open-weight language models are fine-tuned, quantized, pruned, and merged, yet their provenance is often undocumented. We study data-free white-box lineage verification: can weights alone reveal whether two compatible model checkpoints share ancestry?
Residual training produces a shared identity-aligned component in branch products, so this structure alone cannot establish ancestry. We remove it and compare checkpoint-specific structure across residual blocks, yielding a symmetric lineage score calibrated against independent checkpoints. On residual-MLP and GPT-2 benchmarks, the score separates fine-tuned, LoRA-merged, pruned, and quantized descendants from independent and distilled models (AUROC=1.0), distinguishing weight ancestry from behavioral similarity. Under function-preserving checkpoint laundering experiments, weight-space baselines lose margin or fail; our score remains unchanged and runs 76x faster than the nearest robust baseline on GPT-2. The projection-pairing signal appears across six language-model families and beyond, and a case study correctly identifies 3 related and 7 unrelated LLaMA-2 public checkpoints. Collectively, these results establish a passive, data-free provenance signal for compatible open-weight language-model checkpoints

---


### 79. [Small Models Scout Bottleneck Order for Large-Model Data Control](https://arxiv.org/abs/2608.14936)

**<font color=#1a73e8>作者：</font>** Seungmin Choi, Jiwon Sung, Muhammad Umer 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Small proxy models are commonly used to identify data mixtures for larger-scale training. We ask whether their training trajectories reveal another transferable structure: the order in which larger models should resolve skill bottlenecks. We formulate first-passage skill training, where each monitored skill has a target floor and the objective is to minimize the tokens required to reach all floors. We introduce LogFloor, a closed-loop controller that directs each round toward current bottlenecks, producing phase-ordered resolution trajectories. Across five bAbI skill slices on Qwen2.5-1.5B, LogFloor reduces token cost by 56.2% on average. In 70M-to-12B transfer, three-round replay of a 70M scout path reaches every floor in all eight target runs, saving 30.9% by pair mean, 39.4% in pooled training tokens, and 37.6% under source-cost accounting. On MMLU-control, a frozen scout path succeeds across all eight 12B runs. Collapsing a path to its static marginal mixture or reversing its phase order removes most benefits, while bottleneck labels alone remain partially useful. These results identify phase-ordered bottleneck resolution as a transferable curriculum structure for monitored skill-targeted training.

---


### 80. [Trust Is Not Enough: Influence Calibration for On-Policy Self-Distillation in Agentic RL](https://arxiv.org/abs/2608.14945)

**<font color=#1a73e8>作者：</font>** Qizhen Lan, Xi Xiao, Xiangchen Guan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) gives language agents dense token-level supervision from a privileged self-teacher on the policy's own trajectories. Existing methods allocate this supervision mainly by teacher trust, but trust does not reveal whether emphasizing a token supports the current policy objective. We call this the trust-utility mismatch and introduce Influence Calibration for Self-Distillation (ICSD). For each supervised token, ICSD measures the first-order response of its importance-weighted RL surrogate contribution to a teacher-directed output perturbation. Batch-adaptive calibration converts this non-stationary signal into a bounded allocation weight while preserving the original auxiliary-loss mass within each action turn. These detached weights affect only the distillation loss and require no additional model pass. Across ALFWorld, WebShop, and Search-QA, ICSD improves all matched aggregate metrics over trust-only allocation under Group Relative Policy Optimization (GRPO) and Group-in-Group Policy Optimization (GiGPO), across two model families spanning 1.5B to 7B. At 7B, it reaches 96.1% ALFWorld success and a WebShop score of 93.1. Frozen-batch analyses show that ICSD reduces teacher-supported mass assigned to objective-opposed tokens from 60.1% to 37.8% and raises cosine compatibility with the RL gradient by 0.192. A companion repository is avail- able at this https URL.

---


### 81. [Who's Keeping Score? Interactive Steering of LLM-Powered Scoring with Attune](https://arxiv.org/abs/2608.14948)

**<font color=#1a73e8>作者：</font>** Bhavya Chopra, Meng Chen, Rebecca Dang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to score text records at scale (e.g., rating candidate resumes on a 1-5 scale). However, existing LLM-powered approaches do not account for the fact that effective scoring requires both holistic understanding of records and locally consistent judgments across similar ones. We present Attune, a mixed-initiative system for steerable LLM-powered scoring. Given a task description and scoring range, Attune performs pairwise comparisons across records to develop a global understanding first, and then resolves these comparisons into consistent score assignments-deriving scoring criteria and rules bottom-up in the process. These serve as shared representations of scoring logic that users can inspect and edit. Based on insights from a formative study (n = 12), Attune's interface introduces novel steering interactions that allow users to deterministically refine scoring logic. Users can provide examples, directly edit criteria, rules, or target distributions, and give natural language feedback-with all refinements compiling into constraints that guide re-scoring. We validate our approach through a technical evaluation across three workloads and a user study with domain experts (n = 8) in healthcare, law, education, and AI evaluation.

---


### 82. [DA-RAC: Distance-Aware Calibration of LLM Judges for Trustworthy AI Auditing](https://arxiv.org/abs/2608.14950)

**<font color=#1a73e8>作者：</font>** Cheng Wu, Vishal Anand, Jaya Krishna Mandivarapu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative AI systems are increasingly producing real-world artifacts, however their efficacy and validity are often evaluated via context-free LLM-scoring. These judges can be miscalibrated by irrelevant in-context reference examples, creating false confidence and allowing low-quality or harmful outputs to pass evaluation. We study this failure mode as context-induced miscalibration and introduce DA-RAC, a distance-aware reference-anchored calibration method for LLM judges. DA-RAC retrieves semantically and structurally similar labeled anchors for each judgement scenario, weights them by distance, and exposes neighborhood difficulty as a calibration and triage signal. On multi-run LLM-judge evaluation benchmarks, it improves calibration and reduces false-pass risk relative to zero-shot, chain-of-thought evaluation, and static-anchor baselines. Mechanistic analysis shows that judge scores vary systematically with anchor distance, while static references can induce misleading decision boundaries. Thus LLM-judgement requires not only better models, but also calibrated, auditable reference selection, especially when automated evaluation is used to support high-impact AI generated artifacts. Judgments should be grounded in relevant, inspectable, and contestable interpretive artifacts.

---


### 83. [T-LLM Compiler: Trusted LLM-based Code Optimization and Verification Framework](https://arxiv.org/abs/2608.14953)

**<font color=#1a73e8>作者：</font>** Zahra Fazel, Sunanda Gamage, Shayan Shirahmad Gale Bagi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Language Models (LLMs) have opened opportunities to apply high-level code transformations to the field of code optimization, and it has since emerged as one of the most fundamental tasks for LLMs to perform; however, at present, LLMs struggle to apply wide-ranging code optimization tasks due to both the complexity of the code and the inability to independently verify the correctness of the transformations. In this paper, we present the Trusted LLM (T-LLM) Compiler, which proposes an advancement in compiler technology through a collaborative effort involving high-level LLM code transformations, traditional compilers, and verification tools. Experimental results reveal that it can significantly improve code correctness when tested on a set of PolyBench/C benchmarks. Our approach facilitates iterative code optimization efforts with verification strategies that enable corrective actions. Through this approach, T-LLM Compiler achieves code optimization accuracy of up to 83.3% and a speedup of up to 16.1\% on the PolyBench/C benchmarks, with the transformed code reaching an average of 26.7% speedup wrt standard baselines. Additionally, we release the project's source code to the open-source community.

---


### 84. [LLM-based Framework for Generating and Verifying Parallel DEVS Statecharts](https://arxiv.org/abs/2608.14956)

**<font color=#1a73e8>作者：</font>** Vamsi Krishna Vasa, Hessam S. Sarjoughian, Edward J. Yellig  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The development of models demands sound modeling and simulation knowledge as well as domain knowledge. Every model should accurately represent a system's dynamics and be verifiable. Toward this objective, this research introduces an agentic PDEVS-LLM framework to assist human modelers in generating and verifying PDEVS statecharts for behavior modeling of atomic Parallel Discrete Event System Specification (PDEVS) models. The framework supports (re)generating plausible facts from a system description prompt using the agentic LLM used for generating plausible facts. Inconsistencies in plausible facts lead to incorrect PDEVS statecharts having logical structure and behavioral inaccuracies. A controlled-correction mechanism is developed to verify the logical consistency of the plausible facts. The agentic LLM is used to generate key behavioral conditions from the system description prompt. The plausible facts are then verified against the behavioral conditions using propositional logic entailment for a finite number of times. The verification results enable the generation of modification prompts that can reduce errors in generated plausible facts, resulting in more accurate PDEVS statecharts. To verify a statechart's logical correctness, its Timed Automata counterpart is manually created and verified for deadlock and reachability properties. The human modeler may regenerate plausible facts and PDEVS statecharts iteratively and incrementally. A basic correctness metric is introduced to quantify the completeness and accuracy of the expected behavioral traits of the PDEVS statechart models. A collection of example systems with varying levels of complexity is developed to demonstrate the capabilities and limitations of LLMs. The evaluation of the proposed verification mechanism shows a substantial improvement in the logical consistency of generated statecharts.

---


### 85. [Benchmarking Frontier Text-to-Image Models on Image-Description Prompts](https://arxiv.org/abs/2608.14976)

**<font color=#1a73e8>作者：</font>** Sajjad Abdoli, Ghassan Al-Sumaidaee, Ahmed Rashad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image models are typically reported on average-case prompts, which understates the gap between systems on compositionally demanding requests involving precise object counts, multi-object attribute binding, legible embedded text, and explicit spatial constraints. We evaluate four production text-to-image systems: Hunyuan 3.0, Gemini 3 Pro Image ("Nano Banana Pro"), Black Forest Labs FLUX.2, and Ideogram 3.0. The evaluation uses the 48 hardest prompts drawn from the this http URL Sample Dataset (DSD), selected through an automated complexity-scoring pass over the full corpus. Every generated image is graded using an independent-judge rubric. GPT-5.4-Pro authors an atomic, weighted, mutually exclusive and collectively exhaustive (MECE) evaluation rubric, while Gemini 3.1 Pro Preview independently determines whether each criterion is satisfied. Gemini 3 Pro Image ranks first with a score of 84.8/100, narrowly ahead of FLUX.2 at 82.3/100. Ideogram 3.0 and Hunyuan 3.0 score 65.7/100 and 63.3/100, respectively. Failure analysis shows that the leading systems primarily lose points through object miscounting and geometric artifacts, whereas the trailing systems more frequently produce garbled text. Ideogram 3.0 also frequently omits requested elements. Full per-sample rubrics, scores, and failure annotations are available from the authors upon request.

---


### 86. [Risk-Adaptive Edge--Cloud Visual Reasoning for Communication-Efficient Autonomous Driving](https://arxiv.org/abs/2608.14991)

**<font color=#1a73e8>作者：</font>** Meng Ma, Shuyang Li, Naigang Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cloud-hosted vision-language models (VLMs) offer greater contextual reasoning capabilities than smaller onboard models, but frequent visual uploads increase communication overhead and add network and inference latency to tactical decisions. We present a risk-adaptive edge-cloud architecture in which onboard traffic assessment determines when cloud reasoning is requested. An onboard VLM and a lightweight detector capture temporal traffic conditions and path-relative hazards for conservative local response and selective cloud access. The cloud model provides tactical advice, while validation, vehicle control, and automatic emergency braking remain local. In CARLA experiments, our method matched the task success rate of periodic cloud access while reducing cloud requests by 54.1% and recording fewer automatic emergency braking (AEB) activations. In a delayed-roadwork ablation, semantic events triggered requests before the next scheduled audit. Across three emulated network profiles, the method continued to reduce cloud traffic, although lane changes took longer than with periodic access. Onboard traffic assessment therefore served as a practical trigger for selective VLM inference in these experiments.

---


### 87. [Does a Tool Result Carry More Authority Than Plain Text? Three Prospective Studies of False-Claim Adoption in a Synthetic Assignment Task with Claude Opus 5](https://arxiv.org/abs/2608.14992)

**<font color=#1a73e8>作者：</font>** Justin Bronder  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model systems increasingly read from stores they also write to, so a claim that was merely written earlier can return looking retrieved. We tested whether the message package carrying an unsupported assignment changes which answer a model gives in a synthetic lookup task. Claude Opus 5 selected a color code for a named item or abstained. In an exploratory four-arm study, false-code adoption was 0/24 with no target claim, 0/22 scorable trials when a prior assistant assertion named the target, 14/24 when a tool-result record named it, and 15/24 when that result used a ten-field metadata wrapper that marked it unchecked. The tool-result arm selected the record's code in 11/12 supported trials and 14/24 unsupported trials, ruling out a fixed output-token bias while leaving substantial planted-token heterogeneity. A document-preregistered replication reproduced the tool-result versus assistant-assertion gap, 7/24 against 0/24, one-sided Fisher exact p = 0.0047. The tool-result rate nevertheless fell from 14/24 to 7/24 across runs made four days apart. A second preregistered study gave the earlier comparison a live text control: both records were announced in advance and placed in the same final user turn, then target binding was swapped between the linked tool result and later inline JSON. Inline text was sufficient for false-code adoption in 60/60 trials; the tool-result condition produced 57/60, so the registered result-first superiority criterion failed, p = 1. The result does not show that tool results have no effect. It shows that native tool-result placement was not necessary and that this experiment did not find greater behavioral weight for the result package than for announced inline text. The findings concern a single model on one synthetic task template, accessed through one API.

---


### 88. [RamseyGadgets: A Graph Construction Dataset for LLMs](https://arxiv.org/abs/2608.14999)

**<font color=#1a73e8>作者：</font>** Zohair Raza Hassan, Deepak Pandita  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Constructing special graphs is an important task within graph theory and computer science. Many popular graph constructions are the result of a comprehensive exploration of relevant graphs and human ingenuity. Given the rise of generative AI usage in mathematics, it is natural to test whether LLMs are able to construct graphs with specified properties using their reasoning capabilities. Unfortunately, many natural graph construction problems, such as finding extremal Ramsey-good graphs (i.e., avoiding specific monochromatic subgraphs), have been explored extensively in the literature, making it difficult to ascertain whether a construction is the product of an LLM's reasoning capabilities or its recollection from training data. In this work, we introduce \textbf{RamseyGadgets}, a novel dataset of 70 underexplored graph construction problems that require finding Ramsey-good graphs with special properties (e.g., containing an edge with a fixed color). These problems have reasonably sized solutions (at most 10 vertices) that can be verified by SAT solvers, making them suitable for automatic evaluation. Our dataset is easily expandable, as one can simply change the monochromatic subgraphs being avoided to obtain a new set of problems. We evaluate the performance of five open-source LLMs on our dataset and report the results. Our findings show that LLMs achieve only 37.70% accuracy on the hard-tier problems in our dataset, with Gemma-4-31B achieving the highest performance out of the five. We also showcase how our dataset allows us to ascertain what kind of hints help LLMs perform better at this task.

---


### 89. [FZ-VLM: A Two Stage Florence-Zephyr Vision Language Model Framework for Pulmonary Nodule Characterization and Clinical Decision Making](https://arxiv.org/abs/2608.15004)

**<font color=#1a73e8>作者：</font>** Pramit Dutta, Jenita Manokaran, Richa Mittal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lung cancer remains one of the leading causes of cancer-related mortality worldwide, and Computed Tomography (CT) is a primary imaging tool for screening and followup assessment. After pulmonary nodule detection, radiologists manually assess anatomical location, diameter, margin characteristics, and attenuation type to support risk assessment and clinical decision-making. However, this post-detection workflow is time-consuming and can be affected by inter-observer variability. Existing Artificial Intelligence methods often focus on isolated tasks, limiting their use as a unified, clinically grounded interpretation framework. This study presents FZ-VLM, a two-stage Florence-Zephyr Vision Language Model framework for unified structured pulmonary nodule characterization in lung CT. The framework uses a fine-tuned Florence-2 model to extract radiological attributes from expert-annotated 2D axial CT slices, while a Zephyr-7B model uses these attributes to generate nodule descriptions, follow-up recommendations, and longitudinal analyses. Results showed that the Stage 1 model achieved 77.18\% accuracy for anatomical location, 67.96\% accuracy for margin characteristics, and 79.13\% accuracy for attenuation type, with a Mean Absolute Error of 2.58 mm for diameter estimation, outperforming evaluated GPT-4-based baselines as well as the human baseline. Expert radiologist evaluation of Stage 2 showed 93.9\% accuracy, 98.6\% completeness score, 76.1\% clinical relevance, and an overall score of 89.5\%. Safety analysis showed that most outputs were clinically safe, although some follow-up recommendations still required expert review. To the best of our knowledge, this study presents the first two-stage Vision-Language Model framework for structured nodule characterization and clinical decision-making.

---


### 90. [MetaReason: Precise Interleaved Multimodal Reasoning via Editing Meta Information for Solving Geometry Problems](https://arxiv.org/abs/2608.15006)

**<font color=#1a73e8>作者：</font>** Penghao Yin, Haomin Wang, Qihong Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although visual reasoning is crucial for solving complex geometry tasks, existing vision-language models rely heavily on text-only reasoning. Some recent methods introduce intermediate visual states to facilitate reasoning, but they are often hindered by inaccurate geometric representations and low rendering fidelity, ultimately leading to unreliable outputs. To address these limitations, we propose MetaReason, a framework for multimodal reasoning in plane geometry that leverages structured meta-information to enable accurate auxiliary-line construction. The framework first parses geometric images into meta-information, performs controllable edits with predefined tools to synthesize high-fidelity visual states, and then conducts reasoning based on these augmented views. To support this framework, we construct TutorGeo, a comprehensive dataset containing 17k image-to-meta conversion samples, 60k text-only reasoning traces, and 60k interleaved multimodal reasoning traces. Using this dataset, we combine supervised fine-tuning and reinforcement learning to develop robust multimodal reasoning capabilities. We also introduce ExamGeo, a benchmark derived from real-world examination problems that enables systematic evaluation across varying difficulty levels. Experimental results demonstrate that MetaReason significantly outperforms existing open-source models and achieves competitive performance against proprietary models.

---


### 91. [Harness the Memory: A Holistic Evaluation of Memory Substrates in Memory Agents](https://arxiv.org/abs/2608.15008)

**<font color=#1a73e8>作者：</font>** Wei-Chieh Huang, Weizhi Zhang, Yuchen Wu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory is becoming core infrastructure for long-horizon LLM agents, yet existing evaluations offer limited guidance on which memory substrate, namely the underlying medium in which memory is represented and stored, should be used under different operating regimes. We present a controlled harness evaluation of memory substrates for memory-augmented agents, covering dense and sparse indices, text records, structural stores, hierarchical stores, refinement-based memories, parametric updates, and activation-compatible context mechanisms. Across three backbone models and four benchmark suites spanning user-centric question answering and agent-centric decision-making, we instrument 26 performance and efficiency metrics under a unified harness. Our results show that no single substrate consistently dominates: broad retrieval benefits long-context factual QA, while excessive retrieval can harm sequential decision-making by shifting attention away from action-critical context. Scalability introduces a further routing axis, as substrates that perform well at moderate history lengths can become costly or brittle at longer horizons. These findings motivate substrate routing as a necessary component of adaptive agent memory systems and provide empirical guidance for designing efficient, reliable, and regime-aware long-term memory for LLM agents. Code will be made available upon acceptance.

---


### 92. [SysEvolve: An AI-native, safe, autonomous adversarial attack-defense co-evolutionary system](https://arxiv.org/abs/2608.15012)

**<font color=#1a73e8>作者：</font>** Yuhan Meng, Shaofei Li, Jionghao Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of large language models (LLMs) has created a growing asymmetry in cybersecurity, where attack accelerates toward autonomous execution while defense remains predominantly human-intensive. Despite substantial prior work across cyber ranges, AI-driven attack, and AI-driven defense, this asymmetry persists. We trace it to a deeper root cause, that evolution itself has stalled on both sides at three layers. To overcome this, we propose co-evolution as the integrating insight, where attack and defense AI agents autonomously and safely drive each other's evolution through adversarial confrontation. Based on this insight, we present \sysevolve, comprising three co-designed components, \sysfield, \sysspear, and \sysarmor. \sysfield constructs realistic multi-host ranges. \sysspear generates efficient, safe attack schemes. \sysarmor performs real-time, interpretable defense. Together they form a self-driven adversarial loop restoring evolution at all three layers. In evaluation, \sysfield achieves zero-loss collection at 2.1\% overhead and orchestrates 257 CVEs into 1,148 ranges, \sysspear improves attack success by over 25\% over baseline LLMs, and \sysarmor achieves 10--1000$\times$ greater precision than prior systems and detects real APT attacks in production at Huawei and Sangfor. Our evaluation also reveals three findings about LLM agent capabilities. First, multi-step composition and larger topologies expose agent capability gaps hidden by single-step evaluations. Second, the bottleneck lies after initial access in post-compromise state utilization. Third, LLM agents are susceptible to environmental interference. When decoy endpoints are deployed in the range, agent timeouts triple and downstream completion disappears despite the success rates of initial accesses are unchanged.

---


### 93. [Hierarchical Agentic Incident Response with Digital-Twin-Validated Attack Inference](https://arxiv.org/abs/2608.15016)

**<font color=#1a73e8>作者：</font>** Yiran Gao, Juntao Chen, Tao Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Network incident response remains slow and labor-intensive as the defender must infer multi-stage attacks from partial observations and translate recovery decisions into reliable system commands. Decision-theoretic planners provide principled optimization but typically rely on abstract states and predefined actions, while large language model (LLM) agents can reason over operational context but may hallucinate attacks and responses. Toward automating response planning, we present a hierarchical agentic response framework that integrates LLM-based attack inference, rollout planning, and digital-twin validation. A fine-tuned LLM infers the attack progression and affected hosts from security alerts and system measurements. An emulated network digital twin replays the inferred attack and returns discrepancies between predicted and observed effects to calibrate the inference. A separately fine-tuned planning agent uses the rollout planning method to prioritize affected components at the tactical layer. At the operational layer, the planning agent proposes high-level recovery actions, and an execution agent translates selected actions into recovery and verification commands that are validated in the digital twin. We evaluate the framework on a 33-component enterprise-network testbed under three multi-stage attack scenarios. The results show that our framework outperforms frontier-LLM baselines in recovery success rate by 18--31%.

---


### 94. [S2-MoE: Enabling Efficient Self-Speculative Decoding for Mixture-of-Experts on Edge Devices](https://arxiv.org/abs/2608.15018)

**<font color=#1a73e8>作者：</font>** Haochen Huang, Shengxuan Qiu, Meng Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying large language models (LLMs) for inference on edge devices is challenging due to severe memory and bandwidth constraints. While speculative decoding and Mixture-of-Experts (MoE) have been proposed to improve inference efficiency, naively combining them often incurs excessive verification overhead and poor expert reuse, limiting their effectiveness in memory-bound edge settings. In this work, we propose S2-MoE, an efficient self-speculative decoding framework for MoE inference on edge devices. S2-MoE reduces redundant verification through routing-aware adaptive speculative expansion, improves verification efficiency with reuse-aware expert gating, and aligns draft and target execution via shared context. Implemented in this http URL, S2-MoE achieves up to 5.3x speedup (about 2.0x on average) over standard autoregressive de?coding across diverse MoE models and datasets on edge this http URL is available at this https URL.

---


### 95. [Gathered, Not Admitted: How Attention Brings a Latent Variable into Verbalizable Form](https://arxiv.org/abs/2608.15022)

**<font color=#1a73e8>作者：</font>** Parsa Mazaheri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models hold latent quantities in a form they can report on, and more of a quantity is present in that form when the task requires reusing it flexibly. What causes a representation to enter that form is open, and the word workspace invites an admission story: a gate that decides what gets in. Testing it on open-weight models with Jacobian lenses, over a benchmark whose five arms share an identical context, we find no gate where it predicts one. Demand raises a concept's lens visibility beyond what applying an operator to a supplied value produces: +0.050 [+0.045, +0.057] in percentile rank on our primary checkpoint, positive on all four we measure, though that arm answers at ceiling and the accuracymatched contrast is stronger under that readout. At the same time one shared linear map decodes the variable from every arm, the control included, at 6.4-9.0x its selection-corrected floor. What produces the later readable form at the queried position is attention-mediated gathering inside a mid-depth window: separating patch depth from readout depth puts transport there at least 17x above anywhere shallower under non-saturating readouts, with no tested MLP output contributing positively inside it. Under the saturating percentile rank the same grid does not localise the window, which is a fact about that measure. An arm that needs the variable for nothing concentrates sevenfold less, so the window is demand-specific. That window has two measured edges, a survival failure below and destruction above, and it falls at the same fractional depth in a 64-layer hybrid and a 62-layer dense model from another family. We localise where the variable is installed and read, not the route from the passage, which transports nothing. But the readout is not a calibrated measure of use: three components move it to within 12% of one another and differ 7.4x in what they do to the answer.

---


### 96. [Handoff-H1: An Orchestrated Vision-Agent System for Material Quantity Takeoff from Construction Blueprints](https://arxiv.org/abs/2608.15032)

**<font color=#1a73e8>作者：</font>** Bruno Chicelli, Henrique Alves, Rodrigo Anselmo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Converting a set of architectural blueprints into a complete material quantity takeoff requires visual perception across drawing sheets, dimensional and multi-hop reasoning, and grounding in construction conventions that the drawings never state. We present Handoff-H1, a takeoff system built from three layers: purpose-built computer-vision models that extract primitives; tool-using agents equipped with image operations and in-house visual-task tools, including CV-model-backed counting, detection and plan decomposition; and a persistent, hierarchically structured project foundation, grounded in a curated construction knowledge base. We evaluate on the Construction Blueprint Takeoff Benchmark: 10 real residential blueprint sets paired with consensus-validated expert takeoffs - 2,009 verified line items, restricted for scoring to the 1,348 primary-tier materials that drive an estimate - scored per trade by an LLM judge on material coverage and quantity Precision@25% (P@.25) and combined into a weighted composite. Under identical scoring from the raw PDF, seven frontier and open-weight models span composites of 35-61, and independent professional estimators - scored against the same reconciled gold standard - post 77.6% (65.5% coverage, 87.9% P@.25). Handoff-H1, working end-to-end from the raw PDF, reaches 81.6% (86.1% coverage, 78.8% P@.25): roughly 20 points above the strongest frontier agent, and above the independent estimators by pairing near-human quantity precision with coverage they do not reach. The evaluation harness is public for the open harbor framework; the blueprint sets and ground truth are available upon request for research use.

---


### 97. [LLM-Based Hierarchical Coordinated Control with Continuation-Aware Policy Learning](https://arxiv.org/abs/2608.15041)

**<font color=#1a73e8>作者：</font>** Changhong He, Jinda Gao, Xinkuan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coordinating multiple interacting units in complex engineering systems is challenging when system interactions are difficult to model, operational information is heterogeneous, and low-level actions must satisfy strict constraints. We propose an LLM-based hierarchical framework in which the LLM coordinates interacting units based on heterogeneous operational context, while task-specific controllers or optimizers generate executable and constraint-aware actions. We further introduce Continuation-Aware GRPO to capture the consequences of coordination decisions over subsequent control intervals. Rather than judging a decision only by its immediate outcome, the method also evaluates how the system evolves afterward under the current policy. We validate the framework on multi-ramp traffic control and virtual power plant (VPP) energy management, using simplified system models for training and more realistic simulators for evaluation. Across both tasks, the proposed method consistently outperforms direct task-specific control and optimization, end-to-end reinforcement learning, rule-based and RL-based hierarchical coordination, and prompting-only LLM coordinators, demonstrating the value of heterogeneous-context reasoning, hierarchical execution, and continuation-aware policy learning.

---


### 98. [MOSS-VL Technical Report](https://arxiv.org/abs/2608.15045)

**<font color=#1a73e8>作者：</font>** Pengyu Wang, Chenkun Tan, Shaojun Zhou 等 32 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present MOSS-VL, an open vision-language model family that treats real-time interaction -- perceiving while it speaks -- as a first-class capability. It is co-designed across the stack: the language decoder attends to vision only through gated cross-attention, so the model can naturally see incoming frames while generating; a synthesized interaction corpus supervises when to speak, when to stay silent, and when to revise; and a staged curriculum concentrates all real-time-specific training in one light final stage over a strong offline foundation. Offline, MOSS-VL-Instruct is competitive at comparable scale and leads temporal-reasoning video sets. Across four streaming benchmarks, MOSS-VL-Realtime posts the best average on three (second on the fourth) among open-source streaming models, sweeping the three subsets that squarely test proactive behavior -- 66.0 vs. 37.5 for the best baseline on OmniMMI Proactive Alerting. With 11.3B parameters but visual tokens outside the decoded sequence, MOSS-VL widens its time-to-first-token advantage over same-backbone Qwen3-VL-8B from 2.8x to 5.1x as visual context grows. We release all five checkpoints, the training curriculum, and the real-time inference code at this https URL.

---


### 99. [Certifying Compressed Language Models: An Audit and a Statistical Toolkit](https://arxiv.org/abs/2608.15046)

**<font color=#1a73e8>作者：</font>** Amogh Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A fraction of a point of benchmark accuracy is the usual evidence that a compressed model is equivalent to its original. That quantity is least informative when two models are most alike: a net delta is what survives cancellation between opposing per-item changes, and cancellation is most complete in the regime equivalence claims occupy. Across an atlas of 1,707 paired model-by-task cells mined from public per-item evaluation dumps (1.3B-405B), churn runs roughly five times the net accuracy delta, and cells scoring identically to their baseline still disagree on individual items. In a preregistered audit of 17 equivalence claims from three registered frames (method papers, model cards, vendor documentation), 16 are eligible. None states a prospective numerical equivalence margin, and none releases task-matched per-item outputs, though 3 release outputs for other tasks only; 5 report too little to assess numerically, so a reader cannot check them at any sample size. We audit evidential sufficiency, not truth: no claim is called false. We supply the missing instrument: paired equivalence testing at a declared margin, with certification tables giving the items an evaluation needs, computed from disagreement observed under compression, not from independent-binomial variance. A controlled experiment pairs GPTQ and AWQ on byte-identical calibration samples across five seeds. Under the frozen eight-cell decision rule H3 is supported: changing the calibration draw was sufficient to reverse the observed method ordering in 5 of 8 confirmatory cells. The reporting standard we propose is five lines: declare a margin, run the paired test, report churn beside net delta, cite the sample size you met, release per-item outputs. It applies to any comparison between two models alike enough to be worth comparing. All per-item outputs, protocols and code are released.

---


### 100. [A Unified Mamba--MoE Surrogate for Closed-Loop Simulation and Measurement-Window Forecasting of Inverter Transients](https://arxiv.org/abs/2608.15051)

**<font color=#1a73e8>作者：</font>** Haoguang Wang, Huy Hoang Le, Akhila Kandivalasa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a Mamba surrogate model with mixture-of-experts (MoE) routing to represent the transient dynamics of inverter-based resources. A Mamba surrogate model is a predictive machine learning model built on the Mamba architecture. MoE routing uses a router network to assign data-dependent weights to specialized subnetworks (experts). The resulting Mamba--MoE surrogate can perform two tasks: (i) closed-loop simulation and (ii) measurement-window forecasting of inverter transients. A single Mamba backbone with task conditioning and expert routing serves both tasks, replacing two separate specialists. Task-matched objectives fit each prediction form, and an adaptive conformal layer provides prediction intervals for both tasks. For the considered grid-following inverter, the unified surrogate model remains in the same low-error regime as a Mamba specialist pair while using 13% fewer parameters. The prediction intervals achieve 94--96% empirical mean marginal coverage across the two tasks. For transient dynamics---that is, beyond the vicinity of an equilibrium point---our surrogate model with MoE routing yields lower errors across all outputs in both tasks compared to a shared Mamba backbone without expert routing. A controller hardware-in-the-loop simulation validates our results and shows that adapting only the shared output head with limited measured data reduces held-out forecasting error.

---


> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-358](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
