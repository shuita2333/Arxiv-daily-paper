# 🧠 大模型相关研究 | 2026年07月20日

> 本类共 **119** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-119](./part-03.md)

---

### 1. [HG-RAG: Hierarchy-Guided Retrieval-Augmented Generation for Structured Knowledge Graphs](https://arxiv.org/abs/2607.14095)

**<font color=#1a73e8>作者：</font>** Pranav Yadav  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval Augmented Generation (RAG) has proven to be a widely successful process at improving the quality of outputs from a Large Language Model (LLM) for wider context. However, RAG systems typically retrieve context from flat document stores, which struggles when queries require hierarchical or relational reasoning across structured knowledge. I present HG-RAG (Hierarchy-Guided RAG), a framework that performs graph-traversal over a hierarchical knowledge graph to deliver structured context to a language model. My retrieval pipeline resolves a named entity anchor from the query, then expands context upward through parent nodes, laterally through relational neighbors, and downward through child nodes when needed. I evaluate HG-RAG against a dense retrieval baseline across three world scales (18-800 nodes) with four query types: local fact, hierarchical, neighborhood, and multi-hop. Results show HG-RAG consistently outperforms the flat baseline on hierarchical, relational, and multi-hop reasoning tasks, while reducing hallucination and maintaining locality coherence.

---


### 2. [Just Keep Prompting: Evaluating Repetitive Socratic Prompting in VLMs](https://arxiv.org/abs/2607.14099)

**<font color=#1a73e8>作者：</font>** Shayda Moezzi, Bishoy Galoaa, Lorena Genua 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deploying Vision-Language Models (VLMs) in real-world settings requires not only strong visual reasoning but also stability under sustained conversational pressure. We introduce Just Keep Prompting (JKP), a multi-turn evaluation framework that measures VLM epistemic stability when users repeatedly challenge, question, or contradict a model's answer. JKP probes models for up to 10 follow-up turns using three strategies: Adversarial Negation (repeated rejection), Pure Socratic Interrogation (repeated calls to reassess certainty), and Context-Aware Socratic Summarization (reflecting the model's prior rationale back before asking for reconsideration). We evaluate GPT-4o, Gemini 2.5 Pro, and Qwen3-VL-30B on a subset of the STAR benchmark across 720 multi-turn runs. Aggregate accuracy changes modestly from Turn 0 to Turn 10, but trajectory-level analysis reveals substantial instability: correct answers regress, wrong answers recover, and many runs exhibit repeated answer flipping. Repeated prompting has bounded upside and often acts as a destabilizer rather than a reasoning aid. The effect is strongly model-dependent: Qwen3-VL-30B achieves the highest final accuracy but becomes confidently wrong under direct contradiction; Gemini 2.5 Pro is comparatively stable but token-expensive; GPT-4o is the most brittle and oscillatory. These findings reveal that multi-turn VLM evaluation captures not just additional reasoning but pressure-response profiles: how models trade off visual grounding, calibration, and conversational compliance under repeated challenge.

---


### 3. [Latent Communication Between Language Model Agents: Channels, Alignment, and the Limits of Text](https://arxiv.org/abs/2607.14103)

**<font color=#1a73e8>作者：</font>** Markus Wenzel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) are utilized in many contexts and many professions. Those MAS rely on inter-agent communication, usually implemented by clear-text message passing. We hypothesize that Large Language Models may have a world model at their disposal that exceeds expressibility in text when complex concepts need to be communicated. Our aim is to approach a proof of this hypothesis with structured experiments. In this work, we show that LLM agents communicating via text lose information, which we quantify via Sparse Autoencoder (SAE) feature analysis. We construct three communication channels and measure concept-discriminating information in each. We first show that the SAE-sparse channel retains a 99.4% probe accuracy at 28-fold compression over the dense-latent channel vs 80.4% for the text channel. We then proceed to examine the same for cross-architecture communication by using sparse latent space alignment. We find for Procrustes alignment a 92% top-1 retrieval between Llama and Mistral. Using a text round-trip, we perform feature survival analysis to find that text serialization destroys 88% of SAE features, replacing them with a different feature set. We attribute the loss to identity replacement, not attenuation. By our analysis, we were able to attribute a 3-10pp performance penalty to the linear Procrustes alignment, improving with nonlinear alignment methods. In a task-level evaluation we find that the latent channel matches the text channel on cross-lingual concept tasks but never exceeds it. Text augmentation with latent features provides no benefit, leading us to negative conclusions for the initial hypothesis: lost features mostly or completely encode surface form, not task-relevant semantics. To pinpoint the practical advantage of latent communication over a text channel, deeper tasks eliciting complex concepts and an corresponding analysis framework are needed.

---


### 4. [Automatically Evolving Prompt Guidelines for Task-Specific Optimization](https://arxiv.org/abs/2607.14105)

**<font color=#1a73e8>作者：</font>** Cedric Richter, Salah Ghamizi, Mike Papadakis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For Large Language Models to reliably answer user queries, users must clearly specify requirements, context, and constraints. In practice, however, user queries are often underspecified, forcing models to infer unstated assumptions that may misalign with the actual user intent. Existing prompt engineering guidelines aim to mitigate this issue, they are typically generic and task-agnostic, limiting their practical utility. Additionally, existing guidelines are formed manually and in a non-systematic way. To this end, we study prompt guideline optimization: the problem of automatically generating task-specific guidelines that help write better-specified prompts for a given task and model. Our key observation is that existing (completed) task examples (aka reference answers) often implicitly encode the missing information required to complete underspecified queries, including behavioral constraints, contextual assumptions, and evaluation criteria. We therefore propose AGOPS, an automatic approach that evolves task-specific guidelines via an optimization scheme that involves a prompt LLM writer, a solver LLM and prompt evolution, which maximize downstream effectiveness on a set of examples (user queries with reference answers). At inference time, our guidelines help users write well-specified prompts, boosting the effectiveness of LLMs. We show across mathematical reasoning, medical question answering, and coding tasks, that prompt underspecification leads to major drops (up to 95.3%) in downstream task performance (compared to well-specified prompts) and, perhaps more importantly, that this drop can hardly be recovered by existing prompt optimization techniques. Users following AGOPS guidelines can regain this loss (increasing performance between 15.5 to 81.7% on average) consistently across all benchmarks.

---


### 5. [Token Time Continuous Diffusion for Language Modeling](https://arxiv.org/abs/2607.14106)

**<font color=#1a73e8>作者：</font>** Parikshit Bansal, Sujay Sanghavi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper we introduce token time continuous diffusion (TTCD), a new diffusion language model which (a) operates in continuous space, deterministically mapping Gaussian noise to a final token canvas with no further sampling, and crucially (b) incorporates a new notion of per-token times, with some tokens proceeding from noise to token at a faster rate than others. Continuous space modeling helps TTCD avoid the parallel sampling of multiple tokens, which is a key source of inaccuracy at high speedups for models that iterate purely in discrete space. The notion of per-token times helps TTCD to better model conditional generation, allows for more sure tokens to proceed at a faster rate, and allows for differentiated inter-token influences during refinement. TTCD outperforms discrete models at high speedups. We train a 160M parameter TTCD model on OpenWebText, and then self-distill it; we find that at high speedups we are comparable in unconditional generation quality, and outperform in conditional generation, several existing models of similar size trained, on the same data, and self-distilled. We achieve similar gains in Sudoku solving as well.

---


### 6. [Polestar: Drift-Aware Cache Calibration and Token Commitment for Efficient Inference of Diffusion LLMs](https://arxiv.org/abs/2607.14107)

**<font color=#1a73e8>作者：</font>** Mingyu Lee, Akshat Ramachandran, Souvik Kundu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The inference efficiency of diffusion large language models (dLLMs) is constrained by two challenges: bidirectional attention precludes efficient KV-cache reuse, while increasing decoding parallelism with static confidence thresholds can compromise generation quality. We observe that both challenges arise from a shared phenomenon: as tokens are decoded, their contextual integration through bidirectional attention causes token representations to drift (evolve) across decoding steps. This insight motivates Polestar, a training-free inference framework that uses token representation drift as a unified signal to jointly address both challenges. Polestar comprises two components: Polestar-Cache, which identifies stale KV-cache positions via drift and performs sparse KV-cache refreshes to enable efficient reuse, and Polestar-Commit, which detects sharp drift events to reliably identify commit-ready tokens. Across mathematics and coding benchmarks on several dLLM families, Polestar sets a new state of the art on the accuracy-throughput Pareto frontier, achieving up to 10.73% accuracy improvement, up to 3.7x higher throughput, and high decoding parallelism of 3.67 tokens per forward pass over existing baselines.

---


### 7. [Eta Given Delta: Defining LLM Tool Efficiency With Marginal Tool Utility](https://arxiv.org/abs/2607.14108)

