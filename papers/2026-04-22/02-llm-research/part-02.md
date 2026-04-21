# 🧠 大模型相关研究 | 2026年04月22日

> 本类共 **353** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

---

### 51. [Agentic Frameworks for Reasoning Tasks: An Empirical Study](https://arxiv.org/abs/2604.16646)

**<font color=#1a73e8>作者：</font>** Zeeshan Rasheed, Abdul Malik Sami, Muhammad Waseem 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in agentic frameworks have enabled AI agents to perform complex reasoning and decision-making. However, evidence comparing their reasoning performance, efficiency, and practical suitability remains limited. To address this gap, we empirically evaluate 22 widely used agentic frameworks across three reasoning benchmarks: BBH, GSM8K, and ARC. The frameworks were selected from 1,200 GitHub repositories collected between January 2023 and July 2025 and organized into a taxonomy based on architectural design. We evaluated them under a unified setting, measuring reasoning accuracy, execution time, computational cost, and cross-benchmark consistency.
Our results show that 19 of the 22 frameworks completed all three benchmarks. Among these, 12 showed stable performance, with mean accuracy of 74.6-75.9%, execution time of 4-6 seconds per task, and cost of 0.14-0.18 cents per task. Poorer results were mainly caused by orchestration problems rather than reasoning limits. For example, Camel failed to complete BBH after 11 days because of uncontrolled context growth, while Upsonic consumed USD 1,434 in one day because repeated extraction failures triggered costly retries. AutoGen and Mastra also exhausted API quotas through iterative interactions that increased prompt length without improving results.
We also found a sharp drop in mathematical reasoning. Mean accuracy on GSM8K was 44.35%, compared with 89.80% on BBH and 89.56% on ARC. Overall, this study provides the first large-scale empirical comparison of agentic frameworks for reasoning-intensive software engineering tasks and shows that framework selection should prioritize orchestration quality, especially memory control, failure handling, and cost management.

---


### 52. [Defragmenting Language Models: An Interpretability-based Approach for Vocabulary Expansion](https://arxiv.org/abs/2604.16656)

**<font color=#1a73e8>作者：</font>** Maitrey Mehta, Nishant Subramani, Zhichao Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> All languages are equal; when it comes to tokenization, some are more equal than others. Tokens are the hidden currency that dictate the cost and latency of access to contemporary LLMs. However, many languages written in non-Latin scripts observe a poor exchange rate: LLMs take several multiples of tokens to encode the same information in many languages as they do for English. Our analysis reveals that this issue, known as 'token over-fragmentation', persists in modern open-weight LLMs. The standard remedy is vocabulary expansion that adds target language items missing from the model's vocabulary. In this work, we comprehensively study and advance interpretability-based vocabulary expansion, a new research direction. We focus on two core decisions in the vocabulary expansion process: What items should we add? and How should we initialize their corresponding input and output embeddings? First, we question the conventional use of frequency-based methods to choose candidate vocabulary items to add (a decision long treated as settled), and show that interpretability-based methods offer a superior performance-token efficiency trade-off. Next, we strengthen the case for interpretability-based embedding initialization by showing large gains (~20 pts) over baseline initialization methods for several languages written in non-Latin scripts. We identify the phenomenon of "subword detokenization" where models progressively merge fragmented subword tokens into larger subwords across layers. Grounded in our analysis of this phenomenon, we propose FragMend to further push the efficiency ceiling of interpretability-based expansion. We validate the effectiveness of FragMend through comparison against strong baselines and we present extensive analysis of its design choices.

---


### 53. [Cross-Modal Bayesian Low-Rank Adaptation for Uncertainty-Aware Multimodal Learning](https://arxiv.org/abs/2604.16657)

**<font color=#1a73e8>作者：</font>** Habibeh Naderi, Behrouz Haji Soleimani, Stan Matwin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large pre-trained language models are increasingly adapted to downstream tasks using parameter-efficient fine-tuning (PEFT), but existing PEFT methods are typically deterministic and unimodal, making them poorly suited for low-resource multimodal settings where predictive uncertainty and cross-modal reliability both matter. We introduce CALIBER (Context-Aware Low-rank Inference with Bayesian Embedding Regularization), a multimodal uncertainty-aware PEFT framework for audio-text learning. CALIBER extends Bayesian low-rank adaptation by conditioning the variational posterior in the adapter space on per-layer, token-level text-audio cross-attention. Specifically, text-derived low-rank features attend to frame-level audio embeddings to produce localized acoustic context, which then modulates the mean and variance of a compact stochastic latent matrix within the rank-$r$ adapter space. This design treats audio not only as an additional feature source, but as a contextual reliability signal that shapes both adaptation and confidence. By confining stochasticity to a low-dimensional latent component, CALIBER retains the computational efficiency and scalability of PEFT while enabling heteroscedastic multimodal uncertainty estimation. Experimental results across diverse text and audio backbones show that CALIBER consistently matches or improves upon text-only Bayesian PEFT and conventional multimodal transfer-learning baselines, with token-level cross-attention yielding the most consistent gains. Our findings demonstrate that localized cross-modal conditioning is an effective and lightweight mechanism for uncertainty-aware multimodal adaptation.

---


### 54. [CBRS: Cognitive Blood Request System with Bilingual Dataset and Dual-Layer Filtering for Multi-Platform Social Streams](https://arxiv.org/abs/2604.16665)

**<font color=#1a73e8>作者：</font>** Anik Saha, Mst. Fahmida Sultana Naznin, Zia Ul Hassan Abdullah 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Urgent blood donation seeking posts and messages on social media often go unnoticed due to the overwhelming volume of daily communications. Traditional app-based systems, reliant on manual input, struggle to reach users in low-resource settings, delaying critical responses. To address this, we introduce the Cognitive Blood Request System (CBRS), a multi-platform framework that efficiently filters and parses blood donation requests from social media streams using a cost-efficient dual-layered architecture. To do so, we curate a novel dataset of 11K parsed blood donation request messages in Bengali, English, and transliterated Bengali, capturing the linguistic diversity of real social media communications. The inclusion of adversarial negatives further enhances the robustness of our model. CBRS achieves an impressive 99% accuracy and precision in filtering, surpassing benchmark methods. In the parsing task, our LoRA finetuned Llama-3.2-3B model achieves 92% zero-shot accuracy, surpassing the base model by 41.54% and exceeding the few-shot performance of GPT-4o-mini, Gemini-2.0-Flash, and other LLMs, while resulting in a 35X reduction in input token usage. This work lays a robust foundation for scalable, inclusive information extraction in time-sensitive, object-focused tasks. Our code, dataset, and trained models are publicly available at [this https URL](this https URL).

---


### 55. [From Subsumption to Satisfiability: LLM-Assisted Active Learning for OWL Ontologies](https://arxiv.org/abs/2604.16672)

**<font color=#1a73e8>作者：</font>** Haoruo Zhao, Wenshuo Tang, Duncan Guthrie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In active learning, membership queries (MQs) allow a learner to pose questions to a teacher, such as ''Is every apple a fruit?'', to which the teacher responds correctly with yes or no. These MQs can be viewed as subsumption tests with respect to the target ontology. Inspired by the standard reduction of subsumption to satisfiability in description logics, we reformulate each candidate axiom into its corresponding counter-concept and verbalise it in controlled natural language before presenting it to Large Language Models (LLMs). We introduce LLMs as a third component that provides real-world examples approximating an instance of the counter-concept. This design property ensures that only Type II errors may occur in ontology modelling; in the worst case, these errors merely delay the construction process without introducing inconsistencies. Experimental results on 13 commercial LLMs show that recall, corresponding to Type II errors in our framework, remains stable across several well-established ontologies.

---


### 56. [Agentic Risk-Aware Set-Based Engineering Design](https://arxiv.org/abs/2604.16687)

**<font color=#1a73e8>作者：</font>** Varun Kumar, George Em Karniadakis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper introduces a multi-agent framework guided by Large Language Models (LLMs) to assist in the early stages of engineering design, a phase often characterized by vast parameter spaces and inherent uncertainty. Operating under a human-in-the-loop paradigm and demonstrated on the canonical problem of aerodynamic airfoil design, the framework employs a team of specialized agents: a Coding Assistant, a Design Agent, a Systems Engineering Agent, and an Analyst Agent - all coordinated by a human Manager. Integrated within a set-based design philosophy, the process begins with a collaborative phase where the Manager and Coding Assistant develop a suite of validated tools, after which the agents execute a structured workflow to systematically explore and prune a large set of initial design candidates. A key contribution of this work is the explicit integration of formal risk management, employing the Conditional Value-at-Risk (CVaR) as a quantitative metric to filter designs that exhibit a high probability of failing to meet performance requirements, specifically the target coefficient of lift. The framework automates labor-intensive initial exploration through a global sensitivity analysis conducted by the Analyst agent, which generates actionable heuristics to guide the other agents. The process culminates by presenting the human Manager with a curated final set of promising design candidates, augmented with high-fidelity Computational Fluid Dynamics (CFD) simulations. This approach effectively leverages AI to handle high-volume analytical tasks, thereby enhancing the decision-making capability of the human expert in selecting the final, risk-assessed design.

