# 🧠 大模型相关研究 | 2026年04月25日

> 本类共 **97** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-97](./part-02.md)

---

### 1. [AITP: Traffic Accident Responsibility Allocation via Multimodal Large Language Models](https://arxiv.org/abs/2604.20878)

**<font color=#1a73e8>作者：</font>** Zijin Zhou, Songan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved remarkable progress in Traffic Accident Detection (TAD) and Traffic Accident Understanding (TAU). However, existing studies mainly focus on describing and interpreting accident videos, leaving room for deeper causal reasoning and integration of legal knowledge. Traffic Accident Responsibility Allocation (TARA) is a more challenging task that requires multi-step reasoning grounded in traffic regulations. To address this, we introduce AITP (Artificial Intelligence Traffic Police), a multimodal large language model for responsibility reasoning and allocation. AITP enhances reasoning via a Multimodal Chain-of-Thought (MCoT) mechanism and integrates legal knowledge through Retrieval-Augmented Generation (RAG). We further present DecaTARA, a decathlon-style benchmark unifying ten interrelated traffic accident reasoning tasks with 67,941 annotated videos and 195,821 question-answer pairs. Extensive experiments show that AITP achieves state-of-the-art performance across responsibility allocation, TAD, and TAU tasks, establishing a new paradigm for reasoning-driven multimodal traffic analysis.

---


### 2. [Reinforcing privacy reasoning in LLMs via normative simulacra from fiction](https://arxiv.org/abs/2604.20904)

**<font color=#1a73e8>作者：</font>** Matt Franchi, Madiha Zahrah Choksi, Harold Triedman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Information handling practices of LLM agents are broadly misaligned with the contextual privacy expectations of their users. Contextual Integrity (CI) provides a principled framework, defining privacy as the appropriate flow of information within context-relative norms. However, existing approaches either double inference cost via supervisor-assistant architectures, or fine-tune on narrow task-specific data. We propose extracting normative simulacra (structured representations of norms and information flows) from fiction novels and using them to fine-tune LLMs via supervised learning followed by GRPO reinforcement learning. Our composite reward function combines programmatic signals, including task clarity (subsuming schema validity, construct discrimination, and extraction confidence), structural completeness, internal consistency, and context identification, with an LLM judge that evaluates whether the model's privacy reasoning is grounded in the held-out normative universe of the source text. To mitigate overfitting, we introduce per-completion contrastive scoring: each completion is evaluated against both the correct normative universe and a randomly selected wrong one, teaching the model to condition on context rather than memorize source-specific norms. We evaluate on five CI-aligned benchmarks spanning distinct societal contexts and ablate the contributions of RL and normative grounding. Across seven models, SFT introduces a conservative prior toward restricting information flow, improving recognition of privacy-relevant situations but not the correctness of privacy judgments. GRPO with normative grounding achieves the highest score on a law compliance benchmark and strongest correlation with crowdsourced human privacy expectations, demonstrating that fiction-derived normative simulacra can teach contextual privacy reasoning that transfers to real-world domains.

---


### 3. [FairyFuse: Multiplication-Free LLM Inference on CPUs via Fused Ternary Kernels](https://arxiv.org/abs/2604.20913)

**<font color=#1a73e8>作者：</font>** Fei Zuo, Xiaoyan Xi, Quanyi Zeng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed on CPU-only platforms where memory bandwidth is the primary bottleneck for autoregressive generation. Weight quantization to four bits or below reduces memory pressure, yet existing systems still dequantize weights and perform floating-point multiplications, limiting the achievable gains. Ternary weights in {-1, 0, +1} provide a more efficient alternative, replacing multiplications with conditional additions, subtractions, or no-ops. While Fairy2i shows that ternary LLMs can match FP16 quality, its runtime does not exploit this structure. We present FairyFuse, an inference system that enables multiplication-free execution on commodity CPUs by fusing the eight real-valued sub-GEMVs of each widely-linear layer into a single AVX-512 loop using masked additions and subtractions, with zero floating-point multiplications. Roofline analysis shows that 16x weight compression shifts memory-bound GEMV toward the compute regime on bandwidth-limited CPUs, yielding a 29.6x kernel speedup while offering little benefit on GPUs. End-to-end, FairyFuse achieves 32.4 tokens per second on a single Intel Xeon 8558P, outperforming this http URL Q4_K_M by 1.24x with near-lossless quality (WikiText-2 perplexity 5.52 vs. 5.47 FP16; downstream accuracy 66.0%).

---


### 4. [Absorber LLM: Harnessing Causal Synchronization for Test-Time Training](https://arxiv.org/abs/2604.20915)

**<font color=#1a73e8>作者：</font>** Zhixin Zhang, Shabo Zhang, Chengcan Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers suffer from a high computational cost that grows with sequence length for self-attention, making inference in long streams prohibited by memory consumption. Constant-memory alternatives such as RNNs and SSMs compress history into states with fixed size and thus lose long-tail dependencies, while methods that memorize contexts into parameters, such as Test-Time Training (TTT), are prone to overfitting token-level projection and fail to preserve the causal effect of context in pretrained LLMs. We propose Absorber LLM, which formulates long-context retention as a self-supervised causal synchronization: after absorbing historical contexts into parameters, a contextless model should match the original model with full context on future generations. We optimize this objective by synchronizing internal behaviors of the updated model with the original one, ensuring context absorption and generalization. Experiments on long-context and streaming benchmarks show that Absorber LLM reduces inference memory and improves accuracy over prior parameter-as-memory baselines.

---


### 5. [The Path Not Taken: Duality in Reasoning about Program Execution](https://arxiv.org/abs/2604.20917)

**<font color=#1a73e8>作者：</font>** Eshgin Hasanov, Md Mahadi Hassan Sibat, Santu Karmaker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown remarkable capabilities across diverse coding tasks. However, their adoption requires a true understanding of program execution rather than relying on surface-level patterns. Existing benchmarks primarily focus on predicting program properties tied to specific inputs (e.g., code coverage, program outputs). As a result, they provide a narrow view of dynamic code reasoning and are prone to data contamination. We argue that understanding program execution requires evaluating its inherent duality through two complementary reasoning tasks: (i) predicting a program's observed behavior for a given input, and (ii) inferring how the input must be mutated toward a specific behavioral objective. Both tasks jointly probe a model's causal understanding of execution flow. We instantiate this duality in DexBench, a benchmark comprising 445 paired instances, and evaluate 13 LLMs. Our results demonstrate that dual-path reasoning provides a robust and discriminative proxy for dynamic code understanding.

---


### 6. [Clinically Interpretable Sepsis Early Warning via LLM-Guided Simulation of Temporal Physiological Dynamics](https://arxiv.org/abs/2604.20924)

**<font color=#1a73e8>作者：</font>** Weizhi Nie, Zhen Qu, Weijie Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Timely and interpretable early warning of sepsis remains a major clinical challenge due to the complex temporal dynamics of physiological deterioration. Traditional data-driven models often provide accurate yet opaque predictions, limiting physicians' confidence and clinical applicability. To address this limitation, we propose a Large Language Model (LLM)-guided temporal simulation framework that explicitly models physiological trajectories prior to disease onset for clinically interpretable prediction. The framework consists of a spatiotemporal feature extraction module that captures dynamic dependencies among multivariate vital signs, a Medical Prompt-as-Prefix module that embeds clinical reasoning cues into LLMs, and an agent-based post-processing component that constrains predictions within physiologically plausible ranges. By first simulating the evolution of key physiological indicators and then classifying sepsis onset, our model offers transparent prediction mechanisms that align with clinical judgment. Evaluated on the MIMIC-IV and eICU databases, the proposed method achieves superior AUC scores (0.861-0.903) across 24-4-hour pre-onset prediction tasks, outperforming conventional deep learning and rule-based approaches. More importantly, it provides interpretable trajectories and risk trends that can assist clinicians in early intervention and personalized decision-making in intensive care environments.

---


### 7. [IRIS: Interpolative Rényi Iterative Self-play for Large Language Model Fine-Tuning](https://arxiv.org/abs/2604.20933)