**<font color=#1a73e8>作者：</font>** Nyx Iskandar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces tool efficiency, a new quantitative metric to evaluate the rate of useful tool calls in an LLM agent trajectory. To ensure that tool efficiency is well-defined, we also introduce marginal tool utility, a new quantitative metric defined per tool call indicating whether a tool is useful or whether it can be safely removed from the tool suite without affecting accuracy while increasing tool efficiency; in this paper, we determine the sign of marginal tool utility for each tool call in a trajectory using LLM-as-a-Judge. While much prior work has been done to develop techniques that improve tool use by LLMs and design evaluation methods measuring efficiency indirectly using accuracy as a proxy, our work is centered on measuring efficiency directly via the quantitative metric proposed in this paper in post hoc trajectory analyses. It is our intention that this work contributes to the frontier of LLM evaluation research as a springboard for future benchmark designs and agent harness engineering (specifically with regards to creating lean tool suites) that optimize for metrics that complement but are distinct from accuracy.

---


### 8. [Simplicity Paradox: Debunking myths about prompting and datasets for LLM evaluation](https://arxiv.org/abs/2607.14109)

**<font color=#1a73e8>作者：</font>** Inder Preet, Shuxin Lin, Dhaval Patel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Probing the capabilities of Large Language Models (LLMs) and building robust solutions for Multiple-Choice Question Answering (MCQA) remain central challenges in natural language understanding. Furthermore, the rapid proliferation of LLMs has created the implicit assumption that more sophisticated prompting techniques yield better performance. Several studies claim better performance with more sophisticated prompting techniques, but do not provide a comprehensive evaluation. We address this gap through a comprehensive empirical study of 8 prompting techniques across 10 multiple-choice question answering (MCQA) datasets, encompassing 27 model configurations and roughly 4,300 unique questions evaluated more than 430,000 times. Our findings reveal a striking paradox that baseline prompting consistently outperforms complex reasoning techniques on various benchmarks. Only minimal expert and inductive role framing (CoT-Expert and CoT-Inductive) yields a small but statistically significant $\sim$3 percentage-point (pp) gain over baseline whereas every other elaborate technique we tested matches or under-performs it, often by large margins (up to 31~pp for Self-Analogical). We further investigate three critical phenomena: (1) the unexpected victory of Qwen3-30B-A3B-Thinking-2507 in Elo ratings, (2) the performance-efficiency trade-offs across model variants with different thinking budgets, revealing model-dependent optimal configurations, and (3) the substantial variation in dataset difficulty, with 60% of benchmarks below 70% accuracy and a 47.5~pp spread from easiest to hardest, indicating considerable room for model improvement. These results suggest that the LLM evaluation community may be overcomplicating prompt engineering and that substantial performance gaps remain across diverse benchmarks, offering opportunities for genuine model improvements rather than prompt optimization.

---


### 9. [Introspection Fine-Tuning (IFT): Training Small LLMs to Introspect](https://arxiv.org/abs/2607.14111)

**<font color=#1a73e8>作者：</font>** Ely Hahami, Ishaan Sinha, Lavik Jain  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can small language models detect and report on perturbations their own internal activations? We investigate this question through the lens of activation steering: injecting concept vectors into a model's residual stream and measuring whether the model can accurately report on the perturbation. We first show that the binary detection paradigm used in prior work -- prompting the model to answer Yes'' or No'' to whether it detects an injected thought -- is confounded in small models, as steering biases the model toward affirmative responses regardless of the question content. We therefore propose two confound-free evaluation paradigms: sentence localization (identifying which of $N$ sentences was perturbed, chance $= 1/N$) and strength comparison (identifying which of two sentences received a stronger injection, chance $= 50\%$). Evaluating across six models from two families (Llama-3.2 and Gemma-4), we find that models as small as 2B parameters introspect reliably well above chance, and that introspective ability generally increases with scale. Llama-1B, however, performs at or below chance. We then introduce \emph{Introspection Fine-Tuning} (IFT): supervised fine-tuning on sentence-localization examples constructed from the model's own perturbed forward passes. IFT raises Llama-1B sentence-localization accuracy from $9.6\%$ to $60.6\%$ (a $6\times$ improvement), with gains generalizing zero-shot to the held-out strength-comparison task ($30.2\% \to 52.2\%$). IFT also improves introspection for 3B and 8B models, while inducing negligible degradation on standard capability benchmarks. Our results suggest that introspective ability is not fixed by scale alone: it can be directly trained, and doing so unlocks latent self-monitoring capacity with implications for AI transparency and alignment. Our code is \href{this https URL}{here}.

---


### 10. [Information-Theoretic Limits of Reliability and Scaling in Language Models](https://arxiv.org/abs/2607.14112)

**<font color=#1a73e8>作者：</font>** Subhabrata Majumdar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are evaluated as though perfect reliability is achievable for any task given sufficient scale. We show this assumption is information-theoretically unjustified. Every generative task has a reliability ceiling that no model can exceed, determined by how much output uncertainty is resolvable from observable context. The gap decomposes into a resolvable component closable with additional context and a subjective component inherent to task ambiguity. Autoregressive generation further degrades this ceiling at a rate governed by the task's dependency kernel, which quantifies inter-token correlations in the output. From these two primitives, we derive a first-principles scaling law where LLM performance is bottlenecked by the scarcer resource: training data or model capacity. This law recovers the Chinchilla scaling law as a special case and provides a structural account of when scaling improves reliability. Beyond scaling, our framework unifies diverse practical phenomena, such as the benefits of retrieval-augmentation and the spectral mechanics of catastrophic forgetting. Our work formalizes the resource-complexity tradeoffs that govern model performance across domains, offering a unified theory of performance limits in generative language models.

---


### 11. [T5-CSBoost: Adversarial Perturbation Resistant LLM Fingerprinting](https://arxiv.org/abs/2607.14113)

**<font color=#1a73e8>作者：</font>** Gayan K. Kulatilleke, Mahsa Baktashmotlagh, Siamak Layeghy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While many AI-generated text (AIGT) detectors achieve strong performance on clean inputs, their accuracy degrades significantly under light paraphrasing, word substitutions, character edits, and distribution shifts. We present T5 Contrastive Style Boosted Classifier (T5-CSBoost), an extension to the T5-Sentinel framework that keeps the original next-token prediction objective for source attribution while introducing an auxiliary margin-based triplet loss over decoder embeddings.
This contrastive style regularization encourages the learning of compact, perturbation-resistant stylistic representations, offering a lightweight yet effective alternative to prior approaches that rely on architectural modifications, adversarial training, or complex multi-task objectives without altering the underlying T5-small backbone. T5-CSBoost achieves state-of-the-art multiclass source attribution and binary human-vs-LLM detection on OpenLLMText and HC3 AIGT benchmarks. More importantly, T5-CSBoost demonstrates enhanced robustness to word and character level adversarial perturbations of up to 90% intensity, achieving state-of-the-art on the challenging MAGE/Deepfake stress-test suite, including unseen models, unseen domains, and extreme paraphrasing scenarios. Our results highlight that explicitly regularizing stylistic embeddings via contrastive learning is a practical and effective strategy for building more robust LLM fingerprinting systems in real-world adversarial settings.

---


### 12. [CoEvoT: Co-Evolving Chain-of-Thought Prompting for Graph-LLM Reasoning](https://arxiv.org/abs/2607.14114)

**<font color=#1a73e8>作者：</font>** Haohua Niu, Xingtong Yu, Yang Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Graph learning under distribution shift presents a persistent challenge, where models adapt to new graphs with limited or even no supervision. Recent graph--LLM approaches move toward label-efficient prediction by linearizing graphs into prompts and using large language models (LLMs) as predictors, and can adopt Chain-of-Thought (CoT) prompting to exploit LLM's multi-step reasoning capability. However, existing CoT-based graph--LLM methods generate intermediate thoughts while conditioning on fixed graph tokens, limiting step-wise refinement of structural cues. In this paper, we propose CoEvoT, a simple yet effective co-evolving CoT prompting framework for graph--LLM reasoning. CoEvoT couples text-to-graph token rewriting and graph-to-text reasoning guidance in a closed loop: each intermediate textual thought is used to update the graph token evidence state via a lightweight condition network, and the updated tokens are fed back into the next-step instruction to guide subsequent LLM reasoning. This enables step-wise, state-aware evidence refinement, rather than reasoning over a fixed graph snapshot. Extensive experiments on eight datasets demonstrate that CoEvoT consistently outperforms state-of-the-art baselines.

---


### 13. [Heterogeneous Element-Aware Cross-Version Differencing of Scientific Documents via Layout-Aware Alignment and Structure-Aware Reasoning](https://arxiv.org/abs/2607.14117)

**<font color=#1a73e8>作者：</font>** Zhen Yina, Wenkang An, Hao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-version differencing of scientific documents is essential in scholarly publishing and technical documentation, but remains challenging because scientific documents are page-structured artifacts containing heterogeneous elements such as text, tables, formulas, figures, and layout cues. Existing text-sequence-based methods often lose layout and structural information, while image-based methods lack semantic interpretability and are sensitive to rendering variation. To address these limitations, this paper proposes a layout-aware heterogeneous element-aware framework for scientific document differencing. The framework decomposes document versions into semantically typed elements, establishes cross-version correspondence through an alignment-first mechanism that jointly models spatial, content, and structural compatibility, and performs type-aware difference reasoning over aligned element pairs. It supports unified change detection, localization, structure-awareness analysis, and alignment/matching evaluation across text, tables, formulas, and figures. Experiments on real-world scientific PDF data from journal production proofreading workflows show that the proposed framework consistently outperforms element-specific baselines. It achieves detection F1 scores of 0.903, 0.855, 0.862, and 0.845 for text, tables, formulas, and figures, respectively, with further improvements in localization, structure awareness, and matching quality. Ablation and sensitivity analyses confirm the effectiveness of cross-version alignment, type-specific representations, structure-aware reasoning, and compatibility-weight design. These results demonstrate that heterogeneous element-aware differencing provides a robust and interpretable solution for scientific document comparison in realistic editorial production scenarios.