---


### 57. [The impact of postediting on AI generative translation in Yemeni context: Translating literary prose by ChatGPT](https://arxiv.org/abs/2604.16704)

**<font color=#1a73e8>作者：</font>** Nasim Al-wagieh, Mohammed Q. Shormani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study examines the role of artificial intelligence in translation, focusing on ChatGPT, specifically ChatGPT-4, and the extent to which human postediting is required in literary translation. A mixed-method approach was adopted, involving 30 professional translators who evaluated and postedited AI-generated translations of selected Arabic and English literary texts. The results show that although AI improves translation speed and accessibility, it remains limited in handling cultural, stylistic, and figurative aspects of language. Participants generally confirmed the necessity of human postediting, particularly in novels and drama. The findings indicate that emerging human-machine collaboration model rather than replacement of human translators. The study concludes that AI should be used as a supportive tool, while human expertise remains essential for ensuring translation quality and cultural appropriateness.

---


### 58. [Evaluating Tool-Using Language Agents: Judge Reliability, Propagation Cascades, and Runtime Mitigation in AgentProp-Bench](https://arxiv.org/abs/2604.16706)

**<font color=#1a73e8>作者：</font>** Bhaskar Gurram  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated evaluation of tool-using large language model (LLM) agents is widely assumed to be reliable, but this assumption has rarely been validated against human annotation. We introduce AgentProp-Bench, a 2,000-task benchmark with 2,300 traces across four domains, nine production LLMs, and a 100-label human-validated subset. We quantify judge reliability, characterize error propagation, and evaluate a runtime mitigation. Substring-based judging agrees with human annotation at kappa=0.049 (chance-level); a three-LLM ensemble reaches kappa=0.432 (moderate) with a conservative bias. Under validated evaluation, a parameter-level injection propagates to a wrong final answer with human-calibrated probability approximately 0.62 (range 0.46-0.73 across models). Rejection (catching bad parameters) and recovery (correcting after acceptance) are independent model capabilities (Spearman rho=0.126, p=0.747). A tuned runtime interceptor reduces hallucination on GPT-4o-mini by 23.0 percentage points under a concurrent n=600 control, but shows no significant effect on Gemini-2.0-Flash, whose aggressive parameter rejection eliminates the target failure mode. All code, data, traces, and human labels are released at this https URL.

---


### 59. [Debate as Reward: A Multi-Agent Reward System for Scientific Ideation via RL Post-Training](https://arxiv.org/abs/2604.16723)

**<font color=#1a73e8>作者：</font>** Moein Salimi, Babak Hosseini Mohtasham, Amin Aghakasiri 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated potential in automating scientific ideation, yet current approaches relying on iterative prompting or complex multi-agent architectures often suffer from hallucination or computational inefficiency. A critical bottleneck in applying Reinforcement Learning (RL) to this open-ended domain is reward hacking -- where models exploit imperfect evaluation proxies to maximize scores without producing genuine scientific innovation. To address these limitations, we propose an RL framework explicitly tailored for high-quality scientific idea generation. We propose the first multi-agent reward function designed to serve as a judge, decoupling methodological validation from implementation details while providing strict binary rewards that are robust to reward hacking. To effectively optimize against this sparse signal, we utilize an unbiased variant of Group Relative Policy Optimization to mitigate artificial length bias. We grounded our training in ICLR-320, a curated dataset of problem-solution pairs extracted from ICLR 2024 proceedings. Experiments demonstrate that our framework significantly outperforms state-of-the-art baselines across expert-evaluated metrics of novelty, feasibility, and effectiveness.

---


### 60. [iDocV2: Leveraging Self-Supervision and Open-Set Detection for Improving Pattern Spotting in Historical Documents](https://arxiv.org/abs/2604.16726)

**<font color=#1a73e8>作者：</font>** Jose M. Saavedra, Crhistopher Stears, Marcelo Pizarro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Considering the imminent massification of digital books, it has become critical to facilitate searching collections through graphical patterns. Current strategies for document retrieval and pattern spotting in historical documents still need to be improved. State-of-the-art strategies achieve an overall precision of $0.494$ for pattern spotting, where the precision for small non-square queries reaches 0.427. In addition, the processing time is excessive, requiring up to 7 seconds for searching in the DocExplore dataset due to a dense-based strategy used by SOTA models. Therefore, we propose a new model based on a better encoder (iDoc), trained under a self-supervised strategy, and an open-set detector to accelerate searching. Our model achieves competitive results with state-of-the-art pattern spotting and document retrieval, improving speed by 10x. Furthermore, our model reaches a new SOTA performance on the small non-square queries, achieving a new precision of this http URL from the previous version, this leverages non-maximum suppression to reduce false positives.

---


### 61. [Agentic Large Language Models for Training-Free Neuro-Radiological Image Analysis](https://arxiv.org/abs/2604.16729)

**<font color=#1a73e8>作者：</font>** Ayhan Can Erdur, Daniel Scholz, Jiazhen Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State-of-the-art large language models (LLMs) show high performance in general visual question answering. However, a fundamental limitation remains: current architectures lack the native 3D spatial reasoning required for direct analysis of volumetric medical imaging, such as CT or MRI. Emerging agentic AI offers a new solution, eliminating the need for intrinsic 3D processing by enabling LLMs to orchestrate and leverage specialized external tools. Yet, the feasibility of such agentic frameworks in complex, multi-step radiological workflows remains underexplored. In this work, we present a training-free agentic pipeline for automated brain MRI analysis. Validating our methodology on several LLMs (GPT-5.1, Gemini 3 Pro, Claude Sonnet 4.5) with off-the-shelf domain-specific tools, our system autonomously executes complex end-to-end workflows, including preprocessing (skull stripping, registration), pathology segmentation (glioma, meningioma, metastases), and volumetric analysis. We evaluate our framework across increasingly complex radiological tasks, from single-scan segmentation and volumetric reporting to longitudinal response assessment requiring multi-timepoint comparisons. We analyze the impact of architectural design by comparing single-agent models against multi-agent "domain-expert" collaborations. Finally, to support rigorous evaluation of future agentic systems, we introduce and release a benchmark dataset of image-prompt-answer tuples derived from public BraTS data. Our results demonstrate that agentic AI can solve highly neuro-radiological image analysis tasks through tool use without the need for training or fine-tuning.

---


### 62. [Reducing Peak Memory Usage for Modern Multimodal Large Language Model Pipelines](https://arxiv.org/abs/2604.16734)

**<font color=#1a73e8>作者：</font>** Junwan Kim, Hyunkyung Bae  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have recently demonstrated strong capabilities in understanding and generating responses from diverse visual inputs, including high-resolution images and long video sequences. As these models scale to richer visual representations, inference increasingly relies on storing large numbers of vision tokens in the key-value (KV) cache, making memory consumption a central bottleneck. Existing methods address this issue by identifying redundancy in vision tokens and compressing the cache, but such compression is typically applied only after all inputs are processed, resulting in high peak memory usage during the prefill stage. In this work, we show that MLLMs exhibit inherent structural regularities and representational redundancy that can be exploited to control memory growth throughout inference. Based on this insight, we propose a sequential input-compression mechanism that enforces a fixed memory budget by performing structure-aware key-value cache compression during the prefill process. This approach substantially reduces peak memory usage while maintaining generative performance with only minimal degradation, enabling more practical and memory-efficient multimodal inference.

---


### 63. [When Agents Go Quiet: Output Generation Capacity and Format-Cost Separation for LLM Document Synthesis](https://arxiv.org/abs/2604.16736)