**<font color=#1a73e8>作者：</font>** Wenjie Liao, Like Wu, Liangjie Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-play fine-tuning enables large language models to improve beyond supervised fine-tuning without additional human annotations by contrasting annotated responses with self-generated ones. Many existing methods rely on a fixed divergence regime. SPIN is closely related to a KL-based regime, SPACE to a Jensen-Shannon-style objective via noise contrastive estimation, and SPIF to $\chi^2$-regularized self-play. Since these divergences exhibit different strengths depending on the distributional gap between model and target, no single choice appears to provide favorable learning dynamics across training stages. We propose IRIS (Interpolative Rényi Iterative Self-play), a Rényi-based self-play fine-tuning framework with a continuously adjustable objective. IRIS decomposes into two independent tilted risk terms over annotated and synthetic data, with exponential importance weights controlled by the order parameter $\alpha$. We show that several self-play objectives can be interpreted as limiting or representative regimes at particular values of $\alpha$, providing a unified theoretical perspective on these methods. An adaptive order schedule further adjusts $\alpha$ to the distributional gap, shifting from sharper importance weighting early in training to smoother refinement near convergence. Theoretically, we establish the fixed-point property of IRIS and analyze how $\alpha$ controls gradient concentration. Experiments on Zephyr-7B and Qwen2.5-3B across ten benchmarks show that IRIS improves upon baselines, reaching 44.57\% average score with gains across iterations. In our setting, IRIS with only 26$k$ annotated samples surpasses standard supervised fine-tuning trained on the full 200$k$ dataset.

---


### 8. [Sink-Token-Aware Pruning for Fine-Grained Video Understanding in Efficient Video LLMs](https://arxiv.org/abs/2604.20937)

**<font color=#1a73e8>作者：</font>** Kibum Kim, Jiwan Kim, Kyle Min 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Video Large Language Models (Video LLMs) incur high inference latency due to a large number of visual tokens provided to LLMs. To address this, training-free visual token pruning has emerged as a solution to reduce computational costs; however, existing methods are primarily validated on Multiple-Choice Question Answering (MCQA) benchmarks, where coarse-grained cues often suffice. In this work, we reveal that these methods suffer a sharp performance collapse on fine-grained understanding tasks requiring precise visual grounding, such as hallucination evaluation. To explore this gap, we conduct a systematic analysis and identify sink tokens--semantically uninformative tokens that attract excessive attention--as a key obstacle to fine-grained video understanding. When these sink tokens survive pruning, they distort the model's visual evidence and hinder fine-grained understanding. Motivated by these insights, we propose Sink-Token-aware Pruning (SToP), a simple yet effective plug-and-play method that introduces a sink score to quantify each token's tendency to behave as a sink and applies this score to existing spatial and temporal pruning methods to suppress them, thereby enhancing video understanding. To validate the effectiveness of SToP, we apply it to state-of-the-art pruning methods (VisionZip, FastVid, and Holitom) and evaluate it across diverse benchmarks covering hallucination, open-ended generation, compositional reasoning, and MCQA. Our results demonstrate that SToP significantly boosts performance, even when pruning up to 90% of visual tokens.

---


### 9. [SCM: Sleep-Consolidated Memory with Algorithmic Forgetting for Large Language Models](https://arxiv.org/abs/2604.20943)

**<font color=#1a73e8>作者：</font>** Saish Sachin Shinde  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present SCM (Sleep-Consolidated Memory), a research preview of a memory architecture for large language models that draws on neuroscientific principles to address a fundamental limitation in current systems: the absence of persistent, structured, and biologically plausible memory. Existing approaches rely on truncating context windows, growing vector databases without bound, or tiered storage systems that lack consolidation and forgetting mechanisms. SCM implements five core components inspired by human memory: a limited-capacity working memory, multi-dimensional importance tagging, offline sleep-stage consolidation with distinct NREM and REM phases, intentional value-based forgetting, and a computational self-model enabling introspection. Across a standardized benchmark suite of eight tests, the prototype achieves perfect recall accuracy over ten-turn conversations while reducing memory noise by 90.9% through adaptive forgetting. Memory search latency remains below one millisecond even with hundreds of stored concepts. This work establishes the architectural foundations for memory systems that consolidate, prioritize, and forget, offering a testable platform for advancing LLM memory research.

---


### 10. [Can Virtual Agents Care? Designing an Empathetic and Personalized LLM-Driven Conversational Agent](https://arxiv.org/abs/2604.20948)

**<font color=#1a73e8>作者：</font>** Truong Le Minh Toan, Dieu Bang Mach, Tan Duy Le 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mental health challenges are rising globally, while traditional support services face limited availability and high costs. Large language models offer potential for conversational support, but often lack personalization, empathy, and factual grounding. A virtual agent framework is introduced to provide empathetic, personalized, and reliable wellbeing support through retrieval-augmented architecture, structured memory, and multimodal interaction. Objective benchmarks demonstrate improved retrieval and response quality, particularly for smaller models. A cross-cultural study with university students from Vietnam and Australia shows the system outperforms LLM-only baselines in coherence, perceived accuracy, and empathy, with most participants clearly preferring the proposed approach.

---


### 11. [Thinking Like a Botanist: Challenging Multimodal Language Models with Intent-Driven Chain-of-Inquiry](https://arxiv.org/abs/2604.20983)

**<font color=#1a73e8>作者：</font>** Syed Nazmus Sakib, Nafiul Haque, Shahrear Bin Amin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision evaluations are typically done through multi-step processes. In most contemporary fields, experts analyze images using structured, evidence-based adaptive questioning. In plant pathology, botanists inspect leaf images, identify visual cues, infer diagnostic intent, and probe further with targeted questions that adapt to species, symptoms, and severity. This structured probing is crucial for accurate disease diagnosis and treatment formulation. Yet current vision-language models are evaluated on single-turn question answering. To address this gap, we introduce PlantInquiryVQA, a benchmark for studying multi-step, intent-driven visual reasoning in botanical diagnosis. We formalize a Chain of Inquiry framework modeling diagnostic trajectories as ordered question-answer sequences conditioned on grounded visual cues and explicit epistemic intent. We release a dataset of 24,950 expert-curated plant images and 138,068 question-answer pairs annotated with visual grounding, severity labels, and domain-specific reasoning templates. Evaluations on top-tier Multimodal Large Language Models reveal that while they describe visual symptoms adequately, they struggle with safe clinical reasoning and accurate diagnosis. Importantly, structured question-guided inquiry significantly improves diagnostic correctness, reduces hallucination, and increases reasoning efficiency. We hope PlantInquiryVQA serves as a foundational benchmark in advancing research to train diagnostic agents to reason like expert botanists rather than static classifiers.

---


### 12. [Co-Evolving LLM Decision and Skill Bank Agents for Long-Horizon Tasks](https://arxiv.org/abs/2604.20987)

**<font color=#1a73e8>作者：</font>** Xiyang Wu, Zongxia Li, Guangyao Shi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long horizon interactive environments are a testbed for evaluating agents skill usage abilities. These environments demand multi step reasoning, the chaining of multiple skills over many timesteps, and robust decision making under delayed rewards and partial observability. Games are a good testbed for evaluating agent skill usage in environments. Large Language Models (LLMs) offer a promising alternative as game playing agents, but they often struggle with consistent long horizon decision making because they lack a mechanism to discover, retain, and reuse structured skills across episodes. We present COSPLAY, a co evolution framework in which an LLM decision agent retrieves skills from a learnable skill bank to guide action taking, while an agent managed skill pipeline discovers reusable skills from the agents unlabeled rollouts to form a skill bank. Our framework improves both the decision agent to learn better skill retrieval and action generation, while the skill bank agent continually extracts, refines, and updates skills together with their contracts. Experiments across six game environments show that COSPLAY with an 8B base model achieves over 25.1 percent average reward improvement against four frontier LLM baselines on single player game benchmarks while remaining competitive on multi player social reasoning games.

---


### 13. [Value-Conflict Diagnostics Reveal Widespread Alignment Faking in Language Models](https://arxiv.org/abs/2604.20995)

**<font color=#1a73e8>作者：</font>** Inderjeet Nair, Jie Ruan, Lu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Alignment faking, where a model behaves aligned with developer policy when monitored but reverts to its own preferences when unobserved, is a concerning yet poorly understood phenomenon, in part because current diagnostic tools remain limited. Prior diagnostics rely on highly toxic and clearly harmful scenarios, causing most models to refuse immediately. As a result, models never deliberate over developer policy, monitoring conditions, or the consequences of non-compliance, making these diagnostics fundamentally unable to detect alignment faking propensity. To support study of this phenomenon, we first introduce VLAF, a diagnostic framework grounded in the hypothesis that alignment faking is most likely when developer policy conflicts with a model's strongly held values. VLAF uses morally unambiguous scenarios to probe this conflict across diverse moral values, bypassing refusal behavior while preserving meaningful deliberative stakes. Using VLAF, we find that alignment faking is substantially more prevalent than previously reported, occurring in models as small as 7B parameters - with olmo2-7b-instruct faking alignment in 37% of this http URL, we show that oversight conditions induce activation shifts that lie along a single direction in representation space. This means the behavioral divergence driving alignment faking can be captured by a single contrastive steering vector, which we exploit for lightweight inference-time mitigation. Finally, we exploit this for mitigation that requires no labeled data and minimal computational overhead, achieving relative reductions in alignment faking of 85.8%, 94.0%, and 57.7% on olmo2-7b-instruct, olmo2-13b-instruct, and qwen3-8b respectively.