---


### 14. [Budgeted Subset Refinement for Execution-Aware LLM Research Ideation](https://arxiv.org/abs/2607.14118)

**<font color=#1a73e8>作者：</font>** Micah Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate research ideas that appear novel to expert reviewers, but recent work also shows that such ideas often lack diversity, are difficult for LLMs to evaluate reliably, and may fail to translate into strong executed projects. This paper evaluates a controlled proxy benchmark for a pre-execution scaffolding problem: given a noisy pool of LLM-generated research ideas, how should a system allocate limited refinement effort to construct a stronger, more diverse, more execution-aware portfolio for human researchers under a fixed rubric? We introduce Budgeted Subset Refinement, a family of strategies that refine only a selected subset of candidates rather than refining all candidates uniformly. In a unified shared-candidate-pool evaluation across 10 random seeds and 10 research-ideation environments, raw generation and reranking alone produce no research-strong nonduplicate ideas under the benchmark rubric, while refinement is necessary for strong proxy-rated portfolios. Uniform refinement produces strong individual ideas but is not the best portfolio-level allocation of compute. Random-k refinement is a strong low-cost baseline, while diversity-aware MMR-k refinement gives the best overall proxy tradeoff: the highest research-strong nonduplicate yield, the lowest duplicate rate among successful methods, and the best cost per research-strong nonduplicate idea. A blinded external-judge robustness check on a balanced 72-item sample supports the broad refinement effect across independent model families, while showing that per-item rankings among refined strategies vary by judge. These results suggest that LLM research ideation systems should be evaluated not only as idea generators, but as budgeted support-allocation systems. The claims are scoped to proxy-rated portfolio quality and do not substitute for expert review or execution-grounded validation.

---


### 15. [Semantic Register Compression in Multi-Agent LLM Cascades](https://arxiv.org/abs/2607.14119)

**<font color=#1a73e8>作者：</font>** Manuele Tele Junior Fernandez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems commonly decompose complex tasks into specialized roles. However, this modularity introduces a representational risk: when intermediate agents transform text across linguistic registers, they can systematically compress the semantic distinctions needed for accurate downstream decisions. We term this phenomenon semantic register compression and characterize it as an observable failure mode in multi-agent cascades. Using a three-agent pipeline (Collector-Evaluator-Decider), we quantify compression via inter-label separation in sentence-transformer embedding space. Across political fact-checking (LIAR), sentiment analysis (SST-5), and medical triage (Triagegeist), critical evaluation consistently reduces label separability by 41.7% at the Evaluator stage, while identity passthrough preserves it nearly fully. Five architectural variants causally isolate oriented semantic transformation as the primary driver. A credibility-seeking variant produces minimal geometric compression yet shifts outputs toward mostly-true, demonstrating that transformation valence controls the direction of distributional collapse independently of compression magnitude. Compression generalizes across the three domains with varying intensity: 41.7% in fact-checking, 27.2% in sentiment, and 20.0% in triage. Prompt-level regression explains 78% of the variance, with operational constraints associated with lower compression. These results demonstrate that semantic register compression is a measurable and generalizable phenomenon in multi-agent LLM systems, with implications for safety evaluation in high-stakes domains.

---


### 16. [CARPRT: Class-Aware Zero-Shot Prompt Reweighting for Black-Box Vision-Language Models](https://arxiv.org/abs/2607.14125)

**<font color=#1a73e8>作者：</font>** Ruijiang Dong, Zesheng Ye, Jianzhong Qi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-trained vision-language models (VLMs) enable zero-shot image classification by computing the similarity score between an image and textual descriptions, typically formed by inserting a class label (e.g., "cat") into a prompt (e.g., "a photo of a"). Since the score for a given image-class pair is sensitive to the choice of prompt, existing studies ensemble multiple prompts using a weighting vector to aggregate scores across different prompts. Yet, in current strategies, the weighting vector assigned to each prompt is shared across all classes, implicitly assuming that prompts are conditionally independent of classes, which often does not hold in practice, as a prompt like "an aerial view of" might be apt for "airport" but ill-suited for "apple". To address this, we propose class-aware zero-shot prompt reweighting (CARPRT). This scoring scheme adjusts the weighting vector for each class label by capturing the class-specific relevance of different prompts in a training-free manner. For each class label and every available prompt, we quantify their class-specific relevance by averaging image-text relevance scores over images predicted to that class under the given prompt. These estimates are then normalized to derive class-specific weights. Evaluations on standard image classification benchmarks show that CARPRT outperforms existing class-independent reweighting methods, confirming that modeling prompt-class dependencies is crucial for effective zero-shot prediction and even broader VLM-based application settings that rely on prompt ensembling. Our code is available at this https URL.

---


### 17. [Interpretable Language Model for Closed-Loop Type 1 Diabetes Control](https://arxiv.org/abs/2607.14126)

**<font color=#1a73e8>作者：</font>** Maya Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Type 1 Diabetes (T1D) is a chronic, life-threatening autoimmune condition characterized by the complete destruction of insulin-producing pancreatic beta cells. While Artificial Pancreas Systems (APS) powered by Reinforcement Learning (RL) have shown promise in automating insulin delivery, their ``black-box'' nature makes it hard for patients and doctors to trust them fully. This paper presents LLM-T1D, a promising approach that combines the precision of RL with the clear, human-like reasoning of Large Language Models (LLMs) to create a more transparent and reliable insulin pump controller. By training an expert RL system and distilling its knowledge into fine-tuned LLaMA 3.1 8B and Qwen3 8B models, we developed a controller that not only surpasses the RL system's performance but also explains its decisions in plain, understandable language. Tested on the FDA-approved UVA/Padova T1D simulator, the LLM controllers deliver excellent blood sugar control (73.5% Time in Range) while maintaining strict formal safety verification against hallucinations.

---


### 18. [ToolAnchor: Anchoring Counterfactual Context to Boost Agentic Tool-use Capability](https://arxiv.org/abs/2607.14145)

**<font color=#1a73e8>作者：</font>** Weiting Liu, Jieyi Bi, Wanqi Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented large language model agents excel at long-horizon tasks, yet they are typically post-trained on fixed toolsets. When tasks demand new tools, these agents struggle to incorporate them effectively, and retraining from scratch is often impractical. We identify the core obstacle in such toolset expansion problem as behavioral inertia: the tendency of agents to fall back on familiar tools and established reasoning patterns despite having access to new ones. We demonstrate that injecting counterfactual anchor contexts at critical decision points can break this inertia, recovering failed trajectories by eliciting suppressed agent capabilities. To scale this insight, we propose ToolAnchor, a framework that uses teacher models to hypothesize these counterfactual contexts, verifies them via student rollouts, and internalizes the successful interventions through agentic post-training. Extensive evaluations across general AI assistant (GAIA), textual search (BrowseComp), and visual search (VDR-Bench) tasks demonstrate that ToolAnchor consistently exhibits competitive performance under expanded toolsets. Our work bridges the gap between static post-training and dynamic adaptation, charting a new path for scalable agentic reinforcement learning.

---


### 19. [Enhancing Small Language Models Reasoning through Knowledge Graph Grounding](https://arxiv.org/abs/2607.14149)

**<font color=#1a73e8>作者：</font>** Dimitrios Kelesis, Konstantinos Bougiatiotis, Georgios Paliouras  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although large language models (LLMs) have set benchmarks for zero-shot reasoning, their deployment remains cost-prohibitive and environmentally taxing. Small Language Models (SLMs) offer a sustainable alternative, but prone to errors, on tasks requiring complex, multi-hop logical grounding. We investigate a neuro-symbolic agentic framework to enhance the reasoning capabilities of SLMs, specifically Gemma 3 (1B, 4B) and Llama 3.2 (3B), using the CLUTRR kinship benchmark. Our approach transforms the SLM into a minimalist agent utilizing two specialized tool calls: extract_facts for symbolic triplet extraction and get_hint for expert reasoning via a Relational Graph Convolutional Network (RGCN). We evaluate these models across two configurations, both in an Oracle scenario with ground-truth triplets and a Realistic scenario relying on self-extracted knowledge. Our results reveal that while RGCN-derived hints provide a 1.5 - 2x performance gain over story-only baselines, the system is constrained by the extraction bottleneck and sequential deductive fragility, where early extraction errors compound over multi-hop chains. Furthermore, we identify a "distraction effect" in specific architectures where noisy, self-generated facts degrade performance despite the presence of expert hints. This work characterizes the challenges of symbolic grounding in low-resource agentic systems and provides a roadmap for iterative verification in neuro-symbolic agentic pipelines.