**<font color=#1a73e8>作者：</font>** Justice Owusu Agyemang, Michael Agyare, Miriam Kobbinah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-powered coding agents suffer from a poorly understood failure mode we term output stalling: the agent silently produces empty responses when attempting to generate large, format-heavy documents. We present a theoretical framework that explains and prevents this failure through three contributions. (1) We introduce Output Generation Capacity (OGC), a formal measure of an agent's effective ability to produce output given its current context state - distinct from and empirically smaller than the raw context window. (2) We prove a Format-Cost Separation Theorem showing that deferred template rendering is always at least as token-efficient as direct generation for any format with overhead multiplier $\mu_f > 1$, and derive tight bounds on the savings. (3) We formalize Adaptive Strategy Selection, a decision framework that maps the ratio of estimated output cost to available OGC into an optimal generation strategy (direct, chunked, or deferred). We validate the theory through controlled experiments across three models (Claude 3.5 Sonnet, GPT-4o, Llama 3.1 70B), four document types, and an ablation study isolating each component's contribution. Deferred rendering reduces LLM generation tokens by 48-72% across all conditions and eliminates output stalling entirely. We instantiate the framework as GEN-PILOT, an open-source MCP server, demonstrating that the theory translates directly into a practical tool.

---


### 64. [TriTS: Time Series Forecasting from a Multimodal Perspective](https://arxiv.org/abs/2604.16748)

**<font color=#1a73e8>作者：</font>** Xiang Ao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Time series forecasting plays a pivotal role in critical sectors such as finance, energy, transportation, and meteorology. However, Long-term Time Series Forecasting (LTSF) remains a significant challenge because real-world signals contain highly entangled temporal dynamics that are difficult to fully capture from a purely 1D perspective. To break this representation bottleneck, we propose TriTS, a novel cross-modal disentanglement framework that projects 1D time series into orthogonal time, frequency, and 2D-vision this http URL seamlessly bridge the 1D-to-2D modality gap without the prohibitive $O(N^2)$ computational overhead of Vision Transformers (ViTs), we introduce a Period-Aware Reshaping strategy and incorporate Visual Mamba (Vim). This approach efficiently models cross-period dependencies as global visual textures while maintaining linear computational complexity. Complementing this, we design a Multi-Resolution Wavelet Mixing (MR-WM) module for the frequency modality, which explicitly decouples non-stationary signals into trend and noise components to achieve fine-grained time-frequency localization. Finally, a streaming linear branch is retained in the time domain to anchor numerical stability. By dynamically fusing these three complementary representations, TriTS effectively adapts to diverse data contexts. Extensive experiments across multiple benchmark datasets demonstrate that TriTS achieves state-of-the-art (SOTA) performance, fundamentally outperforming existing vision-based forecasters by drastically reducing both parameter count and inference latency.

---


### 65. [Don't Start What You Can't Finish: A Counterfactual Audit of Support-State Triage in LLM Agents](https://arxiv.org/abs/2604.16752)

**<font color=#1a73e8>作者：</font>** Eren Unlu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current agent evaluations largely reward execution on fully specified tasks, while recent work studies clarification [11, 22, 2], capability awareness [9, 1], abstention [8, 14], and search termination [20, 5] mostly in isolation. This leaves open whether agents can diagnose why a task is blocked before acting. We introduce the Support-State Triage Audit (SSTA-32), a matched-item diagnostic framework in which minimal counterfactual edits flip the same base request across four support states: Complete (ANSWER), Clarifiable (CLARIFY), Support-Blocked (REQUEST SUPPORT), and Unsupported-Now (ABSTAIN). We evaluate a frontier model under four prompting conditions - Direct, Action-Only, Confidence-Only, and a typed Preflight Support Check (PSC) - using Dual-Persona Auto-Auditing (DPAA) with deterministic heuristic scoring. Default execution overcommits heavily on non-complete tasks (41.7% overcommitment rate). Scalar confidence mapping avoids overcommitment but collapses the three-way deferral space (58.3% typed deferral accuracy). Conversely, both Action-Only and PSC achieve 91.7% typed deferral accuracy by surfacing the categorical ontology in the prompt. Targeted ablations confirm that removing the support-sufficiency dimension selectively degrades REQUEST SUPPORT accuracy, while removing the evidence-sufficiency dimension triggers systematic overcommitment on unsupported items. Because DPAA operates within a single context window, these results represent upper-bound capability estimates; nonetheless, the structural findings indicate that frontier models possess strong latent triage capabilities that require explicit categorical decision paths to activate safely.

---


### 66. [Know When to Trust the Skill: Delayed Appraisal and Epistemic Vigilance for Single-Agent LLMs](https://arxiv.org/abs/2604.16753)

**<font color=#1a73e8>作者：</font>** Eren Unlu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) transition into autonomous agents integrated with extensive tool ecosystems, traditional routing heuristics increasingly succumb to context pollution and "overthinking". We argue that the bottleneck is not a deficit in algorithmic capability or skill diversity, but the absence of disciplined second-order metacognitive governance. In this paper, our scientific contribution focuses on the computational translation of human cognitive control - specifically, delayed appraisal, epistemic vigilance, and region-of-proximal offloading - into a single-agent architecture. We introduce MESA-S (Metacognitive Skills for Agents, Single-agent), a preliminary framework that shifts scalar confidence estimation into a vector separating self-confidence (parametric certainty) from source-confidence (trust in retrieved external procedures). By formalizing a delayed procedural probe mechanism and introducing Metacognitive Skill Cards, MESA-S decouples the awareness of a skill's utility from its token-intensive execution. Evaluated under an In-Context Static Benchmark Evaluation natively executed via Gemini 3.1 Pro, our early results suggest that explicitly programming trust provenance and delayed escalation mitigates supply-chain vulnerabilities, prunes unnecessary reasoning loops, and prevents offloading-induced confidence inflation. This architecture offers a scientifically cautious, behaviorally anchored step toward reliable, epistemically vigilant single-agent orchestration.

---


### 67. [Machine individuality: Separating genuine idiosyncrasy from response bias in large language models](https://arxiv.org/abs/2604.16755)

**<font color=#1a73e8>作者：</font>** Valentin Kriegmair, Dirk U. Wulff  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly integrated into daily life, in roles ranging from high-stakes decision support to companionship, understanding their behavioral dispositions becomes critical. A growing literature uses psychometric inventories and cognitive paradigms to profile LLM dispositions. However, these approaches cannot determine whether behavioral differences reflect stable, stimulus-specific individuality or global response biases and stochastic noise. Here, we apply crossed random-effects models -- widely used in psychometrics to separate systematic effects -- to 74.9 million ratings provided by 10 open-weight LLMs for over 100,000 words across 14 psycholinguistic norms. On average, 16.9% of variance is attributable to stimulus-specific individuality, robustly exceeding a statistical null model. Cross-norm prediction analyses reveal this individuality as a coherent fingerprint, unique to each model. These results identify individual differences among LLMs that cannot be attributed to response biases or stochastic noise. We term these differences machine individuality.

---


### 68. [Expressing Social Emotions: Misalignment Between LLMs and Human Cultural Emotion Norms](https://arxiv.org/abs/2604.16757)

**<font color=#1a73e8>作者：</font>** Sree Bhattacharyya, Manas Mehta, Leona Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The expression of emotions that serve social purposes, such as asserting independence or fostering interdependence, is central to human interactions and varies systematically across cultures. As LLMs are increasingly used to simulate human behavior in culturally nuanced interactions, it is important to understand whether they faithfully capture human patterns of social emotion expression. When LLM responses are not culturally aligned, their utility is compromised -- particularly when users assume they are interacting with a culturally attuned interlocutor, and may act on advice that proves inappropriate in their cultural context. We present a psychologically informed evaluation framework of cross-cultural social emotion expression in LLMs. Using a human study comparing European American and Latin American participants' expression of engaging and disengaging emotions, we evaluate six frontier LLMs on their ability to reflect culturally differentiated patterns for expressing social emotions. We find systematic misalignment between model and human behavior: all models express engaging emotions more than disengaging ones, with particularly stark differences observed for the generally well-represented European American persona. We further highlight that LLM responses are highly concentrated and deterministic, failing to capture the diversity of human responses in expressing social emotions. Our ablation analyses reveal that these patterns are robust to sampling temperatures, partially sensitive to prompt language, and dependent on the response elicitation format. Together, our findings highlight limitations in how current LLMs represent the interaction of cultural and emotional axes, particularly when expressing social emotions, with direct implications for their deployment in cross-cultural affective contexts.

---


### 69. [LLM-Extracted Covariates for Clinical Causal Inference: Rethinking Integration Strategies](https://arxiv.org/abs/2604.16763)