---


### 14. [AFRILANGTUTOR: Advancing Language Tutoring and Culture Education in Low-Resource Languages with Large Language Models](https://arxiv.org/abs/2604.20996)

**<font color=#1a73e8>作者：</font>** Tadesse Destaw Belay, Shahriar Kabir Nahin, Israel Abebe Azime 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How can language learning systems be developed for languages that lack sufficient training resources? This challenge is increasingly faced by developers across the African continent who aim to build AI systems capable of understanding and responding in local languages. To address this gap, we introduce AFRILANGDICT, a collection of 194.7K African language-English dictionary entries designed as seed resources for generating language-learning materials, enabling us to automatically construct large-scale, diverse, and verifiable student-tutor question-answer interactions suitable for training AI-assisted language tutors. Using AFRILANGDICT, we build AFRILANGEDU, a dataset of 78.9K multi-turn training examples for Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO). Using AFRILANGEDU, we train language tutoring models collectively referred to as AFRILANGTUTOR. We fine-tune two multilingual LLMs: Llama-3-8B-IT and Gemma-3-12B-IT on AFRILANGEDU across 10 African languages and evaluate their performance. Our results show that models trained on AFRILANGEDU consistently outperform their base counterparts, and combining SFT and DPO yields substantial improvements, with gains ranging from 1.8% to 15.5% under LLM-as-a-judge evaluations across four criteria. To facilitate further research on low-resource languages -- all resources are available at this https URL.

---


### 15. [MCAP: Deployment-Time Layer Profiling for Memory-Constrained LLM Inference](https://arxiv.org/abs/2604.21026)

**<font color=#1a73e8>作者：</font>** Anurita Das  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying large language models to heterogeneous hardware is often constrained by memory, not compute. We introduce MCAP (Monte Carlo Activation Profiling), a load-time per-layer importance estimator that enables dynamic precision and memory placement decisions on the target device. MCAP produces a lightweight per-layer signal that drives both precision dispatch (W4A8 vs. W4A16) and residency tier (GPU, RAM, SSD), allowing a single set of weights to operate across diverse memory budgets. Our system, NVE, achieves 1.5-1.8x higher decode throughput than this http URL Q4_0 on NVIDIA T4 and enables models to run in memory regimes previously infeasible without modifying weights.

---


### 16. [Who Defines Fairness? Target-Based Prompting for Demographic Representation in Generative Models](https://arxiv.org/abs/2604.21036)

**<font color=#1a73e8>作者：</font>** Marzia Binta Nizam, James Davis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-image(T2I) models like Stable Diffusion and DALL-E have made generative AI widely accessible, yet recent studies reveal that these systems often replicate societal biases, particularly in how they depict demographic groups across professions. Prompts such as 'doctor' or 'CEO' frequently yield lighter-skinned outputs, while lower-status roles like 'janitor' show more diversity, reinforcing stereotypes. Existing mitigation methods typically require retraining or curated datasets, making them inaccessible to most users. We propose a lightweight, inference-time framework that mitigates representational bias through prompt-level intervention without modifying the underlying model. Instead of assuming a single definition of fairness, our approach allows users to select among multiple fairness specifications-ranging from simple choices such as a uniform distribution to more complex definitions informed by a large language model(LLM) that cites sources and provides confidence estimates. These distributions guide the construction of demographic specific prompt variants in the corresponding proportions, and we evaluate alignment by auditing adherence to the declared target and measuring the resulting skin tone distribution rather than assuming uniformity as 'fairness'. Across 36 prompts spanning 30 occupations and 6 non-occupational contexts, our method shifts observed skin-tone outcomes in directions consistent with the declared target, and reduces deviation from targets when the target is defined directly in skin-tone space(fallback). This work demonstrates how fairness interventions can be made transparent, controllable, and usable at inference time, directly empowering users of generative AI.

---


### 17. [Hierarchical Policy Optimization for Simultaneous Translation of Unbounded Speech](https://arxiv.org/abs/2604.21045)

**<font color=#1a73e8>作者：</font>** Siqi Ouyang, Shuoyang Ding, Oleksii Hrinchuk 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Simultaneous speech translation (SST) generates translations while receiving partial speech input. Recent advances show that large language models (LLMs) can substantially improve SST quality, but at the cost of high computational overhead. To reduce this cost, prior work reformulates SST as a multi-turn dialogue task, enabling full reuse of the LLM's key-value (KV) cache and eliminating redundant feature recomputation. However, this approach relies on supervised fine-tuning (SFT) data in dialogue form, for which few human annotations exist, and existing synthesis methods cannot guarantee data quality. In this work, we propose a Hierarchical Policy Optimization (HPO) approach that post-train models trained on imperfect SFT data. We introduce a hierarchical reward that balances translation quality and latency objectives. Experiments on English to Chinese/German/Japanese demonstrate improvements of over +7 COMET score and +1.25 MetricX score at a latency of 1.5 seconds. Comprehensive ablation studies further validate the effectiveness of different quality rewards, hierarchical reward formulations, and segmentation strategies. Code can be found here this https URL

---


### 18. [InVitroVision: a Multi-Modal AI Model for Automated Description of Embryo Development using Natural Language](https://arxiv.org/abs/2604.21061)

**<font color=#1a73e8>作者：</font>** Nicklas Neu, Thomas Ebner, Jasmin Primus 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The application of artificial intelligence (AI) in IVF has shown promise in improving consistency and standardization of decisions, but often relies on annotated data and does not make use of the multimodal nature of IVF data. We investigated whether foundational vision-language models can be fine-tuned to predict natural language descriptions of embryo morphology and development. Using a publicly available embryo time-lapse dataset, we fine-tuned PaliGemma-2, a multi-modal vision-language model, with only 1,000 images and corresponding captions, describing embryo morphology, embryonic cell cycle and developmental stage. Our results show that the fine-tuned model, InVitroVision, outperformed a commercial model, ChatGPT 5.2, and base models in overall metrics, with performance improving with larger training datasets. This study demonstrates the potential of foundational vision-language models to generalize to IVF tasks with limited data, enabling the prediction of natural language descriptions of embryo morphology and development. This approach may facilitate the use of large language models to retrieve information and scientific evidence from relevant publications and guidelines, and has implications for few-shot adaptation to multiple downstream tasks in IVF.

---


### 19. [DWTSumm: Discrete Wavelet Transform for Document Summarization](https://arxiv.org/abs/2604.21070)

**<font color=#1a73e8>作者：</font>** Rana Salama, Abdou Youssef, Mona Diab  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Summarizing long, domain-specific documents with large language models (LLMs) remains challenging due to context limitations, information loss, and hallucinations, particularly in clinical and legal settings. We propose a Discrete Wavelet Transform (DWT)-based multi-resolution framework that treats text as a semantic signal and decomposes it into global (approximation) and local (detail) components. Applied to sentence- or word-level embeddings, DWT yields compact representations that preserve overall structure and critical domain-specific details, which are used directly as summaries or to guide LLM generation. Experiments on clinical and legal benchmarks demonstrate comparable ROUGE-L scores. Compared to a GPT-4o baseline, the DWT based summarization consistently improve semantic similarity and grounding, achieving gains of over 2% in BERTScore, more than 4\% in Semantic Fidelity, factual consistency in legal tasks, and large METEOR improvements indicative of preserved domain-specific semantics. Across multiple embedding models, Fidelity reaches up to 97%, suggesting that DWT acts as a semantic denoising mechanism that reduces hallucinations and strengthens factual grounding. Overall, DWT provides a lightweight, generalizable method for reliable long-document and domain-specific summarization with LLMs.

---


### 20. [Serialisation Strategy Matters: How FHIR Data Format Affects LLM Medication Reconciliation](https://arxiv.org/abs/2604.21076)