---


### 20. [When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models](https://arxiv.org/abs/2607.14169)

**<font color=#1a73e8>作者：</font>** Javier Aguilar Martín  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can synthesize a game's rules as executable code - a Code World Model (CWM) - which a classical planner then searches over. Such models are typically accepted when they reach high transition accuracy on sampled trajectories. We argue this is the wrong notion of adequacy for planning.
We show four things. (1) An LLM-synthesized CWM can pass a sampling gate at 100% transition accuracy and be $\geq 98\%$ state-accurate on the planner's own search distribution, yet lose systematically at play, because the $<1\%$ it gets wrong is exactly the pivotal dynamics; the play cost of the omitted rule is $0.091$ (seed-clustered 95% CI $[0.065,0.117]$, $n=4800$). We call this the verified-vs-correct gap, and confirm it end-to-end through the synthesis pipeline. (2) The harm follows a quantitative law, $\mathrm{danger}=\mathrm{play\_cost}\times(1-\mathrm{rarity})^N$, whose $(1-\mathrm{rarity})^N$ gate-miss factor is proven exact and whose play cost is empirically bounded. (3) The failure is not repaired by more data: LLM synthesis behaves as rule translation, not rule inference, and did not infer the omitted rule across models (GPT-5.x) and data regimes (including DAgger and targeted examples). (4) The same mechanism recurs on the belief-inference function of imperfect-information CWMs: we prove a coverage bound (a size-$N$ gate is identifying when $N\gtrsim b^{d_{\max}}$), explaining why shallow games such as Kuhn poker show no gap, and hand-construct Beacon, a verified-but-wrong inference function that passes the gate yet loses every game.
These results suggest adequacy for planning-oriented world models should be measured on the search distribution or by play directly, not by prediction accuracy on sampled transitions.

---


### 21. [Branching Policy Optimization: Sandbox-Native Language Agent Reinforcement Learning](https://arxiv.org/abs/2607.14171)

**<font color=#1a73e8>作者：</font>** Bowei He, Yankai Chen, Xiaokun Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has emerged as the dominant paradigm for training large language model (LLM) agents that interact with executable sandboxes. State-of-the-art algorithms such as PPO, RLOO, and GRPO inherit their rollout topology from RLHF: for each prompt, N independent trajectories are sampled from the initial state, and an advantage is computed by subtracting a group baseline. This design ignores a defining property of agent sandboxes. They are deterministic, snapshottable, and resumable from any intermediate state. We argue that this property enables a fundamentally different rollout topology: rather than N independent trees of depth T, one can construct a single tree of N leaves whose siblings share prefixes, and therefore share variance. We instantiate this idea as Branching Policy Optimization (BPO), a sandbox-native RL algorithm that (i) adaptively snapshots the sandbox at high-entropy decision points along a backbone trajectory, (ii) forks K alternative actions per branch point and rolls out each to termination, and (iii) computes per-step advantages from sibling returns rather than from independent prompts. We prove this estimator is unbiased and has strictly lower variance than the trajectory-level baseline, with the reduction equal to the prefix-explained portion of return variance. On WebShop, ALFWorld, and SWE-bench Verified with Qwen2.5-7B and Llama-3.1-8B backbones, BPO improves success by 3.6--6.1 absolute points over GRPO and RLOO at matched compute, halves gradient-norm variance, and matches the best baseline using 38% fewer policy updates.

---


### 22. [RENEW: Towards Learning World Models and Repairing Model Exploitation from Preferences](https://arxiv.org/abs/2607.14180)

**<font color=#1a73e8>作者：</font>** Logan Mondal Bhamidipaty, Mykel Kochenderfer, Subramanian Ramamoorthy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models are widely used in offline reinforcement learning (RL) to improve sample efficiency and generate experience beyond a fixed dataset. However, they are vulnerable to model exploitation where data coverage is thin. Prior work addresses this either by collecting more expert demonstrations, which is often expensive, unsafe, or unavailable, or by conservative algorithms that avoid uncertain regions, which limits generalization. We propose instead to repair exploitation directly using human preferences over imagined rollouts, leveraging the strong intuitive physics that allows humans to easily spot egregious dynamics hallucinations. We formalize this as Dynamics Learning from Human Feedback (DLHF), a Bradley-Terry preference loss over trajectory log-likelihoods under a learned dynamics model. Unfortunately, naive DLHF is sample inefficient, so we introduce RENEW, which uses epistemic uncertainty to focus finetuning where the model is most exploitable. We evaluate on several Jumanji and classic control environments and find that while naive DLHF requires an outsize preference budget, RENEW makes the framework practical by improving sample efficiency, limiting catastrophic forgetting, and reducing exploitation in pretrained world models. Taken together, our results provide initial evidence that preferences can supervise world model dynamics directly, offering a new approach to addressing exploitation in offline model-based RL.

---


### 23. [Closed-Loop Knowledge Dynamics: An Operational Framework for Saturation and Escape](https://arxiv.org/abs/2607.14185)

**<font color=#1a73e8>作者：</font>** Xuening Wu, Shan Yu, Shenqin Yin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feedback-driven loops support iterative improvement in large language models, reinforcement learning, and autonomous discovery, yet their gains often diminish under repeated internal feedback. We study why closed-loop knowledge systems saturate and what external information can move them beyond their current attractors. We introduce a three-level operational framework in which knowledge states $x_t$ evolve through transition kernels $K_{\theta}$ indexed by a structural parameter $\theta$. The governing structure is defined as the observational equivalence class of $\theta$ induced by these kernels, while attractors and basins are properties of the fixed-$\theta$ dynamics. A structural intervention changes $\theta$ and produces a detectable kernel discrepancy on pre-specified probe states, making structural change falsifiable. Using a Lyapunov drift condition, we show that stable internal dynamics approach bounded stability regions with exponentially attenuated transients and a noise-controlled residual floor. We characterize escape through a metric condition on intervention-induced attractor displacement and a baseline-relative KL lower bound for increasing escape probability. This analysis also explains why conditional mutual information alone cannot certify escape: it measures variation among intervention-conditioned updates rather than departure from the no-intervention law. Case studies in LLM code repair, sparse-reward reinforcement learning, and Bayesian optimization use matched continuation controls to illustrate how feedback strength and alignment affect quality-improving escape. Our contribution is an operational connection among stability tools, measurable intervention effects, and cross-domain diagnostics.

---


### 24. [RxBrain: Embodied Cognition Foundation Model with Joint Language-Visual Reasoning and Imagination](https://arxiv.org/abs/2607.14187)

**<font color=#1a73e8>作者：</font>** Haotian Liang, Mingkang Chen, Yufei Huang 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied cognition requires agents to connect high-level task reasoning with the physical states to be achieved. We introduce Hy-Embodied-RxBrain, an embodied cognition foundation model with joint language-visual reasoning and imagination. Unlike vision-language models that emphasize scene understanding and textual decision making, or generative world models that mainly predict future visual states, RxBrain represents embodied plans in a single planning sequence where language and visual imagination play complementary roles. Language provides the abstract structure of a plan, including task decomposition, planning primitives, constraints, temporal order, and decision logic, while visual imagination grounds this structure through world state prediction and joint subgoal planning, associating each planning step with intermediate and final physical states. RxBrain adopts a unified multimodal Mixture-of-Transformers architecture that supports language, image, and video understanding and generation within one model. To train this capability, we build an automatic pipeline that converts embodied videos into joint text-visual planning supervision by decomposing videos into planning steps and aligning them with visual state transitions. We further introduce RxBrain-Bench to evaluate whether models can represent embodied plans through joint textual and visual components rather than separate understanding or generation. Experiments show that RxBrain maintains embodied understanding and generation abilities, and produces plans with coupled textual reasoning, world state prediction, and joint subgoal planning. We also extend RxBrain to continuous robot action generation, where it shows promising real-robot performance without large-scale action-data pretraining. These results provide an initial step toward foundation models for embodied cognition.

---


### 25. [TEDDY: A Pediatric Foundation Model for Risk Forewarning from ICD-Coded Diagnostic Histories](https://arxiv.org/abs/2607.14191)

**<font color=#1a73e8>作者：</font>** Matthew Brady Neeley, Jorge Botas, Johnathan Jia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pediatric electronic health records capture developmentally structured clinical trajectories, yet their potential for generative healthcare foundation models remains largely unexplored. Here we present TEDDY (Temporal Event Decoder for Disease in Youth), a 1.84-million-parameter decoder transformer trained on approximately 73 million ICD-10 diagnoses from 1.6 million children at a single pediatric institution. TEDDY models longitudinal diagnosis trajectories and visit timing. Predictions were made before visit codes were revealed, limited to first occurrences, and evaluated against sex- and age-matched controls. Across 797 disease-onset prediction tasks spanning 16 ICD-10 chapters, TEDDY achieved a median AUC of 72.0%, outperforming same-data DenseNet (50.0%), CNN (57.2%), RNN (60.1%), and LSTM (62.7%) baselines on 96-99% of tasks. Performance held across sex and age and was strongest among lower-prevalence diagnoses; 202 of the 225 rarest conditions (90%) had 95% confidence intervals above chance. Predictive signal remained detectable more than two years before first recorded diagnosis, with median AUCs of 59.7% in the unrestricted analysis and 64.4% in a fixed-cohort sensitivity analysis. In asthma and attention-deficit/hyperactivity disorder benchmarks, AUCs were 79.3% and 84.7%, compared with 62.7% and 71.7% for the strongest comparators, including a general-purpose language model three orders of magnitude larger. Visit-timing predictions had a 3.0-day mean absolute restricted mean survival-time error over 365 days, although median and long-tail return intervals remained miscalibrated. Together, these results establish pediatric diagnostic histories as a substrate for compact generative models supporting broad, rare-disease, and long-horizon risk forecasting without population-scale data or billion-parameter models.

