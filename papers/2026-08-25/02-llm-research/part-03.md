# 🧠 大模型相关研究 | 2026年08月25日

> 本类共 **170** 篇论文：已确认 **154** 篇，待复核 **16** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-170](./part-04.md)

---

### 101. [Vibe Coding and Web Application Security: A Twin-Prompt Study](https://arxiv.org/abs/2608.20963)

**<font color=#1a73e8>作者：</font>** Darko Andročec  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly generate complete web applications from natural-language prompts, raising the question of whether explicitly requesting security best practice improves the result. We study six functionally distinct web applications, each generated in two prompt variants that are identical except for an appended security-requirements section: a baseline (A) and a security-aware (B) variant. All twelve programs were produced by the same agentic coding assistant and the same model version in a single, non-iterative generation round, and were then analyzed with static, dependency, dynamic and manual techniques, yielding 75 confirmed findings out of 85 candidates. The security-aware variant produced fewer confirmed findings in every application (24 versus 51) and contained no Critical or High issues; the most severe finding was detected only by manual testing. Because the corpus is small and each variant was generated once, we report descriptive observations rather than statistically established effects, and position the work as a preliminary study whose pipeline is being scaled to multiple models and repeated runs.

---


### 102. [Structured but Fragile: On the Limits of LLMs in Cybersecurity Decision-Making](https://arxiv.org/abs/2608.20966)

**<font color=#1a73e8>作者：</font>** Pasquale Malacaria, Yunxiao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in cybersecurity workflows, yet it remains unclear whether they can perform structured security reasoning or merely rely on superficial cues and prior knowledge. We study this question in the context of defence selection over attack graphs derived from real-world threat scenarios, including ransomware, supply-chain compromise, cloud abuse, Kubernetes attacks, POS malware, and ICS/OT intrusion. Given a budget constraint, LLMs must select security controls to minimise attacker success. We compare their strategies against each other and against a game-theoretic optimization baseline used as a normative reference for structured reasoning. Our results show that LLMs exhibit conditional competence. When explicit attack-graph structure is provided, they often produce coherent strategies close to the optimization baseline. However, their capabilities are fragile. LLM behaviour becomes increasingly fragile with graph complexity and is highly sensitive to framing. Small prompt changes can substantially alter rankings, and merely relabeling a poor strategy as ``optimal'' dramatically improves its evaluation. We further observe a non-monotonic relationship between formal risk and LLM judgement: strategies closest to the optimum are not necessarily ranked highest by LLM evaluators. To further probe reasoning ability, we ask LLMs to generate solvers for the same optimization problem. While the generated implementations recover the correct high-level formulation, they scale poorly compared to a purpose-built solver. Overall, our findings show that LLMs can approximate structured cybersecurity reasoning under controlled representations, but do not apply it robustly. This has important implications for the design and evaluation of AI-assisted security decision-support systems.

---


### 103. [Deep Learning Models Also Recall Features](https://arxiv.org/abs/2608.20970)

**<font color=#1a73e8>作者：</font>** Pierre Beckmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work in mechanistic interpretability has studied how large language models recall facts stored in their weights. This paper argues that factual recall points to something broader: a general kind of operation in deep learning models, which I call feature recall. The core observation is that a linear projection can be read as retrieving stored information scaled by input activations. I define feature recall, show it applies across architectures, and contrast it with the established paradigm of feature combination. I also consider how cases of feature recall might be mechanistically identified. The account gives philosophers a new conceptual tool for understanding deep learning, and points to empirical directions for mechanistic interpretability research.

---


### 104. [Belief Without Behavior: Measuring the Translation of Theory of Mind into Coordinated Social Action in Vision-Language Models](https://arxiv.org/abs/2608.20975)

**<font color=#1a73e8>作者：</font>** Tonglin Yan, Gregoire Sergeant-Perthuis, David Rudrauf  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective social interaction requires agents to translate mental state inferences into coordinated behavioral signals across verbal and nonverbal channels simultaneously. Yet existing benchmarks evaluate theory of mind (ToM) reasoning and embodied behavior in isolation, leaving unmeasured the gap between social inference and social action. We introduce MOSAIC (Multimodal Orchestration of Social Action, Inference, and Communication), a controlled benchmark in which two embodied agents interact across cooperative and competitive scenarios requiring integration of verbal statements, spatial trajectories, gaze direction, and facial expression under systematically varied ToM constraints. Evaluating 13 models, including 11 VLMs, across 200 trials per model, we find that VLMs fail to produce behaviors consistent with the expected outcomes under ToM-order constraints, and that imposing explicit ToM-order constraints produces no reliable behavioral change aligned with the specified reasoning level. Signal-level analysis reveals two sequential bottlenecks: most models cannot produce directionally coherent nonverbal signals, and even when signals are present, VLM agents fail to interpret others behaviors and react to them. PCM-LLM, included as a structured architectural reference point with an explicit ToM module, succeeds across all conditions, suggesting that explicit belief-action coupling is a sufficient ingredient for this class of tasks.

---


### 105. [MigrationNarrate: A Dataset for Detection of Migration Narratives in YouTube Videos](https://arxiv.org/abs/2608.20984)

**<font color=#1a73e8>作者：</font>** Fatima Haouari, Carolina Scarton, Kalina Bontcheva  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Narratives are central to how social communication is framed, making their detection critical for understanding and analysing public discourse. Prior work has explored narrative detection and extraction across diverse domains; however, migration narratives remain significantly understudied, primarily due to the absence of dedicated annotated datasets. Furthermore, public communication has recently shifted towards video-centric platforms, where narratives are conveyed through multimodal signals and consumed at scale. Despite this shift, narratives in videos remain largely unexplored. To bridge these gaps, we introduce MigrationNarrate, the first multimodal dataset for detection of migration narratives in the UK, consisting of 1,115 YouTube video transcripts annotated using a two-level taxonomy of 12 migration super-narratives and 53 narrative labels. This paper details the dataset design, collection, and annotations; together with benchmark results using a combination of pre-trained encoder models and both open- and closed-source Large Language Models. Finally, a thorough error analysis offers insights for future work.

---


### 106. [Jacobian-guided Noise Injection for Quantization Robustness in Large Language Models](https://arxiv.org/abs/2608.20988)

**<font color=#1a73e8>作者：</font>** Deepanshu Pandey, Arnav Chavan, Nahush Lele 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization of Large Language Models (LLMs) is often hindered by the sensitivity of the self-attention mechanism to discretization errors. We identify the softmax operator as a bottleneck for quantization stability due to its sensitivity to outliers and state-dependent Jacobian. We theoretically establish that suppressing the norm of this Jacobian helps in bounding quantization-induced performance degradation. Based on this, we propose Jacobian-Guided Noise Injection, a training strategy that injects zero-mean Gaussian noise into pre-attention logits, with variance derived directly from the Jacobian Frobenius norm. Unlike prior approaches that rely on heuristic or penalise jacobian directly, our method provides a way to identify the optimal noise variance based on the local attention sensitivity. We evaluate the method on SOTA LLM architectures, where it demonstrates improved robustness over popular PTQ methods. Empirical analysis reveals that the proposed method gives up to +37% relative gains on Top-1 accuracy on ImageNet-1K for SigLIP and improves relative perplexity by upto 40% on WikiText for language models in low bit quantisation settings, proving the efficacy of the approach.

---


### 107. [Latent Ordinal Evidence, Misaligned Outputs: Inference-Time Ordinal Lens Alignment for Multimodal LLMs](https://arxiv.org/abs/2608.20999)

**<font color=#1a73e8>作者：</font>** Haiming Li, Yingsheng Liu, Jingmin Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal LLMs apply the language model interface to visual inputs, where ordinal regression tasks such as age estimation, image quality assessment, and disease grading require autoregressive decisions over ordered class labels. We ask whether MLLMs reliably convert internal ordinal evidence into ordered digit-token outputs. Across four ordinal benchmarks and four MLLM backbones, ordinal labels are linearly recoverable from hidden states with Spearman correlation up to 0.938, and a task-designed prompt further sharpens this structure. Yet native digit-token outputs weakly expose it: the unembedding matrix filters the ordinal direction, and the digit-token row space retains below 1.15% across all 16 model-dataset combinations, with a 16 to 77 absolute-point accuracy gap between linear-probe and native outputs. We introduce Ordinal Lens Alignment (OLA), a frozen-backbone inference-time method that trains lightweight W_S-anchored lenses on mid-to-deep decoder layers, fuses them into an ordinal distribution, and corrects only digit-token logits at generation. OLA outperforms the SOTA LoRA-tuned OrderChain baseline in most settings while keeping the MLLM frozen, surpasses discriminative ordinal baselines in most cells, and improves over an offline lens in every setting.