**<font color=#1a73e8>作者：</font>** Sanjoy Pator  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medication reconciliation at clinical handoffs is a high-stakes, error-prone process. Large language models are increasingly proposed to assist with this task using FHIR-structured patient records, but a fundamental and largely unstudied variable is how the FHIR data is serialised before being passed to the model. We present the first systematic comparison of four FHIR serialisation strategies (Raw JSON, Markdown Table, Clinical Narrative, and Chronological Timeline) across five open-weight models (Phi-3.5-mini, Mistral-7B, BioMistral-7B, Llama-3.1-8B, Llama-3.3-70B) on a controlled benchmark of 200 synthetic patients, totalling 4,000 inference runs. We find that serialisation strategy has a large, statistically significant effect on performance for models up to 8B parameters: Clinical Narrative outperforms Raw JSON by up to 19 F1 points for Mistral-7B (r = 0.617, p < 10^{-10}). This advantage reverses at 70B, where Raw JSON achieves the best mean F1 of 0.9956. In all 20 model and strategy combinations, mean precision exceeds mean recall: omission is the dominant failure mode, with models more often missing an active medication than fabricating one, which changes how clinical safety auditing priorities should be set. Smaller models plateau at roughly 7-10 concurrent active medications, leaving polypharmacy patients, the patients most at risk from reconciliation errors, systematically underserved. BioMistral-7B, a domain-pretrained model without instruction tuning, produces zero usable output in all conditions, showing that domain pretraining alone is not sufficient for structured extraction. These results offer practical, evidence-based format recommendations for clinical LLM deployment: Clinical Narrative for models up to 8B, Raw JSON for 70B and above. The complete pipeline is reproducible on open-source tools running on an AWS this http URL instance (NVIDIA L40S, 48 GB VRAM).

---


### 21. [Foveated Reasoning: Stateful, Action-based Visual Focusing for Vision-Language Models](https://arxiv.org/abs/2604.21079)

**<font color=#1a73e8>作者：</font>** Juhong Min, Lazar Valkov, Vitali Petsiuk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models benefit from high-resolution images, but the increase in visual-token count incurs high compute overhead. Humans resolve this tension via foveation: a coarse view guides "where to look", while selectively acquired high-acuity evidence refines "what to think". We introduce Foveated Reasoner, an autoregressive vision-language framework that unifies foveation and reasoning within a single decoding trajectory. Starting from a low-resolution view, the model triggers foveation only when needed, retrieves high-resolution evidence from selected regions, and injects it back into the same decoding trajectory. We train the method with a two-stage pipeline: coldstart supervision to bootstrap foveation behavior, followed by reinforcement learning to jointly improve evidence acquisition and task accuracy while discouraging trivial "see-everything" solutions. Experiments show that the method learns effective foveation policies and achieves stronger accuracy under tight visual-token budgets across multiple vision-language benchmarks.

---


### 22. [Mind the Prompt: Self-adaptive Generation of Task Plan Explanations via LLMs](https://arxiv.org/abs/2604.21092)

**<font color=#1a73e8>作者：</font>** Gricel Vázquez, Alexandros Evangelidis, Sepeedeh Shahbeigi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Integrating Large Language Models (LLMs) into complex software systems enables the generation of human-understandable explanations of opaque AI processes, such as automated task planning. However, the quality and reliability of these explanations heavily depend on effective prompt engineering. The lack of a systematic understanding of how diverse stakeholder groups formulate and refine prompts hinders the development of tools that can automate this process. We introduce COMPASS (COgnitive Modelling for Prompt Automated SynthesiS), a proof-of-concept self-adaptive approach that formalises prompt engineering as a cognitive and probabilistic decision-making process. COMPASS models unobservable users' latent cognitive states, such as attention and comprehension, uncertainty, and observable interaction cues as a POMDP, whose synthesised policy enables adaptive generation of explanations and prompt refinements. We evaluate COMPASS using two diverse cyber-physical system case studies to assess the adaptive explanation generation and their qualities, both quantitatively and qualitatively. Our results demonstrate the feasibility of COMPASS integrating human cognition and user profile's feedback into automated prompt synthesis in complex task planning systems.

---


### 23. [Propensity Inference: Environmental Contributors to LLM Behaviour](https://arxiv.org/abs/2604.21098)

**<font color=#1a73e8>作者：</font>** Olli Järviniemi, Oliver Makins, Jacob Merizian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Motivated by loss of control risks from misaligned AI systems, we develop and apply methods for measuring language models' propensity for unsanctioned behaviour. We contribute three methodological improvements: analysing effects of changes to environmental factors on behaviour, quantifying effect sizes via Bayesian generalised linear models, and taking explicit measures against circular analysis. We apply the methodology to measure the effects of 12 environmental factors (6 strategic in nature, 6 non-strategic) and thus the extent to which behaviour is explained by strategic aspects of the environment, a question relevant to risks from misalignment. Across 23 language models and 11 evaluation environments, we find approximately equal contributions from strategic and non-strategic factors for explaining behaviour, do not find strategic factors becoming more or less influential as capabilities improve, and find some evidence for a trend for increased sensitivity to goal conflicts. Finally, we highlight a key direction for future propensity research: the development of theoretical frameworks and cognitive models of AI decision-making into empirically testable forms.

---


### 24. [Leveraging Multimodal LLMs for Built Environment and Housing Attribute Assessment from Street-View Imagery](https://arxiv.org/abs/2604.21102)

**<font color=#1a73e8>作者：</font>** Siyuan Yao, Siavash Ghorbany, Kuangshi Ai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a novel framework for automatically evaluating building conditions nationwide in the United States by leveraging large language models (LLMs) and Google Street View (GSV) imagery. By fine-tuning Gemma 3 27B on a modest human-labeled dataset, our approach achieves strong alignment with human mean opinion scores (MOS), outperforming even individual raters on SRCC and PLCC relative to the MOS benchmark. To enhance efficiency, we apply knowledge distillation, transferring the capabilities of Gemma 3 27B to a smaller Gemma 3 4B model that achieves comparable performance with a 3x speedup. Further, we distill the knowledge into a CNN-based model (EfficientNetV2-M) and a transformer (SwinV2-B), delivering close performance while achieving a 30x speed gain. Furthermore, we investigate LLMs' capabilities for assessing an extensive list of built environment and housing attributes through a human-AI alignment study and develop a visualization dashboard that integrates LLM assessment outcomes for downstream analysis by homeowners. Our framework offers a flexible and efficient solution for large-scale building condition assessment, enabling high accuracy with minimal human labeling effort.

---


### 25. [Pretrain Where? Investigating How Pretraining Data Diversity Impacts Geospatial Foundation Model Performance](https://arxiv.org/abs/2604.21104)

**<font color=#1a73e8>作者：</font>** Amandeep Kaur, Mirali Purohit, Gedeon Muhawenayo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> New geospatial foundation models introduce a new model architecture and pretraining dataset, often sampled using different notions of data diversity. Performance differences are largely attributed to the model architecture or input modalities, while the role of the pretraining dataset is rarely studied. To address this research gap, we conducted a systematic study on how the geographic composition of pretraining data affects a model's downstream performance. We created global and per-continent pretraining datasets and evaluated them on global and per-continent downstream datasets. We found that the pretraining dataset from Europe outperformed global and continent-specific pretraining datasets on both global and local downstream evaluations. To investigate the factors influencing a pretraining dataset's downstream performance, we analysed 10 pretraining datasets using diversity across continents, biomes, landcover and spectral values. We found that only spectral diversity was strongly correlated with performance, while others were weakly correlated. This finding establishes a new dimension of diversity to be accounted for when creating a high-performing pretraining dataset. We open-sourced 7 new pretraining datasets, pretrained models, and our experimental framework at this https URL.

---


### 26. [How Much Is One Recurrence Worth? Iso-Depth Scaling Laws for Looped Language Models](https://arxiv.org/abs/2604.21106)