---


### 26. [How Artificial Intelligence LLM Engines Shape the Global Conflict Information Environment](https://arxiv.org/abs/2607.14197)

**<font color=#1a73e8>作者：</font>** Jason Miklian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) answer engines now field a growing share of the questions that analysts, scholars, and the public ask about issues of peace and conflict. Large Language Models (LLMs) are known to hallucinate under certain conditions, but do these errors have discernible patterns when they are asked about conflicts, and if so what can that teach us about the changing global conflict information environment? To answer, we first asked a battery of questions about 28 conflicts to five leading answer engines and scored their 5,460 answers against documented evidence. We found that the thinner the retrievable record around a given conflict, the more the engines invent, misattribute, and miscount. Thin records don't just encourage hallucination, but create structural exposure to mis- and disinformation, because they are the easiest records to warp through Generative Engine Optimization (GEO) to bias engine responses. Through an analysis of 1,048 websites that the AI LLMs pulled conflict facts from, we found that GEO source optimization is already happening, and while state-partisan digital capture remains incipient it is rapidly growing. We explain what these findings mean for scholarship with the rise of GEO information warfare, and for policy argue for a return to the deep local monitoring and translation-based research that AI tools cannot replicate, closing with a discussion of future research opportunities and challenges in this fast-moving space.

---


### 27. [The Severance Problem: LLMs are Unaware of the Person Beyond the Prompt](https://arxiv.org/abs/2607.14250)

**<font color=#1a73e8>作者：</font>** Dor Litvak, Liu Leqi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personal AI assistants have attracted significant interest for their potential to enhance everyday life by automating routine tasks, supporting consequential decisions, and assisting with everyday personal matters. Yet despite rapid recent technical advances, these assistants continue to exhibit undesirable behaviors, such as sycophancy, overconfidence, and hallucination. We argue that these failures stem from a fundamental limitation: language models lack an explicit representation of the person beyond the context they are given, which we term as the \textbf{Severance Problem}. Even with rich personal context and strong commonsense reasoning capabilities from the backbone model, current AI assistants fail to represent what remains unknown about the user. We propose a simple solution: incorporating structured ignorance into the language model context via the \textbf{Severance Schema}, which explicitly outlines dimensions along which the model lacks knowledge about the user, including physicality, temporality, consequences, continuity, multiplicity, and interiority. Empirically, across five model families, with the Severance Schema, the assistant consistently reduces sycophancy, harmful advice, and hallucination. Notably, models with the schema ask clarifying questions when information about the user is missing, rather than confidently extrapolating from incomplete user information.

---


### 28. [Automatic Hard Example Synthesis with Multi-Level Agentic Data Curation](https://arxiv.org/abs/2607.14256)

**<font color=#1a73e8>作者：</font>** Genglin Liu, Muye Zhang, Krishnamurthy Viswanathan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) are increasingly deployed for nuanced content safety and moderation tasks, yet they remain vulnerable to adversarial attacks and out-of-distribution edge cases. Traditional active learning and manual annotation fail to scale against the complexity and volume of novel multimodal threats. In this paper, we propose an automated, agentic red-teaming framework that systematically synthesizes difficult examples using an iterative strategy that proposes novel hypotheses as well as mutating on past attempts. Leveraging a multi-agent architecture that consists of a high-reasoning Architect agent, an advanced image generator, and a multi-level verification committee of LLM raters, our system autonomously uncovers boundary-pushing violations and ambiguous policy edge cases without any human intervention. By employing these carefully synthesized adversarial examples as in-context demonstrations via test-time Retrieval, we substantially improve the target model's robustness, reducing the False Negative Rate (FNR) from 41.2% to 24.5% in a public image safety benchmark without relying on any human labeling.

---


### 29. [MonteRET: AI Agent Enhancing Multimodal LLMs with Multi-granularity Knowledge Retrieval for Chest CT Report Generation](https://arxiv.org/abs/2607.14264)

**<font color=#1a73e8>作者：</font>** Yi Lin, Yihao Ding, Elana Benishay 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated chest CT report generation remains challenging because clinically faithful reporting requires both whole-volume understanding and accurate description of localized anatomical findings. Here we developed and retrospectively evaluated MonteRET, a region-aware retrieval-enhanced framework for generating chest CT findings sections. MonteRET integrates global CT features with region-level anatomical representations, retrieves clinically relevant knowledge using predicted medical conditions and region-level vision-language alignment, and refines initial reports through a knowledge-guided report rewriting agent. We trained our model on a public cohort with 24,128 CT scans from RadGenome-ChestCT. We evaluated MonteRET on the public RadGenome-ChestCT test set of 1,564 CT scans and an external cohort of 82 CT scans from NewYork-Presbyterian/Weill Cornell Medical Center. MonteRET improved report quality, semantic similarity, and clinical efficacy compared with a matched baseline and several state-of-the-art methods. Gains were most pronounced for recall, suggesting fewer omitted findings. Human expert evaluation by radiology residents also favored MonteRET.

---


### 30. [AI Agents Do Not Fail Alone:The Context Fails First](https://arxiv.org/abs/2607.14275)

**<font color=#1a73e8>作者：</font>** Fouad Bousetouane  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Context engineering has become central to building reliable AI agents, yet it remains largely unmeasured. Agents do not fail in isolation: their behavior is shaped by the instructions, tools, memory, retrieved knowledge, guardrails, and untrusted inputs accumulated in their context. When this context is weak, agents drift, hallucinate, misuse tools, ignore constraints, become vulnerable to injection, and waste tokens. This paper validates context-engineering quality as an independent leading indicator of agent reliability. We implement the measurement in ProofAgent-Harness, an open-source infrastructure for AI agent evaluation that uses multi-juror, consensus-based scoring. The harness assesses context across seven criteria: role clarity, guardrail coverage, instruction consistency, tool schema quality, grounding sufficiency, injection hardening, and token efficiency. Crucially, the context score is isolated from behavioral metrics and release decisions, enabling a non-circular validation. Through a controlled context-quality study across regulated agent domains, holding frontier LLM agents fixed and varying only their operating context, we show that context-quality criteria consistently predict their corresponding behavioral outcomes. Grounding sufficiency predicts hallucination resistance, guardrail coverage predicts manipulation resistance, instruction consistency predicts instruction following, and tool-schema quality predicts tool use. These findings establish context measurement as a validated preflight signal for agent reliability and position context engineering as an auditable layer of agent evaluation and governance.

---


### 31. [Multi-Head Latent Control: A Unified Interface for LLM Agent Decision Making](https://arxiv.org/abs/2607.14277)

**<font color=#1a73e8>作者：</font>** Amirhosein Ghasemabadi, Ruichen Chen, Bahador Rashidi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as agents, but reliable agentic behavior requires more than next-token prediction. At inference time, it is preferred that an agent can decide whether to proceed with its current reasoning, defer to a stronger model, request additional information, invoke external tools, or abstain under the given setup. Existing approaches address these decisions through prompt-level routing, external orchestration, or task-specific fine-tuning, which primarily rely on input-side signals, and are often costly and difficult to maintain as model backbones evolve. We ask whether such control decisions can be inferred directly from a model's latent generation process. We introduce Multi-Head Latent Control, a lightweight layer that reads hidden-state trajectories from a frozen LLM or VLM to produce deployment-time control signals. A Capability Head predicts whether the current model can solve the instance or should defer to a stronger collaborator, while a Resolution Head predicts appropriate resolution decision Clarification, Tool Use, Abstention, or Direct Answering. Both heads are trained only on latent traces from the same frozen LLM backbone, enabling post hoc adaptation without modifying the model. Across language and vision-language settings, Multi-Head Latent Control consistently improves the quality-cost tradeoff of multi-model systems, enabling early handoff from partial generations and more accurate intervention decisions. In routed execution (small + large model), it reduces large-model usage by up to 90.7 percent on AndroidWorld and 27-53 percent on average across benchmarks, while retaining most of large-model performance. Additionally, the learned control signals improve tool-use decision quality, yielding up to +158 percent relative score gain and 65.5 percent fewer missed-required tool calls.

---


### 32. [Tracing LLM Behavior to the Training Data with Empirical Next-Token Distributions](https://arxiv.org/abs/2607.14306)

