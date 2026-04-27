# 🧠 大模型相关研究 | 2026年04月28日

> 本类共 **63** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-63**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-63**

---

### 51. [Controllable Spoken Dialogue Generation: An LLM-Driven Grading System for K-12 Non-Native English Learners](https://arxiv.org/abs/2604.22542)

**<font color=#1a73e8>作者：</font>** Haidong Yuan, Haokun Zhao, Wanshi Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often fail to meet the pedagogical needs of K-12 English learners in non-native contexts due to a proficiency mismatch. To address this widespread challenge, we introduce a proficiency-aligned framework that adapts LLM outputs to learner abilities, using China's national curriculum (CSE) as a representative case. Our framework enables precise control over lexical complexity through a four-tier grading system, supported by a comprehensive suite of new resources: graded vocabulary lists and a multi-turn dialogue corpus.
Our core technical contribution is the \textbf{DDPO} algorithm,Diversity Driven Policy Optimization, a multi-turn GRPO-based approach designed to preserve dialogue diversity while holistically optimizing dialogue quality. This method significantly outperforms conventional approaches, achieving low out-of-vocabulary rates and high diversity while enhancing conversational naturalness and pedagogical value. While grounded in the CSE, our framework is designed for flexibility and can be readily adapted to other educational standards. Our models, data, and code will all be open-sourced, providing a scalable platform for personalized English speaking practice that effectively addresses the unique challenges faced by K-12 learners in non-immersive environments.

---


### 52. [SOLAR-RL: Semi-Online Long-horizon Assignment Reinforcement Learning](https://arxiv.org/abs/2604.22558)

**<font color=#1a73e8>作者：</font>** Jichao Wang, Liuyang Bian, Yufeng Zhou 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As Multimodal Large Language Models (MLLMs) mature, GUI agents are evolving from static interactions to complex navigation. While Reinforcement Learning (RL) has emerged as a promising paradigm for training MLLM agents on dynamic GUI tasks, its effective application faces a dilemma. Standard Offline RL often relies on static step-level data, neglecting global trajectory semantics such as task completion and execution quality. Conversely, Online RL captures the long-term dynamics but suffers from high interaction costs and potential environmental instability. To bridge this gap, we propose SOLAR-RL (Semi-Online Long-horizon Assignment Reinforcement Learning). Instead of relying solely on expensive online interactions, our framework integrates global trajectory insights directly into the offline learning process. Specifically, we reconstruct diverse rollout candidates from static data, detect the first failure point using per-step validity signals, and retroactively assign dense step-level rewards with target-aligned shaping to reflect trajectory-level execution quality, effectively simulating online feedback without interaction costs. Extensive experiments demonstrate that SOLAR-RL significantly improves long-horizon task completion rates and robustness compared to strong baselines, offering a sample-efficient solution for autonomous GUI navigation.

---


### 53. [Learning Evidence Highlighting for Frozen LLMs](https://arxiv.org/abs/2604.22565)

**<font color=#1a73e8>作者：</font>** Shaoang Li, Yanhang Shi, Yufei Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can reason well, yet often miss decisive evidence when it is buried in long, noisy contexts. We introduce HiLight, an Evidence Emphasis framework that decouples evidence selection from reasoning for frozen LLM solvers. HiLight avoids compressing or rewriting the input, which can discard or distort evidence, by training a lightweight Emphasis Actor to insert minimal highlight tags around pivotal spans in the unaltered context. A frozen Solver then performs downstream reasoning on the emphasized input. We cast highlighting as a weakly supervised decision-making problem and optimize the Actor with reinforcement learning using only the Solver's task reward, requiring no evidence labels and no access to or modification of the Solver. Across sequential recommendation and long-context question answering, HiLight consistently improves performance over strong prompt-based and automated prompt-optimization baselines. The learned emphasis policy transfers zero-shot to both smaller and larger unseen Solver families, including an API-based Solver, suggesting that the Actor captures genuine, reusable evidence structure rather than overfitting to a single backbone.

---


### 54. [SpikingBrain2.0: Brain-Inspired Foundation Models for Efficient Long-Context and Cross-Platform Inference](https://arxiv.org/abs/2604.22575)