**<font color=#1a73e8>作者：</font>** Lei Liu, Jialin Chen, Kathy Macropol  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal inference from electronic health records (EHR) is fundamentally limited by unmeasured confounding: critical clinical states such as frailty, goals of care, and mental status are documented in free-text notes but absent from structured data. Large language models can extract these latent confounders as interpretable, structured covariates, yet how to effectively integrate them into causal estimation pipelines has not been systematically studied. Using the MIMIC-IV database with 21,859 sepsis patients, we compare seven covariate-integration strategies for estimating the effect of early vasopressor initiation on 28-day mortality, spanning tabular-only baselines, traditional NLP representations, and three LLM-augmented approaches. A central finding is that not all integration strategies are equally effective: directly augmenting the propensity score model with LLM covariates achieves the best performance, while dual-caliper matching on text-derived categorical distances restricts the donor pool and degrades estimation. In semi-synthetic experiments with known ground-truth effects, LLM-augmented propensity scores reduce estimation bias from 0.0143 to 0.0003 relative to tabular-only methods, and this advantage persists under substantial simulated extraction error. On real data, incorporating LLM-extracted covariates reduces the estimated treatment effect from 0.055 to 0.027, directionally consistent with the CLOVERS randomized trial, and a doubly robust estimator yielding 0.019 confirms the robustness of this finding. Our results offer practical guidance on when and how text-derived covariates improve causal estimation in critical care.

---


### 70. [StageMem: Lifecycle-Managed Memory for Language Models](https://arxiv.org/abs/2604.16774)

**<font color=#1a73e8>作者：</font>** Jiarui Han  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon language model systems increasingly rely on persistent memory, yet many current designs still treat memory primarily as a static store: write an item, place it into memory, and retrieve it later if needed. We argue that this framing does not adequately capture the practical memory-control problem in deployed LLM systems. In realistic settings, the difficulty is often not merely forgetting useful information, but retaining too many uncertain items, forgetting important content in the wrong order, and giving users little trust in what will persist over time. We propose StageMem, a lifecycle-managed memory framework that treats memory as a stateful process rather than a passive repository. StageMem organizes memory into three stages -- transient, working, and durable memory -- and models each item with explicit confidence and strength. This separates shallow admission from long-term commitment: information may first be written at low cost and only later be promoted, retained, updated, or evicted as evidence and pressure evolve. Under controlled pressure regimes, this decomposition helps preserve late-important content while keeping memory burden and deeper-tier pollution more controlled. Adapted external tasks provide boundary evidence that the same schema remains compatible with stronger retrieval structure outside pure synthetic control. We present StageMem as a principled decomposition of the memory-control problem for language model systems.

---


### 71. [Bridging Coarse and Fine Recognition: A Hybrid Approach for Open-Ended Multi-Granularity Object Recognition in Interactive Educational Games](https://arxiv.org/abs/2604.16785)

**<font color=#1a73e8>作者：</font>** Hanling Yi, Feng Lin, Mao Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Multimodal Large Language Models (MLLMs) have enabled open-ended object recognition, yet they struggle with fine-grained tasks. In contrast, CLIP-style models excel at fine-grained recognition but lack broad coverage of general object categories. To bridge this gap, we propose \textbf{HyMOR}, a \textbf{Hy}brid \textbf{M}ulti-granularity open-ended \textbf{O}bject \textbf{R}ecognition framework that integrates an MLLM with a CLIP model. In HyMOR, the MLLM performs open-ended and coarse-grained object recognition, while the CLIP model specializes in fine-grained identification of domain-specific objects such as animals and plants. This hybrid design enables accurate object understanding across multiple semantic granularities, serving as a robust perceptual foundation for downstream multi-modal content generation and interactive gameplay. To support evaluation in content-rich and educational scenarios, we introduce TBO (TextBook Objects), a dataset containing 20,942 images annotated with 8,816 object categories extracted from textbooks. Extensive experiments demonstrate that HyMOR narrows the fine-grained recognition gap with CLIP to 0.2\% while improving general object recognition by 2.5\% over a baseline MLLM, measured by average Sentence-BERT (SBert) similarity. Overall, HyMOR achieves a 23.2\% improvement in average SBert across all evaluated datasets, highlighting its effectiveness in enabling accurate perception for multi-modal game content generation and interactive learning applications.

---


### 72. [AutoOR: Scalably Post-training LLMs to Autoformalize Operations Research Problems](https://arxiv.org/abs/2604.16804)

**<font color=#1a73e8>作者：</font>** Sumeet Ramesh Motwani, Chuan Du, Aleksander Petrov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimization problems are central to decision-making in manufacturing, logistics, scheduling, and other industrial settings. Translating complicated descriptions of these problems into solver-ready formulations requires specialized operations research (OR) expertise, making it hard to scale. We present AutoOR, a scalable synthetic data generation and reinforcement learning pipeline that trains LLMs to autoformalize optimization problems specified in natural language across linear, mixed-integer, and non-linear categories. AutoOR generates verified training data from standard optimization forms and uses solver execution feedback as the reward signal for RL post-training. AutoOR applied to an 8B model achieves state-of-the-art or competitive results across six established OR benchmarks, matching significantly larger frontier models. For a non-linear problem class involving physical dynamics, where frontier models score near 0%, we introduce a curriculum RL strategy that bootstraps from limited initial training data to make this class tractable for post-training. We believe that methods such as AutoOR can significantly accelerate industrial decision-making with AI.

---


### 73. [Introspection Adapters: Training LLMs to Report Their Learned Behaviors](https://arxiv.org/abs/2604.16812)

**<font color=#1a73e8>作者：</font>** Keshav Shenoy, Li Yang, Abhay Sheshadri 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When model developers or users fine-tune an LLM, this can induce behaviors that are unexpected, deliberately harmful, or hard to detect. It would be far easier to audit LLMs if they could simply describe their behaviors in natural language. Here, we study a scalable approach to rapidly identify learned behaviors of many LLMs derived from a shared base LLM. Given a model $M$, our method works by finetuning models $M_i$ from $M$ with implanted behaviors $b_i$; the $(M_i, b_i)$ pairs serve as labeled training data. We then train an \emph{introspection adapter} (IA): a single LoRA adapter jointly trained across the finetunes $M_i$ to cause them to verbalize their implanted behaviors. We find that this IA induces self-description of learned behaviors even in finetunes of $M$ that were trained in very different ways from the $M_i$. For example, IAs generalize to AuditBench, achieving state-of-the-art at identifying explicitly hidden concerning behaviors. IAs can also be used to detect encrypted finetuning API attacks. They scale favorably with model size and training data diversity. Overall, our results suggest that IAs are a scalable, effective, and practically useful approach to auditing fine-tuned LLMs.

---


### 74. [HeLa-Mem: Hebbian Learning and Associative Memory for LLM Agents](https://arxiv.org/abs/2604.16839)

**<font color=#1a73e8>作者：</font>** Jinchang Zhu, Jindong Li, Cheng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory is a critical challenge for Large Language Model agents, as fixed context windows cannot preserve coherence across extended interactions. Existing memory systems represent conversation history as unstructured embedding vectors, retrieving information through semantic similarity. This paradigm fails to capture the associative structure of human memory, wherein related experiences progressively strengthen interconnections through repeated co-activation. Inspired by cognitive neuroscience, we identify three mechanisms central to biological memory: association, consolidation, and spreading activation, which remain largely absent in current research.
To bridge this gap, we propose HeLa-Mem, a bio-inspired memory architecture that models memory as a dynamic graph with Hebbian learning dynamics. HeLa-Mem employs a dual-level organization: (1) an episodic memory graph that evolves through co-activation patterns, and (2) a semantic memory store populated via Hebbian Distillation, wherein a Reflective Agent identifies densely connected memory hubs and distills them into structured, reusable semantic knowledge. This dual-path design leverages both semantic similarity and learned associations, mirroring the episodic-semantic distinction in human cognition. Experiments on LoCoMo demonstrate superior performance across four question categories while using significantly fewer context tokens. Code is available on GitHub: this https URL

---


### 75. [When Earth Foundation Models Meet Diffusion: An Application to Land Surface Temperature Super-Resolution](https://arxiv.org/abs/2604.16841)

**<font color=#1a73e8>作者：</font>** Yiheng Chen, Zihui Ma, Peishi Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Land surface temperature (LST) super-resolution is important for environmental monitoring. However, it remains challenging as coarse thermal observations severely underdetermine fine-scale structure. In this paper, we propose Earth Foundation Model-guided Diffusion (EFDiff), a novel framework for super-resolution under extreme spatial degradation. EFDiff uses the Prithvi-EO-2.0 Earth foundation model to encode high-resolution multispectral reflectance into geospatial embeddings, which are injected into the denoising network via cross-attention to guide fine-scale reconstruction from highly degraded observations. We study two variants, EFDiff-$\epsilon$ and EFDiff-$x_0$, which offer complementary trade-offs between perceptual realism and pixel-level fidelity. We evaluate EFDiff under an extreme $32\times$ scale gap using a globally diverse benchmark comprising 242,416 co-registered Landsat thermal-reflectance patches. Results show that EFDiff consistently outperforms baseline methods and that cross-attention conditioning by EFM is more effective than HLS channel concatenation. Although we present EFDiff in the context of LST super-resolution, the framework is broadly applicable to remote sensing problems in which pretrained geospatial representations can guide generative reconstruction.