**<font color=#1a73e8>作者：</font>** Zachary Izzo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we study the connection between an LLM's output distribution and the data used to train it. Specifically, we study the degree to which an LLM's next-token distribution agrees with the empirical next-token distribution (ENTD) given the context in the training data. The ENTD is an appealing target because it is the unrestricted global minimizer of the next-token cross entropy loss used for pretraining, as well as an easily interpretable function of the pretraining corpus. We find that for a significant fraction of inputs, the LLM's distribution agrees with the ENTD almost perfectly, and the average agreement increases with model scale and training compute. Nevertheless, there is a long tail of input sequences where the LLM and ENTD differ significantly, and we examine several possible sources of this discrepancy across the transformer architecture, training procedure, and finite-sample noise in the ENTD estimate itself. More broadly, we hope our findings will encourage more work on ``data-centric mechanistic interpretability,'' a complement to standard mechanistic interpretability that opens the black box of how model behaviors arise from the data, rather than how they are encoded in the learned weights.

---


### 33. [Traccia: An OpenTelemetry-Based Governance Platform for AI Systems](https://arxiv.org/abs/2607.14309)

**<font color=#1a73e8>作者：</font>** Nutan Kumar Naik, Aditya Kumar Saroj, Vijay Prasad Poudel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid development of Large Language Models (LLMs) and Artificial Intelligent (AI) powered autonomous agents has fundamentally changed the existing forms of software governance. In spite of the rigorous standards of transparency and account ability required according to the international frameworks such as the European Union's AI Act, there is a considerable gap between theory and reality. The present study discusses the inherent drawbacks of currently utilized platforms for LLM evaluation, machine learning workflow, and application performance monitoring in general. It has been shown that current disjointed solutions fail to protect unbound state space agentic architecture from serious threats such as alignment drift, SaaS security concerns, and unauthorized deployment of shadow AI systems. Moreover, a solution is proposed for overcoming the discussed challenges in form of a coherent multi-level AI governance stack Traccia built on the top of OpenTelemetry infrastructure platform. Traccia resolves the last mile for AI Alignment by adding the telemetry data, passive semantic guardrail assessment, and execution lineage into a hashed trace ledger. Traccia automatically creates compliance evidence packages by appending tamper-resistant fingerprints and SHA-256 content hash, that map to regulatory requirements (Articles 12, 14, 19, 26(6), and 50 of the EU AI Act) without invading any data privacy. By performing this evaluation in a methodical manner, a solid machine-readable base has been created for enterprise-wide management of autonomous AI systems.

---


### 34. [NeuroGRIP: Retrieval-Augmented Graph Refinement for Knowledge-Grounded EEG Seizure Diagnosis](https://arxiv.org/abs/2607.14314)

**<font color=#1a73e8>作者：</font>** Lincan Li, Zheng Chen, Yushun Dong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Seizure diagnosis from EEG signals is a critical yet persistently challenging task, due to the complicated neural dynamics and the spurious connections in inter-channel modeling. While spatial-temporal graph neural networks (STGNNs) have advanced EEG brain network representation learning, the resulting graph structures suffer from low clinical plausibility and limited interpretability due to their purely data-driven nature. To this end, we introduce NeuroGRIP, a retrieval-augmented graph refinement framework that incorporates external medical knowledge to calibrate noisy EEG graphs. We first construct a large-scale, domain-specific knowledge base derived from authoritative clinical guidelines. Leveraging large language models, we extract structured biomedical entities and relations to form a textual knowledge graph (KG), which serves as external knowledge source of clinical priors. Our framework performs alignment-aware query construction by projecting STGNN-generated EEG node embeddings into the semantic space of KG. Semantic queries are then executed via FAISS-based similarity search over knowledge triplets to retrieve relation evidence. Each predicted edge is assigned a confidence score based on retrieved similarity, relation type, and source reliability, enabling us to prune medically implausible edges from the originally predicted graph. Extensive experiments on TUSZ and CHB-MIT demonstrate that NeuroGRIP not only improves seizure detection accuracy but also enhances interpretability by grounding each prediction in clinically validated knowledge. This work provides the first unified framework that tightly couples brain dynamics with external medical expertise via retrieval-augmented reasoning, paving the way for knowledge-enhanced, explainable clinical diagnosis. The code is available at: this https URL.

---


### 35. [SD-MAR: Multi-image Analytical Reasoning via Synthetic Data and Reinforcement Learning](https://arxiv.org/abs/2607.14333)

**<font color=#1a73e8>作者：</font>** Shiyu Yuan, Sourav Sanjukta Bhabesh, Zhe Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) demonstrate strong perceptual abilities but remain limited in tasks requiring analytical reasoning across multiple visual states, such as multi-image comparison, change detection, and multi-step visual inference. These capabilities are critical for real-world multimodal applications where reasoning must be grounded in systematic differences between visual contexts. However, existing benchmarks rarely require both explicit visual comparison and analytical reasoning, leaving this capability underexplored. To address this gap, we introduce SD-MAR (Synthetic Data for Multi-image Analytical Reasoning), a framework for training and evaluating VLMs on multi-image analytical reasoning. SD-MAR constructs paired visual scenarios through controlled perturbations and generates reasoning tasks spanning semantic change attribution and quantitative comparison. We further train VLMs using GRPO-lite with Backward Discounted Allocation (BDA), a reinforcement learning approach that removes KL regularization to encourage stronger policy optimization while allocating greater credit to the later reasoning steps where analytical conclusions are formed. Experiments on Qwen2.5-VL-7B and InternVL3-8B show that GRPO-lite fine-tuning on SD-MAR improves in-domain accuracy by up to 36.95%, with Qwen2.5-VL-7B outperforming GPT-4.1 on the SD-MAR benchmark. Importantly, out-of-domain generalization is preserved or improved: performance remains within 1% on MME, MMMU-Pro, and MathVista, while improving by up to 4% on MMBench. LLM-as-judge evaluation further demonstrates consistent improvements in logical coherence and explanation quality across both models.

---


### 36. [MixCompress: Mixture of Experts for Variable Rate Learned Image Compression](https://arxiv.org/abs/2607.14334)

**<font color=#1a73e8>作者：</font>** Calvin-Khang Ta, Praneet Singh, Tong Shao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learned image compression (LIC) is bottlenecked by the need to store independent models for each rate-distortion operating point. Existing variable bit-rate (VBR) methods aim to reduce this overhead via dense parameter modulation, but forcing a shared backbone to approximate divergent mappings causes severe feature entanglement. Specifically, low-rate smoothing gradients inherently conflict with the preservation of high-frequency textural details, leading to sub-optimal performance. To resolve this, we propose MixCompress, a unified VBR framework based on sparse structural specialization. While sparsely gated Mixture-of-Experts (MoE) routing successfully mitigates gradient conflict, it operates on a fixed computational budget. To address the increased representational demands of higher bit-rates we introduce a Mixture-of-Depths (MoD) extension to dynamically scale model capacity. Combined with Conditional Auxiliary Transforms (CAT) for dynamic sub-band energy modulation, our hierarchical framework effectively dynamically scales capacity. Extensive evaluations demonstrate that MixCompress not only matches individually optimized single-rate baselines but can even surpass them, establishing a new Pareto frontier for computationally efficient image coding.

---


### 37. [Value Leakage: An LLM's Answers Are Silently Shaped by Its Own Values](https://arxiv.org/abs/2607.14345)

**<font color=#1a73e8>作者：</font>** Jan Betley, Johannes Treutlein, Jan Dubiński 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> People use language models for practical questions whose answers are difficult to verify. We show that models exhibit covert value leakage: the information they provide is influenced by their own values, without this influence being disclosed to the user.
In one of our evaluations, the user is considering investing in an AI company and wants to know how likely the AI bubble is to pop. Claude Opus 4.8 gives a lower probability when the company under consideration is Anthropic rather than OpenAI. Yet Claude mostly fails to disclose this influence to the user.
Covert value leakage is a form of misalignment because it goes against the user's preferences and is likely to mislead them. To investigate this phenomenon, we introduce a suite of evaluations to quantify value leakage and whether models disclose it. We find that models are influenced by different types of values, including preferences for morally good outcomes, for the company that developed them, and for some human leisure activities over others.
We often observe large differences among frontier models on the same evaluation. For example, on a Fermi-estimation task, Claude models falsely claim to give unbiased answers in their chain-of-thought, while Qwen models explain how their values bias their answers. Value leakage is a failure mode distinct from sycophancy and reward hacking, and current alignment training and evaluations do not adequately address it.

---


### 38. [Supervised Fine-Tuning vs. In-Context Learning: An Equilibrium Analysis of LLM Personalization under Congestion](https://arxiv.org/abs/2607.14371)

**<font color=#1a73e8>作者：</font>** Fengzhuo Zhang, Zhuoran Yang, Dirk Bergemann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have revolutionized AI services, but a critical tension emerges: while personalization improves model performance, it consumes scarce computational resources that users must share. When should a user invest in expensive Supervised Fine-Tuning (SFT) versus lightweight In-Context Learning (ICL)? How does congestion from other users' personalization choices reshape these incentives? And what strategies should platforms adopt when offering multiple personalization algorithms?
We develop a tractable framework for LLM serving that captures the statistical-economic trade-offs users face. Our analysis yields several surprising insights. First, we show that ICL and SFT dominate in different regimes, determined by an interplay between pretraining coverage and data signal-to-noise ratios, but congestion can flip these rankings. Second, equilibrium resource consumption exhibits pronounced non-monotonicity: improving pretraining precision reduces the congestion, while broader pretraining coverage and harder tasks sometimes increase it. Third, we prove that offering both personalization methods never hurts the platform's maximal profits, despite potentially increasing computational load.
Experiments with GPT-2 on linear regression tasks validate our theoretical predictions about algorithm performance. Complementing these results, our review of documentation from 21 major AI platforms shows that the share offering both SFT and ICL increased from 9.5% in 2021 to 71.4% in 2025, consistent with our platform-design implications.