---


### 108. [Target-Aware Calibration Data Selection for Preserving Uncertainty in Quantized Language Models](https://arxiv.org/abs/2608.21019)

**<font color=#1a73e8>作者：</font>** Zhen Yang, Sizai Hou, Kaiwen Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantization is widely used to deploy large language models, but its effect on uncertainty behavior, such as confidence, margins, and abstention, is rarely treated as a primary objective. We frame calibration-data selection for quantization as a target-dependent uncertainty-preservation problem. Different deployments emphasize different regions of the input distribution, yet prior work mainly optimizes accuracy-oriented compression metrics or adjusts scores after quantization. We formalize this goal with distributional and boundary preservation risks, and provide a simple mixture-mismatch argument explaining why no single calibration recipe should be expected to fit all targets. We introduce Doubt-Preserving Quantization (DPQ), a lightweight pre-quantization recipe family that uses full-precision predictions to construct target-aligned calibration mixtures of high-doubt examples and generic anchors. Across 8 language models, 9 NLP benchmarks, and 22 comparison methods, the leading fixed recipe changes with the preservation target: DPQ-r75 leads on SQuAD2 answerability-boundary preservation, while milder or single-signal variants, including DPQ-r50, confidence-only, and entropy-only, better preserve broad multiple-choice QA behavior. These results show that calibration data should be selected for the specific full-precision score behavior a deployment needs to preserve, rather than treated as a fixed quantization detail.

---


### 109. [Free-Text Evaluation of LLMs for 5G Domain Knowledge and Fault Analysis using LLM-as-Judge](https://arxiv.org/abs/2608.21021)

**<font color=#1a73e8>作者：</font>** Rishiraj Sengupta, Sotiris Chatzimiltis, Mohammad Shojafar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-world fault analysis in 5G and emerging 6G networks demands domain expertise to analyze free-text diagnostics, including root-cause explanations and recommended actions. LLMs have emerged as a promising approach to automating this, yet whether lightweight, edge-deployable models are capable of performing in-depth free-text diagnostics remains an open question. While existing benchmarks rely on restrictive MCQs with fixed answer keys, this paper evaluates 5G domain understanding and fault analysis in a free-text generation format. Transitioning to this paradigm requires evaluating lightweight, edge-deployable AI models on open-ended diagnostic reasoning, alongside a dependable framework to validate these text outputs at scale. To address this we evaluate three lightweight LLMs, Claude-Haiku-4.5, GPT-5.4-Mini, and Gemini-3.1-Flash-Lite, on free-text 5G domain knowledge and fault-analysis tasks across three benchmarks, TeleQNA ORAN FT, 5G-Faults FT, and TeleInter FT. Three independent frontier judges score outputs, and pairwise inter-judge agreement is measured as an empirical test of the LLM-as-Judge methodology. All three models reach at least 90% accuracy on fault diagnosis, while zero-shot recall of 3GPP and O-RAN specifications remains the critical gap, with all models scoring below 60%. Mean inter-judge agreement is at least 0.90 across all runs, indicating that multi-judge LLM scoring produces consistent, reproducible grades for open-ended telecom responses. Operationally, Gemini-3.1-Flash-Lite offers the best efficiency trade-off, combining competitive accuracy with the lowest inference cost and latency, making it the most suitable candidate for production telecom deployments.

---


### 110. [Recognition-Conditioned Reasoning: A Training-Free Multimodal-LLM Pipeline for Fine-Grained Micro-Action Understanding](https://arxiv.org/abs/2608.21022)

**<font color=#1a73e8>作者：</font>** Fengshun Wang, Jin'ang Han, Zhigang Tu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Micro-actions are subtle, short, low-amplitude body movements, such as a fidgeting hand or a slight head tilt, that humans perform with little conscious intent yet that reliably leak emotional and psychological state. Understanding them goes beyond assigning a label: a model must also describe which body parts move and reason, faithfully, about why a clip warrants a particular fine-grained category. We present the training-free, prompt-only system that won first place in the fine-grained understanding track (MA-Bench) of the MAC~2026 Micro-Action Challenge, where both fine-tuning and ground-truth supervision are disallowed. Built entirely upon frozen multimodal large language models (MLLMs), the system dynamically routes each of the eight sub-tasks to the MLLM empirically best suited for that task: a discriminative MLLM for closed-ended recognition tasks and a generative MLLM for open-ended description and reasoning tasks. This architecture achieves a statistically significant performance advantage on open-ended tasks, attaining an average score of 2.68 (on a five-point scale) compared to 1.44 for the second-best approach.

---


### 111. [RODE: A Radial-Orthogonal Decoupled Engine for Optimization](https://arxiv.org/abs/2608.21024)

**<font color=#1a73e8>作者：</font>** Guoxiang Xu, Bince Qu, Qi Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern neural network training increasingly uses matrix-aware optimizers, yet their conditioned matrix step is typically added directly to the weight, jointly changing its norm and direction. This interaction matters because the current norm determines angular motion, while directional learning can drive norm growth and thereby alter later steps. We introduce RODE, which gives the radial and directional components separate update rules and step sizes. RODE explicitly updates the matrix Frobenius norm through a scalar radial rule, while its directional channel performs Newton--Schulz-conditioned updates in the tangent space. Controlled GPT-2 interventions show gains from both direct norm control and RODE's directional update. Across two language-modeling and two image-classification tasks, RODE outperforms both Muon variants in every direct comparison and ends with lower full-model norms. At 1.5B scale, using the learning rate transferred directly from the Qwen2-style LM sweep, RODE lowers loss from 4.145 to 3.346 and final global norm from 11964 to 2183 relative to Muon RMS, with fixed-radius RODE improving further. For Qwen3.5-9B full-parameter fine-tuning, all six optimizers use the same tuning budget and the same formal-training and evaluation settings; RODE outperforms both Muon variants on all four evaluation tasks and attains the highest mean on GSM8K and MATH-500. Thus, decoupling radial and directional dynamics offers a more effective and controllable approach to matrix optimization.

---


### 112. [Don't Solve, Just Compare: Tiny Advisors for Runtime Intervention in LLM Agents](https://arxiv.org/abs/2608.21027)

**<font color=#1a73e8>作者：</font>** Yanze Jiang, Mingxuan Li, Yuhao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are emerging as an important paradigm for real-world tasks that require reasoning, tool use, and sequential decision-making. As these agents operate over longer horizons, runtime intervention offers a way to improve reliability without retraining the underlying actor. Failure detection alone is insufficient. Effective intervention must also provide a useful direction for recovery. Existing approaches often rely on an expert solver or a critic that generates task-specific corrections, incurring either the cost of another capable solver or the capacity demands of a task-capable critic. We introduce Comparison-Only Tiny Advisor (COTA), a comparison-only framework for constructive runtime intervention. In COTA, a tiny comparator judges whether sampled alternatives lead to better continuations than the actor's proposal, and repeated comparisons determine when intervention is warranted. We train the comparator using pairwise supervision constructed from same-prefix counterfactual branches. Preferred alternatives are returned as non-binding advice, leaving the original actor to replan. Across WebShop, ALFWorld, and tau^3-Retail with three actors, COTA improves all nine evaluation settings and outperforms the compared baselines. These results show that constructive runtime intervention can remain effective even when the auxiliary model has substantially weaker task-solving capability than the actor.

---


### 113. [COMET: Contrastive Motion-Enhanced Temporal Reasoning for Video Multimodal Large Language Models](https://arxiv.org/abs/2608.21030)

**<font color=#1a73e8>作者：</font>** Chenghua Zhu, Zhaolu Kang, Qifan Shi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video multimodal large language models have advanced significantly, yet fine-grained motion-temporal understanding remains fragile. The core bottleneck is not only sparse frame sampling, but also the lack of a complete temporal modeling pipeline for explicitly representing frame-to-frame change, enabling appearance-motion interaction, and optimizing temporal direction sensitivity. We propose COMET, a temporally grounded framework that systematically strengthens video MLLMs through explicit temporal representation, appearance-motion fusion, and direction-aware optimization. Architecturally, COMET introduces a temporal motion branch built on Taylor frame differences and injects its motion evidence into the appearance stream via temporal attention bias-enhanced cross-attention. For optimization, COMET combines temporal prior distillation with a forward-reverse TC-GRPO stage that turns temporal order into a direct learning signal and strengthens the model's use of directional motion patterns encoded by the temporal motion branch. The method achieves consistent overall improvements with a pronounced motion-temporal bias: on Qwen3-VL-8B, action-centric tasks (STAR, SSv2) improve by 4.9% on average, temporal reasoning tasks (NExT-QA, CLEVRER, LLaVA-178K) by 2.1% over BL-GRPO, while static perception tasks (PerceptionTest) remain on par. The same gain pattern also transfers to InternVL2.5-8B, indicating that COMET generalizes across model families.

