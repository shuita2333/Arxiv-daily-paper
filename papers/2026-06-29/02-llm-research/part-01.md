# 🧠 大模型相关研究 | 2026年06月29日

> 本类共 **135** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-135](./part-03.md)

---

### 1. [Know2Guess: A Contamination-Aware Multi-Zone Benchmark for Knowledge-Boundary Evaluation in Large Language Models](https://arxiv.org/abs/2606.26101)

**<font color=#1a73e8>作者：</font>** Renwei Meng, Bowen Zhang, Jian Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable evaluation of large language models should separate supported answering from unsupported guessing without conflating either with data contamination, prompt idiosyncrasy, or generic refusal behavior. We present a contamination-aware, multi-zone benchmark for measuring the transition from answerable knowledge to abstention-expected unknowns under frozen build-time labels. The benchmark contains 1,200 items across five domains, explicit abstention expectations, contamination-risk metadata, and dual parsing with an official strict parser plus a normalized robustness parser. We evaluate FLAN-T5, Qwen2.5-Instruct, and Llama-3-Instruct models under locked answer-or-abstain prompts, answer-only controls, and prompt-template variants. The benchmark is not solved by generic non-answer behavior: FLAN baselines remain weak on productive abstention, while stronger instruction-tuned models expose a selective but incomplete transition from answering to abstaining. Qwen2.5-3B-Instruct achieves the best overall reliability, but answer-expected zones remain difficult, calibration remains poor, and benign-item refusal persists. Prompt and parser robustness analyses preserve the main ranking and qualitative conclusions. The benchmark therefore provides a reproducible protocol for auditing answerability, abstention, refusal, and contamination as distinct but interacting dimensions of LLM this http URL dataset is publicly available at this https URL.

---


### 2. [Helpfulness Hurts: Domain-Dependent Degradation of Mid-Trained Compassion Values Under Post-Training](https://arxiv.org/abs/2606.26102)

**<font color=#1a73e8>作者：</font>** Jasmine Brazilek, Juliana Seawell  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard post-training pipelines apply supervised fine-tuning (SFT) and reinforcement learning (RL) to make language models helpful, but these processes may inadvertently degrade values instilled during pre-training. We investigate whether the domain of post-training data differentially affects the retention of animal compassion values in a Llama 3.1 8B model mid-trained on compassion-oriented synthetic data, using both SFT (helpfulness via Dolly-15k vs. coding via Magicoder-110K) and GRPO (helpfulness via RLHFlow vs. coding via Magicoder), evaluated on the Animal Harm Benchmark (AHB 2.2) and MORU benchmark (Moral Reasoning Under Uncertainty). Helpfulness training significantly degrades animal compassion relative to coding training on AHB (SFT: 35.7% vs. 65.2%; GRPO: 18.7% vs. 32.0%), replicating across two independent helpfulness datasets and two training paradigms. On English MORU items, helpfulness training degrades general moral reasoning by 25.5 percentage points (46.4% vs. 71.9%), a striking gap that rivals the compassion effect in magnitude. However, this effect does not transfer cross-lingually: on the multilingual MORU benchmark, the domain effect disappears (SFT: 52.3% vs. 51.2%). In contrast, the animal compassion effect transfers consistently across languages, with Magicoder's AHB percentage-point gain over the base model 4.5 times larger on non-English items than English items. This divergence suggests that values instilled through mid-training are encoded more deeply and cross-lingually than reasoning improvements from domain-specific post-training. These results suggest that, for labs building on value-laden mid-training, coding-domain post-training may better preserve mid-trained values than helpfulness post-training without harming general reasoning capabilities.

---


### 3. [Investigating LLM's Problem Solving Capability -- a Study on Statics Questions](https://arxiv.org/abs/2606.26103)

**<font color=#1a73e8>作者：</font>** Tanner Culleton, Hung-Fu Chang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have rapidly influenced many aspects of society, particularly education, due to their demonstrated ability to complete assignments and examinations across a wide range of subjects. Although prior studies have examined the educational impact of LLMs, much of the existing work relies on public or open problem datasets and lacks topic-specific analysis. In engineering education, especially within mechanical engineering, systematic investigations of LLM performance on specific problem types remain limited. Instead of using traditional methods that directly ask textbook questions to an LLM tool, our study adopts a model distillation process to evaluate LLM capabilities in solving statics problems. By distilling ChatGPT, we extracted 25 text-only statics questions and further constructed two additional datasets by adding diagrams and modifying their numerical values. Experimental results show that while LLMs perform well on text-only statics problems, their accuracy decreases when diagrams are introduced and the problems require multi-step reasoning. Further analysis suggests that this performance drop is not primarily caused by limitations in image recognition, but rather by difficulties in multi-step reasoning and in consistently applying extracted visual information across successive solution stages.

---


### 4. [Assert, don't describe: Linguistic features that shift LLM reasoning about animal welfare](https://arxiv.org/abs/2606.26104)

**<font color=#1a73e8>作者：</font>** Jasmine Brazilek, Harper Dunn  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Animal-welfare advocates produce a lot of writing, and increasingly that writing trains the language models that millions of people then ask about animal welfare. Using vocabulary-matched stance-contrast probes on a held-out animal-welfare benchmark, we measure how each of ten linguistic features changes Llama-3.2-1B's preference for pro-animal-welfare reasoning when used as fine-tuning data. Eight of the ten features produce statistically significant shifts. Seven move the model toward stronger pro-animal-welfare reasoning: assertive certainty, explicit moral vocabulary, emotion words, evaluative claims, narrative structure, depicted harm severity, and immediate temporal framing. Two move it the other way: hedged language and concrete sensory description both dilute the pro-animal-welfare stance. First-person perspective has no statistically significant effect. The practical recommendation for anyone writing animal-welfare text that may end up in LLM training corpora: assert a position rather than describe a scene neutrally. The features that shift the model are the ones that make the writer's position explicit; the features that dilute it hold animal-welfare content but withhold stance.

---


### 5. [Context Recycling for Long-Horizon LLM Inference](https://arxiv.org/abs/2606.26105)

**<font color=#1a73e8>作者：</font>** Derek Thomas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit strong capabilities in short-context reasoning but degrade in performance over long conversational horizons due to context window limitations and inefficient token usage. We introduce ContextForge, a system for context recycling that maintains task-relevant information across turns by combining structured query generation, external memory retrieval, and controlled synthesis. The system enables efficient reuse of prior computation without relying on full context replay, reducing token overhead while preserving answer quality. We evaluate ContextForge using a 15-turn conversational benchmark that tests multi-turn reasoning, back-references, and domain shifts across structured healthcare queries. Compared to a baseline agent using identical underlying models, ContextForge demonstrates improved consistency and reduced token consumption, while maintaining comparable response accuracy. These results suggest that context recycling provides a practical approach for extending LLM capabilities in long-horizon tasks without requiring larger context windows or model retraining. Code and evaluation artifacts are available at this https URL.

---


### 6. [Reducing Conversational Escalation in Large Language Model Dialogue with Nonviolent Communication Constraints](https://arxiv.org/abs/2606.26106)

**<font color=#1a73e8>作者：</font>** Zhixing Sun, Shenghe Xu, Tao Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in emotionally charged situations involving interpersonal conflict, frustration, and distress. While prior safety research has focused on preventing explicit harms such as toxic or policy-violating content, less attention has been paid to conversational behaviors that may unintentionally escalate conflict. In this paper, we investigate whether LLMs can be guided toward more de-escalating dialogue behavior through lightweight prompt-level constraints derived from Nonviolent Communication (NVC). We reformulate NVC principles as process-oriented guidelines that discourage blame attribution, emphasize attention to users' emotional experiences, and encourage clarification before advice. Using a dual-agent simulation framework across multiple instruction-tuned models and user resistance levels, we show that NVC-constrained prompting consistently reduces conversational escalation and stabilizes interactions with highly resistant users. These results suggest that simple communication constraints can meaningfully improve the trustworthiness of LLM dialogue in conflict-prone settings.

---


### 7. [Low Resource Multimodal Translation of Nepali Spoken Words into Emotion-Conditioned Sign Language Avatars](https://arxiv.org/abs/2606.26107)