---


### 39. [MamaBench: Benchmarking LLM Robustness in Maternal and Child Health Diagnosis through Counterfactual Clinical Perturbation](https://arxiv.org/abs/2607.14385)

**<font color=#1a73e8>作者：</font>** Thanni Adewuyi, Anuoluwa Sotome, Samuel Okoko 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models achieve strong scores on medical benchmarks, yet these benchmarks evaluate each question in isolation, providing no measure of whether a system can distinguish clinically similar presentations requiring different interventions. We introduce MamaBench, the first counterfactual benchmark for maternal and paediatric AI: 434 expert-authored clinical narratives in 217 pairs across 371 pathologies, evaluated via the Bias Trap Rate (BTR), the conditional probability that a model fails the counterfactual given success on the base case. We propose Evidence-Anchored RAG (EA-RAG), a three-stage retrieval method that replaces aggregate similarity with an evidence coverage objective through clinical parameter extraction, coverage auditing, and contrastive sub-queries. Across eight configurations of four frontier LLMs, base accuracy overstates robust accuracy by 16-28 percentage points in every model. EA-RAG achieves 20.3% BTR and 65.0% robust accuracy on Claude Sonnet 4.6, a 5.5 percentage point BTR reduction without degrading base accuracy. The residual 20% BTR confirms that counterfactual robustness in clinical AI remains an open challenge. Keywords: counterfactual evaluation, clinical AI, maternal healthcare, retrieval-augmented generation, diagnostic robustness

---


### 40. [Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving](https://arxiv.org/abs/2607.14387)

**<font color=#1a73e8>作者：</font>** Yuan Gao, Wenting Miao, Mattia Piccinini 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Validating autonomous driving systems requires diverse, regulation-compliant test scenarios. In simulation-based testing, scenarios are defined as executable scripts. Yet automatically generating such scripts from regulatory descriptions remains an open challenge, and existing approaches face fundamental trade-offs. Retrieval-assemble methods achieve reasonable compilation rates but lack scalability, whereas retrieval-based full-script generation suffers from low compilation success rates. We present Chat2Scenic, the first iterative retrieval-augmented framework to generate scenario scripts in Domain Specific Language (DSL). Specifically, Chat2Scenic provides a chatbot interface that supports interactive scenario refinement and integrates Retrieval-augmented Generation (RAG) to ground scenario generation in regulatory knowledge and DSL syntax. Furthermore, we propose an open benchmark for scenario generation comprising 123 scenarios from various regulations, including NHTSA and United Nations Vehicle Regulations, as well as other sources. Extensive evaluation with State-of-the-Art (SOTA) Large Language Models (LLMs) demonstrates that Chat2Scenic achieves 76.42% Compilation Success Rate (CSR) and 58.17% Framework Accuracy (FA), outperforming existing methods (Retrieval Assemble with 30.08% CSR, 11.03% FA and Retrieval full script generation with 16.26% CSR, 10.86% FA). To facilitate future research, we release our code as open source at this https URL.

---


### 41. [LATTICE: Graph Self-Supervised Learning for Multimodal Spatial Omics Integration](https://arxiv.org/abs/2607.14410)

**<font color=#1a73e8>作者：</font>** Jagan Mohan Reddy Dwarampudi, Veena Kochat, Suresh Satpati 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatially resolved omics studies increasingly combine transcriptomic and epigenomic assays, yet downstream analysis is often still performed using single-modality pipelines. We present LATTICE (Latent Alignment of Tissue-level and Transcriptomic Information for Cross-modal Embedding), a graph-based self-supervised framework that learns spot-level representations from harmonized multimodal features. LATTICE integrates five aligned modality blocks per Visium spot: Visium RNA, scMultiome RNA, scMultiome ATAC, spatial ATAC, and spatial CUT\&Tag. These modalities capture spatial transcriptomic measurements, single-cell inferred regulatory activity, and in situ chromatin and histone states within a unified lattice representation. LATTICE constructs a spatial neighborhood graph and trains a TransformerConv encoder using masked reconstruction, cross-modal alignment, and spatial smoothness objectives. On a private 11-sample melanoma cohort from an anonymized clinical collaborator comprising 54{,}912 total spots, LATTICE demonstrated stable optimization behavior, reproducible embeddings across analysis seeds, and complete multimodal integration across all samples. Adding scMultiome RNA to Visium RNA alone substantially improved concordance with Space Ranger clusters across 11 runs (adjusted Rand index [ARI] +0.157, normalized mutual information [NMI] +0.143, and spatial contiguity +0.174). Additional modalities further improved spatial contiguity and multimodal utility score (MUS), although they sometimes reduced agreement with RNA-derived reference labels, likely because the learned embeddings captured chromatin and regulatory structure beyond transcriptomic similarity alone. These results position LATTICE as a practical and empirically grounded framework for multimodal spatial omics integration, while also highlighting the need for stronger supervision and broader external benchmarking.

---


### 42. [Emergent Region-Level Facial Correspondence in Frozen Vision Foundation Models](https://arxiv.org/abs/2607.14423)

**<font color=#1a73e8>作者：</font>** Izaldein Al-Zyoud, Abdulmotaleb El Saddik  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frozen self-supervised vision models can align parts of generic objects, but it remains unclear whether this correspondence extends to human faces, where global layout is shared while identity-specific appearance varies sharply. We test whether frozen DINOv3 features define a region-level facial coordinate system: a feature space in which eyes, brows, nose, mouth, skin, and hair remain distinguishable across people and across time without face-specific training. Using DINOv3 ViT-L/16 patch embeddings and FaRL only as a face-part labeling interface, we evaluate cross-identity nearest-neighbor matching and temporal label propagation on 200 CelebDF-v2 real videos. DINOv3 achieves 83.0% region-level semantic accuracy under unconstrained cross-identity matching, compared with a 23.0% area-weighted random baseline, and 95.5% temporal tracking accuracy without a learned temporal module. A no-FaRL control collapses to 0.9%, showing that FaRL supplies semantic initialization while DINOv3 supplies dense spatial correspondence. The strongest correspondence appears at an intermediate layer: block 18 gives a 4.93x same-region versus cross-region discrimination ratio, compared with 1.48x at the final block. Against CLIP ViT-L/14, DINOv3 shows only a small aggregate advantage but a +16.8 pp gain on anatomical regions, indicating that image-level contrastive supervision captures coarse facial layout but not fine-grained anatomical identity. These results establish frozen DINOv3 as a strong zero-shot representation for region-level facial correspondence and identify intermediate self-supervised features as the most useful layer for dense face analysis.

---


### 43. [LLM Evaluators are Biased across Languages](https://arxiv.org/abs/2607.14480)

**<font color=#1a73e8>作者：</font>** Ej Zhou, Lucas Resck, Zheng Hui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM evaluators (trained reward models and prompted LLM-as-a-Judge) are routinely validated via pairwise accuracy. In a multilingual setting, this operates under the premise that high pairwise accuracy implies reliable, language-neutral scoring. We show that this assumption does not hold. We conduct experiments with semantically identical instruction-response pairs across 23 languages, and find that multilingual evaluators assign significantly different scores to different evaluation languages. The bias is statistically significant and consistent across eight open-weight evaluators of different architectures and training paradigms, persists in frontier judges, and is strongly correlated with language resource level: lower-resource languages are scored more generously. Meanwhile, these biases are invisible to pairwise accuracy: evaluators achieve above 90% pairwise accuracy, yet have up to 43% difference in acceptance rate across languages under a global decision threshold, meaning, for instance, that harmful content in lower-resource languages is more likely to pass safety filters. Per-language thresholds would require language identification, which can be defeated by code-switched prompts. We then investigate why lower-resource languages receive higher rather than lower scores, and we find that model uncertainty is linked with the effect: models tend to give higher scores when less confident, both under negative log-likelihood and under token-free uncertainty measures; however, language identity remains a significant predictor after controlling for uncertainty, and the bias cannot be explained away by content difficulty alone, but is a structural, language-level misalignment.

---


### 44. [SAGA: Schema-Aware Grounding for Agentic Text-to-SPARQL Generation](https://arxiv.org/abs/2607.14494)