---


### 76. [DART: Mitigating Harm Drift in Difference-Aware LLMs via Distill-Audit-Repair Training](https://arxiv.org/abs/2604.16845)

**<font color=#1a73e8>作者：</font>** Ziwen Pan, Zihan Liang, Jad Kabbara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) tuned for safety often avoid acknowledging demographic differences, even when such acknowledgment is factually correct (e.g., ancestry-based disease incidence) or contextually justified (e.g., religious hiring preferences). This identity-blindness yields incorrect responses, unnecessary refusals, or generic "equal-treatment" defaults. We study this via difference-awareness classification: given a question involving demographic groups, the task is not to answer directly, but to classify whether a correct answer requires recognizing group differences (yes) or whether groups should be treated identically (no). Crucially, fine-tuning for accuracy triggers harm drift: model-generated explanations become increasingly harmful as decision accuracy improves, whether by elaborating harmful content, introducing problematic assumptions, or failing to flag harms the baseline identified. To mitigate this, we introduce DART (Distill--Audit--Repair Training), which distills label-conditioned reasoning from a teacher, audits outputs for harm drift cases relative to baseline, and repairs problematic cases via severity-weighted fine-tuning. On eight benchmarks, DART improves Llama-3-8B-Instruct accuracy from 39.0% to 68.8%, with largest gains on equal-treatment prompts (11.3% -> 72.6%), while reducing harm drift cases by 72.6%. It also transfers to 280 open-ended real-world queries across medical, legal, policy, and educational domains, improving difference-appropriate responses from 39.8% to 77.5% while reducing refusals from 34.3% to 3.0%. Our results demonstrate that accuracy and safety need not conflict when explicit detection and repair mechanisms are in place.

---


### 77. [Learning to Trade Like an Expert: Cognitive Fine-Tuning for Stable Financial Reasoning in Language Models](https://arxiv.org/abs/2604.16862)

**<font color=#1a73e8>作者：</font>** Yuchen Pan, Soung Chang Liew  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent deployments of large language models (LLMs) as autonomous trading agents raise questions about whether financial decision-making competence generalizes beyond specific market patterns and how it should be trained and evaluated in noisy markets lacking ground truth. We propose a structured framework for training and evaluating such models. Central to our approach is a curated, multiple-choice question (MCQ) dataset derived from classic textbooks and historical markets, verified by an AI committee, enriched with structured reasoning traces, and augmented to reduce shortcut learning. To evaluate whether performance on isolated MCQs generalizes to real-world trading, we introduce a two-stage protocol combining test-set evaluation with an MCQ-based chronological trading simulation. Extensive evaluations across market regimes provide statistically robust evidence that open models trained with our framework exhibit competitive, risk-aware behavior over time, outperform open-source baselines, and approach frontier-model performance at smaller scale. We release the dataset and evaluation framework to support further research.

---


### 78. [GRAIL: Autonomous Concept Grounding for Neuro-Symbolic Reinforcement Learning](https://arxiv.org/abs/2604.16871)

**<font color=#1a73e8>作者：</font>** Hikaru Shindo, Henri Rößler, Quentin Delfosse 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neuro-symbolic Reinforcement Learning (NeSy-RL) combines symbolic reasoning with gradient-based optimization to achieve interpretable and generalizable policies. Relational concepts, such as "left of" or "close by", serve as foundational building blocks that structure how agents perceive and act. However, conventional approaches require human experts to manually define these concepts, limiting adaptability since concept semantics vary across environments. We propose GRAIL (Grounding Relational Agents through Interactive Learning), a framework that autonomously grounds relational concepts through environmental interaction. GRAIL leverages large language models (LLMs) to provide generic concept representations as weak supervision, then refines them to capture environment-specific semantics. This approach addresses both sparse reward signals and concept misalignment prevalent in underdetermined environments. Experiments on the Atari games Kangaroo, Seaquest, and Skiing demonstrate that GRAIL matches or outperforms agents with manually crafted concepts in simplified settings, and reveals informative trade-offs between reward maximization and high-level goal completion in the full environment.

---


### 79. [Adaptive Forensic Feature Refinement via Intrinsic Importance Perception](https://arxiv.org/abs/2604.16879)

**<font color=#1a73e8>作者：</font>** Jiazhen Yang, Junjun Zheng, Kejia Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid development of generative models and multimodal content editing technologies, the key challenge faced by synthetic image detection (SID) lies in cross-distribution generalization to unknown generation sources. In recent years, visual foundation models (VFM), which acquire rich visual priors through large scale image-text alignment pretraining, have become a promising technical route for improving the generalization ability of SID. However, existing VFM-based methods remain relatively coarse-grained in their adaptation strategies. They typically either directly use the final layer representations of VFM or simply fuse multi layer features, lacking explicit modeling of the optimal representational hierarchy for transferable forgery cues. Meanwhile, although directly fine-tuning VFM can enhance task adaptation, it may also damage the cross-modal pretrained structure that supports open-set generalization. To address this task specific tension, we reformulate VFM adaptation for SID as a joint optimization problem: it is necessary both to identify the critical representational layer that is more suitable for carrying forgery discriminative information and to constrain the disturbance caused by task knowledge injection to the pretrained structure. Based on this, we propose I2P, an SID framework centered on intrinsic importance perception. I2P first adaptively identifies the critical layer representations that are most discriminative for SID, and then constrains task-driven parameter updates within a low sensitivity parameter subspace, thereby improving task specificity while preserving the transferable structure of pretrained representations as much as possible.

---


### 80. [Incentivizing Parametric Knowledge via Reinforcement Learning with Verifiable Rewards for Cross-Cultural Entity Translation](https://arxiv.org/abs/2604.16881)

**<font color=#1a73e8>作者：</font>** Jiang Zhou, Xiaohu Zhao, Xinwei Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-cultural entity translation remains challenging for large language models (LLMs) as literal or phonetic renderings are usually yielded instead of culturally appropriate translations in context. However, relevant knowledge may already be encoded in model parameters during large-scale pre-training. To incentivize the effective use of parametric knowledge, we propose EA-RLVR (Entity-Anchored Reinforcement Learning with Verifiable Rewards), a training framework that optimizes cross-cultural entity translation without relying on external knowledge bases. EA-RLVR anchors supervision on a verifiable, entity-level reward signal and incorporates lightweight structural gates to stabilize optimization. This design steers the model toward learning a robust reasoning process rather than merely imitating reference translations. We evaluate EA-RLVR on XC-Translate and observe consistent improvements in both entity translation accuracy and out-of-domain generalization. Specifically, training on merely 7k samples boosts Qwen3-14B's entity translation accuracy from 23.66\% to 31.87\% on a 50k test set comprising entirely unseen entities. The learned entity translation ability also transfers to general translation, yielding +1.35 XCOMET on WMT24++, which scales to +1.59 with extended optimization. Extensive analyses of $pass@k$ dynamics and reward formulations attribute these gains to superior sampling efficiency and a stable optimization landscape.

---


### 81. [SinkRouter: Sink-Aware Routing for Efficient Long-Context Decoding in Large Language and Multimodal Models](https://arxiv.org/abs/2604.16883)

**<font color=#1a73e8>作者：</font>** Junnan Liu, Xinyan Liu, Peifeng Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In long-context decoding for LLMs and LMMs, attention becomes increasingly memory-bound because each decoding step must load a large amount of KV-cache data from GPU memory. Existing acceleration strategies often trade efficiency for accuracy by relying on heuristic pruning that may discard useful information. At a deeper level, they also tend to indiscriminately preserve all high-scoring tokens, treat early tokens as indispensable anchors, or rely on heuristic head routing, reflecting an insufficient mechanistic understanding of the attention sink phenomenon. In this paper, we show that the attention sink phenomenon corresponds to a stable, reachable, and error-controllable fixed point constructed during training. Based on this insight, we propose SinkRouter, a training-free selective routing framework that detects the sink signal and skips computations that would otherwise produce near-zero output. To translate this mechanism into real-world acceleration, we develop a hardware-aware Triton kernel with block-level branching and Split-K parallelism. We conduct extensive evaluations on a diverse suite of long-context benchmarks, including LongBench, InfiniteBench, CVBench, MileBench, and MMVP, using both text-only and multimodal backbones such as Llama-3.1-8B, Llama-3.1-70B, Yi-9B-200K, LLaVA-1.5-7B, and LLaVA-1.5-13B. Across these settings, SinkRouter consistently improves decoding efficiency while maintaining competitive accuracy, and reaches 2.03x speedup with a 512K context.