**<font color=#1a73e8>作者：</font>** Jatin Bhusal, Salma Tamang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sign language communication systems, that integrate emotional expression remain underexplored, particularly for low-resource languages. This pilot study presents NEST-V1 (Nepali Emotion and Speech Transformer - Version 1), a proof-of-concept multimodal framework that demonstrates the feasibility of generating emotion-conditioned Nepali Sign Language avatars from spoken input. As a preliminary investigation, we focus on four common Nepali words ("thank you", "hello", "house", "me") across three emotional states (happy, neutral, sad) to validate our core technical approach. Our lightweight architecture employs a shared acoustic encoder for simultaneous Automatic Speech Recognition and emotion classification, achieving 81.1% ASR accuracy and 79.21% emotion recognition accuracy on a dataset of 600 labeled audio samples from 50 speakers. The system demonstrates 37% parameter efficiency compared to separate model architectures while maintaining a lightweight footprint with only 22.1M parameters suitable for edge deployment. This pilot work establishes the technical foundation for emotion-aware sign language translation in low-resource settings and provides a scalable framework for future expansion to larger vocabularies and more diverse emotional expressions. Our preliminary results indicate the viability of real-time, emotionally expressive sign language communication systems for the hearing-impaired community, with clear pathways for enhancement in subsequent development phases.

---


### 8. [Where Larger Models Excel: The Primacy of Constraint-Guided Reasoning](https://arxiv.org/abs/2606.26108)

**<font color=#1a73e8>作者：</font>** Guan-Yi Lin, Hen-Hsen Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Larger language models consistently outperform smaller ones on reasoning benchmarks, yet the reasoning differences underlying this gap remain underexplored. Across benchmarks in mathematics, physics, chemistry, and programming, we observe stable performance gaps: averaged over datasets, Qwen3-32B outperforms Qwen3-8B by 6.43%, while GPT-OSS-120B exceeds GPT-OSS-20B by 7.38%. To study the reasoning differences behind these gains, we develop AdvCluster, an automated framework that identifies questions where the larger model shows a stable advantage, extracts fine-grained advantage descriptions from paired reasoning traces produced by larger and smaller models, and organizes them through semantic clustering with quantitative evaluation and selection guided by a reviewer model. Our analysis yields a systematic taxonomy of larger model reasoning advantages, spanning both common advantages that recur across domains and specialized advantages associated with particular domains. Across these patterns, a recurring theme is Constraint-Guided Reasoning: larger models are better at identifying explicit and implicit constraints, organizing them into structured reasoning, and using them to rule out infeasible paths and verify intermediate steps.

---


### 9. [Dynamic-dLLM: Dynamic Cache-Budget and Adaptive Parallel Decoding for Training-Free Acceleration of Diffusion LLM](https://arxiv.org/abs/2606.26120)

**<font color=#1a73e8>作者：</font>** Tianyi Wu, Xiaoxi Sun, Yanhua Jiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (dLLMs) offer a promising alternative to autoregressive models, excelling in text generation tasks due to their bidirectional attention mechanisms. However, their computational complexity scales on the order of L cubed with the sequence length L. This poses significant challenges for long-sequence and real-time applications, primarily due to the lack of compatibility with key-value caching and the non-autoregressive nature of denoising steps. Existing acceleration methods rely on static caching or parallel decoding strategies, which fail to account for the dynamic behavior of token properties across layers and decoding steps. We propose Dynamic-dLLM, a training-free framework that enhances dLLM inference efficiency through two components: Dynamic Cache Updating (DCU), which adaptively allocates cache-update budgets based on layer-wise token dynamics, and Adaptive Parallel Decoding (APD), which dynamically calibrates decoding thresholds to balance generation quality and efficiency. Extensive experiments on models like LLaDA-8B-Instruct, LLaDA-1.5, and Dream-v0-7B-Instruct across benchmarks such as MMLU, GSM8K, and HumanEval demonstrate that Dynamic-dLLM significantly improves inference speed. It attains an average speedup exceeding 3 times while maintaining performance. Dynamic-dLLM outperforms state-of-the-art acceleration methods and provides a plug-and-play solution for efficient dLLM deployment without compromising performance. The code is available at this https URL.

---


### 10. [DocArena: Turning Raw Documents into Controllable Training Environments for Document Search Agents](https://arxiv.org/abs/2606.26122)

**<font color=#1a73e8>作者：</font>** Jiamian Wang, Ruiyi Zhang, Tong Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent methods train search agents via reinforcement learning from (question, answer, evidence) tuples without requiring expert trajectories. The tuples serve as the training environment, and whose properties directly shape what search strategies and generalization abilities the agent can develop. While prior works have made encouraging progress in improving training data quality, existing environments remain predominantly text-based and existing approaches can struggle to construct training environments that are controllable, scalable, and account for multimodal data. Given this, we propose DocArena, a fully automated data curation pipeline building on the practical need for multimodal document search and question-answering. It transforms raw document collections into training environments for search agents without any human annotation. The pipeline first structures and indexes documents through MLLM-based visual perception, then profiles and leverage the cross-page information distribution to construct reasoning-intensive QA pairs, as well as performs cascaded quality assurance operations via MLLM. We introduce DocArena-79K with QA pairs from 8,336 documents spanning 16 domains and 49 languages. We further design a Doc-Search agent infrastructure that decouples visual perception from the policy model, allowing text-based LLMs to serve as the reasoning backbone for multimodal document retrieval and QA. Under a unified evaluation framework where only the policy model differs, experiments on six multimodal document scenarios and seven text-based QA benchmarks show that agents trained on DocArena data achieve the best performance on both retrieval accuracy and QA quality. Further analysis on agent search behaviors confirms the effectiveness and controllability of the constructed training environment.

---


### 11. [Thinking Like a Scientist? A Structural Study of LLM-Generated Research Methods](https://arxiv.org/abs/2606.26130)

**<font color=#1a73e8>作者：</font>** Francesca Carlon, Brecht Verbeken, Vincent Ginis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used to guide research methodology, yet their default methodological tendencies under minimal prompting remain unclear. Here, we prompt GPT-5.1, Gemini 3 Pro, and DeepSeek-V3.2 with an LLM-extracted research question from each of 1,000 recent arXiv computer-science papers and compare the resulting methodology suggestions against a paper-derived experimental inventory. Since we provide only the research question, the differences we measure reflect initial suggestions and not how optimal those suggestions are. We extract structured method features from both sources, map them into a shared taxonomy, and quantify divergence across multiple taxonomy dimensions including model provider, dataset task type, and evaluation metric type. The strongest imbalance appears in provider choice, with Jensen-Shannon divergence about 3-5x larger than any other taxonomy dimension. Other/Academic single-occurrence models are underrepresented by 23-24 percentage points, while reused academic/community models are slightly overrepresented (4-6pp). LLMs also suggest a much narrower range of methods overall: the effective number of model entities contracts from 1,232 to 59-96, and inter-LLM rank correlations (0.55-0.68) generally exceed LLM-to-paper correlations (0.33-0.56), so the distortions are largely shared across models. Popularity baselines, BM25 retrieval calibration, and paper-level similarity tests confirm that the outputs are query-specific responses, but filtered through a narrower set of options. Researchers who rely on LLM suggestions without cross-checking therefore risk narrowing their methodological search space toward a more concentrated default.

---


### 12. [\chisao{}: A GPU-Native Parallel Optimizer for Multimodal Black-Box Functions via Convergence-Anticonvergence Oscillation](https://arxiv.org/abs/2606.26164)

**<font color=#1a73e8>作者：</font>** Ira Wolfson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finding all modes of a multimodal black-box function is a fundamental challenge in optimization, Bayesian inference, and scientific computing. Existing approaches -- basin-hopping, CMA-ES, multistart gradient descent -- operate sequentially and cannot exploit the massive parallelism of modern GPU hardware. We introduce \chisao{} (\textbf{C}onvergence-\textbf{H}alt-\textbf{I}nvert-\textbf{S}tick-\textbf{A}nd-\textbf{O}scillate), a GPU-native population optimizer that runs an entire sample batch simultaneously and exploits a deliberate convergence-anticonvergence oscillation cycle to escape local traps while freezing confirmed modes. The structural move is asymmetric: samples that reach true peaks are frozen (``stuck'') and preserved, while the rest keep exploring via momentum-based anti-convergence and stochastically smoothed gradients. Adaptive reseeding via two complementary strategies (Repulse Monkey and Golden Rooster) maintains population diversity throughout. On all 42 functions of the Simon Fraser University optimization benchmark suite across dimensions $d \in \{2, 4, 8, 16, 32, 64\}$, \chisao{} achieves \textbf{100\%} mode recovery where all CPU baselines collapse at $d \geq 8$ on the hardest multimodal functions, at up to \textbf{$34\times$} speedup over basin-hopping on functions where all methods succeed (Michalewicz $d=64$) and up to \textbf{$39\times$} on unimodal functions (Rotated Hyper-Ellipsoid $d=64$, pure GPU dividend). All benchmarks evaluate the objective by value alone -- gradients come from finite differences -- so the reported speedups are a derivative-free worst case. Under substantial likelihood noise ($\sigma_{\mathrm{noise}}$ up to 1.0), mode detection remains 100\% reliable. The algorithm is available as a standalone open-source Python package on PyPI.