**<font color=#1a73e8>作者：</font>** Yuqi Pan, Jinghao Zhuang, Yupeng Feng 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling context length is reshaping large-model development, yet full-attention Transformers suffer from prohibitive computation and inference bottlenecks at long sequences. A key challenge is to design foundation models that maintain performance and long-context efficiency with minimal training overhead. We introduce SpikingBrain2.0 (SpB2.0), a 5B model that advances both architecture and training efficiency of its predecessor.
Our contributions are two-fold. (1) Architectural Innovation: We propose Dual-Space Sparse Attention (DSSA), an inter-layer hybrid of Sparse Softmax Attention (MoBA) and Sparse Linear Attention (SSE), achieving an improved performance-efficiency trade-off for long-context modeling. SpB2.0 further supports dual quantization paths: INT8-Spiking coding enables sparse event-driven computation, while FP8 coding accelerates inference on modern GPUs. (2) Enhanced Training Strategy: We develop an optimized Transformer-to-Hybrid (T2H) pipeline with dual conversion paths for LLMs and VLMs using curated open-source data.
Empirically, SpB2.0-5B and SpB2.0-VL-5B recover most of the base Transformer (Qwen3-4B) capability with under 7k A100 GPU hours. SpB2.0 achieves a 10.13x TTFT speedup at 4M context and supports over 10M tokens on 8 A100 GPUs under vLLM, where full-attention models exceed memory limits. It also demonstrates strong cross-platform compatibility, enabling FP8 GPU inference (2.52x speedup at 250k) and efficient neuromorphic execution (64.31% sparsity, with 70.6% and 46.5% area and power reduction at 500MHz).
Overall, SpikingBrain2.0 provides a practical pathway for lightweight, multimodal, spiking foundation models, highlighting the potential of combining brain-inspired mechanisms with efficient architectures for resource-constrained and edge scenarios.

---


### 55. [Rethinking Math Reasoning Evaluation: A Robust LLM-as-a-Judge Framework Beyond Symbolic Rigidity](https://arxiv.org/abs/2604.22597)

**<font color=#1a73e8>作者：</font>** Erez Yosef, Oron Anschel, Shunit Haviv Hakimi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advancements in large language models have led to significant improvements across various tasks, including mathematical reasoning, which is used to assess models' intelligence in logical reasoning and problem-solving. Models are evaluated on mathematical reasoning benchmarks by verifying the correctness of the final answer against a ground truth answer. A common approach for this verification is based on symbolic mathematics comparison, which fails to generalize across diverse mathematical representations and solution formats. In this work, we offer a robust and flexible alternative to rule-based symbolic mathematics comparison. We propose an LLM-based evaluation framework for evaluating model-generated answers, enabling accurate evaluation across diverse mathematical representations and answer formats. We present failure cases of symbolic evaluation in two popular frameworks, Lighteval and SimpleRL, and compare them to our approach, demonstrating clear improvements over commonly used methods. Our framework enables more reliable evaluation and benchmarking, leading to more accurate performance monitoring, which is important for advancing mathematical problem-solving and intelligent systems.

---


### 56. [Dharma, Data and Deception: An LLM-Powered Rhetorical Analysis of Cow-Urine Health Claims on YouTube](https://arxiv.org/abs/2604.22606)

**<font color=#1a73e8>作者：</font>** Sheza Munir, Ratna Kandala, Anamta Khan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Health misinformation remains one of the most pressing challenges on social media, particularly when cultural traditions intersect with scientific-sounding claims. These dynamics are not only global but also deeply local, manifesting in culturally specific controversies that require careful analysis. Motivated by this, we examine 100 YouTube transcripts that promote or debunk cow urine (gomutra) as a health remedy, focusing on rhetorical strategies such as appeals to authority, efficacy appeals, and conspiracy framing. We employ large language models (LLMs) including GPT-4, GPT-4o, GPT-4.1, GPT-5, Gemini 2.5 Pro, and Mistral Medium 3 to annotate transcripts using a 14-category taxonomy of persuasive tactics. Our analysis reveals that promoters predominantly rely on efficacy appeals and social proof, while debunkers emphasize authority and rebuttal. Human evaluation of a subset of annotations yielded 90.1\% inter-annotator agreement, confirming the reliability of our taxonomy and validation process. This work advances computational methods for misinformation analysis and demonstrates how LLMs can support large-scale studies of cultural discourse online.