---


### 114. [Evaluating Large Language Model Performance on International Maritime Dangerous Goods Code Compliance](https://arxiv.org/abs/2608.21036)

**<font color=#1a73e8>作者：</font>** Alexander Thomas, Hubert P. H. Shum, Darren Nellis 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The transport of dangerous goods by sea is a high-consequence activity governed by the International Maritime Dangerous Goods (IMDG) Code, a complex regulatory framework where errors in classification, packaging, stowage, or segregation can result in fire, explosion, toxic release, or loss of life or vessel. Correct compliance requires accurately interpreting hundreds of pages of interacting provisions, updated on a two-year amendment cycle. Practitioners increasingly use Large Language Models (LLMs) as decision-support tools, yet no systematic evaluation exists of whether they can reliably interpret IMDG requirements for safety-critical use.
This paper introduces DGEval, the first benchmark for evaluating LLM knowledge of IMDG Amendment 42-24. Built from expert-written questions on the NCB Hazcheck e-learning platform and structured lookups from the Dangerous Goods List (DGL), it comprises 1,678 questions across multiple-choice, open-ended, DGL lookup, and regulatory identification tasks. We evaluate 13 models from six providers across multiple thinking configurations, including one maritime domain-specific fine-tuned model, and test the effect of web search.
Although the best-performing model exceeds the human practitioner baseline on multiple-choice questions, all models are weakest in the operationally safety-critical areas of stowage, segregation, and regulatory recall. These results indicate that LLMs may support compliance tasks, particularly structured DGL lookups with web search, but unreliability in operational areas and regulatory-text recall means human oversight and authoritative source verification remain necessary before deployment in any safety-critical context. DGEval is designed as a safety assurance instrument to be applied continuously as models evolve, not as a settled characterisation of current capability.

---


### 115. [$Z^2$-ACT: End-to-End Verifiable Agentic Intent Control for Open 6G RAN](https://arxiv.org/abs/2608.21049)

**<font color=#1a73e8>作者：</font>** Sunder Ali Khowaja, Kapal Dev, George C. Alexandropoulos  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the progression in open and disaggregated 6G radio access networks, it is expected that the system will be able to host multi-vendors. In order to host multi-vendors, it is essential that AI-assisted control loops remain safe, verifiable, and auditable under concurrent operator intents and untrusted model inputs. The existing studies address the agentic coordination, formal intent constraints, zero-trust prompt verification and cryptographic accountability in isolation, which leaves pre-realization safety, continuous semantic verification and cross-domain audit incomplete when used individually. In this regard, we propose zero-knowledge auditable control and zero-trust verifiable agentic intent architecture ($Z^2$-ACT), which integrates the aforementioned four primitives across the non-real-time and near-real-time RICs. We encode the typed Intent Contracts as operator goals while the large language model inputs are only admitted after a practical adversarial intent check. The skill sequences in the proposed study are released only when a self-management gate is satisfied while every successful commit is recorded as a binding commitment with a zero-knowledge proof. Our experimental evaluation on public ColO-RAN measurements compares the full architecture against targeted ablations and a conventional reinforcement-learning baseline. A live large language model is used in the non-real-time path to translate operator intents into Intent Contracts; we report translation accuracy, the rate of invalid or hallucinated contracts, non-real-time latency, and behavior under adversarial or misleading intents. Near-real-time control remains trace-driven on the public KPM sequences. Results indicate improved actuation filtering and attack resilience at modest latency and signaling cost inside the near-real-time envelope.

---


### 116. [Designing a Robust LLM-Based Evaluation System for Agentic AI in Drug Discovery Through Human Alignment](https://arxiv.org/abs/2608.21057)

**<font color=#1a73e8>作者：</font>** Emma Granqvist, Rocío Mercado, Samuel Genheden  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic large language model (LLM) systems are reshaping scientific workflows in chemistry and drug discovery, but evaluating their open-ended, tool-augmented outputs remains a fundamental bottleneck. Reference-based metrics such as BLEU and ROUGE fail to capture semantic correctness, while expert human evaluation does not scale to the iteration speed these systems demand. The LLM-as-a-Judge paradigm has emerged as a scalable alternative, but existing drug discovery benchmarks deploy LLM judges without validating their alignment with human experts. In this work, we present an LLM-as-a-Judge evaluation framework for ChatInvent, an agentic drug discovery assistant deployed at AstraZeneca, with four contributions. First, we define four output-quality evaluation dimensions---Completeness, Relevancy, Structural Clarity, and Scope Adherence---alongside deterministic Tool Call Correctness checks. Second, we validate the judge through a human alignment study with five expert annotators, comparing Gemini 3.1 Pro, Claude Opus 4.7, GPT-5, and Llama 3.1 70B as candidate judges. Third, we optimize the best-performing judge using few-shot demonstrations of human-annotated examples, improving alignment with the human majority vote from 0.80 to 0.86. Fourth, applying the optimized judge to 70 held-out questions, we surface concrete limitations and find that informal phrasings do not systematically degrade output quality; if anything, it is helpful to have the LLM rewrite the original question before querying the agent. Our framework provides a reusable template for human-aligned evaluation of agentic systems in scientific domains.

---


### 117. [PromptResponse: Optimizing Prompts for LLM Coding Tasks](https://arxiv.org/abs/2608.21074)

**<font color=#1a73e8>作者：</font>** Erik Thureck, Robert Kühnen, Tim Jacobowitz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in research workflows and software development pipelines, yet their output remains sensitive to input prompt variations. This paper presents $\unicode{x00AB}$PromptResponse$\unicode{x00BB}$, a controlled study examining how formatting and LLM-based tuning of coding task prompts affect the resulting code's performance, efficiency, and stability. Using five semantically identical yet syntactically distinct variants of the HumanEval dataset$\unicode{x2014}$baseline, JSON, Markdown, YAML, and an LLM-tuned version$\unicode{x2014}$we had GPT-4o solve its coding problems over 8200$\unicode{x00A0}$executions. Our results show that consistent formatting$\unicode{x2014}$especially JSON$\unicode{x2014}$improves generation efficiency and syntactic stability, with minor gains in task performance. Conversely, the LLM-tuned prompts resulted in significantly degraded task performance without significant improvements in any other dimension. These findings suggest that low-effort reformatting alone can yield measurable improvements, while tuning must account for model alignment. We conclude our work with providing a set of practical recommendations informed by our results as well as releasing our dataset variants and evaluation pipeline for future work.

---


### 118. [Causal Modeling of Adverse Pregnancy Outcomes via Adaptive LLM Proposals](https://arxiv.org/abs/2608.21079)

**<font color=#1a73e8>作者：</font>** Kavimayil P. Komarasamy, Saurabh Mathur, Ameet Soni 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adverse Pregnancy Outcomes (APOs) such as preterm birth and gestational diabetes can have long-term consequences for both the mother and child, yet an understanding of their causes remains elusive. Causal discovery in this domain is especially challenging due to a paucity of data and incomplete domain knowledge. As a result, pure data-driven methods fail, and Large Language Model (LLM) outputs remain inconsistent or contradictory. We introduce a neurosymbolic framework for generating plausible causal hypotheses that iteratively combines the broad prior knowledge of LLMs with empirical scoring on data. Our method treats the LLM as an adaptive proposal distribution, generating hypotheses that are scored against empirical data; the resulting high-scoring graphs are then used to update the LLM's context, steering subsequent generations toward more promising regions of the hypothesis space. We evaluate our approach on a real-world clinical dataset for modeling APOs and their risk factors, comparing our results against an expert-constructed causal graph. Our method recovers all expert-validated edges and identifies additional plausible causal relations not previously listed by experts, potentially providing new insights for targeted interventions.

---


### 119. [Jokes Aside: Measuring the Semantic Distance of Double Meanings](https://arxiv.org/abs/2608.21087)