---


### 13. [AlgoEvolve: LLM-driven Meta-evolution of Algorithmic Trading Programs](https://arxiv.org/abs/2606.26173)

**<font color=#1a73e8>作者：</font>** Dhruv Sharma, Gautam Shroff  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work shows that Large Language Models (LLMs) can act as semantic mutation operators for the evolutionary discovery of programs and proofs. Most current applications focus on static coding benchmarks. We extend this paradigm to algorithmic trading. This domain is uniquely challenging because it is noisy, non-stationary, and highly discontinuous. We present AlgoEvolve, an LLM-driven evolutionary framework that generates, evaluates, and iteratively improves executable trading strategies. These strategies are expressed as Python code and evaluated through a rigorous testing protocol. Across multiple experiments, the system exhibits emergent regime-adaptive strategy logic, including autonomous shifts in trading rules. We further introduce a meta-evolutionary outer loop that evolves the prompts guiding program synthesis in the inner loop. This outer loop discovers improved search heuristics. These heuristics balance exploration and exploitation while reducing zero-trade failures. They consistently outperform initial human-designed instructions. The results demonstrate that LLM-based semantic evolution provides a viable approach for continual program synthesis in complex environments.

---


### 14. [Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations](https://arxiv.org/abs/2606.26185)

**<font color=#1a73e8>作者：</font>** Hiroki Tamba  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-as-judge ("grader") components are now standard in evaluation harnesses, including safety evaluations where a pass/fail verdict may gate downstream deployment decisions. A widespread assumption is that setting the grader's sampling temperature to 0 makes grading deterministic. We test this assumption against a real safety-evaluation codebase (Japan AISI's open-source aisev) and show it fails on two levels. First, the harness invokes its grader without setting temperature or seed; the underlying provider silently applies its default of 1.0, so items near the decision boundary flip pass/fail across identical runs (per-item disagreement up to ~50% over 20 runs). Second, pinning temperature=0 reduces but does not eliminate flips: across 690 API calls spanning two providers, three model tiers, and five sampling configurations, 1-2 of 7 borderline items remain non-reproducible even under forced greedy decoding (top_k=1). Claude Opus 4.7/4.8 has since deprecated temperature entirely, rendering the primary mitigation inapplicable to newer model generations. These findings expose a structural gap: evaluation harnesses that report single-run verdicts without variance or grader-disagreement metrics can present noise as a safety property. We release a reproduction harness (690 calls, 7 conditions) and recommend that harnesses treat grader disagreement as a first-class health metric alongside the scores themselves.

---


### 15. [From Structure to Synergy: A Survey of Vision-Language Perception Paradigm Evolution in Multimodal Large Language Models](https://arxiv.org/abs/2606.26196)

**<font color=#1a73e8>作者：</font>** Haoxiang Sun, Tao Wang, Li Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have recently made remarkable progress in unifying vision-language understanding and reasoning, especially following the introduction of models such as OpenAI's O-series and DeepSeek's R-series, which have driven a paradigm shift toward perception-centric intelligence. However, there remains a lack of systematic surveys that examine perception from a truly unified vision-language perspective -- one that treats vision and language as an inseparable modality. Existing reviews are often fragmented, focusing separately on either vision or language, and thus rarely capture the cross-modal evolution of perception as an integrated capability. To bridge this gap, we present the first systematic survey of unified vision-language perception in MLLMs. Specifically, we (1) formalize MLLM perception as an intrinsic, unified vision-language capability analogous to human innate perception, (2) introduce a five-stage taxonomy tracing the paradigm evolution of MLLM perception and survey representative methods and milestones at each phase, and (3) identify open challenges and outline promising research directions toward truly general, unified multimodal intelligence. We hope our study will provide both a foundational understanding and an actionable roadmap to foster further innovation on the path toward artificial general intelligence (AGI).

---


### 16. [Agentic Analysis for Agentic Infrastructure: An LLM-Powered Pipeline for Comparative Governance of DAO and Corporate AI Protocols](https://arxiv.org/abs/2606.26203)

**<font color=#1a73e8>作者：</font>** Yutian Wang, Luyao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI agent protocols proliferate, the governance structures shaping their interoperability standards remain empirically underexamined. We introduce an LLM-powered comparative pipeline for large-scale governance discourse analysis, integrating automated annotation, neural topic modeling, and multi-layer network analysis to study socio-technical power structures at scale. We validate it on two contrasting standards for agent interoperability: ERC-8004 (permissionless, on-chain) and Google A2A (corporate-led). Analyzing 4,323 governance participation records, we combine LLM-assisted coding, topic modeling, and multi-layer network analysis to examine how institutional design shapes thematic priorities and community structure. We find that while governance form influences substantive focus, both regimes exhibit comparable levels of participation inequality and community fragmentation. Discourse alignment is denser in the permissionless setting, suggesting that open governance may foster greater thematic convergence despite decentralized participation. These findings illustrate how LLM-assisted methods can advance the empirical study of technology governance, with implications for designing more equitable agentic AI standards. All data and code are openly available.

---


### 17. [Knowledge-augmented Agentic AI for Mental Health Medication Information Seeking](https://arxiv.org/abs/2606.26205)

**<font color=#1a73e8>作者：</font>** Huizi Yu, Jian Liu, Wenkong Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Patients increasingly seek medication information online, yet safety knowledge for psychiatric drugs is split between regulatory adverse-event records, which are authoritative but abstract, and patient narratives, which are experience-near but unvalidated. Integrating them without conflating evidence and anecdote is especially consequential in psychiatry, where poorly contextualised information can amplify fear, nocebo responses, and non-adherence. Here we develop a provenance-aware, knowledge-graph-based multi-agent framework unifying 466,525 Reddit posts, 60,782 WebMD reviews, and twenty years of U.S. FDA Adverse Event Reporting System records for nine antidepressants. A large-language-model entity-recognition pipeline benchmarked against physician annotations reached highest F1 scores of 0.969 for medications and 0.973 for conditions. The two community platforms were far more concordant with each other (overlap up to a Jaccard similarity of 0.905) than with regulatory reports, indicating that patient-generated data form a partly independent safety signal. For sertraline, many adverse events appeared in community sources hundreds of days before the corresponding FDA date. A Neo4j knowledge graph grounded in ATC-N, ICD-10, and MedDRA vocabularies preserves provenance, keeping every claim traceable and regulatory facts distinct from patient experience. These results establish source-aware integration as a route to more auditable psychiatric medication information, with usefulness and patient benefit to be tested prospectively.

---


### 18. [GeMoE: Gating Entropy is All You Need for Uncertainty-aware Adaptive Routing in MoE-based Large Vision-Language Models](https://arxiv.org/abs/2606.26287)

**<font color=#1a73e8>作者：</font>** Chaoxiang Cai, Minghe Weng, Jie Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the increase in model parameters and training data, the instruction following and generalization capabilities of Large VisionLanguage Models (LVLMs) have been significantly improved. Based on the Mixture of Experts (MoE) architecture, LVLMs expand their parameter capacity while maintaining the inference cost. However, traditional MoE methods employ a Top-k static routing strategy, which fails to account for variations in the input and adaptively select the number of experts, resulting in suboptimal resource utilization. In this paper, we propose viewing token routing as an information encoding task, framing dynamic routing as a Minimum Description Length (MDL) problem in encoding By validating the connection between MDL and gating entropy in the MoE scenario, we introduce Gating Entropy-based Uncertainty-aware Adaptive Routing (GeMoE) for MoE. Unlike traditional static or heuristic-based dynamic routing methods, GeMoE explicitly models the trade-off between model complexity and performance. By using gating entropy to assess the complexity of tokens, GeMoE adaptively determines the number of experts each token should engage. On a wide range of backbones and benchmarks, our method achieves 99.5% average performance retention compared to the original static routing, while improving average expert activation sparsity by 36.5%.