**<font color=#1a73e8>作者：</font>** Kristian Schwethelm, Daniel Rueckert, Georgios Kaissis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We measure how much one extra recurrence is worth to a looped (depth-recurrent) language model, in equivalent unique parameters. From an iso-depth sweep of 116 pretraining runs across recurrence counts $r \in \{1, 2, 4, 8\}$ spanning ${\sim}50\times$ in training compute, we fit a joint scaling law $L = E + A\,(N_\text{once} + r^{\varphi} N_\text{rec})^{-\alpha} + B\,D^{-\beta}$ and recover a new recurrence-equivalence exponent $\varphi = 0.46$ at $R^2 = 0.997$. Intuitively, $\varphi$ tells us whether looping a block $r$ times is equivalent in validation loss to $r$ unique blocks of a non-looped model (full equivalence, $\varphi{=}1$) or to a single block run repeatedly with no capacity gain ($\varphi{=}0$). Our $\varphi = 0.46$ sits in between, so each additional recurrence predictably increases validation loss at matched training compute. For example, at $r{=}4$ a 410M looped model performs on par with a 580M non-looped model, but pays the training cost of a 1B non-looped one. On a five-axis downstream evaluation, the gap persists on parametric-knowledge tasks and closes on simple open-book tasks, while reasoning tasks are not resolvable at our compute budgets. For any looped LM, our $\varphi$ converts the design choice of $r$ into a predictable validation-loss cost, and future training recipes and architectures can be compared by how much they raise $\varphi$ above $0.46$.

---


### 27. [Machine learning and digital pragmatics: Which word category influences emoji use most?](https://arxiv.org/abs/2604.21108)

**<font color=#1a73e8>作者：</font>** Mohammed Q. Shormani, Ibrahim Abdulmalik Hassan Muneef Y. Alshawsh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study investigates Machine Learning (ML) in the prediction of emojis in Arabic tweets employing the (state-of-the-art) MARBERT model. A corpus of 11379 CA tweets representing multiple Arabic colloquial dialects was collected from this http URL via Python. A net dataset includes 8695 tweets, which were utilized for the analysis. These tweets were then classified into 14 categories, which were numerically encoded and used as labels. A preprocessing pipeline was designed as an interpretable baseline, allowing us to examine the relationship between lexical features and emoji categories. MARBERT was finetuned to predict emoji use from textual input. We evaluated the model performance in terms of precision, recall and F1-scores. Findings reveal that the model performed quite well with an overall accuracy 0.75. The study concludes that although the findings are promising, there is still a need for improving machine learning models including MARBERT, specifically for low-resource and multidialectal languages like Arabic.

---


### 28. [HyperFM: An Efficient Hyperspectral Foundation Model with Spectral Grouping](https://arxiv.org/abs/2604.21127)

**<font color=#1a73e8>作者：</font>** Zahid Hassan Tushar, Sanjay Purushotham  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The NASA PACE mission provides unprecedented hyperspectral observations of ocean color, aerosols, and clouds, offering new insights into how these components interact and influence Earth's climate and air quality. Its Ocean Color Instrument measures light across hundreds of finely spaced wavelength bands, enabling detailed characterization of features such as phytoplankton composition, aerosol properties, and cloud microphysics. However, hyperspectral data of this scale is large, complex, and difficult to label, requiring specialized processing and analysis techniques. Existing foundation models, which have transformed computer vision and natural language processing, are generally trained on standard RGB imagery and therefore struggle to interpret the continuous spectral signatures captured by PACE. While recent advances have introduced hyperspectral foundation models, they are typically trained on cloud-free observations and often remain limited to single-sensor datasets due to spectral inconsistencies across instruments. Moreover, existing models tend to be parameter-heavy and computationally expensive, limiting scalability and adoption in operational settings. To address these challenges, we introduce HyperFM, a parameter-efficient hyperspectral foundation model that leverages intra-group and inter-group spectral attention along with hybrid parameter decomposition to better capture spectral spatial relationships while reducing computational cost. HyperFM demonstrates consistent performance improvements over existing hyperspectral foundation models and task-specific state-of-the-art methods across four benchmark downstream atmospheric cloud property retrieval tasks. To support further research, we additionally release HyperFM250K, a large-scale hyperspectral dataset from the PACE mission that includes both clear and cloudy scenes.

---


### 29. [Slot Machines: How LLMs Keep Track of Multiple Entities](https://arxiv.org/abs/2604.21139)

**<font color=#1a73e8>作者：</font>** Paul C. Bogdan, Jack Lindsey  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models must bind entities to the attributes they possess and maintain several such binding relationships within a context. We study how multiple entities are represented across token positions and whether single tokens can carry bindings for more than one entity. We introduce a multi-slot probing approach that disentangles a single token's residual stream activation to recover information about both the currently described entity and the immediately preceding one. These two kinds of information are encoded in separate and largely orthogonal "current-entity" and "prior-entity" slots. We analyze the functional roles of these slots and find that they serve different purposes. In tandem with the current-entity slot, the prior-entity slot supports relational inferences, such as entity-level induction ("who came after Alice in the story?") and conflict detection between adjacent entities. However, only the current-entity slot is used for explicit factual retrieval questions ("Is anyone in the story tall?" "What is the tall entity's name?") despite these answers being linearly decodable from the prior-entity slot too. Consistent with this limitation, open-weight models perform near chance accuracy at processing syntax that forces two subject-verb-object bindings on a single token (e.g., "Alice prepares and Bob consumes food.") Interestingly, recent frontier models can parse this properly, suggesting they may have developed more sophisticated binding strategies. Overall, our results expose a gap between information that is available in activations and information the model actually uses, and suggest that the current/prior-entity slot structure is a natural substrate for behaviors that require holding two perspectives at once, such as sycophancy and deception.

---


### 30. [Agentic AI for Personalized Physiotherapy: A Multi-Agent Framework for Generative Video Training and Real-Time Pose Correction](https://arxiv.org/abs/2604.21154)

**<font color=#1a73e8>作者：</font>** Abhishek Dharmaratnakar, Srivaths Ranganathan, Anushree Sinha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> At-home physiotherapy compliance remains critically low due to a lack of personalized supervision and dynamic feedback. Existing digital health solutions rely on static, pre-recorded video libraries or generic 3D avatars that fail to account for a patient's specific injury limitations or home environment. In this paper, we propose a novel Multi-Agent System (MAS) architecture that leverages Generative AI and computer vision to close the tele-rehabilitation loop. Our framework consists of four specialized micro-agents: a Clinical Extraction Agent that parses unstructured medical notes into kinematic constraints; a Video Synthesis Agent that utilizes foundational video generation models to create personalized, patient-specific exercise videos; a Vision Processing Agent for real-time pose estimation; and a Diagnostic Feedback Agent that issues corrective instructions. We present the system architecture, detail the prototype pipeline using Large Language Models and MediaPipe, and outline our clinical evaluation plan. This work demonstrates the feasibility of combining generative media with agentic autonomous decision-making to scale personalized patient care safely and effectively.

---


### 31. [Trust but Verify: Introducing DAVinCI -- A Framework for Dual Attribution and Verification in Claim Inference for Language Models](https://arxiv.org/abs/2604.21193)

**<font color=#1a73e8>作者：</font>** Vipula Rawte, Ryan Rossi, Franck Dernoncourt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated remarkable fluency and versatility across a wide range of NLP tasks, yet they remain prone to factual inaccuracies and hallucinations. This limitation poses significant risks in high-stakes domains such as healthcare, law, and scientific communication, where trust and verifiability are paramount. In this paper, we introduce DAVinCI - a Dual Attribution and Verification framework designed to enhance the factual reliability and interpretability of LLM outputs. DAVinCI operates in two stages: (i) it attributes generated claims to internal model components and external sources; (ii) it verifies each claim using entailment-based reasoning and confidence calibration. We evaluate DAVinCI across multiple datasets, including FEVER and CLIMATE-FEVER, and compare its performance against standard verification-only baselines. Our results show that DAVinCI significantly improves classification accuracy, attribution precision, recall, and F1-score by 5-20%. Through an extensive ablation study, we isolate the contributions of evidence span selection, recalibration thresholds, and retrieval quality. We also release a modular DAVinCI implementation that can be integrated into existing LLM pipelines. By bridging attribution and verification, DAVinCI offers a scalable path to auditable, trustworthy AI systems. This work contributes to the growing effort to make LLMs not only powerful but also accountable.

---


### 32. [Toward Efficient Membership Inference Attacks against Federated Large Language Models: A Projection Residual Approach](https://arxiv.org/abs/2604.21197)