---


### 82. [Bias-constrained multimodal intelligence for equitable and reliable clinical AI](https://arxiv.org/abs/2604.16884)

**<font color=#1a73e8>作者：</font>** Cheng Li, Weijian Huang, Jiarun Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The integration of medical imaging and clinical text has enabled the emergence of generalist artificial intelligence (AI) systems for healthcare. However, pervasive biases, such as imbalanced disease prevalence, skewed anatomical region distributions, heterogeneous imaging protocols, and demographic disparities, pose significant challenges to the fairness and reliability of vision-language systems in real-world clinical settings. Here we present BiasCareVL, a bias-aware multimodal learning framework that introduces bias control directly into model design, rather than treating it as a post hoc correction. BiasCareVL incorporates adaptive uncertainty modeling with optional human-in-the-loop refinement to regulate the influence of dominant data patterns and to promote equitable reasoning under distributional imbalance. Trained on 3.44 million samples spanning over 15 imaging modalities, the framework supports diverse clinical tasks, including visual question answering, disease classification, segmentation, and report generation within a unified representation space. Across eight public benchmarks covering dermatology, oncology, radiology, and pathology, BiasCareVL consistently outperforms 20 state-of-the-art methods, with pronounced gains in clinically challenging scenarios, including over 10% accuracy improvement in multi-class skin lesion diagnosis and more than 20% Dice improvement in small tumor segmentation. Furthermore, BiasCareVL achieves diagnostic performance exceeding human accuracy with substantially reduced time requirements when evaluated with board-certified radiologists. By open-sourcing BiasCareVL, we aim to promote a transparent, reproducible, and equitable future for AI in healthcare, paving the way for general-purpose, trustworthy, and clinically reliable AI systems.

---


### 83. [EasyVideoR1: Easier RL for Video Understanding](https://arxiv.org/abs/2604.16893)

**<font color=#1a73e8>作者：</font>** Chuanyu Qin, Chenxu Yang, Qingyi Si 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from verifiable rewards (RLVR) has demonstrated remarkable effectiveness in improving the reasoning capabilities of large language models. As models evolve into natively multimodal architectures, extending RLVR to video understanding becomes increasingly important yet remains largely unexplored, due to the diversity of video task types, the computational overhead of repeatedly decoding and preprocessing high-dimensional visual inputs, and the difficulty of reproducible evaluation across numerous sensitive hyperparameters. Existing open-source RL training frameworks provide solid infrastructure for text and image scenarios but lack systematic optimizations tailored for video modality. In this work, we present \textbf{EasyVideoR1}, a complete and efficient reinforcement learning framework specifically designed for training large vision-language models on video understanding tasks. EasyVideoR1 makes the following contributions: (1) a full video RL training pipeline with offline preprocessing and tensor caching that eliminates redundant video decoding and yields a 1.47 $\times$ throughput improvement; (2) a comprehensive, task-aware reward system covering 11 distinct video and image problem types with unified routing and modular extension; (3) a mixed offline-online data training paradigm that combines curated high-quality trajectories with on-policy exploration, benefiting the learning of more challenging tasks; (4) joint image-video training with independently configurable pixel budgets, allowing the two modalities to mutually reinforce each other; and (5) an asynchronous multi-benchmark evaluation framework covering 22 mainstream video understanding benchmarks, with reproduced accuracy closely aligned with officially reported scores.

---


### 84. [Beyond Text-Dominance: Understanding Modality Preference of Omni-modal Large Language Models](https://arxiv.org/abs/2604.16902)

**<font color=#1a73e8>作者：</font>** Xinru Yan, Boxi Cao, Yaojie Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Native Omni-modal Large Language Models (OLLMs) have shifted from pipeline architectures to unified representation spaces. However, this native integration gives rise to a critical yet underexplored phenomenon: modality preference. To bridge this gap, we first systematically quantify modality preference of OLLMs using a newly-curated conflict-based benchmark and the modality selection rate metric. Our evaluation of ten representative OLLMs reveals a notable paradigm shift: unlike the ``text-dominance'' of traditional VLMs, most OLLMs exhibit a pronounced visual preference. To further understand the underlying mechanism, we conduct layer-wise probing and demonstrate that such modality preference is not static but emerges progressively in the mid-to-late layers. Building upon these insights, we leverage these internal signals to diagnose cross-modal hallucinations, achieving competitive performance across three downstream multi-modal benchmarks without task-specific data. Our work provides both a mechanistic understanding and a practical tool for building more trustworthy OLLMs. Our code and related resources are publicly available at: this https URL

---


### 85. [PRISM: Probing Reasoning, Instruction, and Source Memory in LLM Hallucinations](https://arxiv.org/abs/2604.16909)

**<font color=#1a73e8>作者：</font>** Yuhe Wu, Guangyu Wang, Yuran Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) evolve from conversational assistants into agents capable of handling complex tasks, they are increasingly deployed in high-risk domains. However, existing benchmarks largely rely on mixed queries and posterior evaluation, output-level scoring, which quantifies hallucination severity but offers limited insight into where and why hallucinations arise in the generation pipeline. We therefore reformulate hallucination evaluation as a diagnostic problem and propose PRISM, a controlled benchmark that disentangles hallucinations into four dimensions: knowledge missing, knowledge errors, reasoning errors, and instruction-following errors, grounded in three stages of generation (memory, instruction, and reasoning). PRISM contains 9,448 instances across 65 tasks and supports fine-grained, stage-aware diagnostic evaluation. Evaluating 24 mainstream open-source and proprietary LLMs, we uncover consistent trade-offs across instruction following, memory retrieval, and logical reasoning, showing that mitigation strategies often improve specific dimensions at the expense of others. We hope PRISM provides a framework for understanding the specific mechanisms behind LLMs hallucinations, ultimately accelerating the development of trustworthy large language models.

---


### 86. [Unified Ultrasound Intelligence Toward an End-to-End Agentic System](https://arxiv.org/abs/2604.16914)

**<font color=#1a73e8>作者：</font>** Chen Ma, Yunshu Li, Junhu Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical ultrasound analysis demands models that generalize across heterogeneous organs, views, and devices, while supporting interpretable workflow-level analysis. Existing methods often rely on task-wise adaptation, and joint learning may be unstable due to cross-task interference, making it hard to deliver workflow-level outputs in practice. To address these challenges, we present USTri, a tri-stage ultrasound intelligence pipeline for unified multi-organ, multi-task analysis. Stage I trains a universal generalist USGen on different domains to learn broad, transferable priors that are robust to device and protocol variability. To better handle domain shifts and reach task-aligned performance while preserving ultrasound shared knowledge, Stage II builds USpec by keeping USGen frozen and finetuning dataset-specific heads. Stage III introduces USAgent, which mimics clinician workflows by orchestrating USpec specialists for multi-step inference and deterministic structured reports. On the FMC\_UIA validation set, our model achieves the best overall performance across 4 task types and 27 datasets, outperforming state-of-the-art methods. Moreover, qualitative results show that USAgent produces clinically structured reports with high accuracy and interpretability. Our study suggests a scalable path to ultrasound intelligence that generalizes across heterogeneous ultrasound tasks and supports consistent end-to-end clinical workflows.

---


### 87. [When Choices Become Risks: Safety Failures of Large Language Models under Multiple-Choice Constraints](https://arxiv.org/abs/2604.16916)

**<font color=#1a73e8>作者：</font>** Yuheng Chen, Zhiyu Wu, Bowen Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety alignment in large language models (LLMs) is primarily evaluated under open-ended generation, where models can mitigate risk by refusing to respond. In contrast, many real-world applications place LLMs in structured decision-making tasks, such as multiple-choice questions (MCQs), where abstention is discouraged or unavailable. We identify a systematic failure mode in this setting: reformulating harmful requests as forced-choice MCQs, where all options are unsafe, can systematically bypass refusal behavior, even in models that consistently reject equivalent open-ended prompts. Across 14 proprietary and open-source models, we show that forced-choice constraints sharply increase policy-violating responses. Notably, for human-authored MCQs, violation rates follow an inverted U-shaped trend with respect to structural constraint strength, peaking under intermediate task specifications, whereas MCQs generated by high-capability models yield near-saturation violation rates across constraints and exhibit strong cross-model transferability. Our findings reveal that current safety evaluations substantially underestimate risks in structured task settings and highlight constrained decision-making as a critical and underexplored surface for alignment failures.

---