---


### 19. [SSM Adapters via Hankel Reduced-order Modeling: Injection Site Determines Task Suitability in Long-Context Fine-Tuning](https://arxiv.org/abs/2606.26290)

**<font color=#1a73e8>作者：</font>** Omanshu Thapliyal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While parameter-efficient fine-tuning (PEFT) typically targets attention projectors, its efficacy for tasks requiring sequential state accumulation remains under-explored. We examine if PEFT for such tasks can benefit from state space model (SSMs) adapters, and if MLP blocks are better injection sites. We introduce Hankel Reduced order Model (HRM) adapter, an SSM-based residual module initialized via Balanced Truncation of empirical Hankel Grammians. By leveraging the time-invariance of the system matrix $\bar{A}$, HRM enables an exact FFT-based parallel scan, achieving computational parity with LoRA across all context lengths. In iso-parametric evaluations on Mistral-7B (8.4M trainable parameters), HRM outperforms LoRA variants on LongBench tasks, including QuALITY (+34.8\% relative accuracy) and QMSum (+71.6\% relative ROUGE-1). HRM further demonstrates consistent superiority across 18 configurations of synthetic state-tracking (DFA, Parity) and character-level language modeling (enwik8). Gate analysis reveals that HRM adapters effectively learn to modulate recurrence, providing a robust architectural alternative to low-rank adaptation for long-context sequence modeling.

---


### 20. [EVOM: Agentic Meta-Evolution of Actor-Critic Architectures for Reinforcement Learning](https://arxiv.org/abs/2606.26327)

**<font color=#1a73e8>作者：</font>** Boyun Zhang, Chao Wang, Kai Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In actor-critic reinforcement learning, network architectures are typically manually designed. Automating this design is challenging because each candidate must be trained before evaluation, and the design space is open-ended. To address these challenges, we introduce EVOM, an agentic meta-evolution framework for discovering high-performance actor-critic architectures. We frame architecture search as a bi-level optimization: an inner loop trains weights via the low-fidelity proximal policy optimization (PPO), while an outer loop drives meta-evolution by iteratively refining architecture programs. Crucially, this outer loop is powered by an LLM-based design agent that operates purely as an architecture designer, completely decoupled from policy execution and environment control. Experiments reveal that EVOM outperforms the manually designed baseline, an LLM-guided random search, and the state-of-the-art LLM-guided programmatic policy search method MLES, delivering superior performance on Ant-v4 and HalfCheetah-v4. Ablation studies validate that both the meta-evolution loop and the LLM Design Agent are indispensable for final performance.

---


### 21. [How Do Tool-Augmented LLM Agents Perform on Real-World Energy Analytics Tasks?](https://arxiv.org/abs/2606.26346)

**<font color=#1a73e8>作者：</font>** David Akinpelu, Akintonde Abbas, Rereloluwa Alimi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic benchmarks have emerged across general-purpose and domain-specific settings, including finance, coding, law, and drug discovery, yet energy-domain evaluations remain largely limited to static knowledge recall. This is a critical gap for a sector that requires live data retrieval, specialized regulatory and market knowledge, and multi-step quantitative reasoning under real-world constraints.
We present an empirical study of tool-augmented LLM agents on real-world energy market analytics tasks. Our evaluation environment includes 243 expert-curated problems across three categories: (1) Market Data Retrieval and Analysis, (2) Knowledge Retrieval and Interpretation, and (3) Advanced Quantitative Modeling and Decision Analytics. Tasks include price and demand analysis, tariff impact modeling, asset revenue and returns estimation, hedging strategy analysis, and optimization modeling, with problems spanning multiple difficulty levels.
Agents are equipped with a configurable suite of domain tools, including live electricity market APIs for major U.S. ISOs, regulatory docket search, utility tariff databases, asset optimization models, and retrieval-augmented generation over energy market documents. We assess agent responses using a multi-dimensional evaluation protocol that scores approach correctness, answer accuracy, attribute alignment, and source validity, with category-aware routing to match scoring criteria to question type. We evaluate both closed-source and open-source LLMs, providing a comparative analysis of how model capability and domain tooling interact in a high-stakes professional domain. Key artifacts are publicly released to support reproducibility and future research.

---


### 22. [What We are Missing in Multimodal LLM Evaluation?](https://arxiv.org/abs/2606.26348)

**<font color=#1a73e8>作者：</font>** Po-han Li, Shenghui Chen, Sandeep Chinchali 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) can process diverse inputs, e.g., text, images, audio, and video, and generate textual responses. While their capabilities have advanced rapidly, evaluation of such models has not kept pace. Most existing evaluation benchmarks are limited to isolated tasks and reveal little about whether a model integrates information across modalities. We examine current means for evaluating MLLMs and review the existing benchmark taxonomy to identify gaps, including temporal-spatial coherence, physical world understanding, multimodal consistency, and selective attention. Addressing these gaps is essential for measuring real progress in multimodal intelligence and exposing capability boundaries.

---


### 23. [OpenFinGym: A Verifiable Multi-Task Gym Environment for Evaluating Quant Agents](https://arxiv.org/abs/2606.26350)

**<font color=#1a73e8>作者：</font>** Kaicheng Zhang, Wen Ge, Lei Jiang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although large language model agents are increasingly applied to quantitative-finance workflows, their evaluation remains fragmented across isolated tasks, while the financial relevance of benchmark tasks is often overlooked. Yet financial workflows are inherently multi-stage, spanning interdependent tasks such as forecasting, strategy construction, risk management, and trading. Existing platforms typically focus on a single task, and can therefore overstate agent competence and fail to reveal weaknesses in generalization, real-market interaction, and financially meaningful decision-making. We introduce OpenFinGym, a unified gym environment for quantitative-finance agent development that covers forecasting, market generation, real-time trading, and fraud detection under a single execution and verification interface. OpenFinGym additionally provides an automated task-construction pipeline that turns quantitative finance publications into executable task packages; a containerised runtime with a host-side verifier service that supports scalable agent rollouts and prevents runtime train-test leakage; a paper trading engine with a low-latency data-stream design; deferred-resolution support for long-horizon and event-market forecasts; and integration for SFT and RL post-training

---


### 24. [Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems](https://arxiv.org/abs/2606.26356)

**<font color=#1a73e8>作者：</font>** Ching-Yu Lin, Yifan Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Practitioners of prompt-composed agentic systems report a recurring failure mode: editing one prompt module silently shifts the behavior of others despite no shared variable or executable dependency. We formalize this as compositional behavioral leakage (CBL): interference between modules sharing a context window. CBL is enabled by architectural non-isolation: transformer self-attention provides no formal boundary between concatenated modules. We probe CBL on a deployed job-evaluation agent (Claude Sonnet 4.6, 144 trials) through a reusable three-channel protocol that perturbs non-focal modules along volume, content, and form. Only the content channel produces a detectable paired effect (Cohen's d = 0.63, bootstrap 95% CI excluding zero); no recommendation flipped -- a sub-threshold regime invisible to standard QA but compounding across the thousands of decisions a deployed agent makes. CBL is orthogonal to known agent-failure axes (adversarial injection, cognitive degradation, multi-agent fault propagation, privacy leakage). We contribute an operational definition, a reusable protocol, a falsifiable prediction set, and a system-class characterization, establishing cross-module interference measurement as a requirement for prompt-composed agent evaluation.

---


### 25. [Narration-of-Thought: Inference-Time Scaffolding for Defeasible Ethical Reasoning in Large Language Models](https://arxiv.org/abs/2606.26366)

**<font color=#1a73e8>作者：</font>** Patrick Cooper, Alvaro Velasquez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Standard chain-of-thought on moral dilemmas exhibits two failure modes: stakeholder collapse (the trace names at most one party with a stake in the outcome) and uncertainty suppression (no explicit unknowns or hedges before committing to an action). We introduce narration-of-thought (NoT), a system prompt that structures chain-of-thought into five sections: protagonist, stakeholders, two-step consequences, uncertainty, then commitment. NoT adds no training, parameters, or fine-tuning. On 100 DailyDilemmas scenarios across four generators from three vendors, NoT cuts stakeholder collapse from up to 31% to under 1% and uncertainty suppression from up to 72% to 1-24% on every model. A matched-budget verbose-CoT control rules out token spend as the active ingredient; NoT retains Cliff's delta advantages of +0.79 to +0.90 on stakeholder count and +0.65 to +0.93 on uncertainty score for three of four generators, and a section ablation attributes each shift to its specific sub-instruction. Textual-gradient descent initialised at NoT improves the scaffold further; a cross-family training judge (different vendor from the generator) dominates an in-family one on every measured axis. Extended to a five-round multi-stakeholder debate protocol, the scaffold converts a 6% standoff into 95% full consensus on a calibration set and 100% combined convergence on a DailyDilemmas replication. The resulting traces externalise the stakeholders, consequences, and uncertainty grounding each commitment, providing an auditable substrate for dependable agentic deployment.