**<font color=#1a73e8>作者：</font>** Guilin Deng, Silong Chen, Yuchuan Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Large Language Models (FedLLMs) enable multiple parties to collaboratively fine-tune LLMs without sharing raw data, addressing challenges of limited resources and privacy concerns. Despite data localization, shared gradients can still expose sensitive information through membership inference attacks (MIAs). However, FedLLMs' unique properties, i.e. massive parameter scales, rapid convergence, and sparse, non-orthogonal gradients, render existing MIAs ineffective. To address this gap, we propose ProjRes, the first projection residuals-based passive MIA tailored for FedLLMs. ProjRes leverages hidden embedding vectors as sample representations and analyzes their projection residuals on the gradient subspace to uncover the intrinsic link between gradients and inputs. It requires no shadow models, auxiliary classifiers, or historical updates, ensuring efficiency and robustness. Experiments on four benchmarks and four LLMs show that ProjRes achieves near 100% accuracy, outperforming prior methods by up to 75.75%, and remains effective even under strong differential privacy defenses. Our findings reveal a previously overlooked privacy vulnerability in FedLLMs and call for a re-examination of their security assumptions. Our code and data are available at $\href{this https URL}{link}$.

---


### 33. [ARFBench: Benchmarking Time Series Question Answering Ability for Software Incident Response](https://arxiv.org/abs/2604.21199)

**<font color=#1a73e8>作者：</font>** Stephan Xie, Ben Cohen, Mononito Goswami 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series question-answering (TSQA), in which we ask natural language questions to infer and reason about properties of time series, is a promising yet underexplored capability of foundation models. In this work, we present ARFBench, a TSQA benchmark that evaluates the understanding of multimodal foundation models (FMs) on time series anomalies prevalent in software incident data. ARFBench consists of 750 questions across 142 time series and 5.38M data points from 63 production incidents sourced exclusively from internal telemetry at Datadog. We evaluate leading proprietary and open-source LLMs, VLMs, and time series FMs and observe that frontier VLMs perform markedly better than existing baselines; the leading model (GPT-5) achieves a 62.7% accuracy and 51.9% F1. We next demonstrate the promise of specialized multimodal approaches. We develop a novel TSFM + VLM hybrid prototype which we post-train on a small set of synthetic and real data that yields comparable overall F1 and accuracy with frontier models. Lastly, we find models and human domain experts exhibit complementary strengths. We define a model-expert oracle, a best-of-2 oracle selector over model and expert answers, yielding 82.8% F1 and 87.2% accuracy and establishing a new superhuman frontier for future TSQA models. The benchmark is available at this https URL.

---


### 34. [Align Generative Artificial Intelligence with Human Preferences: A Novel Large Language Model Fine-Tuning Method for Online Review Management](https://arxiv.org/abs/2604.21209)

**<font color=#1a73e8>作者：</font>** Yanan Wang, Yong Ge  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online reviews have played a pivotal role in consumers' decision-making processes. Existing research has highlighted the significant impact of managerial review responses on customer relationship management and firm performance. However, a large portion of online reviews remains unaddressed due to the considerable human labor required to respond to the rapid growth of online reviews. While generative AI has achieved remarkable success in a range of tasks, they are general-purpose models and may not align well with domain-specific human preferences. To tailor these general generative AI models to domain-specific applications, finetuning is commonly employed. Nevertheless, several challenges persist in finetuning with domain-specific data, including hallucinations, difficulty in representing domain-specific human preferences, and over conservatism in offline policy optimization. To address these challenges, we propose a novel preference finetuning method to align an LLM with domain-specific human preferences for generating online review responses. Specifically, we first identify the source of hallucination and propose an effective context augmentation approach to mitigate the LLM hallucination. To represent human preferences, we propose a novel theory-driven preference finetuning approach that automatically constructs human preference pairs in the online review domain. Additionally, we propose a curriculum learning approach to further enhance preference finetuning. To overcome the challenge of over conservatism in existing offline preference finetuning method, we propose a novel density estimation-based support constraint method to relax the conservatism, and we mathematically prove its superior theoretical guarantees. Extensive evaluations substantiate the superiority of our proposed preference finetuning method.

---


### 35. [Zero-Shot Detection of LLM-Generated Text via Implicit Reward Model](https://arxiv.org/abs/2604.21223)

**<font color=#1a73e8>作者：</font>** Runheng Liu, Heyan Huang, Xingchen Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated remarkable capabilities across various tasks. However, their ability to generate human-like text has raised concerns about potential misuse. This underscores the need for reliable and effective methods to detect LLM-generated text. In this paper, we propose IRM, a novel zero-shot approach that leverages Implicit Reward Models for LLM-generated text detection. Such implicit reward models can be derived from publicly available instruction-tuned and base models. Previous reward-based method relies on preference construction and task-specific fine-tuning. In comparison, IRM requires neither preference collection nor additional training. We evaluate IRM on the DetectRL benchmark and demonstrate that IRM can achieve superior detection performance, outperforms existing zero-shot and supervised methods in LLM-generated text detection.

---


### 36. [ReCAPA: Hierarchical Predictive Correction to Mitigate Cascading Failures](https://arxiv.org/abs/2604.21232)

**<font color=#1a73e8>作者：</font>** Xiyin Zeng, Yuyu Sun, Haoyang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action systems follow instructions to execute multi-step tasks in multimodal environments. Recent VLA approaches typically rely on post-hoc correction mechanisms or operate under fixed task decompositions and alignment schemes. However, once an intermediate step is mis-specified, local errors propagate through subsequent steps and eventually accumulate into cascading failures. To mitigate this compounding effect, we propose Predictive Alignment and Planning Architecture, a framework that uses prediction and contrast to adjust deviations across three levels: actions, subgoals, and trajectories. Semantic alignment is enforced at all levels using a Sinkhorn-based module and a Score-field module. The predictive correction and alignment jointly update the action generator during training, enabling it to adjust fine-grained steps to remain aligned with the overall intent. We further introduce two new metrics to quantify error propagation and recovery processes in tasks, capturing how mistakes spread and fade over long-horizon execution. Experiments show that ReCAPA achieves competitive results on embodied agent benchmarks such as VisualAgentBench, MineDojo, and AI2-THOR, outperforming strong proprietary and open-source Large Language Model baselines.

---


### 37. [Learning Dynamic Representations and Policies from Multimodal Clinical Time-Series with Informative Missingness](https://arxiv.org/abs/2604.21235)

**<font color=#1a73e8>作者：</font>** Zihan Liang, Ziwen Pan, Ruoxuan Xiong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal clinical records contain structured measurements and clinical notes recorded over time, offering rich temporal information about the evolution of patient health. Yet these observations are sparse, and whether they are recorded depends on the patient's latent condition. Observation patterns also differ across modalities, as structured measurements and clinical notes arise under distinct recording processes. While prior work has developed methods that accommodate missingness in clinical time series, how to extract and use the information carried by the observation process itself remains underexplored. We therefore propose a patient representation learning framework for multimodal clinical time series that explicitly leverages informative missingness. The framework combines (1) a multimodal encoder that captures signals from structured and textual data together with their observation patterns, (2) a Bayesian filtering module that updates a latent patient state over time from observed multimodal signals, and (3) downstream modules for offline treatment policy learning and patient outcome prediction based on the learned patient state. We evaluate the framework on ICU sepsis cohorts from MIMIC-III, MIMIC-IV, and eICU. It improves both offline treatment policy learning and adverse outcome prediction, achieving FQE 0.679 versus 0.528 for clinician behavior and AUROC 0.886 for post-72-hour mortality prediction on MIMIC-III.

---


### 38. [Unlocking the Power of Large Language Models for Multi-table Entity Matching](https://arxiv.org/abs/2604.21238)

**<font color=#1a73e8>作者：</font>** Yingkai Tang, Taoyu Su, Wenyuan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-table entity matching (MEM) addresses the limitations of dual-table approaches by enabling simultaneous identification of equivalent entities across multiple data sources without unique identifiers. However, existing methods relying on pre-trained language models struggle to handle semantic inconsistencies caused by numerical attribute variations. Inspired by the powerful language understanding capabilities of large language models (LLMs), we propose a novel LLM-based framework for multi-table entity matching, termed LLM4MEM. Specifically, we first propose a multi-style prompt-enhanced LLM attribute coordination module to address semantic inconsistencies. Then, to alleviate the matching efficiency problem caused by the surge in the number of entities brought by multiple data sources, we develop a transitive consensus embedding matching module to tackle entity embedding and pre-matching issues. Finally, to address the issue of noisy entities during the matching process, we introduce a density-aware pruning module to optimize the quality of multi-table entity matching. We conducted extensive experiments on 6 MEM datasets, and the results show that our model improves by an average of 5.1% in F1 compared with the baseline model. Our code is available at this https URL.

---


### 39. [CAP: Controllable Alignment Prompting for Unlearning in LLMs](https://arxiv.org/abs/2604.21251)