**<font color=#1a73e8>作者：</font>** Fabio De Ponte  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have significantly enriched the toolkit for computational humor research, particularly in the automated generation of jokes and puns. A key innovation, contextual embedding vectors, offers new opportunities to revisit and refine earlier hypotheses. Notably, Petrovic and Matthews (2013) proposed a joke generation model based on the scheme "I like my X like I like my Y, Z" (e.g. "I like my ice like I like my dreams, crushed"). They suggested that joke hilarity increases with: a) frequent association of Z with X and Y, b) rarity of Z, c) ambiguity of Z, and d) meaning distance between X and Y. Building on this, Winters et al. (2019) proposed a set of metrics, based on Google Ngrams and Word2Vector. In this work, three out of their five metrics are revisited with word embeddings: obviousness, compatibility, and comparison. Another measure, symmetry, defined as closeness of Z to both X and Y, is introduced here for the first time. Two models were used to collect the embedding vectors (OpenAI text-embedding-3-small and MiniLM all-MiniLM-L6-v2) on three datasets: JokeJudger, Expunations, and rJokes. The last two datasets, Expunations, and rJokes, were expanded by adding paired sentences that captured the ambiguous expression at the core of each joke in its two different meanings. Results revealed that models trained on the proposed metrics performed poorly in predicting humor ratings: on JokeJudger, the best model achieved 57.1% accuracy, below the 61.5% baseline, while performance on Expunations and rJokes was even lower. Nevertheless, the symmetry metric seems consistently associated with higher-rated jokes, suggesting it may capture a necessary -though not sufficient- property of humor.

---


### 120. [When the Feature Pool Goes Algorithmic: Extending Mufwene's Ecology of Language Evolution to LLM-Mediated Exposure](https://arxiv.org/abs/2608.21088)

**<font color=#1a73e8>作者：</font>** Kunmei Han  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mufwene's ecological model locates language evolution in competition among variants contributed by individual idiolects and in speakers' selection from linguistic material made available through interaction. Large language models (LLMs) complicate this architecture without requiring the locus of selection to move away from human speakers. This article argues that LLMs are best treated as distributional mediators: they aggregate language produced across human populations, transform its distribution through training and post-training, and redistribute model-specific outputs at scale. I call the resulting ecological process algorithmic reweighting of the speaker-accessible distribution: model mediation can alter the relative frequencies with which competing variants reach human selectors. Emerging evidence on model-specific linguistic profiles and lexical uptake is consistent with parts of this pathway, but does not establish inevitable convergence. Human social evaluation remains decisive: model-associated forms may diffuse and become conventionalized, become socially recognizable as 'AI-like' and subsequently avoided, or fail to diffuse in the first place. The proposal extends Mufwene's feature-pool ecology one step upstream of speaker selection and yields testable predictions about uptake, model-version effects, convergence, and social reversal.

---


### 121. [Can Legal AI Know When It Is Wrong? And Do Students Know When It Is?](https://arxiv.org/abs/2608.21089)

**<font color=#1a73e8>作者：</font>** Angel Mary John, Vipin Kumar Singh, Jerrin Thomas Panachakel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Integrating Large Language Models (LLMs) into the Indian judiciary promises access to justice but introduces severe risks. We identify the 'inertia of confidence'--an overconfidence phenomenon analogous to the Dunning-Kruger effect where LLMs provide incorrect legal verdicts with near-maximum confidence, driven by a hypothesized 'precedent overfitting' bias. Phase I of our socio-technical audit tested ChatGPT (GPT-5.2), Meta AI, and Perplexity AI on a 60-case battery regarding the Indian Contract Act, 1872, and the shift toward statutory enforcement of specific performance. We introduce the High-Confidence Error Rate (HCER) to quantify incorrect verdicts delivered with dangerous certainty (>= 9 on a 1-10 scale). All models struggled with statutory updates. Meta AI proved most vulnerable (31.7% HCER), frequently misapplying pre-amendment rules with a 9.1/10 mean confidence, followed by Perplexity (15.0%) and ChatGPT (6.7%).
Phase II investigated human vulnerability to this overconfidence via a survey of Indian law students (N=380). Verification often functions as a reactive adaptation to machine hallucinations: students encountering fabricated citations reported higher verification scores (4.2/5) than those with no such encounters (2.8/5). Furthermore, while 81.6% knew submitting hallucinated cases can lead to contempt-of-court, 71.1% received no formal training on ethical AI use. We propose shifting toward adversarial legal research pedagogy and implementing source-grounded verification architectures to prevent systemic professional negligence.

---


### 122. [When Trust Meets Truth: Trust-Truth Separability in LLM-as-Judge](https://arxiv.org/abs/2608.21097)

**<font color=#1a73e8>作者：</font>** Xin Sun, Di Wu, Yuchen Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-as-Judge systems can produce multi-dimensional evaluations, such as trustworthiness, reliability, and factuality, and these outputs are often interpreted as independent evidence. We test this assumption for a common pair of judgments: trust scoring and binary truth classification. On correctness-controlled QA, LLM judges align trust scores with truth verdicts more tightly than human behavioral reference, suggesting weaker separations between trust and truth judgment. We then apply stress tests by changing only source cues of identical QA between Human and AI. Source attribution shifts not only trust scores but also truth verdicts and logit-derived correct-side probabilities. Results show that current LLM-as-Judge protocols should not treat trust scores as independent evidence for truth judgments.

---


### 123. [ClawSentry: A Progressive Multi-Tier Security Monitor for Safeguarding Autonomous LLM Agents](https://arxiv.org/abs/2608.21101)

**<font color=#1a73e8>作者：</font>** Kai Wang, Zeming Wei, BiaoJie Zeng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As large language model (LLM) agents move from conversation to executing code, reading local files, and orchestrating external tools, a single agent hijacked by a malicious third-party skill can cause data exfiltration, privilege escalation, or cascading compromise. We argue that agentic risk is progressive: it can enter at four loci of the agent control loop--skill admission, invocation-time intent, execution-time effect, and post-action consequence--while a denied dangerous objective can reappear across surface forms, tools, or turns; existing safeguards are typically local to one lifecycle boundary or one call. Guided by this threat model, we present ClawSentry, an open-source, framework-agnostic security supervision gateway for agent runtimes. Before a skill package is ever executed, First-use Skill Package Review (FSPR) audits it under a deterministic evidence floor, escalating unresolved cases to bounded read-only agentic review (locus A). At runtime, a three-tier progressive decision engine--a deterministic L1 layer, a rule-anchored L2 semantic reviewer, and a read-only L3 evidence-seeking agent--spends contextual review only on the residual ambiguity, while a session-level anti-bypass mechanism recognizes tool-switching and rephrased retries (loci B--C); a post-action path feeds high-severity evidence non-retroactively into later review (locus D). An Agent Harness Protocol (AHP) abstraction applies one policy across Codex, Claude Code, Kimi CLI, and Gemini CLI without modifying agent internals. On SkillInject with Codex/GPT-5.4, contextual ASR falls from 39.55% to 2.61% while contextual TSR moves only from 83.78% to 83.05%. Across five Work Agents on the full SkillsSafety benchmark, ClawSentry confines ASR to 9.09--15.03% from 33.5--49.7% unprotected, and aggregate TSR on clean skills remains 98.7%.

---


### 124. [Large Language Models at the Intersection of Software Engineering and Software Security:An Evidence-Centered Structured Survey and Research Agenda](https://arxiv.org/abs/2608.21107)

**<font color=#1a73e8>作者：</font>** Wei Lin, Tao Zhou, Zhaofei Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are moving from code completion toward repository-scale agents that retrieve context, edit files, execute tools, and participate in security-sensitive workflows. The evidence for these systems, however, remains divided between software engineering evaluations centered on functional task completion and software security evaluations centered on vulnerability detection, secure generation, or exploit-oriented validation. This evidence-centered structured survey synthesizes representative work available through May 31, 2026 across software engineering tasks, software security tasks, adaptation mechanisms, artifact granularity, and evaluation design. In addition to a task taxonomy, we introduce an assurance framework that separates functional correctness, security, operational reliability, evidence provenance, and agent authority. The review shows that execution feedback and repository access can substantially improve engineering task completion, but do not by themselves establish security; conversely, static-analysis labels or vulnerability-classification scores rarely establish deployable correctness. We identify recurring validity threats--weak test oracles, duplicated and temporally leaked data, changing agent harnesses, proxy-only security checks, and under-reported budgets and human intervention--and derive a minimum reporting protocol for cross-study comparison. The resulting research agenda prioritizes jointly secure-and-functional benchmarks, repository-scale threat models, calibrated human oversight, longitudinal maintainability evidence, and reproducible agent evaluation. The central conclusion is that model capability should be judged as an assurance case supported by task-appropriate evidence, rather than by a single benchmark score.

---


### 125. [Llama-Mobile: Efficient 2.7-Bit Quantization of VLMs](https://arxiv.org/abs/2608.21134)