---


### 26. [Layer-Specific Prompt Fusion Discovery via Differentiable Search in Vision Foundation Models](https://arxiv.org/abs/2606.26379)

**<font color=#1a73e8>作者：</font>** Xi Xiao, Xingjian Li, Yunbei Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual prompt tuning has emerged as a parameter-efficient fine-tuning approach for adapting large-scale Vision Transformers (ViTs) to downstream tasks. As its learnable prompts are applied in input and feature spaces, prior to jointly going through attention in transformer layers, the most commonly used scheme for fusing image and prompt tokens is concatenation or addition. In this paper, we aim to study a fundamental yet essential problem in visual prompt tuning: whether a single fusion scheme tends to yield better results, and whether that would be beneficial to develop a hybrid fusion scheme. To this end, we formulate the task as a bi-level optimization problem, and solve it leveraging differentiable architecture search. In this context, the learnable prompts and their fusion schemes are jointly optimized. To enrich the search space in the architecture search, we propose two additional fusion schemes, namely, affine transformation and cross-attention, in addition to concatenation and addition. Extensive experiments on 34 datasets spanning VTAB-1k, FGVC, and HTA show consistent gains over prompt-tuning baselines. With a frozen ViT backbone, our method delivers a favorable accuracy--latency--parameter trade-off compared with VPT-Deep and recent variants. Our findings reveal that how prompts fuse with image tokens plays a significant role in visual prompt tuning, and a hybrid fusion fashion can more effectively leverage layer semantics of ViTs, contributing a novel perspective for visual prompt-tuning research.

---


### 27. [Charting the Growth of Social-Physical HRI (spHRI): A Systematic Review Pipeline Augmented by Small Language Models](https://arxiv.org/abs/2606.26382)

**<font color=#1a73e8>作者：</font>** Mayumi Mohan, Ju-Hung Chen, Alexis E. Block  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social-physical human-robot interaction (spHRI) has grown rapidly across robotics, human-computer interaction, human-robot interaction, and haptics. Yet, fragmented terminology and inconsistent methodologies make systematic synthesis difficult. To support scalable review practices, we evaluated the extent to which small language models (SLMs; < 1.5B parameters) can assist with title and abstract screening for a large spHRI systematic review. While no SLMs matched human reviewers' performance, the models operated locally and screened papers orders of magnitude faster. The combined SLM ensemble identified 39 papers reviewers missed, representing 10.29% of the final relevant dataset. These results demonstrate that SLMs can augment, rather than replace, expert reviewers and make large-scale literature reviews accessible and sustainable.

---


### 28. [Staying VIGILant: Mitigating Visual Laziness via Counterfactual Visual Alignment in MLLMs](https://arxiv.org/abs/2606.26387)

**<font color=#1a73e8>作者：</font>** Xi Xiao, Chen Liu, Chih-Ting Liao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) extend large language models (LLMs) with visual perception, enabling joint reasoning over images and text. Despite inheriting strong reasoning capabilities from LLMs, they remain prone to hallucinations that contradict their visual inputs. Mechanistic studies indicate that this weakness stems from visual laziness: MLLMs encode the correct visual evidence internally, but overly rely on strong language priors during response. Existing alignment methods, such as direct preference optimization, primarily optimize outcome-level rewards based on text. This introduces an optimization bias toward linguistic shortcuts, leading to responses that often contradict the visual evidence. To address this, we propose Visual Information Gain In aLignment (VIGIL), a reinforcement-learning (RL) post-training framework that shifts the focus from numerical reward fitting to causal visual grounding. VIGIL introduces a geometric constraint that explicitly maximizes the mutual information between the visual input and the generated response. We achieve this by penalizing "blind confidence" instances where the model remains improperly certain even when textual-visual attention is masked to create a counterfactual blind state. Extensive experiments show that VIGIL consistently outperforms recent alignment methods across hallucination and reasoning benchmarks without compromising text-only capabilities. Our approach matches the full-data performance of state-of-the-art methods using only 25% of the preference data and even demonstrates emergent spatial grounding capabilities without explicit bounding box supervision.

---


### 29. [At the Edge of Understanding: Sparse Autoencoders Trace The Limits of Transformer Generalization](https://arxiv.org/abs/2606.26396)

**<font color=#1a73e8>作者：</font>** Praneet Suresh, Jack Stanley, Sonia Joseph 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-trained transformers have demonstrated remarkable generalization abilities, at times extending beyond the scope of their training data. Yet, real-world deployments often face unexpected or adversarial data that diverges from training data distributions. Without explicit mechanisms for handling such shifts, model reliability and safety degrade, urging more disciplined study of out-of-distribution (OOD) settings for transformers. By systematic experiments, we present a mechanistic framework for delineating the precise contours of transformer model robustness. We find that OOD inputs, including subtle typos and jailbreak prompts, drive language models to operate on an increased number of fallacious concepts in their internals. We leverage this device to quantify and understand the degree of distributional shift in prompts, enabling a mechanistically grounded fine-tuning strategy to robustify LLMs. Expanding the very notion of OOD from input data to a model's private computational processes, a new transformer diagnostic at inference time is a critical step toward making AI systems safe for deployment across science, business, and government.

---


### 30. [ProfileFoundry: A Synthetic Person-Object Substrate for Privacy, Memory, and Tool-Use Evaluation in LLM Agent](https://arxiv.org/abs/2606.26403)

**<font color=#1a73e8>作者：</font>** Sriram Selvam, Anneswa Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Foundation-model research increasingly needs data about people: user state, personal histories, relationships, contact-like fields, documents, and longitudinal updates. Real user data is difficult to share, perturb, audit, or redistribute responsibly, while independently generated fake fields rarely preserve the cross-field and temporal consistency needed for controlled evaluation. We present PROFILEFOUNDRY, a deterministic generator and fixed reference release of 100,000 adult synthetic Person Objects across eight locales. Each object combines a typed current snapshot, household, family, and employer links, snapshot-aligned events, normalized relational views, and generation provenance. The release contains 709,228 events, 40,338 households, 52,491 employers, and 518,564 directed relationship edges. We report evidence in separate categories: selected population-marginal comparisons, per-object invariant checks, release-wide referential and temporal closure, and coincidence/provenance screens. PROFILEFOUNDRY is not a population-fidelity model, a rendered-text corpus, or a formal privacy mechanism. Instead, it is a responsible synthetic source layer for constructing downstream foundation-model evaluations involving memory, privacy, document understanding, record linkage, and agent state while keeping the synthetic person behind each artifact inspectable

---


### 31. [Methane-Plume Segmentation From Hyperspectral Satellite Imagery Via Multimodal Deep Learning](https://arxiv.org/abs/2606.26416)

**<font color=#1a73e8>作者：</font>** Brayan Quintero, Jeferson Acevedo, Samuel Traslaviña 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient detection of methane plumes is crucial for understanding and mitigating global warming, as accurately identifying and segmenting them in earth observation imagery remain essential for large-scale monitoring. In this work, we propose a multimodal deep learning model that integrates a feature-guided methane enhancement (FGME) mechanism which injects physically meaningful methane cues into transformer-based RGB representations at multiple semantic scales. Our method is evaluated on the MPDataset, where it outperforms the state-of-the-art with improvements of +0.92 in MIoU, +0.87 in MPrecision and +1.01 in Recall. Notably, these gains are obtained with a substantially lower computational cost than other high-performing architectures, resulting in a favorable accuracy-efficiency trade-off for large-scale methane monitoring. These results highlight the potential of efficient multimodal fusion strategies for accurate and scalable methane plume segmentation in real-world remote sensing applications.

---


### 32. [Estimating Uncertainty in Classifier Performance with Applications to Large Language Models and Nested Data](https://arxiv.org/abs/2606.26422)