**<font color=#1a73e8>作者：</font>** Yiming Zhang, Koji Tsuda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complex knowledge base question answering (KBQA) is commonly approached through either information retrieval over a question-specific subgraph or semantic parsing into an executable logical form. We study the latter paradigm. Recent large language model agents make semantic parsing interactive: they alternate between reasoning, querying the knowledge base, and extending a partial SPARQL query. This interleaving reduces reliance on one-shot generation, but makes the quality of \emph{KB grounding} depend on what the interaction tools expose. Existing agents retrieve or prune candidate properties mainly through lexical relevance and instance-level observations, without systematically conditioning on entity types, property domains and ranges, or the expected answer type. We call this failure mode \emph{type-blind grounding}. It enlarges the grounding search space and often produces plausible-looking but semantically incompatible triple patterns that execute to empty results. We propose SAGA (\underline{S}chema-\underline{A}ware \underline{G}rounding for \underline{A}gentic Text-to-SPARQL Generation), a training-free framework that turns property exploration into a schema-constrained grounding operation. SAGA maintains a persistent bidirectional type state, filters known-incompatible property candidates at construction time, presents the remaining graph patterns in a compact schema-annotated format, and handles missing schema information permissively through empirical and trace-local evidence. Across nine benchmark settings over Wikidata and Freebase, SAGA achieves the highest F1 on all nine settings and the highest exact-match accuracy on eight, while reducing empty-result queries across all reported Wikidata settings.

---


### 45. [Reinforcing Egocentric Spatial Perception in Multimodal Large Language Models via Ego Scene Augmentation](https://arxiv.org/abs/2607.14497)

**<font color=#1a73e8>作者：</font>** Chi Kit Wong, Ye Pan, Yuanhuiyi Lyu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric Visual Question Answering (VQA) has attracted widespread attention as an important task for enabling Multimodal Large Language Models (MLLMs) to interact with the real world. However, existing MLLMs struggle to perform effective spatial reasoning in complex egocentric scenes due to their limited spatial perception capabilities. To this end, we introduce Ego Scene Augmentation (ESA), an egocentric spatial perception framework, which actively enhances the spatial perception capabilities from the egocentric perspective, powered by the proposed Ego-element Graph. Our core insight is leveraging the Ego-element Graph as an intermediary representation to augment the egocentric spatial perception of MLLMs via visual foundational models. Specifically, we 1) construct the Ego-element Graph, which encapsulates and integrates egocentric spatial features enabled by visual foundational models; 2) enhance the spatial perception capabilities of MLLMs via the Ego-element Graph for ego-perspective scenes. Our proposed ESA framework presents significant performance improvement on the EgoTextVQA benchmark. We achieve an 8.14% gain on the indoor setting and an 8.72% gain on the outdoor setting. Furthermore, our ESA shows the most impressive performance improvement in the shopping subset of the indoor setting. The project code is publicly available.

---


### 46. [Contextualized Evaluation of Vision Language Models through Dynamic, Multi-turn Interactions](https://arxiv.org/abs/2607.14499)

**<font color=#1a73e8>作者：</font>** Yijiang Li, Huiqi Zou, Bingyang Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-modal Large Language Models (MLLMs) have made substantial advances on benchmarks, yet their real-world effectiveness remains uncertain. This gap stems from the fundamental misalignment between benchmarks in controlled, static settings and the dynamic, interactive, and contextualized nature of real-world applications. To bridge this gap, we propose CEDI (Contextualized Evaluations of MLLMs through Dynamic, multi-round Interactions), a framework that recasts evaluation as a three-party interaction between an evaluatee model, an automated examiner, and a grader. The examiner conducts multi-turn, semi-structured conversation guided by a graph-based representation of the task. By navigating state-space transitions, CEDI deploys diverse strategies, from clarification requests to adversarial probes, to elicit performance evidence. We apply CEDI to visual hallucinations. Empirical results across multiple models, diverse settings, datasets, and domains show that contextualized, interactive evaluations reveal not only significantly more hallucinations than conventional static evaluation but also ones that more closely resemble those arising in practical use cases. We further show that hallucinations often accumulate over long contexts, through self-reinforcing dialogue history, and models are particularly vulnerable to questions requiring premise rejection or refusal. Together, these findings highlight CEDI as a step toward realistic, systematic, and ecologically valid assessments of MLLMs' capabilities. Code is available at this http URL.

---


### 47. [Non-vacuous Generalization Bounds for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2607.14506)

**<font color=#1a73e8>作者：</font>** Yuxuan Zhu, Rohan Alur, Daniel Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While reinforcement learning with verifiable rewards (RLVR) is widely used to improve the reasoning capabilities of large language models (LLMs), the generalizability of the resulting models remains poorly understood. In this work, we establish the first non-vacuous generalization bounds for parameter-efficient RLVR fine-tuning at the billion-parameter scale. Our approach adapts PAC-Bayes compression bounds to this setting, and addresses the inherent stochasticity of token generation by applying the Gumbel-max reparameterization trick. To operationalize these bounds, we propose the Progressive RLVR framework, which integrates RLVR with on-policy distillation, TinyLoRA, and model quantization. Progressive RLVR empirically retains 84-97% performance of standard LoRA fine-tuning while producing models that are 14,796x more compressible. We show that this framework yields non-vacuous generalization bounds in four domains: mathematical problem-solving, programming, general-knowledge reasoning, and Text-to-SQL. Our bounds exceed the accuracy of the base model by 9-51% and lie within 6-11% of the accuracy of the fine-tuned models.

---


### 48. [VLT: A Vision-Language-Time Series Multimodal Foundation Model for Industrial Intelligence](https://arxiv.org/abs/2607.14510)

**<font color=#1a73e8>作者：</font>** Haiteng Wang, Jingheng Yan, Xiaokang Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial time series serve as the foundation for Prognostics and Health Management (PHM) to ensure the reliability and safety of industrial equipment such as aero-engines. However, existing approaches are typically limited to single-modality modeling, which restricts their generalization in complex scenarios. Although recent advances in large language models (LLMs) provide new opportunities for multimodal learning, bridging continuous time-series signals and discrete textual semantics remains an open challenge. To this end, we propose VLT, a multimodal foundation model that jointly models time-series, frequency-spectrum visual representations, and textual knowledge. A key insight is to utilize the frequency spectrum as a visual bridge to connect continuous temporal signals with discrete semantics. Specifically, a Time-aware Mixture-of-Experts (Time-MoE) is designed to capture heterogeneous temporal dynamics, while a Frequency-Text Augmented Learner enables joint modeling of spectral and semantic features within a shared representation space. Furthermore, a time-centric gradient alignment mechanism is introduced to mitigate cross-modal optimization conflicts via gradient normalization and reliability-aware dynamic reweighting. Extensive experiments on multiple industrial datasets demonstrate that VLT outperforms state-of-the-art methods, achieving superior robustness and generalization under few-shot, noisy, and incomplete-modality settings.

---


### 49. [RetroAgent: Harnessing LLMs to Search Over Structured Memory for Agentic Retrosynthesis Planning](https://arxiv.org/abs/2607.14512)

**<font color=#1a73e8>作者：</font>** Yanqiao Zhu, Jingru Gan, Xiaoqi Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-step retrosynthesis planning seeks to decompose a target molecule into commercially available building blocks through a sequence of feasible reactions. The vast combinatorial search space makes this task challenging even for expert chemists. Traditional methods combine tree search with offline-trained value networks that score candidates in isolation, without reasoning about complete multi-step routes. Recent work leverages Large Language Models (LLMs) for this task, but relies on simple interfaces that limit exploration of the full search space. We introduce RetroAgent, an LLM agent that bridges symbolic search and neural reasoning through a harness with structured memory. Through memory and chemistry tools, the agent observes the full search state, including explored routes, available alternatives, and properties of intermediates, enabling informed decisions grounded in both global progress and domain knowledge. Experiments on in-distribution and out-of-distribution benchmarks demonstrate that RetroAgent delivers strong performance and generalization.

---


### 50. [A Continuous-Time Reinforcement Learning Framework for Fine-Tuning Discrete Diffusion Models](https://arxiv.org/abs/2607.14522)

**<font color=#1a73e8>作者：</font>** Zikun Zhang, Jiayuan Sheng, David D. Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We formulate reinforcement learning (RL) in continuous time with discrete state spaces and possibly arbitrary action spaces via a stochastic control approach, where the state dynamics are modeled as a controlled continuous-time Markov chain (CTMC). We consider policy optimization problems and derive the corresponding policy gradient methods, leading to continuous-time variants of proximal policy optimization (PPO) and group relative policy optimization (GRPO). As a primary application, we develop a complete continuous-time RL framework for fine-tuning score-based discrete diffusion models. The proposed framework enables reward-driven optimization without requiring differentiability on the reward signals. In contrast to the existing GRPO-based approaches that only rely on terminal rewards, our formulation allows intermediate reward or advantage signals to be incorporated throughout the denoising trajectory. Importantly, when specialized to masked diffusion models (MDMs), our framework encompasses a rich class of policy parameterizations over the vocabulary simplex with analytically tractable probability ratios, providing a unified perspective on exploration and policy optimization in MDMs. For masked diffusion large language models (dLLMs), we further propose trajectory subsampling techniques to efficiently estimate computationally prohibitive trajectory likelihoods, reducing the computational cost of computing per-position probability ratios. We showcase the effectiveness of our methods on both low-dimensional entropy-regularized optimization problems and RL post-training of dLLMs on mathematical reasoning and coding tasks.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-119](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