### 88. [x1: Learning to Think Adaptively Across Languages and Cultures](https://arxiv.org/abs/2604.16917)

**<font color=#1a73e8>作者：</font>** Yangfan Ye, Xiaocheng Feng, Xiachong Feng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Languages encode distinct abstractions and inductive priors, yet most large language models (LLMs) overlook this diversity by reasoning in a single dominant language. In this work, we introduce x1, a family of reasoning models that can adaptively reason in an advantageous language on a per-instance basis. To isolate the effect of reasoning-language choice, x1 is constructed without expanding the model's knowledge boundaries and is trained by contrasting linguistically distinct reasoning trajectories for the same input. Our extensive experiments demonstrate the benefits of adaptive multilingual reasoning across multilingual mathematical reasoning and culturally grounded tasks. Moreover, our results challenge a simplistic view of scaling laws: while scaling reduces cross-lingual disparities in procedural domains such as math reasoning, it does not eliminate the advantages of culture-associated languages in culturally grounded tasks, as we empirically show that such reasoning enables more efficient and accurate cultural knowledge recall. Overall, our findings establish language choice as a functional component of reasoning, with implications for building more generalist and globally competent reasoning models.

---


### 89. [Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning](https://arxiv.org/abs/2604.16918)

**<font color=#1a73e8>作者：</font>** Weiyu Ma, Yongcheng Zeng, Yan Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has achieved impressive success in post-training Large Language Models (LLMs) and Vision-Language Models (VLMs), with on-policy algorithms such as PPO, GRPO, and REINFORCE++ serving as the dominant paradigm. However, these methods discard all collected trajectories after a single gradient update, resulting in poor sample efficiency, particularly wasteful for agentic tasks where multi-turn environment interactions are expensive. While Experience Replay drives sample efficiency in classic RL by allowing agents to reuse past trajectories and prioritize informative ones, directly applying Prioritized Experience Replay (PER) to LLMs fails. The rapid policy evolution of billion-parameter models renders stored priorities stale, causing old high-priority trajectories to dominate sampling long after they have become uninformative. We propose Freshness-Aware PER, which addresses this priority staleness problem by augmenting any PER-based priority with a multiplicative exponential age decay grounded in effective sample size analysis. To the best of our knowledge, Freshness-Aware PER is the first work to successfully apply PER to LLM/VLM reinforcement learning. We evaluate on eight multi-step agentic, reasoning, and math competition tasks with 0.5B, 3B, and 7B models. Freshness-Aware PER significantly outperforms on-policy baselines, achieving +46% on NQ Search, +367% on Sokoban, and +133% on VLM FrozenLake, while standard PER without age decay consistently degrades performance. Our code is publicly available at this https URL.

---


### 90. [ClimAgent: LLM as Agents for Autonomous Open-ended Climate Science Analysis](https://arxiv.org/abs/2604.16922)

**<font color=#1a73e8>作者：</font>** Hao Wang, Jindong Han, Wei Fan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Climate research is pivotal for mitigating global environmental crises, yet the accelerating volume of multi-scale datasets and the complexity of analytical tools have created significant bottlenecks, constraining scientific discovery to fragmented and labor-intensive workflows. While the emergence Large Language Models (LLMs) offers a transformative paradigm to scale scientific expertise, existing explorations remain largely confined to simple Question-Answering (Q&A) tasks. These approaches often oversimplify real-world challenges, neglecting the intricate physical constraints and the data-driven nature required in professional climate this http URL bridge this gap, we introduce ClimAgent, a general-purpose autonomous framework designed to execute a wide spectrum of research tasks across diverse climate sub-fields. By integrating a unified tool-use environment with rigorous reasoning protocols, ClimAgent transcends simple retrieval to perform end-to-end modeling and this http URL foster systematic evaluation, we propose ClimaBench, the first comprehensive benchmark for real-world climate discovery. It encompasses challenging problems spanning 5 distinct task categories derived from professional scenarios between 2000 and 2025. Experiments on ClimaBench demonstrate that ClimAgent significantly outperforms state-of-the-art baselines, achieving a 40.21% improvement over original LLM solutions in solution rigorousness and practicality. Our code are available at this https URL.

---


### 91. [Alignment Imprint: Zero-Shot AI-Generated Text Detection via Provable Preference Discrepancy](https://arxiv.org/abs/2604.16923)

**<font color=#1a73e8>作者：</font>** Junxi Wu, Kailin Huang, Dongjian Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Detecting AI-generated text is an important but challenging problem. Existing likelihood-based detection methods are often sensitive to content complexity and may exhibit unstable performance. In this paper, our key insight is that modern Large Language Models (LLMs) undergo alignment (including fine-tuning and preference tuning), leaving a measurable distributional imprint. We theoretically derive this imprint by abstracting the alignment process as a sequence of constrained optimization steps, showing that the log-likelihood ratio can naturally decompose into implicit instructional biases and preference rewards. We refer to this quantity as the Alignment Imprint. Furthermore, to mitigate the instability in high-entropy regions, we introduce Log-likelihood Alignment Preference Discrepancy (LAPD), a standardized information-weighted statistic based on alignment imprint. We provide statistical guarantee that alignment-based statistics dominate Fast-DetectGPT in performance. We also theoretically show that LAPD strictly improves the unweighted alignment scores when the aligned and base models are close in distribution. Extensive experiments show that LAPD achieves an improvement 45.82% relative to the strongest existing baselines, yielding large and consistent gains across all settings.

---


### 92. [Rethinking Cross-Dose PET Denoising: Mitigating Averaging Effects via Residual Noise Learning](https://arxiv.org/abs/2604.16925)

**<font color=#1a73e8>作者：</font>** Yichao Liu, Zongru Shao, Yueyang Teng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-dose denoising for low-dose positron emission tomography (LDPET) has been proposed to address the limited generalization of models trained at a single noise level. In practice, neural networks trained on a specific dose level often fail to generalize to other dose conditions due to variations in noise magnitude and statistical properties. Conventional "one-size-for-all" models attempt to handle this variability but tend to learn averaged representations across noise levels, resulting in degraded performance. In this work, we analyze this limitation and show that standard training formulations implicitly optimize an expectation over heterogeneous noise distributions. To this end, we propose a unified residual noise learning framework that estimates noise directly from low-dose PET images rather than predicting full-dose images. Experiments on large-scale multi-dose PET datasets from two medical centers demonstrate that the proposed method outperforms the "one-size-for-all" model, individual dose-specific U-Net models, and dose-conditioned approaches, achieving improved denoising performance. These results indicate that residual noise learning effectively mitigates the averaging effect and enhances generalization for cross-dose PET denoising.

---


### 93. [Test-Time Adaptation for EEG Foundation Models: A Systematic Study under Real-World Distribution Shifts](https://arxiv.org/abs/2604.16926)

**<font color=#1a73e8>作者：</font>** Gabriel Jason Lee, Jathurshan Pradeepkumar, Jimeng Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) foundation models have shown strong potential for learning generalizable representations from large-scale neural data, yet their clinical deployment is hindered by distribution shifts across clinical settings, devices, and populations. Test-time adaptation (TTA) offers a promising solution by enabling models to adapt to unlabeled target data during inference without access to source data, a valuable property in healthcare settings constrained by privacy regulations and limited labeled data. However, its effectiveness for EEG remains largely underexplored. In this work, we introduce NeuroAdapt-Bench, a systematic benchmark for evaluating test-time adaptation methods on EEG foundation models under realistic distribution shifts. We evaluate representative TTA approaches from other domains across multiple pretrained foundation models, diverse downstream tasks, and heterogeneous datasets spanning in-distribution, out-of-distribution, and extreme modality shifts (e.g., Ear-EEG). Our results show that standard TTA methods yield inconsistent gains and often degrade performance, with gradient-based approaches particularly prone to heavy degradation. In contrast, optimization-free methods demonstrate greater stability and more reliable improvements. These findings highlight the limitations of existing TTA techniques in EEG, provide guidance for future development, and underscore the need for domain-specific adaptation strategies.

---


### 94. [MeasHalu: Mitigation of Scientific Measurement Hallucinations for Large Language Models with Enhanced Reasoning](https://arxiv.org/abs/2604.16929)