---


### 57. [BERAG: Bayesian Ensemble Retrieval-Augmented Generation for Knowledge-based Visual Question Answering](https://arxiv.org/abs/2604.22678)

**<font color=#1a73e8>作者：</font>** Jinghong Chen, Jingbiao Mei, Guangyu Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A common approach to question answering with retrieval-augmented generation (RAG) is to concatenate documents into a single context and pass it to a language model to generate an answer. While simple, this strategy can obscure the contribution of individual documents, making attribution difficult and contributing to the ``lost-in-the-middle'' effect, where relevant information in long contexts is overlooked. Concatenation also scales poorly: computational cost grows quadratically with context length, a problem that becomes especially severe when the context includes visual data, as in visual question answering. Attempts to mitigate these issues by limiting context length can further restrict performance by preventing models from benefiting from the improved recall offered by deeper retrieval. We propose Bayesian Ensemble Retrieval-Augmented Generation (BERAG), along with Bayesian Ensemble Fine-Tuning (BEFT), as a RAG framework in which language models are conditioned on individual retrieved documents rather than a single combined context. BERAG treats document posterior probabilities as ensemble weights and updates them token by token using Bayes' rule during generation. This approach enables probabilistic re-ranking, parallel memory usage, and clear attribution of document contribution, making it well-suited for large document collections. We evaluate BERAG and BEFT primarily on knowledge-based visual question answering tasks, where models must reason over long, imperfect retrieval lists. The results show substantial improvements over standard RAG, including strong gains on Document Visual Question Answering and multimodal needle-in-a-haystack benchmarks. We also demonstrate that BERAG mitigates the ``lost-in-the-middle'' effect. The document posterior can be used to detect insufficient grounding and trigger deflection, while document pruning enables faster decoding than standard RAG.

---


### 58. [Seeing the Whole Elephant: A Benchmark for Failure Attribution in LLM-based Multi-Agent Systems](https://arxiv.org/abs/2604.22708)

**<font color=#1a73e8>作者：</font>** Mengzhuo Chen, Junjie Wang, Fangwen Mu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Failure attribution, i.e., identifying the responsible agent and decisive step of a failure, is particularly challenging in LLM-based multi-agent systems (MAS) due to their natural-language reasoning, nondeterministic outputs, and intricate interaction dynamics. A reliable benchmark is therefore essential to guide and evaluate attribution techniques. Yet existing benchmarks rely on partially observable traces that capture only agent outputs, omitting the inputs and context that developers actually use when debugging. We argue that failure attribution should be studied under full execution observability, aligning with real-world developer-facing scenarios where complete traces, rather than only outputs, are accessible for diagnosis. To this end, we introduce TraceElephant, a benchmark designed for failure attribution with full execution traces and reproducible environments. We then systematically evaluate failure attribution techniques across various configurations. Specifically, full traces improve attribution accuracy by up to 76\% over a partial-observation counterpart, confirming that missing inputs obscure many failure causes. TraceElephant provides a foundation for follow-up failure attribution research, promoting evaluation practices that reflect real-world debugging and supporting the development of more transparent MASs.

---


### 59. [Thinking Without Words: Efficient Latent Reasoning with Abstract Chain-of-Thought](https://arxiv.org/abs/2604.22709)