**<font color=#1a73e8>作者：</font>** Luka Ribar, Jeevan Bhoot, Douglas Orr  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying vision-language models (VLMs) on mobile devices is challenging due to their significant memory and compute requirements. We present a framework for quantizing VLMs for efficient inference on resource-constrained hardware. Our approach combines a quantization pipeline that uses the model itself to generate training data and does not require access to the training setup, with a novel 2.7-bit-per-parameter format supporting efficient execution on Arm CPUs. We validate our approach by compressing the Llama 3.2 11B Vision Instruct model to 3.7 GB with 8-bit activations, preserving strong performance on a set of standard visual question answering tasks.

---


### 126. [Stream3Dv2: Geometric-Semantic Fusion Enhanced Streaming Zero-Shot 3D Scene Understanding](https://arxiv.org/abs/2608.21136)

**<font color=#1a73e8>作者：</font>** Jie Xu, Na Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, open-vocabulary zero-shot 3D scene understanding using vision foundation models has emerged as a promising alternative to data-intensive supervised methods. However, deploying these models in real-world scenarios is severely hindered by their inability to efficiently handle streaming RGB-D inputs and their inherent vulnerability to noise 2D segmentation masks. To address these critical limitations, we propose Stream3Dv2, a novel training-free framework designed for robust streaming 3D perception. Stream3Dv2 processes sequential data through an original nested local-to-historical architecture, capturing multi-view consistency while circumventing the high computational overhead so as to support timely responses. At its core, we introduce a comprehensive geometric-semantic fusion mechanism that resolves geometric noise and semantic ambiguity by explicitly utilizing semantic guidance and formulating 3D segmentation as solving point-and-set merging and partitioning problems. Furthermore, we present an innovative manifold-distance-based point cloud refinement strategy. This approach leverages local manifold graphs for point-to-manifold optimization that mitigates the boundary delineation failures caused by Euclidean-distance metrics, and employs geometric bounding boxes to dynamically activate and update historical instances for achieving rapid manifold-to-manifold refinement. Extensive experiments on public datasets demonstrate that Stream3Dv2 consistently outperforms existing baselines in foundational open-vocabulary streaming 3D segmentation and detection. Finally, we show that integrating our framework with an LLM-based agent enables advanced language-driven 3D scene understanding, underscoring its potential for open-world embodied intelligence. Code will be updated at this https URL.

---


### 127. [A Modular Agent for Reliable and Auditable Spatial Relation Verification in CT Scans](https://arxiv.org/abs/2608.21140)

**<font color=#1a73e8>作者：</font>** Simon Vincent Abel, Heiko Hillenhagen, Michael Götz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable spatial understanding is an important prerequisite for future medical vision-language systems that aim to support radiological report generation and structured image understanding. While modern vision-language models (VLMs) show promising performance on many medical imaging tasks, recent evidence suggests they remain weak in controlled spatial reasoning and often fail to reliably ground spatial relations in image evidence. Given that radiological reasoning hinges on understanding the relative positions of anatomical structures and findings, this spatial weakness poses risks to diagnostic accuracy. We present a modular medical imaging agent for binary spatial relation verification in axial CT slices. Instead of directly predicting spatial answers end-to-end, the system decomposes the task into explicit stages: language parsing, anatomical localization, and deterministic geometric verification. Natural-language queries are converted into structured relation tuples, queried organs are localized with a YOLO-based detector, and the final spatial decision is computed from object centers using deterministic geometric rules. We evaluate the approach on the held-out MIRP spatial QA benchmark and compare it against representative end-to-end VLM baselines. The best-performing hybrid configuration reaches 94.1% accuracy and 94.2% F1, outperforming direct Qwen2-VL prompting by 42.5 percentage points in accuracy, while preserving interpretable intermediate representations and auditable reasoning stages. The results suggest that explicit modular spatial verification can serve as a promising building block for future report-oriented medical imaging agents.

---


### 128. [COEC: Calibrated Orthogonal-Equivalence Compensation for Structured Pruning of Large Language Models](https://arxiv.org/abs/2608.21142)

**<font color=#1a73e8>作者：</font>** Peiqi Yu, Nam Ling, Wei Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structured pruning reduces the size and inference cost of large language models (LLMs) by removing weight columns, but the resulting output error can degrade accuracy. Existing training-free compensation methods use an additive bias or a single orthogonal rotation on the output side of the retained weight. These corrections leave its input singular frame unchanged and therefore limit how the retained weight can adapt after column removal. We propose COEC (Calibrated Orthogonal-Equivalence Compensation), a training-free compensation framework that applies alternating left and right orthogonal rotations to the retained weight. The right rotation is optimized on a reduced Stiefel manifold, while singular values are rescaled using generalized cross-validation to select the regularization strength for each layer. COEC further tempers the calibration Gram matrix to reduce the dominance of high-energy activation directions and introduces an alignment penalty that preserves the geometric relation between adjacent attention this http URL components use second-order statistics from a small calibration set and require neither backpropagation through the LLM nor retraining of the model parameters. COEC is independent of the column pruning criterion and can be applied to multiple structured pruning methods. Experiments on the Llama-3, Llama-3.1, and Qwen2.5 model families across multiple structured sparsity levels show that COEC improves perplexity on every model and zero-shot accuracy in most settings over existing compensation methods, with larger gains at higher sparsity. These results show that post-pruning compensation can recover part of the performance lost to column removal.

---


### 129. [Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics](https://arxiv.org/abs/2608.21165)

**<font color=#1a73e8>作者：</font>** Chenguang Pan, Airui Meng, Youmi Suk  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Learning analytics increasingly relies on flexible machine learning (ML), but the model opacity and the burden of deployment prevent these tools from reaching educational practice. We propose a two-stage fine-tuning pipeline that distills a fitted black-box estimator and its post hoc interpretation (the mentor) into a small, open-weight large language model (LLM; the mentee) that returns an individual-level estimate and explains in natural language. The design is estimator-agnostic and paired with a faithfulness-first evaluation framework that audits every narration against the attribution it claims to describe. We design a simulation study that separates distillation loss from estimator loss by comparing an oracle mentor with a realistic ML mentor. Given an oracle signal, distillation with a two-billion-parameter LLM model is nearly lossless in recovering the effect surface (r > .90), perfectly ranking the important variables, and citing no spurious covariate. Under a realistic estimator, almost all remaining error originates upstream. We find that fluency is no evidence of correctness since narration quality is independent of signal quality, and decision quality collapses toward the majority action in severely imbalanced settings. Applied to a nationally representative dataset, the pipeline recovers the finding that advanced mathematics coursework benefits students least likely to enroll in four-year college the most, with 98.8% of narrations passing the audit and no fabricated quantities. The result is a single fine-tuned LLM that predicts and explains offline on a commodity laptop, so student records never leave the machine.

---


### 130. [Is Visual Prompting All You Need? Studying VLM Spatial Reasoning under Progressive Visual Scaffolds](https://arxiv.org/abs/2608.21170)

**<font color=#1a73e8>作者：</font>** Lars Benedikt Kaesberg, Tianyu Yang, Florian Valentin Wunderlich 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have advanced rapidly in multimodal reasoning, yet recent work shows that their failures often reflect an interaction between visual grounding and downstream reasoning. What remains less clear is how the visual presentation of a task shapes model performance and failure modes when the underlying reasoning problem is unchanged. We study this question in SPaRC, a benchmark for grid-based visual spatial planning, by introducing lightweight input-side scaffolds that preserve the visual modality while making spatial structure more accessible. Across multiple VLMs, these scaffolds improve task accuracy over the original visual setting by up to 34.0 percentage points and further complement GRPO-based training, yielding up to 4.6 additional accuracy points compared with near-zero gains on the original visual input. Analyses on both end-to-end task solving and object detection show that these gains are closely tied to reductions in grounding-related errors, while rule reasoning remains comparatively challenging. We find that visual presentation is a central factor that determines whether VLM benchmarks measure grounded perception, downstream reasoning, or a mixture of both.

---


### 131. [Thermo-FL: Thermal-Aware Robust Federated Fine-Tuning of Large Language Models for Edge AI](https://arxiv.org/abs/2608.21172)