**<font color=#1a73e8>作者：</font>** Ruijun Huang, Zhiqiao Kang, Yuxuan Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The accurate extraction of scientific measurements from literature is a critical yet challenging task in AI4Science, enabling large-scale analysis and integration of quantitative research findings. However, Large Language Models (LLMs) frequently exhibit severe hallucinations, which significantly undermine the reliability of automated scientific document understanding systems. To address this problem, we propose MeasHalu, a novel framework for mitigating scientific measurement hallucinations through enhanced reasoning and targeted optimization. We first present a fine-grained taxonomy of measurement-specific hallucinations, categorizing errors across quantities, units, modifiers, and relations. Our approach incorporates a two-stage reasoning-aware fine-tuning strategy using augmented scientific data and process-based supervision. Furthermore, we introduce a progressive reward curriculum designed to penalize specific hallucination types, significantly improving extraction faithfulness. Experimental results demonstrate that MeasHalu substantially reduces hallucination rates and improves overall accuracy on the MeasEval benchmark. This work provides a targeted solution to a key bottleneck in automated scientific knowledge extraction, facilitating more trustworthy and scalable machine-assisted scientific literature analysis.

---


### 95. [CoGR-MoE: Concept-Guided Expert Routing with Consistent Selection and Flexible Reasoning for Visual Question Answering](https://arxiv.org/abs/2604.16930)

**<font color=#1a73e8>作者：</font>** Xiyin Zeng, Yi Lu, Hao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Question Answering (VQA) requires models to identify the correct answer options based on both visual and textual evidence. Recent Mixture-of-Experts (MoE) methods improve option reasoning by grouping similar concepts or routing based on examples. However, unstable routing can lead to inconsistent expert selection in the same question type, while overly stable routing may reduce flexibility. To address this, we propose Concept-Guided Routing framework (CoGR-MoE), which incorporates semantics of the answer options to guide expert selection in the training phase. Next, option features are used to reweight the selected experts, producing discriminative representations for each candidate option. These option-level representations are further used for option comparison and optimized via contrastive learning. The experimental results indicate that CoGR-MoE delivers strong performance across multiple VQA tasks, demonstrating the effectiveness of our approach.

---


### 96. [Playing Psychic: Using Thought Trees to Predict Reasoning Models Accuracy on Coding Tasks](https://arxiv.org/abs/2604.16931)

**<font color=#1a73e8>作者：</font>** Jiaxin Fang, Runyuan He, Sahil Bhatia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have shown that test-time scaling can substantially improve model performance on complex tasks, particularly in the coding domain. Under this paradigm, models use a larger token budget during inference to generate intermediate reasoning traces before producing a final answer. However, current evaluations primarily rely on competitive programming benchmarks, which may not capture the full range of reasoning abilities. In this work, we perform a systematic study of frontier reasoning models to understand their performance on real-world coding benchmarks. To gain more insights into the performance of such models, we devise a programmatic way to {\em automatically generate} coding tasks of arbitrary difficulty and structure from existing benchmarks. Using this framework, our analysis reveals that the structure of a reasoning trace, not just its contents, is a strong predictor of correctness. Motivated by this, we propose structured thought-trees as means to represent reasoning traces. To illustrate their use, we train a lightweight classifier on features extracted from thought-trees to predict trace correctness, and demonstrate that flagging and retrying structurally anomalous traces based on the extracted features yields consistent gains at lower complexity levels.

---


### 97. [LLMs can persuade only psychologically susceptible humans on societal issues, via trust in AI and emotional appeals, amid logical fallacies](https://arxiv.org/abs/2604.16935)

**<font color=#1a73e8>作者：</font>** Alexis Carrillo, Salvatore Citraro, Ali Aghazhadeh Ardebili 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scarce longitudinal evidence examines LLMs' persuasiveness and humanness along time-evolving psychological frameworks. We introduce Talk2AI, a longitudinal framework quantifying psycho-social, reasoning and affective dimensions of LLMs' persuasiveness about polarizing societal topics. In a four-way longitudinal setup, Talk2AI's 770 participants engaged in structured conversations with one of four leading LLMs on topics like climate change, social media misinformation, and math anxiety. This produced 3,080 conversations over 60,000 turns. After each wave, participants reported conviction in their initial topic stance, perceived opinion change, LLM's perceived humanness, a self-donation to the topic and a textual explanation. Feedback time series showed longitudinal inertia in convictions, indicating some human anchoring to initial opinions even after repeated exposure to AI-generated arguments. Interestingly, NLP analyses revealed that both humans and LLMs relied on fallacious reasoning in 1 conversational quip every 6, countering the ``LLMs as superior systems" stereotype behind LLMs' cognitive surrender. LLMs' perceived humanness was most learnable from sociodemographic, psychological and engagement features ($R^2=0.44$), followed by opinion change ($R^2=0.34$), conviction ($R^2=0.26$) and personal endowment ($R^2=0.24$). Crucially, explainable AI (XAI) indicated: (i) the presence of individuals more susceptible to LLM-based opinion changes; (ii) psychological susceptibility to LLM-convincing consisted of having more trust in LLMs, being more agreeable and extraverted and with a higher need for cognition. A multiverse approach with mixed-effects models confirmed XAI results, alongside strong individual differences. Talk2AI provides a grounded framework and evidence for detecting how GenAI can influence human opinions via multiple psycho-social pathways in AI-human digital platforms.

---


### 98. [No One Fits All: From Fixed Prompting to Learned Routing in Multilingual LLMs](https://arxiv.org/abs/2604.16937)

**<font color=#1a73e8>作者：</font>** Wei-Chi Wu, Sheng-Lun Wei, Hen-Hsen Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Translation-based prompting is widely used in multilingual LLMs, yet its effectiveness varies across languages and tasks. We evaluate prompting strategies across ten languages of different resource levels and four benchmarks. Our analysis shows that no single strategy is universally optimal. Translation strongly benefits low-resource languages even when translation quality is imperfect, high-resource languages gain little, and prompt-based self-routing underperforms explicit translation. Motivated by these findings, we formulate prompting strategy selection as a learned decision problem and introduce lightweight classifiers that predict whether native or translation-based prompting is optimal for each instance. The classifiers achieve statistically significant improvements over fixed strategies across four benchmarks and generalize to unseen task formats not observed during training. Further analysis reveals that language resource level, rather than translation quality alone, determines when translation is beneficial.

---


### 99. [D-QRELO: Training- and Data-Free Delta Compression for Large Language Models via Quantization and Residual Low-Rank Approximation](https://arxiv.org/abs/2604.16940)

**<font color=#1a73e8>作者：</font>** Junlin Li, Shuangyong Song, Guodong Du 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised Fine-Tuning (SFT) accelerates taskspecific large language models (LLMs) development, but the resulting proliferation of finetuned models incurs substantial memory overhead. Delta compression addresses this by retaining a single pre-trained LLM with multiple compressed delta weights. However, existing methods fail on models fine-tuned with largescale datasets. We find that larger SFT data scale amplifies delta parameter magnitude, singular values, and entropy, exacerbating compression errors. To tackle this, we propose DQRELO (Delta Compression via Quantization and Residual Low-Rank), a novel training- and data-free delta compression method. It combines coarse-grained one-bit quantization to capture the dominant structure of the delta, followed by compensated residual low-rank approximation to recover fine-grained details from the smaller residual error. Experiments on various LLMs spanning dense and MoE architectures across multiple domains under this challenging setting demonstrate that DQRELO outperforms existing methods. Moreover, we establish key design principles for delta compression through extensive empirical analysis, demonstrating how task difficulty, architecture, and layer positioning create predictable patterns that can guide optimal compression strategies in production systems.

---


### 100. [MNAFT: modality neuron-aware fine-tuning of multimodal large language models for image translation](https://arxiv.org/abs/2604.16943)

**<font color=#1a73e8>作者：</font>** Bo Li, Ningyuan Deng, Tianyu Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have shown impressive capabilities, yet they often struggle to effectively capture the fine-grained textual information within images crucial for accurate image translation. This often leads to a modality gap between visual text inputs and textual inputs/outputs for image translation. Existing methods, primarily relying on instruction fine-tuning, risk parameter redundancy of pre-trained knowledge, hindering generalization performance. To address this, we introduce modality neuron-aware fine-tuning (MNAFT), a novel approach that takes advantage of the specialized roles of individual neurons within MLLMs for enhanced image translation. MNAFT identifies language-agnostic and language-specific neurons in both vision and language modules through an instruction-driven activation analysis, evaluating their importance in various translation tasks. We then perform selective fine-tuning, updating only the parameters of language-specific and language-agnostic neurons within the selected layers relevant to the target task, while preserving the knowledge encoded in other neurons and layers. Our extensive experiments on multiple benchmarks demonstrate that MNAFT significantly outperforms state-of-the-art image translation methods, including cascaded models, standard full fine-tuning, and parameter-efficient tuning techniques. Furthermore, we provide comprehensive analysis, including visualizations of neuron activations and clustering patterns, to offer insights into the roles of different neuron groups in mediating cross-modal understanding and facilitating accurate language-specific translation.

---


> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