**<font color=#1a73e8>作者：</font>** Kylie Anglin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Researchers increasingly use text classification--supervised models or large language models--to measure constructs from natural language, providing metrics such as recall and precision as evidence of their validity. Yet, though these metrics are point estimates subject to sampling variation, measures of uncertainty are inconsistently reported alongside them. Further, when they are reported, they are often estimated with methods that are not appropriate when relevant labelled datasets are small or performance is high. To increase and improve confidence interval reporting in the field, this paper evaluates confidence interval methods for performance metrics under conditions typical of social science text classification: small to moderate sample sizes, infrequent constructs, and texts nested within individuals. Across simulations, default methods such as the Wald interval and the basic percentile bootstrap are the least accurate, with coverage sometimes far below the nominal 95% level. Accuracy is improved with the use of Agresti-Coull, Wilson, Clopper-Pearson, and a novel pseudo-count regularized bootstrap (which is particularly relevant to the calculation of F1). When texts are nested within individuals, we demonstrate that adjustment for both effective N and the appropriate degrees of freedom is necessary for producing accurate analytic intervals. Among bootstrap intervals, the hierarchical bootstrap is more accurate than the cluster bootstrap when individuals produce a moderate number of texts but overly conservative when individuals produce only a few. By providing guidance to the field on appropriate interval estimation, we aim to improve the transparency of machine learning applications, and to encourage greater attention to the validation sample size at the design stage.

---


### 33. [DualEval: Joint Model-Item Calibration for Unified LLM Evaluation](https://arxiv.org/abs/2606.26429)

**<font color=#1a73e8>作者：</font>** Aaron J. Li, Hao Huang, Youngmin Park 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current LLM evaluation relies on two complementary but often disconnected signals: static benchmarks with objective correctness labels and arena-style preference data that better reflect open-ended user interactions. We introduce DualEval, a latent model-item calibration framework that represents models and evaluation items in a shared space, jointly estimating model ability together with item difficulty and sharpness. We apply DualEval across four domains: coding, math, miscellaneous domain-knowledge tasks, and generic everyday user queries. Our evaluation uses 18 frontier LLMs, static benchmark labels, and reward-model scores validated against held-out human preferences for open-ended model responses. Empirically, our framework produces reliable and balanced model rankings, and its learned item-level profiles support downstream applications such as benchmark compression for sample-efficient evaluation and anomaly detection for contamination or outlier analysis. Overall, DualEval unifies static and arena-style evaluation through joint model-item calibration, producing model rankings and item-level diagnostics that support more sample-efficient, interpretable, and auditable evaluation pipelines.

---


### 34. [Embedding Foundation Model Predictions in Discrete-Choice Models with Structural Guarantees](https://arxiv.org/abs/2606.26432)

**<font color=#1a73e8>作者：</font>** Yingshuo Wang, Xian Sun, Yanhang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models achieve strong accuracy on choice prediction tasks, but their predictions often violate the economic logic those tasks require: raising a price can increase predicted demand, implied willingness-to-pay estimates are frequently negative or implausible, and unavailable alternatives receive nonzero probability. We propose a two-stage adapter that takes a foundation model's predicted choice probabilities as a precomputed feature and embeds them inside a multinomial logit's utility. In Stage 1, we fit the multinomial logit's structural coefficients by maximum likelihood with sign constraints; in Stage 2, we freeze those coefficients and fit a small neural correction operating on the foundation model's predictions. We prove that this composition exactly preserves the multinomial logit's marginal rate of substitution, so analytically computable value-of-time becomes a mathematical guarantee rather than an empirical accident. Across three datasets and two foundation models, the adapter gains 6.4 percentage points (pp) of test accuracy on average over the multinomial logit and up to 12.8 pp, maintains 100% cost monotonicity, and produces values of time within the published transportation-economics range on the transportation datasets. Performance degrades gracefully under foundation-model context restriction, retaining at least 6 pp of accuracy gain even at 10% of the original foundation-model context.

---


### 35. [ConflictScore: Identifying and Measuring How Language Models Handle Conflicting Evidence](https://arxiv.org/abs/2606.26437)

**<font color=#1a73e8>作者：</font>** Siyi Liu, Aaron Halfaker, Dan Roth 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing metrics for factuality and faithfulness evaluate whether an answer is supported or contradicted by its grounding documents, but they fail to capture when both supporting and contradicting evidence coexist. We introduce ConflictScore, a novel metric that quantifies how well a model's response acknowledges conflicting evidence in its grounding documents. Our framework decomposes responses into atomic claims, labels each claim against each grounding document, and then aggregates these labels into two complementary measures: ConflictScore-Count (CS-C), the proportion of claims exhibiting conflicts, and ConflictScore-Ratio (CS-R), the balance between supporting and contradicting evidence. We develop ConflictBench, a benchmark covering diverse forms of conflicts such as ambiguity, contradiction, and divergent opinions, to systematically evaluate our metric. Experiments show that ConflictScore effectively detects overconfident claims across domains and can serve as a corrective feedback mechanism that improves truthfulness on TruthfulQA.

---


### 36. [Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization](https://arxiv.org/abs/2606.26453)

**<font color=#1a73e8>作者：</font>** Jiading Gai, Shuai Zhang, Kaj Bostrom 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present KernelPro, a closed-loop multi-agent system that automatically generates, profiles, and iteratively optimizes GPU kernel code by integrating large language model (LLM) code generation with hardware profiler feedback and pluggable bottleneck detection tools. KernelPro introduces four contributions: (1) a semantic feedback operator that encodes expert heuristics as pluggable micro-profiling tools, transforming raw hardware metrics into actionable natural language guidance; (2) a two-stage tool invocation architecture where roofline-based bottleneck classification filters which specialized analysis tools execute, combining kernel-level (ncu), instruction-level (SASS), and system-level (nsys) profiling; (3) a domain-adapted MCTS with progressive widening, asymmetric branching, log-reward calibration, dead-end pruning, and search memory for cross-iteration learning; and (4) direct CuTe source-level code generation via autonomous code search over the CUTLASS/CuTe codebase. On KernelBench, KernelPro achieves geometric mean speedups of 2.42x/4.69x/5.30x on Levels 1/2/3, establishing state-of-the-art performance across all difficulty levels. On VeOmni's expert-optimized MoE training kernels, KernelPro achieves 1.23x over hand-tuned Triton by generating a from-scratch raw-CUDA+CuTe Hopper WGMMA kernel. Ablation studies demonstrate that each design component independently and significantly improves optimization quality: micro-profiling tools (p < 0.0001 vs raw metrics), MCTS search (26% higher geometric mean vs greedy, p = 0.004), and proactive tool orchestration (23% improvement, p = 0.035). Finally, KernelPro is the first CUDA kernel coding agent to optimize energy efficiency beyond the speed-only focus of prior systems, demonstrating an 11.6% measured energy reduction at matched speed.

---


### 37. [MKG-RAG-Bench: Benchmarking Retrieval in Multimodal Knowledge Graph-Augmented Generation](https://arxiv.org/abs/2606.26458)

**<font color=#1a73e8>作者：</font>** Xiaochen Wang, Bao Hoang, Han Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) over knowledge graphs has emerged as a promising approach for grounding large language models, yet existing benchmarks largely overlook the challenges of retrieval in multimodal knowledge graph RAG (MKG-RAG). In practice, retrieval is a critical bottleneck: multimodal knowledge is heterogeneous, difficult to align across modalities, and often poorly served by retrievers designed for unstructured corpora. To address this gap, we introduce MKG-RAG-Bench, a cross-domain benchmark explicitly designed to evaluate retrieval in MKG-RAG. MKG-RAG-Bench is constructed from two multimodal knowledge graphs spanning general and medical domains, and includes carefully aligned question-answering datasets that support controlled evaluation of both retrieval and downstream generation. The benchmark is built using an LLM-based curation pipeline that filters low-utility knowledge, generates structurally grounded queries with exact supervision, and systematically covers diverse modality configurations. Through extensive experiments across representative retriever families and modality settings, we show that effective multimodal retrieval remains challenging yet crucial for end-to-end MKG-RAG performance, and that retrieval quality strongly determines generation outcomes. By isolating retrieval as a first-class evaluation target, MKG-RAG-Bench provides a principled foundation for diagnosing current limitations and advancing multimodal knowledge graph RAG systems.

---


### 38. [Soft Token Alignment for Cross-Lingual Reasoning](https://arxiv.org/abs/2606.26466)