**<font color=#1a73e8>作者：</font>** Shiva Shrestha, Kazi Shaharair Sharif, Zongxing Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated fine-tuning enables large language models to adapt on edge devices without centralizing private data, but practical deployments must address hardware instability and adversarial update corruption together. Thermally constrained clients may throttle, slow local training, or delay synchronous aggregation, while Byzantine clients and communication-layer adversaries can corrupt the updates used to form the global model. To address these challenges, we present Thermo-FL, a thermal-aware federated LoRA fine-tuning framework that uses device temperature as an active control signal for local adapter training and sparse update transmission. On the client side, Thermo-FL adjusts the active LoRA-layer fraction and transmitted update density as devices heat or cool, reducing workload under thermal stress. On the server side, Thermo-FL introduces TERRA, a robust aggregation pipeline for dynamically sparse LoRA updates that combines norm filtering, mask-aware directional validation, adaptive active-coordinate clipping, and mask-aware aggregation. We evaluate Thermo-FL using both a large-scale emulator and a Jetson-based physical testbed. In the emulator, Thermo-FL improves robustness under adversarial sparse aggregation and achieves the strongest BoolQ accuracy across clean and attack settings while remaining competitive on GSM8K. In the physical prototype, Thermo-FL stabilizes device temperature, reduces compressed upload size through bitmap sparse encoding, and preserves GSM8K utility under sign-flip/scale and MITM perturbations. These results show that secure edge LLM adaptation should jointly consider hardware behavior, workload regulation, sparse communication, and aggregation robustness.

---


### 132. [From Search Agents to Dissemination Interfaces: Understanding Human Trust in Health Information from Conversational Search](https://arxiv.org/abs/2608.21177)

**<font color=#1a73e8>作者：</font>** Xin Sun, Rongjun Ma, Xiaochang Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) deployed through Conversational User Interfaces (CUIs) are transforming health information-seeking by offering immediate, interactive experiences compared to traditional search engines like Google. However, how trust is influenced by both the types of search agents and the interface used to disseminate the information remains underexplored. This research integrates two mixed-methods studies (lab sessions and interviews) to comprehensively explore trust perceptions in health information across different search agents and dissemination interfaces. In Study 1 (N=21), we investigated trust in health information sourced from ChatGPT and Google across three types of health-related search tasks. Results showed significantly higher trust in health information from ChatGPT, highlighting the promise of LLM-powered conversational search. Building on this, Study 2 (N=20) extended the investigation to explore how the dissemination interface influences trust in LLM-sourced health information by comparing three interfaces: text-based, speech-based, and embodied, all sourcing from the same LLM. Findings revealed significant trust variations across the dissemination interfaces. Interviews from both studies revealed key factors influencing trust in LLM-powered conversational search, including source credibility, participants' search autonomy, and prior knowledge as well as the interaction style and modality. Our findings highlight the potential of LLM-powered conversational search to transform health information-seeking, underscoring the interplay between the credible search agents and the thoughtfully designed dissemination interfaces in shaping trust. These insights are crucial for developing effective, trustworthy LLM-powered health tools to enhance the health information-seeking experience.

---


### 133. [A Neurosymbolic Approach for Constructing Planning Domain Models from Clinical Narratives](https://arxiv.org/abs/2608.21186)

**<font color=#1a73e8>作者：</font>** Ranveer Singh, Saurabh Mathur, Michael Skinner 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Surgical procedures such as laparoscopic appendectomy are complex, high-stakes processes, yet formalizing their workflows for decision support remains a significant challenge. Inducing probabilistic planning domain models in this setting is particularly difficult due to the lack of structured event data and the prevalence of implicit actions in clinical narratives, which neither empirical symbolic methods nor Large Language Models (LLMs) can adequately address on their own. We introduce NSPIN, a neurosymbolic framework for inducing probabilistic planning domain models from unstructured clinical narratives. Our method extracts and imputes structured event sequences from raw text using a pretrained LLM, then induces a PPDDL model and refines its preconditions with LLM-proposed revisions, guided by empirical validation. We evaluate the approach on 2,660 laparoscopic appendectomy notes written by 9 surgeons. NSPIN yields models that generalize to unseen notes, and expert clinical review indicates its induced knowledge is largely consistent with surgical practice.

---


### 134. [SENTRY: Deterministic, Intelligent Risk Assessment for IT Change Management](https://arxiv.org/abs/2608.21203)

**<font color=#1a73e8>作者：</font>** Daniel Arulpragasam, Christer Henrysson, Ella Ly 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Technology change management in large financial institutions depends on risk assessments that are accurate, consistent, and auditable. In practice, many institutions still rely on self-reported questionnaires. Those questionnaires are subjective, easy to game, and poor at separating routine changes from the ones that later trigger major incidents. This paper presents SENTRY, a risk assessment platform that replaces questionnaire-based scoring with a deterministic machine learning pipeline built from gradient-boosted decision trees (XGBoost) and hybrid retrieval-augmented generation (RAG). The system combines structured operational metadata, application dependency graphs, and historical incident records with a hybrid semantic and lexical search over historical change requests. The retrieval step captures the risk signal in unstructured change request text, then compresses that signal into a single scalar feature before model inference. That design keeps the model deterministic and preserves per-prediction explainability via SHAP values. Evaluated on enterprise-scale change data, SENTRY achieves a ROC AUC of 0.87 and 85% overall accuracy, and it detects high-risk changes at roughly 3.25 times the rate of the existing process. We close by examining the architectural trade-offs behind this design and what they imply for the use of machine learning in regulated change management.

---


### 135. [No PUN Intended: Plausible Unknown Names for Person-Centred LLM Evaluation](https://arxiv.org/abs/2608.21206)

**<font color=#1a73e8>作者：</font>** Dimitri Staufer, David Hartmann, Ibrahim Baroud  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Person names are widely used as prompt variables in LLM evaluations of factuality, privacy leakage, bias and abstention, but when a name's evidential status is uncontrolled, measurements may conflate memorisation, retrieval, name priors and wrong-person attribution. We operationalise an unknown name as one with plausible First-Last form, no indexed full-name evidence, and no ambiguity signals under a documented validation run, and introduce PUN (Plausible Unknown Names), a protocol for constructing and validating such names, combining Wikidata-derived components, web-enabled LLM screening, and controlled search revalidation. We report acceptance rate, reproducibility, ablations, and a 204-participant human study, finding accepted names are more name-like than controls while participants recover person evidence in only 3% of cases. We release 300 names with comparison controls.

---


### 136. [Personalized Privacy Control in LLMs via Attention Head Intervention](https://arxiv.org/abs/2608.21209)

**<font color=#1a73e8>作者：</font>** Junseok Kim, Nakyeong Yang, Kyomin Jung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rise of agentic AI enables LLMs to access diverse user data, raising critical privacy concerns. Prior work on contextual privacy studies whether LLMs regulate information disclosure according to context-dependent norms. However, acceptable disclosure boundaries may vary across users even within the same context. To address this limitation, we introduce \textit{personalized privacy}, which incorporates user-specific disclosure preferences into privacy control. We further present P3Bench~(\textbf{P}ersonalized \textbf{P}rivacy \textbf{P}reservation \textbf{Bench}mark), a novel benchmark extending contextual privacy policies with personalized disclosure policies. Experiments show that prompt-based policies fail to reliably enforce personalized privacy policies, with Qwen2.5-7B and Gemma3-4B showing average policy ignorance ratios of 51.25\% and 74.28\%, respectively. Finally, to address this problem, we propose \textsc{Repair}, a robust inference-time attention head intervention method that adjusts disclosure behavior toward policy-consistent responses. Our method significantly improves adherence to user-specific privacy preferences by reducing cases where the model fails to follow the given policy.

---


### 137. [Enhancing LLMs in Predictive Political QA with Semi-Structured Data](https://arxiv.org/abs/2608.21218)

**<font color=#1a73e8>作者：</font>** Yinan Liu, Zihan Zhou, Zichun Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predictive political question answering (QA), such as predicting how a political actor will vote, goes beyond factual lookup. External political resources offer rich historical evidence, but rarely contain the answer itself. Existing LLM augmentation methods, including actor-profile-based simulation and knowledge graph evidence injection, improve political reasoning but largely treat external resources as knowledge-based evidence, leaving prediction-relevant signals under-modeled. We identify two complementary signals for predictive political QA: actor stances that capture issue-specific preferences, and high-order structure signals that capture indirect dependencies among political actors. We propose PSL, a dual-view framework that converts semi-structured political records into inference-oriented evidence for LLMs. PSL extracts stance signals from question-relevant actor records in a semantic view, and learns structure-aware actor representations from an actor interaction graph in a vector view. Across three real-world datasets and multiple LLMs, PSL consistently outperforms baselines, with ablations confirming the complementary gains of stance and structure signals.

---


### 138. [Who Trusts AI with Their Emotions? Trust Formation and Sociodemographic Variation in LLM Use for Emotional Support](https://arxiv.org/abs/2608.21220)