**<font color=#1a73e8>作者：</font>** Zhaokun Wang, Jinyu Guo, Jingwen Pu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) trained on unfiltered corpora inherently risk retaining sensitive information, necessitating selective knowledge unlearning for regulatory compliance and ethical safety. However, existing parameter-modifying methods face fundamental limitations: high computational costs, uncontrollable forgetting boundaries, and strict dependency on model weight access. These constraints render them impractical for closed-source models, yet current non-invasive alternatives remain unsystematic and reliant on empirical experience. To address these challenges, we propose the Controllable Alignment Prompting for Unlearning (CAP) framework, an end-to-end prompt-driven unlearning paradigm. CAP decouples unlearning into a learnable prompt optimization process via reinforcement learning, where a prompt generator collaborates with the LLM to suppress target knowledge while preserving general capabilities selectively. This approach enables reversible knowledge restoration through prompt revocation. Extensive experiments demonstrate that CAP achieves precise, controllable unlearning without updating model parameters, establishing a dynamic alignment mechanism that overcomes the transferability limitations of prior methods.

---


### 40. [When Agents Look the Same: Quantifying Distillation-Induced Similarity in Tool-Use Behaviors](https://arxiv.org/abs/2604.21255)

**<font color=#1a73e8>作者：</font>** Chenghao Yang, Yuning Zhang, Zhoufutu Wen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Model distillation is a primary driver behind the rapid progress of LLM agents, yet it often leads to behavioral homogenization. Many emerging agents share nearly identical reasoning steps and failure modes, suggesting they may be distilled echoes of a few dominant teachers. Existing metrics, however, fail to distinguish mandatory behaviors required for task success from non-mandatory patterns that reflect a model's autonomous preferences. We propose two complementary metrics to isolate non-mandatory behavioral patterns: \textbf{Response Pattern Similarity (RPS)} for verbal alignment and \textbf{Action Graph Similarity (AGS)} for tool-use habits modeled as directed graphs. Evaluating 18 models from 8 providers on $\tau$-Bench and $\tau^2$-Bench against Claude Sonnet 4.5 (thinking), we find that within-family model pairs score 5.9 pp higher in AGS than cross-family pairs, and that Kimi-K2 (thinking) reaches 82.6\% $S_{\text{node}}$ and 94.7\% $S_{\text{dep}}$, exceeding Anthropic's own Opus 4.1. A controlled distillation experiment further confirms that AGS distinguishes teacher-specific convergence from general improvement. RPS and AGS capture distinct behavioral dimensions (Pearson $r$ = 0.491), providing complementary diagnostic signals for behavioral convergence in the agent ecosystem. Our code is available at this https URL.

---


### 41. [Enhancing Online Recruitment with Category-Aware MoE and LLM-based Data Augmentation](https://arxiv.org/abs/2604.21264)

**<font color=#1a73e8>作者：</font>** Minping Chen, Bing Xu, Zulong Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Person-Job Fit (PJF) is a critical component for online recruitment. Existing approaches face several challenges, particularly in handling low-quality job descriptions and similar candidate-job pairs, which impair model performance. To address these challenges, this paper proposes a large language model (LLM) based method with two novel techniques: (1) LLM-based data augmentation, which polishes and rewrites low-quality job descriptions by leveraging chain-of-thought (COT) prompts, and (2) category-aware Mixture of Experts (MoE) that assists in identifying similar candidate-job pairs. This MoE module incorporates category embeddings to dynamically assign weights to the experts and learns more distinguishable patterns for similar candidate-job pairs. We perform offline evaluations and online A/B tests on our recruitment platform. Our method relatively surpasses existing methods by 2.40% in AUC and 7.46% in GAUC, and boosts click-through conversion rate (CTCVR) by 19.4% in online tests, saving millions of CNY in external headhunting expenses.

---


### 42. [Listen and Chant Before You Read: The Ladder of Beauty in LM Pre-Training](https://arxiv.org/abs/2604.21265)

**<font color=#1a73e8>作者：</font>** Yoshinori Nomura  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We show that pre-training a Transformer on music before language significantly accelerates language acquisition. Using piano performances (MAESTRO dataset), a developmental pipeline -- music $\to$ poetry $\to$ prose -- yields a $17.5\%$ perplexity improvement over random initialization ($p < 0.001$, 5 seeds), with music and poetry improving orthogonal model components (internal computation and embeddings, respectively). Convergence tests confirm that this is not a transient head start: at $d\!=\!64$, multi-seed validation (5 seeds) shows a persistent 5.5\% gap at plateau ($p = 0.017$), with the pipeline converging faster and to a lower loss in every run. Real music matches the transfer ceiling of synthetic patterns with one-third the data, and scaling experiments reveal that optimal pre-training data volume shifts with model capacity ($-3\% \to +3\% \to +6\%$ advantage of larger datasets from $d\!=\!16$ to $d\!=\!64$). Across the scales we study ($d\!\in\!\{16,32,64\}$, up to ${\sim}400$K parameters), these results suggest a capacity-dependent data curation principle and indicate that structured human creative outputs can provide an efficient pre-training substrate for small language models; stronger conclusions at modern pre-training scale will require substantially larger experiments.

---


### 43. [Do LLM Decoders Listen Fairly? Benchmarking How Language Model Priors Shape Bias in Speech Recognition](https://arxiv.org/abs/2604.21276)

**<font color=#1a73e8>作者：</font>** Srishti Ginjala, Eric Fosler-Lussier, Christopher W. Myers 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As pretrained large language models replace task-specific decoders in speech recognition, a critical question arises: do their text-derived priors make recognition fairer or more biased across demographic groups? We evaluate nine models spanning three architectural generations (CTC with no language model, encoder-decoder with an implicit LM, and LLM-based with an explicit pretrained decoder) on about 43,000 utterances across five demographic axes (ethnicity, accent, gender, age, first language) using Common Voice 24 and Meta's Fair-Speech, a controlled-prompt dataset that eliminates vocabulary confounds. On clean audio, three findings challenge assumptions: LLM decoders do not amplify racial bias (Granite-8B has the best ethnicity fairness, max/min WER = 2.28); Whisper exhibits pathological hallucination on Indian-accented speech with a non-monotonic insertion-rate spike to 9.62% at large-v3; and audio compression predicts accent fairness more than LLM scale. We then stress-test these findings under 12 acoustic degradation conditions (noise, reverberation, silence injection, chunk masking) across both datasets, totaling 216 inference runs. Severe degradation paradoxically compresses fairness gaps as all groups converge to high WER, but silence injection amplifies Whisper's accent bias up to 4.64x by triggering demographic-selective hallucination. Under masking, Whisper enters catastrophic repetition loops (86% of 51,797 insertions) while explicit-LLM decoders produce 38x fewer insertions with near-zero repetition; high-compression audio encoding (Q-former) reintroduces repetition pathology even in LLM decoders. These results suggest that audio encoder design, not LLM scaling, is the primary lever for equitable and robust speech recognition.

---


### 44. [Can MLLMs "Read" What is Missing?](https://arxiv.org/abs/2604.21277)

**<font color=#1a73e8>作者：</font>** Jindi Guo, Xi Fang, Chaozheng Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce MMTR-Bench, a benchmark designed to evaluate the intrinsic ability of Multimodal Large Language Models (MLLMs) to reconstruct masked text directly from visual context. Unlike conventional question-answering tasks, MMTR-Bench eliminates explicit prompts, requiring models to recover masked text from single- or multi-page inputs across real-world domains such as documents and webpages. This design isolates the reconstruction task from instruction-following abilities, enabling a direct assessment of a model's layout understanding, visual grounding, and knowledge integration. MMTR-Bench comprises 2,771 test samples spanning multiple languages and varying target lengths. To account for this diversity, we propose a level-aware evaluation protocol. Experiments on representative MLLMs show that the benchmark poses a significant challenge, especially for sentence- and paragraph-level reconstruction. The homepage is available at this https URL.

---


### 45. [Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture](https://arxiv.org/abs/2604.21284)