**<font color=#1a73e8>作者：</font>** Jiayi He, Jungsoo Park, Wei Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual large language models often produce inconsistent reasoning and answers for semantically equivalent prompts in different languages. Prior work suggests that intermediate representations can be relatively language-agnostic, but generation becomes increasingly language-specific as models commit to discrete output tokens. This is problematic because language-specific lexical choices can cause semantically equivalent reasoning paths to diverge across languages. These divergences motivate searching for a cross-lingual alignment signal that is less tied to any single vocabulary item or script. We propose SOLAR, an auxiliary objective for supervised fine-tuning that aligns soft-token representations across languages, using English as a pivot. Soft tokens are probability-weighted mixtures over the vocabulary embeddings, yielding continuous representations that can aggregate information from semantically related tokens across languages. We then align each non-English soft-token summary to its English counterpart in the shared embedding space. Across four multilingual reasoning benchmarks, SOLAR improves accuracy by up to +17.7 points over the base model and +3.8 over standard supervised fine-tuning, with the largest gains on low-resource languages. SOLAR also strengthens final-layer cross-lingual similarity and substantially reduces language-cluster separability, suggesting that aligning soft-token representations helps preserve shared semantic structure during multilingual reasoning.

---


### 39. [A Causal Foundation Model for Structure and Outcome Prediction](https://arxiv.org/abs/2606.26467)

**<font color=#1a73e8>作者：</font>** Max Zhu, Martino Mansoldo, Ching-Hao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce TabPFN-CFM, a causal foundation model that can handle multiple causal problems. TabPFN-CFM predicts both causal structure and outcomes from observational data, supports queries on all three levels of Pearl's Causal Hierarchy and uses known graph structure when available to improve predictions. TabPFN-CFM is trained on synthetic datasets, and generalises to real datasets, demonstrating improved performance over both structural and outcome prediction baselines.

---


### 40. [When Does Quality-Aware Multimodal Fusion Matter? A Leakage-Safe Diagnostic for Decision-Level Dependence](https://arxiv.org/abs/2606.26473)

**<font color=#1a73e8>作者：</font>** Jaden Moon, Arvind Pillai, Andrew Campbell  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many multimodal systems estimate the reliability of each modality and weight their contributions to the final prediction. However, it remains unclear whether these scores influence model decisions or merely correlate with performance. We propose a simple diagnostic to test whether reliability information is used during inference. After training, the model and inputs are fixed while reliability scores are permuted across test examples. If predictions depend on these scores, performance should degrade. Experiments on StressID for stress recognition and CMU-MOSEI for sentiment analysis show that permuting reliability scores leaves performance unchanged despite substantial potential gains from selecting the best modality per example. In positive controls where reliability signals identify the correct modality, the same frozen fusion rules yield significant improvements, indicating that reliability signals influence fused decisions only when they reliably predict unimodal correctness.

---


### 41. [Localizing RL-Induced Tool Use to a Single Crosscoder Feature](https://arxiv.org/abs/2606.26474)

**<font color=#1a73e8>作者：</font>** Andrii Shportko, Shubham Bhokare, Ahmed Zeyad A Alzahrani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning through RL reshapes the internal representations of language models to enable agentic behaviors such as tool use, yet the mechanistic basis of these changes remains poorly understood. While RL substantially improves structured tool-call generation, it is unclear which features emerge, which are preserved, and whether identified features can be leveraged for retraining-free behavioral control. In this work, we show that $\textit{Dedicated Feature Crosscoders (DFC)}$ isolate a compact set of RL-specific features that mediate tool-calling capability in $\texttt{Qwen2.5-3B}$. Across a $48$-crosscoder hyperparameter sweep, encode-decode reconstruction improves the RL model's tool correctness by $+31.1 \pm {9.7}$ pp and passively transfers tool-calling ability to the frozen base model by $+6.8 \pm 5.0$ pp which we call a $\textit{capability spillover}$. Our findings show that DFC partitioning concentrates RL-introduced capability into a minimal, steerable feature set that enables runtime behavioral control of agentic LLMs.

---


### 42. [Extracting Problem and Method Sentence from Scientific Papers: A Context-enhanced Transformer Using Formulaic Expression Desensitization](https://arxiv.org/abs/2606.26481)

**<font color=#1a73e8>作者：</font>** Yingyi Zhang, Chengzhi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Billions of scientific papers lead to the need to identify essential parts from the massive text. Scientific research is an activity from putting forward problems to using methods. To learn the main idea from scientific papers, we focus on extracting problem and method sentences. Annotating sentences within scientific papers is labor-intensive, resulting in small-scale datasets that limit the amount of information models can learn. This limited information leads models to rely heavily on specific forms, which in turn reduces their generalization capabilities. This paper addresses the problems caused by small-scale datasets from three perspectives: increasing dataset scale, reducing dependence on specific forms, and enriching the information within sentences. To implement the first two ideas, we introduce the concept of formulaic expression (FE) desensitization and propose FE desensitization-based data augmenters to generate synthetic data and reduce models' reliance on FEs. For the third idea, we propose a context-enhanced transformer that utilizes context to measure the importance of words in target sentences and to reduce noise in the context. Furthermore, this paper conducts experiments using large language model (LLM) based in-context learning (ICL) methods. Quantitative and qualitative experiments demonstrate that our proposed models achieve a higher macro F1 score compared to the baseline models on two scientific paper datasets, with improvements of 3.71% and 2.67%, respectively. The LLM based ICL methods are found to be not suitable for the task of problem and method extraction.

---


### 43. [Speaking Numbers to LLMs: Multi-Wavelet Number Embeddings for Time Series Forecasting](https://arxiv.org/abs/2606.26487)

**<font color=#1a73e8>作者：</font>** Defu Cao, Zijie Lei, Muyan Weng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are attractive for context-aware time series forecasting because they can integrate heterogeneous textual signals, yet their discrete, language-oriented tokenization and embedding interfaces are misaligned with continuous numerical values, often harming numerical ordering and forecasting reliability. We propose TempoWave, a plug-and-play temporal wavelet digit interface that maps each scalar observation into digit-wise embeddings constructed from multi-wavelet, multi-scale coefficients. By directly overriding standard token representations, TempoWave seamlessly exposes both fine-grained local fluctuations and macro global structures in a transformer-compatible form, ensuring that precise numerical formatting, distinct digit identity, and robustness to common normalization operations are maintained throughout the LLM pipeline. Experiments across five context-enriched forecasting benchmarks demonstrate that TempoWave consistently improves LLM-based forecasters over standard numeric tokenization and alternative embedding interfaces, achieving a new state-of-the-art. These results highlight the numeric interface as a key bottleneck and suggest that principled multi-resolution embeddings can better couple LLMs' contextual reasoning with precise forecasting. Our code is available at this https URL and our model can be accessed at this https URL.

---


### 44. [Comparing BERT Sentence-Pair Classification and Few-Shot LLM Prompting for Detecting Threat and Solution Framing in German Climate News](https://arxiv.org/abs/2606.26489)

**<font color=#1a73e8>作者：</font>** Raven Adam, David Maier, Marie Kogler  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> News media play a central role in shaping public perceptions of climate change, and whether coverage emphasizes threats or solutions has measurable effects on audience engagement and policy support. Automated detection of these framing patterns at the sentence level would allow researchers to analyze large corpora that are infeasible to code manually. We present a systematic comparison of two approaches for classifying sentences from German-language climate news articles as threat-oriented, solution-oriented, both, or neither. The first approach uses few-shot prompting with an open-weights large language model (Llama 4 Maverick), employing chain-of-thought reasoning and structured output with confidence scoring. The second approach fine-tunes a German BERT model (deepset/gbert-large) for sentence-pair classification, where the preceding sentence provides contextual information for the target sentence. Both approaches implement two independent binary classifiers, one for threat framing and one for solution framing. We evaluate both methods on a corpus of 440 Austrian newspaper articles that were manually coded following a detailed coding scheme developed with domain experts. The fine-tuned BERT classifiers achieve an F1 score of 0.83 for both the threat and solution tasks, while the LLM-based classifiers reach an F1 of 0.78. An ablation study confirms that providing the preceding sentence as context improves BERT classification performance substantially compared to single-sentence input. These results contribute to the growing body of work comparing fine-tuned encoder models with prompted generative models for text classification in computational social science.

---


### 45. [Nemotron-TwoTower: Diffusion Language Modeling with Pretrained Autoregressive Context](https://arxiv.org/abs/2606.26493)