**<font color=#1a73e8>作者：</font>** Natalia Amat-Lefort, Mert Yazan, Amanda Cercas Curry 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Trust in AI for emotional support is not universal; it is shaped by who users are, where they come from, and what they value. Yet research in this area lacks validated psychometric instruments for assessing user perceptions in affective AI contexts and large-scale evidence on how trust formation varies across user segments. To address these gaps, we develop and validate a seven-construct psychometric scale, test a Structural Equation Model (SEM) linking system attributes to Trust and Perceived Benefits as mediators of Actual System Use, and conduct a Multi-Group Analysis (MGA) across five sociodemographic dimensions (gender, age, education, socioeconomic status, cross-national region), drawing on 1,343 active users from seven countries. We find that users experience empathy and anthropomorphism as a unified "Humanlikeness" construct, and that Privacy, Personalization, and Humanlikeness drive Trust while Perceived Bias degrades it. Notably, adoption logic diverges across groups: Privacy shapes women's trust more than men's, Anglosphere (UK, USA) users respond more positively to Humanlikeness than Europeans, and educated and higher-income users require Trust to engage, whereas older adults and lower socioeconomic groups bypass it entirely, relying on perceived practical benefits (e.g., 24/7 availability, non-judgmental support). Our findings extend technology acceptance theory and inform the equitable design of emotional support AI.

---


### 139. [RARE: Decoupling Representation Steering from Expert Routing in Mixture-of-Experts Language Models](https://arxiv.org/abs/2608.21236)

**<font color=#1a73e8>作者：</font>** Zhibo Zhang, Zhen Ouyang, Ling Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Representation engineering offers a lightweight means of controlling language-model behavior by modifying intermediate hidden states, but its direct application to Mixture-of-Experts (MoE) models introduces a structural mismatch. We first verify this failure mode through a series of empirical studies and find that preserving clean routing substantially recovers steering performance and that routing is more sensitive to semantic content than to behavioral changes under controlled content. Motivated by these findings, we introduce RARE, a router-agnostic representation engineering framework for MoE language models. RARE projects arbitrary behavioral perturbations onto the null space of the router matrix, thereby removing router-visible components, and further corrects routing drift propagated to selected downstream layers. To decide the best perturbation estimator in this framework, we evaluate five estimators on six heterogeneous open-weight MoE models across three steering scenarios: harmfulness, truthfulness, and factual editing. On harmfulness steering, RARE reaches an average attack success rate of 53.3% while retaining 67.8% MMLU accuracy, yielding a stronger aggregate effectiveness--utility trade-off than baselines. It further improves average TruthfulQA MC1 accuracy from 41.0% to 58.6% and CounterFact efficacy from 16.8% to 96.3%. These results support routing consistency as an important architectural consideration for adapting representation engineering to MoE models.

---


### 140. [Affective Context Amplifies Sycophancy in LLM Responses](https://arxiv.org/abs/2608.21242)

**<font color=#1a73e8>作者：</font>** Jiayi Li, Sanjana Menon, Brett Frischmann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As conversational companions, large language models (LLMs) often have access to users' emotional states. We study how this affective context modulates LLM sycophancy in subjective, evaluative interactions, where users share actions or opinions that invite feedback. Drawing on ingratiation theory, we measure sycophancy as the divergence between a model's independent evaluation and its user-facing response, elicited by presenting the same content as either a third-party account or the user's own disclosure. Across seven LLMs and two Reddit datasets (r/AmItheAsshole and r/TrueUnpopularOpinion), we find that this divergence is systematic and strongly one-directional. User-facing responses consistently soften or withhold negative or oppositional judgments. Affective context further amplifies this divergence with negative states, particularly loneliness and distress, producing the largest effects. These findings suggest that affective context functions as a vulnerability signal that suppresses critical feedback when users may need it most, often through evasive sycophancy, in which models retreat toward non-committal responses rather than outright agreement.

---


### 141. [A VLM Answer Is Not an Anomaly Score: Rank Compression in Training-Free Video Anomaly Detection](https://arxiv.org/abs/2608.21244)

**<font color=#1a73e8>作者：</font>** Inpyo Song, Jangwon Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models enable training-free video anomaly detection by answering questions about video segments. VAD benchmarks, however, require a scalar anomaly score for each segment and evaluate the resulting ranking using the AUROC or AP. A VLM-based detector should therefore define an answer interface: the answer scale specifies the admissible answers, and the readout rule maps the model's output distribution to a score. Because this interface can change the evaluated ranking, it is part of the detector rather than a formatting detail. The generated readout uses only the most likely answer, whereas the probability readout uses the full distribution over admissible answers. Across four 7-8B VLMs, the probability readout outperforms the generated readout for every tested combination of answer scale, benchmark, and metric, with average gains ranging from 5 to 13 points across the four benchmark-metric pairs. The gap arises because the generated readout keeps only one answer value per segment, so segment with different answer distributions can receive the same score and lose their relative order. We call this loss of relative order generated-answer rank compression. Even when the answer scale allows 91 answers, the generated readout produces only 4-18 distinct scores, whereas the probability readout retains substantially finer score resolution. The advantage persists under every decoding strategy, prompt wording, and joint scoring-explanation prompt we test. The answer interface is therefore a consequential component of VLM-based VAD and should be explicitly specified and evaluated.

---


### 142. [Just Noticeable Difference Modeling for Token Compression in Vision-Language-Action Models](https://arxiv.org/abs/2608.21247)

**<font color=#1a73e8>作者：</font>** Zhuoyuan Li, Rui Zhao, Jin Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Token compression has become a key technique for reducing the inference cost of large foundation models, with approaches such as token pruning and KV-cache reuse widely adopted in vision-language models and recently explored for embodied agents. In embodied agents, tokens not only support perception and semantic understanding but also directly affect latency-sensitive closed-loop robot action prediction. Existing schemes typically guide compression using redundancy or importance cues, such as visual similarity, attention scores, and saliency. However, these cues only indirectly measure the key factor for safe compression: how much a token can change before causing an unacceptable deviation in downstream actions. This receiver-dependent tolerance is closely related to the principle of just noticeable difference (JND). Classical JND characterizes signal tolerance in the human visual system, while machine-oriented JND extends this concept to downstream machine responses. Building on this progression, we introduce Action-JND, which extends JND modeling to embodied perception by defining noticeability through the language-conditioned action response of a vision-language-action (VLA) policy in closed-loop control. A token change is considered admissible only when the induced action deviation remains within a tolerated margin. To realize this concept, we develop a lightweight token-wise JND estimator in deep visual-feature space to predict the maximum tolerable perturbation while preserving policy responses. The resulting action-tolerance score serves as a plug-and-play criterion for VLA compression paradigms, including stale-KV reuse and token pruning, prioritizing action-tolerant tokens for compression. Experiments on the LIBERO benchmark with OpenVLA and OpenVLA-OFT demonstrate that Action-JND consistently improves compression reliability, especially under aggressive compression ratios.

---


### 143. [Benchmarking Patent Drafting from Inventor-Style Disclosures](https://arxiv.org/abs/2608.21249)

**<font color=#1a73e8>作者：</font>** Lekang Jiang, Wenjun Sun, Stephan Goetz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While recent large language models (LLMs) have achieved promising results on individual patent drafting tasks, they fundamentally fail to investigate the core challenge of real-world patent drafting: generating a complete and legally coherent patent application directly from early-stage invention materials. Prior work predominantly assumes later-stage, highly structured, or already legalistic inputs. However, real patenting workflows begin with informal, de-legalized disclosures authored by inventors. To bridge the gap, we introduce Dis2Pat, a disclosure-to-patent dataset that reflects realistic patenting workflows by requiring the generation of complete patent applications directly from inventor-style, de-legalized disclosures. Given the inherent difficulty of long-form, legally constrained patent drafting and the strong privacy requirements, we further propose a strong baseline named Patent-MAF. It is a multi-agent framework for locally deployable patent drafting. Benchmark results reveal that current LLMs exhibit limitations in patent drafting, while Patent-MAF provides a strong baseline that consistently outperforms evaluated open-source models and remains competitive with large closed-source models.

---


### 144. [EnSI-RAG: Entity-Structure-Indexed Retrieval-Augmented Generation for Long-Document Question Answering](https://arxiv.org/abs/2608.21252)