**<font color=#1a73e8>作者：</font>** Keshav Ramji, Tahira Naseem, Ramón Fernandez Astudillo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While long, explicit chains-of-thought (CoT) have proven effective on complex reasoning tasks, they are costly to generate during inference. Non-verbal reasoning methods have emerged with shorter generation lengths by leveraging continuous representations, yet their performance lags behind verbalized CoT. We propose $\textbf{Abstract Chain-of-Thought}$, a discrete latent reasoning post-training mechanism in which the language model produces a short sequence of tokens from a reserved vocabulary in lieu of a natural language CoT, before generating a response. To make previously unseen ''abstract'' tokens useful, we introduce a policy iteration-style warm-up loop that alternates between (i.) bottlenecking from a verbal CoT via masking and performing supervised fine-tuning, and (ii.) self-distillation by training the model to generate abstract tokens from the prompt alone via constrained decoding with the codebook. After warm-up, we optimize the generation of abstract sequences with warm-started reinforcement learning under constrained decoding. Abstract-CoT achieves up to $11.6\times$ fewer reasoning tokens while demonstrating comparable performance across mathematical reasoning, instruction-following, and multi-hop reasoning, and generalizes across language model families. We also find an emergent power law distribution over the abstract vocabulary, akin to those seen in natural language, that evolves across the training phases. Our findings highlight the potential for post-training latent reasoning mechanisms that enable efficient inference through a learned abstract reasoning language.

---


### 60. [Inter-Stance: A Dyadic Multimodal Corpus for Conversational Stance Analysis](https://arxiv.org/abs/2604.22739)

**<font color=#1a73e8>作者：</font>** Xiang Zhang, Xiaotian Li, Taoyue Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Social interactions dominate our perceptions of the world and shape our daily behavior by attaching social meaning to acts as simple and spontaneous as gestures, facial expressions, voice, and speech. People mimic and otherwise respond to each other's postures, facial expressions, mannerisms, and other verbal and nonverbal behavior, and form appraisals or evaluations in the process. Yet, no publicly-available dataset includes multimodal recordings and self-report measures of multiple persons in social interaction. Dyadic recordings and annotation are lacking. We present a new data corpus of multimodal dyadic interaction (45 dyads, 90 persons) that includes synchronized multi-modality behavior (2D face video, 3D face geometry, thermal spectrum dynamics, voice and speech behavior, physiology (PPG, EDA, heart-rate, blood pressure, and respiration), and self-reported affect of all participants in a communicative interaction scenario. Two types of dyads are included: persons with shared past history and strangers. Annotations include social signals, agreement, disagreement, and neutral stance. With a potent emotion induction, these multimodal data will enable novel modeling of multimodal interpersonal behavior. We present extensive experiments to evaluate multimodal dyadic communication of dyads with and without interpersonal history, and their affect. This new database will make multimodal modeling of social interaction never possible before. The dataset includes 20TB of multimodal data to share with the research community.

---


### 61. [Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond](https://arxiv.org/abs/2604.22748)

**<font color=#1a73e8>作者：</font>** Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin 等 42 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.

---


### 62. [Representational Harms in LLM-Generated Narratives Against Global Majority Nationalities](https://arxiv.org/abs/2604.22749)

**<font color=#1a73e8>作者：</font>** Ilana Nguyen, Harini Suresh, Thema Monroe-White 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for text generation tasks from everyday use to high-stakes enterprise and government applications, including simulated interviews with asylum seekers. While many works highlight the new potential applications of LLMs, there are risks of LLMs encoding and perpetuating harmful biases about non-dominant communities across the globe. To better evaluate and mitigate such harms, more research examining how LLMs portray diverse individuals is needed. In this work, we study how national origin identities are portrayed by widely-adopted LLMs in response to open-ended narrative generation prompts. Our findings demonstrate the presence of persistent representational harms by national origin, including harmful stereotypes, erasure, and one-dimensional portrayals of Global Majority identities. Minoritized national identities are simultaneously underrepresented in power-neutral stories and overrepresented in subordinated character portrayals, which are over fifty times more likely to appear than dominant portrayals. The degree of harm is amplified when US nationality cues (e.g., ``American'') are present in input prompts. Notably, we find that the harms we identify cannot be explained away via sycophancy, as US-centric biases persist even when replacing US nationality cues with non-US national identities in the prompts. Based on our findings, we call for further exploration of cultural harms in LLMs through methodologies that center Global Majority perspectives and challenge the uncritical adoption of US-based LLMs for the classification, surveillance, and misrepresentation of the majority of our planet.

---


### 63. [How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks](https://arxiv.org/abs/2604.22750)

**<font color=#1a73e8>作者：</font>** Longju Bai, Zhemin Huang, Xingyao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.

---


> [!TIP]
> 当前位于：**51-63**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-63**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