**<font color=#1a73e8>作者：</font>** Fitsum Reda, John Kamalu, Roger Waleffe 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models offer a promising alternative to autoregressive models due to their potential for parallel and iterative generation. However, existing approaches use a single network for both context representation and iterative denoising, forcing one model to serve both roles and limiting its capacity for either role. We propose TwoTower, a block-wise autoregressive diffusion model that decouples these roles into two towers: a frozen AR context tower that causally processes clean tokens, and a trainable diffusion denoiser tower with bidirectional block attention that refines noisy blocks via cross-attention to the context. Built on Nemotron-3-Nano-30B-A3B, an open-weight 30B hybrid Mamba-Transformer MoE model, and trained on approximately 2.1T tokens, Nemotron-TwoTower retains 98.7% of the autoregressive baseline's quality while offering 2.42X higher wall-clock generation throughput. We release the code and model weights at this https URL.

---


### 46. [Humans Disengage, Reasoning Models Persist: Separating Difficulty Registration from Deliberation Allocation](https://arxiv.org/abs/2606.26502)

**<font color=#1a73e8>作者：</font>** Han-yu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) take longer on harder problems, just as humans do. This surface similarity hides an opposite pattern within items. When an LRM gets a problem wrong, it spends more tokens than when it gets the same problem right; humans do the reverse, spending less time on the trials they get wrong. We separate two levels of deliberation: how response time tracks difficulty across items (registration), and, with item identity held fixed, whether an agent spends more on its own failures or successes (allocation). On a public matched human-LRM corpus, humans and all five thinking LRMs reproduce the known cross-item alignment (registration) but diverge within items (allocation): every LRM shows a large wrong-vs-right effect (Cohen's d = 1.47-3.13 on H-ARC) while humans show the opposite sign. The comparison stays inside each agent's own scale; we never put seconds and tokens on one axis. The dissociation holds under item fixed effects, replicates across datasets, and is absent in a non-thinking baseline. We read the human pattern as engagement versus abandonment: people stay on items they expect to solve and give up on the rest. We read the LRM pattern as length driven by uncertainty: chains grow when the model is unsure, which is exactly when it tends to fail. Both policies produce the same cross-item correlation with difficulty, so they look aligned on the measure prior work has used; the divergence shows up only once item identity is fixed. Under resource-rational metareasoning, the split is between two stopping policies that share a difficulty signal but implement opposite control; trace length captures the signal and misses the control.

---


### 47. [Boundary-Aware Context Grounding for A Low-Channel EEG Agent](https://arxiv.org/abs/2606.26519)

**<font color=#1a73e8>作者：</font>** Zhiyuan Xu, Yueqing Dai, Junling Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can make scientific software easier to use. However, a general model does not automatically know which measurements a particular sensor can support, which algorithms are implemented in the current software, or which conclusions are justified by a computed result. These distinctions are especially important for low-channel electroencephalography (EEG), where sparse spatial coverage and variable signal quality make plausible but unsupported interpretations easy to produce. We present NeuraDock Agent, an open-source architecture that separates a deterministic local EEG engine from a hardware-aware language layer. The numerical engine parses recordings, performs quality control, executes reviewed spectral workflows, and writes machine-readable artifacts. The LLM receives only a compact, allowlisted summary and a versioned context pack. The context describes the seven-channel hardware, reviewed workflows, result fields, implementation boundaries, scientific limits, and reference cases. Raw EEG and dense per-sample arrays remain local
We evaluate the system at three levels. First, 12 recordings produced identical structured results over ten numerical repetitions, and a complete Rest/Task run produced identical result, report, and figure hashes over three repetitions. Second, request-capture and failure-injection experiments confirmed the tested data boundary and preservation of local artifacts under HTTP, malformed-output, and connection failures. Third, a boundary-awareness benchmark tested 36 ordinary and adversarial questions under four context ablations and two LLMs, yielding 288 this http URL results support hardware- and implementation-aware grounding as a practical mechanism for calibrating what an EEG agent accepts, qualifies, or refuses; they do not establish clinical validity or a validated absolute cognitive-load index.

---


### 48. [\textsc{DiARC}: Distinguishing Positive and Negative Samples Helps Improving ARC-like Reasoning Ability of Large Language Models](https://arxiv.org/abs/2606.26530)

**<font color=#1a73e8>作者：</font>** Yuxuan Yang, Feiyang Li, Yile Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Abstraction and Reasoning Corpus (ARC;~\citealp{chollet2019measure}) contains tasks that require summarizing patterns from limited grid samples and predicting output grids. Recently, many large language model based approaches have attempted to transform it into a text-based reasoning task. However, methods based on open-source models have generally yielded unsatisfactory results, while those relying on closed-source models are too costly. Current efforts mainly focus on data augmentation, constructing ARC-like data for more comprehensive supervised fine-tuning. In this work, we argue that solving ARC-like problems requires not only \textit{positive} sample supervision but also the ability to improve model reasoning by distinguishing \textit{negative} samples. To this end, we draw on the idea of preference alignment and propose \textsc{DiARC}, a method that constructs preference pairs to enable the model to distinguish between them. Specifically, we propose three ways to construct negative samples, including output-level visual transformations, DSL-level rule inversion, and task-specific rule editing. The resulting negative samples provide informative near-miss alternatives while keeping the observed demonstrations unchanged. Experimental results across multiple ARC-like benchmarks show that \textsc{DiARC} consistently improves performance over baseline models. The code is released at this https URL.

---


### 49. [From Hallucination to Grounding: Diagnosing Visual Spatial Intelligence via CRISP](https://arxiv.org/abs/2606.26535)

**<font color=#1a73e8>作者：</font>** Zhixing Li, Yinan Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current VLM evaluations often conflate language priors with genuine spatial reasoning. To address this, we introduce CRISP, a novel structural-diagnostic evaluation paradigm that assesses visual spatial intelligence through consistency, the alignment between implicit perception and explicit reasoning. Unlike traditional black-box QA, CRISP utilizes metric 3D Scene Graphs and an oracle intervention protocol to decouple latent reasoning capabilities from perceptual bottlenecks. This granular diagnosis uncovers a systematic perception-reasoning disconnect. Crucially, we reveal that while proprietary models possess robust latent reasoning engines, they suffer from inaccurate metric estimation and a critical failure to leverage their implicit structural representations. Conversely, open-source models remain fundamentally bottlenecked by their lack of multi-hop compositional reasoning. By shifting the focus from merely ``guessing correctly'' via language priors to genuinely ``perceiving, verifying, and reasoning,'' CRISP offers a rigorous roadmap for multimodal alignment beyond end-to-end post-training. The code and dataset are available at this https URL.

---


### 50. [Can Large Language Models Reliably Code Qualitative Humanitarian Data? A Benchmark Study Against Human Expert Adjudication](https://arxiv.org/abs/2606.26541)

**<font color=#1a73e8>作者：</font>** Jerome Marston, Tino Kreutzer, Salomé Garnier 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data from affected populations are crucial for informing humanitarian response, but their value depends on timely and consistent interpretation of nuanced accounts of need. Humanitarian organizations often lack the staff, time, and specialist expertise required to analyze this information at scale. Large language models (LLMs) may expand this capacity, but their reliability for coding qualitative humanitarian data has not been directly established. This benchmark study compares 46 LLMs to a human Gold Standard using 150 high-fidelity synthetic humanitarian transcripts. Evaluation combined inter-rater reliability testing with Krippendorff's alpha, discrepancy analysis distinguishing correct, near-correct, and incorrect codes, and qualitative assessment across humanitarian-specific criteria including discrimination, complex needs hierarchies, and non-standard communication styles. The authors find that multiple LLMs can perform deductive coding at reliability levels comparable to experienced human coders, especially when structured prompts and reasoning-enabled configurations are used. At the same time, aggregate reliability metrics alone are insufficient for deployment decisions. Models varied in recognizing needs expressed indirectly, needs outside predefined categories, and protection-relevant concerns such as physical safety and discrimination. These findings suggest that LLMs can materially expand humanitarian analytical capacity, but not as substitutes for human judgment. Appropriate use requires structured codebooks, reasoning-enabled models, attention to theme-specific performance, and tiered oversight focused on categories where miscoding would have the greatest programmatic consequences. For sensitive humanitarian data, open-weights models deployed on self-hosted infrastructure may offer a viable path for combining analytical scalability with stronger data governance.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-135](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