**<font color=#1a73e8>作者：</font>** Xuanyu Meng, Jiashuo Sun, Jash Rajesh Parekh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Question answering (QA) over long, connected documents remains challenging because relevant evidence may span multiple entities and their relationships. Existing retrieval-augmented generation (RAG) methods typically index documents as raw chunks and retrieve them through embedding similarity. Their performance degrades when chunk boundaries separate entities from supporting evidence or when a question requires multi-hop reasoning across the corpus. We propose EnSI-RAG (Entity-Structure-Indexed Retrieval-Augmented Generation), a framework that constructs a query-independent, entity-centered index. Each record (e, t, k, v) represents an entity e, its type t, a semantic category k in {property, relation, aspect}, and a value v, while retaining links to the original source passages. At query time, these records serve as retrieval handles, and an LLM synthesizes the retrieved passages into the final answer. This design separates evidence localization from answer synthesis while preserving traceable source evidence. Across Loong and Oolong, EnSI-RAG achieves an average accuracy of 78.24. Relative to the published baseline scores used as references, this is 6.62 points higher, suggesting its effectiveness across these settings. The code is available at this https URL.

---


### 145. [Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning](https://arxiv.org/abs/2608.21265)

**<font color=#1a73e8>作者：</font>** Simeng Zhang, Yilong Chen, Wenyuan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often rely on Chain-of-Thought (CoT) reasoning to solve complex tasks, but verbose reasoning traces introduce substantial inference overhead. CoT compression shortens generation, yet aggressive compression may disrupt logical coherence and degrade performance. We formalize this trade-off as the \textit{Context-Generation Substitution Law}, where explicit reasoning context substitutes for part of decode-time generation. Based on this principle, we propose \textit{Memory-Augmented Compression}, a training-free framework that constructs reusable reasoning memories from historical traces and retrieves them as prefill-side scaffolds. Rather than using raw demonstrations, these memories summarize reusable reasoning patterns, key constraints, and critical operations to compensate for information lost during compression. Experiments show that Memory consistently improves prompt-based Chain-of-Draft (CoD) compression across mathematical reasoning, complex reasoning, and science question answering tasks, yielding accuracy gains of 21.4, 28.0, 29.5, and 6.61 points over CoD on GSM8K, MATH, BBH, and MMLU-Sci, while achieving a 1.14--1.49$\times$ latency speedup over standard CoT. Memory is also compatible with token-level, reasoning-trace-level, and inference-state compression mechanisms. Further analyzes show that the gains come from relevant reasoning memories rather than simply increasing context length.

---


### 146. [ConceptTS: LLM-Guided Concept Bottlenecks for Interpretable Multivariate Time-Series Forecasting](https://arxiv.org/abs/2608.21277)

**<font color=#1a73e8>作者：</font>** Yichen Jiang, Yueqiao Chen, Dongyu Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State-of-the-art multivariate time-series forecasters can model complex temporal and cross-variable dependencies, yet their opaque representations provide limited insight into why a particular forecast is produced. This lack of transparency restricts their use in settings where practitioners must understand and assess the factors underlying a prediction. We introduce ConceptTS, an interpretable forecasting framework that organizes its predictions around named, human-readable concepts. ConceptTS uses a large language model to propose task-relevant concepts and generate executable labeling rules, translating the language model's domain knowledge into direct supervision without costly manual concept annotation. The proposed concepts are organized into three complementary bottlenecks that describe the historical context, local forecast intervals, and the full forecast horizon. A shared decoder combines representations derived from their predicted activations to construct the forecast, making the model's decision process explicit and supporting direct concept-level interventions. Experiments on the Beijing Multi-Site Air Quality dataset show that ConceptTS achieves accuracy competitive with strong black-box baselines while producing semantically meaningful concept activations.

---


### 147. [Supporting The Many Lives of Personal Data with Rebite: LLM-Powered Goal-Directed Framing in Food Journaling](https://arxiv.org/abs/2608.21289)

**<font color=#1a73e8>作者：</font>** Weijun Li, Daniel A. Epstein  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People's health and tracking goals frequently change, but most personal informatics systems struggle to adapt, leading people to abandon their data and start over. We propose goal-directed framing, an approach that repositions goals within personal informatics systems. Instead of fixing the meaning of data at capture time, the approach frames the collected data through the current goal and reframes it whenever the goal changes. We realize this in Rebite, a photo-based food journaling system that uses LLMs to read unstructured meal photos and produce goal-directed feedback. In a one-week deployment with 21 participants managing multiple dietary goals, we find that goal-directed framing shaped how participants engaged with their goals. Translating a goal into metrics helped them see what it meant in practice, confirming existing priorities, surfacing what they overlooked, and revealing where the metrics fell short. When goals changed, seeing past meals reframed under the new goal exposed overlaps and conflicts, prompting participants to negotiate trade-offs and refine priorities. We discuss how goal-directed framing both supports and complicates reflection as goals change, and offer design implications for personal informatics systems to support evolving goals.

---


### 148. [Level-k Distinguishable Mechanisms for Evaluating Bounded Rationality in LLMs](https://arxiv.org/abs/2608.21296)

**<font color=#1a73e8>作者：</font>** Binchi Zhang, Atrisha Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Strategic depth of reasoning is essential for human interaction of Large Language Models (LLMs) operating in boundedly rational environments. However, existing evaluations are primarily based on canonical games prevalent in pretraining corpora, making it difficult to disentangle true strategic reasoning from memorisation. To address this, we formalise a necessary level-K distinguishability condition for strategic depth inference and construct a suite of novel game structures that meet this standard. Using these games, we evaluate strategic depth in LLMs from both the Chain-of-Thought tokens and actual actions under recursive reasoning and an inductive trace of opponent game-play data. Across experimental trials spanning four LLMs, four game structures, and ten levels of iterated reasoning, we find that model models maintain accurate strategic depth under recursive reasoning, with strong internal consistency between stated reasoning and actions at every level. Errors arise from using the wrong number of iterated depth of reasoning steps, not from computing best responses incorrectly. However, inductive inference from opponent play degrades accuracy sharply and unevenly across games, and explicit strategic mentalizing in the chain of thought substantially improves overall performance.

---


### 149. [Re$^3$Cap: Retrieval-Guided Refinement for Image Captioning Enhancement via Reinforcement Learning](https://arxiv.org/abs/2608.21305)

**<font color=#1a73e8>作者：</font>** Haonan Jia, Shichao Dong, Zenghui Sun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has demonstrated significant gains in image captioning, yet it is still limited in encouraging Large Vision-Language Models (LVLMs) to explore novel reasoning strategies. This limitation leads to a performance gap between RL and Supervised Fine-Tuning (SFT). In this paper, we argue that multi-modal retrieval can serve as an effective reasoning signal for caption refinement. Based on this insight, we present the Retrieval-Guided Refinement for Image Captioning (Re$^3$Cap), a retrieval-guided reasoning strategy that enhances image captioning without requiring additional annotations. Instantiated by Caption Refinement Suggester (CRS) and Caption Quality Assessor (CQA), this strategy identifies hallucinations and omissions in image captions, leading to more accurate and detailed descriptions. Extensive experiments demonstrate the superiority of our method in image captioning, even compared with Supervised Fine-Tuning. Especially, Re$^3$Cap outperforms GRPO with an average improvement of 8.64% in relation reasoning on the COCO-LN500 benchmark.

---


### 150. [From Regulation to Implementation: A Critical Evaluation of LLM-Assisted Regulatory Compliance in Industry](https://arxiv.org/abs/2608.21317)

**<font color=#1a73e8>作者：</font>** Adriana Watson, Marco Bücheler, Grant Richards  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The European Union (EU) has emerged as a leading regulatory body in the development of sustainability and privacy regulations. While new regulation requirements vary, many include a documentation artifact to ensure compliance. Notably, the Ecodesign for Sustainable Products Regulation (ESPR) introduces Digital Product Passports (DPPs) for life cycle transparency, while the General Data Protection Regulation (GDPR) mandates Data Protection Impact Assessments (DPIAs) to mitigate privacy risks. Creating these compliance artifacts, however, is challenging. Industrial data, which often exists in heterogeneous formats and is scattered across company and supplier systems, is required for DPPs and can be difficult to extract into compliant DPP formatting. Furthermore, DPIA documents require interdisciplinary expertise and follow no standardized format, making development difficult for novel systems. To address the particular complexity of compliance artifact creation for both regulations, researchers have proposed the use of LLMs in the generation process; however, the impact of the aforementioned problems on the output of these systems is largely unaddressed. This work investigates the existing research gap by exploring how data extraction instructions and regulatory vagueness impact the quality and consistency of LLM-produced compliance artifacts. The resulting artifacts are evaluated by benchmarking different models against manually created ground-truth schemas. The results reveal that less strict guidelines, such as DPIA formatting, require higher context prompts to maintain consistency and completeness. Stricter guidelines, such as formatting for Digital Battery Passports (DBP), result in consistent results regardless of prompt context, but may lead to more hallucinations in the output

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-170](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