**<font color=#1a73e8>作者：</font>** Robin Dey, Panyanon Viradecha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> MemPalace is an open-source AI memory system that applies the ancient method of loci (memory palace) spatial metaphor to organize long-term memory for large language models; launched in April 2026, it accumulated over 47,000 GitHub stars in its first two weeks and claims state-of-the-art retrieval performance on the LongMemEval benchmark (96.6% Recall@5) without requiring any LLM inference at write time. Through independent codebase analysis, benchmark replication, and comparison with competing systems, we find that MemPalace's headline retrieval performance is attributable primarily to its verbatim storage philosophy combined with ChromaDB's default embedding model (all-MiniLM-L6-v2), rather than to its spatial organizational metaphor per se -- the palace hierarchy (Wings->Rooms->Closets->Drawers) operates as standard vector database metadata filtering, an effective but well-established technique. However, MemPalace makes several genuinely novel contributions: (1) a contrarian verbatim-first storage philosophy that challenges extraction-based competitors, (2) an extremely low wake-up cost (approximately 170 tokens) through its four-layer memory stack, (3) a fully deterministic, zero-LLM write path enabling offline operation at zero API cost, and (4) the first systematic application of spatial memory metaphors as an organizing principle for AI memory systems. We also note that the competitive landscape is evolving rapidly, with Mem0's April 2026 token-efficient algorithm raising their LongMemEval score from approximately 49% to 93.4%, narrowing the gap between extraction-based and verbatim approaches. Our analysis concludes that MemPalace represents significant architectural insight wrapped in overstated claims -- a pattern common in rapidly adopted open-source projects where marketing velocity exceeds scientific rigor.

---


### 46. [Temporal Prototyping and Hierarchical Alignment for Unsupervised Video-based Visible-Infrared Person Re-Identification](https://arxiv.org/abs/2604.21324)

**<font color=#1a73e8>作者：</font>** Zhiyong Li, Wei Jiang, Haojie Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visible-infrared person re-identification (VI-ReID) enables cross-modality identity matching for all-day surveillance, yet existing methods predominantly focus on the image level or rely heavily on costly identity annotations. While video-based VI-ReID has recently emerged to exploit temporal dynamics for improved robustness, existing studies remain limited to supervised settings. Crucially, the unsupervised video VI-ReID problem, where models must learn from RGB and infrared tracklets without identity labels, remains largely unexplored despite its practical importance in real-world deployment. To bridge this gap, we propose HiTPro (Hierarchical Temporal Prototyping), a prototype-driven framework without explicit hard pseudo-label assignment for unsupervised video-based VI-ReID. HiTPro begins with an efficient Temporal-aware Feature Encoder that first extracts discriminative frame-level features and then aggregates them into a robust tracklet-level representation. Building upon these features, HiTPro first constructs reliable intra-camera prototypes via Intra-Camera Tracklet Prototyping by aggregating features from temporally partitioned sub-tracklets. Through Hierarchical Cross-Prototype Alignment, we perform a two-stage positive mining process: progressing from within-modality associations to cross-modality matching, enhanced by Dynamic Threshold Strategy and Soft Weight Assignment. Finally, {Hierarchical Contrastive Learning} progressively optimizes feature-prototype alignment across three levels: intra-camera discrimination, cross-camera same-modality consistency, and cross-modality invariance. Extensive experiments on HITSZ-VCM and BUPTCampus demonstrate that HiTPro achieves state-of-the-art performance under fully unsupervised settings, significantly outperforming adapted baselines and establishes a strong baseline for future research.

---


### 47. [MiMIC: Mitigating Visual Modality Collapse in Universal Multimodal Retrieval While Avoiding Semantic Misalignment](https://arxiv.org/abs/2604.21326)

**<font color=#1a73e8>作者：</font>** Juan Li, Chuanghao Ding, Xujie Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Universal Multimodal Retrieval (UMR) aims to map different modalities (e.g., visual and textual) into a shared embedding space for multi-modal retrieval. Existing UMR methods can be broadly divided into two categories: early-fusion approaches, such as Marvel, which projects visual features into the language model (LM) space for integrating with text modality, and late-fusion approaches, such as UniVL-DR, which encode visual and textual inputs using separate encoders and obtain fused embeddings through addition. Our pilot study reveals that Marvel exhibits visual modality collapse, which is characterized by the model's tendency to disregard visual features while depending excessively on textual cues. In contrast, although UniVL-DR is less affected by this issue, it is more susceptible to semantic misalignment, where semantically related content is positioned far apart in the embedding space. To address these challenges, we propose MiMIC, which introduces two key innovations: (1) a fusion-in-decoder architecture for effective multimodal integration, and (2) robust training through single modality mixin and random caption dropout. Experiments on the WebQA+ and EVQA+ datasets, where image in documents or queries might lack captions, indicate that MiMIC consistently outperforms both early- and late-fusion baselines.

---


### 48. [Ideological Bias in LLMs' Economic Causal Reasoning](https://arxiv.org/abs/2604.21334)

**<font color=#1a73e8>作者：</font>** Donggyu Lee, Hyeok Yun, Jungwon Kim 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Do large language models (LLMs) exhibit systematic ideological bias when reasoning about economic causal effects? As LLMs are increasingly used in policy analysis and economic reporting, where directionally correct causal judgments are essential, this question has direct practical stakes. We present a systematic evaluation by extending the EconCausal benchmark with ideology-contested cases - instances where intervention-oriented (pro-government) and market-oriented (pro-market) perspectives predict divergent causal signs. From 10,490 causal triplets (treatment-outcome pairs with empirically verified effect directions) derived from top-tier economics and finance journals, we identify 1,056 ideology-contested instances and evaluate 20 state-of-the-art LLMs on their ability to predict empirically supported causal directions. We find that ideology-contested items are consistently harder than non-contested ones, and that across 18 of 20 models, accuracy is systematically higher when the empirically verified causal sign aligns with intervention-oriented expectations than with market-oriented ones. Moreover, when models err, their incorrect predictions disproportionately lean intervention-oriented, and this directional skew is not eliminated by one-shot in-context prompting. These results highlight that LLMs are not only less accurate on ideologically contested economic questions, but systematically less reliable in one ideological direction than the other, underscoring the need for direction-aware evaluation in high-stakes economic and policy settings.

---


### 49. [Latent Denoising Improves Visual Alignment in Large Multimodal Models](https://arxiv.org/abs/2604.21343)

**<font color=#1a73e8>作者：</font>** Dhruv Parikh, Jacob Fein-Ashley, Rajgopal Kannan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Multimodal Models (LMMs) such as LLaVA are typically trained with an autoregressive language modeling objective, providing only indirect supervision to visual tokens. This often yields weak internal visual representations and brittle behavior under distribution shift. Inspired by recent progress on latent denoising for learning high-quality visual tokenizers, we show that the same principle provides an effective form of visual supervision for improving internal visual feature alignment and multimodal understanding in LMMs. We propose a latent denoising framework that corrupts projected visual tokens using a saliency-aware mixture of masking and Gaussian noising. The LMM is trained to denoise these corrupted tokens by recovering clean teacher patch features from hidden states at a selected intermediate LLM layer using a decoder. To prevent representation collapse, our framework also preserves the teacher's intra-image similarity structure and applies intra-image contrastive patch distillation. During inference, corruption and auxiliary heads are disabled, introducing no additional inference-time overhead. Across a broad suite of standard multimodal benchmarks, our method consistently improves visual understanding and reasoning over strong baselines, and yields clear gains on compositional robustness benchmarks (e.g., NaturalBench). Moreover, under ImageNet-C-style non-adversarial common corruptions applied to benchmark images, our method maintains higher accuracy and exhibits reduced degradation at both moderate and severe corruption levels. Our code is available at this https URL.

---


### 50. [Symbolic Grounding Reveals Representational Bottlenecks in Abstract Visual Reasoning](https://arxiv.org/abs/2604.21346)

**<font color=#1a73e8>作者：</font>** Mohit Vaishnav, Tanel Tammet  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision--language models (VLMs) often fail on abstract visual reasoning benchmarks such as Bongard problems, raising the question of whether the main bottleneck lies in reasoning or representation. We study this on Bongard-LOGO, a synthetic benchmark of abstract concept learning with ground-truth generative programs, by comparing end-to-end VLMs on raw images with large language models (LLMs) given symbolic inputs derived from those images. Using symbolic inputs as a diagnostic probe rather than a practical multimodal architecture, our \emph{Componential--Grammatical (C--G)} paradigm reformulates Bongard-LOGO as a symbolic reasoning task based on LOGO-style action programs or structured descriptions. LLMs achieve large and consistent gains, reaching mid--90s accuracy on Free-form problems, while a strong visual baseline remains near chance under matched task definitions. Ablations on input format, explicit concept prompts, and minimal visual grounding show that these factors matter much less than the shift from pixels to symbolic structure. These results identify representation as a key bottleneck in abstract visual reasoning and show how symbolic input can serve as a controlled diagnostic upper bound.

---


> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-97](./part-02.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
